package dispatcher

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

// HTTP will dispatch via HTTP
type HTTP struct {
	URL    string `json:"url"`
	client *http.Client
}

// NewHTTP will return a new HTTP Dispatcher
func NewHTTP(url string) *HTTP {
	// TODO build a proper http.Client, don't rely on the 0val default like we did in the v1 sdk
	hc := &http.Client{
		Transport: &http.Transport{
			MaxIdleConnsPerHost: 1,
		},
		Timeout: 5 * time.Second,
	}
	return &HTTP{
		URL:    url,
		client: hc,
	}
}

// Send dispatches a trigger event
func (d *HTTP) Send(e interface{}) error {
	messageBytes, err := json.Marshal(e)
	if err != nil {
		return err
	}
	req, err := http.NewRequest("POST", d.URL, bytes.NewBuffer(messageBytes))
	if err != nil {
		return fmt.Errorf("Unable to POST to dispatcher: %s", err.Error())
	}
	req.Header.Set("Content-Type", "application/json")
	resp, err := d.client.Do(req)
	if err != nil {
		return fmt.Errorf("Unable to send event to http dispatcher: %s", err.Error())
	}
	// Since we don't even touch the body, the Close call will fast-track an ioutil.Discard copy
	// this will never return an error we need to care about here afaik. Explicitly _-ing the error by design
	_ = resp.Body.Close()
	if resp.StatusCode != 200 {
		return fmt.Errorf("Response failed, stopping trigger: %s %+v", resp.Status, resp.Header)
	}
	return nil
}
