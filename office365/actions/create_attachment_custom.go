package actions

import (
	"strings"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	// jh stuff
)

// Validate is a stub because input validation happens in the implementation.
func (i *CreateAttachmentInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *CreateAttachmentOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run the create_attachment action.
func (a *CreateAttachmentAction) Run(conn *connection.Connection, input *CreateAttachmentInput, log plog.Logger) (*CreateAttachmentOutput, error) {
	output := &CreateAttachmentOutput{}

	messageID := input.MessageID
	contentBytes := input.AttachmentContent
	contentURI := ""
	mimeType := input.AttachmentType
	mType := strings.Split(input.AttachmentType, " ")[0]
	if mType == "OTHER" {
		mimeType = input.OtherAttachmentType
	}
	isInline := false
	name := input.AttachmentName

	newAttachmentID, err := conn.CustomParams.API.CreateAttachment(
		input.UserIDPrincipal,
		messageID,
		contentBytes,
		contentURI,
		mimeType,
		isInline,
		name,
	)
	if err != nil {
		log.Info("create_attachment action failed")
		return nil, err
	}

	log.Info("create_attachment action succeeded")
	output.AttachmentID = newAttachmentID
	return output, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (a *CreateAttachmentAction) Test(conn *connection.Connection, input *CreateAttachmentInput, log plog.Logger) (*CreateAttachmentOutput, error) {
	output := &CreateAttachmentOutput{}
	return output, nil
}
