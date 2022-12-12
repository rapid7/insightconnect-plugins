# Description

InsightVM is a powerful vulnerability management tool which finds, prioritizes, and remediates vulnerabilities. This plugin uses the v4 cloud API to view assets, retrieve scan results and start scans. With an InsightVM scan engine paired to the platform, take advantage of triggering scans on assets in your environment along with performing robust asset searches to lookup and make actionable the asset and vulnerability data in your environment.

# Key Features

* Perform scan management functionality including starting and checking the status of scans
* Perform asset searches leveraging flexible asset and vulnerability filters
* Retrieve individual asset information

# Requirements

* Requires an InsightVM API Key
* InsightVM Scan Engine(s) paired to the Insight Platform

# Supported Product Versions

* InsightVM Cloud Integration API v4
* 2022-08-10

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_secret_key|None|True|API key from account|None|9de5069c5afe602b2ea0a04b66beb2c0|
|region|string|None|True|the region in which the plugin will work|['us', 'us2', 'us3', 'eu', 'ca', 'au', 'ap']|us|

Example input:

```
{
  "credentials": "9de5069c5afe602b2ea0a04b66beb2c0",
  "region": "us"
}
```

## Technical Details

### Actions

#### Vulnerability Search

This action is used to search for vulnerabilities using filtered vulnerability search.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|asset_criteria|string|None|False|Filters to apply to the asset search such as IPv4 or IPv6 addresses and hostnames|None|https://example.com = 2001:db8:1:1:1:1:1:1 || https://example.com STARTS WITH 'example'|
|size|number|200|False|The number of vulnerabilities to retrieve. If blank then will default to 200 vulnerabilities returned, the maximum limit is 500 vulnerabilities|None|100|
|sort_criteria|object|None|False|JSON object for sorting by criteria. Multiple criteria can be specified with an order of 'asc' (ascending) or 'desc' (descending)|None|{'risk-score': 'asc', 'criticality-tag': 'desc'}|
|vuln_criteria|string|None|False|Vulnerability criteria to filter by|None|https://example.com IN ['example']|

Example input:

```
{
  "asset_criteria": "asset.ipv4 = 2001:db8:1:1:1:1:1:1 || asset.name STARTS WITH 'example'",
  "size": 100,
  "sort_criteria": "{'risk-score': 'asc', 'criticality-tag': 'desc'}",
  "vuln_criteria": "vulnerability.categories IN ['example']"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|vulnerabilities|[]vulnerability|True|Vulnerabilities associated with the asset|

Example output:

```
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
            "cvss_v2_exploit_score": 9.9,
            "cvss_v2_impact_score": 10.0,
            "cvss_v2_integrity_impact": "complete",
            "cvss_v2_score": 10.0,
            "cvss_v2_vector": "(AV:N/AC:L/Au:N/C:C/I:C/A:C)",
            "cvss_v3_attack_complexity": null,
            "cvss_v3_attack_vector": null,
            "cvss_v3_availability_impact": null,
            "cvss_v3_confidentiality_impact": null,
            "cvss_v3_exploit_score": 0.0,
            "cvss_v3_impact_score": null,
            "cvss_v3_integrity_impact": null,
            "cvss_v3_privileges_required": null,
            "cvss_v3_scope": null,
            "cvss_v3_score": 0.0,
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
                },
                {
                    "href": "http://www.example.com",
                    "id": "12345",
                    "source": "bid"
                },
                {
                    "href": "http://example.com/CVE-1234-5467",
                    "id": "CVE-1234-5467",
                    "source": "cve"
                },
                {
                    "href": "http://www.example.com/thing.pdf",
                    "id": "http://www.example.com/thing.pdf",
                    "source": "url"
                }
            ],
            "malware_kits": [],
            "modified": "2018-06-08T00:00:00Z",
            "pci_cvss_score": 10.0,
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
            "cvss_v2_exploit_score": 8.5,
            "cvss_v2_impact_score": 10.0,
            "cvss_v2_integrity_impact": "complete",
            "cvss_v2_score": 9.3,
            "cvss_v2_vector": "(AV:N/AC:M/Au:N/C:C/I:C/A:C)",
            "cvss_v3_attack_complexity": "low",
            "cvss_v3_attack_vector": "local",
            "cvss_v3_availability_impact": "high",
            "cvss_v3_confidentiality_impact": "high",
            "cvss_v3_exploit_score": 1.8,
            "cvss_v3_impact_score": 5.8,
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
                },
                {
                    "href": "http://www.example.com/12345",
                    "id": "12345",
                    "source": "bid"
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
        },
     ]
