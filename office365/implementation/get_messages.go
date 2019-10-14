package implementation

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"regexp"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/types"
)

// GetMessagesResponse contains the JSON for the list of messages
// obtained from the Office 365 REST API.
type GetMessagesResponse struct {
	Value         []types.Message `json:"value"`
	OdataNextLink string          `json:"@odata.nextLink"`
	// weirdly, need OdataContext in order to unmarshal OdataNextLink
	OdataContext string `json:"@odata.context"`
}

func (a *API) MarkMessageAsRead(apiURL string, msgID string) (string, error) {
	payload := map[string]interface{}{
		"IsRead": true,
	}

	bytesRepresentation, err := json.Marshal(payload)
	if err != nil {
		return "", err
	}

	url := apiURL + "/" + msgID
	req, err := http.NewRequest("PATCH", url, bytes.NewBuffer(bytesRepresentation))
	req.Header.Add("Content-Type", "application/json")
	if err != nil {
		log.Fatalln(err)
	}
	_, err = a.Do(req)
	if err != nil {
		return "", err
	}

	return url, nil
}

// GetMessages accesses the Office 365 REST API to get a list of all
// the email messages in the given folder.  The following are
// well-known folder IDs:
//   "Inbox"
//   "Drafts"
//   "SentItems"
//   "DeletedItems"
// For performance, you can use the selectedFields arg to limit which
// fields are retrieved.
func (a *API) GetMessages(userID string,
	folderID string,
	chunk int,
	continuationToken string,
	orderBy string,
	unreadOnly bool,
	log plog.Logger,
) ([]types.Message, string, error) {

	apiURL := a.UsersURL(userID) + "/messages"

	if unreadOnly {
		apiURL = apiURL //+ "$filter=isRead eq false"
	}

	ret := OpReturnValue{}
	thunk := func() error {
		messages, continuation, err := a.retryableGetMessages(apiURL, log)
		ret.RetMessages = messages
		ret.RetString = continuation
		return err
	}

	err := a.WithRetry(thunk)

	return ret.RetMessages, ret.RetString, err
}

func (a *API) retryableGetMessages(apiURL string, log plog.Logger) ([]types.Message, string, error) {

	req, err := http.NewRequest("GET", apiURL, nil)
	if err != nil {
		ctl := "GetMessages, http.NewRequest(), error: %v"
		return nil, "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	jsonBlob, err := a.Do(req)
	if err != nil {
		return nil, "", err
	}
	body := GetMessagesResponse{}
	if err := json.Unmarshal(jsonBlob, &body); err != nil {
		ctl := "GetMessages, json.Unmarshal(), error: %v"
		return nil, "", &Office365Error{fmt.Sprintf(ctl, err)}
	}

	newContinuation := ""
	re := regexp.MustCompile(`.*%24(skip=\d+)`)
	if mat := re.FindStringSubmatch(body.OdataNextLink); mat != nil {
		newContinuation = mat[0]
	}

	return body.Value, newContinuation, nil
}
