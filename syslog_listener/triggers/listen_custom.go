package triggers

import (
	"errors"
	"fmt"
	"regexp"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/syslog_listener/connection"
	syslog "gopkg.in/mcuadros/go-syslog.v2"
	"gopkg.in/mcuadros/go-syslog.v2/format"
)

// CustomListenTriggerInputParams defines any bonus params needed for the trigger run
type CustomListenTriggerInputParams struct {
	Facility  string `json:"facility"`
	Filter    string `json:"filter"`
	Level     string `json:"level"`
	Port      int    `json:"port"`
	Transport string `json:"transport"`

	MinLevel int            `json:"-"`
	MsgRegex *regexp.Regexp `json:"-"`
}

var severities = map[int]string{
	-1: "None",
	0:  "EMERG",
	1:  "ALERT",
	2:  "CRIT",
	3:  "ERR",
	4:  "WARNING",
	5:  "NOTICE",
	6:  "INFO",
	7:  "DEBUG",
}

var facilities = map[int]string{
	-1: "None",
	0:  "KERN",
	1:  "USER",
	2:  "MAIL",
	3:  "DAEMON",
	4:  "AUTH",
	5:  "SYSLOG",
	6:  "LPR",
	7:  "NEWS",
	8:  "UUCP",
	15: "CRON",
	10: "AUTHPRIV",
	11: "FTP",
	16: "LOCAL0",
	17: "LOCAL1",
	18: "LOCAL2",
	19: "LOCAL3",
	20: "LOCAL4",
	21: "LOCAL5",
	22: "LOCAL6",
	23: "LOCAL7",
}

// Validate will validate the input is properly setup with whatever rules you put in
// You can also use this to pre-set any values before they are run by the Run method.
// Note that for Triggers, the initial Input message is only inspected one time, at the
// booting up of the Trigger. Keep this in mind when setting any properties on the Input i
// You can return a set of errors for any reason to fail the step.
// Otherwise, return nil for success
func (i *ListenTriggerInput) Validate(log plog.Logger) []error {
	// add logic to validate input here.
	if i.Transport != "TCP" && i.Transport != "UDP" {
		return []error{
			errors.New("Transport must be TCP or UDP"),
		}
	}
	if i.Facility == "None" {
		i.Facility = ""
	}
	if i.Level != "None" {
		for l, name := range severities {
			if name == i.Level {
				i.MinLevel = l
			}
		}
	} else {
		i.Level = ""
	}

	if i.Filter != "" {
		var err error
		i.MsgRegex, err = regexp.Compile(i.Filter)
		if err != nil {
			return []error{err}
		}
	}

	return nil
}

// Validate will validate the output is properly setup with whatever rules you put in
// You can leave this blank if you want to, but if you need to enforce restrictions
// here is where you can return a number of errors. Otherwise, return nil for success
func (o *ListenTriggerOutput) Validate(log plog.Logger) []error {
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
func (t *ListenTrigger) Run(conn *connection.Connection, input *ListenTriggerInput, log plog.Logger) (*ListenTriggerOutput, error) {

	channel := make(syslog.LogPartsChannel)
	handler := syslog.NewChannelHandler(channel)
	server := syslog.NewServer()
	server.SetFormat(syslog.Automatic)
	server.SetHandler(handler)
	if input.Transport == "UDP" {
		server.ListenUDP(fmt.Sprintf("%s:%d", input.Endpoint, input.Port))
	} else {
		server.ListenTCP(fmt.Sprintf("%s:%d", input.Endpoint, input.Port))
	}

	server.Boot()

	log.Infof("Listening: %s:%d %s", input.Endpoint, input.Port, input.Transport)

	go func(channel syslog.LogPartsChannel) {
		for logParts := range channel {
			log.Infof("Received: %+v", logParts)
			out := input.handleInput(logParts, log)
			t.Send(out)
		}
	}(channel)

	server.Wait()
	return nil, nil
}

// Test runs the trigger, but does not block and only runs the trigger polling one time
func (t *ListenTrigger) Test(conn *connection.Connection, input *ListenTriggerInput, log plog.Logger) (*ListenTriggerOutput, error) {
	output := &ListenTriggerOutput{}
	// Your code here
	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}

func (t *ListenTriggerInput) handleInput(logParts format.LogParts, log plog.Logger) *ListenTriggerOutput {
	facility := ""
	severity := ""
	host := ""
	proc := ""
	msg := ""
	msgid := ""
	if f, ok := logParts["facility"]; ok {
		i := f.(int)
		facility = facilities[i]
	}

	if f, ok := logParts["severity"]; ok {
		i := f.(int)
		severity = severities[i]

		if t.Level != "" {
			if i > t.MinLevel {
				// skipping
				return nil
			}
		}
	}

	if h, ok := logParts["hostname"]; ok {
		host = h.(string)
	}
	if h, ok := logParts["proc_id"]; ok {
		proc = h.(string)
	}

	if h, ok := logParts["msg_id"]; ok {
		msgid = h.(string)
	}

	if t.Facility != "" && facility != t.Facility {
		// skipping
		return nil
	}

	if h, ok := logParts["content"]; ok {
		// Should be always be string
		msg = h.(string)
		log.Infof("Found in content key: %s", msg)
	} else if h, ok := logParts["message"]; ok {
		// Should be always be string
		msg = h.(string)
		log.Infof("Found in message key: %s", msg)
	} else {
		return nil
	}

	if t.MsgRegex != nil {
		log.Infof("Supplied regex attempted")
		matched := t.MsgRegex.MatchString(msg)
		if !matched {
			return nil
		}
	}

	output := &ListenTriggerOutput{
		Facility: facility,
		Level:    severity,
		Host:     host,
		Msg:      msg,
		Proc:     proc,
		Msgid:    msgid,
	}

	return output
}
