# Description

Make searching the Rapid7 vulnerability and exploit data fast, easy and efficient with the InsightConnect plugin. Leverage this curated repository of vetted computer software exploits and exploitable vulnerabilities to ensure your security operations are always aware of the latest threats that could be used against your environment vulnerabilities

# Key Features

* Search Database for vulnerabilities
* Retrieve vulnerability or Metasploit module details based on a CVE or module identifier

# Requirements


# Supported Product Versions

* v1

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Get Content

This action is used to fetch content record for  vulnerability or module

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|identifier|string|None|True|Rapid7 vulnerability/module identifier|None|apple-itunes-cve-2019-8835|None|None|
  
Example input:

```
{
  "identifier": "apple-itunes-cve-2019-8835"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|content_result|content|True|Content record for the vulnerability or module|{"published_at":"2015-11-05T00:00:00.000Z","references":"mozilla-thunderbird-upgrade-38_4","severity":"7","solutions":"mozilla-thunderbird-upgrade-38_4","title":"MFSA2015-123 Thunderbird: Buffer overflow during i...","alternate_ids":"BID/77411,CVE/2015-7189,DEBIAN/DSA-3393,DEBIAN/DSA...","content_type":"vulnerability","description":"\n    <p>Race condition in the JPEGEncoder function..."}|
  
Example output:

```
{
  "content_result": {
    "alternate_ids": "BID/77411,CVE/2015-7189,DEBIAN/DSA-3393,DEBIAN/DSA...",
    "content_type": "vulnerability",
    "description": "\n    <p>Race condition in the JPEGEncoder function...",
    "published_at": "2015-11-05T00:00:00.000Z",
    "references": "mozilla-thunderbird-upgrade-38_4",
    "severity": "7",
    "solutions": "mozilla-thunderbird-upgrade-38_4",
    "title": "MFSA2015-123 Thunderbird: Buffer overflow during i..."
  }
}
```

#### Search Database

This action is used to search the database to find vulnerabilities and exploits

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|database|string|None|True|Name of the database|["Vulnerability Database", "Metasploit Modules"]|Vulnerability Database|None|None|
|search|string|None|True|Search parameter for database|None|cve-2015-9542|None|None|
  
Example input:

```
{
  "database": "Vulnerability Database",
  "search": "cve-2015-9542"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results_found|bool|True|Will return false if no results are found|None|
|search_results|[]search_result|False|Vulnerability and exploits found|{"identifier":"ubuntu-cve-2015-9542","title":"Ubuntu: (Multiple Advisories) (CVE-2015-9542): libpam-radius-auth vulnerability","published_at":"2020-02-24T00:00:00.000Z","solutions":"ubuntu-upgrade-chromium","link":"https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/content/ubuntu-cve-2015-9542"}|
  
Example output:

```
{
  "results_found": true,
  "search_results": {
    "identifier": "ubuntu-cve-2015-9542",
    "link": "https://vdb-kasf1i23nr1kl2j4.rapid7.com/v1/content/ubuntu-cve-2015-9542",
    "published_at": "2020-02-24T00:00:00.000Z",
    "solutions": "ubuntu-upgrade-chromium",
    "title": "Ubuntu: (Multiple Advisories) (CVE-2015-9542): libpam-radius-auth vulnerability"
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**search_result**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Content Identifier|string|None|False|Content identifier for module or vulnerability|None|
|Link|string|None|False|Link to vulnerability|None|
|Published At|string|None|False|Published date of vulnerability|None|
|Solutions|string|None|False|List of possible solutions for the vulnerability|None|
|Title|string|None|False|Title of vulnerability|None|
  
**content**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alternative Identifiers|string|None|False|List of alternative identifiers for the vulnerability|None|
|architectures|string|None|False|List of applicable architectures for the module|None|
|Authors|string|None|False|List of module authors|None|
|Content type|string|None|False|Type of returned content for module or vulnerability|None|
|Description|string|None|False|Brief summary of the returned content|None|
|Published_at|string|None|False|Published date of vulnerability|None|
|Rank|int|None|False|Rank of module|None|
|References|string|None|False|List of references|None|
|Reliability|string|None|False|Reliability of module|None|
|Severity|string|None|False|Severity of vulnerability|None|
|Solutions|string|None|False|List of possible solutions for the vulnerability|None|
|Title|string|None|False|Title of Vulnerability|None|


## Troubleshooting

* This plugin does not contain any troubleshooting information.

# Version History

* 2.1.8 - Updated SDK to the latest version (6.3.10)
* 2.1.7 - Updated SDK to the latest version (6.3.3)
* 2.1.6 - Updated SDK to the latest version (6.2.5)
* 2.1.5 - Updated SDK to the latest version (v6.2.2) | Address vulnerabilities
* 2.1.4 - Initial updates for fedramp compliance | Updated SDK to the latest version
* 2.1.3 - Fix critical Snyk vulnerability | Update SDK
* 2.1.2 - Bumping SDK version to 5.6.1
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

* [Rapid7 Vulnerability & Exploit Database API Specification](https://vdb.rapid7.com/swagger_doc)

## References

* [Rapid7 Vulnerability & Exploit Database API Specification](https://vdb.rapid7.com/swagger_doc)