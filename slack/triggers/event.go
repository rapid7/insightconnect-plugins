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
)

// EventTriggerCustomLooper is an interface you can implement to override RunLoop behavior
type EventTriggerCustomLooper interface {
	RunLoopCustom(ctx context.Context, conn *connection.Connection, input *EventTriggerInput, log plog.Logger) error
}

// EventTriggerInputSubtypeBotMessage is an enumerated value
const EventTriggerInputSubtypeBotMessage = "bot_message"

// EventTriggerInputSubtypeChannelArchive is an enumerated value
const EventTriggerInputSubtypeChannelArchive = "channel_archive"

// EventTriggerInputSubtypeChannelJoin is an enumerated value
const EventTriggerInputSubtypeChannelJoin = "channel_join"

// EventTriggerInputSubtypeChannelLeave is an enumerated value
const EventTriggerInputSubtypeChannelLeave = "channel_leave"

// EventTriggerInputSubtypeChannelName is an enumerated value
const EventTriggerInputSubtypeChannelName = "channel_name"

// EventTriggerInputSubtypeChannelPurpose is an enumerated value
const EventTriggerInputSubtypeChannelPurpose = "channel_purpose"

// EventTriggerInputSubtypeChannelTopic is an enumerated value
const EventTriggerInputSubtypeChannelTopic = "channel_topic"

// EventTriggerInputSubtypeChannelUnarchive is an enumerated value
const EventTriggerInputSubtypeChannelUnarchive = "channel_unarchive"

// EventTriggerInputSubtypeFileComment is an enumerated value
const EventTriggerInputSubtypeFileComment = "file_comment"

// EventTriggerInputSubtypeFileMention is an enumerated value
const EventTriggerInputSubtypeFileMention = "file_mention"

// EventTriggerInputSubtypeFileShare is an enumerated value
const EventTriggerInputSubtypeFileShare = "file_share"

// EventTriggerInputSubtypeGroupArchive is an enumerated value
const EventTriggerInputSubtypeGroupArchive = "group_archive"

// EventTriggerInputSubtypeGroupJoin is an enumerated value
const EventTriggerInputSubtypeGroupJoin = "group_join"

// EventTriggerInputSubtypeGroupLeave is an enumerated value
const EventTriggerInputSubtypeGroupLeave = "group_leave"

// EventTriggerInputSubtypeGroupName is an enumerated value
const EventTriggerInputSubtypeGroupName = "group_name"

// EventTriggerInputSubtypeGroupPurpose is an enumerated value
const EventTriggerInputSubtypeGroupPurpose = "group_purpose"

// EventTriggerInputSubtypeGroupTopic is an enumerated value
const EventTriggerInputSubtypeGroupTopic = "group_topic"

// EventTriggerInputSubtypeGroupUnarchive is an enumerated value
const EventTriggerInputSubtypeGroupUnarchive = "group_unarchive"

// EventTriggerInputSubtypeMeMessage is an enumerated value
const EventTriggerInputSubtypeMeMessage = "me_message"

// EventTriggerInputSubtypeMessageChanged is an enumerated value
const EventTriggerInputSubtypeMessageChanged = "message_changed"

// EventTriggerInputSubtypeMessageDeleted is an enumerated value
const EventTriggerInputSubtypeMessageDeleted = "message_deleted"

// EventTriggerInputSubtypePinnedItem is an enumerated value
const EventTriggerInputSubtypePinnedItem = "pinned_item"

// EventTriggerInputSubtypeUnpinnedItem is an enumerated value
const EventTriggerInputSubtypeUnpinnedItem = "unpinned_item"

// EventTriggerInput defines the input for the EventTrigger
type EventTriggerInput struct {
	CustomEventTriggerInputParams
	Subtype string `json:"subtype"`
}

// EventTriggerOutput defines the output for the EventTrigger
type EventTriggerOutput struct {
	Event     interface{} `json:"event"`
	Timestamp string      `json:"timestamp"`
}

// EventTrigger a trigger
type EventTrigger struct {
	queue      chan *EventTriggerOutput
	dispatcher dispatcher.Dispatcher
	meta       json.RawMessage
}

// NewEventTrigger returns a new EventTrigger properly initialized and ready to run.
func NewEventTrigger(d dispatcher.Dispatcher, meta json.RawMessage) *EventTrigger {
	return &EventTrigger{
		queue:      make(chan *EventTriggerOutput, 1),
		dispatcher: d,
		meta:       meta,
	}
}

// Send will submit a EventTriggerOutput onto the internal queue, which then buffers to the external queue
func (t *EventTrigger) Send(o interface{}) {
	t.queue <- o.(*EventTriggerOutput)
}

// Stop will close the internal queue, which will prevent new jobs from entering.
func (t *EventTrigger) Stop() {
	close(t.queue)
}

// RunLoop runs the trigger and blocks until the trigger polling is complete or errors. It will block.
// TODO This could be optimized so that the "instant tick" idiom is only used when the ticker is used
// It would take more work but it would be a definite improvement. Also this does mean the first iteration
// of the loop will ignore a cancelletion from the context, but at this time i am willing to accept that tradeoff
// since this helps the more likely case of a message being lost on sudden shutdown.
func (t *EventTrigger) RunLoop(ctx context.Context, conn *connection.Connection, input *EventTriggerInput, log plog.Logger) error {
	// Trigger inputs only get sent in once. Before we event bother with this loop stuff, check it
	// Bail if it's invalid
	var err error
	for _, err = range input.Validate(log) {
		log.Errorf("Error while validating EventTriggerInput: %s\n", err.Error())
	}
	if err != nil {
		return fmt.Errorf("Error while validating EventTriggerInput. Check logs for details")
	}
	// This timer idiom is a bit odd - it is the "instant tick" idiom
	// Basically, i don't need to wait for the first iteration of the timer for it to fire
	// it fires immediately, then every duration thereafter.
	// See: https://www.reddit.com/r/golang/comments/5g0hor/ticker_with_instant_start/daoxqey/
	// You will only see a ticker here if the Trigger defined the "Interval" field, otherwise this is a vanilla for{select{}}
	for {
		output, err := t.Run(conn, input, log)
		if err != nil {
			log.Errorf("Error while running trigger action for EventTrigger: %s\n", err.Error())
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
func (t *EventTrigger) ReadLoop(ctx context.Context, log plog.Logger) error {
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
