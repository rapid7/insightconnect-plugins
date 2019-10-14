package implementation

import "net/http"

import "encoding/json"
import "bytes"
import "fmt"

// MoveFolder moves a folder form one place in an Outlook mailbox to
// another.
func (a *API) MoveFolder(userID, folderToMoveID, destinationFolderID string) (bool, error) {

	apiURL := a.UsersFoldersURL(userID) + "/" + folderToMoveID + "/move"

	details := RelocateRequest{DestinationID: destinationFolderID}

	serial, err := json.Marshal(details)
	if err != nil {
		ctl := "MoveFolder, json.Marshal(), error: %v"
		return false, &Office365Error{fmt.Sprintf(ctl, err)}
	}

	ret := OpReturnValue{}
	thunk := func() error {
		success, err := a.retryableMoveFolder(apiURL, serial)
		ret.RetBool = success
		return err
	}

	return ret.RetBool, a.WithRetry(thunk)
}

func (a *API) retryableMoveFolder(apiURL string, serial []byte) (bool, error) {

	req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(serial))
	if err != nil {
		ctl := "MoveFolder, http.NewRequest(), error: %v"
		return false, &Office365Error{fmt.Sprintf(ctl, err)}
	}

	if _, err := a.Do(req); err != nil {
		return false, err
	}

	return true, nil
}
