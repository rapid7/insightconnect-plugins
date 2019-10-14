package connection

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	impl "github.com/rapid7/komand-plugins/office365/implementation"
)

// CustomParams includes an instance of the implementation.API struct,
// which is supplies an access token to the Office 365 REST API,
// updating said token when necessary.
type CustomParams struct {
	API *impl.API
}

// Connect returns a ready to use Connection object containing the
// credentials necessary to access the Office 365 REST API.
func Connect(cd *Data, log plog.Logger) (*Connection, error) {
	api := &impl.API{
		TenantID:  cd.TenantID,
		AppID:     cd.AppID,
		AppSecret: cd.AppSecret.SecretKey,
	}

	if err := api.SetAccessToken(); err != nil {
		return nil, err
	}

	log.Info("connection object created")
	return &Connection{
		CustomParams: CustomParams{
			API: api,
		},
	}, nil
}

// Validate is a stub because validation happens in the implementation.
func (c *Connection) Validate() []error {
	return nil
}

// Key comprises any fields needed to make up a unique value for each isntance of a connection
// For example, 2 messages with the same conn params should share 1 connection, and will
// but the next message with different params would use a different connection.
func (c *Data) Key() string {
	if c.ConnectionCacheKey != "" {
		return c.ConnectionCacheKey
	}
	// TODO auto-comprise off string fields
	return c.TenantID + c.AppID
}

// Place Custom Connection Functions and Methods Below
