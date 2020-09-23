# Description

Type Converter is a utility plugin for converting data types within a Rapid7 InsightConnect workflow. This is useful
for enabling input interoperability between certain plugins.

# Key Features

* Convert arrays, booleans, integers, numbers, objects, and strings from one type to another to easily retype any variable

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Combine Arrays

This action is used to combine and deduplicate one or more arrays into a larger array.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|array1|[]string|None|True|First array|None|["rapid7", "insight_connect"]|
|array2|[]string|None|True|Second array|None|["rapid7", "insight_connect"]|
|array3|[]string|None|False|Third array|None|["rapid7", "insight_connect"]|
|array4|[]string|None|False|Fourth array|None|["rapid7", "insight_connect"]|
|array5|[]string|None|False|Fifth array|None|["rapid7", "insight_connect"]|

Example input:

```
{
  "array1": [
    "rapid7",
    "insight_connect"
  ],
  "array2": [
    "rapid7",
    "insight_connect"
  ],
  "array3": [
    "rapid7",
    "insight_connect"
  ],
  "array4": [
    "rapid7",
    "insight_connect"
  ],
  "array5": [
    "rapid7",
    "insight_connect"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|combined_array|[]string|True|Combined array|

Example output:

```
{
  "combined_array": [
    "rapid7",
    "insight_connect"
  ]
}

```

#### Array to String

This action converts an array to a string.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|delimiter|string|None|False|Characters used to join an array to a string. Default is a space, if not provided by user|None||
|input|[]string|None|True|Array to convert|None|["hello", "world"]|

Example input:

```
{
  "delimiter": "",
  "input": [
    "hello",
    "world"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|string|True|Joined string|

Example output:

```
{
  "output": "hello world"
}
```

#### Boolean to Integer

This action converts a boolean to an integer. True -> 1, False -> 0.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|input|boolean|None|True|Input variable|None|False|

Example input:

```
{
  "input": false
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|integer|True|Type converted input|

Example output:

```
{
  "output": 0
}
```

#### Boolean to String

This action converts a boolean to a string.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|input|boolean|None|True|Input variable|None|False|

Example input:

```
{
  "input": false
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|string|True|Type converted input|

Example output:

```
{
  "output": "false"
}
```

#### Integer to Boolean

This action converts an integer to a boolean. Non-Zero -> True, 0 -> False.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|input|integer|None|True|Input variable|None|123|

Example input:

```
{
  "input": 123
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|boolean|True|Type converted input|

Example output:

```
{
  "output": true
}
```

#### Integer to Number

This action converts an integer to a number.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|input|integer|None|True|Type converted input|None|123|

Example input:

```
{
  "input": 123
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|number|True|Type converted input|

Example output:

```
{
  "output": 123
}
```

#### Integer to String

This action converts an integer to a string.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|input|integer|None|True|Input variable|None|123|

Example input:

```
{
  "input": 123
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|string|True|Type converted input|

Example output:

```
{
  "output": "123"
}
```

#### Number to Integer

This action converts a number to an integer.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|input|number|None|True|Input variable|None|123|

Example input:

```
{
  "input": 123
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|integer|True|Type converted input|

Example output:

```
{
  "input": 123
}
```

#### Object to String

This action encodes an object to a string.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|input|object|None|True|Input variable|None|{"object":["rapid","7"],"rapid7":"value"}|

Example input:

```
{
  "input": {
    "object": ["rapid", "7"],
    "rapid7": "value"
  }
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|string|True|Type converted input|

Example output:

```
{
  "output": "{\"object\": [\"rapid\", \"7\"], \"rapid7\": \"value\"}"
}
```

#### String to Boolean

This action converts a string to a boolean. Case-insensitive true -> True, else -> False.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|input|string|None|True|Input variable|None|True|

Example input:

```
{
  "input": "true"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|boolean|True|Type converted input|

Example output:

```
{
  "output": true
}
```

#### String to Float

This action converts a string to a float.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|input|string|None|True|Type converted input|None|123.456|

Example input:

```
{
  "input": "123.456"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|float|True|Type converted output|

Example output:

```
{
  "output": 123.456
}
```

#### String to Integer

This action converts a string to an integer.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|input|string|None|True|Input variable|None|123|
|strip|boolean|None|False|Strip whitespace|None|True|

Example input:

```
{
  "input": " 123",
  "strip": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|integer|True|Type converted input|

Example output:

```
{
  "output": 123
}
```

#### String to List

This action converts a string to a list of strings.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|delimiter|string|None|False|Character used to split the string into slices for the list. Default is a newline, if not provided by user|None||
|input|string|None|True|Type converted input|None|Rapid7 Insightconnect|

Example input:

```
{
  "delimiter": "",
  "input": "Rapid7\nInsightconnect"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|[]string|True|Type converted output|

Example output:

```
{
  "output": [
    "Rapid7",
    "Insightconnect"
  ]
}
```

#### String to Object

This action converts a string to an object.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|input|string|None|True|Input variable|None|{"object":["rapid","7"],"rapid7":"value"}|

Example input:

```
{
  "input": "{\"object\":[\"rapid\",\"7\"],\"rapid7\":\"value\"}"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|object|True|Type converted input|

Example output:

```
{
  "output": {
    "object": [
      "rapid",
      "7"
    ],
    "rapid7": "value"
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.6.0 - New action Combine Arrays
* 1.5.2 - Rewrite plugin in Python 3 | Configure as Cloud Plugin
* 1.5.1 - New spec and help.md format for the Extension Library
* 1.5.0 - New action Array to String
* 1.4.1 - Update plugin tag from `util` to `utilities` for Marketplace searchability
* 1.4.0 - New action String to Float
* 1.3.0 - New action String to List
* 1.2.2 - Regenerate with latest Go SDK to solve bug with triggers
* 1.2.0 - Support web server mode
* 1.1.0 - Add action Number->Integer, Integer->Number
* 1.0.0 - Bug fix for int->bool and bool->int
* 0.1.2 - Bug fix for string_to_object action
* 0.1.1 - Bug fix string to int with spaces
* 0.1.0 - Initial plugin

# Links

## References
