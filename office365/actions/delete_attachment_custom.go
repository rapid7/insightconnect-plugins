package actions

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	// jh stuff
)

// Validate is a stub because input validation happens in the implementation.
func (i *DeleteAttachmentInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *DeleteAttachmentOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run the delete_attachment action.
func (a *DeleteAttachmentAction) Run(conn *connection.Connection, input *DeleteAttachmentInput, log plog.Logger) (*DeleteAttachmentOutput, error) {
	output := &DeleteAttachmentOutput{}

	attachmentID := input.AttachmentID
	messageID := input.MessageID

	if _, err := conn.CustomParams.API.DeleteAttachment(input.UserIDPrincipal, attachmentID, messageID); err != nil {
		log.Info("delete_attachment action failed")
		return nil, err
	}

	log.Info("delete_attachment action succeeded")
	return output, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (a *DeleteAttachmentAction) Test(conn *connection.Connection, input *DeleteAttachmentInput, log plog.Logger) (*DeleteAttachmentOutput, error) {
	output := &DeleteAttachmentOutput{}
	return output, nil
}
