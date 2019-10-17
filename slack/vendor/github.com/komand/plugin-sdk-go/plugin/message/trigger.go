package message

import "encoding/json"

// TriggerStart is the format of the message that starts a Trigger
type TriggerStart struct {
	Meta    *json.RawMessage `json:"meta"`
	Trigger string           `json:"trigger"` // Trigger is the name of the trigger
	startMessage
}

// TriggerEvent messages encapsulate any output event emitted by the plugins.
type TriggerEvent struct {
	ID      string           `json:"id"`       // Application level identifier for the TriggerEvent for later tracking via the UI
	GroupID string           `json:"group_id"` // Another application level id, this one is used internally to allow us to re-publish a job and track them under a common ID
	Meta    *json.RawMessage `json:"meta"`
	Output  OutputMessage    `json:"output"`
}
