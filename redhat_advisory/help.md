# Description

The [Red Hat Security Advisories](https://access.redhat.com/security/updates/advisory) triggers on any new security advisories. The Red Hat Security Advisory gives information about security flaws that affect Red Hat products and services.

Advisories and update notifications are also provided via the Red Hat Network for products serviced by the Red Hat Network.

# Key Features

* Trigger a workflow on a new advisory

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

This plugin does not contain any actions.

### Triggers

#### New Advisory

This trigger is used to monitor for new new advisories.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|after|string|None|False|Look for new advisories after provided date. Default is when trigger starts|None|
|include_cvrf|boolean|False|False|Include the full source CVRF|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|publisher|publisher|False|Publisher|
|severity|string|False|Severity|
|released_packages|[]string|False|Released Packages|
|title|string|False|Title of Advisory|
|url|string|False|URL to advisory|
|type|string|False|Type, e.g. 'Security Advisory'|
|notes|string|False|Notes|
|source|object|False|Original Source CVRF doc|
|references|[]reference|False|URL references|
|oval|object|False|OVAL|
|bugzillas|[]string|False|Bugzilla IDs|
|resource_url|string|False|Resource JSON URL|
|released_on|date|False|Release Date|
|rhsa|string|False|Red Hat Security Advisory ID|
|cves|[]string|False|CVE IDs|

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.2 - New spec and help.md format for the Hub | Add missing title values for actions in plugin.spec.yaml
* 1.0.1 - Support web server mode
* 1.0.0 - Update to v2 Python plugin architecture
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Red Hat Security Advisories](https://access.redhat.com/security/updates/advisory)
* [Red Hat Advisory API](https://access.redhat.com/labs/securitydataapi)
