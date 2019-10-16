package actions

import (
	"regexp"
	"time"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/extractit/connection"
)

// Validate will validate the input is properly setup with whatever rules you put in
// You can also use this to pre-set any values before they are run by the Run method.
// Note that for Actions, the  Input message is inspected every time time, just before it
// is handed to the Run method. Keep this in mind when setting any properties on the Input i
// You can return a set of errors for any reason to fail the step.
// Otherwise, return nil for success
func (i *DateExtractorInput) Validate(log plog.Logger) []error {
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
func (o *DateExtractorOutput) Validate(log plog.Logger) []error {
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
func (a *DateExtractorAction) Run(conn *connection.Connection, input *DateExtractorInput, log plog.Logger) (*DateExtractorOutput, error) {
	output := &DateExtractorOutput{}
	r := regexp.MustCompile(`\d{1,2}/\d{1,2}/\d{4}`)
	layout := "02/01/2006"
	var err error

	if input.File != nil {
		for _, e := range r.FindAllString(string(input.File), -1) {
			t, er := time.Parse(layout, e)
			output.Dates = append(output.Dates, t)
			err = er
		}
	} else if input.Str != "" {
		for _, e := range r.FindAllString(string(input.Str), -1) {
			t, er := time.Parse(layout, e)
			output.Dates = append(output.Dates, t)
			if er != nil {
				err = er
			}
		}
	} else {
		err = nil
	}
	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure
	return output, err
}

// Test will test the action with the given input over the given connection.
// For this, you should design the output result to be used with the tests in the test/ directory.
// You do not need to / should not need to invoke the actual API, this is just for testing.
func (a *DateExtractorAction) Test(conn *connection.Connection, input *DateExtractorInput, log plog.Logger) (*DateExtractorOutput, error) {
	output := &DateExtractorOutput{}
	// Your code here
	// NOTE: The input you receive in the test method cannot be gauranteed to contain "good" value.
	// You should not assume the input is something you can trust in this context.

	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}
