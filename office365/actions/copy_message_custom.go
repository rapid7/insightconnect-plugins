package actions

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	impl "github.com/rapid7/komand-plugins/office365/implementation" // jh stuff
)

// Validate is a stub because input validation happens in the implementation.
func (i *CopyMessageInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *CopyMessageOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run the copy_message action.
func (a *CopyMessageAction) Run(conn *connection.Connection, input *CopyMessageInput, log plog.Logger) (*CopyMessageOutput, error) {
	output := &CopyMessageOutput{}

	messageID := input.MessageID
	folderID := input.WellKnownFolderID
	if folderID == impl.OtherFolderKey {
		folderID = input.OtherFolderID
	}
	userID := input.UserIDPrincipal

	newMessageID, err := conn.CustomParams.API.CopyMessage(userID, messageID, folderID)
	if err != nil {
		log.Info("copy_message action failed")
		return nil, err
	}

	log.Info("copy_message action succeeded")
	output.NewMessageID = newMessageID
	return output, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (a *CopyMessageAction) Test(conn *connection.Connection, input *CopyMessageInput, log plog.Logger) (*CopyMessageOutput, error) {
	output := &CopyMessageOutput{}
	return output, nil
}
