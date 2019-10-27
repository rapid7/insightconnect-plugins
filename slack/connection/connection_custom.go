package connection

import (
	"fmt"

	"github.com/nlopes/slack"
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
)

// CustomParams is where you the developer will fill in any custom properties, which you would need
// to use or work with in Connect. One example might be any client libraries or supporting properties for working
// with the client libraries you need, but don't want to lose if you regenerate the plugin
type CustomParams struct {
	Token    string                  `json:"token"`
	API      *slack.Client           `json:"-"`
	LoggedIn *slack.AuthTestResponse `json:"-"`
	Channels []slack.Channel         `json:"-"`
	Groups   []slack.Group           `json:"-"`
	Users    []slack.User            `json:"-"`
}

func (c *Connection) LookupUserByID(id string) (*slack.User, error) {
	for _, user := range c.Users {
		if user.ID == id {
			return &user, nil
		}
	}

	ch, _ := c.API.GetUserInfo(id)
	if ch != nil {
		c.Users = append(c.Users, *ch)
		return ch, nil
	}

	return nil, nil
}

func (c *Connection) LookupChannelOrGroupByName(name string) (*string, error) {
	// try to look it up by id first
	if ch, _ := c.LookupChannelByName(name); ch != nil {
		return &ch.ID, nil
	}

	if gr, _ := c.LookupGroupByName(name); gr != nil {
		return &gr.ID, nil
	}

	return nil, nil
}

func (c *Connection) LookupChannelByName(name string) (*slack.Channel, error) {
	for _, channel := range c.Channels {
		if channel.Name == name {
			return &channel, nil
		}
	}
	return nil, nil
}

func (c *Connection) LookupGroupByName(name string) (*slack.Group, error) {
	for _, channel := range c.Groups {
		if channel.Name == name {
			return &channel, nil
		}
	}
	return nil, nil
}

func (c *Connection) LookupChannelByID(id string) (*slack.Channel, error) {
	for _, channel := range c.Channels {
		if channel.ID == id {
			return &channel, nil
		}
	}

	ch, _ := c.API.GetChannelInfo(id)
	if ch != nil {
		c.Channels = append(c.Channels, *ch)
		return ch, nil
	}

	return nil, nil
}

func (c *Connection) LookupGroupByID(id string) (*slack.Group, error) {
	for _, group := range c.Groups {
		if group.ID == id {
			return &group, nil
		}
	}

	ch, _ := c.API.GetGroupInfo(id)
	if ch != nil {
		c.Groups = append(c.Groups, *ch)
		return ch, nil
	}

	return nil, nil
}

// Connect is the custom code for the developer to write to fully initialize and return a
// ready to use Connection object.
func Connect(cd *Data, log plog.Logger) (*Connection, error) {
	c := &Connection{}
	api := slack.New(c.Token)
	loggedIn, err := api.AuthTest()
	if err != nil {
		return nil, fmt.Errorf("Error connecting: %s", err)
	}
	c.API = api
	c.LoggedIn = loggedIn
	c.Channels, _ = api.GetChannels(false)
	c.Users, _ = api.GetUsers()
	c.Groups, _ = api.GetGroups(false)

	log.Infof("Connected to Slack: %+v", c.LoggedIn)
	// log.Printf("Users: %+v", c.Users)
	// log.Printf("Channel: %+v", c.Channels)
	// log.Printf("Groups: %+v", c.Groups)

	return c, nil
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
	return ""
}

// Place Custom Connection Functions and Methods Below
