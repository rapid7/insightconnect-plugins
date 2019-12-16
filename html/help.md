# Description

Utility plugin to convert an HTML document into a variety of formats using [pypandoc](https://pypi.python.org/pypi/pypandoc). Supported formats are:

* DOCX
* EPUB
* Markdown
* PDF
* HTML5
* Plain Text

# Key Features

* Convert HTML into another format

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Windows Document

This action is used to convert an HTML document to DOCX.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|doc|string|None|True|Document to transform|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|docx|bytes|False|Docx File|

#### Markdown

This action is used to convert an HTML document to Markdown.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|doc|string|None|True|Document to transform|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|markdown_contents|string|False|Markdown Contents|
|markdown_file|bytes|False|Markdown File|

#### HTML5

This action is used to convert an HTML document to HTML5.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|doc|string|None|True|Document to transform|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|html5_file|bytes|False|HTML5 File|
|html5_contents|string|False|HTML5 Contents|

#### PDF

This action is used to convert an HTML document to PDF.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|doc|string|None|True|Document to transform|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|pdf|bytes|False|PDF File|

#### Validate

This action is used to validate an HTML document using the [W3 validator](https://validator.w3.org).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|html_contents|string|None|True|HTML Contents|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|validated|boolean|False|HTML Syntax Validation Status|

#### EPUB

This action is used to convert an HTML document to EPUB.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|doc|string|None|True|Document to transform|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|epub|bytes|False|Epub file|

#### Text

This action is used to strip an HTML string of all tags and return only the text.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|doc|string|None|True|Document to transform|None|
|remove_scripts|boolean|None|False|Remove non-HTML scripts from the document|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|text|string|False|String without HTML tags|

Example output:

```
{
  "text": "Yup, this is some text"
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.2.1 - New spec and help.md format for the Hub
* 1.2.0 - Update to add the Remove Scripts option to Text
* 1.1.0 - New action: Text
* 1.0.1 - Add `utilities` plugin tag for Marketplace searchability
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [pypandoc](https://pypi.python.org/pypi/pypandoc)
* [W3 Validator](https://validator.w3.org)