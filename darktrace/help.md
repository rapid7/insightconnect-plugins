# Description

[DarkTrace](https://www.darktrace.com/) is an AI cybersecurity company for threat detection and response across cloud, email, industrial and the network.

# Key Features

* Add or remove watched domains

# Requirements

* Requires an API public and private Token from the DarkTrace

# Documentation
## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_private_token|credential_secret_key|None|True|Enter API private token|None|1452d258-7c12-7c12-7c12-1452d25874c2|
|api_public_token|credential_secret_key|None|True|Enter API public token|None|1452d258-7c12-7c12-7c12-1452d25874c2|
|url|string|None|True|Connection URL|None|None|

Example input:

```
{
  "api_private_token": "1452d258-7c12-7c12-7c12-1452d25874c2",
  "api_public_token": "1452d258-7c12-7c12-7c12-1452d25874c2"
}
```
## Technical Details

### Actions

#### Update Watched Domains

This action is used to add or remove items from DarkTrace. If an indicator is added, DarkTrace will monitor network traffic for that URL and create alerts from it.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|description|string|Watched Domains managed by InsightConnect|False|Description of the indicator|None|Watched Domains managed by InsightConnect|
|entry|string|None|True|An external domain, hostname or IP address|None|192.168.10.10|
|expiration_time|string|None|False|Expiration time of an indicator|None|2020-04-03 15:23:20|
|hostname|boolean|None|False|Set to true to treat the added items as hostnames rather than domains|None|True|
|source|string|InsightConnect|False|Source of an indicator|None|InsightConnect|
|watched_domain_status|boolean|None|True|Determine whether item should be added or remove from the list. Set True to add, set false to remove|None|True|

Example input:

```
{
  "description": "Watched Domains managed by InsightConnect",
  "entry": "192.168.10.10",
  "expiration_time": "2020-04-03 15:23:20",
  "hostname": true,
  "source": "InsightConnect",
  "watched_domain_status": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|added|integer|False|Added|
|success|boolean|True|Success|
|updated|integer|False|Updated|

Example output:

```
{
  "added": 1,
  "success": true,
  "updated": 0
}
```

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

* [DarkTrace](https://www.darktrace.com/)
