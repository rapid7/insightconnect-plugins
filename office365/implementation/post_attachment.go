package implementation

import "net/http"

import "encoding/json"
import "bytes"
import "fmt"

import "github.com/rapid7/komand-plugins/office365/types"

// CreateAttachment associates a new attachment with the given mail
// message.  The message may have already been read, it doesn't
// matter.
func (a *API) CreateAttachment(userID, messageID, contentBytes, contentURI, mimeType string, isInline bool, name string) (string, error) {
	apiURL := a.UsersURL(userID) + "/messages/" + messageID + "/attachments"

	attachment := types.Attachment{
		ContentBytes: contentBytes,
		ContentType:  mimeType,
		IsInline:     isInline, // isInline == true doesn't seem to work
		Name:         name,
		OdataType:    "#Microsoft.OutlookServices.FileAttachment",
	}

	serial, err := json.Marshal(attachment)
	if err != nil {
		ctl := "CreateAttachment, json.Marshal(), error: %v"
		return "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	ret := OpReturnValue{}
	thunk := func() error {
		newAttachmentID, err := a.retryableCreateAttachment(apiURL, serial)
		ret.RetString = newAttachmentID
		return err
	}

	return ret.RetString, a.WithRetry(thunk)
}

func (a *API) retryableCreateAttachment(apiURL string, serial []byte) (string, error) {
	req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(serial))
	if err != nil {
		ctl := "CreateAttachment, http.NewRequest(), error: %v"
		return "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	jsonBlob, err := a.Do(req)
	if err != nil {
		return "", err
	}
	newAttachment := types.Attachment{}
	if err := json.Unmarshal(jsonBlob, &newAttachment); err != nil {
		ctl := "CreateAttachment, json.Unmarshal(), error: %v"
		return "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	//fmt.Printf("status: %v, ID: %v\n", resp.StatusCode, newAttachment.ID) //debug
	return newAttachment.ID, nil
}
