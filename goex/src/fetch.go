package src

import (
	"io"
	"net/http"

	"golang.org/x/text/encoding"
)

// This is a collection of functions to fetch remove resources such as web pages and structured data provided by APIs.

// Fetch sends out an HTTP GET request and returns an HTTP response
func Fetch(url string, params map[string]string, headers map[string]string) (*http.Response, error) {

	client := &http.Client{}
	req, err := http.NewRequest("GET", url, nil)

	// TODO: Fill in query strings
	//for k, v := range params {
	//}

	for k, v := range headers {
		req.Header.Set(k, v)
	}

	res, err := client.Do(req)
	return res, err
}

func ForceConvertEncoding(reader io.Reader, encoding encoding.Encoding) io.Reader {
	decoder := encoding.NewDecoder()
	return decoder.Reader(reader)
}
