package message

import (
	"encoding/json"
	"fmt"

	"github.com/komand/plugin-sdk-go/plugin/parameter"
)

// Message contains general message information that other messages should embed
type Message struct {
	Header // Message header
	Body   // Message body
}

// StatusType contains the possible step return statuses
type StatusType string

const (
	// OK everything worked
	OK = StatusType("ok")
	// ERROR something failed
	ERROR = StatusType("error")
)

// Validate the msg against the provided msgtype.
func (m *Message) Validate() error {
	if m.Version != Version {
		return fmt.Errorf("Unexpected version, wanted: %s but got %s", Version, m.Version)
	}
	return nil
}

// MarshalJSON marshals a Message object.
func (m *Message) MarshalJSON() ([]byte, error) {

	bodyBytes, err := json.Marshal(m.Body)
	if err != nil {
		return nil, err
	}
	msg := struct {
		Header
		Body json.RawMessage `json:"body"`
	}{
		Header: m.Header,
		Body:   json.RawMessage(bodyBytes),
	}
	return json.Marshal(&msg)
}

// MarshalBody marshals a Message object with the provided body into JSON
func (m *Message) MarshalBody(body interface{}) ([]byte, error) {

	// if body is provided, set it here.
	if body != nil {
		m.Body = Body{
			Contents: body,
		}
	}

	return json.Marshal(m)
}

// Unmarshal unmarshals a Message object
func (m *Message) Unmarshal(p *parameter.ParamSet) error {
	p.Param("type", &m.Type)
	p.Param("version", &m.Version)
	p.Param("body", &m.Body)

	if err := p.Parse(); err != nil {
		return err
	}

	if err := m.Validate(); err != nil {
		return err
	}

	return nil
}

// UnmarshalBody unmarshalls a Body object
func (m *Message) UnmarshalBody(body interface{}) error {
	err := json.Unmarshal(m.Body.RawMessage, body)
	if err != nil {
		return fmt.Errorf("Unable to unmarshal Body: %+v", err)
	}
	return nil
}
