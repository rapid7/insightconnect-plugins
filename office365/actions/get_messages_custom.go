package actions

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	impl "github.com/rapid7/komand-plugins/office365/implementation" // jh stuff
)

// Validate is a stub because input validation happens in the implementation.
func (i *GetMessagesInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *GetMessagesOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run the get_messages action.
func (a *GetMessagesAction) Run(conn *connection.Connection, input *GetMessagesInput, log plog.Logger) (*GetMessagesOutput, error) {
	output := &GetMessagesOutput{}

	folderID := input.WellKnownFolderID
	if folderID == impl.OtherFolderKey {
		folderID = input.OtherFolderID
	}
	chunk := impl.DefaultChunkForPagination
	continuationToken := input.PaginationToken
	orderBy := ""

	messages, newContinuationToken, err := conn.CustomParams.API.GetMessages(
		input.UserIDPrincipal,
		folderID,
		chunk,
		continuationToken,
		orderBy,
		false,
		log,
	)
	if err != nil {
		log.Info("get_messages action failed")
		return nil, err
	}
	log.Info("get_messages action succeeded")
	output.Messages = messages
	output.PaginationToken = newContinuationToken
	return output, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (a *GetMessagesAction) Test(conn *connection.Connection, input *GetMessagesInput, log plog.Logger) (*GetMessagesOutput, error) {
	output := &GetMessagesOutput{}
	return output, nil
}
