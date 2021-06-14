# Description

Hypertext Markup Language (HTML) is the standard markup language for documents designed to be displayed in a web browser. This plugin provides the ability to convert an HTML document into a variety of formats using [pypandoc](https://pypi.python.org/pypi/pypandoc). Supported formats are:

* DOCX
* EPUB
* Markdown
* PDF
* HTML5
* Plain Text

# Key Features

* Convert an HTML document into another format to more easily export, share, or edit the document's contents

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Windows Document

This action is used to convert an HTML document to DOCX.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|doc|string|None|True|Document to transform|None|<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Convert HTML to DOCX</p></body></html>|

Example input:

```
{
  "doc": "\u003c!DOCTYPE html\u003e\u003chtml\u003e\u003chead\u003e\u003ctitle\u003eRapid7 InsightConnect\u003c/title\u003e\u003c/head\u003e\u003cbody\u003e\u003cp\u003eConvert HTML to DOCX\u003c/p\u003e\u003c/body\u003e\u003c/html\u003e"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|docx|bytes|False|Docx File|

Example output:

```
{
  "docx": "UEsDBBQAAggIACEf91DPOFToaQEAAKgGAAA..."
}
```

#### Markdown

This action is used to convert an HTML document to Markdown.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|doc|string|None|True|Document to transform|None|<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Convert HTML to Markdown</p></body></html>|

Example input:

```
{
  "doc": "\u003c!DOCTYPE html\u003e\u003chtml\u003e\u003chead\u003e\u003ctitle\u003eRapid7 InsightConnect\u003c/title\u003e\u003c/head\u003e\u003cbody\u003e\u003cp\u003eConvert HTML to Markdown\u003c/p\u003e\u003c/body\u003e\u003c/html\u003e"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|markdown_contents|string|False|Markdown Contents|
|markdown_file|bytes|False|Markdown File|

Example output:

```
{
  "markdown_file": "Q29udmVydCBIVE1MIHRvIE1hcmtkb3duCg==",
  "markdown_contents": "Convert HTML to Markdown\n"
}
```

#### HTML5

This action is used to convert an HTML document to HTML5.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|doc|string|None|True|Document to transform|None|<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Convert HTML to HTML5</p></body></html>|

Example input:

```
{
  "doc": "\u003c!DOCTYPE html\u003e\u003chtml\u003e\u003chead\u003e\u003ctitle\u003eRapid7 InsightConnect\u003c/title\u003e\u003c/head\u003e\u003cbody\u003e\u003cp\u003eConvert HTML to HTML5\u003c/p\u003e\u003c/body\u003e\u003c/html\u003e"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|html5_contents|string|False|HTML5 Contents|
|html5_file|bytes|False|HTML5 File|

Example output:

```
{
  "html5_contents": "&lt;!DOCTYPE html&gt;\n<html>\n<head>\n<title>\nRapid7 InsightConnect\n</title>\n</head>\n<body>\n<p>\nConvert HTML to HTML5\n</p>\n</body>\n</html>\n", 
  "html5_file": "Jmx0OyFET0NUWVBFIGh0bWwmZ3Q7Cj..."
}
```

#### PDF

This action is used to convert an HTML document to PDF.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|doc|string|None|True|Document to transform|None|<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Convert HTML to PDF</p></body></html>|

Example input:

```
{
  "doc": "\u003c!DOCTYPE html\u003e\u003chtml\u003e\u003chead\u003e\u003ctitle\u003eRapid7 InsightConnect\u003c/title\u003e\u003c/head\u003e\u003cbody\u003e\u003cp\u003eConvert HTML to PDF\u003c/p\u003e\u003c/body\u003e\u003c/html\u003e"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|pdf|bytes|False|PDF File|

Example output:

```
{
  "pdf": "JVBERi0xLjUKJdDUxdgKNSAwIG9iago8PA..."
}
```

#### Validate

This action is used to validate an HTML document using the [W3 validator](https://validator.w3.org).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|html_contents|string|None|True|HTML Contents|None|<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Automate with InsightConnect!</p></body></html>|

Example input:

```
{
  "html_contents": "\u003c!DOCTYPE html\u003e\u003chtml\u003e\u003chead\u003e\u003ctitle\u003eRapid7 InsightConnect\u003c/title\u003e\u003c/head\u003e\u003cbody\u003e\u003cp\u003eAutomate with InsightConnect!\u003c/p\u003e\u003c/body\u003e\u003c/html\u003e"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|validated|boolean|False|HTML Syntax Validation Status|

Example output:

```
{
  "validated": true
}
```

#### EPUB

This action is used to convert an HTML document to EPUB.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|doc|string|None|True|Document to transform|None|<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Convert HTML to EPUB</p></body></html>|

Example input:

```
{
  "doc": "\u003c!DOCTYPE html\u003e\u003chtml\u003e\u003chead\u003e\u003ctitle\u003eRapid7 InsightConnect\u003c/title\u003e\u003c/head\u003e\u003cbody\u003e\u003cp\u003eConvert HTML to EPUB\u003c/p\u003e\u003c/body\u003e\u003c/html\u003e"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|epub|bytes|False|Epub file|

Example output:

```
{
  "epub": "UEsDBBQAAggAAPAe91BvYassFAAAABQAAAA..."
}
```

#### Text

This action is used to strip an HTML string of all tags and return only the text.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|doc|string|None|True|Document to transform|None|<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Automate with InsightConnect!</p></body></html>|
|remove_scripts|boolean|None|False|Remove non-HTML scripts from the document|None|False|

Example input:

```
{
  "doc": "\u003c!DOCTYPE html\u003e\u003chtml\u003e\u003chead\u003e\u003ctitle\u003eRapid7 InsightConnect\u003c/title\u003e\u003c/head\u003e\u003cbody\u003e\u003cp\u003eAutomate with InsightConnect!\u003c/p\u003e\u003c/body\u003e\u003c/html\u003e",
  "remove_scripts": false
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|text|string|False|String without HTML tags|

Example output:

```
{
  "text": "Automate with InsightConnect!"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.2.2 - Update to v4 Python plugin runtime
* 1.2.1 - New spec and help.md format for the Extension Library
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