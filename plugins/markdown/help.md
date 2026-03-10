# Description

[Markdown](https://en.wikipedia.org/wiki/Markdown) is a lightweight markup language with plain text formatting syntax. This plugin utilizes [pandoc](https://pandoc.org/) via [pypandoc](https://pypi.python.org/pypi/pypandoc/) to manipulate Markdown content

# Key Features

* Convert HTML to Markdown for simpler editing
* Convert Markdown to HTML or PDF for formatted beautification

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2024-03-13

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### HTML to Markdown

This action is used to convert HTML to Markdown

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|html|bytes|None|False|HTML data as bytes|None|PGgxPlJhcGlkNzwvaDE+|None|None|
|html_string|string|None|False|HTML data as string|None|<h1>Rapid7</h1>|None|None|
  
Example input:

```
{
  "html": "PGgxPlJhcGlkNzwvaDE+",
  "html_string": "<h1>Rapid7</h1>"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|markdown|bytes|False|Markdown data as bytes|UmFwaWQ3Cj09PT09PQo=|
|markdown_string|bytes|False|Markdown data as string|Rapid7\n======\n|
  
Example output:

```
{
  "markdown": "UmFwaWQ3Cj09PT09PQo=",
  "markdown_string": "Rapid7\\n======\\n"
}
```

#### Markdown to HTML

This action is used to convert Markdown to HTML

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|markdown|bytes|None|False|Markdown content represented in base64|None|IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q=|None|None|
|markdown_string|string|None|False|Markdown content as a string|None|# Rapid7 InsightConnect|None|None|
  
Example input:

```
{
  "markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q=",
  "markdown_string": "# Rapid7 InsightConnect"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|html|bytes|False|HTML data as bytes|PGgxIGlkPSJyYXBpZDctaW5zaWdodGNvbm5lY3QiPlJhcGlkNyBJbnNpZ2h0Q29ubmVjdDwvaDE+Cg==|
|html_string|string|False|HTML data|<h1 id="rapid7-insightconnect">Rapid7 InsightConnect</h1>|
  
Example output:

```
{
  "html": "PGgxIGlkPSJyYXBpZDctaW5zaWdodGNvbm5lY3QiPlJhcGlkNyBJbnNpZ2h0Q29ubmVjdDwvaDE+Cg==",
  "html_string": "<h1 id=\"rapid7-insightconnect\">Rapid7 InsightConnect</h1>"
}
```

#### Markdown to PDF

This action is used to convert Markdown to PDF

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|markdown|bytes|None|False|Markdown content represented in base64|None|IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q=|None|None|
|markdown_string|string|None|False|Markdown content as a string|None|# Rapid7 InsightConnect|None|None|
  
Example input:

```
{
  "markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q=",
  "markdown_string": "# Rapid7 InsightConnect"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|pdf|bytes|False|PDF data as bytes|JVBERi0xLjQKJcOiw6MKMSAwIG9iago8PAovVGl0bGUgKCkKL0NyZWF0b3IgKO+/v|
|pdf_string|string|False|PDF data as string|PDF-1.4 0 obj<</Title Creator|
  
Example output:

```
{
  "pdf": "JVBERi0xLjQKJcOiw6MKMSAwIG9iago8PAovVGl0bGUgKCkKL0NyZWF0b3IgKO+/v",
  "pdf_string": "PDF-1.4 0 obj<</Title Creator"
}
```

#### Markdown to TXT

This action is used to convert Markdown to TXT

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|markdown|bytes|None|False|Markdown content represented in base64|None|IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q=|None|None|
|markdown_string|string|None|False|Markdown content as a string|None|# Rapid7 InsightConnect|None|None|
  
Example input:

```
{
  "markdown": "IyBSYXBpZDcgSW5zaWdodENvbm5lY3Q=",
  "markdown_string": "# Rapid7 InsightConnect"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|txt|bytes|False|TXT data as bytes|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
|txt_string|string|False|TXT data as string|Rapid7 InsightConnect|
  
Example output:

```
{
  "txt": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "txt_string": "Rapid7 InsightConnect"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 4.0.0 - Update SDK to version 6.4.3
* 3.1.4 - `Markdown to PDF` - Fix issue which produced blank PDF files
* 3.1.3 - Update PyPandoc dependency | Update SDK
* 3.1.2 - Added additional error messaging | Refactored code | Fixed bug in Markdown to TXT action which resulted in an incorrect output
* 3.1.1 - Use input and output constants inm Markdown to PDF action | Change docker image from `komand/python-2-plugin:2` to `insightconnect-python-3-38-plugin:4` | Changed `Exception` to `PluginException` in Markdown to PDF action | Add `USER nobody` in Dockerfile | Update `pypandoc` and `beautifulsoup4` version in requirements | Add example inputs and outputs
* 3.1.0 - `Markdown to TXT`: New action
* 3.0.0 - Update Markdown to HTML and Markdown to PDF action titles and descriptions
* 2.2.2 - New spec and help.md format for the Extension Library
* 2.2.1 - Add `utilities` plugin tag for Marketplace searchability
* 2.2.0 - PyPandoc bug fix | Support web server mode
* 2.1.0 - Update to v2 Python plugin architecture | Change type of input/output to string
* 2.0.1 - SSL bug fix in SDK
* 2.0.0 - Rewrite
* 0.1.0 - Initial plugin

# Links

* [Markdown](https://en.wikipedia.org/wiki/Markdown)

## References

* [pandoc](https://pandoc.org/)
* [pypandoc](https://pypi.python.org/pypi/pypandoc/)