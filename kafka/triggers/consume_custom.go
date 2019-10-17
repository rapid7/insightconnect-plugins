package triggers

import (
	"bufio"
	"context"
	"fmt"
	"io"
	"strconv"
	"time"

	"github.com/rapid7/komand-plugin-sdk-go2/cache"
	plog "github.com/rapid7/komand-plugin-sdk-go2/log"
	"github.com/rapid7/komand-plugins/kafka/connection"
	sarama "github.com/shopify/sarama"
)

// CustomConsumeTriggerInputParams defines any bonus params needed for the trigger run
type CustomConsumeTriggerInputParams struct {
	// Put any custom parameters that the input might need here
	// For example, since Trigger Inputs only get evaluated one time
	// you could put needed regexes here, then have them set and compiled
	// in the Validate method. This way you won't lose any work when
	// regenerating the plugin, and can still customize the input
	CacheFileName string
}

// CustomLooper is an interface you can implement to override RunLoop behavior
type CustomLooper interface {
	RunLoopCustom(ctx context.Context, conn *connection.Connection, input *ConsumeTriggerInput, log plog.Logger) error
}

// Validate will validate the input is properly setup with whatever rules you put in
// You can also use this to pre-set any values before they are run by the Run method.
// Note that for Triggers, the initial Input message is only inspected one time, at the
// booting up of the Trigger. Keep this in mind when setting any properties on the Input i
// You can return a set of errors for any reason to fail the step.
// Otherwise, return nil for success
func (i *ConsumeTriggerInput) Validate(log plog.Logger) []error {
	errors := make([]error, 0)

	// Custom validation code here
	// Append errors as needed

	// return
	if len(errors) > 0 {
		return errors
	}
	return nil
}

// Validate will validate the output is properly setup with whatever rules you put in
// You can leave this blank if you want to, but if you need to enforce restrictions
// here is where you can return a number of errors. Otherwise, return nil for success
func (o *ConsumeTriggerOutput) Validate(log plog.Logger) []error {
	errors := make([]error, 0)

	// Custom validation code here
	// Append errors as needed

	// return
	if len(errors) > 0 {
		return errors
	}
	return nil
}

// RunLoopCustom overrides the RunLoop behavior in consume.go
// Run was removed from this file since it is not used for this trigger
func (t *ConsumeTrigger) RunLoopCustom(ctx context.Context, conn *connection.Connection, input *ConsumeTriggerInput, log plog.Logger) error {
	// Trigger inputs only get sent in once. Before we event bother with this loop stuff, check it
	// Bail if it's invalid
	var err error
	for _, err = range input.Validate(log) {
		log.Errorf(fmt.Sprintf("Error while validating ConsumeTriggerInput: %s", err.Error()))
	}
	if err != nil {
		return fmt.Errorf("Error while validating ConsumeTriggerInput. Check logs for details")
	}

	partitionList, err := conn.Client.Partitions(input.Topic) //get all partitions on the given topic
	if err != nil {
		return fmt.Errorf("Error retrieving partitionList: %s", err.Error())
	}

	consumer, err := sarama.NewConsumerFromClient(conn.Client)
	if err != nil {
		return fmt.Errorf("Error while creating Kafka consumer: %s", err.Error())
	}

	// In memory tracker of offset so we can write out on error
	var currentOffset int64

	messages := make(chan *sarama.ConsumerMessage, 1)
	// Loop over partitions, listen on messages for each
	for _, partition := range partitionList {
		cacheFileName := fmt.Sprintf("triggers_kafka_high_watermark_offset-%s-%d-%d", input.Topic, partition, currentOffset)
		offset, err := t.getOffset(cacheFileName, input)
		if err != nil {
			return fmt.Errorf("Failed to get Kafka offset: %s", err.Error())
		}

		pc, err := consumer.ConsumePartition(input.Topic, partition, offset)
		if err != nil {
			return fmt.Errorf("Error consuming topic %s on partition %d with offset %d: %s", input.Topic, partition, offset, err.Error())
		}

		defer func() {
			if err := pc.Close(); err != nil {
				log.Errorf("Failed to close partition consumer: %s", err.Error())
			}
		}()

		go func() {
			// Listen on this particular partition consumer's message channel,
			// and send them to the internal one to be dispatched
			for {
				select {
				case <-ctx.Done():
					if err := t.writeOffset(cacheFileName, pc.HighWaterMarkOffset()); err != nil {
						log.Errorf("Failed to write offset to %s cache file: %s", input.CustomConsumeTriggerInputParams.CacheFileName, err.Error())
					}
					return
				case message := <-pc.Messages():
					messages <- message
					currentOffset = message.Offset
				default:
					continue
				}
			}
		}()
	}

	for {
		select {
		case message := <-messages:
			t.Send(&ConsumeTriggerOutput{
				Message: string(message.Value),
			})
		case <-ctx.Done():
			return ctx.Err()
		default:
			continue
		}
	}
}

