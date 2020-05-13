# Description

[Markdown](https://en.wikipedia.org/wiki/Markdown) is a lightweight markup language with plain text formatting syntax.
This plugin utilizes [pandoc](https://pandoc.org/) via [pypandoc](https://pypi.python.org/pypi/pypandoc/) to manipulate Markdown content.

# Key Features

* Convert HTML to Markdown for simpler editing
* Convert Markdown to HTML or PDF for formatted beautification

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### HTML to Markdown

This action is used to convert HTML to Markdown.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|html|bytes|None|False|HTML data as bytes|None|None|
|html_string|string|None|False|HTML data as string|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|markdown|bytes|False|Markdown data as bytes|
|markdown_string|bytes|False|Markdown data as string|

#### Markdown to PDF

This action is used to convert Markdown to PDF.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|markdown|bytes|None|False|Markdown content represented in base64|None|IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q=|
|markdown_string|string|None|False|Markdown content as a string|None|# Rapid7 InsightConnect|

Example input:

```
{
  "markdown_string": "# Rapid7 InsightConnect"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|pdf|bytes|False|PDF data as bytes|
|pdf_string|string|False|PDF data as string|

#### Markdown to HTML

This action is used to convert Markdown to HTML.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|markdown|bytes|None|False|Markdown content represented in base64|None|IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q=|
|markdown_string|string|None|False|Markdown content as a string|None|# Rapid7 InsightConnect|

Example input:

```
{
  "markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q="
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|html|bytes|False|HTML data as bytes|
|html_string|string|False|HTML data|

Example output:

```
{
  "html": "PGgxIGlkPSJyYXBpZDctaW5zaWdodGNvbm5lY3QiPlJhcGlkNyBJbnNpZ2h0Q29ubmVjdDwvaDE+Cg==",
  "html_string": "\u003ch1 id=\"rapid7-insightconnect\"\u003eRapid7 InsightConnect\u003c/h1\u003e\n"
}
```

#### Markdown to TXT

This action is used to convert Markdown to TXT.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|markdown|bytes|None|False|Markdown content represented in base64|None|IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q=|
|markdown_string|string|None|False|Markdown content as a string|None|# Rapid7 InsightConnect|

Example input:

```
{
  "markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q="
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|txt|bytes|False|TXT data as bytes|
|txt_string|string|False|TXT data as string|

Example output:

```
{
  "txt_string": "Rapid7 InsightConnect\n",
  "txt": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 3.1.0 - New action: Markdown to TXT
* 3.0.0 - Update Markdown to HTML and Markdown to PDF action titles and descriptions
* 2.2.2 - New spec and help.md format for the Extension Library
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
