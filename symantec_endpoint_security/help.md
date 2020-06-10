# Description

Symantec Endpoint Security delivers the most complete, integrated endpoint security platform on the planet

# Key Features

Identify key features of plugin.

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

# Documentation
## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password|None|{"username": example, "password": "test"}|
|domain|string|None|True|The Symantec Endpoint Protection Manager domain to which the username logs on|None|mydomain|
|host|string|None|True|Symantec Endpoint Protection Manager host, either IP address or domain|None|sepm-14|
|port|integer|8446|True|Symantec Endpoint Protection server port, typically 8446|None|8446|

Example input:

```
{
  "credentials": "{\"username\": example, \"password\": \"test\"}",
  "domain": "mydomain",
  "host": "sepm-14",
  "port": 8446
}
```
## Technical Details



### Actions

_This plugin does not contain any actions._

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._
## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Symantec Endpoint Security](LINK TO PRODUCT/VENDOR WEBSITE)
