
# Description

[Statsd](https://github.com/etsy/statsd) is a friendly front-end proxy for the Graphite/Carbon metrics server. The Statsd plugin will allow you to create metrics from your workflow. It will allow you to increment, decrement, and set various metrics.

This plugin utilizes the [Python Statsd](https://statsd.readthedocs.io/en/latest/) library.

# Key Features

* Stores information to be retrieved later

# Requirements

* Host information for your Statsd installation
* Port number of the host
* Prefix information about the metrics to manipulate
* Protocol information

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|udp|maxudpsize|None|False|None|None|
|protocol|string|None|True|Transport Protocol|['UDP', 'TCP']|
|host|string|None|True|Statsd Host|None|
|prefix|string|None|False|Statsd Prefix|None|
|tcp|timeout|None|False|None|None|
|port|integer|None|True|Statsd Port|None|

## Technical Details

### Actions

#### Record Timer

This action is used to this action is used to record timer information.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|stat|string|None|True|The name of the timer to use|None|
|rate|float|None|False|A sample rate e.g. 1. Default is 1|None|
|delta|integer|None|True|The number of milliseconds whatever action took|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|stat|string|True|The name of the used timer|
|delta|integer|False|The number of milliseconds whatever action took|

Example output:

```

{
  "stat": "timingtest",
  "delta": 5
}

```

#### Increment Counter

This action is used to this action is used to increment a counter.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|count|integer|None|False|The amount to increment by e.g. 1. Default is 1|None|
|stat|string|None|True|The name of the counter to increment|None|
|rate|float|None|False|A sample rate e.g. 1. Default is 1|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|stat|string|False|The name of the incremented counter|
|increment|integer|False|The number incremented by|

Example output:

```

{
  "stat": "perstest1",
  "increment": 1
}

```

#### Increment Set

This action is used to this action is used to increment a set value.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|stat|string|None|True|The name of the set to update|None|
|rate|float|None|False|A sample rate e.g. 1. Default is 1|None|
|value|integer|None|True|The unique value to count|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|stat|string|False|The name of the updated set|
|value|integer|False|The unique value to count|

Example output:

```

{
  "stat": "settest",
  "value": 2
}

```

#### Set Gauge

This action is used to this action is used to set a gauge value.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|stat|string|None|True|The name of the gauge to set|None|
|rate|float|None|False|A sample rate e.g. 1. Default is 1|None|
|value|integer|None|True|The current value of the gauge|None|
|delta|boolean|False|False|Whether or not to consider this a delta value or an absolute value|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|stat|string|False|The name of the set gauge|
|value|integer|False|The current value of the gauge|

Example output:

```

{
  "stat": "gaugetest",
  "value": 3
}

```

#### Decrement Counter

This action is used to this action is used to decrement a counter.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|count|integer|None|False|The amount to decrement by e.g. 1. Default is 1|None|
|stat|string|None|True|The name of the counter to decrement|None|
|rate|float|None|False|A sample rate e.g. 1. Default is 1|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|stat|string|True|The name of the decremented counter|
|decrement|integer|False|The number decremented by|

Example output:

```

{
  "stat": "decrtest1",
  "decrement": 1
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### timeout

|Name|Type|Required|Description|
|----|----|--------|-----------|
|timeout|integer|False|TCP timeout|

#### maxudpsize

|Name|Type|Required|Description|
|----|----|--------|-----------|
|maxudpsize|integer|False|Max UDP Size|

## Troubleshooting

The sample `rate` value defaults to 1 if not provided by the user.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to Python v2 architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Statsd](https://github.com/etsy/statsd)
* [Python Statsd](https://statsd.readthedocs.io/en/latest/)