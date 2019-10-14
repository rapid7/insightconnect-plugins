package actions

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	impl "github.com/rapid7/komand-plugins/office365/implementation" // jh stuff
)

// Validate is a stub because input validation happens in the implementation.
func (i *CreateFolderInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *CreateFolderOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run the create_folder action.
func (a *CreateFolderAction) Run(conn *connection.Connection, input *CreateFolderInput, log plog.Logger) (*CreateFolderOutput, error) {
	output := &CreateFolderOutput{}

	parentFolderID := input.WellKnownParentID
	if parentFolderID == impl.OtherFolderKey {
		parentFolderID = input.OtherParentID
	}
	displayName := input.FolderName

	newFolderID, err := conn.CustomParams.API.CreateFolder(input.UserIDPrincipal, parentFolderID, displayName)
	if err != nil {
		log.Info("create_folder action failed")
		return nil, err
	}

	log.Info("create_folder action succeeded")
	output.FolderID = newFolderID
	return output, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (a *CreateFolderAction) Test(conn *connection.Connection, input *CreateFolderInput, log plog.Logger) (*CreateFolderOutput, error) {
	output := &CreateFolderOutput{}
	return output, nil
}
