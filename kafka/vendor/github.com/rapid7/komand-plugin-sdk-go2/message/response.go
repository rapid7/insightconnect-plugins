package message

import "encoding/json"

// Response is the format of the message from an Actions result
type Response struct {
	Meta   json.RawMessage `json:"meta"`
	Status string          `json:"status"` // Status identifies the result status from the Action
	Error  string          `json:"error"`  // Error identifies any error that occured during the Action
	Output interface{}     `json:"output"` // Output contains the output of the Action
	Log    string          `json:"log"`    // Log contains any captured log information
}

// RawResponse is the format of the message from an Actions result, but meant for the consumer
// This leaves output as a json.RawMessage, which is easier to parse into a custom type on the consumer
// side than an interface{} is
type RawResponse struct {
	Meta   json.RawMessage `json:"meta"`
	Status string          `json:"status"` // Status identifies the result status from the Action
	Error  string          `json:"error"`  // Error identifies any error that occured during the Action
	Output json.RawMessage `json:"output"` // Output contains the output of the Action
	Log    string          `json:"log"`    // Log contains any captured log information
}
