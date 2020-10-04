# Description

Timestamps, timezones, and Datetimes can be difficult to work with, especially when dealing with different locales on different systems. The Datetime InsightConnect plugin manipulates timestamps using Python's [Maya](https://pypi.org/project/maya/) library, which makes the simple things much easier while admitting that time is an illusion (timezones doubly so).

# Key Features

* Convert a Datetime to an Epoch and vice versa
* Convert a Datetime to a specified format
* Determine the elapsed time between two dates
* Convert date from localtime to UTC
* Convert date from UTC to localtime

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### To UTC

This action is used to convert time from localtime to UTC.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|base_time|date|None|True|Datetime to convert, eg. 22 Jul 2020 21:20:33. Milliseconds is not supported|None|22 Jul 2020 21:20:33|
|timezone|string|None|True|Timezone to convert from localtime|None|US/Eastern|

Example input:

```
{
  "base_time": "22 Jul 2020 21:20:33",
  "timezone": "US/Eastern"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|converted_date|date|True|Date in UTC|

Example output:

```
{
  "converted_date": "2020-07-23T01:20:33.0Z"
}

```

#### To Localtime

This action is used to convert time from UTC to localtime.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|base_time|date|None|True|Datetime to convert, eg. 22 Jul 2020 21:20:33. Milliseconds is not supported|None|22 Jul 2020 21:20:33|
|timezone|string|None|True|Timezone to convert from UTC to localtime|None|US/Eastern|

Example input:

```
{
  "base_time": "22 Jul 2020 21:20:33",
  "timezone": "US/Eastern"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|converted_date|date|True|Date in localtime|

Example output:

```
{
  "converted_date": "2020-07-22T17:20:33.0Z"
}
```

#### Get Datetime

This action is used to get the current Datetime in a specified format.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|format_string|string|%d %b %Y %H:%M:%S|True|Format string for the output|None|%d %b %Y %H:%M:%S|
|use_rfc3339_format|boolean|None|True|Use RFC3339 format (eg. 2017-10-24T18:27:36.23Z). This is the most compatible date format for timestamp manipulation. Enabling this will override the format string input|None|True|

Example input:

```
{
  "format_string": "%d %b %Y %H:%M:%S",
  "use_rfc3339_format": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|datetime|string|True|Datetime|
|epoch_timestamp|integer|True|Epoch timestamp|

Example output:

```

{
  "datetime": "2017-10-26T04:04:36.91Z",
  "epoch_timestamp": 1508990676
}

```

#### Subtract from Datetime

This action is used to subtract Datetime units from a Datetime.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|base_time|date|None|True|Datetime from which to subtract from|None|22 Jul 2020 21:20:33|
|days|integer|0|True|How many days to subtract from the specified Datetime|None|0|
|hours|integer|0|True|How many hours to subtract from the specified Datetime|None|0|
|minutes|integer|0|True|How many minutes to subtract from the specified Datetime|None|0|
|months|integer|0|True|How many months to subtract from the specified Datetime|None|0|
|seconds|integer|0|True|How many seconds to subtract from the specified Datetime|None|0|
|years|integer|0|True|How many years to subtract from the specified Datetime|None|0|

Example input:

```
{
  "base_time": "22 Jul 2020 21:20:33",
  "days": 0,
  "hours": 0,
  "minutes": 0,
  "months": 0,
  "seconds": 0,
  "years": 0
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|date|date|True|The Datetime after subtraction|

Example output:

```

{
  "date": "2015-08-13T13:21:10.42Z"
}

```

#### Add to Datetime

This action is used to add Datetime units to a Datetime.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|base_time|date|None|True|Datetime with which to add to|None|22 Jul 2020 21:20:33|
|days|integer|0|True|How many days to add to the specified Datetime|None|0|
|hours|integer|0|True|How many hours to add to the specified Datetime|None|0|
|minutes|integer|0|True|How many minutes to add to the specified Datetime|None|0|
|months|integer|0|True|How many months to add to the specified Datetime|None|0|
|seconds|integer|0|True|How many seconds to add to the specified Datetime|None|0|
|years|integer|0|True|How many years to add to the specified Datetime|None|0|

Example input:

```
{
  "base_time": "22 Jul 2020 21:20:33",
  "days": 0,
  "hours": 0,
  "minutes": 0,
  "months": 0,
  "seconds": 0,
  "years": 0
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|date|date|True|The Datetime after addition|

Example output:

```

{
  "date": "2015-08-13T13:21:10.42Z"
}

```

#### Date from Epoch

This action is used to convert an epoch as an integer to a Datetime.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|epoch|number|None|True|Epoch as integer or float|None|1595452833|

Example input:

```
{
  "epoch": 1595452833
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|date|date|True|Datetime after epoch conversion|

Example output:

```

{
  "date": "2017-11-14T21:07:53.00Z"
}

```

#### Epoch from Date

This action is used to convert a Datetime to an epoch.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|datetime|date|None|True|Date in RFC3339 format|None|22 Jul 2020 21:09:09|

Example input:

```
{
  "datetime": "22 Jul 2020 21:09:09"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|epoch|integer|True|Epoch after conversion|

Example output:

```

{
  "epoch": 1521045250
}

```

#### Time Elapsed

This action is used to find the difference between two Datetime inputs.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|first_time|date|None|True|First date|None|2020-07-22T21:20:33.0Z|
|result_unit|string|None|True|Time unit of measurement for result|['Years', 'Months', 'Days', 'Hours', 'Minutes', 'Seconds']|Years|
|second_time|date|None|True|Second date|None|2022-07-22T21:20:33.0Z|

Example input:

```
{
  "first_time": "2020-07-22T21:20:33.0Z",
  "result_unit": "Years",
  "second_time": "2022-07-22T21:20:33.0Z"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|difference|integer|True|Quantity of time difference|
|time_unit|string|True|Time unit of measurement|

Example output:

```

{
  "difference": 4
  "unit": "Months"
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.1.1 - Update to latest plugin runtime with support for gevent worker class
* 2.1.0 - New actions To UTC and To Localtime
* 2.0.6 - Update to v4 Python plugin runtime 
* 2.0.5 - New spec and help.md format for the Extension Library | Changed const string in params.get to Input constants | Update to use the `komand/python-3-37-slim-plugin:3` Docker image to reduce plugin size
* 2.0.4 - Update plugin tag from `utility` to `utilities` for Marketplace searchability
* 2.0.3 - Fixed issue where connection test failed
* 2.0.2 - Fixed issue where action Date from Epoch will not accept floats
* 2.0.1 - Fixed issue where action Epoch from Date may return a float and not an integer
* 2.0.0 - Bug fix for epoch type
* 1.0.0 - Add action: Time Elapsed | Support web server mode
* 0.5.0 - Add action: Epoch from Date
* 0.4.1 - Bug fix for CI tool incorrectly uploading plugins
* 0.4.0 - Add action: Date from Epoch
* 0.3.1 - SSL bug fix in SDK
* 0.3.0 - Update Get Datetime: Add output for epoch timestamp
* 0.2.1 - Update Get Datetime: Add option to output in RFC3339 format for greater compatibility
* 0.2.0 - Add actions: Add to Datetime, Subtract from Datetime
* 0.1.0 - Initial plugin

# Links

## References

* [Python Time](https://docs.python.org/3/library/time.html#time.strftime)

