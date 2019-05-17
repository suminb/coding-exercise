package main

import (
	"bufio"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"net/http"
	"net/http/cookiejar"
	"net/url"
	"os"
	"strings"

	"github.com/PuerkitoBio/goquery"
	"golang.org/x/net/publicsuffix"
	"golang.org/x/text/encoding"
)

func MakeSessionedClient() (*http.Client, error) {
	jar, err := cookiejar.New(&cookiejar.Options{PublicSuffixList: publicsuffix.List})
	if err != nil {
		return nil, err
	}

	client := &http.Client{
		Jar: jar,
	}
	return client, nil
}

// GetReaderFromFile returns a reader object from a file
func GetReaderFromFile(filename string) io.Reader {
	file, _ := os.Open(filename)
	return bufio.NewReader(file)
}

func ForceConvertEncoding(reader *io.Reader, encoding encoding.Encoding) io.Reader {
	decoder := encoding.NewDecoder()
	return decoder.Reader(*reader)
}

func FetchLoginForm(client *http.Client, loginURL string) (*http.Response, error) {
	parsedURL, err := url.Parse(loginURL)
	if err != nil {
		return nil, err
	}

	log.Printf("GET Request: %s\n", parsedURL)
	resp, err := client.Get(parsedURL.String())
	if err != nil {
		return nil, err
	}
	return resp, nil
}

func PostAuthForm(client *http.Client, loginDoc *goquery.Document, loginURL string) (*http.Response, error) {
	// FIXME: This is a temporary workaround
	username := os.Getenv("AWS_USERNAME")
	password := os.Getenv("AWS_PASSWORD")

	parsedURL, _ := url.Parse(loginURL)
	loginForm := loginDoc.Find("form#login")
	actionPath, _ := loginForm.Attr("action")
	actionURL := fmt.Sprintf("%s://%s%s", parsedURL.Scheme, parsedURL.Host, actionPath)

	postData := make(url.Values)
	postData["j_username"] = []string{username}
	postData["j_password"] = []string{password}

	log.Printf("POST Request: %s", actionURL)
	return client.PostForm(actionURL, postData)
}

func PostSamlForm(client *http.Client, authDoc *goquery.Document) (*http.Response, error) {
	samlForm := authDoc.Find("form")
	samlResp := samlForm.Find("input[name=SAMLResponse]")
	samlRespValue, _ := samlResp.Attr("value")
	actionURL, _ := samlForm.Attr("action")

	postData := make(url.Values)
	postData["SAMLResponse"] = []string{samlRespValue}

	log.Printf("POST Request: %s", actionURL)
	return client.PostForm(actionURL, postData)
}

// ProcessSamlForm is a temporary workaround to deal with malformed HTML. We are
// going to need a more robust solution.
func ProcessSamlForm(reader io.Reader) io.Reader {
	samlContentBuf, _ := ioutil.ReadAll(reader)
	samlContent := string(samlContentBuf)
	start := strings.Index(samlContent, "<div id=\"container\">")
	end := strings.Index(samlContent, "</body>")
	return strings.NewReader(samlContent[start:end])
}

func GetRoles(samlDoc *goquery.Document) []string {
	html, _ := samlDoc.Html()
	fmt.Println(html)
	roles := make([]string, 0)
	inputFields := samlDoc.Find("input[name=roleIndex]")
	inputFields.Each(func(i int, s *goquery.Selection) {
		value, _ := s.Attr("value")
		roles = append(roles, value)
	})
	return roles
}

func NewDocumentFromReader(reader io.Reader) (*goquery.Document, error) {
	doc, err := goquery.NewDocumentFromReader(reader)
	if err != nil {
		return nil, err
	}
	return doc, nil
}

func main() {
	loginURL := os.Getenv("AWS_AUTH_URL")
	client, _ := MakeSessionedClient()

	// Redirect to the auth form
	loginFormResp, _ := FetchLoginForm(client, loginURL)
	loginDoc, _ := NewDocumentFromReader(loginFormResp.Body)

	// Authentication
	authResp, _ := PostAuthForm(client, loginDoc, loginURL)
	authDoc, _ := NewDocumentFromReader(authResp.Body)

	// Choose a role
	samlResp, _ := PostSamlForm(client, authDoc)
	samlDoc, _ := NewDocumentFromReader(ProcessSamlForm(samlResp.Body))

	// reader := GetReaderFromFile("saml.html")
	// samlDoc, _ := NewDocumentFromReader(ProcessSamlForm(reader))

	roles := GetRoles(samlDoc)
	fmt.Println(roles)
}
