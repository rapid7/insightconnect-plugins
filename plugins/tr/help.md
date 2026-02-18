# Description

The Translate plugin uses the `tr` command in UNIX which is a command line utility for translating or deleting characters. It supports a range of transformations including uppercase to lowercase, squeezing repeating characters, deleting specific characters and basic find and replace. `tr` stands for Translate

# Key Features

* Replace characters in a string
* Delete characters in a string

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* tr (GNU coreutils) 9.7

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Replace

This action is used to run a translate expression on a string input

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expression|string|None|True|Correct tr expression (e.g. -s [:space:] ' ')|None|a-z A-Z|None|None|
|text|string|None|True|Text to process|None|Hello World|None|None|
  
Example input:

```
{
  "expression": "a-z A-Z",
  "text": "Hello World"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|string|True|Processed text|HELLO WORLD|
  
Example output:

```
{
  "result": "HELLO WORLD"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* In case an error is raised, make sure that the given expression can be correctly handled by the `tr` program

# Version History

* 2.0.3 - Updated SDK version to 6.4.3
* 2.0.2 - New spec and help.md format for the Extension Library
* 2.0.1 - Add utilities plugin tag for Marketplace searchability
* 2.0.0 - Rename "Tr" plugin title to "Translate"
* 1.0.0 - Initial plugin

# Links

* [tr examples](https://www.geeksforgeeks.org/tr-command-unixlinux-examples/)

## References

* [tr manual](https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html)