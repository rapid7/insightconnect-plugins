# Description

[Unshorten.me](https://unshorten.me/) provides an easy and free method to unshorten a wide range of shortened URLs.
The Unshorten.me plugin for Rapid7 InsightConnect can help assist phishing investigations, URL analysis,
 deobfuscation, and more.

This plugin utilizes the [Unshorten.me API](https://unshorten.me/api).

# Key Features

* URL unshortening

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Unshorten

This action is used to unshorten a URL.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|Short URL|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|error|string|False|Error message|
|requested_url|string|True|Short URL|
|resolved_url|string|True|Long URL|
|success|boolean|True|To indicate if the operation was successful or not|
|usage_count|integer|False|The usage count for the current IP|

Example output:

```

{
  "requested_url": "https://bit.ly/1dNVPAW",
  "resolved_url": "http://www.google.com/",
  "success": true,
  "usage_count": 5
}

```

An error can occur from the Unshorten API e.g. submitting a malformed URL. Any error messages from the API are contained in a key called `error`.
In addition, `success` will be set to `false`.

Example output:

```

{
  "requested_url": "https://adfasdfadsfadsfasdfadsf.netadfa",
  "resolved_url": "",
  "error": "Connection Error",
  "success": false,
  "usage_count": 0
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Note that the API is limited to 10 requests per hour per IP address.

# Version History

* 1.0.3 - Use input and output constants | Changed `Exception` to `PluginException` | Change docker image from `komand/python-pypy3-plugin:2` to `komand/python-3-37-slim-plugin:3` | Add user nobody in Dockerfile
* 1.0.2 - New spec and help.md format for the Extension Library
* 1.0.1 - Graceful exit for invalid URLs
* 1.0.0 - Initial plugin

# Links

## References

* [Unshorten.me](https://unshorten.me/)
* [API](https://unshorten.me/)

