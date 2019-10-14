package implementation

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"time"
)

// API constants for the Microsoft Graph API
const (
	// APIHost is the host handling Office365 REST API requests.
	APIHost = "https://graph.microsoft.com"

	// API Version is the version of Microsoft Graph API
	APIVersion = "v1.0"
)

// API is a struct contining all data necessary to support the plugin connection.
type API struct {
	// TenantID identifies the tenant of the application (equivalent to directory ID)
	TenantID string

	// AppID identifies the user's app (equivalent to application ID)
	AppID string

	// AppSecret is the secret held by the user's app (equivalent to application key)
	AppSecret string

	// AppIDURI is the URI found on the Properties section in the registered app's settings
	AppIDURI string

	// accessToken holds the access token for authentication
	accessToken string

	timeReceived time.Time
}

// BaseURL returns the base URL for the current Microsoft Graph API
func (a *API) BaseURL() string {
	return APIHost + "/v1.0"
}

// UsersURL returns the URL for the users
func (a *API) UsersURL(userID string) string {
	return a.BaseURL() + "/" + a.TenantID + "/users/" + userID
}

// UsersFoldersURL returns the URL for managing users mail folders
func (a *API) UsersFoldersURL(userID string) string {
	return a.UsersURL(userID) + "/mailFolders/"
}

// WithRetry is a "scoping function" that runs a given Office 365 op
// in a context where a 401 will be retried in case it is due to an
// expired token.
func (a *API) WithRetry(thunk func() error) error {
	if err := thunk(); err != nil { // side-effects an OpReturnValue lexically closed by thunk
		maybe401, ok := err.(*Office365Error)
		if ok && maybe401 == &Office365UnauthorizedError {
			a.accessToken = "" // setting to empty will force refresh
			if err := thunk(); err != nil {
				return err
			}
		}
	}
	return nil
}

// Do executes an API call against the Microsoft Graph API
func (a *API) Do(req *http.Request) ([]byte, error) {
	if elapsed := time.Now().Sub(a.timeReceived); elapsed.Minutes() >= 59 {
		a.SetAccessToken()
	}
	auth := "Bearer " + a.accessToken
	req.Header.Set("Authorization", auth)
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		ctl := "http.Client.do(), error: %v"
		return nil, &Office365Error{fmt.Sprintf(ctl, err)}
	}
	defer resp.Body.Close()

	if resp.StatusCode < 200 || resp.StatusCode >= 300 {
		if resp.StatusCode == 401 {
			return nil, &Office365UnauthorizedError
		}
		ctl := "failure response, status: %v, details:\n%v"
		return nil, &Office365Error{fmt.Sprintf(ctl, resp.StatusCode)}
	}

	jsonBlob, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		ctl := "ioutil.ReadAll(), error: %v"
		return nil, &Office365Error{fmt.Sprintf(ctl, err)}
	}

	return jsonBlob, nil
}
