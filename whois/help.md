# Description

[WHOIS](https://en.wikipedia.org/wiki/WHOIS) is a query and response protocol that is widely used for querying databases that store the registered users
or assignees of an Internet resource, such as a domain name, an IP address block, or an autonomous system, but is also used for a wider range of other information.

The WHOIS plugin enables address and domain lookups in the WHOIS databases.

# Key Features

* Query for an address
* Query for a URL

# Requirements

* _This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Domain Lookup

This action is used to retrieve data about a domain name.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain name to lookup|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|last_updated|date|False|None|
|dnssec|string|False|None|
|creation_date|date|False|None|
|registrar_whois_server|string|False|None|
|domain_status|[]string|False|None|
|name_servers|[]string|False|None|
|registrar_abuse_contact_phone|string|False|None|
|registrar_url|string|False|None|
|registrant_name|string|False|None|
|name|string|False|None|
|registrant_cc|string|False|None|
|expiration_date|date|False|None|
|registrar|string|False|None|
|registry_domain_id|string|False|None|
|registrar_abuse_contact_email|string|False|None|
|registrar_iana_id|string|False|None|

Example output:

```

{
  "registrar_whois_server": "whois.markmonitor.com",
  "registry_domain_id": "2138514_domain_com-vrsn",
  "last_updated": "2011-07-20T16:55:31",
  "registrar_iana_id": "292",
  "registrar": "MarkMonitor Inc.",
  "dnssec": "unsigned",
  "domain_status": ["clientdeleteprohibited https://icann.org/epp#clientdeleteprohibited", "clienttransferprohibited https://icann.org/epp#clienttransferprohibited", "clientupdateprohibited https://icann.org/epp#clientupdateprohibited", "serverdeleteprohibited https://icann.org/epp#serverdeleteprohibited", "servertransferprohibited https://icann.org/epp#servertransferprohibited", "serverupdateprohibited https://icann.org/epp#serverupdateprohibited"],
  "registrar_url": "http://www.markmonitor.com",
  "creation_date": "1997-09-15T04:00:00",
  "name_servers": ["ns2.google.com", "ns3.google.com", "ns1.google.com", "ns4.google.com"],
  "registrar_abuse_contact_email": "abusecomplaints@markmonitor.com",
  "registrar_abuse_contact_phone": "+1.2083895740",
  "name": "google.com"
}

```

#### Address Lookup

This action is used to retrieve data about an IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|string|None|True|IP to Lookup|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|netname|string|False|None|
|update|string|False|None|
|org_abuse_email|string|False|None|
|address|string|False|None|
|cidr|string|False|None|
|postal|string|False|None|
|org_tech_email|string|False|None|
|city|string|False|None|
|netrange|string|False|None|
|country|string|False|None|
|regdate|string|False|None|
|org_tech_phone|string|False|None|
|orgname|string|False|None|
|state|string|False|None|
|org_abuse_phone|string|False|None|
|nettype|string|False|None|
|organization|string|False|None|

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
  "org_abuse_email": "security@level3.com",
  "org_abuse_phone": "+1-877-453-8353 ",
  "org_tech_email": "ipaddressing@level3.com",
  "org_tech_phone": "+1-877-453-8353 ",
  "organization": "Level 3 Communications, Inc. (LVLT)",
  "orgname": "Level 3 Communications, Inc.",
  "postal": "80021",
  "regdate": "1992-12-01",
  "state": "CO",
  "update": "2012-02-24"
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Multiple records can be returned by the server, this plugin currently only returns the first unique records found.

# Links

## References

_This plugin has no references._

# Version History

* 1.0.7 - New spec and help.md format for the Hub
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
