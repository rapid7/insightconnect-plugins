# Description

Access Rapid7 Intelligence Hub for threat intelligence data including CVE information, vulnerabilities, and security insights

# Key Features

* Search CVE database for vulnerability information
* Retrieve detailed CVE information by ID
* Access threat intelligence data from Rapid7 Intelligence Hub

# Requirements

* Rapid7 Insight Platform API Key
* An InsightIDR or Intelligence Hub license for the organization that owns the API key

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
|cve_id|string|None|True|The CVE identifier to look up (e.g., CVE-2024-3400)|None|CVE-2024-3400|None|None|
  
Example input:

```
{
  "cve_id": "CVE-2024-3400"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|cve|cve|True|Detailed CVE information|{"cve_id": "CVE-2024-3400", "title": "CVE-2024-3400: Improper Neutralization of Special Elements used in a Command", "published_date": "2024-04-12T00:00:00", "modified_date": "2025-11-21T00:00:00", "cvss_v3_base_score": 10.0, "cvss_v3_severity": "Critical", "cvss_v3_vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H", "epss_score": 0.94297, "epss_percentile": 0.9994, "active_risk_score": 1000, "exploitable": true, "exploited_in_the_wild": true, "cisa_kev": true, "campaign_count": 9, "threat_actor_count": 3, "references": [], "description": "A command injection as a result of arbitrary file creation vulnerability in the GlobalProtect feature of Palo Alto Networks PAN-OS software for specific PAN-OS versions and distinct feature configurations may enable an unauthenticated attacker to execute arbitrary code with root privileges on the firewall.\n\nCloud NGFW, Panorama appliances, and Prisma Access are not impacted by this vulnerability.", "tags": ["Remote Execution", "CISA KEV", "Exploited in the Wild", "Rapid7 Critical"]}|
|found|boolean|True|Whether the CVE was found|True|
  
Example output:

```
{
  "cve": {
    "active_risk_score": 1000,
    "campaign_count": 9,
    "cisa_kev": true,
    "cve_id": "CVE-2024-3400",
    "cvss_v3_base_score": 10.0,
    "cvss_v3_severity": "Critical",
    "cvss_v3_vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",
    "description": "A command injection as a result of arbitrary file creation vulnerability in the GlobalProtect feature of Palo Alto Networks PAN-OS software for specific PAN-OS versions and distinct feature configurations may enable an unauthenticated attacker to execute arbitrary code with root privileges on the firewall.\n\nCloud NGFW, Panorama appliances, and Prisma Access are not impacted by this vulnerability.",
    "epss_percentile": 0.9994,
    "epss_score": 0.94297,
    "exploitable": true,
    "exploited_in_the_wild": true,
    "modified_date": "2025-11-21T00:00:00",
    "published_date": "2024-04-12T00:00:00",
    "references": [],
    "tags": [
      "Remote Execution",
      "CISA KEV",
      "Exploited in the Wild",
      "Rapid7 Critical"
    ],
    "threat_actor_count": 3,
    "title": "CVE-2024-3400: Improper Neutralization of Special Elements used in a Command"
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
|cvss_score|string|None|False|Filter by CVSS severity level|["", "critical", "high", "medium", "low", "informational"]|high|None|None|
|epss_score|string|None|False|Filter by EPSS score range (e.g., 0-0.5, 0.5-1)|None|0-0.5|None|None|
|exploitable|boolean|None|False|Filter by whether the CVE is exploitable|None|True|None|None|
|last_updated|string|None|False|Filter by the time range in which the CVE was last updated|["", "last 20 minutes", "last 1 hour", "last 6 hours", "last 12 hours", "last 24 hours", "last 48 hours", "last 72 hours"]|last 24 hours|None|None|
|page|integer|1|False|Page number for pagination (starts at 1)|None|1|None|None|
|page_size|integer|10|False|Number of results per page (max 100)|None|10|None|None|
|search|string|None|False|Part of the CVE ID to search for, such as CVE-2024 or 3400|None|CVE-2024|None|None|
  
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
|cves|[]cve|True|List of CVEs matching the search criteria|[{"cve_id": "CVE-2024-3400", "title": "CVE-2024-3400: Improper Neutralization of Special Elements used in a Command", "published_date": "2024-04-12T00:00:00", "modified_date": "2025-11-21T00:00:00", "cvss_v3_base_score": 10.0, "cvss_v3_severity": "Critical", "cvss_v3_vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H", "epss_score": 0.94297, "epss_percentile": 0.9994, "active_risk_score": 1000, "exploitable": true, "exploited_in_the_wild": true, "cisa_kev": true, "campaign_count": 9, "threat_actor_count": 3, "references": [], "description": "A command injection as a result of arbitrary file creation vulnerability in the GlobalProtect feature of Palo Alto Networks PAN-OS software for specific PAN-OS versions and distinct feature configurations may enable an unauthenticated attacker to execute arbitrary code with root privileges on the firewall.\n\nCloud NGFW, Panorama appliances, and Prisma Access are not impacted by this vulnerability.", "tags": ["Remote Execution", "CISA KEV", "Exploited in the Wild", "Rapid7 Critical"]}]|
|pagination|pagination|False|Pagination information for the results|{"page": 1, "page_size": 10, "total_count": 100, "total_pages": 10}|
  
Example output:

```
{
  "cves": [
    {
      "active_risk_score": 1000,
      "campaign_count": 9,
      "cisa_kev": true,
      "cve_id": "CVE-2024-3400",
      "cvss_v3_base_score": 10.0,
      "cvss_v3_severity": "Critical",
      "cvss_v3_vector": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H",
      "description": "A command injection as a result of arbitrary file creation vulnerability in the GlobalProtect feature of Palo Alto Networks PAN-OS software for specific PAN-OS versions and distinct feature configurations may enable an unauthenticated attacker to execute arbitrary code with root privileges on the firewall.\n\nCloud NGFW, Panorama appliances, and Prisma Access are not impacted by this vulnerability.",
      "epss_percentile": 0.9994,
      "epss_score": 0.94297,
      "exploitable": true,
      "exploited_in_the_wild": true,
      "modified_date": "2025-11-21T00:00:00",
      "published_date": "2024-04-12T00:00:00",
      "references": [],
      "tags": [
        "Remote Execution",
        "CISA KEV",
        "Exploited in the Wild",
        "Rapid7 Critical"
      ],
      "threat_actor_count": 3,
      "title": "CVE-2024-3400: Improper Neutralization of Special Elements used in a Command"
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
  
**cve**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Active Risk Score|integer|None|False|Rapid7 Active Risk score of the vulnerability, from 0 to 1000|None|
|Campaign Count|integer|None|False|Number of campaigns associated with the CVE|None|
|CISA KEV|boolean|None|False|Whether the CVE is in the CISA Known Exploited Vulnerabilities catalog|None|
|CVE ID|string|None|False|The CVE identifier|None|
|CVSS v3 Base Score|number|None|False|CVSS v3 base score of the vulnerability|None|
|CVSS v3 Severity|string|None|False|CVSS v3 severity of the vulnerability|None|
|CVSS v3 Vector|string|None|False|CVSS v3 vector string|None|
|CVSS v4 Base Score|number|None|False|CVSS v4 base score of the vulnerability|None|
|CVSS v4 Severity|string|None|False|CVSS v4 severity of the vulnerability|None|
|CVSS v4 Vector|string|None|False|CVSS v4 vector string|None|
|Description|string|None|False|Description of the vulnerability|None|
|EPSS Percentile|number|None|False|Percentile of the EPSS score among all scored CVEs, from 0 to 1|None|
|EPSS Score|number|None|False|Exploit Prediction Scoring System (EPSS) probability, from 0 to 1, that the vulnerability will be exploited|None|
|Exploitable|boolean|None|False|Whether the CVE is exploitable|None|
|Exploited in the Wild|boolean|None|False|Whether the CVE has been exploited in the wild|None|
|Modified Date|string|None|False|Date the CVE was last modified|None|
|Published Date|string|None|False|Date the CVE was published|None|
|References|[]string|None|False|List of reference URLs|None|
|Tags|[]string|None|False|Tags describing the vulnerability|None|
|Threat Actor Count|integer|None|False|Number of threat actors associated with the CVE|None|
|Title|string|None|False|Title of the CVE. For CVEs without a description, it can hold the full CVE description|None|
  
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
* If the connection test fails with `Product license not found`, the API key is valid but its organization has neither an InsightIDR nor an Intelligence Hub license
* The Search input of the Search CVEs action matches part of the CVE ID, such as `CVE-2024` or `3400`, not keywords in the CVE title or description
* Intelligence Hub does not provide Metasploit modules or vulnerability solutions

# Version History

* 1.0.0 - Initial plugin

# Links

* [Rapid7 Insight Platform](https://insight.rapid7.com)

## References

* [Rapid7 Intelligence Hub](https://docs.rapid7.com/intelligence-hub/)