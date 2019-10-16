
# Timers

## About

The Timers plugin is an implementation of crond functionality. It allows events to be trigger on a scheduled time interval.

## Actions

### Delay

This action delays a variable number of seconds before resuming.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|delay|float|None|True|How long to delay (in seconds)|None|

#### Output

```
None
```

## Triggers

### Hourly

This trigger is used to create an hourly event with a user specified minute after the hour and an optional message.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|message|string|None|False|(optional) The message to send|None|
|minute|integer|None|False|The minute after the hour to trigger the workflow|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|
|time|string|False|None|

Example output:

```

{
  "message": "The timer went off!"
  "time": ""
}

```

### Every X Minutes

This trigger is used to create a periodic event every *n* minutes with an optional message.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|message|string|None|False|A message to send with the event|None|
|period|float|60|False|Minutes between events|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|
|time|date|False|None|

### Daily

This trigger is used to create a daily event with user supplied times and an optional message.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|message|string|None|False|(optional) The message to send|None|
|times_in_utc|string|None|False|A comma-separated list of UTC times when you want the trigger to occur, e.g. 15\:04,01\:00,5\:00|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|
|time|string|False|None|

### Weekly

This trigger is used to create a weekly event with user supplied day of week and an optional message.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|message|string|None|False|(optional) The message to send|None|
|times_in_utc|string|None|False|A comma-separated list of UTC times on those days when you want the trigger to occur|None|
|day|string|None|False|Names of the day that you want the trigger to run|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|
|time|string|False|None|

### Monthly

This trigger is used to trigger events monthly.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|message|string|None|False|The message to send (optional)|None|
|times_in_utc|string|00\:00|False|UTC times on the day you want the trigger to occur|None|
|day_of_month|integer|None|True|Names of the days that you want the trigger|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|Message|
|time|string|False|Time|

Example output:

```
```

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Scheduling

## Versions

* 1.0.0 - Initial plugin
* 1.1.0 - Support web server mode | Update to v2 Go architecture
* 2.0.0 - Reimplement periodic trigger | Rewrite weekly trigger | Fix double pointer bug in all triggers
* 2.0.1 - Regenerate with latest go sdk to solve bug with actions
* 2.0.2 - Regenerate with latest go sdk to solve bug with triggers

## References

* [Crontab](https://www.freebsd.org/cgi/man.cgi?crontab(5))
