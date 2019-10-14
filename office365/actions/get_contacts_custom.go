package actions

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	impl "github.com/rapid7/komand-plugins/office365/implementation" // jh stuff
)

// Validate is a stub because input validation happens in the implementation.
func (i *GetContactsInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *GetContactsOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run the get_contacts action.
func (a *GetContactsAction) Run(conn *connection.Connection, input *GetContactsInput, log plog.Logger) (*GetContactsOutput, error) {
	output := &GetContactsOutput{}
	chunk := impl.DefaultChunkForPagination
	continuationToken := input.PaginationToken

	contacts, newContinuationToken, err := conn.CustomParams.API.GetContacts(
		input.UserIDPrincipal,
		chunk,
		continuationToken,
	)
	if err != nil {
		log.Info("get_contacts action failed")
		return nil, err
	}

	log.Info("get_contacts action succeeded")
	output.Contacts = contacts
	output.PaginationToken = newContinuationToken

	return output, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (a *GetContactsAction) Test(conn *connection.Connection, input *GetContactsInput, log plog.Logger) (*GetContactsOutput, error) {
	output := &GetContactsOutput{}
	return output, nil
}
