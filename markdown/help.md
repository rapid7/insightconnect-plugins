# Description

[Markdown](https://en.wikipedia.org/wiki/Markdown) is lightweight markup language with plain text formatting syntax.
This plugin utilizes [pandoc](https://pandoc.org/) via [pypandoc](https://pypi.python.org/pypi/pypandoc/) to manipulate Markdown content.

# Key Features

* Convert from HTML to Markdown and vice-versa

# Requirements

_This plugin does not contain any requirements_

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### HTML to Markdown

This action is used to convert HTML to Markdown.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|html|bytes|None|True|HTML data|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|markdown|bytes|False|Markdown data|

#### Markdown to PDF

This action is used to convert Markdown to PDF.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|markdown|bytes|None|True|Markdown data|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|pdf|bytes|False|PDF data|

#### Markdown to HTML

This action is used to convert Markdown to HTML.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|markdown|bytes|None|True|Markdown data|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|html|bytes|False|HTML data|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.2.2 - New spec and help.md format for the Hub
* 2.2.1 - Add `utilities` plugin tag for Marketplace searchability
* 2.2.0 - PyPandoc bug fix | Support web server mode
* 2.1.0 - Update to v2 Python plugin architecture | Change type of input/output to string
* 2.0.1 - SSL bug fix in SDK
* 2.0.0 - Rewrite
* 0.1.0 - Initial plugin

# Links

## References

* [Markdown](https://en.wikipedia.org/wiki/Markdown)
* [pandoc](https://pandoc.org/)
* [pypandoc](https://pypi.python.org/pypi/pypandoc/)

