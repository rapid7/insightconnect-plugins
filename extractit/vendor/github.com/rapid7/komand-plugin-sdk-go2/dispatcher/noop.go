package dispatcher

// NOOP will dispatch events to nowhere - it's for testing only
type NOOP struct{}

// NewNOOP returns a new NOOP dispatcher
func NewNOOP() *NOOP {
	return &NOOP{}
}

// Send dispatches a trigger event, except not for NOOP it doesn't
func (d *NOOP) Send(e interface{}) error {
	return nil
}
