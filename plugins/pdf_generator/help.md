# Description

The PDF Generator plugin creates a PDF from user provided data

# Key Features

* Generate a PDF

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* Pillow 10.2.0

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Generate PDF

This action is used to generate a PDF from a text input

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|text|string|None|True|Text input|None|example|None|None|
  
Example input:

```
{
  "text": "example"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|pdf|bytes|True|Generated PDF|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cgo=|
  
Example output:

```
{
  "pdf": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cgo="
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

* 1.0.6 - Bumping requirements.txt | SDK Bump
* 1.0.5 - Pin additional version dependency
* 1.0.4 - Update SDK | Update vulnerable libraries
* 1.0.3 - Change library to generate PDF
* 1.0.2 - Update plugin runtime to InsightConnect | Add unit tests | Updated all dependencies to the newest versions
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

* [PyPDF2](https://pypdf2.readthedocs.io/)

## References

* [PDF](https://en.wikipedia.org/wiki/Portable_Document_Format)