```

#### Stop Scan

This action is used to stop a scan in progress.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Scan ID|None|abb37782-df95-4cf6-b4c2-8d466ca5734|

Example input:

```
{
  "id": "abb37782-df95-4cf6-b4c2-8d466ca5734"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|Reason why the action failed|
|status_code|integer|False|Code returned by API call|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "success": true
}
```

#### Start Scan

This action is used to start an InsightVM scan of previously scanned devices.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|asset_ids|[]string|None|False|IDs of the assets to scan|None|["abc978-5678-abc-a5a94a1234b8-asset"]|
|hostnames|[]string|None|False|List of hostnames to scan|None|["https://example.com"]|
|ips|[]string|None|False|List of IPv4 or IPv6 addresses to scan|None|["2001:db8:1:1:1:1:1:1"]|
|name|string|None|True|The name of the scan|None|test cloud scan|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|asset_ids|[]string|False|List of identifiers of the assets scanned|
|data|object|False|Information received about the scan|
|ids|[]string|False|List of identifiers of the scans started|

Example output:

```
{
  "scans": [
    {
      "engine_id": "c8970d2ee174180e202af83b66cd0c4b",
      "finished": null,
      "id": "436a59e4-b203-4743-89a9-5b76294f20f4",
      "name": "testing scan action",
      "asset_ids": [
        "cdc978de-4178-a1d9-d5a94a114b87-example..."
      ]
    }
  ],
  "unscanned_assets": []
}
```

#### Asset Search

This action is used to search for assets using filtered asset search.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|asset_criteria|string|None|False|Filters to apply to the asset search such as IPv4 or IPv6 addresses and hostnames|None|https://example.com = 2001:db8:1:1:1:1:1:1 || https://example.com STARTS WITH 'example'|
|size|number|200|False|The number of assets to retrieve. If blank then will default to 200 assets returned, the maximum limit is 500 assets|None|100|
|sort_criteria|object|None|False|JSON object for sorting by criteria. Multiple criteria can be specified with an order of 'asc' (ascending) or 'desc' (descending)|None|{'risk-score': 'asc', 'criticality-tag': 'desc'}|
|vuln_criteria|string|None|False|Vulnerability criteria to filter by|None|https://example.com IN ['example']|

Example input:

```
{
  "asset_criteria": "asset.ipv4 = 2001:db8:1:1:1:1:1:1 || asset.name STARTS WITH 'example'",
  "size": 100,
  "sort_criteria": "{'risk-score': 'asc', 'criticality-tag': 'desc'}",
  "vuln_criteria": "vulnerability.categories IN ['example']"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|assets|[]asset|True|List of asset details returned by the search|

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
          "id": "cdc978de-4178-a1d9-d5a94a114b87-example,
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

This action gets an asset by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Get an asset by ID|None|abc978-5678-abc-a5a94a1234b8-asset|
|include_vulns|boolean|False|False|Whether or not the list of vulnerabilities should be returned|None|True|

Example input:

```
{
  "id": "abc978-5678-abc-a5a94a1234b8-asset",
  "include_vulns": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|asset|asset|True|Asset details|
|vulnerabilities|[]vulnerability|False|Vulnerabilities associated with the asset|

Example output:

```
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
      }
    }
