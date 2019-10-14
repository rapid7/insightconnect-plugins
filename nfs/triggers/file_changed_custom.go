package triggers

import (
	"fmt"
	"time"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/nfs/actions/implementation"
	"github.com/rapid7/komand-plugins/nfs/connection"
)

// CustomFileChangedTriggerInputParams defines any bonus params needed for the trigger run
type CustomFileChangedTriggerInputParams struct {
	// Put any custom parameters that the input might need here
	// For example, since Trigger Inputs only get evaluated one time
	// you could put needed regexes here, then have them set and compiled
	// in the Validate method. This way you won't lose any work when
	// regenerating the plugin, and can still customize the input
}

var curAttrs *implementation.Fattr3

type changedError struct {
	ErrorString string
}

func (err *changedError) Error() string { return err.ErrorString }

// Validate will validate the input is properly setup with whatever rules you put in
// You can also use this to pre-set any values before they are run by the Run method.
// Note that for Triggers, the initial Input message is only inspected one time, at the
// booting up of the Trigger. Keep this in mind when setting any properties on the Input i
// You can return a set of errors for any reason to fail the step.
// Otherwise, return nil for success
func (i *FileChangedTriggerInput) Validate(log plog.Logger) []error {
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
func (o *FileChangedTriggerOutput) Validate(log plog.Logger) []error {
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
func (t *FileChangedTrigger) Run(conn *connection.Connection, input *FileChangedTriggerInput, log plog.Logger) (*FileChangedTriggerOutput, error) {
	config := implementation.NewConfig(
		conn.ClientMachineName,
		conn.ExportsFileHostname,
		conn.ClientExternalIP,
	)
	attrs, err := lookupCurAttrs(conn, input, &config)
	if err != nil {
		ctl := "error while initializing file_changed: %v"
		return nil, &changedError{fmt.Sprintf(ctl, err)}
	}
	curAttrs = attrs

	interval := 60
	if input.Interval != 0 {
		interval = input.Interval
	}
	timeout := implementation.DefaultModifiedTimeoutInSec
	if conn.Timeout != 0 {
		timeout = conn.Timeout
	}

	for {
		output := &FileChangedTriggerOutput{}
		baseFH := conn.BaseFileHandle
		path := input.FilePathname
		diffs, err := implementation.NFSModified(baseFH, path, curAttrs, timeout, &config)
		if err != nil {
			return nil, err
		}
		output.ChangedAttributes = diffs
		t.Send(output)
		time.Sleep(time.Duration(interval) * time.Second)
	}
}

// Test runs the trigger, but does not block and only runs the trigger polling one time
func (t *FileChangedTrigger) Test(conn *connection.Connection, input *FileChangedTriggerInput, log plog.Logger) (*FileChangedTriggerOutput, error) {
	output := &FileChangedTriggerOutput{}
	// Your code here
	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}

func lookupCurAttrs(conn *connection.Connection, input *FileChangedTriggerInput, config *implementation.NFSConfig) (*implementation.Fattr3, error) {
	baseFH := conn.BaseFileHandle
	path := input.FilePathname
	timeout := implementation.DefaultLookupTimeoutInSec
	if conn.Timeout != 0 {
		timeout = conn.Timeout
	}
	volume, err := implementation.NFSLookup(baseFH, path, timeout, config)
	if err == nil {
		return volume.Attrs, nil
	}
	ctl := "error while initializing file_changed: %v"
	return nil, &changedError{fmt.Sprintf(ctl, err)}
}
