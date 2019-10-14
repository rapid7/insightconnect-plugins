package actions

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	impl "github.com/rapid7/komand-plugins/office365/implementation" // jh stuff
)

// Validate is a stub because input validation happens in the implementation.
func (i *GetAttachmentsInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *GetAttachmentsOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run the get_attachments action.
func (a *GetAttachmentsAction) Run(conn *connection.Connection, input *GetAttachmentsInput, log plog.Logger) (*GetAttachmentsOutput, error) {
	output := &GetAttachmentsOutput{}

	messageID := input.MessageID
	chunk := impl.DefaultChunkForPagination
	continuationToken := input.PaginationToken

	attachments, newContinuationToken, err := conn.CustomParams.API.GetAttachments(
		input.UserIDPrincipal,
		messageID,
		chunk,
		continuationToken,
	)

	if err != nil {
		log.Info("get_attachments action failed")
		return nil, err
	}

	log.Info("get_attachments action succeeded")
	output.Attachments = attachments
	output.PaginationToken = newContinuationToken
	return output, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (a *GetAttachmentsAction) Test(conn *connection.Connection, input *GetAttachmentsInput, log plog.Logger) (*GetAttachmentsOutput, error) {
	output := &GetAttachmentsOutput{}
	return output, nil
}
