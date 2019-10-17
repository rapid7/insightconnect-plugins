package triggers

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/slack/connection"
)

// CustomEventTriggerInputParams defines any bonus params needed for the trigger run
type CustomEventTriggerInputParams struct {
	// Put any custom parameters that the input might need here
	// For example, since Trigger Inputs only get evaluated one time
	// you could put needed regexes here, then have them set and compiled
	// in the Validate method. This way you won't lose any work when
	// regenerating the plugin, and can still customize the input
}

// Validate will validate the input is properly setup with whatever rules you put in
// You can also use this to pre-set any values before they are run by the Run method.
// Note that for Triggers, the initial Input message is only inspected one time, at the
// booting up of the Trigger. Keep this in mind when setting any properties on the Input i
// You can return a set of errors for any reason to fail the step.
// Otherwise, return nil for success
func (i *EventTriggerInput) Validate(log plog.Logger) []error {
	errors := make([]error, 0)

	// Custom validation code here
	// Append errors as needed

	// return
	if len(errors) > 0 {
		return errors
	}
	return nil
}

// Validate will validate the output is properly setup with whatever rules you put in
// You can leave this blank if you want to, but if you need to enforce restrictions
// here is where you can return a number of errors. Otherwise, return nil for success
func (o *EventTriggerOutput) Validate(log plog.Logger) []error {
	errors := make([]error, 0)

	// Custom validation code here
	// Append errors as needed

	// return
	if len(errors) > 0 {
		return errors
	}
	return nil
}

// Run runs the trigger, but does not blocks and only runs the trigger polling one time
// It is intended to be called from inside of a loop, which handles submitting the results
// and keeping track of when to call this method.
func (t *EventTrigger) Run(conn *connection.Connection, input *EventTriggerInput, log plog.Logger) (*EventTriggerOutput, error) {
	output := &EventTriggerOutput{}
	// Your code here
	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}

// Test runs the trigger, but does not block and only runs the trigger polling one time
func (t *EventTrigger) Test(conn *connection.Connection, input *EventTriggerInput, log plog.Logger) (*EventTriggerOutput, error) {
	output := &EventTriggerOutput{}
	// Your code here
	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}
