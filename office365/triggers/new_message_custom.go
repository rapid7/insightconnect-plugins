package triggers

import (
	"context"
	"fmt"
	"time"

	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/office365/connection"
	impl "github.com/rapid7/komand-plugins/office365/implementation" // jh stuff
	"github.com/rapid7/komand-plugins/office365/types"
)

// CustomNewMessageTriggerInputParams contains the state necessary to
// determine if a new message has arrived.
type CustomNewMessageTriggerInputParams struct {
	AtLeastOneMessage bool
	MostRecentMessage types.Message
}

// Validate is a stub because input validation happens in the implementation.
func (i *NewMessageTriggerInput) Validate(log plog.Logger) []error {
	errors := make([]error, 0)
	if len(errors) > 0 {
		return errors
	}
	return nil
}

// Validate is a stub because output validation happens in the implementation.
func (o *NewMessageTriggerOutput) Validate(log plog.Logger) []error {
	errors := make([]error, 0)
	if len(errors) > 0 {
		return errors
	}
	return nil
}

// RunLoopCustom (ctx context.Context, conn *connection.Connection, input *NewMessageTriggerInput, log plog.Logger) error
func (t *NewMessageTrigger) RunLoopCustom(ctx context.Context, conn *connection.Connection, input *NewMessageTriggerInput, log plog.Logger) error {
	// Trigger inputs only get sent in once. Before we event bother with this loop stuff, check it
	// Bail if it's invalid
	var err error
	for _, err = range input.Validate(log) {
		log.Errorf("Error while validating NewMessageTriggerInput: %s\n", err.Error())
	}
	if err != nil {
		return fmt.Errorf("Error while validating NewMessageTriggerInput. Check logs for details")
	}
	// This timer idiom is a bit odd - it is the "instant tick" idiom
	// Basically, i don't need to wait for the first iteration of the timer for it to fire
	// it fires immediately, then every duration thereafter.
	// See: https://www.reddit.com/r/golang/comments/5g0hor/ticker_with_instant_start/daoxqey/
	// You will only see a ticker here if the Trigger defined the "Interval" field, otherwise this is a vanilla for{select{}}
	count := 0

	for tick := time.NewTicker(time.Second * time.Duration(input.Interval)); ; {
		output, err := t.Run(conn, input, log)
		if err != nil {
			log.Errorf("Error while running trigger action for NewMessageTrigger: %s\n", err.Error())
			continue
		}
		if output.NewMessageReceived {
			count++
			t.Send(output)
		}

		select {
		case <-ctx.Done():
			return ctx.Err()
		case <-tick.C:
			// When it ticks, loop back to the top
			continue
		}
	}
}

// Run the new_message trigger.
func (t *NewMessageTrigger) Run(conn *connection.Connection, input *NewMessageTriggerInput, log plog.Logger) (*NewMessageTriggerOutput, error) {
	output := &NewMessageTriggerOutput{}

	haveMessage, message, err := getMostRecentMessageIfAny(conn, input, log)
	if err != nil {
		log.Info("getMostRecentMessageIfAny failed")
		return output, err
	}

	if haveMessage {
		output.NewMessageReceived = haveMessage
		output.MostRecentMessage = message

		input.CustomNewMessageTriggerInputParams.MostRecentMessage = output.MostRecentMessage

		url := conn.CustomParams.API.UsersURL(input.UserIDPrincipal) + "/messages"
		_, err = conn.CustomParams.API.MarkMessageAsRead(url, output.MostRecentMessage.ID)
		if err != nil {
			return nil, err
		}
		if message.HasAttachments {
			attachemtns, _, err := conn.CustomParams.API.GetAttachments(
				input.UserIDPrincipal,
				message.ID,
				impl.DefaultChunkForPagination,
				"",
			)
			if err != nil {
				return output, err
			}
			output.MostRecentMessage.Attachments = attachemtns
		}
		return output, nil
	} else {
		return output, nil
	}
}

func getMostRecentMessageIfAny(conn *connection.Connection, input *NewMessageTriggerInput, log plog.Logger) (bool, types.Message, error) {

	folderID := input.WellKnownFolderID
	if folderID == impl.OtherFolderKey {
		folderID = input.OtherFolderID
	}
	chunk := 1
	continuationToken := ""
	orderBy := "ReceivedDateTime"

	messages, _, err := conn.CustomParams.API.GetMessages(
		input.UserIDPrincipal,
		folderID,
		chunk,
		continuationToken,
		orderBy,
		true,
		log,
	)
	if err != nil {
		return false, types.Message{}, err
	} else if len(messages) <= 0 {
		return false, types.Message{}, err
	}

	for _, msg := range messages {
		if !msg.IsRead {
			return true, msg, nil
		}
	}

	return true, types.Message{}, nil
}

// Test is a stub because the unit tests are in the implementation package (see office365_test.go).
func (t *NewMessageTrigger) Test(conn *connection.Connection, input *NewMessageTriggerInput, log plog.Logger) (*NewMessageTriggerOutput, error) {
	output := &NewMessageTriggerOutput{}
	return output, nil
}
