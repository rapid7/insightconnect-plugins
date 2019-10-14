
# Kafka

## About

Kafka is used for building real-time data pipelines and streaming apps. It is horizontally scalable, fault-tolerant, wicked fast, and runs in production in thousands of companies.

## Actions

### Get Brokers

This action is used to retrieve the current set of active brokers.

#### Input

There is no input for this action.

#### Output

|Name|Type|Required|Description|Enum|
|----|----|--------|-----------|----|
|brokers|[]string|True|List of Kafka broker addresses|None|

### Get Topics

This action is used to retrieve the set of available topics.

#### Input

There is no input for this action.

#### Output

|Name|Type|Required|Description|Enum|
|----|----|--------|-----------|----|
|topics|[]string|True|List of Kafka topics|None|

### Get Partitions

This action is used to retrieve the sorted list of all partition IDs.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic|string|None|True|Topic on which to retrieve partitions|None|

#### Output

|Name|Type|Required|Description|Enum|
|----|----|--------|-----------|----|
|partitions|[]integer|True|List of Kafka partitions|None|

### Get Writeable Partitions

This action is used to retrieve the sorted list of all writeable partition IDs.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic|string|None|True|Topic on which to retrieve partitions|None|

#### Output

|Name|Type|Required|Description|Enum|
|----|----|--------|-----------|----|
|partitions|[]integer|True|List of Kafka partitions|None|

### Get Leader

This action is used to return the broker address that is the leader of the current topic/partition.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic|string|None|True|Topic on which to retrieve the leader|None|
|partition|integer|None|True|Partition on which to retrieve the leader|None|

#### Output

|Name|Type|Required|Description|Enum|
|----|----|--------|-----------|----|
|leader|string|True|Broker address of the leader|None|

### Produce

This action is used to produce messages to a Kafka topic.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic|string|None|True|Kafka topic|None|
|key|string|None|False|Kafka key (required if using Hash Partitioning)|None|
|message|string|None|True|Kafka message|None|

#### Output

|Name|Type|Required|Description|Enum|
|----|----|--------|-----------|----|
|partition|integer|True|Kafka partition ID|None|
|offset|integer|True|Kafka offset|None|

### Produce Async

This action is used to produce messages to a Kafka topic asynchronously. This means
that there will be no output from this step, because it does not wait for a response
from Kafka before continuing.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic|string|None|True|Kafka topic|None|
|key|string|None|False|Kafka key (required if using Hash Partitioning)|None|
|message|string|None|True|Kafka message|None|

#### Output

There is no output for this action.

## Triggers

### Consume

This trigger is used to consume message from a Kafka topic.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic|string|None|True|Kafka Topic|None|
|partition|integer|None|False|Kafka Partition|None|
|offset|integer|0|True|Kafka Partition Offset|None|

#### Output

|Name|Type|Required|Description|Enum|
|----|----|--------|-----------|----|
|message|string|True|Kafka Message|None|

## Connection

The connection for Kafka holds needed information for various actions, if you do not
need to fine tune a certain section, leave the defaults in place. If you want to customize
a producer or consumer, fill out the producer or consumer section, respectively.

Connection Config parameters are mirrors of the config used [here](https://godoc.org/github.com/Shopify/sarama#Config).

|Name|Type|Default|Required|Description|
|----|----|-------|--------|-----------|
|Broker Address|string|None|True|Address of the broker of which to connect|
|Config|Config|(See Config Type)|False|Kafka configuration|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Consume events

## Versions

* 0.1.0 - Initial plugin
* 1.0.0 - Update to v2 architecure | Support web server mode | Semver compliance
* 1.0.1 - Updating to Go SDK 2.6.4
* 1.0.2 - Regenerate with latest Go SDK to solve bug with triggers

## References

* [Kafka](https://kafka.apache.org)
* [Shopify's Go Library for Kafka](https://github.com/Shopify/sarama)
