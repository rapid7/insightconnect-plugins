package connection

// Code generated by the Komand Go SDK Generator. DO NOT EDIT
import (
	"github.com/rapid7/komand-plugins/qualys_reports/types"
)

// Connection is the connection object that the developer will add to when integrating a third party
// API. Add any kind of long lived or custom 3rd party connection objects into this struct.
// Each instance of this struct WILL be shared globally, so be sure to add mutexes or atomic
// operations where needed.
type Connection struct {
	CustomParams
	Credentials types.CredentialUsernamePassword `json:"credentials"`
	Hostname    string                           `json:"hostname"`
}

// Data is the struct that holds the raw connection params from the incoming message
// This will be turned into a real connection by the SDK runtime. You should never directly
// need to use this object, only the regular connection. As such, avoid adding any properties to it.
type Data struct {
	ConnectionCacheKey string                           `json:"connection_cache_key"`
	Credentials        types.CredentialUsernamePassword `json:"credentials"`
	Hostname           string                           `json:"hostname"`
}
