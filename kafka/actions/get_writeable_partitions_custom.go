package actions

import (
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/kafka/connection"
)

// Validate will validate the input is properly setup with whatever rules you put in
// You can also use this to pre-set any values before they are run by the Run method.
// Note that for Actions, the  Input message is inspected every time time, just before it
// is handed to the Run method. Keep this in mind when setting any properties on the Input i
// You can return a set of errors for any reason to fail the step.
// Otherwise, return nil for success
func (i *GetWriteablePartitionsInput) Validate(log plog.Logger) []error {
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
func (o *GetWriteablePartitionsOutput) Validate(log plog.Logger) []error {
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
func (a *GetWriteablePartitionsAction) Run(conn *connection.Connection, input *GetWriteablePartitionsInput, log plog.Logger) (*GetWriteablePartitionsOutput, error) {
	ps, err := conn.Client.WritablePartitions(input.Topic)
	if err != nil {
		return &GetWriteablePartitionsOutput{}, err
	}

	// Need to convert everything to int
	partitions := make([]int, len(ps))
	for i, p := range ps {
		partitions[i] = int(p)
	}

	return &GetWriteablePartitionsOutput{
		Partitions: partitions,
	}, nil
}

// Test will test the action with the given input over the given connection.
// For this, you should design the output result to be used with the tests in the test/ directory.
// You do not need to / should not need to invoke the actual API, this is just for testing.
func (a *GetWriteablePartitionsAction) Test(conn *connection.Connection, input *GetWriteablePartitionsInput, log plog.Logger) (*GetWriteablePartitionsOutput, error) {
	return a.Run(conn, input, log)
}
