# Description

The PDF Generator plugin creates a PDF from user provided data. This allows the user to create robust 
reports to distribute workflow details.

# Key Features

* Generate a PDF

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions
  
* Pillow 10.1.0  
* WeasyPrint==52.5

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Generate PDF
  
Generate a PDF from a text input

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|text|string|None|True|Text input|None|example|
  
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
  
*There is no troubleshooting for this plugin.*

# Version History

* 1.0.2 - Update plugin runtime to InsightConnect | Add unit tests | Updated all dependencies to the newest versions
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

[Weasyprint](https://doc.courtbouillon.org/weasyprint/stable/)

## References

* [PDF](https://en.wikipedia.org/wiki/Portable_Document_Format)

