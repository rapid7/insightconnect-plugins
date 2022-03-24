# Description

Make searching the Rapid7 vulnerability and exploit data fast, easy and efficient with the InsightConnect plugin. Leverage this curated repository of vetted computer software exploits and exploitable vulnerabilities to ensure your security operations are always aware of the latest threats that could be used against your environment

# Key Features

* Search Database for vulnerabilities
* Retrieve vulnerability or Metasploit module details based on a CVE or module identifier

# Requirements

_This plugin does not contain any requirements._

# Supported Product Versions

* v1

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Search Database

This action is used to search the database to find vulnerabilities and exploits.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|database|string|None|True|Name of the database|['Vulnerability Database', 'Metasploit Modules']|Vulnerability Database|
|search|string|None|True|Search parameter for database|None|cve-2015-9542|

Example input:

```
{
  "database": "Vulnerability Database",
  "search": "cve-2015-9542"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results_found|bool|True|Will return false if no results are found|
|search_results|[]search_result|False|Vulnerability and exploits found|

Example output:

```
{
  "results_found": true,
  "search_results": [
    {
      "identifier": "ubuntu-cve-2015-9542",
      "title": "Ubuntu: (Multiple Advisories) (CVE-2015-9542): libpam-radius-auth vulnerability",
      "published_at": "2020-02-24T00:00:00.000Z",
      "solutions": "ubuntu-upgrade-chromium",
      "link": "https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/content/ubuntu-cve-2015-9542"
    }
  ]
}
```

#### Get Content

This action is used to fetch content results for a vulnerability or module.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|identifier|string|None|True|Rapid7 vulnerability/module identifier|None|apple-itunes-cve-2019-8835|

Example input:

```
{
  "identifier": "apple-itunes-cve-2019-8835"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|content_result|content|True|Content record for the vulnerability or module|

Example output:

```
{
  "content_result": {
    "published_at": "2015-11-05T00:00:00.000Z",
    "references": "mozilla-thunderbird-upgrade-38_4",
    "severity": "7",
    "solutions": "mozilla-thunderbird-upgrade-38_4",
    "title": "MFSA2015-123 Thunderbird: Buffer overflow during i...",
    "alternate_ids": "BID/77411,CVE/2015-7189,DEBIAN/DSA-3393,DEBIAN/DSA...",
    "content_type": "vulnerability",
    "description": "\n    <p>Race condition in the JPEGEncoder function..."
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### content

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Alternative identifiers|string|False|List of alternative identifiers of vulnerability|
|architectures|string|False|List of applicable architectures for the module|
|Authors|string|False|List of module authors|
|Content type|string|False|Type of returned content, module or vulnerability|
|Description|string|False|Brief summary of the returned content|
|Published_at|string|False|Published date of vulnerability|
|Rank|int|False|Rank of module|
|References|string|False|List of references|
|Reliability|string|False|Reliability of module|
|Severity|string|False|Severity of vulnerability|
|Solutions|string|False|List of possible solutions for vulnerability|
|Title|string|False|Title of Vulnerability|

#### search_result

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Link|string|False|Link to vulnerability|
|Published_at|string|False|Published date of vulnerability|
|Title|string|False|Title of Vulnerability|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.1.1 - Add 404 and 504 error handlers | Add retry
* 2.1.0 - Return list of vulnerability solutions in the Search Database action with new `solutions` output field
* 2.0.4 - Correct spelling in help.md
* 2.0.3 - Update to v4 Python plugin runtime | Add example inputs
* 2.0.2 - Implement workaround for VulnDB API bug in Get Content action where the `severity` datatype response differs based on the action input
* 2.0.1 - Add identifier field to the Search Database action
* 2.0.0 - Utilize VulnDB API
* 1.1.1 - New spec and help.md format for the Extension Library
* 1.1.0 - Fix issue where Published Date input in the Search Database action would not always parse correctly | Fix issue with memory leaks
* 1.0.1 - Update to v2 Python plugin architecture and support web server mode
* 1.0.0 - Initial plugin

# Links

## References

* [Rapid7 Vulnerability & Exploit Database API Specification](https://vdb.rapid7.com/swagger_doc)
