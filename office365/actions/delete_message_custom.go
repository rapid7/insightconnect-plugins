package actions

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	// jh stuff
)

// Validate is a stub because input validation happens in the implementation.
func (i *DeleteMessageInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *DeleteMessageOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run the delete_message action.
func (a *DeleteMessageAction) Run(conn *connection.Connection, input *DeleteMessageInput, log plog.Logger) (*DeleteMessageOutput, error) {
	output := &DeleteMessageOutput{}

	messageID := input.MessageID

	if _, err := conn.CustomParams.API.DeleteMessage(input.UserIDPrincipal, messageID); err != nil {
		log.Info("delete_message action failed")
		return nil, err
	}

	log.Info("delete_message action succeeded")
	return output, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (a *DeleteMessageAction) Test(conn *connection.Connection, input *DeleteMessageInput, log plog.Logger) (*DeleteMessageOutput, error) {
	output := &DeleteMessageOutput{}
	return output, nil
}
