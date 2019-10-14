package actions

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	impl "github.com/rapid7/komand-plugins/office365/implementation" // jh stuff
)

// Validate is a stub because input validation happens in the implementation.
func (i *MoveMessageInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *MoveMessageOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run the move_message action.
func (a *MoveMessageAction) Run(conn *connection.Connection, input *MoveMessageInput, log plog.Logger) (*MoveMessageOutput, error) {
	output := &MoveMessageOutput{}

	messageID := input.MessageID
	folderID := input.WellKnownFolderID
	if folderID == impl.OtherFolderKey {
		folderID = input.OtherFolderID
	}

	if _, err := conn.CustomParams.API.MoveMessage(input.UserIDPrincipal, messageID, folderID); err != nil {
		log.Info("move_message action failed")
		return nil, err
	}

	log.Info("move_message action succeeded")
	return output, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (a *MoveMessageAction) Test(conn *connection.Connection, input *MoveMessageInput, log plog.Logger) (*MoveMessageOutput, error) {
	output := &MoveMessageOutput{}
	return output, nil
}
