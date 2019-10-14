package actions

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	impl "github.com/rapid7/komand-plugins/office365/implementation" // jh stuff
)

// Validate is a stub because input validation happens in the implementation.
func (i *CopyFolderInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *CopyFolderOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run the copy_folder action.
func (a *CopyFolderAction) Run(conn *connection.Connection, input *CopyFolderInput, log plog.Logger) (*CopyFolderOutput, error) {
	output := &CopyFolderOutput{}

	destinationFolderID := input.WellKnownParentID
	if destinationFolderID == impl.OtherFolderKey {
		destinationFolderID = input.OtherParentID
	}

	newFolderID, err := conn.CustomParams.API.CopyFolder(input.UserIDPrincipal, input.FolderID, destinationFolderID)
	if err != nil {
		log.Info("copy_folder action failed")
		return nil, err
	}

	log.Info("copy_folder action succeeded")
	output.NewFolderID = newFolderID
	return output, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (a *CopyFolderAction) Test(conn *connection.Connection, input *CopyFolderInput, log plog.Logger) (*CopyFolderOutput, error) {
	output := &CopyFolderOutput{}
	return output, nil
}
