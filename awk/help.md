# Description

The Awk InsightConnect plugin manipulates input data using GNU [Awk](https://www.gnu.org/software/gawk/manual/gawk.html)
 which is a pattern scanning and processing language.

For example, here's a simple example of Awk from the command line:

```

$ awk '{ print "Second column contents:",$2 }' 3columns.txt
Second column contents: dog
Second column contents: cat
Second column contents: horse
Second column contents: birds

```

# Key Features

* Search and replace a string
* Search and replace text in a file

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Process String

This action can be used to process a string with Awk.

##### Input

Accepts an Awk expression and a string to process. Awk's command-line options can be passed in the expression.
Single-quotes are required to enclose the program part of the expression. For example, invoking Awk with a
command-line option and a program: `-F , '{ print $2 }'`.

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|text|string|None|True|String to process|None|
|expression|string|None|True|Awk expression e.g. [pattern] { action }|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|out|string|False|Processed string|

#### Process File

This action is used to process file-encoded data such as a file. The data is decoded and then ran through Awk.

##### Input

Accepts an Awk expression and file-encoded data (file, string, etc.) to process.

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|expression|string|None|True|Awk expression e.g. [pattern] { action }|None|
|data|bytes|None|True|File to process|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|out|string|False|Processed string|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

By default, Awk returns a newline for each record. A common use case is to print a field from a body of text without
the ending newline so that it may be passed to other plugins in an InsightConnect workflow. There's at least two ways to achieve this
by setting the ORS (Output Record Separator) variable to nothing e.g. `-v ORS= '{ print $1 }'` or `'BEGIN { ORS="" } { print $1 }'`.

# Version History

* 1.2.1 - New spec and help.md format for the Hub | Change docker image from `komand/python-pypy3-plugin:2` to `komand/python-3-37-plugin` | Removed duplicated code | Changed string action to use bare string instead temporary file | Changed bare strings in params.get and output to static fields from schema | Repair coding style
* 1.2.0 - Support web server mode
* 1.1.2 - Update to v2 Python plugin architecture
* 1.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Awk](https://www.gnu.org/software/gawk/manual/gawk.html)

