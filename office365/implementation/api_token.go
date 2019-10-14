package implementation

import "net/url"
import "net/http"
import "io/ioutil"
import "encoding/json"
import "bytes"
import "strconv"
import "fmt"
import "time"

// Authentication constants for the Microsoft Graph API
const (
	AuthenticationBaseURL   = "https://login.microsoftonline.com"
	AuthenticationScope     = ".default"
	AuthenticationGrantType = "client_credentials"
	AuthenticationResource  = "https://graph.microsoft.com"
)

// APITokens is a struct that mirrors the JSON structure of the
// response to a request for a token from Azure AD.
type APITokens struct {
	AccessToken string `json:"access_token"`
	Scope       string `json:"scope"`
}

// SetAccessToken takes a consentCode string and returns the
// corresponding access token.
func (a *API) SetAccessToken() error {
	data := url.Values{}
	// pToken := a.accessToken
	data.Set("grant_type", "client_credentials")
	token, err := a.getTokensShared(data, "GetAccessToken")
	if err != nil {
		return err
	}
	a.timeReceived = time.Now()
	a.accessToken = token
	return nil
}

func (a *API) getTokensShared(data url.Values, which string) (string, error) {
	tokenURL := AuthenticationBaseURL + "/" + a.TenantID + "/oauth2/token"
	data.Set("scope", AuthenticationResource+"/"+AuthenticationScope)
	data.Set("client_id", a.AppID)
	data.Set("client_secret", a.AppSecret)
	data.Set("resource", AuthenticationResource)
	encoded := data.Encode()

	req, err := http.NewRequest("POST", tokenURL, bytes.NewBufferString(encoded))
	if err != nil {
		ctl := "%v, http.NewRequest(): %v"
		return "", &Office365Error{fmt.Sprintf(ctl, which, err)}
	}

	req.Header.Add("Content-Type", "application/x-www-form-urlencoded")
	req.Header.Add("Content-Length", strconv.Itoa(len(encoded)))
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		ctl := "%v, http.Client.do: %v"
		return "", &Office365Error{fmt.Sprintf(ctl, which, err)}
	}

	defer resp.Body.Close()
	if resp.StatusCode < 200 || resp.StatusCode >= 300 {
		ctl := "%v, failure response, status: %v"
		return "", &Office365Error{fmt.Sprintf(ctl, which, resp.StatusCode)}
	}

	jsonBlob, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		ctl := "%v, ioutil.ReadAll(), error: %v"
		return "", &Office365Error{fmt.Sprintf(ctl, which, err)}
	}

	tokens := APITokens{}
	if err := json.Unmarshal(jsonBlob, &tokens); err != nil {
		ctl := "%v, json.Unmarshal(), error: %v"
		return "", &Office365Error{fmt.Sprintf(ctl, which, err)}
	}

	return tokens.AccessToken, nil
}
