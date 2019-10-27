// Package cli contains some basic functions, "constants", and helpers for the main
// driver of the plugin
package cli

import (
	"context"
	"encoding/json"
	"os"
	"time"

	"github.com/rapid7/komand-plugin-sdk-go2/dispatcher"
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugin-sdk-go2/message"
	ansi "github.com/mgutz/ansi"
)

// These define various color constants
var (
	Lime  = ansi.ColorCode("green+h:black")
	Red   = ansi.ColorCode("red")
	Green = ansi.ColorCode("green")
	Reset = ansi.ColorCode("reset")
)

// Args represents a simplified set of data passed in from the cli
type Args struct {
	Command     string
	SubCommands []string
	Port        int
}

// HandleShutdown will block on the os.Signal channel, then begin a shutdown procedure
// by signalling the other goroutines via the cancellation context.
func HandleShutdown(cancel context.CancelFunc, c chan os.Signal) {
	<-c
	cancel()
	// Major hack - we should be blocking on a channel or series of channels that say
	// this part of the runtime has shut down, it's ok to proceed, then exit
	// TODO determine if we need 1 or many channels to wait on, pass (it/them) in, and wait
	// before os.Exitting
	time.Sleep(1 * time.Second)
	os.Exit(0)
}

// WrapTriggerTestResult does the boring 1-off work of taking a trigger test output
// and wrapping it in the message envelopes and setting statuses. We only need this
// for triggers tests, since regular triggers submit data with the wrapper in another
// path. Additionally, actions also already wrap their outputs for their own purposes.
// TODO see if there is a simple way to combine all of those to just use this?
func WrapTriggerTestResult(log plog.Logger, o interface{}, err error) *message.V1 {
	l := ""
	if blog, ok := log.(*plog.BufferedLogger); ok {
		l = blog.String()
	}
	response := &message.Response{
		Meta:   []byte(`{}`),
		Output: o,
		Status: "ok",
		Log:    l,
	}
	if err != nil {
		response.Error = err.Error()
		response.Status = "error"
	}
	wrapper := &message.V1{
		Body:    response,
		Type:    "trigger_event",
		Version: "v1",
	}
	return wrapper
}

// DispatcherFromRaw is pretty hacky, not sure if there is a better way but from the engine, it doesn't look
// like we send any kind of "type" flag with the dispatcher... it looks like what we do is default
// to a certain type, and replace it only in certain hardcoded instances. So, the old approach is a pain
// and the new approach is a pain. I'm calling this a lateral change at best until proven otherwise
func DispatcherFromRaw(data json.RawMessage, isDebug bool, mode string) (dispatcher.Dispatcher, error) {
	// No matter what, debug or test always win - and always default to stdout for either of these
	// This design is to maintain compatibility with the older plugins
	if isDebug || mode == "test" {
		return dispatcher.NewStdout(), nil
	}
	// If not debug, try to parse out the HTTP dispatcher data
	m := make(map[string]interface{})
	if err := json.Unmarshal(data, &m); err != nil {
		return nil, err // TODO default to STDOUT here?
	}
	if url, ok := m["url"]; ok { // Komand actually sends 2 values, but we only use this one.
		return dispatcher.NewHTTP(url.(string)), nil
	}
	// If all else fails, fall back to stdout
	return dispatcher.NewStdout(), nil
}
