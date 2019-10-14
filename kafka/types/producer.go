package types

// Code generated by the Komand Go SDK Generator. DO NOT EDIT

// Enumerated values for Compression
const (
	ProducerCompressionNone   = "None"
	ProducerCompressionGZIP   = "GZIP"
	ProducerCompressionSnappy = "Snappy"
	ProducerCompressionLZ4    = "LZ4"
)

// Enumerated values for Partitioner
const (
	ProducerPartitionerHashPartitioner       = "Hash Partitioner"
	ProducerPartitionerRoundRobinPartitioner = "Round Robin Partitioner"
	ProducerPartitionerRandomPartitioner     = "Random Partitioner"
)

// Enumerated values for RequiredAcks
const (
	ProducerRequiredAcksNoResponse   = "No Response"
	ProducerRequiredAcksWaitForLocal = "Wait for Local"
	ProducerRequiredAcksWaitForAll   = "Wait for All"
)

// Producer is a custom type generated off of the spec
type Producer struct {
	Compression     string        `json:"compression"`
	Partitioner     string        `json:"partitioner"`
	Flush           Flush         `json:"flush"`
	Retry           ProducerRetry `json:"retry"`
	MaxMessageBytes int           `json:"max_message_bytes"`
	RequiredAcks    string        `json:"required_acks"`
	Timeout         int           `json:"timeout"`
}
