package message

import "encoding/json"

// Connection is implemented by any connection
// A connection must be able to connect, and validate the supplied config
// is correct.
type Connection interface {
	Validate() []error
	Connect() error
}

// ConnectionConfig stores connection information.
type ConnectionConfig struct {
	json.RawMessage
	Contents Connection
}

// MarshalJSON implements json marshal interfaces
func (c ConnectionConfig) MarshalJSON() ([]byte, error) {

	if c.RawMessage == nil || len(c.RawMessage) == 0 {
		msg, err := json.Marshal(&c.Contents)
		if err != nil {
			return nil, err
		}
		c.RawMessage = msg
	}

	return c.RawMessage, nil
}
