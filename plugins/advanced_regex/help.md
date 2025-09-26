# Description

The Advanced Regex plugin is used to extract or manipulate targeted text using regular expressions operations on a string using Python specific regex

# Key Features

* Data extraction
* Search and replace text
* Split text

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2025-09-25

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Data Extraction

This action is used to extract data via regex from a string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ascii|boolean|False|False|Make \w \W \b \B follow ASCII rules|None|False|None|None|
|dotall|boolean|False|False|Make . match newline|None|True|None|None|
|ignorecase|boolean|False|False|Make regex non-case sensitive|None|True|None|None|
|in_regex|string|None|True|Regex to use for data extraction|None|lorem|None|None|
|in_string|string|None|True|Input string|None|Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sapien ex, lorems odales|None|None|
|multiline|boolean|False|False|Make begin/end consider each line|None|True|None|None|
  
Example input:

```
{
  "ascii": false,
  "dotall": false,
  "ignorecase": false,
  "in_regex": "lorem",
  "in_string": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sapien ex, lorems odales",
  "multiline": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|matches|[]regex_match|True|A list of objects, each with a `value` key containing an array of strings matched by the regex using Python's re.findall()|[{"value": ["lorem"]}]|
  
Example output:

```
{
  "matches": [
    {
      "value": [
        "lorem"
      ]
    }
  ]
}
```

#### Search and Replace

This action is used to regex search and replace string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ascii|boolean|False|False|Make \w \W \b \B follow ASCII rules|None|False|None|None|
|dotall|boolean|False|False|Make . match newline|None|True|None|None|
|ignorecase|boolean|False|False|Make regex non-case sensitive|None|True|None|None|
|in_regex|string|None|True|Regex to match|None|lorem|None|None|
|in_string|string|None|True|Input string|None|Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sapien ex, lorems odales|None|None|
|max_replace|integer|0|False|Max occurrences to replace - if zero all will be replaced|None|0|None|None|
|multiline|boolean|False|False|Make begin/end consider each line|None|True|None|None|
|replace_string|string|None|False|The string to replace matches with|None|REPLACED|None|None|
  
Example input:

```
{
  "ascii": false,
  "dotall": false,
  "ignorecase": false,
  "in_regex": "lorem",
  "in_string": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sapien ex, lorems odales",
  "max_replace": 0,
  "multiline": false,
  "replace_string": "REPLACED"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|string|True|The result of the replace operation|Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sapien ex, REPLACEDs odales|
  
Example output:

```
{
  "result": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sapien ex, REPLACEDs odales"
}
```

#### Split by Regex

This action is used to split a string into array using regex

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ascii|boolean|False|False|Make \w \W \b \B follow ASCII rules|None|False|None|None|
|dotall|boolean|False|False|Make . match newline|None|True|None|None|
|ignorecase|boolean|False|False|Make regex non-case sensitive|None|True|None|None|
|in_regex|string|None|True|Regex to split string on matches|None|lorem|None|None|
|in_string|string|None|True|Input string|None|Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sapien ex, lorems odales sed|None|None|
|max_split|integer|0|False|Max splits - if non-zero last element is remainder of string|None|0|None|None|
|multiline|boolean|False|False|Make begin/end consider each line|None|True|None|None|
  
Example input:

```
{
  "ascii": false,
  "dotall": false,
  "ignorecase": false,
  "in_regex": "lorem",
  "in_string": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sapien ex, lorems odales sed",
  "max_split": 0,
  "multiline": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|[]string|True|An array of the strings returned by the split operation|["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sapien ex, ", "s odales sed"]|
  
Example output:

```
{
  "result": [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sapien ex, ",
    "s odales sed"
  ]
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**regex_match**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Value|[]string|None|False|Stores the list of strings matched by the regular expression using Python's re.findall()|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 2.0.0 - Action `Data Extraction`: Updated output schema to be list of objects | Updated SDK to the latest version (6.3.10)
* 1.0.5 - Updated SDK to the latest version (6.2.5)
* 1.0.4 - Initial updates for fedramp compliance | Updated SDK to the latest version
* 1.0.3 - Update to make replace string non-required
* 1.0.2 - Update to v4 Python plugin runtime | Add example inputs
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

* [Python Regex](https://docs.python.org/library/re.html)

## References

* [Python Regex](https://docs.python.org/library/re.html)