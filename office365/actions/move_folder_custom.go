package actions

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	impl "github.com/rapid7/komand-plugins/office365/implementation" // jh stuff
)

// Validate is a stub because input validation happens in the implementation.
func (i *MoveFolderInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *MoveFolderOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run the move_folder action.
func (a *MoveFolderAction) Run(conn *connection.Connection, input *MoveFolderInput, log plog.Logger) (*MoveFolderOutput, error) {
	output := &MoveFolderOutput{}

	folderToMoveID := input.FolderID
	destinationFolderID := input.WellKnownParentID
	if destinationFolderID == impl.OtherFolderKey {
		destinationFolderID = input.OtherParentID
	}

	if _, err := conn.CustomParams.API.MoveFolder(input.UserIDPrincipal, folderToMoveID, destinationFolderID); err != nil {
		log.Info("move_folder action failed")
		return nil, err
	}

	log.Info("move_folder action succeeded")
	return output, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (a *MoveFolderAction) Test(conn *connection.Connection, input *MoveFolderInput, log plog.Logger) (*MoveFolderOutput, error) {
	output := &MoveFolderOutput{}
	return output, nil
}
