# Description

Hypertext Markup Language (HTML) is the standard markup language for documents designed to be displayed in a web browser. This plugin provides the ability to convert an HTML document into a variety of formats using [pypandoc](https://pypi.python.org/pypi/pypandoc). Supported formats are: DOCX, EPUB, Markdown, PDF, HTML5, Plain Text

# Key Features

* Convert an HTML document into another format to more easily export, share, or edit the document's contents

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2024-09-30

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Windows Document

This action is used to convert an HTML document to DOCX

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|doc|string|None|True|Document to transform|None|<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Convert HTML to DOCX</p></body></html>|None|None|
  
Example input:

```
{
  "doc": "<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Convert HTML to DOCX</p></body></html>"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|docx|bytes|False|Docx File|UEsDBBQAAggIACEf91DPOFToaQEAAKgGAAA...|
  
Example output:

```
{
  "docx": "UEsDBBQAAggIACEf91DPOFToaQEAAKgGAAA..."
}
```

#### EPUB

This action is used to convert an HTML document to EPUB

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|doc|string|None|True|Document to transform|None|<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Convert HTML to EPUB</p></body></html>|None|None|
  
Example input:

```
{
  "doc": "<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Convert HTML to EPUB</p></body></html>"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|epub|bytes|False|Epub file|UEsDBBQAAggAAPAe91BvYassFAAAABQAAAA...|
  
Example output:

```
{
  "epub": "UEsDBBQAAggAAPAe91BvYassFAAAABQAAAA..."
}
```

#### HTML5

This action is used to convert an HTML document to HTML5

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|doc|string|None|True|Document to transform|None|<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Convert HTML to HTML5</p></body></html>|None|None|
  
Example input:

```
{
  "doc": "<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Convert HTML to HTML5</p></body></html>"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|html5_contents|string|False|HTML5 Contents|<title>Rapid7 InsightConnect</title>|
|html5_file|bytes|False|HTML5 File|Jmx0OyFET0NUWVBFIGh0bWwmZ3Q7Cj...|
  
Example output:

```
{
  "html5_contents": "<title>Rapid7 InsightConnect</title>",
  "html5_file": "Jmx0OyFET0NUWVBFIGh0bWwmZ3Q7Cj..."
}
```

#### Markdown

This action is used to convert an HTML document to Markdown

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|doc|string|None|True|Document to transform|None|<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Convert HTML to Markdown</p></body></html>|None|None|
  
Example input:

```
{
  "doc": "<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Convert HTML to Markdown</p></body></html>"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|markdown_contents|string|False|Markdown Contents|Convert HTML to Markdown|
|markdown_file|bytes|False|Markdown File|Q29udmVydCBIVE1MIHRvIE1hcmtkb3duCg==|
  
Example output:

```
{
  "markdown_contents": "Convert HTML to Markdown",
  "markdown_file": "Q29udmVydCBIVE1MIHRvIE1hcmtkb3duCg=="
}
```

#### PDF

This action is used to convert an HTML document to PDF

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|doc|string|None|True|Document to transform|None|<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Convert HTML to PDF</p></body></html>|None|None|
  
Example input:

```
{
  "doc": "<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Convert HTML to PDF</p></body></html>"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|pdf|bytes|False|PDF File|JVBERi0xLjUKJdDUxdgKNSAwIG9iago8PA...|
  
Example output:

```
{
  "pdf": "JVBERi0xLjUKJdDUxdgKNSAwIG9iago8PA..."
}
```

#### Text

This action is used to strip an HTML string of all tags and return only the text

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|doc|string|None|True|Document to transform|None|<!DOCTYPE html><html><head><title>Rapid7 InsightConnect HTML</title></head><body><p>Automate with InsightConnect</p></body></html>|None|None|
|remove_scripts|boolean|None|False|Remove non-HTML scripts from the document|None|False|None|None|
  
Example input:

```
{
  "doc": "<!DOCTYPE html><html><head><title>Rapid7 InsightConnect HTML</title></head><body><p>Automate with InsightConnect</p></body></html>",
  "remove_scripts": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|text|string|False|String without HTML tags|Automate with InsightConnect!|
  
Example output:

```
{
  "text": "Automate with InsightConnect!"
}
```

#### Validate

This action is used to validate an HTML document using the [W3 validator](https://validator.w3.org)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|html_contents|string|None|True|HTML Contents|None|<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Automate with InsightConnect (HTML)!</p></body></html>|None|None|
  
Example input:

```
{
  "html_contents": "<!DOCTYPE html><html><head><title>Rapid7 InsightConnect</title></head><body><p>Automate with InsightConnect (HTML)!</p></body></html>"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|validated|boolean|False|HTML Syntax Validation Status|True|
  
Example output:

```
{
  "validated": true
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

* 2.0.1 - Updated SDK to the latest version (6.3.2)
* 2.0.0 - Updated SDK to the latest version (6.2.6) | Enable Sandbox mode
* 1.2.8 - Updated SDK to the latest version (6.2.5)
* 1.2.7 - Initial updates for fedramp compliance | Updated SDK to the latest version
* 1.2.6 - SDK Bump | Addressing Snyk vulnerabilities | Fixing Unit Tests | Dockerfile USER permission updated
* 1.2.5 - Update requirements for pypandoc
* 1.2.4 - Actions modified in order to implement PluginExceptions
* 1.2.3 - Action HTML5: fix error with encoding to file
* 1.2.2 - Update to v4 Python plugin runtime
* 1.2.1 - New spec and help.md format for the Extension Library
* 1.2.0 - Update to add the Remove Scripts option to Text
* 1.1.0 - New action: Text
* 1.0.1 - Add `utilities` plugin tag for Marketplace searchability
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [W3 Validator](https://validator.w3.org)

## References

* [pypandoc](https://pypi.python.org/pypi/pypandoc)