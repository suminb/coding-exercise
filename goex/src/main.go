package src

import (
	"bufio"
	"fmt"
	"io"
	"log"
	"os"
	"strings"

	"github.com/PuerkitoBio/goquery"
	"golang.org/x/text/encoding/korean"
)

func ExampleScrape() {

	reader := FetchSampleFile("marketindex.html")
	reader = ForceConvertEncoding(reader, korean.EUCKR)

	// Load the HTML document
	doc, err := goquery.NewDocumentFromReader(reader)
	if err != nil {
		log.Fatal(err)
	}

	elements := doc.Find(".tbl_exchange tr")
	elements.Each(func(i int, s *goquery.Selection) {
		label := s.Find("span")
		if label.Text() == "국고채 (3년)" {
			row := label.Parent().Parent().Parent()
			cell := row.Children()

			value := strings.TrimSpace(cell.Eq(1).Text())
			delta := strings.TrimSpace(cell.Eq(2).Text())

			fmt.Printf("value = %s, delta = %s\n", value, delta)
		}
	})
}

func GetReaderWithURL(url string) io.Reader {
	params := make(map[string]string)
	headers := make(map[string]string)
	resp, _ := Fetch("https://finance.naver.com/marketindex/", params, headers)
	defer resp.Body.Close()
	if resp.StatusCode != 200 {
		log.Fatalf("status code error: %d %s", resp.StatusCode, resp.Status)
	}

	return resp.Body
}

func FetchSampleFile(filename string) io.Reader {
	file, _ := os.Open(filename)
	return bufio.NewReader(file)
}

func main() {
	ExampleScrape()
}
