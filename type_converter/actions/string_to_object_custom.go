package actions

import (
	"encoding/json"
	"errors"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/type_converter/connection"
)

func isJSON(s string) bool {
	var js map[string]interface{}
	return json.Unmarshal([]byte(s), &js) == nil
}

// Validate will validate the input is properly setup with whatever rules you put in
// You can also use this to pre-set any values before they are run by the Run method.
// Note that for Actions, the  Input message is inspected every time time, just before it
// is handed to the Run method. Keep this in mind when setting any properties on the Input i
// You can return a set of errors for any reason to fail the step.
// Otherwise, return nil for success
func (i *StringToObjectInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)

	// return
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate will validate the output is properly setup with whatever rules you put in
// You can leave this blank if you want to, but if you need to enforce restrictions
// here is where you can return a number of errors. Otherwise, return nil for success
func (o *StringToObjectOutput) Validate(log plog.Logger) []error {
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
func (a *StringToObjectAction) Run(conn *connection.Connection, input *StringToObjectInput, log plog.Logger) (*StringToObjectOutput, error) {
	output := &StringToObjectOutput{}

	if !isJSON(input.Input) {
		return output, errors.New("input string is not valid json")
	}

	rawIn := json.RawMessage(input.Input)
	bytes, err := rawIn.MarshalJSON()
	if err != nil {
		return nil, err
	}

	err = json.Unmarshal(bytes, &output.Output)
	if err != nil {
		return nil, err
	}

	return output, nil
}

// Test will test the action with the given input over the given connection.
// For this, you should design the output result to be used with the tests in the test/ directory.
// You do not need to / should not need to invoke the actual API, this is just for testing.
func (a *StringToObjectAction) Test(conn *connection.Connection, input *StringToObjectInput, log plog.Logger) (*StringToObjectOutput, error) {
	return a.Run(conn, input, log)
}
