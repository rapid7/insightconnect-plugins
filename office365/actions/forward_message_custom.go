package actions

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	// jh stuff
)

// Validate is a stub because input validation happens in the implementation.
func (i *ForwardMessageInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *ForwardMessageOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run the forward_message action.
func (a *ForwardMessageAction) Run(conn *connection.Connection, input *ForwardMessageInput, log plog.Logger) (*ForwardMessageOutput, error) {
	output := &ForwardMessageOutput{}

	messageID := input.MessageID
	body := input.Comment
	toRecipients := input.ToRecipients

	if _, err := conn.CustomParams.API.ForwardMessage(input.UserIDPrincipal, messageID, body, toRecipients); err != nil {
		log.Info("forward_message action failed")
		return nil, err
	}

	log.Info("forward_message action succeeded")
	return output, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (a *ForwardMessageAction) Test(conn *connection.Connection, input *ForwardMessageInput, log plog.Logger) (*ForwardMessageOutput, error) {
	output := &ForwardMessageOutput{}
	return output, nil
}
