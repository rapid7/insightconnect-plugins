package plugin

// Triggerable must be implemented by a plugin trigger.
type Triggerable interface {
	RunTrigger() error   // RunTrigger will run the trigger.
	Name() string        // Name is the trigger name
	Description() string // Description describes the trigger
}

// Trigger defines a struct that should be embedded within any
// implemented Trigger.
type Trigger struct {
	sendQueue
}

// Send emits an event
func (t *Trigger) Send(event Output) error {
	return t.sendQueue.Send(event)
}
