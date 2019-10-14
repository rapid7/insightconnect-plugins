package actions

import (
	"fmt"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	impl "github.com/rapid7/komand-plugins/office365/implementation" // jh stuff
)

// Validate is a stub because input validation happens in the implementation.
func (i *MostRecentlySentInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *MostRecentlySentOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run the most_recently_sent action.
func (a *MostRecentlySentAction) Run(conn *connection.Connection, input *MostRecentlySentInput, log plog.Logger) (*MostRecentlySentOutput, error) {
	output := &MostRecentlySentOutput{}

	folderID := impl.SentItemsFolderID
	chunk := 1
	continuationToken := ""
	orderBy := "ReceivedDateTime"

	messages, _, err := conn.CustomParams.API.GetMessages(
		input.UserIDPrincipal,
		folderID,
		chunk,
		continuationToken,
		orderBy,
		false,
		log,
	)
	if err != nil {
		log.Info("most_recently_sent action failed")
		return nil, err
	}

	if len(messages) < 1 {
		return nil, fmt.Errorf("most_recently_sent: SentItems folder is empty")
	}

	log.Info("most_recently_sent action succeeded")
	output.MostRecentMessage = messages[0]
	return output, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (a *MostRecentlySentAction) Test(conn *connection.Connection, input *MostRecentlySentInput, log plog.Logger) (*MostRecentlySentOutput, error) {
	output := &MostRecentlySentOutput{}
	// Your code here
	// NOTE: The input you receive in the test method cannot be gauranteed to contain "good" value.
	// You should not assume the input is something you can trust in this context.

	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}
