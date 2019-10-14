package implementation

import "net/http"

import "encoding/json"
import "bytes"
import "fmt"

import "github.com/rapid7/komand-plugins/office365/types"

// CopyMessage uses the Office 365 REST API to copy a message from one
// place in an Outlook mailbox to another.
func (a *API) CopyMessage(userID, messageID, folderID string) (string, error) {
	apiURL := a.UsersURL(userID) + "/messages/" + messageID + "/copy"

	details := RelocateRequest{DestinationID: folderID}

	serial, err := json.Marshal(details)
	if err != nil {
		ctl := "CopyMessage, json.Marshal(), error: %v"
		return "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	ret := OpReturnValue{}
	thunk := func() error {
		newMessageID, err := a.retryableCopyMessage(apiURL, serial)
		ret.RetString = newMessageID
		return err
	}

	return ret.RetString, a.WithRetry(thunk)
}

func (a *API) retryableCopyMessage(apiURL string, serial []byte) (string, error) {
	req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(serial))
	if err != nil {
		ctl := "CopyMessage, http.NewRequest(), error: %v"
		return "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	jsonBlob, err := a.Do(req)
	if err != nil {
		return "", err
	}

	newMessage := types.Message{}
	if err := json.Unmarshal(jsonBlob, &newMessage); err != nil {
		ctl := "CopyMessage, json.Unmarshal(), error: %v"
		return "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	return newMessage.ID, nil
}
