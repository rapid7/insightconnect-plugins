package implementation

import "net/http"

import "encoding/json"
import "bytes"
import "fmt"

import "github.com/rapid7/komand-plugins/office365/types"

// CreateFolderRequest contains the JSON to specify the new folder
// name, without the extra fields whose zero values cause the Office
// 365 REST API to barf.
type CreateFolderRequest struct {
	DisplayName string `json:"DisplayName"`
}

// CreateFolder creates a new folder in an Outlook mailbox.
func (a *API) CreateFolder(userID, parentFolderID, displayName string) (string, error) {
	apiURL := a.UsersURL(userID) + "/mailFolders/" + parentFolderID + "/childfolders"

	folder := CreateFolderRequest{DisplayName: displayName}

	serial, err := json.Marshal(folder)

	if err != nil {
		ctl := "CreateFolder, json.Marshal(), error: %v"
		return "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	ret := OpReturnValue{}
	thunk := func() error {
		newFolderID, err := a.retryableCreateFolder(apiURL, serial)
		ret.RetString = newFolderID
		return err
	}

	return ret.RetString, a.WithRetry(thunk)
}

func (a *API) retryableCreateFolder(apiURL string, serial []byte) (string, error) {

	req, err := http.NewRequest("POST", apiURL, bytes.NewBuffer(serial))
	if err != nil {
		ctl := "CreateFolder, http.NewRequest(), error: %v"
		return "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	jsonBlob, err := a.Do(req)
	if err != nil {
		return "", err
	}

	newFolder := types.Folder{}
	if err := json.Unmarshal(jsonBlob, &newFolder); err != nil {
		ctl := "CreateFolder, json.Unmarshal(), error: %v"
		return "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	return newFolder.ID, nil
}
