package implementation

import "net/http"

import "fmt"

// DeleteFolder removes a folder and its contents from a parent
// folder.
func (a *API) DeleteFolder(userID, folderID string) (bool, error) {
	apiURL := a.UsersFoldersURL(userID) + folderID

	ret := OpReturnValue{}
	thunk := func() error {
		success, err := a.retryableDeleteFolder(apiURL)
		ret.RetBool = success
		return err
	}

	return ret.RetBool, a.WithRetry(thunk)
}

func (a *API) retryableDeleteFolder(apiURL string) (bool, error) {
	req, err := http.NewRequest("DELETE", apiURL, nil)
	if err != nil {
		ctl := "DeleteFolder , http.NewRequest(), error: %v"
		return false, &Office365Error{fmt.Sprintf(ctl, err)}
	}

	if _, err := a.Do(req); err != nil {
		return false, err
	}

	return true, nil
}
