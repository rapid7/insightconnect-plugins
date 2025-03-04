# Description

Type Converter is a utility plugin for converting data types within a Rapid7 InsightConnect workflow. This is useful for enabling input interoperability between certain plugins

# Key Features

* Convert arrays, booleans, integers, numbers, objects, and strings from one type to another to easily retype any variable

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2024-08-29

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Array Diff

This action is used to difference between two arrays

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|array1|[]string|None|True|First array|None|["rapid7", "insight_connect", "example"]|None|None|
|array2|[]string|None|True|Second array|None|["rapid7", "insight_connect"]|None|None|
  
Example input:

```
{
  "array1": [
    "rapid7",
    "insight_connect",
    "example"
  ],
  "array2": [
    "rapid7",
    "insight_connect"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|difference_array|[]string|True|Difference array|["example"]|
  
Example output:

```
{
  "difference_array": [
    "example"
  ]
}
```

#### Array Match

This action is used to identify matched items present across two arrays

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|array1|[]string|None|True|First array|None|["rapid7", "insight_connect", "example"]|None|None|
|array2|[]string|None|True|Second array|None|["rapid7", "insight_connect"]|None|None|
|deduplicates|boolean|True|False|Set to true to return first matches items, set to false to return all matches|None|True|None|None|
  
Example input:

```
{
  "array1": [
    "rapid7",
    "insight_connect",
    "example"
  ],
  "array2": [
    "rapid7",
    "insight_connect"
  ],
  "deduplicates": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Count of matches|2|
|matches_array|[]string|True|Array containing items found in both the first and second arrays|["rapid7","insight_connect"]|
  
Example output:

```
{
  "count": 2,
  "matches_array": [
    "rapid7",
    "insight_connect"
  ]
}
```

#### Array to String

This action is used to converts an array to a string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|delimiter|string|None|False|Characters used to join an array to a string. Default is a space, if not provided by user|None| |None|None|
|input|[]string|None|True|Array to convert|None|["hello", "world"]|None|None|
  
Example input:

```
{
  "delimiter": " ",
  "input": [
    "hello",
    "world"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|output|string|True|Joined string|hello world|
  
Example output:

```
{
  "output": "hello world"
}
```

#### Boolean to Integer

This action is used to converts a boolean to an integer. True -> 1, False -> 0

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|input|boolean|None|True|Input variable|None|False|None|None|
  
Example input:

```
{
  "input": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|output|integer|True|Type converted input|0|
  
Example output:

```
{
  "output": 0
}
```

#### Boolean to String

This action is used to converts a boolean to a string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|input|boolean|None|True|Input variable|None|False|None|None|
  
Example input:

```
{
  "input": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|output|string|True|Type converted input|false|
  
Example output:

```
{
  "output": false
}
```

#### Combine Arrays

This action is used to combine and deduplicate one or more arrays into a larger array

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|array1|[]string|None|True|First array|None|["rapid7", "insight_connect"]|None|None|
|array2|[]string|None|True|Second array|None|["rapid7", "insight_connect"]|None|None|
|array3|[]string|None|False|Third array|None|["rapid7", "insight_connect"]|None|None|
|array4|[]string|None|False|Fourth array|None|["rapid7", "insight_connect"]|None|None|
|array5|[]string|None|False|Fifth array|None|["rapid7", "insight_connect"]|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|combined_array|[]string|True|Combined array|["rapid7", "insight_connect"]|
  
Example output:

```
{
  "combined_array": [
    "rapid7",
    "insight_connect"
  ]
}
```

#### Integer to Boolean

This action is used to converts an integer to a boolean. Non-Zero -> True, 0 -> False

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|input|integer|None|True|Input variable|None|123|None|None|
  
Example input:

```
{
  "input": 123
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|output|boolean|True|Type converted input|True|
  
Example output:

```
{
  "output": true
}
```

#### Integer to Number

This action is used to converts an integer to a number

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|input|integer|None|True|Type converted input|None|123|None|None|
  
Example input:

```
{
  "input": 123
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|output|number|True|Type converted input|123|
  
Example output:

```
{
  "output": 123
}
```

#### Integer to String

This action is used to converts an integer to a string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|input|integer|None|True|Input variable|None|123|None|None|
  
Example input:

```
{
  "input": 123
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|output|string|True|Type converted input|123|
  
Example output:

```
{
  "output": 123
}
```

#### Number to Integer

This action is used to converts a number to an integer

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|input|number|None|True|Input variable|None|123|None|None|
  
Example input:

```
{
  "input": 123
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|output|integer|True|Type converted input|123|
  
Example output:

```
{
  "output": 123
}
```

#### Object to String

This action is used to encodes an object to a string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|input|object|None|True|Input variable|None|{'object':['rapid','7'],'rapid7':'value'}|None|None|
  
Example input:

```
{
  "input": "{'object':['rapid','7'],'rapid7':'value'}"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|output|string|True|Type converted input|{"object":["rapid", "7"],"rapid7":"value"}|
  
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

#### String to Boolean

This action is used to converts a string to a boolean. Case-insensitive true -> True, else -> False

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|input|string|None|True|Input variable|None|true|None|None|
  
Example input:

```
{
  "input": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|output|boolean|True|Type converted input|True|
  
Example output:

```
{
  "output": true
}
```

#### String to Float

This action is used to converts a string to a float

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|input|string|None|True|Type converted input|None|123.456|None|None|
  
Example input:

```
{
  "input": 123.456
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|output|float|True|Type converted output|123.456|
  
Example output:

```
{
  "output": 123.456
}
```

#### String to Integer

This action is used to converts a string to an integer

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|input|string|None|True|Input variable|None|123|None|None|
|strip|boolean|None|False|Strip whitespace|None|True|None|None|
  
Example input:

```
{
  "input": 123,
  "strip": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|output|integer|True|Type converted input|123|
  
Example output:

```
{
  "output": 123
}
```

#### String to List

This action is used to converts a string to a list of strings

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|delimiter|string|None|False|Character used to split the string into slices for the list. Default is a newline, if not provided by user|None| |None|None|
|input|string|None|True|Type converted input|None|Rapid7 InsightConnect|None|None|
  
Example input:

```
{
  "delimiter": " ",
  "input": "Rapid7 InsightConnect"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|output|[]string|True|Type converted output|["Rapid7", "InsightConnect"]|
  
Example output:

```
{
  "output": [
    "Rapid7",
    "InsightConnect"
  ]
}
```

#### String to Object

This action is used to converts a string to an object

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|input|string|None|True|Input variable|None|{'object':['rapid','7'],'rapid7':'value'}|None|None|
  
Example input:

```
{
  "input": "{'object':['rapid','7'],'rapid7':'value'}"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|output|object|True|Type converted input|{"object":["rapid", "7"],"rapid7":"value"}|
  
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
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.8.4 - Updated SDK to the latest version (6.2.5)
* 1.8.3 - Initial updates for fedramp compliance | Updated SDK to the latest version
* 1.8.2 - Updated error handling for string_to_int & string_to_float
* 1.8.1 - Help.md input examples updated
* 1.8.0 - New action Array Match
* 1.7.0 - New action Array Diff
* 1.6.1 - Add Cloud Enabled tag
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

* [Type Converter](https://extensions.rapid7.com/extension/type-converter)

## References

* [Type Converter](https://extensions.rapid7.com/extension/type-converter)