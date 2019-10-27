
# Type Converter

## About

A simple plugin which performs basic type conversion operations.

## Actions

### Array to String

This action converts an array to a string.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|delimiter|string|None|False|Characters used to join an array to a string. Default is a space, if not provided by user|None|
|input|[]string|None|True|Type converted input|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|string|True|Type converted output|

Example output:

```
{
  "output": "hello world"
}
```

### Object to String

This action is used to encodes an object to a string.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|input|object|None|True|Input variable|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|string|True|Type converted input|

Example Output:

```
{
  "output": "{\"object\":\"example\"}"
}
```

### Boolean to Integer

This action is used to convert a boolean to an integer. True -> 1, False -> 0.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|input|boolean|None|True|Input variable|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|integer|True|Type converted input|

Example Output:

```
{
  "output": 0
}
```

### String to Integer

This action is used to convert a string to an integer.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|input|string|None|True|Input variable|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|integer|True|Type converted input|

Example Output:

```
{
  "output": 123
}
```

### String to Object

This action is used to convert a string to an object.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|input|string|None|True|Input variable|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|object|True|Type converted input|

Example Output:

```
{
  "output": {
    "example": "object"
  }
}
```

### Boolean to String

This action is used to convert a boolean to a string.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|input|boolean|None|True|Input variable|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|string|True|Type converted input|

Example Output:

```
{
  "output": "true"
}
```

### String to Boolean

This action is used to convert a string to a boolean. case-insensitive true -> true, else -> false.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|input|string|None|True|Input variable|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|boolean|True|Type converted input|

Example Output:

```
{
  "output": true
}
```

### Integer to Boolean

This action is used to convert an integer to a boolean. 0 -> false, non-zero -> true

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|input|integer|None|True|Input variable|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|boolean|True|Type converted input|

Example Output:

```
{
  "output": true
}
```

### Integer to String

This action is used to convert an integer to a string.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|input|integer|None|True|Input variable|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|string|True|Type converted input|

Example Output:

```
{
  "output": "123"
}
```

### Number to Integer

This action is used to convert a number to an integer.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|input|number|None|True|Input variable|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|integer|True|Type converted input|

Example Output:

```
{
  "output": 123
}
```

### Integer to Number

This action is used to convert an integer to a number.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|input|integer|None|True|Input variable|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|integer|True|Type converted input|

Example Output:

```
{
  "output": 123
}
```

### String to List

This action is used to convert a string to a list of strings.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|input|string|None|True|Type converted input|None|
|delimiter|string|None|False|Character used to split the string into slices for the list. Default is a newline, if not provided by user|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|[]string|True|Type converted output|

Example output:

```
{
  "output": [
    "This is sentence 1.",
    "This is sentence 2."
  ]
}
```

### String to Float

This action is used to convert a string to a float.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|input|string|None|True|Type converted input|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|float|True|Type converted output|

Example output:

```
{
  "output": 1337.12345
}
```

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - Bug fix string to int with spaces
* 0.1.2 - Bug fix for string_to_object action
* 1.0.0 - Bug fix for int->bool and bool->int
* 1.1.0 - Add action Number->Integer, Integer->Number
* 1.2.0 - Support web server mode
* 1.2.2 - Regenerate with latest Go SDK to solve bug with triggers
* 1.3.0 - New action String to List
* 1.4.0 - New action String to Float
* 1.4.1 - Update plugin tag from `util` to `utilities` for Marketplace searchability
* 1.5.0 - New action Array to String

## Workflows

Examples:

* Convert a boolean to an integer
* Convert a boolean to a string
* Convert an integer to a boolean
* Convert an integer to a string
* Convert a string to a boolean
* Convert a string to an integer
* Convert a string to an object
* Convert an object to a string
* Convert a number to an integer
* Convert an integer to a number
* Convert a string to a list
* Convert an array to a string

## References

* [Type conversion](https://en.wikipedia.org/wiki/Type_conversion)
