package implementation

import "net/http"

import "encoding/json"
import "bytes"
import "fmt"

// MoveMessage moves a mail message fromone place in an Outlook
// mailbox to another.
func (a *API) MoveMessage(userID, messageID, folderID string) (bool, error) {

	apiURL := a.UsersURL(userID) + "/messages/" + messageID + "/move"

	details := RelocateRequest{DestinationID: folderID}

	serial, err := json.Marshal(details)
	if err != nil {
		ctl := "MoveMessage, json.Marshal(), error: %v"
		return false, &Office365Error{fmt.Sprintf(ctl, err)}
	}

	ret := OpReturnValue{}
	thunk := func() error {
		success, err := a.retryableMoveMessage(apiURL, serial)
		ret.RetBool = success
		return err
	}

	return ret.RetBool, a.WithRetry(thunk)
}

func (a *API) retryableMoveMessage(apiURL string, serial []byte) (bool, error) {
	req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(serial))
	if err != nil {
		ctl := "MoveMessage, http.NewRequest(), error: %v"
		return false, &Office365Error{fmt.Sprintf(ctl, err)}
	}

	if _, err := a.Do(req); err != nil {
		return false, err
	}
	return true, nil
}
