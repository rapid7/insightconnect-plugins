package actions

import (
	"strconv"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/type_converter/connection"
)

func (i *StringToFloatInput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)

	// Custom validation code here
	// Append errors as needed
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Validate will validate the output is properly setup with whatever rules you put in
// You can leave this blank if you want to, but if you need to enforce restrictions
// here is where you can return a number of errors. Otherwise, return nil for success
func (o *StringToFloatOutput) Validate(log plog.Logger) []error {
	errs := make([]error, 0)
	// Custom validation code here
	// Append errors as needed
	if len(errs) > 0 {
		return errs
	}
	return nil
}

// Run will run the action with the given input over the given connection
func (a *StringToFloatAction) Run(conn *connection.Connection, input *StringToFloatInput, log plog.Logger) (*StringToFloatOutput, error) {
	output := &StringToFloatOutput{}
	s, err := strconv.ParseFloat(input.Input, 64)
	if err != nil {
		log.Error("Float conversion failed.")
		log.Error(err.Error())
		return nil, err
	}
	output.Output = s

	return output, nil
}

// Test will test the action with the given input over the given connection.
// For this, you should design the output result to be used with the tests in the test/ directory.
// You do not need to / should not need to invoke the actual API, this is just for testing.
func (a *StringToFloatAction) Test(conn *connection.Connection, input *StringToFloatInput, log plog.Logger) (*StringToFloatOutput, error) {
	output := &StringToFloatOutput{}
	return output, nil
}
