package qualys

import (
	"bytes"
	"context"
	"encoding/json"
	"encoding/xml"
	"io"
	"io/ioutil"
	"net/http"
	"net/url"
	"reflect"

	"github.com/google/go-querystring/query"
)

const (
	// DrainLimit drains a response body up to 512 bytes
	DrainLimit = 512
)

// A Client manages communication with the Qualys API.
// Design and adaptation of this client comes from Google's Go Github Library
// https://github.com/google/go-github
type Client struct {
	client *http.Client // HTTP client used to communicate with the API.

	// Base URL for API requests. Should always have trailing slash.
	BaseURL *url.URL

	// User agent used when communicating with the Qualys API.
	UserAgent string

	// common allows us to reuse a single service instead of allocating one for each XService on the heap.
	common service

	username string
	password string

	VMScans       *VMScanService
	PCScans       *PCScanService
	SCAPScans     *SCAPScanService
	Reports       *ReportService
	KnowledgeBase *KnowledgeBaseService
}

type service struct {
	client *Client
}

// NewClient returns a new Qualys API client. If a nil httpClient is
// provided, http.DefaultClient will be used.
func NewClient(httpClient *http.Client, baseurl, username, password string) *Client {
	if httpClient == nil {
		httpClient = http.DefaultClient
	}

	u := USPlatform1
	if baseurl != "" {
		u = baseurl
	}
	baseURL, err := url.Parse(u)
	if err != nil {
		baseURL, _ = url.Parse(USPlatform1)
	}

	c := &Client{
		client:    httpClient,
		BaseURL:   baseURL,
		UserAgent: UserAgent,
		username:  username,
		password:  password,
	}
	// Use one instance of client instead of creating one for each service
	c.common.client = c

	// Initialize Services
	c.VMScans = (*VMScanService)(&c.common)
	c.PCScans = (*PCScanService)(&c.common)
	c.SCAPScans = (*SCAPScanService)(&c.common)
	c.Reports = (*ReportService)(&c.common)
	c.KnowledgeBase = (*KnowledgeBaseService)(&c.common)

	return c
}

// RequestOptions ...
type RequestOptions struct {
	Method      string
	URL         string
	ContentType string
	Accept      string
	Body        interface{}
}

// NewRequest creates an API request. A relative URL can be provided in urlStr,
// in which case it is resolved relative to the BaseURL of the Client.
// Relative URLs should always be specified without a preceding slash. If
// specified, the value pointed to by body is JSON/XML encoded and included as the
// request body.
func (c *Client) NewRequest(opt RequestOptions) (*http.Request, error) {
	rel, err := url.Parse(opt.URL)
	if err != nil {
		return nil, err
	}

	u := c.BaseURL.ResolveReference(rel)

	var buf io.ReadWriter
	if opt.Body != nil {
		buf = new(bytes.Buffer)
		if opt.ContentType == "application/xml" {
			if err := xml.NewEncoder(buf).Encode(opt.Body); err != nil {
				return nil, err
			}
		}
		if opt.ContentType == "application/json" {
			if err := json.NewEncoder(buf).Encode(opt.Body); err != nil {
				return nil, err
			}
		}
	}

	req, err := http.NewRequest(opt.Method, u.String(), buf)
	if err != nil {
		return nil, err
	}

	if opt.Body != nil {
		req.Header.Set("Content-Type", opt.ContentType)
	}

	req.Header.Set("Accept", opt.Accept)
	if c.UserAgent != "" {
		req.Header.Set("User-Agent", c.UserAgent)
	}
	// Qualys needs this header
	req.Header.Set("X-Requested-With", c.UserAgent)

	// Qualys uses Basic Auth
	req.SetBasicAuth(c.username, c.password)

	return req, nil
}

// Do sends an API request and returns the API response. The API response is
// JSON/XML decoded and stored in the value pointed to by v, or returned as an
// error if an API error has occurred. If v implements the io.Writer
// interface, the raw response body will be written to v, without attempting to
// first decode it.
//
// The provided ctx must be non-nil. If it is canceled or times out,
// ctx.Err() will be returned.
func (c *Client) Do(ctx context.Context, req *http.Request, v interface{}) (*http.Response, error) {
	req = req.WithContext(ctx)

	resp, err := c.client.Do(req)
	if err != nil {
		// If we got an error, and the context has been canceled,
		// the context's error is probably more useful.
		select {
		case <-ctx.Done():
			return nil, ctx.Err()
		default:
			return nil, err
		}
	}

	defer func() {
		io.CopyN(ioutil.Discard, resp.Body, DrainLimit)
		// Close the body to let the Transport reuse the connection
		resp.Body.Close()
	}()

	if v != nil {
		if w, ok := v.(io.Writer); ok {
			io.Copy(w, resp.Body)
		} else {
			accept := req.Header.Get("Accept")
			if accept == "application/xml" {
				// Try to unmarshal the response body
				// We ignore EOF errors caused if the response body is empty
				if err := xml.NewDecoder(resp.Body).Decode(v); err != io.EOF {
					return nil, err
				}
			}
			if accept == "application/json" {
				if err := json.NewDecoder(resp.Body).Decode(v); err != io.EOF {
					return nil, err
				}
			}
		}
	}

	return resp, nil
}

// addOptions adds the parameters in opt as URL query parameters to s. opt
// must be a struct whose fields may contain "url" tags.
func addOptions(s string, opt interface{}) (string, error) {
	v := reflect.ValueOf(opt)
	if v.Kind() == reflect.Ptr && v.IsNil() {
		return s, nil
	}

	u, err := url.Parse(s)
	if err != nil {
		return s, err
	}

	qs, err := query.Values(opt)
	if err != nil {
		return s, err
	}

	u.RawQuery = qs.Encode()
	return u.String(), nil
}
