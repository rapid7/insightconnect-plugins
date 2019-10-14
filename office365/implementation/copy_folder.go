package implementation

import "net/http"

import "encoding/json"
import "bytes"
import "fmt"

import "github.com/rapid7/komand-plugins/office365/types"

// CopyFolder uses the Office 365 REST API to copy a folder and its
// contents from one place in an Outlook mailbox to another.
func (a *API) CopyFolder(userID, folderToCopyID, destinationFolderID string) (string, error) {
	apiURL := a.UsersFoldersURL(userID) + folderToCopyID + "/copy"

	details := RelocateRequest{DestinationID: destinationFolderID}

	serial, err := json.Marshal(details)
	if err != nil {
		ctl := "CopyFolder, json.Marshal(), error: %v"
		return "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	ret := OpReturnValue{}
	thunk := func() error {
		newFolderID, err := a.retryableCopyFolder(apiURL, serial)
		ret.RetString = newFolderID
		return err
	}

	return ret.RetString, a.WithRetry(thunk)
}

func (a *API) retryableCopyFolder(apiURL string, serial []byte) (string, error) {
	req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(serial))
	if err != nil {
		ctl := "CopyFolder, http.NewRequest(), error: %v"
		return "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	jsonBlob, err := a.Do(req)
	if err != nil {
		return "", err
	}

	newFolder := types.Folder{}
	if err := json.Unmarshal(jsonBlob, &newFolder); err != nil {
		ctl := "CopyFolder, json.Unmarshal(), error: %v"
		return "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	return newFolder.ID, nil
}
