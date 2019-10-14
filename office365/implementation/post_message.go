package implementation

import "net/http"

import "encoding/json"
import "bytes"
import "fmt"

import "github.com/rapid7/komand-plugins/office365/types"

// CreateAndSendRequest ...
type CreateAndSendRequest struct {
	Message         types.Message `json:"Message"`
	SaveToSentItems bool          `json:"SaveToSentItems"`
}

// CreateAndSendMessage is the central use case of a mail client: it
// populates and sends an email message.
func (a *API) CreateAndSendMessage(subject string,
	body string,
	bodyIsHTML bool,
	fromUserID string,
	toRecipients []string,
	ccRecipients []string,
	bccRecipients []string,
	attachmentName string,
	attachmentType string,
	attachmentBase64Bytes string,
	importance string,
	saveToSentItems bool) (bool, error) {

	apiURL := a.UsersURL(fromUserID) + "/sendmail"

	if importance == "" {
		importance = NormalImportance
	}
	attachment := assembleAttachment(attachmentName, attachmentType, attachmentBase64Bytes)
	message := a.assembleMessage(
		subject,
		assembleBody(body, bodyIsHTML),
		fromUserID,
		AssembleRecipients(toRecipients),
		AssembleRecipients(ccRecipients),
		AssembleRecipients(bccRecipients),
		attachment,
		importance,
	)
	container := CreateAndSendRequest{
		Message:         message,
		SaveToSentItems: saveToSentItems,
	}

	serial, err := json.Marshal(container)
	if err != nil {
		ctl := "CreateAndSendMessage, json.Marshal(), error: %v"
		return false, &Office365Error{fmt.Sprintf(ctl, err)}
	}

	ret := OpReturnValue{}
	thunk := func() error {
		success, err := a.retryableCreateAndSendMessage(apiURL, serial)
		ret.RetBool = success
		return err
	}

	return ret.RetBool, a.WithRetry(thunk)
}

func (a *API) retryableCreateAndSendMessage(apiURL string, serial []byte) (bool, error) {
	req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(serial))
	if err != nil {
		ctl := "CreateAndSendMessage, http.NewRequest(), error: %v"
		return false, &Office365Error{fmt.Sprintf(ctl, err)}
	}

	if _, err := a.Do(req); err != nil {
		return false, err
	}
	return true, nil
}

func assembleBody(body string, isHTML bool) types.MessageBody {
	contentType := ContentTypeText
	if isHTML {
		contentType = ContentTypeHTML
	}
	return types.MessageBody{
		ContentType: contentType,
		Content:     body,
	}
}

func assembleAttachment(name string, mimeType string, base64Bytes string) types.Attachment {
	return types.Attachment{
		Name:         name,
		ContentType:  mimeType,
		ContentBytes: base64Bytes,
		OdataType:    "#Microsoft.OutlookServices.FileAttachment",
	}
}

func (a *API) assembleMessage(
	subject string,
	body types.MessageBody,
	fromEmail string,
	toRecipients []types.Recipient,
	ccRecipients []types.Recipient,
	bccRecipients []types.Recipient,
	attachment types.Attachment,
	importance string,
) types.Message {

	fromAddress := types.EmailAddress{Address: fromEmail}
	from := types.Recipient{EmailAddress: fromAddress}
	hasAttachment := attachment.Name != ""
	attachments := []types.Attachment{}
	if hasAttachment {
		attachments = []types.Attachment{attachment}
	}
	return types.Message{
		From:           from,
		Sender:         from,
		ReplyTo:        []types.Recipient{from},
		Subject:        subject,
		HasAttachments: hasAttachment,
		Attachments:    attachments,
		BccRecipients:  bccRecipients,
		CcRecipients:   ccRecipients,
		ToRecipients:   toRecipients,
		Importance:     importance,
		Body:           body,
	}
}
