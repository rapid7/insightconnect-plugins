# Description

Screenshot a URL from the Orchestrator

# Key Features

* Generates a Screenshot of a URL using chromium

# Requirements

* Orchestrator requires network connectivity to the target URL

# Supported Product Versions
  
* Selenium 4.16.0

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Screenshot URL
  
This action is used to take a screenshot of a URL from the Orchestrator.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|delay|integer|None|False|Delay (in seconds) after page loads before taking a screenshot|None|5|
|full_page|boolean|False|True|Export screenshot of `body` element instead of the default viewport. This `body` element may have some formatting issues but should contain all elements of the page|None|False|
|url|string|None|True|The URL to take a screenshot from|None|https://www.google.com|
  
Example input:

```
{
  "delay": 5,
  "full_page": false,
  "url": "https://www.google.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|screenshot|bytes|False|The resulting PNG screenshot of the URL|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
  
Example output:

```
{
  "screenshot": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
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

* 1.0.2 - `Screenshot`: Fixed issue where action couldn't take a screenshot of page | Updated the plugin SDK to latest
* 1.0.1 - Change icon/extension image, update doc with example
* 1.0.0 - Initial plugin

# Links

* [Chromium](https://www.chromium.org/chromium-projects/)

## References

* [ChromeDriver](https://chromedriver.chromium.org/)
