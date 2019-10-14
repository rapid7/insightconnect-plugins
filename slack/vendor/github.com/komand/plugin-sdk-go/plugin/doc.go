package plugin

import (
	"encoding/json"

	"github.com/komand/plugin-sdk-go/plugin/message"
)

// GenerateSampleActionStart generates a sample action start message
func GenerateSampleActionStart(action Actionable) (string, error) {
	m := message.ActionStart{}

	if connectable, ok := action.(Connectable); ok {
		connection := connectable.Connection()
		m.Connection.Contents = connection
	}

	if inputable, ok := action.(Inputable); ok {
		if inputable != nil {
			m.Input.Contents = inputable.Input()
		}
	}

	m.Dispatcher.Contents = &StdoutDispatcher{}
	m.Action = action.Name()

	env := message.Message{
		Header: message.Header{
			Version: message.Version,
			Type:    ActionStart,
		},
		Body: message.Body{
			Contents: &m,
		},
	}

	result, err := json.MarshalIndent(&env, " ", "  ")

	if err != nil {
		return "", err
	}

	return string(result), nil
}

// GenerateSampleTriggerStart generates a sample trigger start message
func GenerateSampleTriggerStart(trigger Triggerable) (string, error) {
	m := message.TriggerStart{}

	if connectable, ok := trigger.(Connectable); ok {
		connection := connectable.Connection()
		m.Connection.Contents = connection
	}

	if inputable, ok := trigger.(Inputable); ok {
		if inputable != nil {
			m.Input.Contents = inputable.Input()
		}
	}
	m.Dispatcher.Contents = &HTTPDispatcher{URL: "http://example.com/trigger/id/event"}
	m.Trigger = trigger.Name()

	env := message.Message{
		Header: message.Header{
			Version: message.Version,
			Type:    TriggerStart,
		},
		Body: message.Body{
			Contents: &m,
		},
	}

	result, err := json.MarshalIndent(&env, " ", "  ")

	if err != nil {
		return "", err
	}

	return string(result), nil
}
