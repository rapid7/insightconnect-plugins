package implementation

import "net/http"

import "fmt"

// DeleteMessage removes a message from an Outlook mailbox.
func (a *API) DeleteMessage(userID, messageID string) (bool, error) {
	apiURL := a.UsersURL(userID) + "/messages/" + messageID

	ret := OpReturnValue{}
	thunk := func() error {
		success, err := a.retryableDeleteMessage(apiURL)
		ret.RetBool = success
		return err
	}

	err := a.WithRetry(thunk)
	return ret.RetBool, err
}

func (a *API) retryableDeleteMessage(apiURL string) (bool, error) {
	req, err := http.NewRequest("DELETE", apiURL, nil)
	if err != nil {
		ctl := "DeleteMessage, http.NewRequest(), error: %v"
		return false, &Office365Error{fmt.Sprintf(ctl, err)}
	}

	if _, err := a.Do(req); err != nil {
		return false, err
	}

	return true, nil
}
