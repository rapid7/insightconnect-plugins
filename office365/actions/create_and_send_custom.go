package actions

import (
	"strings"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	impl "github.com/rapid7/komand-plugins/office365/implementation" // jh stuff
)

// Validate is a stub because input validation happens in the implementation.
func (i *CreateAndSendInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *CreateAndSendOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run the create_and_send action.
func (a *CreateAndSendAction) Run(conn *connection.Connection, input *CreateAndSendInput, log plog.Logger) (*CreateAndSendOutput, error) {
	output := &CreateAndSendOutput{}

	subject := input.Subject
	body := input.Body
	bodyIsHTML := input.BodyIsHTML
	toRecipients := input.ToRecipients
	ccRecipients := input.CcRecipients
	bccRecipients := input.BccRecipients
	attachmentName := input.AttachmentName
	attachmentType := input.AttachmentType
	mType := strings.Split(input.AttachmentType, " ")[0]
	if mType == "OTHER" {
		attachmentType = input.OtherAttachmentType
	}
	attachmentBase64Bytes := input.AttachmentBytes
	importance := impl.NormalImportance
	saveToSentItems := input.SaveToSentItems

	_, err := conn.CustomParams.API.CreateAndSendMessage(
		subject,
		body,
		bodyIsHTML,
		input.UserIDPrincipal,
		toRecipients,
		ccRecipients,
		bccRecipients,
		attachmentName,
		attachmentType,
		attachmentBase64Bytes,
		importance,
		saveToSentItems,
	)
	if err != nil {
		log.Info("create_and_send action failed")
		return nil, err
	}

	log.Info("create_and_send action succeeded")
	return output, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (a *CreateAndSendAction) Test(conn *connection.Connection, input *CreateAndSendInput, log plog.Logger) (*CreateAndSendOutput, error) {
	output := &CreateAndSendOutput{}
	// Your code here
	// NOTE: The input you receive in the test method cannot be gauranteed to contain "good" value.
	// You should not assume the input is something you can trust in this context.

	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}
