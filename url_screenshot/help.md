# Description

Screenshot a URL from the Orchestrator

# Key Features

* Generates a Screenshot of a URL using chromium

# Requirements

* Orchestrator requires network connectivity to the target URL

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Screenshot URL

This action is used to grab a screenshot of a URL from the Orchestrator.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|delay|integer|None|False|Delay (in seconds) after page has loaded before screenshot|None|5|
|full_page|boolean|False|True|Export screenshot of "body" element instead of the default viewport.  This "body" element may have some formatting issues but should contain all elements of the page|None|False|
|url|string|None|True|URL to screenshot|None|https://www.google.com|

Example input:

```
{
  "delay": 5,
  "full_page": false,
  "url": "https://www.google.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|screenshot|bytes|False|The resulting PNG screenshot of the URL|

Example output:

```
{
  "screenshot": "base64 image data"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._
## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - Change icon/extension image, update doc with example
* 1.0.0 - Initial plugin

# Links

## References

* [ChromeDriver](https://chromedriver.chromium.org/)