// Run runs the trigger, but does not blocks and only runs the trigger polling one time
// It is intended to be called from inside of a loop, which handles submitting the results
// and keeping track of when to call this method.
func (t *ConsumeTrigger) Run(conn *connection.Connection, input *ConsumeTriggerInput, log plog.Logger) (*ConsumeTriggerOutput, error) {
	output := &ConsumeTriggerOutput{}
	// Your code here
	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}

// Test runs the trigger, but does not block and only runs the trigger polling one time
func (t *ConsumeTrigger) Test(conn *connection.Connection, input *ConsumeTriggerInput, log plog.Logger) (*ConsumeTriggerOutput, error) {
	output := &ConsumeTriggerOutput{}
	// Your code here
	// Use the `log` object passed into the Connect method and any logging information
	// will be returned with the message in the log field. Otherwise, it will be discarded.

	// return output and no error for success
	// return nil and error for failure

	return output, nil
}

func (t *ConsumeTrigger) writeOffset(filename string, offset int64) error {
	// Try to lock the cache`
	ok, err := cache.LockCacheFile(filename)
	// If there is an error, it fails hard - shouldn't be an error
	if err != nil {
		return fmt.Errorf("Failed to lock %s cache file: %s", filename, err.Error())
	}
	// If we got the lock, then pretend to do some work and unlock it
	if ok {
		file, err := cache.OpenCacheFile(filename)
		if err != nil {
			return fmt.Errorf("Error reading from %s cache file: %s", filename, err.Error())
		}

		fw := bufio.NewWriter(file)
		if _, err = fw.WriteString(string(offset)); err != nil {
			return err
		}
		if err := file.Close(); err != nil {
			return fmt.Errorf("Failed to close %s cache file: %s", filename, err.Error())
		}

		timeout := 1 * time.Millisecond
		cache.UnlockCacheFile(filename, &timeout)
	}
	return nil
}

// getOffset uses the sarama.OffsetOldest as the first fallback,
// if the user specifies an offset it will use it first, except if
// it reads an offset from the cache file, so that it picks up where
// it left off if it happened to fail
func (t *ConsumeTrigger) getOffset(filename string, input *ConsumeTriggerInput) (int64, error) {

	offset := sarama.OffsetOldest //get offset for the oldest message on the topic
	if input.Offset >= 0 {
		offset = int64(input.Offset)
	}

	ok, err := cache.LockCacheFile(filename)
	if err != nil {
		return 0, fmt.Errorf("Error locking %s cache file: %s", filename, err.Error())
	}
	if ok {
		file, err := cache.OpenCacheFile(filename)
		if err != nil {
			return 0, fmt.Errorf("Error opening %s cache file: %s", filename, err.Error())
		}

		fr := bufio.NewReader(file)
		line, _, err := fr.ReadLine()
		if err != nil {
			if err != io.EOF {
				fmt.Println("Got into readline error")
				return 0, fmt.Errorf("Error reading line %s cache file: %s", filename, err.Error())
			}
		}
		if err := file.Close(); err != nil {
			return 0, fmt.Errorf("Error closing %s cache file: %s", filename, err.Error())
		}

		// Fall back to configured value if we can't convert this offset properly
		oi, _ := strconv.Atoi(string(line)) // ignore this error because we make sure the offset is set
		offset = int64(oi)
		if offset < 0 {
			offset = int64(input.Offset)
		}
		timeout := time.Millisecond * 1
		cache.UnlockCacheFile(filename, &timeout)
	}

	return offset, nil
}
