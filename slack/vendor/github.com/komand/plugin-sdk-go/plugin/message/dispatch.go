package message

import "encoding/json"

// Dispatcher defines a dispatcher.
type Dispatcher interface {
	Send(msg *Message) error
}

// DispatcherConfig holds the input configuration within the message
type DispatcherConfig struct {
	json.RawMessage
	Contents Dispatcher
}

// MarshalJSON implmenents custom json.Marshal logic
func (i *DispatcherConfig) MarshalJSON() ([]byte, error) {
	if i.RawMessage == nil || len(i.RawMessage) == 0 {
		msg, err := json.Marshal(&i.Contents)
		if err != nil {
			return nil, err
		}
		i.RawMessage = msg
	}

	return i.RawMessage, nil
}
