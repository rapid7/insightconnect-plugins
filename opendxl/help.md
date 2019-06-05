# OpenDXL

## About

[OpenDXL](https://www.opendxl.com/) is used to create adaptive systems of interconnected services that communicate and share information for real-time, accurate security decisions and actions.
This plugin utilizes the [OpenDXL Python Client API](https://github.com/opendxl/opendxl-client-python).

## Actions

### Publish Event

This action is used to publish a new event to a specified topic.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic|string|None|True|The topic to publish messages to|None|
|event_message|string|None|True|The event message|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Boolean showing whether the event was sent|

Example output:

{
  "success": true
}

## Triggers

### Receive Event

This trigger is used to trigger on receiving a new event from a specified topic.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|topic|string|None|True|The topic to receive messages from|None|
|number_of_messages|integer|1|True|The number of messages to return at one time as a list. Must be one or more|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|messages|[]string|False|Messages found in the subscription|

Example output:

```
{
  "messages": ["test message 1","test message 2","test message 3"]
}
```

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|client_crt|credential_asymmetric_key|None|True|Client certificate file|None|
|host|string|None|True|The broker host e.g. example.com\:8883|None|
|broker_ca|credential_asymmetric_key|None|True|Broker certificate authority bundle|None|
|client_key|credential_asymmetric_key|None|True|Client key file|None|

## Troubleshooting

* If the host input in the plugin connection is not specified then port 8883 will be used by default.

* The `Broker CA`, `Client CRT`, and `Client Key` are all created with the OpenDXL UI.

* The 3 files will be downloaded when created and are named `ca-broker.crt`, `client.crt`, and `client.key` respectively.

* All certificates must end with a '\n' when copying the certificate, please ensure that the ending '\n' is included.

## Versions

* 1.0.0 - Initial plugin
* 1.1.0 - New action Publish Event
* 1.1.1 - Fix issue where certificates in connection were not being escaped correctly

## Workflows

Examples:

* Pull new messages from an OpenDXL topic

## References

* [OpenDXL](https://www.opendxl.com/)
* [API documentation](https://opendxl.github.io/opendxl-client-python/pydoc/index.html#)
