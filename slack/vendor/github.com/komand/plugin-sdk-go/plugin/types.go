package plugin

import (
	"errors"

	"github.com/komand/plugin-sdk-go/plugin/message"
)

// Testable must be implemented by a trigger or action if it accepts a test
// If it works, it should emit a sample output event.
type Testable interface {
	Test() (Output, error)
}

// Input defines input parameters
type Input message.Input

// Inputable must be implemented by a trigger or action if it accepts inputs.
type Inputable interface {
	Input() Input
}

// Output structures define output fields for a trigger or action
type Output message.Output

// Outputable must be implemented by a trigger or action if it emits outputs
type Outputable interface {
	Output() Output
}

type queueable interface {
	Send(Output) error
	Read() Output
	InitQueue()
	Stop() error
}

type sendQueue struct {
	queue chan Output
}

// InitQueue inits the queue
func (s *sendQueue) InitQueue() {
	s.queue = make(chan Output, 1)
}

// Send the event
func (s *sendQueue) Send(output Output) error {
	if s.queue != nil {
		s.queue <- output
		return nil
	}

	return errors.New("No queue defined - did you call Init()?")
}

// Stop the queue
func (s *sendQueue) Stop() error {
	if s.queue != nil {
		close(s.queue)
	}
	return nil
}

// Read the queue event
func (s *sendQueue) Read() Output {
	if s.queue != nil {
		return <-s.queue
	}
	return nil
}

// Connection implements a Connect method
type Connection message.Connection

// Connectable is implemented by a trigger or action that has a connection
type Connectable interface {
	Connection() Connection // Connection will return the actual connection to populate
}

type task interface {
	Run() error
	Test() error
}
