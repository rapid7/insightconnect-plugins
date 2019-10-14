package connection

import (
	"github.com/komand/goqualys/qualys"
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
)

// CustomParams is where you the developer will fill in any custom properties, which you would need
// to use or work with in Connect. One example might be any client libraries or supporting properties for working
// with the client libraries you need, but don't want to lose if you regenerate the plugin
type CustomParams struct {
	Qualys *qualys.Client
}

// Connect is the custom code for the developer to write to fully initialize and return a
// ready to use Connection object.
func Connect(cd *Data, log plog.Logger) (*Connection, error) {
	q := qualys.NewClient(nil, cd.Hostname, cd.Credentials.Username, cd.Credentials.Password)
	conn := &Connection{
		CustomParams: CustomParams{
			Qualys: q,
		},
	}
	return conn, nil
}

// Validate will validate the connection is properly setup with whatever rules you put in
// You can leave this blank if you want to, but if you need to enforce restrictions
// here is where you can return a number of errors. Otherwise, return nil for success
func (c *Connection) Validate() []error {
	// Your code here

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
	return c.Hostname
}

// Place Custom Connection Functions and Methods Below
