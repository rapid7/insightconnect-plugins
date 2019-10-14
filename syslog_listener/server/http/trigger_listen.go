package http

// Code generated by the Komand Go SDK Generator. DO NOT EDIT

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strings"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugin-sdk-go2/message"
	"github.com/rapid7/komand-plugins/syslog_listener/connection"
	"github.com/rapid7/komand-plugins/syslog_listener/triggers"
)

// ListenTriggerHandler is a handler
type ListenTriggerHandler struct {
	c *connection.Cache
}

// NewListenTriggerHandler returns a new ListenHandler
func NewListenTriggerHandler(c *connection.Cache) *ListenTriggerHandler {
	return &ListenTriggerHandler{
		c: c,
	}
}

// ServeHTTP handles the requests
func (h *ListenTriggerHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	response := &message.TriggerEvent{}
	b, err := ioutil.ReadAll(r.Body)
	// TODO use a limit reader to prevent resource attacks?
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		h.replyWithError(response, w, err)
		return
	}
	r.Body.Close()
	if r.Method != "POST" {
		w.WriteHeader(http.StatusMethodNotAllowed)
		h.replyWithError(response, w, fmt.Errorf("method %s is unsupported for plugin triggers", r.Method))
		return
	}
	body := &message.BodyV1{}
	m := &message.V1{
		Body: &body,
	}
	if err := json.Unmarshal(b, m); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		h.replyWithError(response, w, err)
		return
	}
	// Unmarshal the body into the right struct
	// We could avoid the 2 excess json marshal calls in here with a lot of switch-casing on types
	// but in this case, the performance gain is not that great, and it's less generator code to maintain
	// to do it this way.
	// TODO if we suspect this is a bottleneck, profile it and swap back to the switch-case approach
	input := &triggers.ListenTriggerInput{}
	if err := json.Unmarshal(body.Input, input); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		h.replyWithError(response, w, err)
		return
	}
	// Grab the Meta from the incoming data to send to the output as well
	if err := json.Unmarshal(body.Meta, &response.Meta); err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		h.replyWithError(response, w, err)
		return
	}
	// Each request needs a new logger to capture it's output
	// TODO move this to a sync.Pool and grab one from there each time to save on allocs?
	// note to anyone reading this: Do not go adding in sync.Pool without understanding how they
	// work and how to profile to see if adding one will actually make a difference :) It's tricky iirc.
	// Thats why this is a TODO and not a TODONE
	l := plog.NewBufferedLogger(plog.Info)
	for _, err = range input.Validate(l) {
		log.Println(fmt.Sprintf("Error while validating ListenInput: %s", err.Error()))
	}
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		h.replyWithError(response, w, fmt.Errorf("Error while validating ListenInput. Check logs for details"))
		return
	}
	cd := &connection.Data{}
	if err := json.Unmarshal(body.Connection, cd); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		h.replyWithError(response, w, err)
		return
	}

	conn, err := h.c.Get(cd, l)
	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		response.Log = l.String()
		h.replyWithError(response, w, err)
		return
	}

	// We initialize with a nil dispatcher because we do not want to dispatch events on test
	trigger := triggers.NewListenTrigger(nil, response.Meta)
	var output *triggers.ListenTriggerOutput
	if strings.HasSuffix(r.URL.String(), "test") {
		output, err = trigger.Test(conn, input, l)
	} else {
		// Triggers can ONLY be tested via proxy, never invoked
		w.WriteHeader(http.StatusBadRequest)
		h.replyWithError(response, w, err)
		return
	}

	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		h.replyWithError(response, w, err)
		return
	}
	response.Log = l.String()
	response.Output = output
	reply := message.V1{
		Type:    "trigger_event",
		Version: "v1",
		Body:    response,
	}
	b, _ = json.Marshal(reply) // There is nothing we can do if this errs?
	w.WriteHeader(http.StatusOK)
	w.Write(b)
}

// Light wrapper around returning an error with the response object over http
func (h *ListenTriggerHandler) replyWithError(response *message.TriggerEvent, w http.ResponseWriter, err error) {
	response.Error = err.Error()
	response.Status = "error"
	m := &message.V1{
		Body:    response,
		Type:    "trigger_event",
		Version: "v1",
	}
	b, _ := json.Marshal(m) // There is nothing we can do if this fails?
	w.Write(b)
}
