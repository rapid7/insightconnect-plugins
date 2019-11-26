# Description

Make searching the Rapid7 vulnerability and exploit data fast, easy and efficient with the InsigthConnect plugin. Leverage this curated repository of vetted computer software exploits and exploitable vulnerabilities to ensure your security operations are always aware of the latest threats that could be used against your environment

# Key Features

* Search Database for vulnerabilities

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Search Database

This action is used to search the database for vulnerabilities and exploits.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|database|string|All|True|Name of the database|['Vulnerability Database', 'Metasploit Modules', 'All']|
|search|string|None|True|Search parameter for database|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|search_results|[]vuln_found|False|Vulnerability and exploits found|
|results_found|boolean|True|Will return false if no results are found|

Example output:

```
{
  "search_results": [
    {
      "name": "Cisco ASA SSL VPN Privilege Escalation Vulnerability",
      "link": "https://rapid7com/db/modules/auxiliary/scanner/http/cisco_ssl_vpn_priv_esc",
      "type": "Exploit",
      "summary": "This module exploits a privilege escalation vulnerability for Cisco\n        ASA SSL VPN (aka: WebVPN). It allows level 0 users to escalate to\n        level 15.",
      "published": "April 09, 2014"
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

* 1.1.2 - New spec and help.md format for the Hub
* 1.1.1 - New spec and help.md format for the Hub
* 1.1.0 - Fix issue where Published Date input in the Search Database action would not always parse correctly | Fix issue with memory leaks
* 1.0.1 - Update to v2 Python plugin architecture and support web server mode
* 1.0.0 - Initial plugin

# Links

## References

* [VulnDB](https://www.rapid7.com/db)

