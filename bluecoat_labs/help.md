# Description

[Bluecoat Labs](https://www.bluecoat.com/support-services) is a provider of hardware, software, and services designed for cybersecurity and network management.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Site Reviewer

This action takes a provided URL and uses Bluecoat's Site Reviewer service to categorize the given URL.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|target_url|string|None|True|URL to be reviewed|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|site_review_results|[]url_properties|False|URL properties|

Example output:

```
{
  "site_review_results": [
    {
      "url": "http://komand.com/",
      "date_since_last_checked": "> 7",
      "category": "Technology/Internet"
    }
  ]
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.0 - Fix issue where a change in Bluecoat Labs API was causing the plugin to fail
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [Bluecoat](https://www.bluecoat.com/support-services)

