package triggers

import (
	"time"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/timers/connection"
)

// CustomHourlyTriggerInputParams defines any bonus params needed for the trigger run
type CustomHourlyTriggerInputParams struct {
	// Put any custom parameters that the input might need here
	// For example, since Trigger Inputs only get evaluated one time
	// you could put needed regexes here, then have them set and compiled
	// in the Validate method. This way you won't lose any work when
	// regenerating the plugin, and can still customize the input
}

//Minutes makes integers into minutes
func (i *HourlyTriggerInput) Minutes() []int {
	return []int{i.Minute}
}

// Validate will validate the input is properly setup with whatever rules you put in
// You can also use this to pre-set any values before they are run by the Run method.
// Note that for Triggers, the initial Input message is only inspected one time, at the
// booting up of the Trigger. Keep this in mind when setting any properties on the Input i
// You can return a set of errors for any reason to fail the step.
// Otherwise, return nil for success
func (i *HourlyTriggerInput) Validate(log plog.Logger) []error {
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
func (o *HourlyTriggerOutput) Validate(log plog.Logger) []error {
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
func (t *HourlyTrigger) Run(conn *connection.Connection, input *HourlyTriggerInput, log plog.Logger) (*HourlyTriggerOutput, error) {
	output := &HourlyTriggerOutput{}

	times := make([]time.Time, len(input.Minutes()))
	for i, offset := range input.Minutes() {
		times[i] = times[i].Add(time.Duration(offset) * time.Minute)
	}

	output.Message = input.Message
	for {
		sleepUntilNextTime(times, hourlyPeriod)
		output.Time = time.Now().String()
		t.Send(output)
	}
}

// Test runs the trigger, but does not block and only runs the trigger polling one time
func (t *HourlyTrigger) Test(conn *connection.Connection, input *HourlyTriggerInput, log plog.Logger) (*HourlyTriggerOutput, error) {
	output := &HourlyTriggerOutput{}
	// Your code here
	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}
