# Description

[Sed](https://www.gnu.org/software/sed/manual/sed.html) is a powerful stream editor. This plugin uses GNU Sed 4.2.2 to manipulate input data.
For example, from the command line, an example of the stream editor becomes clear:

```
$ printf 'Cats are enjoyable animals\n' | sed 's/Cats/Dogs/'
Dogs are enjoyable animals
```


# Key Features

* Manipulate input streams and strings

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Process Bytes

This action is used to process bytes of base64 encoded string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|bytes|bytes|None|True|File/bytes to Process|None|b25lIHR3byB0aHJlZSBmb3VyIGZpdmUgb25lIHR3bw==|None|None|
|expression|[]string|None|True|Sed Expression|None|["s/one/ONE/", "s/two/2/g"]|None|None|
|options|string|None|False|Sed Options|None|-r|None|None|
  
Example input:

```
{
  "bytes": "b25lIHR3byB0aHJlZSBmb3VyIGZpdmUgb25lIHR3bw==",
  "expression": [
    "s/one/ONE/",
    "s/two/2/g"
  ],
  "options": "-r"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|output|string|False|Processed String|ONE 2 three four five ONE 2|
  
Example output:

```
{
  "output": "ONE 2 three four five ONE 2"
}
```

#### Process String

This action is used to process string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expression|[]string|None|True|Sed Expression|None|["s/one/ONE/", "s/two/2/g"]|None|None|
|options|string|None|False|Sed Options|None|-r|None|None|
|string|string|None|True|String to Process|None|one two three four five one two|None|None|
  
Example input:

```
{
  "expression": [
    "s/one/ONE/",
    "s/two/2/g"
  ],
  "options": "-r",
  "string": "one two three four five one two"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|output|string|False|Processed String|ONE 2 three four five ONE 2|
  
Example output:

```
{
  "output": "ONE 2 three four five ONE 2"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* Careful attention to the use of double-quotes should be used, the expression will not work if it's surrounded by double-quotes.
If a literal double-quote is required it must be escaped by a backslash `\`. For example:

* `s/\"//g` - A stream editor expression to remove all double-quotes from a string.
* `'s/\"/\'/g'` - A stream editor expression to replace all double-quotes with single-quotes.


# Version History

* 2.0.4 - Refreshed the plugin | Updated SDK to the latest version (6.4.3)
* 2.0.3 - Add action input and output examples to the documentation
* 2.0.2 - New spec and help.md format for the Extension Library | Refactor duplicate code | Remove returning dummy output in connection test | Refactor Exception to PluginException | Changed type in help to be the same as in plugin spec
* 2.0.1 - Fix issue with both actions not returning all results
* 2.0.0 - Update action inputs to allow for multiple expressions
* 1.0.1 - Add `utilities` plugin tag for Marketplace searchability
* 1.0.0 - Support web server mode | Rename action to "Process String"
* 0.1.2 - Update to v2 Python plugin architecture
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Sed](https://www.gnu.org/software/sed/manual/sed.html)

## References

* [Sed](https://www.gnu.org/software/sed/manual/sed.html)