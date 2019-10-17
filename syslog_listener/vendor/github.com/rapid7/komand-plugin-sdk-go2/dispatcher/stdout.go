package dispatcher

import (
	"encoding/json"
	"os"
)

// Stdout will dispatch events to stdout
type Stdout struct{}

// NewStdout returns a new Stdout dispatcher
func NewStdout() *Stdout {
	return &Stdout{}
}

// Send dispatches a trigger event
func (d *Stdout) Send(e interface{}) error {
	messageBytes, err := json.Marshal(e)
	if err != nil {
		return err
	}
	_, err = os.Stdout.Write(messageBytes)
	return err
}
