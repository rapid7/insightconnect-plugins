package implementation

import "net/http"

import "encoding/json"
import "bytes"
import "fmt"

// ReplyRequest ...
type ReplyRequest struct {
	Comment string `json:"Comment"`
}

// ReplyToMessage replies to a given mail message, with te given body
// prepended.
func (a *API) ReplyToMessage(userID, messageID string, body string) (bool, error) {

	apiURL := a.UsersURL(userID) + "/messages/" + messageID + "/reply"

	container := ReplyRequest{Comment: body}

	serial, err := json.Marshal(container)
	if err != nil {
		ctl := "ReplyToMessage, json.Marshal(), error: %v"
		return false, &Office365Error{fmt.Sprintf(ctl, err)}
	}

	ret := OpReturnValue{}
	thunk := func() error {
		success, err := a.retryableReplyToMessage(apiURL, serial)
		ret.RetBool = success
		return err
	}

	return ret.RetBool, a.WithRetry(thunk)
}

func (a *API) retryableReplyToMessage(apiURL string, serial []byte) (bool, error) {

	req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(serial))
	if err != nil {
		ctl := "ReplyToMessage, http.NewRequest(), error: %v"
		return false, &Office365Error{fmt.Sprintf(ctl, err)}
	}

	if _, err := a.Do(req); err != nil {
		return false, err
	}

	return true, nil
}
