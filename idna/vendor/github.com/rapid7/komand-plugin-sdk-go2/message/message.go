package message

import "encoding/json"

// These define the types of messages used in the SDK
const (
	ActionStart  = "action_start"
	TriggerStart = "trigger_start"
)

// V1 is the general purpose komand plugin message envelope, which contains the body and other metadata
type V1 struct {
	Version string      `json:"version"`
	Type    string      `json:"type"`
	Body    interface{} `json:"body"`
}

// BodyV1 is the V1 message body
type BodyV1 struct {
	Meta json.RawMessage `json:"meta"`
	// Of Action and Trigger, only one will be set at a time.
	Action     string          `json:"action"`
	Trigger    string          `json:"trigger"`
	Connection json.RawMessage `json:"connection"` // connection.Data is defined per plugin, so it will be serialized individually
	Dispatcher json.RawMessage `json:"dispatcher"` // Dispatcher is one of a few options, but we need to pull metadata from it to know what, so we use m[s]i{}
	Input      json.RawMessage `json:"input"`      // Inputs are defined per action, so they will be serialized individually
}

// ActionEventMeta is full of information about the workflow and the step being invoked.
// Plugins typically do not use this data, but it's ferried back and forth from engine to engine
// so we know where the plugin response is coming from
type ActionEventMeta struct {
	StepUID            string `json:"step_uid"`
	WorkflowUID        string `json:"workflow_uid,omitempty"`
	WorkflowVersionUID string `json:"workflow_version_uid,omitempty"`
}
