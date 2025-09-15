# Description

[WHOIS](https://en.wikipedia.org/wiki/WHOIS) is a query and response protocol that is widely used for querying databases that store the registered users or assignee's of an Internet resource, such as a domain name, an IP address block, or an autonomous system

# Key Features

* Perform a WHOIS lookup for a provided IP address or domain to gain information on who is responsible for a domain or IP

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2024-09-09

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Address Lookup
  
This action is used to retrieve data about an IP address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|IP to Lookup|None|198.51.100.100|None|None|
|registrar|string|Autodetect|False|Domain Registrar|["Autodetect", "RIPE", "ARIN", "LACNIC", "APNIC"]|Autodetect|None|None|
  
Example input:

```
{
  "address": "198.51.100.100",
  "registrar": "Autodetect"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|address|string|False|Address|1025 Eldorado Blvd.|
|cidr|string|False|CIDR|8.0.0.0/8|
|city|string|False|City|Broomfield|
|country|string|False|Country|US|
|netname|string|False|Network name|LVLT-ORG-8-8|
|netrange|string|False|Network Range|8.0.0.0 - 8.255.255.255|
|nettype|string|False|Network type|Direct Allocation|
|org_abuse_email|string|False|Organization abuse e-mail|user@example.com|
|org_abuse_phone|string|False|Organization abuse phone|+1-877-453-8353 |
|org_tech_email|string|False|Organization tech e-mail|user@example.com|
|org_tech_phone|string|False|Organization tech phone|+1-877-453-8353 |
|organization|string|False|Organization|Level 3 Communications, Inc. (LVLT)|
|orgname|string|False|Organization name|Level 3 Communications, Inc.|
|postal|string|False|Postal|80021|
|regdate|string|False|Registration date|1992-12-01|
|state|string|False|State|CO|
|update|string|False|WHOIS updated date|2012-02-24|
  
Example output:

```
{
  "address": "1025 Eldorado Blvd.",
  "cidr": "8.0.0.0/8",
  "city": "Broomfield",
  "country": "US",
  "netname": "LVLT-ORG-8-8",
  "netrange": "8.0.0.0 - 8.255.255.255",
  "nettype": "Direct Allocation",
  "org_abuse_email": "user@example.com",
  "org_abuse_phone": "+1-877-453-8353 ",
  "org_tech_email": "user@example.com",
  "org_tech_phone": "+1-877-453-8353 ",
  "organization": "Level 3 Communications, Inc. (LVLT)",
  "orgname": "Level 3 Communications, Inc.",
  "postal": 80021,
  "regdate": "1992-12-01",
  "state": "CO",
  "update": "2012-02-24"
}
```

#### Domain Lookup
  
This action is used to retrieve data about a domain name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name to lookup|None|rapid7.com|None|None|
  
Example input:

```
{
  "domain": "rapid7.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|creation_date|date|False|Creation date|1997-09-15T04:00:00|
|dnssec|string|False|DNSSEC|unsigned|
|domain_status|[]string|False|Domain status|["clientdeleteprohibited https://icann.org/epp#clientdeleteprohibited", "clienttransferprohibited https://icann.org/epp#clienttransferprohibited", "clientupdateprohibited https://icann.org/epp#clientupdateprohibited", "serverdeleteprohibited https://icann.org/epp#serverdeleteprohibited", "servertransferprohibited https://icann.org/epp#servertransferprohibited", "serverupdateprohibited https://icann.org/epp#serverupdateprohibited"]|
|expiration_date|date|False|Expiration date||
|last_updated|date|False|Last updated date||
|name|string|False|Domain name|google.com|
|name_servers|[]string|False|Nameservers|["ns2.google.com", "ns3.google.com", "ns1.google.com", "ns4.google.com"]|
|registrant_cc|string|False|Registrant country|US|
|registrant_name|string|False|Registrant name||
|registrar|string|False|Domain registrar|MarkMonitor Inc.|
|registrar_abuse_contact_email|string|False|Registrar abuse contact email|user@example.com|
|registrar_abuse_contact_phone|string|False|Registrar abuse Contact phone|+1.2083895740|
|registrar_iana_id|string|False|Registrar IANA ID|292|
|registrar_url|string|False|Registrar URL|http://www.markmonitor.com|
|registrar_whois_server|string|False|Registrar WHOIS server|whois.markmonitor.com|
|registry_domain_id|string|False|Registry domain ID|2138514_domain_com-vrsn|
  
Example output:

```
{
  "creation_date": "1997-09-15T04:00:00",
  "dnssec": "unsigned",
  "domain_status": [
    "clientdeleteprohibited https://icann.org/epp#clientdeleteprohibited",
    "clienttransferprohibited https://icann.org/epp#clienttransferprohibited",
    "clientupdateprohibited https://icann.org/epp#clientupdateprohibited",
    "serverdeleteprohibited https://icann.org/epp#serverdeleteprohibited",
    "servertransferprohibited https://icann.org/epp#servertransferprohibited",
    "serverupdateprohibited https://icann.org/epp#serverupdateprohibited"
  ],
  "expiration_date": "",
  "last_updated": "",
  "name": "google.com",
  "name_servers": [
    "ns2.google.com",
    "ns3.google.com",
    "ns1.google.com",
    "ns4.google.com"
  ],
  "registrant_cc": "US",
  "registrant_name": "",
  "registrar": "MarkMonitor Inc.",
  "registrar_abuse_contact_email": "user@example.com",
  "registrar_abuse_contact_phone": "+1.2083895740",
  "registrar_iana_id": 292,
  "registrar_url": "http://www.markmonitor.com",
  "registrar_whois_server": "whois.markmonitor.com",
  "registry_domain_id": "2138514_domain_com-vrsn"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* Multiple records can be returned by the server, this plugin currently only returns the first unique records found.

# Version History

* 3.1.10 - Updated SDK to the latest version (6.3.10)
* 3.1.9 - Updated SDK to the latest version (6.3.3)
* 3.1.8 - Updated SDK to the latest version (6.2.5)
* 3.1.7 - Updated SDK to the latest version (v6.2.3) | Address vulnerabilities | Updated `Whois` dependency
* 3.1.6 - Fix mapping issue (RIPE) for address action. Adding 'description' output field for RIPE (address action) | SDK bump to 6.2.0
* 3.1.5 - Action `Address`: Fixed issue with result parsing
* 3.1.4 - Initial updates for fedramp compliance | Updated SDK to the latest version
* 3.1.3 - Updated SDK to the latest version (v6.0.0) | Bump setuptools version to v70.0.0
* 3.1.2 - Updated SDK to the latest version | Added validation for input parameters
* 3.1.1 - Add empty `__init__.py` file to `unit_test` folder | Refresh with new tooling
* 3.1.0 - Add support for `.monster` and `.nl` domains
* 3.0.3 - Add PluginException in Domain and Address action when response is empty
* 3.0.2 - Support non-UTF-8 responses in the Address action
* 3.0.1 - Clean up help.md formatting
* 3.0.0 - Add input `registrar` for manual server selection to Address Lookup action
* 2.0.3 - Upgrade to latest Python plugin runtime | Define `cloud_ready` in spec
* 2.0.2 - Fix issue where com.br style domains could crash the plugin
* 2.0.1 - Update to v4 Python plugin runtime
* 2.0.0 - Add example inputs | Fix capitalization in the title of the `last_updated` output.
* 1.0.7 - Upgrade komand/python-whois version to 0.4.2 | Update whois.conf to support .in domains | Updated help.md for the Extension Library
* 1.0.6 - New spec and help.md format for the Extension Library
* 1.0.5 - Upgrade komand/python-whois version to 0.4.1 | Upgrade SDK
* 1.0.4 - Fix variable name in domain lookup
* 1.0.3 - Handle instances where domain name is prefixed with a protocol
* 1.0.2 - Fix typo in plugin spec
* 1.0.1 - Add support for LACNIC, APNIC, RIPE registries
* 1.0.0 - Support web server mode
* 0.3.3 - Bug fix for CI tool incorrectly uploading plugins
* 0.3.2 - Added new date formats
* 0.3.1 - Update to v2 Python plugin architecture
* 0.3.0 - Support for more TLDs
* 0.2.1 - SSL bug fix in SDK
* 0.2.0 - Fix domain query and adjust output
* 0.1.1 - Bugfixes and pagination support
* 0.1.0 - Initial plugin

# Links

* [WHOIS](https://en.wikipedia.org/wiki/WHOIS)

## References

* [WHOIS](https://en.wikipedia.org/wiki/WHOIS)