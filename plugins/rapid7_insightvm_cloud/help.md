# Description

InsightVM is a powerful vulnerability management tool which finds, prioritizes, and remediates vulnerabilities. This plugin uses the InsightVM Cloud Integrations API to view assets and start scans

# Key Features

* Perform scan management functionality including starting and checking the status of scans
* Perform asset searches leveraging flexible asset and vulnerability filters
* Retrieve individual asset information

# Requirements

* Requires an InsightVM API Key
* InsightVM Scan Engine(s) paired to the Insight Platform

# Supported Product Versions

* InsightVM Cloud Integration API v4
* 2024-06-19

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_secret_key|None|True|API key from account|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|region|string|None|True|the region in which the plugin will work|["us", "us2", "us3", "eu", "ca", "au", "ap"]|us|None|None|

Example input:

```
{
  "credentials": "9de5069c5afe602b2ea0a04b66beb2c0",
  "region": "us"
}
```

## Technical Details

### Actions


#### Asset Search

This action is used to search for assets using filtered asset search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_criteria|string|None|False|Filters to apply to the asset search such as IPv4 or IPv6 addresses and hostnames|None|asset.ipv4 = 2001:db8:1:1:1:1:1:1 || asset.name STARTS WITH 'example'|None|None|
|comparison_time|date|None|False|The date and time to compare the asset current state against to detect changes|None|2021-04-15T17:56:47Z|None|None|
|criteria_operator|string|None|False|The logical query operator used to combine asset and/or vulnerability criteria. Only applicable when both asset and vulnerability criteria are entered|["", "AND", "OR"]|AND|None|None|
|current_time|date|None|False|The current date and time to compare against the asset state to detect changes|None|2021-04-15T17:56:47Z|None|None|
|size|integer|200|False|The number of assets to retrieve. If blank then will default to 200 assets returned|None|100|None|None|
|sort_criteria|object|None|False|JSON object for sorting by criteria. Multiple criteria can be specified with an order of 'asc' (ascending) or 'desc' (descending)|None|{"risk-score": "asc", "criticality-tag": "desc"}|None|None|
|vuln_criteria|string|None|False|Vulnerability criteria to filter by|None|vulnerability.categories IN ['example']|None|None|
  
Example input:

