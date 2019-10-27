// Package dispatcher defines an interface for Dispatchers, which are ways for triggers to emit
// results - either over http, stdout, or to a file
package dispatcher

// Dispatcher is a simple interface over the ability to send data out of the current system and into another
type Dispatcher interface {
	Send(interface{}) error
}
