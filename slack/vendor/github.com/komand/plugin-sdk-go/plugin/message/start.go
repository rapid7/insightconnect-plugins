package message

import (
	"encoding/json"
	"fmt"
)

// base start message
type startMessage struct {
	Connection ConnectionConfig `json:"connection"` // Connection is the global connection for the plugin
	Dispatcher DispatcherConfig `json:"dispatcher"` // Dispatcher is the dispatcher configuration for the plugin
	Input      InputConfig      `json:"input"`      // Input are the parameters passed to trigger start
}

// Unpack will unpack the contents of the connection and input message.
func (m startMessage) Unpack() error {

	if m.Connection.Contents != nil && m.Connection.RawMessage != nil {
		if err := json.Unmarshal(m.Connection.RawMessage, m.Connection.Contents); err != nil {
			return fmt.Errorf("Unable to parse connection config: %s", err)
		}
	}

	if m.Input.Contents != nil && m.Input.RawMessage != nil {
		if err := json.Unmarshal(m.Input.RawMessage, m.Input.Contents); err != nil {
			return fmt.Errorf("Unable to parse input config: %s", err)
		}
	}

	if m.Dispatcher.Contents != nil && m.Dispatcher.RawMessage != nil {
		if err := json.Unmarshal(m.Dispatcher.RawMessage, m.Dispatcher.Contents); err != nil {
			return fmt.Errorf("Unable to parse dispatcher config: %s", err)
		}
	}
	return nil
}
