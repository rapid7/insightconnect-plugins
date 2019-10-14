package triggers

// Code generated by the Komand Go SDK Generator. DO NOT EDIT

import (
	"context"
	"encoding/json"
	"fmt"

	"github.com/rapid7/komand-plugin-sdk-go2/dispatcher"
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugin-sdk-go2/message"

	"github.com/rapid7/komand-plugins/slack/connection"
	"github.com/rapid7/komand-plugins/slack/types"
)

// MessageWithFileTriggerCustomLooper is an interface you can implement to override RunLoop behavior
type MessageWithFileTriggerCustomLooper interface {
	RunLoopCustom(ctx context.Context, conn *connection.Connection, input *MessageWithFileTriggerInput, log plog.Logger) error
}

// MessageWithFileTriggerInput defines the input for the MessageWithFileTrigger
type MessageWithFileTriggerInput struct {
	CustomMessageWithFileTriggerInputParams
	MatchFilename string `json:"match_filename"`
	MatchText     string `json:"match_text"`
}

// MessageWithFileTriggerOutput defines the output for the MessageWithFileTrigger
type MessageWithFileTriggerOutput struct {
	File      types.SDKFile `json:"file"`
	Message   interface{}   `json:"message"`
	Timestamp string        `json:"timestamp"`
	Type      string        `json:"type"`
}

// MessageWithFileTrigger a trigger
type MessageWithFileTrigger struct {
	queue      chan *MessageWithFileTriggerOutput
	dispatcher dispatcher.Dispatcher
	meta       json.RawMessage
}

// NewMessageWithFileTrigger returns a new MessageWithFileTrigger properly initialized and ready to run.
func NewMessageWithFileTrigger(d dispatcher.Dispatcher, meta json.RawMessage) *MessageWithFileTrigger {
	return &MessageWithFileTrigger{
		queue:      make(chan *MessageWithFileTriggerOutput, 1),
		dispatcher: d,
		meta:       meta,
	}
}

// Send will submit a MessageWithFileTriggerOutput onto the internal queue, which then buffers to the external queue
func (t *MessageWithFileTrigger) Send(o interface{}) {
	t.queue <- o.(*MessageWithFileTriggerOutput)
}

// Stop will close the internal queue, which will prevent new jobs from entering.
func (t *MessageWithFileTrigger) Stop() {
	close(t.queue)
}

// RunLoop runs the trigger and blocks until the trigger polling is complete or errors. It will block.
// TODO This could be optimized so that the "instant tick" idiom is only used when the ticker is used
// It would take more work but it would be a definite improvement. Also this does mean the first iteration
// of the loop will ignore a cancelletion from the context, but at this time i am willing to accept that tradeoff
// since this helps the more likely case of a message being lost on sudden shutdown.
func (t *MessageWithFileTrigger) RunLoop(ctx context.Context, conn *connection.Connection, input *MessageWithFileTriggerInput, log plog.Logger) error {
	// Trigger inputs only get sent in once. Before we event bother with this loop stuff, check it
	// Bail if it's invalid
	var err error
	for _, err = range input.Validate(log) {
		log.Errorf("Error while validating MessageWithFileTriggerInput: %s\n", err.Error())
	}
	if err != nil {
		return fmt.Errorf("Error while validating MessageWithFileTriggerInput. Check logs for details")
	}
	// This timer idiom is a bit odd - it is the "instant tick" idiom
	// Basically, i don't need to wait for the first iteration of the timer for it to fire
	// it fires immediately, then every duration thereafter.
	// See: https://www.reddit.com/r/golang/comments/5g0hor/ticker_with_instant_start/daoxqey/
	// You will only see a ticker here if the Trigger defined the "Interval" field, otherwise this is a vanilla for{select{}}
	for {
		output, err := t.Run(conn, input, log)
		if err != nil {
			log.Errorf("Error while running trigger action for MessageWithFileTrigger: %s\n", err.Error())
			continue
		}
		t.Send(output) // Leave this untouched line, it will submit the trigger output to the Komand system.

		select {
		case <-ctx.Done():
			return ctx.Err()
		default:
			// Loop back to the top, polling and submitting another message
			continue
		}
	}
}

// ReadLoop will block, reading until a nil message is received, meaning the internal queue was closed
func (t *MessageWithFileTrigger) ReadLoop(ctx context.Context, log plog.Logger) error {
	for {
		select {
		case output := <-t.queue:
			if output == nil {
				// The channel was closed, we got an empty-closed-read, so we bail out with no issues
				return nil
			}
			response := message.TriggerEvent{
				Type:    "", // We did not set the type in the SDK before, seems to only be for testing or legacy needs
				ID:      "", // We did not set the ID in the SDK before
				GroupID: "", // We did not set the GroupID in the SDK before
				Output:  output,
				Meta:    t.meta, // Copy the incoming meta to pass it along to the outgoing message
			}
			m := message.V1{
				Version: "v1",
				Type:    "trigger_event",
				Body:    &response,
			}
			// Send the message to the komand system
			if err := t.dispatcher.Send(m); err != nil {
				log.Errorf("Receieved error sending trigger message: %s\n", err)
				return err
			}
		case <-ctx.Done():
			// We check this AFTER the queue, because the publish end of this loop needs to stop submitting
			// things to the trigger, then we make sure we've drained that channel, then we can stop.
			// We don't want to quit with a message still in the pipe, lest it be lost.
			// We're done, bailout
			return ctx.Err()
		}
	}
}
