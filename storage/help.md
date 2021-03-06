# Description

This plugin is obsolete. The functionality of this plugin has been superseded with the following product features:

* [Global Artifacts](https://docs.rapid7.com/insightconnect/manage-global-artifacts/)  
* [Custom Loop Variables](https://docs.rapid7.com/insightconnect/loop-step/)  

The Storage plugin is a utility that stores information across loops and workflows. It is intended to make extracting small pieces of information from complicated workflows easier.

This should not be used to store large objects, such as images or entire emails.

# Key Features

* Stores information to be retrieved later

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Store

This action is used to store a variable in cache.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|variable_name|string|None|True|Name of the variable to store|None|
|variable_value|string|None|True|Value of the variable to store|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "success": true
}
```

#### Delete Variable

This action is used to delete a variable and its contents.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|variable_name|string|None|True|Variable to delete|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "success": true
}
```

#### Retrieve

This action is used to retrieve the value of a variable.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|variable_name|string|None|True|Variable to get value from|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|value|string|True|Value|

Example output:

```
{
  "value": "Malicious Email Found"
}
```

#### Check for Variable

This action is used to find out if a variable exists.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|variable_name|string|None|True|Variable to look for|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|variable_found|boolean|True|Was variable found|

```
{
  "variable_found": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

## References
