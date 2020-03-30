# Description

[WHOIS](https://en.wikipedia.org/wiki/WHOIS) is a query and response protocol that is widely used for querying
databases that store the registered users or assignee's of an Internet resource, such as a domain name, an IP address
block, or an autonomous system.

# Key Features

* Perform a WHOIS lookup for a provided IP address or domain to gain information on who is responsible for a domain or IP

# Requirements

* _This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Domain Lookup

This action is used to retrieve data about a domain name.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain name to lookup|None|

Example input:

```
{
    "domain": "google.com"
}

```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|creation_date|date|False|Creation date|
|dnssec|string|False|DNSSEC|
|domain_status|[]string|False|Domain status|
|expiration_date|date|False|Expiration date|
|last_updated|date|False|Last updated date|
|name|string|False|Domain name|
|name_servers|[]string|False|Nameservers|
|registrant_cc|string|False|Registrant country|
|registrant_name|string|False|Registrant name|
|registrar|string|False|Domain registrar|
|registrar_abuse_contact_email|string|False|Registrar abuse contact email|
|registrar_abuse_contact_phone|string|False|Registrar abuse Contact phone|
|registrar_iana_id|string|False|Registrar IANA ID|
|registrar_url|string|False|Registrar URL|
|registrar_whois_server|string|False|Registrar WHOIS server|
|registry_domain_id|string|False|Registry domain ID|

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
    "serverupdateprohibited https://icann.org/epp#serverupdateprohibited",
    "clientupdateprohibited (https://www.icann.org/epp#clientupdateprohibited)",
    "clienttransferprohibited (https://www.icann.org/epp#clienttransferprohibited)",
    "clientdeleteprohibited (https://www.icann.org/epp#clientdeleteprohibited)",
    "serverupdateprohibited (https://www.icann.org/epp#serverupdateprohibited)",
    "servertransferprohibited (https://www.icann.org/epp#servertransferprohibited)",
    "serverdeleteprohibited (https://www.icann.org/epp#serverdeleteprohibited)"
  ],
  "expiration_date": "2028-09-13T00:00:00-07:00",
  "last_updated": "2019-09-09T15:39:04",
  "name": "google.com",
  "name_servers": [
    "ns1.google.com",
    "ns2.google.com",
    "ns4.google.com",
    "ns3.google.com"
  ],
  "registrant_cc": "us",
  "registrar": "MarkMonitor Inc.",
  "registrar_abuse_contact_email": "user@example.com",
  "registrar_abuse_contact_phone": "+1.2083895740",
  "registrar_iana_id": "292",
  "registrar_url": "http://www.markmonitor.com",
  "registrar_whois_server": "whois.markmonitor.com",
  "registry_domain_id": "2138514_domain_com-vrsn"
}

```

#### Address Lookup

This action is used to retrieve data about an IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|string|None|True|IP to Lookup|None|

Example input:

```
{
  "address": "8.1.1.1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address|string|False|Address|
|cidr|string|False|CIDR|
|city|string|False|City|
|country|string|False|Country|
|netname|string|False|Network name|
|netrange|string|False|Network Range|
|nettype|string|False|Network type|
|org_abuse_email|string|False|Organization abuse e-mail|
|org_abuse_phone|string|False|Organization abuse phone|
|org_tech_email|string|False|Organization tech e-mail|
|org_tech_phone|string|False|Organization tech phone|
|organization|string|False|Organization|
|orgname|string|False|Organization name|
|postal|string|False|Postal|
|regdate|string|False|Registration date|
|state|string|False|State|
|update|string|False|WHOIS updated date|

Example output:

```

{
  "netrange": "8.8.8.0 - 8.8.8.255",
  "cidr": "8.8.8.0/24",
  "netname": "LVLT-GOGL-8-8-8",
  "nettype": "Reallocated",
  "regdate": "2000-03-30",
  "update": "2019-10-31",
  "orgname": "Google LLC",
  "address": "1600 Amphitheatre Parkway",
  "city": "Mountain View",
  "state": "CA",
  "postal": "94043",
  "country": "US",
  "org_abuse_phone": "+1-650-253-0000",
  "org_abuse_email": "user@example.com",
  "org_tech_phone": "+1-650-253-0000",
  "org_tech_email": "user@example.com"
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Multiple records can be returned by the server, this plugin currently only returns the first unique records found.

# Links

## References

_This plugin has no references._

# Version History

* 1.0.8 - Change docker image from `komand/python-3-37-plugin:3` to `komand/python-3-37-slim-plugin:3` | Use input constants | Changed `Exception` to `PluginException` | Added "f" strings
* 1.0.7 - Upgrade komand/python-whois version to 0.4.2 | Update whois.conf to support .in domains | Updated help.md for the Hub
* 1.0.6 - New spec and help.md format for the Hub
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

## References

* [WHOIS](https://en.wikipedia.org/wiki/WHOIS)