```
{
  "asset_criteria": "asset.ipv4 = 2001:db8:1:1:1:1:1:1 || asset.name STARTS WITH 'example'",
  "comparison_time": "2021-04-15T17:56:47Z",
  "criteria_operator": "AND",
  "current_time": "2021-04-15T17:56:47Z",
  "size": 200,
  "sort_criteria": {
    "criticality-tag": "desc",
    "risk-score": "asc"
  },
  "vuln_criteria": "vulnerability.categories IN ['example']"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assets|[]asset|True|List of asset details returned by the search|[{"assessed_for_policies":false,"assessed_for_vulnerabilities":true,"credential_assessments":[],"critical_vulnerabilities":12,"exploits":5,"id":"cdc978de-4178-a1d9-d5a94a114b87-example","ip":"2001:db8:1:1:1:1:1:1","last_assessed_for_vulnerabilities":"2020-06-25T15:19:51.543Z","last_scan_end":"2020-10-26T22:35:53.590Z","last_scan_start":"2020-10-26T22:35:53.564Z","mac":"00:50:56:94:52:04","malware_kits":0,"moderate_vulnerabilities":4,"new":[],"os_architecture":"","os_description":"Linux 2.6.32","os_family":"Linux","os_name":"Linux","os_system_name":"Linux","os_type":"General","os_vendor":"Linux","os_version":"2.6.32","remediated":[],"risk_score":9304.376953125,"severe_vulnerabilities":21,"tags":[{"name":"integrations discovery","type":"SITE"}],"total_vulnerabilities":37,"unique_identifiers":[]},{"assessed_for_policies":false,"assessed_for_vulnerabilities":true,"credential_assessments":[],"critical_vulnerabilities":12,"exploits":5,"id":"cdc978de-4178-a1d9-d5a94a114b87-example","ip":"2001:db8:1:1:1:1:1:1","last_assessed_for_vulnerabilities":"2020-06-25T15:19:51.543Z","last_scan_end":"2020-10-26T22:35:53.590Z","last_scan_start":"2020-10-26T22:35:53.564Z","mac":"00:50:56:94:52:04","malware_kits":0,"moderate_vulnerabilities":4,"new":[],"os_architecture":"","os_description":"Linux 2.6.32","os_family":"Linux","os_name":"Linux","os_system_name":"Linux","os_type":"General","os_vendor":"Linux","os_version":"2.6.32","remediated":[],"risk_score":9304.376953125,"severe_vulnerabilities":21,"tags":[{"name":"integrations discovery","type":"SITE"}],"total_vulnerabilities":37,"unique_identifiers":[]}]|
  
Example output:

```
{
  "assets": [
    {
      "assessed_for_policies": false,
      "assessed_for_vulnerabilities": true,
      "credential_assessments": [],
      "critical_vulnerabilities": 12,
      "exploits": 5,
      "id": "cdc978de-4178-a1d9-d5a94a114b87-example",
      "ip": "2001:db8:1:1:1:1:1:1",
      "last_assessed_for_vulnerabilities": "2020-06-25T15:19:51.543Z",
      "last_scan_end": "2020-10-26T22:35:53.590Z",
      "last_scan_start": "2020-10-26T22:35:53.564Z",
      "mac": "00:50:56:94:52:04",
      "malware_kits": 0,
      "moderate_vulnerabilities": 4,
      "new": [],
      "os_architecture": "",
      "os_description": "Linux 2.6.32",
      "os_family": "Linux",
      "os_name": "Linux",
      "os_system_name": "Linux",
      "os_type": "General",
      "os_vendor": "Linux",
      "os_version": "2.6.32",
      "remediated": [],
      "risk_score": 9304.376953125,
      "severe_vulnerabilities": 21,
      "tags": [
        {
          "name": "integrations discovery",
          "type": "SITE"
        }
      ],
      "total_vulnerabilities": 37,
      "unique_identifiers": []
    },
    {
      "assessed_for_policies": false,
      "assessed_for_vulnerabilities": true,
      "credential_assessments": [],
      "critical_vulnerabilities": 12,
      "exploits": 5,
      "id": "cdc978de-4178-a1d9-d5a94a114b87-example",
      "ip": "2001:db8:1:1:1:1:1:1",
      "last_assessed_for_vulnerabilities": "2020-06-25T15:19:51.543Z",
      "last_scan_end": "2020-10-26T22:35:53.590Z",
      "last_scan_start": "2020-10-26T22:35:53.564Z",
      "mac": "00:50:56:94:52:04",
      "malware_kits": 0,
      "moderate_vulnerabilities": 4,
      "new": [],
      "os_architecture": "",
      "os_description": "Linux 2.6.32",
      "os_family": "Linux",
      "os_name": "Linux",
      "os_system_name": "Linux",
      "os_type": "General",
      "os_vendor": "Linux",
      "os_version": "2.6.32",
      "remediated": [],
      "risk_score": 9304.376953125,
      "severe_vulnerabilities": 21,
      "tags": [
        {
          "name": "integrations discovery",
          "type": "SITE"
        }
      ],
      "total_vulnerabilities": 37,
      "unique_identifiers": []
    }
  ]
}
```

#### Get Asset

This action is used to get an asset by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|Get an asset by ID|None|abc978-5678-abc-a5a94a1234b8-asset|None|None|
|include_vulns|boolean|False|False|Whether or not the list of vulnerabilities should be returned|None|True|None|None|
  
Example input:

```
{
  "id": "abc978-5678-abc-a5a94a1234b8-asset",
  "include_vulns": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|asset|asset|True|Asset details|{"assessed_for_policies":false,"assessed_for_vulnerabilities":true,"credential_assessments":[{"port":22,"protocol":"TCP","status":"NO_CREDS_SUPPLIED"}],"critical_vulnerabilities":1,"exploits":2,"host_name":"example.rapid7.com","id":"cdc978de-4178-a1d9-d5a94a114b87-example","ip":"2001:db8:1:1:1:1:1:1","last_assessed_for_vulnerabilities":"2021-04-26T08:04:28.536Z","last_scan_end":"2021-04-26T08:04:28.536Z","last_scan_start":"2021-04-26T08:00:56.006Z","mac":"00:50:56:94:42:6B","malware_kits":0,"moderate_vulnerabilities":7,"new":[],"remediated":[],"risk_score":9006.3388671875,"severe_vulnerabilities":19,"tags":[{"name":"sn_pt_LDAP Admins","type":"OWNER"},{"name":"sn_CAB Approval","type":"OWNER"},{"name":"integrations","type":"CUSTOM"},{"name":"ck_test_site_2","type":"SITE"},{"name":"integrations","type":"SITE"},{"name":"ck_test_site_3","type":"SITE"},{"name":"integrations discovery","type":"SITE"},{"name":"ck_test_site_1","type":"SITE"}],"total_vulnerabilities":27,"unique_identifiers":[]}|
|vulnerabilities|[]asset_vulnerability|False|Vulnerabilities associated with the asset|[]|
  
Example output:

```
{
  "asset": {
    "assessed_for_policies": false,
    "assessed_for_vulnerabilities": true,
    "credential_assessments": [
      {
        "port": 22,
        "protocol": "TCP",
        "status": "NO_CREDS_SUPPLIED"
      }
    ],
    "critical_vulnerabilities": 1,
    "exploits": 2,
    "host_name": "example.rapid7.com",
    "id": "cdc978de-4178-a1d9-d5a94a114b87-example",
    "ip": "2001:db8:1:1:1:1:1:1",
    "last_assessed_for_vulnerabilities": "2021-04-26T08:04:28.536Z",
    "last_scan_end": "2021-04-26T08:04:28.536Z",
    "last_scan_start": "2021-04-26T08:00:56.006Z",
    "mac": "00:50:56:94:42:6B",
    "malware_kits": 0,
    "moderate_vulnerabilities": 7,
    "new": [],
    "remediated": [],
    "risk_score": 9006.3388671875,
    "severe_vulnerabilities": 19,
    "tags": [
      {
        "name": "sn_pt_LDAP Admins",
        "type": "OWNER"
      },
      {
        "name": "sn_CAB Approval",
        "type": "OWNER"
      },
      {
        "name": "integrations",
        "type": "CUSTOM"
      },
      {
        "name": "ck_test_site_2",
        "type": "SITE"
      },
      {
        "name": "integrations",
        "type": "SITE"
      },
      {
        "name": "ck_test_site_3",
        "type": "SITE"
      },
      {
        "name": "integrations discovery",
        "type": "SITE"
      },
      {
        "name": "ck_test_site_1",
        "type": "SITE"
      }
    ],
    "total_vulnerabilities": 27,
    "unique_identifiers": []
  },
  "vulnerabilities": []
}
```

#### Get Scan

This action is used to get the status of a scan

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|scan_id|string|None|True|ID of the scan to obtain|None|abb37782-df95-4cf6-b4c2-8d466ca57349|None|None|
  
Example input:

```
{
  "scan_id": "abb37782-df95-4cf6-b4c2-8d466ca57349"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|asset_ids|[]string|False|List of IDs of the scanned assets|["abc978-5678-abc-a5a94a1234b8-asset"]|
|finished|date|False|When the scan was finished|2021-04-15T18:00:33Z|
|name|string|False|User-driven scan name for the scan|testing scan action|
|scan_id|string|False|ID of the scan|a9870dce1234180e202af83b66cd0c4b|
|started|date|False|When the scan was started|2021-04-15T17:56:47Z|
|status|string|False|Current status of the retrieved scan|Stopped|
  
Example output:

```
{
  "asset_ids": [
    "abc978-5678-abc-a5a94a1234b8-asset"
  ],
  "finished": "2021-04-15T18:00:33Z",
  "name": "testing scan action",
  "scan_id": "a9870dce1234180e202af83b66cd0c4b",
  "started": "2021-04-15T17:56:47Z",
  "status": "Stopped"
}
```

#### Start Scan

This action is used to start an InsightVM scan of previously scanned devices

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_ids|[]string|None|False|IDs of the assets to scan|None|["abc978-5678-abc-a5a94a1234b8-asset"]|None|None|
|hostnames|[]string|None|False|List of hostnames to scan|None|["rapid7.com"]|None|None|
|ips|[]string|None|False|List of IPv4 or IPv6 addresses to scan|None|["2001:db8:1:1:1:1:1:1"]|None|None|
|name|string|None|True|The name of the scan|None|test cloud scan|None|None|
  
Example input:

```
{
  "asset_ids": [
    "abc978-5678-abc-a5a94a1234b8-asset"
  ],
  "hostnames": [
    "rapid7.com"
  ],
  "ips": [
    "2001:db8:1:1:1:1:1:1"
  ],
  "name": "test cloud scan"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|asset_ids|[]string|False|List of identifiers of the assets scanned|["5058b0b4-701a-414e-9630-430d2cddbf4d"]|
|data|object|False|Information received about the scan|{"scans":[{"engine_id":"5058b0b4-701a-414e-9630-430d2cddbf4d","id":"5058b0b4-701a-414e-9630-430d2cddbf4d","name":"TestScan","asset_ids":["5058b0b4-701a-414e-9630-430d2cddbf4d"]}],"unscanned_assets":[{"id":"5058b0b4-701a-414e-9630-430d2cddbf4d","reason":"Asset has never been scanned with an InsightVM Platform registered engine."}]}|
|ids|[]string|False|List of identifiers of the scans started|["5058b0b4-701a-414e-9630-430d2cddbf4d"]|
  
Example output:

```
{
  "asset_ids": [
    "5058b0b4-701a-414e-9630-430d2cddbf4d"
  ],
  "data": {
    "scans": [
      {
        "asset_ids": [
          "5058b0b4-701a-414e-9630-430d2cddbf4d"
        ],
        "engine_id": "5058b0b4-701a-414e-9630-430d2cddbf4d",
        "id": "5058b0b4-701a-414e-9630-430d2cddbf4d",
        "name": "TestScan"
      }
    ],
    "unscanned_assets": [
      {
        "id": "5058b0b4-701a-414e-9630-430d2cddbf4d",
        "reason": "Asset has never been scanned with an InsightVM Platform registered engine."
      }
    ]
  },
  "ids": [
    "5058b0b4-701a-414e-9630-430d2cddbf4d"
  ]
}
```

#### Stop Scan

This action is used to stop a scan in progress

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|Scan ID|None|abb37782-df95-4cf6-b4c2-8d466ca5734|None|None|
  
Example input:

```
{
  "id": "abb37782-df95-4cf6-b4c2-8d466ca5734"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|string|False|Reason why the action failed|The scan could not be stopped|
|status_code|integer|False|Code returned by API call|400|
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "message": "The scan could not be stopped",
  "status_code": 400,
  "success": true
}
```

#### Vulnerability Search

This action is used to search for vulnerabilities using filtered vulnerability search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|size|integer|200|False|The number of vulnerabilities to retrieve. If blank then will default to 200 vulnerabilities returned, the maximum limit is 500 vulnerabilities|None|100|None|None|
|sort_criteria|object|None|False|JSON object for sorting by criteria. Multiple criteria can be specified with an order of 'asc' (ascending) or 'desc' (descending)|None|{"risk-score": "asc", "criticality-tag": "desc"}|None|None|
|vuln_criteria|string|None|False|Vulnerability criteria to filter by|None|vulnerability.categories IN ['example']|None|None|
  
Example input:

```
{
  "size": 200,
  "sort_criteria": {
    "criticality-tag": "desc",
    "risk-score": "asc"
  },
  "vuln_criteria": "vulnerability.categories IN ['example']"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vulnerabilities|[]vulnerability|True|Vulnerabilities associated with the asset|[{"added":"2018-05-16T00:00:00Z","categories":"7-Zip","cves":"CVE-1234-5678","cvss_v2_access_complexity":"low","cvss_v2_access_vector":"network","cvss_v2_authentication":"none","cvss_v2_availability_impact":"complete","cvss_v2_confidentiality_impact":"complete","cvss_v2_exploit_score":9.996799945831299,"cvss_v2_impact_score":10.000845454680942,"cvss_v2_integrity_impact":"complete","cvss_v2_score":10,"cvss_v2_vector":"(AV:N/AC:L/Au:N/C:C/I:C/A:C)","cvss_v3_attack_complexity":null,"cvss_v3_attack_vector":null,"cvss_v3_availability_impact":null,"cvss_v3_confidentiality_impact":null,"cvss_v3_exploit_score":0,"cvss_v3_impact_score":null,"cvss_v3_integrity_impact":null,"cvss_v3_privileges_required":null,"cvss_v3_scope":null,"cvss_v3_score":0,"cvss_v3_user_interaction":null,"cvss_v3_vector":null,"denial_of_service":false,"description":"Unspecified vulnerability in 7-zip before 4.5.7 has unknown impact and remote attack vectors, as demonstrated by the PROTOS GENOME test suite for Archive Formats (c10).","exploits":[],"id":"7-zip-cve-1234-5678","links":[{"href":"http://www.example.com","id":"http://www.example.com","source":"url"}],"malware_kits":[],"modified":"2018-06-08T00:00:00Z","pci_cvss_score":10,"pci_fail":true,"pci_severity_score":5,"pci_special_notes":"","pci_status":"fail","published":"2009-03-29T00:00:00Z","references":"http://www.example.com","risk_score":898.76,"severity":"critical","severity_score":10,"title":"7-Zip: CVE-1234-5678: Unspecified vulnerability in 7-zip before 4.5.7"},{"added":"2018-05-16T00:00:00Z","categories":"7-Zip,Remote Execution","cves":"CVE-1234-5678","cvss_v2_access_complexity":"medium","cvss_v2_access_vector":"network","cvss_v2_authentication":"none","cvss_v2_availability_impact":"complete","cvss_v2_confidentiality_impact":"complete","cvss_v2_exploit_score":8.588799953460693,"cvss_v2_impact_score":10.000845454680942,"cvss_v2_integrity_impact":"complete","cvss_v2_score":9.3,"cvss_v2_vector":"(AV:N/AC:M/Au:N/C:C/I:C/A:C)","cvss_v3_attack_complexity":"low","cvss_v3_attack_vector":"local","cvss_v3_availability_impact":"high","cvss_v3_confidentiality_impact":"high","cvss_v3_exploit_score":1.8345765900000002,"cvss_v3_impact_score":5.873118720000001,"cvss_v3_integrity_impact":"high","cvss_v3_privileges_required":"none","cvss_v3_scope":"unchanged","cvss_v3_score":7.8,"cvss_v3_user_interaction":"required","cvss_v3_vector":"CVSS:3.0/AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H","denial_of_service":false,"description":"Heap-based buffer overflow in the NArchive::NHfs::CHandler::ExtractZlibFile method in 7zip before 16.00 and p7zip allows remote attackers to execute arbitrary code via a crafted HFS+ image.","exploits":[],"id":"7-zip-cve-1234-5678","links":[{"href":"http://www.example.com","id":"http://www.example.com","source":"url"}],"malware_kits":[],"modified":"2018-06-08T00:00:00Z","pci_cvss_score":9.3,"pci_fail":true,"pci_severity_score":5,"pci_special_notes":"","pci_status":"fail","published":"2016-12-13T00:00:00Z","references":"http://www.example.com","risk_score":718.8,"severity":"critical","severity_score":9,"title":"7-Zip: CVE-1234-5678: Heap-based buffer overflow vulnerability"}]|
  
Example output:

```
{
  "vulnerabilities": [
    {
      "added": "2018-05-16T00:00:00Z",
      "categories": "7-Zip",
      "cves": "CVE-1234-5678",
      "cvss_v2_access_complexity": "low",
      "cvss_v2_access_vector": "network",
      "cvss_v2_authentication": "none",
      "cvss_v2_availability_impact": "complete",
      "cvss_v2_confidentiality_impact": "complete",
      "cvss_v2_exploit_score": 9.996799945831299,
      "cvss_v2_impact_score": 10.000845454680942,
      "cvss_v2_integrity_impact": "complete",
      "cvss_v2_score": 10,
      "cvss_v2_vector": "(AV:N/AC:L/Au:N/C:C/I:C/A:C)",
      "cvss_v3_attack_complexity": null,
      "cvss_v3_attack_vector": null,
      "cvss_v3_availability_impact": null,
      "cvss_v3_confidentiality_impact": null,
      "cvss_v3_exploit_score": 0,
      "cvss_v3_impact_score": null,
      "cvss_v3_integrity_impact": null,
      "cvss_v3_privileges_required": null,
      "cvss_v3_scope": null,
      "cvss_v3_score": 0,
      "cvss_v3_user_interaction": null,
      "cvss_v3_vector": null,
      "denial_of_service": false,
      "description": "Unspecified vulnerability in 7-zip before 4.5.7 has unknown impact and remote attack vectors, as demonstrated by the PROTOS GENOME test suite for Archive Formats (c10).",
      "exploits": [],
      "id": "7-zip-cve-1234-5678",
      "links": [
        {
          "href": "http://www.example.com",
          "id": "http://www.example.com",
          "source": "url"
        }
      ],
      "malware_kits": [],
      "modified": "2018-06-08T00:00:00Z",
      "pci_cvss_score": 10,
      "pci_fail": true,
      "pci_severity_score": 5,
      "pci_special_notes": "",
      "pci_status": "fail",
      "published": "2009-03-29T00:00:00Z",
      "references": "http://www.example.com",
      "risk_score": 898.76,
      "severity": "critical",
      "severity_score": 10,
      "title": "7-Zip: CVE-1234-5678: Unspecified vulnerability in 7-zip before 4.5.7"
    },
    {
      "added": "2018-05-16T00:00:00Z",
      "categories": "7-Zip,Remote Execution",
      "cves": "CVE-1234-5678",
      "cvss_v2_access_complexity": "medium",
      "cvss_v2_access_vector": "network",
      "cvss_v2_authentication": "none",
      "cvss_v2_availability_impact": "complete",
      "cvss_v2_confidentiality_impact": "complete",
      "cvss_v2_exploit_score": 8.588799953460693,
      "cvss_v2_impact_score": 10.000845454680942,
      "cvss_v2_integrity_impact": "complete",
      "cvss_v2_score": 9.3,
      "cvss_v2_vector": "(AV:N/AC:M/Au:N/C:C/I:C/A:C)",
      "cvss_v3_attack_complexity": "low",
      "cvss_v3_attack_vector": "local",
      "cvss_v3_availability_impact": "high",
      "cvss_v3_confidentiality_impact": "high",
      "cvss_v3_exploit_score": 1.8345765900000002,
      "cvss_v3_impact_score": 5.873118720000001,
      "cvss_v3_integrity_impact": "high",
      "cvss_v3_privileges_required": "none",
      "cvss_v3_scope": "unchanged",
      "cvss_v3_score": 7.8,
      "cvss_v3_user_interaction": "required",
      "cvss_v3_vector": "CVSS:3.0/AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H",
      "denial_of_service": false,
      "description": "Heap-based buffer overflow in the NArchive::NHfs::CHandler::ExtractZlibFile method in 7zip before 16.00 and p7zip allows remote attackers to execute arbitrary code via a crafted HFS+ image.",
      "exploits": [],
      "id": "7-zip-cve-1234-5678",
      "links": [
        {
          "href": "http://www.example.com",
          "id": "http://www.example.com",
          "source": "url"
        }
      ],
      "malware_kits": [],
      "modified": "2018-06-08T00:00:00Z",
      "pci_cvss_score": 9.3,
      "pci_fail": true,
      "pci_severity_score": 5,
      "pci_special_notes": "",
      "pci_status": "fail",
      "published": "2016-12-13T00:00:00Z",
      "references": "http://www.example.com",
      "risk_score": 718.8,
      "severity": "critical",
      "severity_score": 9,
      "title": "7-Zip: CVE-1234-5678: Heap-based buffer overflow vulnerability"
    }
  ]
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**link**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|URL|string|None|False|A hypertext reference, which is either a URI (see RFC 3986) or URI template (see RFC 6570)|None|
|Rel|string|None|False|Link relation type following RFC 5988|None|
  
**address**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IP|string|None|False|IPv4 or IPv6 address|None|
|MAC|string|None|False|Media Access Control (MAC) address, e.g. AF:12:BC:5A:F7:48|None|
  
**configuration**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Name of the configuration value|None|
|Value|string|None|False|Configuration value|None|
  
**database**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|Description of the database instance|None|
|ID|integer|None|False|Identifier of the database|None|
|Name|string|None|False|Name of the database instance|None|
  
**file**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attributes|[]configuration|None|False|Attributes detected on the file|None|
|Contents|bytes|None|False|Contents of the file|None|
|Name|string|None|False|Name of the file|None|
|Size|integer|None|False|Size of the regular file (in bytes). If the file is a directory, no value is returned|None|
|Type|string|None|False|Type of the file, e.g. file or directory|None|
  
**history**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Date|string|None|False|Date the asset information was collected or changed|None|
|Description|string|None|False|Additional information describing the change|None|
|Scan ID|integer|None|False|If a scan-oriented change, the identifier of the corresponding scan the asset was scanned in|None|
|Type|string|None|False|Type, for additional information see the help section of this plugin|None|
|User|string|None|False|User|None|
|Version|integer|None|False|Version|None|
|Vulnerability Exception ID|integer|None|False|Vulnerability exception ID|None|
  
**host_name**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Name|None|
|Source|string|None|False|Source|None|
  
**id**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|ID|None|
|Source|string|None|False|Source|None|
  
**cpe**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Edition|string|None|False|Edition-related terms applied by the vendor to the product|None|
|Language|string|None|False|Defines the language supported in the user interface of the product being described. The format of the language tag adheres to RFC 5646|None|
|Other|string|None|False|Captures any other general descriptive or identifying information which is vendor- or product-specific and which does not logically fit in any other attribute value|None|
|Part|string|None|False|A single letter code that designates the particular platform part that is being identified|None|
|Product|string|None|False|Most common and recognizable title or name of the product|None|
|Software Edition|string|None|False|Characterizes how the product is tailored to a particular market or class of end users|None|
|Target Hardware|string|None|False|Characterize the instruction set architecture on which the product operates|None|
|Target Software|string|None|False|Characterizes the software computing environment within which the product operates|None|
|Update|string|None|False|Vendor-specific alphanumeric strings characterizing the particular update, service pack, or point release of the product|None|
|Version 2.2|string|None|False|The full CPE string in the CPE 2.2 format|None|
|Version 2.3|string|None|False|The full CPE string in the CPE 2.3 format|None|
|Vendor|string|None|False|The person or organization that manufactured or created the product|None|
|Version|string|None|False|Vendor-specific alphanumeric strings characterizing the particular release version of the product|None|
  
**os_fingerprint**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Architecture|string|None|False|The architecture of the operating system|None|
|Configuration|[]configuration|None|False|Configuration key-values pairs enumerated on the operating system|None|
|CPE|cpe|None|False|Common Platform Enumeration|None|
|Description|string|None|False|The description of the operating system (containing vendor, family, product, version and architecture in a single string)|None|
|Family|string|None|False|Family of the operating system|None|
|ID|integer|None|False|Identifier of the operating system|None|
|Product|string|None|False|Name of the operating system|None|
|System Name|string|None|False|A combination of vendor and family (with redundancies removed), suitable for grouping|None|
|Type|string|None|False|Type of operating system|None|
|Vendor|string|None|False|Vendor of the operating system|None|
|Version|string|None|False|Version of the operating system|None|
  
**user_group**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|Identifier of the user group|None|
|Name|string|None|False|Name of the user group|None|
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Full Name|string|None|False|Full name of the user account|None|
|ID|integer|None|False|Identifier of the user account|None|
|Name|string|None|False|Name of the user account|None|
  
**page**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Link Type|string|None|False|Type of link used to traverse or detect the page|None|
|Path|string|None|False|Path to the page (URI)|None|
|Response|integer|None|False|HTTP response code observed with retrieving the page|None|
  
**web_application**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|Identifier of the web application|None|
|Pages|[]page|None|False|Pages|None|
|Root|string|None|False|Web root of the web application|None|
|Virtual Host|string|None|False|Virtual host of the web application|None|
  
**service**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Configurations|[]configuration|None|False|Configuration key-values pairs enumerated on the service|None|
|Databases|[]database|None|False|Databases enumerated on the service|None|
|Family|string|None|False|Family of the service|None|
|Links|[]link|None|False|Hypermedia links to corresponding or related resources|None|
|Name|string|None|False|Name of the service|None|
|Port|integer|None|False|Port of the service|None|
|Product|string|None|False|Product running the service|None|
|Protocol|string|None|False|Protocol of the service|None|
|User Groups|[]user_group|None|False|User groups|None|
|Users|[]user|None|False|Users|None|
|Vendor|string|None|False|Vendor of the service|None|
|Version|string|None|False|Version of the service|None|
|Web Applications|[]web_application|None|False|Web applications found on the service|None|
  
**asset_vulnerability**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|First Found|date|None|False|Date the vulnerability was first found in InsightVM|None|
|Vulnerability Key|string|None|False|The key to identify a specific instance if the type is Instance|None|
|Last Found|date|None|False|Date the vulnerability was last found in InsightVM|None|
|Proof|string|None|False|Proof of the vulnerability, i.e. <p><p>OpenBSD OpenSSH 4.3 on Linux</p></p>|None|
|Fix|string|None|False|The steps that are part of the fix this solution prescribes|None|
|Solution ID|string|None|False|The identifier of the solution|None|
|Solution Summary|string|None|False|Remediation summary|None|
|Solution Type|string|None|False|Remediation type|None|
|Status|string|None|False|Status, i.e. vulnerable|None|
|Vulnerability ID|string|None|False|The identifier of the vulnerability|None|
  
**software**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Configurations|[]configuration|None|False|Configurations|None|
|CPE|cpe|None|False|CPE|None|
|Description|string|None|False|Description of the software|None|
|Family|string|None|False|Family of the software|None|
|ID|integer|None|False|ID|None|
|Product|string|None|False|Product of the software|None|
|Type|string|None|False|Type of the software|None|
|Vendor|string|None|False|Vendor of the software|None|
|Version|string|None|False|Version of the software|None|
  
**vulnerability_description**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HTML|string|None|None|Vulnerability description HTML|None|
|Text|string|None|None|Vulnerability description raw text|None|
  
**pci**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Adjusted CVSS score|integer|None|None|PCI adjusted CVSS score|None|
|Adjusted severity score|integer|None|None|PCI adjusted severity score|None|
|Fail|boolean|None|None|Whether this vulnerability results in a PCI assessment failure|None|
|Special Notes|string|None|None|PCI special notes|None|
|Status|string|None|None|PCI status|None|
  
**cvss_v2**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Access Complexity|string|None|None|CVSSv2 access complexity metric|None|
|Access Vector|string|None|None|CVSSv2 access vector metric|None|
|Authentication|string|None|None|CVSSv2 authentication metric|None|
|Availability Impact|string|None|None|CVSSv2 availability impact metric|None|
|Confidentiality Impact|string|None|None|CVSSv2 confidentiality impact metric|None|
|Exploit Score|float|None|None|CVSSv2 combined exploit metric score (Access Complexity/Access Vector/Authentication)|None|
|Impact Score|float|None|None|CVSSv2 combined impact metric score (Confidentiality/Integrity/Availability)|None|
|Integrity Impact|string|None|None|CVSSv2 integrity impact metric|None|
|Score|float|None|None|CVSSv2 score|None|
|Vector|string|None|None|CVSSv2 combined vector string|None|
  
**cvss_v3**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attack Complexity|string|None|None|CVSSv3 attack complexity metric|None|
|Attack Vector|string|None|None|CVSSv3 attack vector metric|None|
|Availability Impact|string|None|None|CVSSv3 availability impact metric|None|
|Confidentiality Impact|string|None|None|CVSSv3 confidentiality impact metric|None|
|Exploit Score|float|None|None|CVSSv3 combined exploit metric score (Attack Complexity/Attack Vector/Privilege Required/Scope/User Interaction)|None|
|Impact Score|float|None|None|CVSSv3 combined impact metric score (Confidentiality/Integrity/Availability)|None|
|Integrity Impact|string|None|None|CVSSv3 integrity impact metric|None|
|Privilege Required|string|None|None|CVSSv3 privilege required metric|None|
|Scope|string|None|None|CVSSv3 scope metric|None|
|Score|float|None|None|CVSSv3 score|None|
|User Interaction|string|None|None|CVSSv3 user interaction metric|None|
|Vector|string|None|None|CVSSv3 combined vector string|None|
  
**cvss**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Links|[]link|None|None|List of hypermedia links to corresponding resources|None|
|V2|cvss_v2|None|None|CVSSv2 details|None|
|V3|cvss_v3|None|None|CVSSv3 details|None|
  
**creds**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Port|integer|None|False|The port that is used|None|
|Protocol|string|None|False|TCP or other|None|
|Status|string|None|False|Which creds apply|None|
  
**identifiers**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|The ID|None|
|Source|string|None|False|The source|None|
  
**asset_tag**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|The name|None|
|Type|string|None|False|The type|None|
  
**asset**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assessed for Policies|boolean|None|False|Whether the asset has been assessed for policies at least once|None|
|Assessed for Vulnerabilities|boolean|None|False|Whether the asset has been assessed for vulnerabilities at least once|None|
|Credential Assessments|[]creds|None|False|Assessments from the credentials|None|
|Critical Vulnerabilities|integer|None|False|Number of critical vulnerabilities|None|
|Exploits|integer|None|False|Number of exploits|None|
|Hostname|string|None|False|Primary host name (local or FQDN) of the asset|None|
|ID|string|None|False|Identifier of the asset|None|
|IP|string|None|False|Primary IPv4 or IPv6 address of the asset|None|
|Last Assessed For Vulnerabilities|string|None|False|Date of last scan|None|
|Last Scan End|string|None|False|When the last scan was ended|None|
|Last Scan Start|string|None|False|When the last scan was started|None|
|MAC|string|None|False|Media Access Control (MAC) address, e.g. AF:12:BC:5A:F7:48|None|
|Malware Kits|integer|None|False|Number of malware kits|None|
|Moderate Vulnerabilities|integer|None|False|Number of moderate vulnerabilities|None|
|New|[]object|None|False|If comparison time is supplied, the vulnerabilities that are new in the latest version at current time|None|
|OS Architecture|string|None|False|The architecture of the os|None|
|OS Description|string|None|False|Description of the os|None|
|OS Family|string|None|False|Family of the os|None|
|OS Name|string|None|False|Name of the os|None|
|OS System Name|string|None|False|Name of the system os|None|
|OS Type|string|None|False|Type of os|None|
|OS Vendor|string|None|False|Vendor of the os|None|
|OS Version|string|None|False|The version of the operating system|None|
|Remediated Vulnerabilities|[]object|None|False|Vulnerabilities that were remediated in the latest version at current time for the asset|None|
|Risk Score|float|None|False|Risk score (with criticality adjustments) of the asset|None|
|Severe Vulnerabilities|integer|None|False|The count of severe vulnerability findings|None|
|Source|string|None|False|Source of the asset|None|
|Tags|[]asset_tag|None|False|The tags applied to the asset|None|
|Total Vulnerabilities|integer|None|False|The total count of vulnerability findings|None|
|Type|string|None|False|The type of asset|None|
|Unique Identifiers|[]identifiers|None|False|Uniqure aspects of the asset|None|
  
**exploit**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|True|A verbose description of the exploit|None|
|ID|string|None|True|The identifier of the exploit|None|
|Name|string|None|True|The name of the exploit|None|
|Rank|string|None|True|The exploit rank|None|
|Skill level|string|None|True|The level of skill required to use the exploit|None|
|Source|string|None|True|Details about where the exploit is defined|None|
  
**vulnerability**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Added|date|None|False|Date the vulnerability was last added to an asset|None|
|Categories|string|None|True|Labels this vulnerability falls under|None|
|CVES|string|None|False|CVES ID|None|
|CVSSv2|cvss_v2|None|False|information regarding CVSSv2|None|
|CVSSv3|cvss_v3|None|False|information regarding CVSSv3|None|
|Denial of Service|boolean|None|False|Whether or not this vulnerability is a denial of service attack|None|
|Description|string|None|False|Description of the vulnerability|None|
|Exploits|[]exploit|None|False|List of exploits related to the vulnerability|None|
|ID|string|None|True|ID of the vulnerability|None|
|Links|[]link|None|False|List of links related to the vulnerability|None|
|Malware Kits|[]object|None|False|List of malware kits related to the vulnerability|None|
|Modified|date|None|False|Date the vulnerability was last modified|None|
|PCI|pci|None|False|information regarding PCI|None|
|Published|date|None|True|Date the vulnerability was added to InsightVM|None|
|References|string|None|False|Links to information related to the vulnerability|None|
|Risk Score|float|None|True|Risk score (with criticality adjustments) of the vulnerability|None|
|Severity|string|None|True|Severity of the vulnerability|None|
|Severity Score|integer|None|True|Severity score of the vulnerability|None|
|Title|string|None|False|Name of the vulnerability|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 8.1.1 - Updated SDK to the latest version (v6.2.3) | Address vulnerabilities
* 8.1.0 - Action `Asset Search`: Added optional asset and vulnerability criteria logical operator | Updated action to return more than 500 results
* 8.0.0 - Output for `Asset Search` and `Get Asset` to label fields `ID` and `Solution Type` as un-required
* 7.0.0 - `Asset Search` and `Get Asset` actions output field `remediated` updated to type array of object
* 6.0.0 - Asset Search: Modify type of output field `new` when `comparison_time` input is used.
* 5.0.0 - Vulnerability Search: fix malware_kits output and remove Asset Criteria input | Updated the documentation with links related to query builder and operators | Updated the SDK
* 4.0.0 - Vulnerability Search: fix schema validation problem for exploits field
* 3.3.0 - Asset Search: add filter fields: `current_time`, `comparison_time`
* 3.2.0 - Add vulnerability search action
* 3.1.0 - Add Cloud enablement to plugin | Updated exception information and error handling | Made status code output for Stop Scan and Get Scan actions more exact | Fix bug relating to empty inputs being passed in request body
* 3.0.0 - Changed output of Get Asset action to include vulnerabilities properly
* 2.2.0 - Added ability to include vulnerabilities on Get Asset action | API call update
* 2.1.0 - Added scanned asset_ids as an output of start_scan
* 2.0.0 - Fix issue where string data-type should be date in actions | Update docs
* 1.0.0 - Initial plugin

# Links

* [InsightVM Query Builder](https://docs.rapid7.com/insightvm/query-builder/)
* [InsightVM Query Operators](https://docs.rapid7.com/insightvm/query-operators-1/)

## References

* [InsightVM Cloud API](https://help.rapid7.com/insightvm/en-us/api/integrations.html)
* [Managing Platform API Keys](https://docs.rapid7.com/insight/managing-platform-api-keys)
* [Scan Engine Pairing](https://docs.rapid7.com/insightvm/scan-engine-management-on-the-insight-platform/#how-to-pair-your-scan-engines-to-the-insight-platform)