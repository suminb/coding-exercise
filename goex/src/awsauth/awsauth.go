package main

import (
	"fmt"
	"log"
	"net/http"
	"net/http/cookiejar"
	"net/url"
	"os"

	"github.com/PuerkitoBio/goquery"
	"golang.org/x/net/publicsuffix"
)

func main() {
	authURL := os.Getenv("AWS_AUTH_URL")
	username := os.Getenv("AWS_USERNAME")
	password := os.Getenv("AWS_PASSWORD")

	parsedURL, err := url.Parse(authURL)
	if err != nil {
		log.Fatal(err)
	}

	jar, err := cookiejar.New(&cookiejar.Options{PublicSuffixList: publicsuffix.List})
	if err != nil {
		log.Fatal(err)
	}

	client := &http.Client{
		Jar: jar,
	}

	log.Printf("GET Request: %s\n", parsedURL)
	resp, err := client.Get(parsedURL.String())
	if err != nil {
		log.Fatal(err)
	}

	// body, err := ioutil.ReadAll(resp.Body)
	// fmt.Printf("Header = %v\n", resp.Body)
	// fmt.Printf("Body = %s\n", body)

	// fmt.Println("After 1st request:")
	// for _, cookie := range jar.Cookies(parsedURL) {
	// 	fmt.Printf("  %s: %s\n", cookie.Name, cookie.Value)
	// }

	doc, err := goquery.NewDocumentFromReader(resp.Body)
	if err != nil {
		log.Fatal(err)
	}

	loginForm := doc.Find("form#login")
	actionPath, _ := loginForm.Attr("action")
	actionURL := fmt.Sprintf("%s://%s%s", parsedURL.Scheme, parsedURL.Host, actionPath)

	log.Printf("POST Request: %s", actionURL)
	postData := make(url.Values)
	postData["j_username"] = []string{username}
	postData["j_password"] = []string{password}
	resp, err = client.PostForm(actionURL, postData)
	if err != nil {
		log.Fatal(err)
	}

	doc, err = goquery.NewDocumentFromReader(resp.Body)
	if err != nil {
		log.Fatal(err)
	}

	samlForm := doc.Find("form")
	samlResp := samlForm.Find("input[name=SAMLResponse]")
	samlRespValue, _ := samlResp.Attr("value")
	actionURL, _ = samlForm.Attr("action")

	log.Printf("POST Request: %s", actionURL)
	postData = make(url.Values)
	postData["SAMLResponse"] = []string{samlRespValue}
	resp, err = client.PostForm(actionURL, postData)
	if err != nil {
		log.Fatal(err)
	}

	doc, err = goquery.NewDocumentFromReader(resp.Body)
	if err != nil {
		log.Fatal(err)
	}

	html, _ := doc.Html()
	fmt.Println(html)
}
