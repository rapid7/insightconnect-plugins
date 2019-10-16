package connection

import (
	"time"

	"github.com/shopify/sarama"
)

// ConfigFromData creates a new sarama.Config object from the connection data
// TODO: add correct default values
func ConfigFromData(cd *Data) *sarama.Config {
	config := sarama.NewConfig()

	// Net configuration
	config.Net.MaxOpenRequests = cd.Config.Net.MaxOpenRequests
	config.Net.DialTimeout = time.Duration(cd.Config.Net.DialTimeout) * time.Second
	config.Net.ReadTimeout = time.Duration(cd.Config.Net.ReadTimeout) * time.Second
	config.Net.WriteTimeout = time.Duration(cd.Config.Net.WriteTimeout) * time.Second
	config.Net.KeepAlive = time.Duration(cd.Config.Net.KeepAlive) * time.Second

	// Metadata configuration
	config.Metadata.Retry.Max = cd.Config.Metadata.Retry.Max
	config.Metadata.Retry.Backoff = time.Duration(cd.Config.Metadata.Retry.Backoff) * time.Millisecond
	config.Metadata.RefreshFrequency = time.Duration(cd.Config.Metadata.RefreshFrequency) * time.Minute

	// Producer configuration
	config.Producer.MaxMessageBytes = cd.Config.Producer.MaxMessageBytes
	config.Producer.RequiredAcks = NewRequiredAcks(cd.Config.Producer.RequiredAcks)
	config.Producer.Timeout = time.Duration(cd.Config.Producer.Timeout) * time.Second
	config.Producer.Compression = NewCompressionCodec(cd.Config.Producer.Compression)
	config.Producer.Partitioner = NewPartitioner(cd.Config.Producer.Partitioner)

	config.Producer.Flush.Bytes = cd.Config.Producer.Flush.Bytes
	config.Producer.Flush.Messages = cd.Config.Producer.Flush.Messages
	config.Producer.Flush.Frequency = time.Duration(cd.Config.Producer.Flush.Frequency) * time.Minute
	config.Producer.Flush.MaxMessages = cd.Config.Producer.Flush.MaxMessages

	config.Producer.Return.Successes = true
	config.Producer.Retry.Max = cd.Config.Producer.Retry.Max
	config.Producer.Retry.Backoff = time.Duration(cd.Config.Producer.Retry.Backoff) * time.Millisecond

	// Consumer configuration
	config.Consumer.Retry.Backoff = time.Duration(cd.Config.Consumer.Retry.Backoff) * time.Second

	config.Consumer.Fetch.Min = int32(cd.Config.Consumer.Fetch.Min)
	config.Consumer.Fetch.Default = int32(cd.Config.Consumer.Fetch.Default)
	config.Consumer.Fetch.Max = int32(cd.Config.Consumer.Fetch.Max)

	config.Consumer.MaxProcessingTime = time.Duration(cd.Config.Consumer.MaxProcessingTime) * time.Millisecond

	config.ClientID = "komand"

	return config
}

// NewRequiredAcks returns a RequiredAcks for one of our string enums
func NewRequiredAcks(a string) sarama.RequiredAcks {
	switch a {
	case "No Response":
		return sarama.NoResponse
	case "Wait for All":
		return sarama.WaitForAll
	default:
		return sarama.WaitForLocal
	}
}

// NewCompressionCodec returns a CompressionCodec for one of our string enums
func NewCompressionCodec(a string) sarama.CompressionCodec {
	switch a {
	case "GZIP":
		return sarama.CompressionGZIP
	case "Snappy":
		return sarama.CompressionSnappy
	case "LZ4":
		return sarama.CompressionLZ4
	default:
		return sarama.CompressionNone
	}
}

// NewPartitioner returns a PartitionerConstructor for use in deciding partitions
func NewPartitioner(a string) sarama.PartitionerConstructor {
	switch a {
	case "Round Robin Partitioner":
		return sarama.NewRoundRobinPartitioner
	case "Random Partitioner":
		return sarama.NewRandomPartitioner
	default:
		return sarama.NewHashPartitioner
	}
}
