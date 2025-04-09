# Description

The String Operations plugin allows easy manipulation of string data.
 
This plugin utilizes the Python 3 String library [set of methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

# Key Features

* Split a string to a list of elements
* Split a string to an object
* Upper case, lower case, and trim a string
* Replace parts of a string

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2024-09-06

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Length

This action is used to return the length of a string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|string|string|None|True|String to return length of|None|return the number of characters in this string|None|None|
  
Example input:

```
{
  "string": "return the number of characters in this string"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|length|integer|True|Length of string|46|
  
Example output:

```
{
  "length": 46
}
```

#### Lower

This action is used to converts uppercase letters to lowercase

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|string|string|None|True|String to convert e.g. USER=bob|None|LOWERCASE THIS STRING|None|None|
  
Example input:

```
{
  "string": "LOWERCASE THIS STRING"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|lower|string|False|Lowercase string|lowercase this string|
  
Example output:

```
{
  "lower": "lowercase this string"
}
```

#### Replace

This action is used to replace parts of a string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|in_string|string|None|True|The string to replace parts of|None|this is a string|None|None|
|replacement_value|string|None|False|The string that will replace the parts that are found. If left blank the characters to find will be deleted|None|replacement|None|None|
|string_part_to_find|string|None|True|The string part to look for. All instances of this string will be replaced|None|string|None|None|
  
Example input:

```
{
  "in_string": "this is a string",
  "replacement_value": "replacement",
  "string_part_to_find": "string"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result_string|string|True|The string after replacement|this is a replacement|
  
Example output:

```
{
  "result_string": "this is a replacement"
}
```

#### Set Encoding

This action is used to encode a string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|encoding|string|None|True|Encoding to use|["UTF-8", "ASCII"]|ASCII|None|None|
|error_handling|string|None|True|Error handler to use for encoding and decoding|["strict", "replace", "ignore"]|ignore|None|None|
|string|string|None|True|String to encode|None|hello|None|None|
  
Example input:

```
{
  "encoding": "ASCII",
  "error_handling": "ignore",
  "string": "hello"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|encoded|string|True|Encoded string|hello|
  
Example output:

```
{
  "encoded": "hello"
}
```

#### Split String to List

This action is used to converts a string to a list of strings

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|delimiter|string|None|False|The character used to split the string into slices for the list. The default is a newline, if not provided by the user|None|,|None|None|
|string|string|None|True|String to break into an array|None|This,is,a,sentence|None|None|
  
Example input:

```
{
  "delimiter": ",",
  "string": "This,is,a,sentence"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|list|[]string|False|List of string components|["This", "is", "a", "sentence"]|
  
Example output:

```
{
  "list": [
    "This",
    "is",
    "a",
    "sentence"
  ]
}
```

#### Split String to Object
  
This action is used to convert a string to an object containing key:value strings.

Any input requiring more than a 
single key:value pair, e.g. `USER=Bob` needs to use the `block_delimiter` option. In this case, the input string is 
split by the `block_delimiter` character first, and the resulting items are then split by the `string_delimiter` option.
 Stripping of double-quotes is automatically applied in this situation for each item before the plugin returns it.

The 
[output object](https://docs.komand.com/v0.42.1/docs/python-script-plugins#section-configure-the-plugin-output-schema) 
on the action's page can be modified to pre-populate the workflow with the names of the keys. It allows users the 
ability to use the green selector and choose a specific variable later in the workflow by name. [Input 
templating](https://docs.komand.com/docs/input-templating) would need to be used to obtain variables by name otherwise.


Please refer to troubleshooting section for a more complex example

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|block_delimiter|string|None|False|The character delimiter for the initial string split, applied before the string delimiter input. This parameter is optional but allows for more complex handling|None|[|None|None|
|string|string|None|True|String to convert e.g. USER=Bob|None|User=Bob|None|None|
|string_delimiter|string|None|False|The character used to split the string into slices for the list. The default is a space, if not provided by the user|None|=|None|None|
  
Example input:

```
{
  "block_delimiter": "[",
  "string": "User=Bob",
  "string_delimiter": "="
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|object|object|False|Object from string split|{"User":"Bob"}|
  
Example output:

```
{
  "object": {
    "User": "Bob"
  }
}
```

#### Trim

This action is used to trim a string of leading and trailing whitespace

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|string|string|None|True|String to trim|None|Extra spaces at the end of this string     |None|None|
  
Example input:

```
{
  "string": "Extra spaces at the end of this string     "
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|trimmed|string|True|Trimmed string|Extra spaces at the end of this string|
  
Example output:

```
{
  "trimmed": "Extra spaces at the end of this string"
}
```

#### Upper

This action is used to converts lowercase letters to uppercase

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|string|string|None|True|String to uppercase|None|uppercase this string|None|None|
  
Example input:

```
{
  "string": "uppercase this string"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|upper|string|False|Uppercase string|UPPERCASE THIS STRING|
  
Example output:

```
{
  "upper": "UPPERCASE THIS STRING"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* `Split String to Object`: if the input contains multiple key:value pairs and these pairs are separated from each other by a space, and the keys and values within each pair are separated by an equal sign we can follow the below example:

  + Example text: `Computer_ID="bef41e8b-47b8-e188-8e43-3a2b662dd55d" Computer_Name="dgdemo\RGWin64" Computer_Type="Windows"`
  + Example Input: `{"block_delimiter": " ","string":
"Computer_ID="bef41e8b-47b8-e188-8e43-3a2b662dd55d" Computer_Name="dgdemo RGWin64" Computer_Type="Windows","string_delimiter": "="}`
  + Example output: `{ "object": { "Computer_ID": "bef41e8b-47b8-e188-8e43-3a2b662dd55d", "Computer_Name": "dgdemo RGWin64", "Computer_Type": "Windows" } }`


* There may be complex string manipulation needs that are likely outside the scope of this plugin. If this is the case, consider using the Python 3 Script plugin instead.

# Version History

* 1.4.4 - Updated SDK to the latest version (6.3.3)
* 1.4.3 - Updated SDK to the latest version (6.2.5)
* 1.4.2 - Updated SDK to the latest version (v6.2.2) | Address vulnerabilities
* 1.4.1 - Initial updates for fedramp compliance | Updated SDK to the latest version
* 1.4.0 - New action Replace
* 1.3.1 - Update to v4 Python plugin runtime
* 1.3.0 - New action Length | Add example inputs
* 1.2.1 - New spec and help.md format for the Extension Library
* 1.2.0 - New action Trim
* 1.1.0 - New action Set Encoding
* 1.0.1 - Update plugin tag from `util` to `utilities` for Marketplace searchability
* 1.0.0 - Initial plugin

# Links

* [Python 3 String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

## References

* [Python 3 String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)