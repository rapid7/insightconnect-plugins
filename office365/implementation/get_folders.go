package implementation

import "net/http"

import "regexp"
import "encoding/json"
import "fmt"

import "github.com/rapid7/komand-plugins/office365/types"

// GetFoldersResponse contains the JSON for the list of
// attachments obtained from the Office 365 REST API.
type GetFoldersResponse struct {
	Value         []types.Folder `json:"value"`
	OdataNextLink string         `json:"@odata.nextLink"`
	// weirdly, need OdataContext in order to unmarshal OdataNextLink
	OdataContext string `json:"@odata.context"`
}

// GetFolders accesses the Office 365 REST API to get a list of all
// subfolders under a given folder.  To get a list of top-level
// folders, specify the empty string as folderID.  For performance,
// you can use the selectedFields arg to limit which fields are
// retrieved.
func (a *API) GetFolders(userID, folderID, continuationToken string, chunk int) ([]types.Folder, string, error) {
	apiURL := a.getFoldersURL(userID, folderID, continuationToken, chunk)

	ret := OpReturnValue{}
	thunk := func() error {
		folders, continuation, err := a.retryableGetFolders(apiURL)
		ret.RetFolders = folders
		ret.RetString = continuation
		return err
	}

	err := a.WithRetry(thunk)
	return ret.RetFolders, ret.RetString, err
}

func (a *API) retryableGetFolders(apiURL string) ([]types.Folder, string, error) {
	req, err := http.NewRequest("GET", apiURL, nil)
	if err != nil {
		ctl := "GetFolders, http.NewRequest(), error: %v"
		return nil, "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	jsonBlob, err := a.Do(req)
	if err != nil {
		return nil, "", err
	}
	body := GetFoldersResponse{}
	if err := json.Unmarshal(jsonBlob, &body); err != nil {
		ctl := "GetFolders, json.Unmarshal(), error: %v"
		return nil, "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	newContinuation := ""
	re := regexp.MustCompile(`.*%24(skip=\d+)`)
	if mat := re.FindStringSubmatch(body.OdataNextLink); mat != nil {
		newContinuation = "$" + mat[1]
	}

	return body.Value, newContinuation, nil
}

func (a *API) getFoldersURL(userID, folderID, continuationToken string, chunk int) string {
	continuation := ""
	if continuationToken != "" {
		continuation = "&" + continuationToken
	}

	subfolder := "/"
	if folderID != "" {
		subfolder += folderID + "/childfolders/"
	}

	apiURL := a.UsersFoldersURL(userID) + subfolder
	apiURL += fmt.Sprintf("?$top=%v", chunk) + continuation
	return apiURL
}
