# Description

The [Red Hat Security Advisories](https://access.redhat.com/security/updates/advisory) plugin triggers workflows on any new security advisories. Red Hat Security Advisories provide information about security flaws that affect Red Hat products and services. This plugin consumes the [Red Hat Security Data API](https://access.redhat.com/security/data) using the CSAF 2.0 format

# Key Features

* Trigger a workflow when Red Hat publishes a new security advisory

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* Red Hat Security Data API CSAF 2.0

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions
  
*This plugin does not contain any actions.*
### Triggers


#### New Advisory

This trigger is used to trigger on new advisory

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|after|string|None|False|Look for new advisories after the provided ISO-8601 date (YYYY-MM-DD). Defaults to the trigger start time in UTC|None|2026-01-01|None|None|
|include_source|boolean|False|False|Include the full source advisory document (CSAF 2.0)|None|False|None|None|
  
Example input:

```
{
  "after": "2026-01-01",
  "include_source": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|bugzillas|[]string|False|Bugzilla IDs|["2481767"]|
|cves|[]string|False|CVE IDs|["CVE-2026-48962"]|
|notes|string|False|Notes|An update for perl-IO-Compress is now available for Red Hat Enterprise Linux 8.|
|publisher|publisher|False|Publisher|{'issuing_authority': 'Red Hat Product Security', 'contact_details': 'user@example.com', 'type': 'vendor'}|
|references|[]reference|False|URL references|[{"description": "Advisory link", "url": "https://access.redhat.com/errata/RHSA-2026:30858", "type": "self"}]|
|released_on|date|False|Release Date|2026-06-29T02:38:12Z|
|released_packages|[]string|False|Released Packages|["perl-IO-Compress-0:2.081-2.el8_10"]|
|resource_url|string|False|Resource JSON URL|https://access.redhat.com/hydra/rest/securitydata/csaf/RHSA-2026:30858.json|
|rhsa|string|False|Red Hat Security Advisory ID|RHSA-2026:30858|
|severity|string|False|Severity|important|
|source|object|False|Original source advisory document (CSAF 2.0)|{}|
|title|string|False|Title of Advisory|Red Hat Security Advisory: perl-IO-Compress security update|
|type|string|False|Type, e.g. 'Security Advisory'|Security Advisory|
|url|string|False|URL to advisory|https://access.redhat.com/errata/RHSA-2026:30858|
  
Example output:

```
{
  "bugzillas": [
    "2481767"
  ],
  "cves": [
    "CVE-2026-48962"
  ],
  "notes": "An update for perl-IO-Compress is now available for Red Hat Enterprise Linux 8.",
  "publisher": {
    "contact_details": "user@example.com",
    "issuing_authority": "Red Hat Product Security",
    "type": "vendor"
  },
  "references": [
    {
      "description": "Advisory link",
      "type": "self",
      "url": "https://access.redhat.com/errata/RHSA-2026:30858"
    }
  ],
  "released_on": "2026-06-29T02:38:12Z",
  "released_packages": [
    "perl-IO-Compress-0:2.081-2.el8_10"
  ],
  "resource_url": "https://access.redhat.com/hydra/rest/securitydata/csaf/RHSA-2026:30858.json",
  "rhsa": "RHSA-2026:30858",
  "severity": "important",
  "source": {},
  "title": "Red Hat Security Advisory: perl-IO-Compress security update",
  "type": "Security Advisory",
  "url": "https://access.redhat.com/errata/RHSA-2026:30858"
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**reference**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|False|Reference Description|Vulnerability details|
|type|string|None|False|Ref Type (e.g. Self)|self|
|url|string|None|False|URL|https://access.redhat.com/security/cve/CVE-2026-48962|
  
**publisher**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|contact_details|string|None|False|Who to contact|user@example.com|
|issuing_authority|string|None|False|Issuer|Red Hat Product Security|
|type|string|None|False|Type of Publisher|vendor|


## Troubleshooting


# Version History

* 2.0.0 - Migrate from the retired Red Hat Security Data API (`/labs/securitydataapi/`, CVRF) to the current endpoint (`/hydra/rest/securitydata/`, CSAF 2.0) | Rename `include_cvrf` input to `include_source` | Change shape of `source`, `publisher` and `references` outputs to CSAF 2.0 format | Change `type` output to a human-readable label (e.g. `Security Advisory`) mapped from CSAF `document.category` | Remove `oval` output (not available in CSAF endpoint) | Persist emitted advisories across polls to prevent duplicate events | Fix plugin title from `Redhat` to `Red Hat` | Update SDK to the latest version (6.6.0)
* 1.0.2 - New spec and help.md format for the Extension Library | Add missing title values for actions in plugin.spec.yaml
* 1.0.1 - Support web server mode
* 1.0.0 - Update to v2 Python plugin architecture
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Red Hat Security Advisories](https://access.redhat.com/security/updates/advisory)
* [Red Hat Security Data API](https://access.redhat.com/security/data)

## References

* [Red Hat Security Data API](https://access.redhat.com/security/data)
* [CSAF 2.0 standard](https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html)