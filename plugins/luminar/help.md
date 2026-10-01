# Description

LUMINAR is an AI-powered external threat intelligence solution that empowers security and risk management leaders with comprehensive visibility into their threat landscape. LUMINAR consolidates all critical threat intelligence capabilities into one unified solution.


# Key Features
  
*Fetch feeds from Luminar Taxii server*

# Requirements
  
*Requires Luminar ClientID, AccountID and ClientSecret.*

# Supported Product Versions

* 2025-09-10

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|account_id|string|None|True|Enter the account ID|None|None|None|None|
|base_url|string|www.cyberluminar.com|True|Enter the Luminar Base URL|None|None|None|None|
|client_id|string|None|True|Enter the client ID|None|None|None|None|
|client_secret|credential_secret_key|None|True|Enter the client secret|None|None|None|None|

Example input:

```
{
  "account_id": "",
  "base_url": "www.cyberluminar.com",
  "client_id": "",
  "client_secret": {
    "secretKey": ""
  }
}
```

## Technical Details

### Triggers


#### Get Cyberfeed feeds

This trigger is used to trigger workflows to get cyberfeeds from Luminar

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|86400|False|Poll frequency in seconds|None|300|None|None|
|initial_fetch_date|string|None|True|The date from which the initial fetch will start. eg YYYY-MM-DD|None|2025-01-01|None|None|
  
Example input:

```
{
  "frequency": 86400,
  "initial_fetch_date": "2025-01-01"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]object|True|cyber feed results|None|
  
Example output:

```
{
  "results": [
    {
      "type": "malware",
      "spec_version": "2.1",
      "id": "malware--b6fa03e7-d74f-5dea-b122-66a5b9bd377b",
      "created": "2025-09-21T05:54:10.000Z",
      "modified": "2025-09-21T19:00:08.762Z",
      "extensions": {
        "extension-definition--ddd2bf71-3c91-5f4d-8251-10cd685737c3": {
          "extension_type": "property-extension",
          "luminar_tenant_id": "XXXXX"
        }
      },
      "name": "CountLoader",
      "aliases": [],
      "capabilities": [
        "cleans-traces-of-infection",
        "communicates-with-c2",
        "fingerprints-host",
        "installs-other-components",
        "persists-after-system-reboot"
      ],
      "malware_types": [
        "dropper"
      ],
      "is_family": false,
      "related_obj": {
        "type": "malware",
        "spec_version": "2.1",
        "id": "malware--f2a44ffe-4f11-5987-a890-09baeca96b4a",
        "created": "2025-09-21T05:54:10.000Z",
        "modified": "2025-09-21T19:00:08.762Z",
        "extensions": {
          "extension-definition--ddd2bf71-3c91-5f4d-8251-10cd685737c3": {
            "extension_type": "property-extension",
            "luminar_tenant_id": "XXXXX"
          }
        },
        "name": "PureHVNC",
        "aliases": [],
        "malware_types": [
          "remote-access-trojan"
        ],
        "is_family": false,
        "related_as": "downloads"
      }
    },
    {
      "type": "malware",
      "spec_version": "2.1",
      "id": "malware--b6fa03e7-d74f-5dea-b122-66a5b9bd377b",
      "created": "2025-09-21T05:54:10.000Z",
      "modified": "2025-09-21T19:00:08.762Z",
      "extensions": {
        "extension-definition--ddd2bf71-3c91-5f4d-8251-10cd685737c3": {
          "extension_type": "property-extension",
          "luminar_tenant_id": "XXXXX"
        }
      },
      "name": "CountLoader",
      "aliases": [],
      "capabilities": [
        "cleans-traces-of-infection",
        "communicates-with-c2",
        "fingerprints-host",
        "installs-other-components",
        "persists-after-system-reboot"
      ],
      "malware_types": [
        "dropper"
      ],
      "is_family": false,
      "related_obj": {
        "type": "malware",
        "spec_version": "2.1",
        "id": "malware--f2a44ffe-4f11-5987-a890-09baeca96b4a",
        "created": "2025-09-21T05:54:10.000Z",
        "modified": "2025-09-21T19:00:08.762Z",
        "extensions": {
          "extension-definition--ddd2bf71-3c91-5f4d-8251-10cd685737c3": {
            "extension_type": "property-extension",
            "luminar_tenant_id": "XXXXX"
          }
        },
        "name": "PureHVNC",
        "aliases": [],
        "malware_types": [
          "remote-access-trojan"
        ],
        "is_family": false,
        "related_as": "uses"
      }
    },
    {
      "type": "report",
      "spec_version": "2.1",
      "id": "report--da299b90-93c2-5953-b9cc-8b415d891543",
      "created": "2025-09-21T05:54:10.000Z",
      "modified": "2025-09-21T19:00:08.760Z",
      "extensions": {
        "extension-definition--ddd2bf71-3c91-5f4d-8251-10cd685737c3": {
          "extension_type": "property-extension",
          "luminar_tenant_id": "XXXXX"
        }
      },
      "name": "Fortra Releases Critical Patch for CVSS 10.0 GoAnywhere MFT Vulnerability",
      "description": "A critical deserialization vulnerability, tracked as CVE-2025-10035, was identified in the License Servlet of GoAnywhere MFT, with a maximum CVSS 3.1 base score of 10.0. Exploitation enables an attacker possessing a validly forged license response signature to deserialize arbitrary actor-controlled objects, which can potentially lead to command injection on affected systems. The vulnerability is categorized under CWE-77 and CWE-502, involving both improper neutralization of special elements used in a command and unsafe deserialization of untrusted data. Successful exploitation requires systems to be externally exposed to the internet but does not require authentication or user interaction. Impact includes possible compromise to confidentiality, integrity, and availability of targeted installations.",
      "published": "2025-09-21T05:54:10.000Z",
      "report_types": [
        "vulnerability"
      ],
      "object_refs": [
        "vulnerability--f8c0d0df-822e-5e94-b60a-a6d2165f5c7b",
        "software--cfcb1a7e-a2b8-5f43-a15a-726cf7a6b4a3"
      ],
      "ref_objects": [
        {
          "type": "vulnerability",
          "spec_version": "2.1",
          "id": "vulnerability--f8c0d0df-822e-5e94-b60a-a6d2165f5c7b",
          "created": "2025-09-21T05:54:10.000Z",
          "modified": "2025-09-21T19:00:08.760Z",
          "extensions": {
            "extension-definition--ddd2bf71-3c91-5f4d-8251-10cd685737c3": {
              "extension_type": "property-extension",
              "luminar_tenant_id": "XXXXX"
            }
          },
          "name": "CVE-2025-10035",
          "external_references": [
            {
              "source_name": "cve",
              "external_id": "CVE-2025-10035"
            }
          ]
        },
        {
          "type": "software",
          "spec_version": "2.1",
          "id": "software--cfcb1a7e-a2b8-5f43-a15a-726cf7a6b4a3",
          "extensions": {
            "extension-definition--ddd2bf71-3c91-5f4d-8251-10cd685737c3": {
              "extension_type": "property-extension",
              "luminar_tenant_id": "XXXXX"
            }
          },
          "name": "GoAnywhere MFT"
        }
      ]
    }
  ]
}
```

#### Get IOC feeds

This trigger is used to trigger workflows to get IOC feeds from Luminar

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|86400|False|Poll frequency in seconds|None|300|None|None|
|initial_fetch_date|string|None|True|The date from which the initial fetch will start. eg YYYY-MM-DD|None|2025-01-01|None|None|
  
Example input:

```
{
  "frequency": 86400,
  "initial_fetch_date": "2025-01-01"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]object|True|IOC feed results|None|
  
