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
	"github.com/rapid7/komand-plugins/type_converter/actions"
	"github.com/rapid7/komand-plugins/type_converter/connection"
)

// BooleanToIntegerHandler is a handler
type BooleanToIntegerHandler struct {
	c *connection.Cache
}

// NewBooleanToIntegerHandler returns a new BooleanToIntegerHandler
func NewBooleanToIntegerHandler(c *connection.Cache) *BooleanToIntegerHandler {
	return &BooleanToIntegerHandler{
		c: c,
	}
}

// ServeHTTP handles the requests
func (h *BooleanToIntegerHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	response := &message.Response{
		Meta:   []byte(`{}`),
		Status: "ok",
	}
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
		h.replyWithError(response, w, fmt.Errorf("method %s is unsupported for plugin actions", r.Method))
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
	input := &actions.BooleanToIntegerInput{}
	if err := json.Unmarshal(body.Input, input); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		h.replyWithError(response, w, err)
		return
	}
	// Each request needs a new logger to capture it's output
	// TODO move this to a sync.Pool and grab one from there each time to save on allocs?
	// note to anyone reading this: Do not go adding in sync.Pool without understanding how they
	// work and how to profile to see if adding one will actually make a difference :) It's tricky iirc.
	// Thats why this is a TODO and not a TODONE
	isTest := strings.HasSuffix(r.URL.String(), "test")
	l := plog.NewBufferedLogger(plog.Error)
	if isTest {
		l.SetLevel(plog.Info)
	}
	for _, err = range input.Validate(l) {
		log.Println(fmt.Sprintf("Error while validating BooleanToIntegerInput: %s", err.Error()))
	}
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		h.replyWithError(response, w, fmt.Errorf("Error while validating BooleanToIntegerInput. Check logs for details"))
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

	action := actions.BooleanToIntegerAction{}
	var output *actions.BooleanToIntegerOutput
	if isTest {
		output, err = action.Test(conn, input, l)
	} else {
		output, err = action.Run(conn, input, l)
	}

	if err != nil {
		w.WriteHeader(http.StatusInternalServerError)
		h.replyWithError(response, w, err)
		return
	}
	response.Meta = body.Meta
	response.Log = l.String()
	response.Output = output
	reply := message.V1{
		Type:    "action_event",
		Version: "v1",
		Body:    response,
	}
	b, _ = json.Marshal(reply) // There is nothing we can do if this errs?
	w.WriteHeader(http.StatusOK)
	w.Write(b)
}

// Light wrapper around returning an error with the response object over http
func (h *BooleanToIntegerHandler) replyWithError(response *message.Response, w http.ResponseWriter, err error) {
	response.Error = err.Error()
	response.Status = "error"
	m := &message.V1{
		Body:    response,
		Type:    "action_event",
		Version: "v1",
	}
	b, _ := json.Marshal(m) // There is nothing we can do if this fails?
	w.Write(b)
}
