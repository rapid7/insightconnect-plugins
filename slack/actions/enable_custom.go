package actions

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/slack/connection"
)

type EnableJson struct {
	Active bool `json:"active"`
}

// Validate will validate the input is properly setup with whatever rules you put in
// You can also use this to pre-set any values before they are run by the Run method.
// Note that for Actions, the  Input message is inspected every time time, just before it
// is handed to the Run method. Keep this in mind when setting any properties on the Input i
// You can return a set of errors for any reason to fail the step.
// Otherwise, return nil for success
func (i *EnableInput) Validate(log plog.Logger) []error {
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
func (o *EnableOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)

	// Custom validation code here
	// Append errors as needed

	// return
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run will run the action with the given input over the given connection
func (a *EnableAction) Run(conn *connection.Connection, input *EnableInput, log plog.Logger) (*EnableOutput, error) {
	output := &EnableOutput{}

	users, err := conn.API.GetUsers()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Enable: %v", err)
	}
	id := ""
	for i := 0; i < len(users); i += 1 {
		if users[i].Profile.Email == input.Email {
			id = users[i].ID
		}
	}
	if id == "" {
		fmt.Fprintf(os.Stderr, "Enable: ID is null")
	}
	ejson := EnableJson{Active: true}
	data, err := json.Marshal(ejson)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Enable: JSON marshaling failed: %s", err)
	}

	b := bytes.NewBuffer(data)
	client := &http.Client{}
	url := "https://api.slack.com/scim/v1/" + "Users/" + id
	req, err := http.NewRequest("PATCH", url, b)
	req.Header.Add("Authorization", conn.Token)
	req.Header.Add("Content-Type", "application/json")
	resp, err := client.Do(req)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Enable: %v\n", err)
		os.Exit(1)
	}
	_, err = ioutil.ReadAll(resp.Body)
	//fmt.Fprintf(os.Stdout, "%s", bytes)
	resp.Body.Close()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Enable: %v\n", err)
		os.Exit(1)
	}
	output.Success = true

	return output, nil
}

// Test will test the action with the given input over the given connection.
// For this, you should design the output result to be used with the tests in the test/ directory.
// You do not need to / should not need to invoke the actual API, this is just for testing.
func (a *EnableAction) Test(conn *connection.Connection, input *EnableInput, log plog.Logger) (*EnableOutput, error) {
	output := &EnableOutput{}
	// Your code here
	// NOTE: The input you receive in the test method cannot be gauranteed to contain "good" value.
	// You should not assume the input is something you can trust in this context.

	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}
