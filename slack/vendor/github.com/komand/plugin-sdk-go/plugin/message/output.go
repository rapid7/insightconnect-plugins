package message

import "encoding/json"

// Output define outputs for a trigger or action.
type Output interface {
	// TODO: Output must support a validation method?
}

// OutputMessage holds the output information for the message.
type OutputMessage struct {
	json.RawMessage
	Contents Output
}

// MarshalJSON implmenents custom json.Marshal logic
func (i *OutputMessage) MarshalJSON() ([]byte, error) {
	if i.RawMessage == nil || len(i.RawMessage) == 0 {
		msg, err := json.Marshal(&i.Contents)
		if err != nil {
			return nil, err
		}
		i.RawMessage = msg
	}

	return i.RawMessage, nil
}
