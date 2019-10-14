package actions

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	// jh stuff
)

// Validate is a stub because input validation happens in the implementation.
func (i *DeleteFolderInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *DeleteFolderOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run the delete_folder action.
func (a *DeleteFolderAction) Run(conn *connection.Connection, input *DeleteFolderInput, log plog.Logger) (*DeleteFolderOutput, error) {
	output := &DeleteFolderOutput{}

	folderID := input.FolderID

	if _, err := conn.CustomParams.API.DeleteFolder(input.UserIDPrincipal, folderID); err != nil {
		log.Info("delete_folder action failed")
		return nil, err
	}

	log.Info("delete_folder action succeeded")
	return output, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (a *DeleteFolderAction) Test(conn *connection.Connection, input *DeleteFolderInput, log plog.Logger) (*DeleteFolderOutput, error) {
	output := &DeleteFolderOutput{}
	return output, nil
}