Example output:

```
{
  "results": [
    {
      "type": "indicator",
      "spec_version": "2.1",
      "id": "indicator--9bacc2e4-4126-52cc-83c3-9344794ff396",
      "created": "2025-09-15T00:00:00.000Z",
      "modified": "2025-09-15T06:00:30.558Z",
      "extensions": {
        "extension-definition--ddd2bf71-3c91-5f4d-8251-10cd685737c3": {
          "score": 85,
          "extension_type": "property-extension",
          "luminar_tenant_id": "XXXXX"
        }
      },
      "confidence": 85,
      "pattern": "[ipv4-addr:value = '89.169.13.147']",
      "created_by_ref": "identity--5bf1ac35-8d08-509e-b31a-044cb09b4199",
      "pattern_type": "stix",
      "indicator_types": [
        "malicious-activity"
      ],
      "valid_from": "2025-09-15T00:00:00.000Z",
      "valid_until": "2025-09-22T00:00:00.000Z",
      "related_obj": {
        "type": "software",
        "spec_version": "2.1",
        "id": "software--b1fb732c-1acb-5ab2-8446-4c499acab785",
        "extensions": {
          "extension-definition--ddd2bf71-3c91-5f4d-8251-10cd685737c3": {
            "extension_type": "property-extension",
            "luminar_tenant_id": "XXXXX"
          }
        },
        "name": "Win11",
        "version": "10.0.26100",
        "related_as": "indicates"
      },
      "iocs": [
        {
          "type": "ipv4-addr",
          "value": "89.169.13.147"
        }
      ]
    }
  ]
}
```

#### Get Leaked Records feeds

This trigger is used to trigger workflows to get leaked records feeds from Luminar

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|86400|False|Poll frequency in seconds|None|300|None|None|
|initial_fetch_date|string|None|True|The date from which the initial fetch will start. eg YYYY-MM-DD|None|2025-01-01|None|None|
  
Example input:

