# Description

[Confluence](https://atlassian.com/software/confluence) is an open and shared workspace for managing documents and 
files within an organization. Using the Confluence plugin for Rapid7 InsightConnect, users can view and update pages 
dynamically within automation workflows.

# Key Features

* Update pages
* View pages

# Requirements

* Confluence URL
* Confluence username and password

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|Connection URL|None|
|username|string|None|False|Username|None|
|password|string|None|False|Password|None|

## Technical Details

### Actions

#### Get Page Content

This action is used to retrieve content of a Wiki page.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|page|string|None|True|Page Name|None|
|space|string|None|True|Space|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|content|string|False|Content|
|found|boolean|False|True if found|

#### Store Page Content

This action is used store a page of user provided content to the Wiki.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|content|string|None|True|Content To Store|None|
|page|string|None|True|Page Name|None|
|space|string|None|True|Space|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|page|page|False|Page Stored|

#### Get Page

This action is used to retrieve a Wiki page.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|page|string|None|True|Page Name|None|
|space|string|None|True|Space|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|page|page|False|Page|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Make sure the credentials are valid and the Confluence URL is correct.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.3 - Pin Confluence python library at 0.2
* 0.1.2 - SSL bug fix in SDK
* 0.1.1 - Fix bug dumping credentials to log
* 0.1.0 - Initial plugin

# Links

## References

* [Confluence](https://www.atlassian.com/software/confluence)
* [Confluence API URL](https://docs.atlassian.com/confluence/REST/latest/)
* [Confluence Python Documentation](https://pythonhosted.org/confluence/)

