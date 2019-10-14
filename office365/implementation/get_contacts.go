package implementation

import (
	"encoding/json"
	"fmt"
	"net/http"
	"regexp"

	"github.com/rapid7/komand-plugins/office365/types"
)

// GetContactsResponse contains the JSON for the list of contacts
// obtained from the Office 365 REST API.
type GetContactsResponse struct {
	Value         []types.Contact `json:"value"`
	OdataNextLink string          `json:"@odata.nextLink"`
	// weirdly, need OdataContext in order to unmarshal OdataNextLink
	OdataContext string `json:"@odata.context"`
}

// GetContacts accesses the Office 365 REST API to get a list of all
// contacts for a given email account.  For performance, you can use
// the selectedFields arg to limit which fields are retrieved.
func (a *API) GetContacts(userID string, chunk int, continuationToken string) ([]types.Contact, string, error) {

	apiURL := a.getContactsURL(userID, chunk, continuationToken)

	ret := OpReturnValue{}
	thunk := func() error {
		contacts, continuation, err := a.retryableGetContacts(apiURL)
		ret.RetContacts = contacts
		ret.RetString = continuation
		return err
	}

	return ret.RetContacts, ret.RetString, a.WithRetry(thunk)
}

func (a *API) retryableGetContacts(apiURL string) ([]types.Contact, string, error) {
	req, err := http.NewRequest("GET", apiURL, nil)
	if err != nil {
		ctl := "GetContacts, http.NewRequest(), error: %v"
		return nil, "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	jsonBlob, err := a.Do(req)
	if err != nil {
		return nil, "", err
	}
	body := GetContactsResponse{}
	if err := json.Unmarshal(jsonBlob, &body); err != nil {
		ctl := "GetContacts, json.Unmarshal(), error: %v"
		return nil, "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	newContinuation := ""
	re := regexp.MustCompile(`.*%24(skip=\d+)`)
	if mat := re.FindStringSubmatch(body.OdataNextLink); mat != nil {
		newContinuation = "$" + mat[1]
	}

	return body.Value, newContinuation, nil
}

func (a *API) getContactsURL(userID string, chunk int, continuationToken string) string {
	continuation := ""
	if continuationToken != "" {
		continuation = "&" + continuationToken
	}
	apiURL := a.UsersURL(userID) + "/contacts"
	apiURL += fmt.Sprintf("?$top=%v", chunk) + continuation

	return apiURL
}
