package actions

import (
	"fmt"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/kafka/connection"
	"github.com/shopify/sarama"
)

// Validate will validate the input is properly setup with whatever rules you put in
// You can also use this to pre-set any values before they are run by the Run method.
// Note that for Actions, the  Input message is inspected every time time, just before it
// is handed to the Run method. Keep this in mind when setting any properties on the Input i
// You can return a set of errors for any reason to fail the step.
// Otherwise, return nil for success
func (i *ProduceAsyncInput) Validate(log plog.Logger) []error {
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
func (o *ProduceAsyncOutput) Validate(log plog.Logger) []error {
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
func (a *ProduceAsyncAction) Run(conn *connection.Connection, input *ProduceAsyncInput, log plog.Logger) (*ProduceAsyncOutput, error) {
	producer, err := sarama.NewAsyncProducerFromClient(conn.CustomParams.Client)
	if err != nil {
		return nil, fmt.Errorf("Failed to create producer for broker %s: %s", conn.BrokerAddress, err.Error())
	}
	defer func() {
		if err := producer.Close(); err != nil {
			log.Errorf("Failed to close producer: %s", err.Error())
		}
	}()

	select {
	case producer.Input() <- &sarama.ProducerMessage{
		Topic: input.Topic,
		Key:   sarama.StringEncoder(input.Key),
		Value: sarama.StringEncoder(input.Message),
	}:
		// Nothing else to do it sent the message to producer Input
	case err := <-producer.Errors():
		return nil, err
	}

	return &ProduceAsyncOutput{}, nil
}

// Test will test the action with the given input over the given connection.
// For this, you should design the output result to be used with the tests in the test/ directory.
// You do not need to / should not need to invoke the actual API, this is just for testing.
func (a *ProduceAsyncAction) Test(conn *connection.Connection, input *ProduceAsyncInput, log plog.Logger) (*ProduceAsyncOutput, error) {
	return a.Run(conn, input, log)
}
