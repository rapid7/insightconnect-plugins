package implementation

import "net/http"

import "fmt"

// DeleteAttachment removes an attachment from a mail message.
func (a *API) DeleteAttachment(userID, attachmentID, messageID string) (bool, error) {
	apiURL := a.UsersURL(userID) + "/messages/" + messageID + "/attachments/" + attachmentID

	ret := OpReturnValue{}
	thunk := func() error {
		success, err := a.retryableDeleteAttachment(apiURL)
		ret.RetBool = success
		return err
	}

	return ret.RetBool, a.WithRetry(thunk)
}

func (a *API) retryableDeleteAttachment(apiURL string) (bool, error) {
	req, err := http.NewRequest("DELETE", apiURL, nil)
	if err != nil {
		ctl := "DeleteAttachment, http.NewRequest(), error: %v"
		return false, &Office365Error{fmt.Sprintf(ctl, err)}
	}

	if _, err := a.Do(req); err != nil {
		return false, err
	}

	return true, nil
}
