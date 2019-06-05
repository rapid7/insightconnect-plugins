
# Rapid7 Vulnerability & Exploit Database

## About

Rapid7's [Vulndb](https://www.rapid7.com/db) is a curated repository of vetted computer software exploits and exploitable vulnerabilities. Technical details for over 70,000 vulnerabilities and 3,000 exploits are available for security professionals and researchers to review. These vulnerabilities are utilized by our vulnerability management tool Nexpose. The exploits are all included in the Metasploit framework and utilized by our penetration testing tool, Metasploit Pro. Our vulnerability and exploit database is updated frequently and contains the most recent security research.

## Actions

### Search Database

This action is used to search the database for vulnerabilities and exploits.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|database|string|All|True|Name of the database|['Vulnerability Database', 'Metasploit Modules', 'All']|
|search|string|None|True|Search parameter for database|None|

#### Output

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

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Search for vulnerabilities and exploits.

## Versions

* 1.0.0 - Initial plugin
* 1.0.1 - Update to v2 Python plugin architecture and support web server mode
* 1.1.0 - Fix issue where Published Date input in the Search Database action would not always parse correctly | Fix issue with memory leaks

## References

* [VulnDB](https://www.rapid7.com/db)
