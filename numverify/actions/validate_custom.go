package actions

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"time"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/numverify/connection"
)

// Validate will validate the input is properly setup with whatever rules you put in
// You can also use this to pre-set any values before they are run by the Run method.
// Note that for Actions, the  Input message is inspected every time time, just before it
// is handed to the Run method. Keep this in mind when setting any properties on the Input i
// You can return a set of errors for any reason to fail the step.
// Otherwise, return nil for success
func (i *ValidateInput) Validate(log plog.Logger) []error {
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
func (o *ValidateOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)

	// Custom validation code here
	// Append errors as needed

	// return
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Params lets us pass the parameters to the web service succinctly
type numberParams struct {
	PhoneNumber    string
	CountryCode    string
	Server         string
	ApplicationKey string
	TimeoutInSec   int
}

// validateNumber is the go process for accessing NumVerify inside the given
// timeout interval
func validateNumber(params numberParams) []byte {
	jsonOut := []byte{}
	webOut := make(chan []byte, 1)
	timeout := time.After(time.Duration(params.TimeoutInSec) * time.Second)
	go func() { webNumVerify(params, webOut) }()
	select {
	case jsonOut = <-webOut:
	case <-timeout:
		msg := fmt.Sprintf(`{"%v":%v}`, "TIMEOUT", params.TimeoutInSec)
		jsonOut = []byte(msg)
	}
	return jsonOut
}

func webNumVerify(params numberParams, webOut chan []byte) {
	url := ""
	url = url + params.Server
	url = url + "?access_key=" + params.ApplicationKey
	url = url + "&number=" + params.PhoneNumber
	url = url + "&country_code=" + params.CountryCode
	resp, getErr := http.Get(url)
	if getErr == nil {
		body, readErr := ioutil.ReadAll(resp.Body)
		if readErr == nil {
			webOut <- body
		}
	}
}

// Run will run the action with the given input over the given connection
func (a *ValidateAction) Run(conn *connection.Connection, input *ValidateInput, log plog.Logger) (*ValidateOutput, error) {
	output := &ValidateOutput{}

	params := numberParams{
		PhoneNumber:    input.PhoneNumber,
		CountryCode:    input.CountryCode,
		Server:         conn.Server,
		ApplicationKey: conn.Token.SecretKey,
		TimeoutInSec:   10,
	}
	marshaledJSON := validateNumber(params)
	jsonOut := map[string]interface{}{}
	err := json.Unmarshal(marshaledJSON, &jsonOut)
	if err == nil {
		output.PhoneInfo = jsonOut
	}
	return output, nil
}

// Test will test the action with the given input over the given connection.
// For this, you should design the output result to be used with the tests in the test/ directory.
// You do not need to / should not need to invoke the actual API, this is just for testing.
func (a *ValidateAction) Test(conn *connection.Connection, input *ValidateInput, log plog.Logger) (*ValidateOutput, error) {
	output := &ValidateOutput{}
	// Your code here
	// NOTE: The input you receive in the test method cannot be gauranteed to contain "good" value.
	// You should not assume the input is something you can trust in this context.

	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}
