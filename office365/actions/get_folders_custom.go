package actions

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	impl "github.com/rapid7/komand-plugins/office365/implementation" // jh stuff
)

// Validate is a stub because input validation happens in the implementation.
func (i *GetFoldersInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *GetFoldersOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run the get_folders_action.
func (a *GetFoldersAction) Run(conn *connection.Connection, input *GetFoldersInput, log plog.Logger) (*GetFoldersOutput, error) {
	output := &GetFoldersOutput{}

	folderID := input.WellKnownParentID
	if folderID == impl.OtherFolderKey {
		folderID = input.OtherParentID
	}
	chunk := impl.DefaultChunkForPagination
	continuationToken := input.PaginationToken

	folders, newContinuationToken, err := conn.CustomParams.API.GetFolders(
		input.UserIDPrincipal,
		folderID,
		continuationToken,
		chunk,
	)
	if err != nil {
		log.Info("get_folders action failed")
		return nil, err
	}

	log.Info("get_folders action succeeded")
	output.Folders = folders
	output.PaginationToken = newContinuationToken
	return output, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (a *GetFoldersAction) Test(conn *connection.Connection, input *GetFoldersInput, log plog.Logger) (*GetFoldersOutput, error) {
	output := &GetFoldersOutput{}
	return output, nil
}
