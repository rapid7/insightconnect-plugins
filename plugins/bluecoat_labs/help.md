# Description

The Bluecoat Labs plugins enables submissions of suspicous URLs to be reviewed by Bluecoat Labs

# Key Features

* URL Review

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2025-10-06

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Site Reviewer

This action is used to categorizes the given URL

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|target_url|string|None|True|URL to be reviewed|None|komand.com|None|None|
  
Example input:

```
{
  "target_url": "komand.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|site_review_results|[]url_properties|False|URL properties|[{"url": "http://komand.com/","date_since_last_checked": "> 7","category": "Technology/Internet"}]|
  
Example output:

```
{
  "site_review_results": [
    {
      "category": "Technology/Internet",
      "date_since_last_checked": "> 7",
      "url": "http://komand.com/"
    }
  ]
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**url_properties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Category|string|None|False|None|None|
|Days Since Last Checked|string|None|False|None|None|
|URL|string|None|False|None|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 2.0.2 - Deprecated the plugin
* 2.0.1 - New spec and help.md format for the Extension Library
* 2.0.0 - Fix issue where a change in Bluecoat Labs API was causing the plugin to fail
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Bluecoat](https://www.bluecoat.com/support-services)

## References

* [Bluecoat](https://www.bluecoat.com/support-services)