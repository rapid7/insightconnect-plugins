package actions

import (
	"encoding/json"
	"fmt"

	"github.com/nlopes/slack"
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/slack/connection"
)

// Validate will validate the input is properly setup with whatever rules you put in
// You can also use this to pre-set any values before they are run by the Run method.
// Note that for Actions, the  Input message is inspected every time time, just before it
// is handed to the Run method. Keep this in mind when setting any properties on the Input i
// You can return a set of errors for any reason to fail the step.
// Otherwise, return nil for success
func (i *PostMessageInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)

	// Custom validation code here
	// Append errors as needed

	// return
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate will validate the output is properly setup with whatever rules you put in
// You can leave this blank if you want to, but if you need to enforce restrictions
// here is where you can return a number of errors. Otherwise, return nil for success
func (o *PostMessageOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)

	// Custom validation code here
	// Append errors as needed

	// return
	if len(errs) > 0 {
		return errs
	}
	return nil
}

func (a *PostMessageAction) lookupUserChannel(conn *connection.Connection, input *PostMessageInput) (string, error) {
	users, err := conn.API.GetUsers()
	if err != nil {
		return "", fmt.Errorf("Unabel to get user channel: %s", err)
	}

	userId := ""
	for _, user := range users {
		if user.Name == input.Username {
			userId = user.ID
			break
		}
	}
	if userId == "" {
		return "", fmt.Errorf("User not found")
	}

	_, _, channel, err := conn.API.OpenIMChannel(userId)
	if err != nil {
		return "", fmt.Errorf("Could not open channel to user: %s", err)
	}
	return channel, nil
}

func (a *PostMessageAction) lookupChannelOrUser(conn *connection.Connection, input *PostMessageInput) (string, error) {
	if input.ChannelID != "" {
		return input.ChannelID, nil
	}

	if input.Channel != "" {
		// try to look it up by id first
		if n, _ := conn.LookupChannelOrGroupByName(input.Channel); n != nil {
			return *n, nil
		}
		return input.Channel, nil
	}
	return a.lookupUserChannel(conn, input)
}

// Run will run the action with the given input over the given connection
func (a *PostMessageAction) Run(conn *connection.Connection, input *PostMessageInput, log plog.Logger) (*PostMessageOutput, error) {
	output := &PostMessageOutput{}

	log.Infof("Running Post Message action")

	// lookup channel or user
	channelID, err := a.lookupChannelOrUser(conn, input)
	if err != nil {
		return nil, err
	}

	params := slack.NewPostMessageParameters()

	if input.Attachments != nil {
		var attachments []slack.Attachment
		if err := json.Unmarshal(input.Attachments, &attachments); err == nil {
			params.Attachments = attachments
		} else {
			log.Infof("Attachments could not unmarshal: %v", err)
		}
	}

	params.IconEmoji = input.IconEmoji
	r1, r2, err := conn.API.PostMessage(channelID, input.Message, params)

	if err != nil {
		return nil, err
	}

	output.MessageID = r1
	output.Timestamp = r2

	log.Infof("Posted message with result: %s %s", r1, r2)

	return output, nil
}

// Test will test the action with the given input over the given connection.
// For this, you should design the output result to be used with the tests in the test/ directory.
// You do not need to / should not need to invoke the actual API, this is just for testing.
func (a *PostMessageAction) Test(conn *connection.Connection, input *PostMessageInput, log plog.Logger) (*PostMessageOutput, error) {
	output := &PostMessageOutput{}
	// Your code here
	// NOTE: The input you receive in the test method cannot be gauranteed to contain "good" value.
	// You should not assume the input is something you can trust in this context.

	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}
