package implementation

import "net/http"

import "encoding/json"
import "regexp"
import "fmt"

import "github.com/rapid7/komand-plugins/office365/types"

// GetAttachmentsResponse contains the JSON for the list of
// attachments obtained from the Office 365 REST API.
type GetAttachmentsResponse struct {
	Value         []types.Attachment `json:"value"`
	OdataNextLink string             `json:"@odata.nextLink"`
	// weirdly, need OdataContext in order to unmarshal OdataNextLink
	OdataContext string `json:"@odata.context"`
}

// GetAttachments accesses the Office 365 REST API to get a list of
// all attachments to a given email message.  For performance, you can
func (a *API) GetAttachments(userID, messageID string, chunk int, continuationToken string) ([]types.Attachment, string, error) {
	apiURL := a.getAttachmentsURL(userID, messageID, chunk, continuationToken)

	ret := OpReturnValue{}
	thunk := func() error {
		attachments, continuation, err := a.retryableGetAttachments(apiURL)
		ret.RetAttachments = attachments
		ret.RetString = continuation
		return err
	}

	return ret.RetAttachments, ret.RetString, a.WithRetry(thunk)
}

func (a *API) retryableGetAttachments(apiURL string) ([]types.Attachment, string, error) {
	req, err := http.NewRequest("GET", apiURL, nil)
	if err != nil {
		ctl := "GetAttachments, http.NewRequest(), error: %v"
		return nil, "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	jsonBlob, err := a.Do(req)
	if err != nil {
		ctl := "GetAttachments, json.Unmarshal(), error: %v"
		return nil, "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	body := GetAttachmentsResponse{}
	if err := json.Unmarshal(jsonBlob, &body); err != nil {
		ctl := "GetAttachments, json.Unmarshal(), error: %v"
		return nil, "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	newContinuation := ""
	re := regexp.MustCompile(`.*%24(skip=\d+)`)
	if mat := re.FindStringSubmatch(body.OdataNextLink); mat != nil {
		newContinuation = mat[0]
	}

	return body.Value, newContinuation, nil
}

func (a *API) getAttachmentsURL(userID, messageID string,
	chunk int,
	continuationToken string) string {

	continuation := ""
	if continuationToken != "" {
		continuation = "&" + continuationToken
	}

	apiURL := a.UsersURL(userID) + "/messages/" + messageID + "/attachments"
	apiURL += fmt.Sprintf("?$top=%v", chunk) + continuation

	return apiURL
}
