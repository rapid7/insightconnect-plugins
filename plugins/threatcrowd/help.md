# Description

[AlienVault ThreatCrowd](https://www.threatcrowd.org/) is an open source search engine for threats.
Using the Threat Crowd plugin for Rapid7 InsightConnect, users can search by domain, IP address, email address,
and other information to discover and enrich information about threats in real-time.

# Key Features

* Gather threat intelligence about MD5 or SHA1 hashes, IP addresses, antivirus software, domain names, and email addresses
* Submit votes for malicious indicators

# Requirements

_This plugin does not contain any requirements._

# Supported Product Versions

* Threatcrowd API 2022-11-02

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ssl_verification|boolean|True|True|Indicates whether to verify SSL certificate or not|None|True|

Example input:

```
{
  "ssl_verification": true
}
```

## Technical Details

### Actions

#### Vote

This action is used to submit votes for malicious entities.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|entity|string|None|True|URL, Email or IP|None|user@example.com|
|vote|boolean|None|True|Vote malicious|None|False|

Example input:

```
{
  "entity": "user@example.com",
  "vote": false
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|True|Status code, 200 is successful|

Example output:

```
{
  "status": "200"
}
```

#### Hash Lookup

This action is used to search a hash string for malicious threats.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|Hash to search - MD5 and SHA1 supported|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domains|[]string|False|List of domains|
|found|boolean|True|Whether search returned results|
|hashes|hash|False|List of hashes|
|ips|[]string|False|List of IP addresses|
|permalink|string|False|Permalink URL|
|references|[]string|False|List of references|
|scans|[]string|False|List of scans|

Example output:

```
{
  "domains": [
    "hpservice.homepc.it",
    "facebook.controlliamo.com"
  ],
  "found": true,
  "hashes": {
    "md5": "31d0e421894004393c48de1769744687",
    "sha1": "4f0eb746d81a616fb9bdff058997ef47a4209a76"
  },
  "ips": [
    "8.8.8.8"
  ],
  "permalink": "https://www.threatcrowd.org/malware.php?md5=31d0e421894004393c48de1769744687",
  "references": [],
  "scans": [
    "Error Scanning File",
    "Malware-gen*Win32*Malware-gen",
    "Gen*Variant.Symmi.50061",
    "W32/Trojan.VSQD-1927",
    "BDS/Plugx.266990",
    "Gen*Variant.Symmi.50061",
    "Gen*Variant.Symmi.50061",
    "Win32/Korplug.CF",
    "W32/FakeAV.CX",
    "Generic11_c.CDQL",
    "Trojan.SuspectCRC*Backdoor.Win32.Gulpix",
    "Riskware ( 0040eff71 )",
    "Trojan.Win32.Generic*Backdoor.Win32.Gulpix.yk",
    "Backdoor*Win32/Plugx",
    "Gen*Variant.Symmi.50061[ZP]"
  ]
}
```

#### Email Lookup

This action is used to search a email for malicious threats.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|Email to search|None|user@example.com|

Example input:

```
{
  "email": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domains|[]string|False|List of domains|
|found|boolean|True|Whether search returned results|
|permalink|string|False|Permalink URL|
|references|[]string|False|List of references|

Example output:

```
{
  "domains": [
    "porta-kiln.com"
  ],
  "found": true,
  "permalink": "https://www.threatcrowd.org/email.php?email=user@example.com",
  "references": []
}
```

#### Domain Lookup

This action is used to search a domain for malicious threats.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|True|Domain to search|None|https://example.com|

Example input:

```
{
  "domain": "https://example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domains|[]resolutions|False|List of domains|
|emails|[]string|False|List of emails|
|found|boolean|True|Whether search returned results|
|hashes|[]string|False|List of hashes|
|malicious|string|False|Category|
|permalink|string|False|Permalink URL|
|references|[]string|False|List of references|
|subdomains|[]string|False|List of subdomains|

Example output:

```
{
  "domains": [
    {
      "ip_address": "-",
      "last_resolved": "2016-02-17"
    },
    {
      "ip_address": "198.51.100.1",
      "last_resolved": "2017-03-03"
    },
    {
      "ip_address": "198.51.100.1",
      "last_resolved": "2018-04-30"
    },
    {
      "ip_address": "198.51.100.1",
      "last_resolved": "2020-07-24"
    },
    {
      "ip_address": "198.51.100.1",
      "last_resolved": "2019-12-28"
    },
    {
      "ip_address": "198.51.100.1",
      "last_resolved": "2017-07-13"
    }
  ],
  "emails": [
    "user@example.com"
  ],
  "found": true,
  "hashes": [],
  "malicious": "Malicious",
  "permalink": "https://www.threatcrowd.org/domain.php?domain=1119.leke.cn",
  "references": [],
  "subdomains": []
}

```

#### AntiVirus Lookup

This action is used to search for known malicious antiviruses.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|antivirus|string|None|True|Antivirus to search|None|plugx|

Example input:

```
{
  "antivirus": "plugx"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|True|Whether search returned results|
|hashes|[]string|False|List of hashes|
|permalink|string|False|Permalink URL|
|references|[]string|False|List of references|

Example output:

```
{
  "found": true,
  "hashes": [
      "31d0e421894004393c48de1769744687",
      "5cd3f073caac28f915cf501d00030b31",
      "bbd9acdd758ec2316855306e83dba469",
      "ef9d8cd06de03bd5f07b01c1cce9761f",
      "06bd026c77ce6ab8d85b6ae92bb34034",
      "2af64ba808c79dccd2c1d84f010b22d7"
  ],
  "permalink": "https://www.threatcrowd.org/listMalware.php?antivirus=plugx",
  "references": []
}

```

#### Address Lookup

This action is used to search an IP for malicious threats.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain|string|None|True|IP to search|None|198.51.100.1|

Example input:

```
{
  "domain": "198.51.100.1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domains|[]domains|False|List of domains|
|found|boolean|True|Whether search returned results|
|hashes|[]string|False|List of hashes|
|malicious|string|False|Category|
|permalink|string|False|Permalink URL|
|references|[]string|False|List of references|
|resolutions|[]string|False|List of resolutions|

Example output:

```
{
  "domains": [
    {
      "domain": "example.com",
      "last_resolved": "2018-09-03"
    },
    {
      "domain": "example2.com",
      "last_resolved": "2018-07-14"
    },
    {
      "domain": "example3.com",
      "last_resolved": "2020-06-17"
    }
  ],
  "found": true,
  "hashes": [],
  "malicious": "50/50 chance malicious",
  "permalink": "https://www.threatcrowd.org/ip.php?ip=13.33.17.182",
  "references": []
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

All lookup actions return a boolean variable called `found` that contains either `true` or `false` as a value.
This variable can be used in automated decisions to check if ThreatCrowd has information on a host before trying to do something with it.

# Version History

* 4.0.0 - Connection: Add SSL Verification boolean field that indicates whether to verify SSL certificate or not | Add unittests
* 3.0.3 - Add PluginException for case 'Too many connections' response from server | Change IP address in api.py file
* 3.0.2 - Add source and license URLs in plugin spec | Set `USER` to `nobody` in Dockerfile
* 3.0.1 - Add Hash input conversion to lowercase in the Hash action to match API requirements
* 3.0.0 - Update to use the `insightconnect-python-3-38-plugin:4` Docker image | Improve error handling | Changed `Exception` to `PluginException` | Update actions to return appropriate JSON | Move test from actions to connection | Update plugin.spec.yaml to include `cloud_ready` | Use input and output constants | Add example input and output | Added "f" strings | Rename `search_hash` input in Hash Lookup action to `hash`
* 2.0.2 - Updated help.md for the Extension Library
* 2.0.1 - New spec and help.md format for the Extension Library
* 2.0.0 - Rename "Antivirus Lookup" to "AntiVirus Lookup"
* 1.0.0 - Fix locking bug where actions hang indefinitely | Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [ThreatCrowd](https://www.threatcrowd.org/)
* [ThreatCrowd API](https://github.com/AlienVault-OTX/ApiV2)
