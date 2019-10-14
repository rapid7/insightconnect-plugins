package message

import "encoding/json"

// Input define inputs for a trigger or action.
// Input fields must supply a validation function.
type Input interface {
	Validate() []error
}

// InputConfig holds the input configuration within the message
type InputConfig struct {
	json.RawMessage
	Contents Input
}

// MarshalJSON implmenents custom json.Marshal logic
func (i *InputConfig) MarshalJSON() ([]byte, error) {
	if i.RawMessage == nil || len(i.RawMessage) == 0 {
		msg, err := json.Marshal(&i.Contents)
		if err != nil {
			return nil, err
		}
		i.RawMessage = msg
	}

	return i.RawMessage, nil
}
