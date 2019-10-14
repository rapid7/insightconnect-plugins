package implementation

import "net/http"

import "encoding/json"
import "bytes"
import "fmt"

import "github.com/rapid7/komand-plugins/office365/types"

// ForwardRequest ...
type ForwardRequest struct {
	Comment      string            `json:"Comment"`
	ToRecipients []types.Recipient `json:"ToRecipients"`
}

// ForwardMessage forwards a given mail message to the given list of
// recipients, with the given body prepended.
func (a *API) ForwardMessage(userID, messageID, body string,
	toRecipients []string) (bool, error) {

	apiURL := a.UsersURL(userID) + "/messages/" + messageID + "/forward"

	container := ForwardRequest{
		Comment:      body,
		ToRecipients: AssembleRecipients(toRecipients),
	}

	serial, err := json.Marshal(container)
	if err != nil {
		ctl := "ForwardMessage, json.Marshal(), error: %v"
		return false, &Office365Error{fmt.Sprintf(ctl, err)}
	}

	ret := OpReturnValue{}
	thunk := func() error {
		success, err := a.retryableForwardMessage(apiURL, serial)
		ret.RetBool = success
		return err
	}

	return ret.RetBool, a.WithRetry(thunk)
}

func (a *API) retryableForwardMessage(apiURL string, serial []byte) (bool, error) {

	req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(serial))
	if err != nil {
		ctl := "ForwardMessage, http.NewRequest(), error: %v"
		return false, &Office365Error{fmt.Sprintf(ctl, err)}
	}

	if _, err := a.Do(req); err != nil {
		return false, err
	}

	return true, nil
}
