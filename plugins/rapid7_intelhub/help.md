# Description

Access Rapid7 Intelligence Hub for threat intelligence data including CVE information, vulnerabilities, and security insights.

# Key Features

* Search CVE database for vulnerability information
* Retrieve detailed CVE information by ID
* Access threat intelligence data from Rapid7 Intelligence Hub

# Requirements

* Rapid7 Insight Platform API Key

# Supported Product Versions

* v1

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|Rapid7 Insight Platform API Key|None|{"secretKey": "abc123-def456-ghi789"}|None|None|
|region|string|United States|True|The region for your Rapid7 Insight Platform account|["United States", "Europe", "Canada", "Australia", "Japan"]|United States|None|None|

Example input:

```
{
  "api_key": {"secretKey": "abc123-def456-ghi789"},
  "region": "United States"
}
```

## Technical Details

### Actions

#### Search CVEs

This action is used to search the Intelligence Hub CVE database.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page|integer|1|False|Page number for pagination (starts at 1)|None|1|None|None|
|page_size|integer|10|False|Number of results per page (max 100)|None|10|None|None|
|search|string|None|False|Search query to filter CVEs (e.g., CVE ID, keyword, product name)|None|Apache|None|None|

Example input:

```
{
  "page": 1,
  "page_size": 10,
  "search": "Apache"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|cves|[]cve_summary|True|List of CVEs matching the search criteria|[{"cve_id": "CVE-2025-12345", "title": "Example Vulnerability", "severity": "High", "cvss_score": 8.5}]|
|pagination|pagination|False|Pagination information for the results|{"page": 1, "page_size": 10, "total_count": 100, "total_pages": 10}|

Example output:

```
{
  "cves": [
    {
      "cve_id": "CVE-2025-12345",
      "title": "Example Vulnerability",
      "severity": "High",
      "cvss_score": 8.5
    }
  ],
  "pagination": {
    "page": 1,
    "page_size": 10,
    "total_count": 100,
    "total_pages": 10
  }
}
```

#### Get CVE

This action is used to get detailed information about a specific CVE by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cve_id|string|None|True|The CVE identifier to look up (e.g., CVE-2025-12345)|None|CVE-2025-12345|None|None|

Example input:

```
{
  "cve_id": "CVE-2025-12345"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|cve|cve_detail|True|Detailed CVE information|{"cve_id": "CVE-2025-12345", "title": "Example Vulnerability", "description": "A vulnerability in...", "severity": "High", "cvss_score": 8.5}|
|found|boolean|True|Whether the CVE was found|true|

Example output:

```
{
  "cve": {
    "cve_id": "CVE-2025-12345",
    "title": "Example Vulnerability",
    "description": "A vulnerability in...",
    "severity": "High",
    "cvss_score": 8.5
  },
  "found": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Tasks

_This plugin does not contain any tasks._

### Custom Types

#### cve_summary

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CVE ID|string|None|True|The CVE identifier|CVE-2025-12345|
|CVSS Score|number|None|False|CVSS score of the vulnerability|8.5|
|Description|string|None|False|Description of the vulnerability|A vulnerability in...|
|Published Date|string|None|False|Date the CVE was published|2025-01-15|
|Severity|string|None|False|Severity level of the CVE|High|
|Title|string|None|False|Title or name of the CVE|Example Vulnerability|

#### cve_detail

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Affected Products|[]string|None|False|List of affected products|["Apache HTTP Server 2.4.x"]|
|CVE ID|string|None|True|The CVE identifier|CVE-2025-12345|
|CVSS Score|number|None|False|CVSS score of the vulnerability|8.5|
|CVSS Vector|string|None|False|CVSS vector string|CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H|
|Description|string|None|False|Detailed description of the vulnerability|A vulnerability in...|
|Modified Date|string|None|False|Date the CVE was last modified|2025-01-20|
|Published Date|string|None|False|Date the CVE was published|2025-01-15|
|References|[]string|None|False|List of reference URLs|["https://nvd.nist.gov/vuln/detail/CVE-2025-12345"]|
|Severity|string|None|False|Severity level of the CVE|High|
|Title|string|None|False|Title or name of the CVE|Example Vulnerability|

#### pagination

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Page|integer|None|False|Current page number|1|
|Page Size|integer|None|False|Number of results per page|10|
|Total Count|integer|None|False|Total number of results available|100|
|Total Pages|integer|None|False|Total number of pages available|10|

## Troubleshooting

* Ensure your API key has access to Intelligence Hub
* Verify the correct region is selected for your account

# Version History

* 1.0.0 - Initial plugin

# Links

* [Rapid7 Insight Platform](https://insight.rapid7.com)

# References

* [Rapid7 Intelligence Hub](https://www.rapid7.com/products/threat-command/)
