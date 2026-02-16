# Description

The Awk InsightConnect plugin manipulates input data using GNU [Awk](https://www.gnu.org/software/gawk/manual/gawk.html)
which is a pattern scanning and processing language.

For example, here's a simple example of Awk from the command line:

```
$ awk '{ print \"Second column contents:\",$2 }' 3columns.txt
Second column contents: dog
Second column contents: cat
Second column contents: horse
Second column contents: birds
```


# Key Features

* Search and replace a string
* Search and replace text in a file

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* GNU AWK 5.3.2

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Process File

This action is used to process file with Awk

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|data|bytes|None|True|File to process|None|VXNlciBEYXRhIEFnZQpKb2huIDI1IDMwCkphbmUgMzAgMzUK|None|None|
|expression|string|None|True|Awk expression e.g. [pattern] { action }|None|awk '{ print $1, $3 }'|None|None|
  
Example input:

```
{
  "data": "VXNlciBEYXRhIEFnZQpKb2huIDI1IDMwCkphbmUgMzAgMzUK",
  "expression": "awk '{ print $1, $3 }'"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|out|string|False|Processed string|User Age
John 30
Jane 35|
  
Example output:

```
{
  "out": "User Age\nJohn 30\nJane 35"
}
```

#### Process String

This action is used to process string with Awk

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expression|string|None|True|Awk expression e.g. [pattern] { action }|None|awk '{ gsub(/text/, 'test'); print }'|None|None|
|text|string|None|True|String to process|None|Example text to process with awk|None|None|
  
Example input:

```
{
  "expression": "awk '{ gsub(/text/, 'test'); print }'",
  "text": "Example text to process with awk"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|out|string|False|Processed string|Example test to process with awk|
  
Example output:

```
{
  "out": "Example test to process with awk"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* By default, Awk returns a newline for each record. A common use case is to print a field from a body of text without
the ending newline so that it may be passed to other plugins in an InsightConnect workflow. There's at least two ways to achieve this
by setting the ORS (Output Record Separator) variable to nothing e.g. `-v ORS= '{ print $1 }'` or `'BEGIN { ORS="" } { print $1 }'`


# Version History

* 1.2.2 - Refreshed the plugin | Updated SDK to the latest version (6.4.3)
* 1.2.1 - New spec and help.md format for the Extension Library | Change docker image from `komand/python-pypy3-plugin:2` to `komand/python-3-37-plugin` | Removed duplicated code | Changed string action to use bare string instead temporary file | Changed bare strings in params.get and output to static fields from schema | Repair coding style
* 1.2.0 - Support web server mode
* 1.1.2 - Update to v2 Python plugin architecture
* 1.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Awk](https://www.gnu.org/software/gawk/manual/gawk.html)

## References

* [Awk](https://www.gnu.org/software/gawk/manual/gawk.html)