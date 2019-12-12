# Description

The Datetime InsightConnect plugin manipulate timestamps using Python's [Maya](https://pypi.org/project/maya/) library.

# Key Features

* Convert a Datetime to an Epoch and vice versa
* Convert a Datetime to specified format
* Determine the elapsed time between two dates

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Get Datetime

This action is used to get the current Datetime in a specified format.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|format_string|string|%d %b %Y %H\:%M\:%S|True|Format string for the output. Example\: %H\:%M\:%S or %d/%m/%Y|None|
|use_rfc3339_format|boolean|None|True|Use RFC3339 format (eg. 2017-10-24T18\:27\:36.23Z). This is the most compatible date format for timestamp manipulation. Enabling this will override the format string input|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|epoch_timestamp|integer|False|None|
|datetime|string|False|None|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hours|integer|0|True|How many hours to subtract from the specified Datetime|None|
|base_time|date|None|True|Datetime from which to subtract from|None|
|seconds|integer|0|True|How many seconds to subtract from the specified Datetime|None|
|months|integer|0|True|How many months to subtract from the specified Datetime|None|
|minutes|integer|0|True|How many minutes to subtract from the specified Datetime|None|
|days|integer|0|True|How many days to subtract from the specified Datetime|None|
|years|integer|0|True|How many years to subtract from the specified Datetime|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|date|date|False|The Datetime after subtraction|

Example output:

```

{
  "date": "2015-08-13T13:21:10.42Z"
}

```

#### Add to Datetime

This action is used to add Datetime units to a Datetime.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hours|integer|0|True|How many hours to add to the specified Datetime|None|
|base_time|date|None|True|Datetime with which to add to|None|
|seconds|integer|0|True|How many seconds to add to the specified Datetime|None|
|months|integer|0|True|How many months to add to the specified Datetime|None|
|minutes|integer|0|True|How many minutes to add to the specified Datetime|None|
|days|integer|0|True|How many days to add to the specified Datetime|None|
|years|integer|0|True|How many years to add to the specified Datetime|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|date|date|False|The Datetime after addition|

Example output:

```

{
  "date": "2015-08-13T13:21:10.42Z"
}

```

#### Date from Epoch

This action is used to convert an epoch as an integer to a Datetime.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|epoch|number|None|True|Epoch as integer or float|None|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|datetime|date|None|True|Date in RFC3339 format|None|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|first_time|date|None|True|First date|None|
|second_time|date|None|True|Second date|None|
|result_unit|string|'Days'|True|Unit of time for output|['Years', 'Months', 'Days', 'Hours', 'Minutes', 'Seconds']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|difference|int|True|The number of X between dates|
|unit|string|True|Unit of measurement for time|

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

* 2.0.5 - New spec and help.md format for the Hub
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

