package plugin

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"

	"github.com/komand/plugin-sdk-go/plugin/message"
)

// the default dispatcher for a trigger is HTTP, and for actions is Stdout.
// However, it can toggled here for testing purposes.
var defaultTriggerDispatcher Dispatcher
var defaultActionDispatcher Dispatcher

func triggerDispatcher() Dispatcher {
	if defaultTriggerDispatcher == nil {
		defaultTriggerDispatcher = &HTTPDispatcher{}
	}

	return defaultTriggerDispatcher
}

func actionDispatcher() Dispatcher {
	if defaultActionDispatcher == nil {
		defaultActionDispatcher = &StdoutDispatcher{}
	}

	return defaultActionDispatcher
}

// dispatchable objects supply dispatchers
type dispatchable interface {
	Dispatcher() Dispatcher
}

// Dispatcher aliases message.Dispatcher
type Dispatcher message.Dispatcher

// StdoutDispatcher will dispatch event to stdout
type StdoutDispatcher struct{}

// Send dispatches a trigger event
func (d *StdoutDispatcher) Send(event *message.Message) error {
	messageBytes, err := json.Marshal(event)

	if err != nil {
		return err
	}

	_, err = os.Stdout.Write(messageBytes)
	return err
}

// HTTPDispatcher will dispatch via HTTP
type HTTPDispatcher struct {
	URL    string `json:"url"`
	client http.Client
}

// Send dispatches a trigger event
func (d *HTTPDispatcher) Send(event *message.Message) error {
	messageBytes, err := json.Marshal(event)

	if err != nil {
		return err
	}

	req, err := http.NewRequest("POST", d.URL, bytes.NewBuffer(messageBytes))

	if err != nil {
		err = fmt.Errorf("Unable to POST to dispatcher: %+v", err)
		return err
	}

	req.Header.Set("Content-Type", "application/json")

	resp, err := d.client.Do(req)
	if err != nil {
		err = fmt.Errorf("Unable to send event to http dispatcher: %+v", err)
		return err
	}
	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		return fmt.Errorf("Response failed, stopping trigger: %v %v", resp.Status, resp.Header)
	}

	return nil
}

// FileDispatcher will dispatch event to a file
type FileDispatcher struct {
	fd *os.File
}

// NewFileDispatcher creates a dispatcher that logs events to a file.
func NewFileDispatcher(filename string) (*FileDispatcher, error) {
	f, err := os.OpenFile(filename, os.O_CREATE|os.O_APPEND|os.O_WRONLY, 0600)
	if err != nil {
		return nil, err
	}
	return &FileDispatcher{fd: f}, nil
}

// Send dispatches a trigger event
func (d *FileDispatcher) Send(event *message.Message) error {
	messageBytes, err := json.Marshal(event)

	if err != nil {
		return err
	}

	if _, err = d.fd.Write(messageBytes); err != nil {
		return err
	}

	return nil
}
