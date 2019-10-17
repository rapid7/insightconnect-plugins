# Storage

## About

This utility creates a place to store information across loops and workflows.

## Actions

### Store

This action is used to store a variable in cache.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|variable_name|string|None|True|Name of the variable to store|None|
|variable_value|string|None|True|Name of the variable to store|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "success": true
}
```

### Delete Variable

This action is used to delete a variable and its contents.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|variable_name|string|None|True|Variable to delete|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "success": true
}
```

### Retrieve

This action is used to retrieve the value of a variable.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|variable_name|string|None|True|Variable to get value from|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|value|string|True|Value|

Example output:

```
{
  "value": "Malicious Email Found"
}
```

### Check for Variable

This action is used to find out if a variable exists.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|variable_name|string|None|True|Variable to look for|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|variable_found|boolean|True|Was variable found|

```
{
  "variable_found": true
}
```

## Triggers

_This plugin does not contain any triggers._

## Connection

_This plugin does not contain a connection._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

## Workflows

Examples:

* Create a flag in a loop step, then later check that flag outside the loop
* Count the number of malicious indicators found across workflows

## Versions

* 1.0.0 - Initial plugin

## References

## Custom Output Types

_This plugin does not contain any custom output types._
