# Description

Access Rapid7 Intelligence Hub for threat intelligence data including CVE information, vulnerabilities, and security insights

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
  "api_key": {
    "secretKey": "abc123-def456-ghi789"
  },
  "region": "United States"
}
```

## Technical Details

### Actions


#### Get CVE

This action is used to get detailed information about a specific CVE by ID

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
|found|boolean|True|Whether the CVE was found|True|
  
Example output:

```
{
  "cve": {
    "cve_id": "CVE-2025-12345",
    "cvss_score": 8.5,
    "description": "A vulnerability in...",
    "severity": "High",
    "title": "Example Vulnerability"
  },
  "found": true
}
```

#### Get Threat Actor

This action is used to get detailed information about a specific threat actor by UUID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|uuid|string|None|True|The threat actor UUID to look up|None|db2101df-e979-433c-b598-17b45d5aeca7|None|None|
  
Example input:

```
{
  "uuid": "db2101df-e979-433c-b598-17b45d5aeca7"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|True|Whether the threat actor was found|True|
|threat_actor|object|True|Detailed threat actor information|{"name": "MuddyWater", "description": "Iranian APT group...", "aliases": ["TA450"]}|
  
Example output:

```
{
  "found": true,
  "threat_actor": {
    "aliases": [
      "TA450"
    ],
    "description": "Iranian APT group...",
    "name": "MuddyWater"
  }
}
```

#### Get Threat Actor CVEs

This action is used to get CVEs associated with a specific threat actor

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page|integer|1|False|Page number for pagination (starts at 1)|None|1|None|None|
|page_size|integer|10|False|Number of results per page (max 100)|None|10|None|None|
|uuid|string|None|True|The threat actor UUID to look up CVEs for|None|db2101df-e979-433c-b598-17b45d5aeca7|None|None|
  
Example input:

```
{
  "page": 1,
  "page_size": 10,
  "uuid": "db2101df-e979-433c-b598-17b45d5aeca7"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|cves|[]object|True|List of CVEs associated with the threat actor|[{"id": "CVE-2023-27350", "last_updated": "2025-11-04T10:27:38Z"}]|
|pagination|pagination|False|Pagination information for the results|{"page": 1, "page_size": 10, "total_count": 3, "total_pages": 1}|
  
Example output:

```
{
  "cves": [
    {
      "id": "CVE-2023-27350",
      "last_updated": "2025-11-04T10:27:38Z"
    }
  ],
  "pagination": {
    "page": 1,
    "page_size": 10,
    "total_count": 3,
    "total_pages": 1
  }
}
```

#### Search CVEs

This action is used to search the Intelligence Hub CVE database

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cisa_kev|boolean|None|False|Filter by CISA Known Exploited Vulnerabilities catalog|None|True|None|None|
|cvss_score|string|None|False|Filter by CVSS severity level|["", "critical", "high", "medium", "low"]|high|None|None|
|epss_score|string|None|False|Filter by EPSS score range (e.g., 0-0.5, 0.5-1)|None|0-0.5|None|None|
|exploitable|boolean|None|False|Filter by whether the CVE is exploitable|None|True|None|None|
|last_updated|string|None|False|Filter by last updated time range (e.g., 'last 24 hours', 'last 72 hours', 'last 7 days')|None|last 24 hours|None|None|
|page|integer|1|False|Page number for pagination (starts at 1)|None|1|None|None|
|page_size|integer|10|False|Number of results per page (max 100)|None|10|None|None|
|search|string|None|False|Search query to filter CVEs (e.g., CVE ID, keyword)|None|CVE-2024|None|None|
  
Example input:

```
{
  "cisa_kev": true,
  "cvss_score": "high",
  "epss_score": "0-0.5",
  "exploitable": true,
  "last_updated": "last 24 hours",
  "page": 1,
  "page_size": 10,
  "search": "CVE-2024"
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
      "cvss_score": 8.5,
      "severity": "High",
      "title": "Example Vulnerability"
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

#### Search Threat Actors

This action is used to search the Intelligence Hub threat actor database

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page|integer|1|False|Page number for pagination (starts at 1)|None|1|None|None|
|page_size|integer|10|False|Number of results per page (max 100)|None|10|None|None|
|search|string|None|False|Search query to filter threat actors by name or alias|None|APT28|None|None|
  
Example input:

```
{
  "page": 1,
  "page_size": 10,
  "search": "APT28"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|pagination|pagination|False|Pagination information for the results|{"page": 1, "page_size": 10, "total_count": 135, "total_pages": 14}|
|threat_actors|[]object|True|List of threat actors matching the search criteria|[{"name": "APT28", "aliases": ["Fancy Bear"], "nationalities": ["RU"]}]|
  
Example output:

```
{
  "pagination": {
    "page": 1,
    "page_size": 10,
    "total_count": 135,
    "total_pages": 14
  },
  "threat_actors": [
    {
      "aliases": [
        "Fancy Bear"
      ],
      "name": "APT28",
      "nationalities": [
        "RU"
      ]
    }
  ]
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**cve_summary**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CVE ID|string|None|True|The CVE identifier|None|
|CVSS Score|number|None|False|CVSS score of the vulnerability|None|
|Description|string|None|False|Description of the vulnerability|None|
|Published Date|string|None|False|Date the CVE was published|None|
|Severity|string|None|False|Severity level of the CVE|None|
|Title|string|None|False|Title or name of the CVE|None|
  
**cve_detail**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Affected Products|[]string|None|False|List of affected products|None|
|CVE ID|string|None|True|The CVE identifier|None|
|CVSS Score|number|None|False|CVSS score of the vulnerability|None|
|CVSS Vector|string|None|False|CVSS vector string|None|
|Description|string|None|False|Detailed description of the vulnerability|None|
|Modified Date|string|None|False|Date the CVE was last modified|None|
|Published Date|string|None|False|Date the CVE was published|None|
|References|[]string|None|False|List of reference URLs|None|
|Severity|string|None|False|Severity level of the CVE|None|
|Title|string|None|False|Title or name of the CVE|None|
  
**pagination**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Page|integer|None|False|Current page number|None|
|Page Size|integer|None|False|Number of results per page|None|
|Total Count|integer|None|False|Total number of results available|None|
|Total Pages|integer|None|False|Total number of pages available|None|


## Troubleshooting

* Ensure your API key has access to Intelligence Hub
* Verify the correct region is selected for your account

# Version History

* 1.0.0 - Initial plugin

# Links

* [Rapid7 Insight Platform](https://insight.rapid7.com)

## References

* [Rapid7 Intelligence Hub](https://docs.rapid7.com/intelligence-hub/)