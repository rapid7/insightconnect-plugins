# Description

The Bluecoat Labs plugins enables submissions of suspicous URLs to be reviewed by Bluecoat Labs.

# Key Features

* URL Review

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

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

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.2 - New spec and help.md format for the Hub
* 2.0.1 - New spec and help.md format for the Hub
* 2.0.0 - Fix issue where a change in Bluecoat Labs API was causing the plugin to fail
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Bluecoat](https://www.bluecoat.com/support-services)

