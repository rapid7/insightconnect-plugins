package actions

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	// jh stuff
)

// Validate is a stub because input validation happens in the implementation.
func (i *ReplyToMessageInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *ReplyToMessageOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run the reply_to_message action.
func (a *ReplyToMessageAction) Run(conn *connection.Connection, input *ReplyToMessageInput, log plog.Logger) (*ReplyToMessageOutput, error) {
	output := &ReplyToMessageOutput{}

	messageID := input.MessageID
	body := input.Comment

	if _, err := conn.CustomParams.API.ReplyToMessage(input.UserIDPrincipal, messageID, body); err != nil {
		log.Info("reply_to__message action failed")
		return nil, err
	}

	log.Info("reply_to__message action succeeded")
	return output, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (a *ReplyToMessageAction) Test(conn *connection.Connection, input *ReplyToMessageInput, log plog.Logger) (*ReplyToMessageOutput, error) {
	output := &ReplyToMessageOutput{}
	return output, nil
}
