# Description

A simple plugin for testing Orchestrator interactions

# Key Features

Orchestrator testing

# Requirements

* N/A

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|True|No-op credentials used to ensure the end to end experience of communicating with the orchestrator is working|None|

## Technical Details

### Actions

#### Ping

This action is used to send a ping to the Orchestrator and receive a message back.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|message|string|None|True|The message to send, and also what you will receive back|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|The message you'll receive, which is also the same as what was sent|

Example output:

```
{
    "message": "Hello World"
}
```

### Triggers

#### Signal

This trigger is used to send a signal to Insight Connect during startup and shutdown.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|shutdown_message|string|None|True|The message to return to Insight Connect when the Orchestrator shuts down|None|
|startup_message|string|None|True|The message to return to Insight Connect when the Orchestrator starts the trigger|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|The message with the signal, either Startup or Shutdown depending on the event|

Example output:

```
{
    "message": "Hello World"
}
```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.1.6 - Port to Python
* 1.0.0 - Initial plugin

# Links

## References

* N/A