```

#### Get Scan

This action is used to get the status of a scan.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_id|string|None|True|ID of the scan to obtain|None|abb37782-df95-4cf6-b4c2-8d466ca57349|

Example input:

```
{
  "scan_id": "abb37782-df95-4cf6-b4c2-8d466ca57349"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|asset_ids|[]string|False|List of IDs of the scanned assets|
|finished|date|False|When the scan was finished|
|name|string|False|User-driven scan name for the scan|
|scan_id|string|False|ID of the scan|
|started|date|False|When the scan was started|
|status|string|False|Current status of the retrieved scan|

Example output:

```
    {
      "scans": [
        {
          "asset_ids": [
            "cdc978de-f683-4178-a1d9-d5a94a114b87-default-asset-13"
          ],
          "engine_id": "c8970d2ee174180e202af83b66cd0c4b",
          "finished": null,
          "id": "7fc3d8ec-24a7-4835-84f2-8877fe96a29b",
          "name": "testing scan action"
        }
      ],
      "unscanned_assets": []
    }
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### address

|Name|Type|Required|Description|
|----|----|--------|-----------|
|IP|string|False|IPv4 or IPv6 address|
|MAC|string|False|Media Access Control (MAC) address, e.g. AF:12:BC:5A:F7:48|

#### asset

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Addresses|[]address|False|All addresses discovered on the asset|
|Assessed for Policies|boolean|False|Whether the asset has been assessed for policies at least once|
|Assessed for Vulnerabilities|boolean|False|Whether the asset has been assessed for vulnerabilities at least once|
|Configurations|[]configuration|False|Configuration key-values pairs enumerated on the asset|
|Databases|[]database|False|Databases enumerated on the asset|
|Files|[]file|False|Files discovered with searching on the asset|
|History|[]history|False|History of changes to the asset over time|
|Hostname|string|False|Primary host name (local or FQDN) of the asset|
|Hostnames|[]hostName|False|All hostnames or aliases discovered on the asset|
|ID|integer|False|Identifier of the asset|
|IDs|[]id|False|Unique identifiers found on the asset, such as hardware or operating system identifiers|
|IP|string|False|Primary IPv4 or IPv6 address of the asset|
|Links|[]link|False|Hypermedia links to corresponding or related resources|
|MAC|string|False|Media Access Control (MAC) address, e.g. AF:12:BC:5A:F7:48|
|OS|string|False|Full description of the operating system of the asset|
|OS Fingerprint|osFingerprint|False|Details of the operating system of the asset|
|Raw Risk Score|float|False|Base risk score of the asset|
|Risk Score|float|False|Risk score (with criticality adjustments) of the asset|
|Services|[]service|False|Services discovered on the asset|
|Software|[]software|False|Software discovered on the asset|
|Type|string|False|Type of asset e.g. unknown, guest, hypervisor, physical, mobile|
|User Groups|[]userGroup|False|User group accounts enumerated on the asset|
|Users|[]user|False|User accounts enumerated on the asset|
|Vulnerabilities|vulnerabilities|False| Summary information for vulnerabilities on the asset|

#### asset_group

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Assets|integer|True|Site asset count|
|Description|string|False|Asset group description|
|ID|integer|True|Site ID|
|Links|[]link|True|Hypermedia links to corresponding or related resources|
|Name|string|True|Asset group name|
|Risk Score|float|True|Site risk score|
|Search Criteria|object|False|Asset group search criteria|
|Type|string|True|Asset group type|
|Vulnerabilities|vulnerabilities_count|True|Asset group vulnerability counts|

#### asset_vulnerability

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Vulnerability ID, ie. ssh-openssh-x11uselocalhost-x11-forwarding-session-hijack|
|Instances|integer|False|Identifier of the report instance|
|Links|[]link|False|Hypermedia links to corresponding or related resources|
|Results|[]asset_vulnerability_result|False|The vulnerability check results for the finding. Multiple instances may be present if one or more checks fired, or a check has multiple independent results|
|Risk Score|float|False|The risk score for the vulnerability|
|Since|string|False|The date when this vulnerability was first detected|
|Status|string|False|Status, ie. vulnerable|

#### asset_vulnerability_result

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Check ID|string|False|Check ID, ie. ssh-openssh-x11uselocalhost-x11-forwarding-session-hijack|
|Exceptions|[]integer|False|If the result is vulnerable with exceptions applied, the identifier(s) of the exceptions actively applied to the result|
|Key|string|False|An additional discriminating key used to uniquely identify between multiple instances of results on the same finding|
|Links|[]link|False|Hypermedia links to corresponding or related resources|
|Port|integer|False|Port of the service the result was discovered on e.g. 22|
|Proof|string|False|Proof of the vulnerability, ie. <p><p>OpenBSD OpenSSH 4.3 on Linux</p></p>|
|Protocol|string|False|Protocol of the service the result was discovered on, ie. TCP|
|Status|string|False|Status of the vulnerability check result, ie. vulnerable-version|

#### authentication_source

|Name|Type|Required|Description|
|----|----|--------|-----------|
|External|boolean|True|Whether the authentication source is external (true) or internal (false)|
|ID|integer|True|Authentication source identifier|
|Links|[]link|True|List of hypermedia links to corresponding or related resources|
|Name|string|True|Authentication source name|
|Type|string|True|Authentication source type|

#### configuration

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Name|string|False|Name of the configuration value|
|Value|string|False|Configuration value|

#### cpe

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Edition|string|False|Edition-related terms applied by the vendor to the product|
|Language|string|False|Defines the language supported in the user interface of the product being described. The format of the language tag adheres to RFC 5646|
|Other|string|False|Captures any other general descriptive or identifying information which is vendor- or product-specific and which does not logically fit in any other attribute value|
|Part|string|False|A single letter code that designates the particular platform part that is being identified|
|Product|string|False|Most common and recognizable title or name of the product|
|Software Edition|string|False|Characterizes how the product is tailored to a particular market or class of end users|
|Target Hardware|string|False|Characterize the instruction set architecture on which the product operates|
|Target Software|string|False|Characterizes the software computing environment within which the product operates|
|Update|string|False|Vendor-specific alphanumeric strings characterizing the particular update, service pack, or point release of the product|
|Version 2.2|string|False|The full CPE string in the CPE 2.2 format|
|Version 2.3|string|False|The full CPE string in the CPE 2.3 format|
|Vendor|string|False|The person or organization that manufactured or created the product|
|Version|string|False|Vendor-specific alphanumeric strings characterizing the particular release version of the product|

#### CVSS

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Links|[]link|False|List of hypermedia links to corresponding resources|
|V2|cvss_v2|False|CVSSv2 details|
|V3|cvss_v3|False|CVSSv3 details|

#### CVSS_v2

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access Complexity|string|False|CVSSv2 access complexity metric|
|Access Vector|string|False|CVSSv2 access vector metric|
|Authentication|string|False|CVSSv2 authentication metric|
|Availability Impact|string|False|CVSSv2 availability impact metric|
|Confidentiality Impact|string|False|CVSSv2 confidentiality impact metric|
|Exploit Score|float|False|CVSSv2 combined exploit metric score (Access Complexity/Access Vector/Authentication)|
|Impact Score|float|False|CVSSv2 combined impact metric score (Confidentiality/Integrity/Availability)|
|Integrity Impact|string|False|CVSSv2 integrity impact metric|
|Score|float|False|CVSSv2 score|
|Vector|string|False|CVSSv2 combined vector string|

#### CVSS_v3

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Attack Complexity|string|False|CVSSv3 attack complexity metric|
|Attack Vector|string|False|CVSSv3 attack vector metric|
|Availability Impact|string|False|CVSSv3 availability impact metric|
|Confidentiality Impact|string|False|CVSSv3 confidentiality impact metric|
|Exploit Score|float|False|CVSSv3 combined exploit metric score (Attack Complexity/Attack Vector/Privilege Required/Scope/User Interaction)|
|Impact Score|float|False|CVSSv3 combined impact metric score (Confidentiality/Integrity/Availability)|
|Integrity Impact|string|False|CVSSv3 integrity impact metric|
|Privilege Required|string|False|CVSSv3 privilege required metric|
|Scope|string|False|CVSSv3 scope metric|
|Score|float|False|CVSSv3 score|
|User Interaction|string|False|CVSSv3 user interaction metric|
|Vector|string|False|CVSSv3 combined vector string|

#### database

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Description|string|False|Description of the database instance|
|ID|integer|False|Identifier of the database|
|Name|string|False|Name of the database instance|

#### exception_review

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Review Comment|string|False|The comment from the reviewer detailing the review|
|Review Date|date|False|The date and time the review took place|
|Links|[]link|False|Hypermedia links to corresponding or related resources|
|Reviewer Name|string|False|The login name of the user that reviewed the vulnerability exception|
|Reviewer ID|integer|False|The identifier of the user that reviewed the vulnerability exception|

#### exception_scope

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Vulnerability Scope ID|integer|True|The identifer of the scope (asset, group, site) the vulnerability exception applies to|
|Exception Scope Key|string|False|Optional key to discriminate the instance when the scope type is Instance|
|Links|[]link|False|Hypermedia links to corresponding or related resources|
|Port|integer|False|If the scope type is Instance, the port the exception applies to|
|Exception Scope Type|string|True|The type of vulnerability exception - Global, Site, Asset, Asset Group, Instance|
|Vulnerability|string|True|The vulnerability the exception applies to|

#### exception_submit

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Submit Comment|string|False|The comment from the submit detailing the exception|
|Submit Date|date|False|The date and time the exception request took place|
|Links|[]link|False|Hypermedia links to corresponding or related resources|
|Submitter Name|string|False|The login name of the user that submitted the vulnerability exception|
|Submitter ID|integer|False|The identifier of the user that submitted the vulnerability exception|

#### file

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Attributes|[]configuration|False|Attributes detected on the file|
|Contents|bytes|False|Contents of the file|
|Name|string|False|Name of the file|
|Size|integer|False|Size of the regular file (in bytes). If the file is a directory, no value is returned|
|Type|string|False|Type of the file, e.g. file or directory|

#### fingerprint

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Description|string|False|None|
|Family|string|False|None|
|Product|string|False|None|
|Vendor|string|False|None|
|Version|string|False|None|

#### history

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Date|string|False|Date the asset information was collected or changed|
|Description|string|False|Additional information describing the change|
|Scan ID|integer|False|If a scan-oriented change, the identifier of the corresponding scan the asset was scanned in|
|Type|string|False|Type, for additional information see the help section of this plugin|
|User|string|False|User|
|Version|integer|False|Version|
|Vulnerability Exception ID|integer|False|Vulnerability exception ID|

#### hostName

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Name|string|False|Name|
|Source|string|False|Source|

#### id

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|ID|
|Source|string|False|Source|

#### link

|Name|Type|Required|Description|
|----|----|--------|-----------|
|URL|string|False|A hypertext reference, which is either a URI (see RFC 3986) or URI template (see RFC 6570)|
|Rel|string|False|Link relation type following RFC 5988|

#### match

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Confidence|string|False|None|
|Fingerprint|fingerprint|False|None|

#### osFingerprint

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Architecture|string|False|The architecture of the operating system|
|Configuration|[]configuration|False|Configuration key-values pairs enumerated on the operating system|
|CPE|cpe|False|Common Platform Enumeration|
|Description|string|False|The description of the operating system (containing vendor, family, product, version and architecture in a single string)|
|Family|string|False|Family of the operating system|
|ID|integer|False|Identifier of the operating system|
|Product|string|False|Name of the operating system|
|System Name|string|False|A combination of vendor and family (with redundancies removed), suitable for grouping|
|Type|string|False|Type of operating system|
|Vendor|string|False|Vendor of the operating system|
|Version|string|False|Version of the operating system|

#### page

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Link Type|string|False|Type of link used to traverse or detect the page|
|Path|string|False|Path to the page (URI)|
|Response|integer|False|HTTP response code observed with retrieving the page|

#### PCI

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Adjusted CVSS score|integer|False|PCI adjusted CVSS score|
|Adjusted severity score|integer|False|PCI adjusted severity score|
|Fail|boolean|False|Whether this vulnerability results in a PCI assessment failure|
|Special Notes|string|False|PCI special notes|
|Status|string|False|PCI status|

#### remediation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Asset Count|integer|True|The number of assets that require the solution to be applied|
|Assets|[]remediation_asset|True|The assets that require the solution to be applied|
|Fix|string|False|The steps that are part of the fix this solution prescribes|
|Rapid7 Solution ID|string|True|The identifier of the solution within InsightVM/Nexpose|
|Risk Score|integer|True|The risk score that is reduced by performing the solution|
|Solution ID|integer|True|The identifier of the solution|
|Summary|string|True|Remediation summary|
|Vulnerabilities|[]remediation_vulnerability|True|The vulnerabilities that would be remediated|
|Vulnerability Count|integer|True|The number of vulnerabilities that would be remediated|

#### remediation_asset

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Criticality Tag|string|False|The criticality tag assigned to the asset|
|Hostname|string|False|Primary host name (local or FQDN) of the asset|
|ID|integer|True|Identifier of the asset|
|IP|string|True|Primary IPv4 or IPv6 address of the asset|
|MAC|string|False|Media Access Control (MAC) address, e.g. AF:12:BC:5A:F7:48|
|OS|string|False|Full description of the operating system of the asset|
|Risk Score|float|False|Risk score (with criticality adjustments) of the asset|

#### remediation_vulnerability

|Name|Type|Required|Description|
|----|----|--------|-----------|
|CVSS Score|string|True|The CVSS score of the vulnerability|
|Description|string|True|The description of the vulnerability|
|ID|integer|True|Identifier of the vulnerability|
|Risk Score|integer|True|The risk score of the vulnerability|
|Severity|integer|True|The severity of the vulnerability|
|Title|string|True|The title of the vulnerability|

#### report_id

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Report ID|integer|False|Identifer|
|Report Name|string|False|Name of report|

#### resources

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Applies To|string|False|None|
|Confidence|string|False|None|
|Estimate|string|False|None|
|ID|string|False|None|
|links|[]link|False|None|
|Matches|[]match|False|None|
|Steps|step|False|None|
|Summary|summary|False|None|
|Type|string|False|None|

#### role

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Description|string|True|The description of the role|
|Id|string|True|ID of the role, e.g 'global-admin'|
|Links|[]link|True|List of hypermedia links to corresponding or related resources|
|Name|string|True|Name of the role|
|Privileges|[]string|True|List of privileges assigned to the role|

#### scan

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Assets|integer|False|Count of assets identified during the scan|
|Duration|date|False|Duration of the scan|
|End Time|date|False|End time of the scan|
|Engine ID|integer|False|ID for the scan engine/scan engine pool used for the scan|
|Engine Name|string|False|Name of the scan engine/scan engine pool used for the scan|
|ID|integer|False|ID of the scan|
|Links|[]link|False|List of hypermedia links to corresponding resources|
|Message|string|False|Scan status message|
|Scan Name|string|False|Name of the scan|
|Scan Type|string|False|Type of scan (automated, manual, scheduled)|
|Site ID|integer|False|ID of the site scanned|
|Site Name|string|False|Name of the site scanned|
|Start Time|date|False|Start time for the scan|
|Started By|string|False|User that started the scan|
|Status|string|False|Scan status (aborted, unknown, running, finished, stopped, error, paused, dispatched, integrating)|
|Vulnerabilities|vulnerabilities_count|False|Counts of vulnerabilities identified during the scan|

#### scan_engine

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Address|string|True|Scan engine address (IP/hostname)|
|Content Version|string|False|Scan engine content version|
|Engine Pools|[]integer|True|Engine pool IDs with which the scan engine is associated|
|ID|integer|True|Scan engine identifier|
|Last Refreshed Date|date|False|Date and time when the engine last communicated with the console|
|Last Updated Date|date|False|Date and time when the engine was last updated|
|Links|[]link|True|List of hypermedia links to corresponding resources|
|Name|string|True|Scan engine name|
|Port|integer|True|Scan engine communication port|
|Product Version|string|False|Scan engine product version|
|Sites|[]integer|False|Sites with which the scan engine is associated|

#### scan_engine_pool

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Engines|[]integer|True|List of scan engine IDs associated with the scan engine pool|
|ID|integer|True|Scan engine pool identifier|
|Links|[]link|True|List of hypermedia links to corresponding resources|
|Name|string|True|Scan engine pool name|

#### service

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Configurations|[]configuration|False|Configuration key-values pairs enumerated on the service|
|Databases|[]database|False|Databases enumerated on the service|
|Family|string|False|Family of the service|
|Links|[]link|False|Hypermedia links to corresponding or related resources|
|Name|string|False|Name of the service|
|Port|integer|False|Port of the service|
|Product|string|False|Product running the service|
|Protocol|string|False|Protocol of the service|
|User Groups|[]userGroup|False|User groups|
|Users|[]user|False|Users|
|Vendor|string|False|Vendor of the service|
|Version|string|False|Version of the service|
|Web Applications|[]webApplication|False|Web applications found on the service|

#### site

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Assets|integer|True|Site asset count|
|Connection Type|string|False|Site discovery connection type (if applicable)|
|Description|string|False|Site description|
|ID|integer|True|Identifier of the site|
|Importance|string|True|Site importance, used with the 'weighted' risk scoring strategy|
|Last Scan Time|date|False|Site last scan time|
|Links|[]link|True|Hypermedia links to corresponding or related resources|
|Name|string|True|Site name|
|Risk Score|float|True|Site risk score|
|Scan Engine|integer|True|Site default scan engine ID|
|Scan Template|string|True|Site default scan template|
|Type|string|True|Site type|
|Vulnerabilities|vulnerabilities_count|True|Site vulnerability counts|

#### software

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Configurations|[]configuration|False|Configurations|
|CPE|cpe|False|CPE|
|Description|string|False|Description of the software|
|Family|string|False|Family of the software|
|ID|integer|False|ID|
|Product|string|False|Product of the software|
|Type|string|False|Type of the software|
|Vendor|string|False|Vendor of the software|
|Version|string|False|Version of the software|

#### step

|Name|Type|Required|Description|
|----|----|--------|-----------|
|HTML|string|False|None|
|text|string|False|None|

#### summary

|Name|Type|Required|Description|
|----|----|--------|-----------|
|HTML|string|False|None|
|text|string|False|None|

#### tag

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Color|string|False|Tag color|
|Created|date|False|Tag creation date|
|ID|integer|True|Tag ID|
|Links|[]link|False|Hypermedia links to corresponding or related resources|
|Name|string|True|Tag name|
|Risk Modifier|string|False|Tag risk score modifier|
|Search Criteria|object|False|Tag search criteria|
|Source|string|False|Tag source|
|Type|string|True|Tag type|

#### tag_asset

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|True|Asset ID|
|Sources|[]string|True|Tag association sources|

#### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Full Name|string|False|Full name of the user account|
|ID|integer|False|Identifier of the user account|
|Name|string|False|Name of the user account|

#### userGroup

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|False|Identifier of the user group|
|Name|string|False|Name of the user group|

#### user_account

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Authentication|authentication_source|False|The authentication source used to authenticate the user|
|Email|string|False|The email address of the user|
|Enabled|boolean|False|Whether the user account is enabled|
|ID|integer|False|The identifier of the user|
|Links|[]link|False|List of hypermedia links to corresponding or related resources|
|Locale|user_account_locale|False|The locale and language preferences for the user|
|Locked|boolean|True|Whether the user account is locked (exceeded maximum password retry attempts)|
|Login|string|True|The login name of the user|
|Name|string|True|The full name of the user|
|Role|user_account_role|False|The privileges and role the user is assigned|

#### user_account_locale

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Default|string|True|Default locale|
|Reports|string|True|Reports locale|

#### user_account_role

|Name|Type|Required|Description|
|----|----|--------|-----------|
|All Asset Groups|boolean|False|Whether the user has access to all asset groups|
|All Sites|boolean|False|Whether the user has access to all sites|
|ID|string|False|The identifier of the role the user is assigned to|
|Privileges|[]string|False|None|
|Superuser|boolean|False|Whether the user is a superuser|

#### vulnerabilities

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Critical|integer|False|Number of critical vulnerabilities|
|Exploits|integer|False|Number of distinct exploits that can exploit any of the vulnerabilities on the asset|
|Malware Kits|integer|False|Number of distinct malware kits that vulnerabilities on the asset are susceptible to|
|Moderate|integer|False|Number of moderate vulnerabilities|
|Severe|integer|False|Number of severe vulnerabilities|
|Total|integer|False|Total number of vulnerabilities|

#### vulnerabilities_count

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Critical|integer|False|Number of critical vulnerabilities|
|Moderate|integer|False|Number of moderate vulnerabilities|
|Severe|integer|False|Number of severe vulnerabilities|
|Total number of vulnerabilities|integer|False|Total|

#### vulnerability

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Added|date|False|Date that the vulnerability was added to InsightVM|
|Categories|[]string|False|List of vulnerabilities categories with which this vulnerability is affiliated|
|CVEs|[]string|False|List of CVE identifiers associated with this vulnerability|
|CVSS|CVSS|False|Vulnerability CVSS details|
|Denial of Service|boolean|False|Whether the vulnerability is a denial of service vulnerability|
|Description|vulnerability_description|False|Vulnerability description|
|Exploits|integer|False|Exploit count|
|ID|string|False|Vulnerability ID|
|Links|[]link|False|List of hypermedia links to corresponding resources|
|Malware Kits|integer|False|Malware kit count|
|Modified|date|False|Date the vulnerability was last modified in InsightVM|
|PCI|PCI|False|Vulnerability PCI details|
|Published|date|False|Date the vulnerability was published|
|Risk Score|float|False|Vulnerability risk score using the configured risk scoring strategy (RealRisk by default)|
|Severity|string|False|Vulnerability severity string (Moderate/Severe/Critical)|
|Severity Score|integer|False|Vulnerability severity score|
|Title|string|False|Vulnerability title|

#### vulnerability_description

|Name|Type|Required|Description|
|----|----|--------|-----------|
|HTML|string|False|Vulnerability description HTML|
|Text|string|False|Vulnerability description raw text|

#### vulnerability_exception

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Expires|date|False|The date and time the vulnerability exception is set to expire|
|Vulnerability Exception ID|integer|True|The ID uniquely identifying the vulnerability exception|
|Links|[]link|False|Hypermedia links to corresponding or related resources|
|Review Details|object|False|Details of the exception review|
|Exception Scope|object|True|Details of the scope of the exception|
|State|string|True|The state of the vulnerability exception|
|Submission Details|object|True|Details of the exception submission|

#### vulnerability_solution

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Links|[]link|False|Hypermedia links to corresponding or related resources|
|Solutions|[]resources|False|Solutions to vulnerabilities|

#### webApplication

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|False|Identifier of the web application|
|Pages|[]page|False|Pages|
|Root|string|False|Web root of the web application|
|Virtual Host|string|False|Virtual host of the web application|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 3.1.0 - Add Cloud enablement to plugin | Updated exception information and error handling | Made status code output for Stop Scan and Get Scan actions more exact | Fix bug relating to empty inputs being passed in request body
* 3.0.0 - Changed output of Get Asset action to include vulnerabilities properly
* 2.2.0 - Added ability to include vulnerabilities on Get Asset action | API call update
* 2.1.0 - Added scanned asset_ids as an output of start_scan
* 2.0.0 - Fix issue where string data-type should be date in actions | Update docs
* 1.0.0 - Initial plugin

# Links

## References

* [InsightVM Cloud API](https://help.rapid7.com/insightvm/en-us/api/integrations.html)
* [Managing Platform API Keys](https://docs.rapid7.com/insight/managing-platform-api-keys)
* [Scan Engine Pairing](https://docs.rapid7.com/insightvm/scan-engine-management-on-the-insight-platform/#how-to-pair-your-scan-engines-to-the-insight-platform)