```
{
  "frequency": 86400,
  "initial_fetch_date": "2025-01-01"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]object|True|leaked records feed results|None|
  
Example output:

```
{
  "results": [
    {
      "type": "malware",
      "spec_version": "2.1",
      "id": "malware--fe203b39-f99a-53a5-9786-90bfddf1b6c7",
      "created": "2025-09-20T13:03:14.219Z",
      "modified": "2025-09-20T19:02:34.504Z",
      "extensions": {
        "extension-definition--ddd2bf71-3c91-5f4d-8251-10cd685737c3": {
          "extension_type": "property-extension",
          "luminar_tenant_id": "XXXXX"
        }
      },
      "name": "Generic Stealer",
      "capabilities": [
        "steals-authentication-credentials"
      ],
      "malware_types": [
        "spyware"
      ],
      "is_family": true,
      "related_obj": {
        "type": "incident",
        "spec_version": "2.1",
        "id": "incident--2fea2f99-cb64-5863-9aec-8607d0c69c14",
        "created": "2025-09-20T13:03:14.219Z",
        "modified": "2025-09-20T19:02:34.504Z",
        "extensions": {
          "extension-definition--ddd2bf71-3c91-5f4d-8251-10cd685737c3": {
            "extension_type": "property-extension",
            "luminar_tenant_id": "XXXXX",
            "luminar_threat_score": 71,
            "collection_date": "2025-09-20T19:00:04.687Z",
            "computer_name": "KARENBUENDIA (Smart FS_Karen)"
          }
        },
        "name": "Generic Stealer - KARENBUENDIA (Smart FS_Karen) - 112.201.109.103 - 20/09/2025",
        "created_by_ref": "identity--5bf1ac35-8d08-509e-b31a-044cb09b4199",
        "related_as": "related-to"
      }
    },
    {
      "type": "user-account",
      "spec_version": "2.1",
      "id": "user-account--88974857-b720-5174-a5e2-cc92bbf6cd38",
      "extensions": {
        "extension-definition--ddd2bf71-3c91-5f4d-8251-10cd685737c3": {
          "url": "https://fam.7-eleven.com/idp/SSO.saml2",
          "source": "ATO feed",
          "extension_type": "property-extension",
          "luminar_tenant_id": "XXXXX",
          "monitoring_plan_terms": [
            "7-eleven.com"
          ],
          "credential_is_fresh": true
        }
      },
      "credential": "leaked-****",
      "account_login": "trista.baker",
      "display_name": "trista.baker",
      "related_obj": {
        "type": "incident",
        "spec_version": "2.1",
        "id": "incident--2fea2f99-cb64-5863-9aec-8607d0c69c14",
        "created": "2025-09-20T13:03:14.219Z",
        "modified": "2025-09-20T19:02:34.504Z",
        "extensions": {
          "extension-definition--ddd2bf71-3c91-5f4d-8251-10cd685737c3": {
            "extension_type": "property-extension",
            "luminar_tenant_id": "XXXXX",
            "luminar_threat_score": 71,
            "collection_date": "2025-09-20T19:00:04.687Z",
            "computer_name": "KARENBUENDIA (Smart FS_Karen)"
          }
        },
        "name": "Generic Stealer - KARENBUENDIA (Smart FS_Karen) - 112.201.109.103 - 20/09/2025",
        "created_by_ref": "identity--5bf1ac35-8d08-509e-b31a-044cb09b4199",
        "related_as": "related-to"
      }
    },
    {
      "type": "ipv4-addr",
      "spec_version": "2.1",
      "id": "ipv4-addr--ae1e92c2-b017-50c1-be50-69497511d434",
      "extensions": {
        "extension-definition--ddd2bf71-3c91-5f4d-8251-10cd685737c3": {
          "extension_type": "property-extension",
          "luminar_tenant_id": "XXXXX"
        }
      },
      "value": "112.201.109.103",
      "related_obj": {
        "type": "incident",
        "spec_version": "2.1",
        "id": "incident--2fea2f99-cb64-5863-9aec-8607d0c69c14",
        "created": "2025-09-20T13:03:14.219Z",
        "modified": "2025-09-20T19:02:34.504Z",
        "extensions": {
          "extension-definition--ddd2bf71-3c91-5f4d-8251-10cd685737c3": {
            "extension_type": "property-extension",
            "luminar_tenant_id": "XXXXX",
            "luminar_threat_score": 71,
            "collection_date": "2025-09-20T19:00:04.687Z",
            "computer_name": "KARENBUENDIA (Smart FS_Karen)"
          }
        },
        "name": "Generic Stealer - KARENBUENDIA (Smart FS_Karen) - 112.201.109.103 - 20/09/2025",
        "created_by_ref": "identity--5bf1ac35-8d08-509e-b31a-044cb09b4199",
        "related_as": "related-to"
      }
    }
  ]
}
```

## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History
  
*1.0.0 - Initial plugin*

# Links
  
## References
  
*https://www.cognyte.com/solutions/external-threat-intelligence/*