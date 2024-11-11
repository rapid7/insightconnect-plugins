# Description

[Sophos Central](https://www.sophos.com) is a unified console for managing Sophos products. Using the Sophos Central plugin for Rapid7 InsightConnect, users can get alerts, endpoints, and SIEM events

# Key Features

* Get endpoints
* Get alerts
* Antivirus Scan
* Get agent details
* Check Tamper Protection status
* Isolate Endpoint
* Get Endpoint Groups
* Add Endpoint Group
* Get Endpoint Group
* Add Endpoint to Group
* Remove Endpoint from Group
* Get Allowed Items
* Add Allowed Item
* Remove Allowed Item
* Get Blocked Items
* Add Blocked Item
* Remove Blocked Item

# Requirements

* Sophos Central API tenant credentials

# Supported Product Versions

* Sophos Central API 2023-03-10

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|client_id|credential_secret_key|None|True|Client ID for Sophos Central instance|None|8a9jbad0-12ab-88be-cad4-3b4cad6f78e0|None|None|
|client_secret|credential_secret_key|None|True|Client secret key that allows access to Sophos Central|None|a1e263620c12382b36054cf34512ef836854e61d27ab2d079dda27af903a5b6eec396416b2dc40aabce6edfg670b0790d9a90|None|None|
|region|string|US East|False|API region|["US West", "US East", "EU Ireland", "DE Germany"]|US East|None|None|
|tenant_id|credential_secret_key|None|False|Tenant ID for Sophos Central instance|None|5b0eba20-ab12-34cd-88be-3a4cdc6a70f8|None|None|

Example input:

```
{
  "client_id": "8a9jbad0-12ab-88be-cad4-3b4cad6f78e0",
  "client_secret": "a1e263620c12382b36054cf34512ef836854e61d27ab2d079dda27af903a5b6eec396416b2dc40aabce6edfg670b0790d9a90",
  "region": "US East",
  "tenant_id": "5b0eba20-ab12-34cd-88be-3a4cdc6a70f8"
}
```

## Technical Details

### Actions


#### Add Allowed Item

This action is used to exempt an item from conviction

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|True|Comment indicating why the item should be allowed|None|Example comment|None|None|
|originEndpointId|string|None|False|Endpoint where the item to be allowed was last seen|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|None|None|
|originPersonId|string|None|False|Person associated with the endpoint where the item to be allowed was last seen|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|None|None|
|propertiesCertificateSigner|string|None|False|Properties value saved for the certificateSigner. Required if 'certificateSigner' is selected in the Type input|None|Example signer|None|None|
|propertiesFileName|string|None|False|Properties file name for the application|None|sample.txt|None|None|
|propertiesPath|string|None|False|Properties path for the application. Required if 'path' is selected in the Type input|None|$path/sample.txt|None|None|
|propertiesSha256|string|None|False|Properties SHA256 value for the application. Required if 'SHA256' is selected in the Type input|None|ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad|None|None|
|type|string|None|True|Property by which an item is allowed. You need to fill in the input starting with 'properties' for the selected type|["sha256", "path", "certificateSigner"]|sha256|None|None|
  
Example input:

```
{
  "comment": "Example comment",
  "originEndpointId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
  "originPersonId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
  "propertiesCertificateSigner": "Example signer",
  "propertiesFileName": "sample.txt",
  "propertiesPath": "$path/sample.txt",
  "propertiesSha256": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
  "type": "sha256"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|allowedItem|item|False|Allowed item created|{}|
  
Example output:

```
{
  "allowedItem": {
    "id": "714083d8-18eb-4f7d-b552-8ccd93e4e560",
    "createdAt": "2023-01-01T11:11:11.111Z",
    "updatedAt": "2023-01-01T11:11:11.111Z",
    "properties": {
      "sha256": "050c194cbbb"
    },
    "comment": "Test comment",
    "type": "sha256",
    "originEndpointId": {
      "id": "fde30644-050f-486d-a54e-06210b892dff"
    }
  }
}
```

#### Add Blocked Item

This action is used to block an item from exoneration

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|True|Comment indicating why the item should be blocked|None|Example comment|None|None|
|propertiesCertificateSigner|string|None|False|Properties value saved for the certificateSigner|None|Example signer|None|None|
|propertiesFileName|string|None|False|Properties file name for the application|None|sample.txt|None|None|
|propertiesPath|string|None|False|Properties path for the application|None|$path/sample.txt|None|None|
|propertiesSha256|string|None|True|Properties SHA256 value for the application|None|ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad|None|None|
|type|string|sha256|True|Property by which an item is blocked. The following values are allowed: SHA256|None|sha256|None|None|
  
Example input:

```
{
  "comment": "Example comment",
  "propertiesCertificateSigner": "Example signer",
  "propertiesFileName": "sample.txt",
  "propertiesPath": "$path/sample.txt",
  "propertiesSha256": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
  "type": "sha256"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|blockedItem|item|False|Blocked item created|{}|
  
Example output:

```
{
  "blockedItem": {
    "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
    "createdAt": "2023-03-02T13:00:19.494Z",
    "updatedAt": "2023-03-02T13:00:19.494Z",
    "properties": {
      "fileName": "sample.txt",
      "path": "$path/sample.txt",
      "sha256": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
      "certificateSigner": "Example signer"
    },
    "comment": "Example comment",
    "type": "sha256",
    "createdBy": {
      "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "name": "Example name"
    },
    "originPerson": {
      "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "name": "Example name"
    },
    "originEndpoint": {
      "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c"
    }
  }
}
```

#### Add Endpoint Group

This action is used to add a new endpoint group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|False|Group description|None|Example description|None|None|
|endpointIds|[]string|None|False|List of endpoint IDs that will be added to the group|None|["9de5069c-5afe-602b-2ea0-a04b66beb2c0"]|None|None|
|name|string|None|True|Endpoint group name|None|Example Group|None|None|
|type|string|computer|True|Group type|["computer", "server"]|computer|None|None|
  
Example input:

```
{
  "description": "Example description",
  "endpointIds": [
    "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
  ],
  "name": "Example Group",
  "type": "computer"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|endpointGroup|endpointGroup|False|Information about the created endpoint group|{}|
  
Example output:

```
{
  "endpointGroup": {
    "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
    "name": "Example Group",
    "description": "Example description",
    "type": "computer",
    "endpoints": {
      "total": 1,
      "itemsCount": 1,
      "items": [
        {
          "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
          "hostname": "Test"
        }
      ]
    },
    "tenant": {
      "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
    },
    "createdAt": "2023-03-24T07:45:29.813Z"
  }
}
```

#### Add Endpoint to Group

This action is used to add endpoints to your group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|groupId|string|None|True|Endpoint group ID|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|None|None|
|ids|[]string|None|True|List of endpoint IDs|None|["9de5069c-5afe-602b-2ea0-a04b66beb2c0"]|None|None|
  
Example input:

```
{
  "groupId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
  "ids": [
    "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|addedEndpoints|[]endpointObject|False|Endpoints added to the group|[]|
  
Example output:

```
{
  "addedEndpoints": [
    {
      "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "hostname": "test"
    }
  ]
}
```

#### Antivirus Scan

This action is used to sends a request to the specified endpoint to perform or configure a scan

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|True|Agent ID, IPv4 address, IPv6 address, MAC address or hostname|None|198.51.100.100|None|None|
  
Example input:

```
{
  "agent": "198.51.100.100"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|string|True|Antivirus scan ID|999fd666-9666-4e66-a066-d66fd966ad66|
|requested_at|string|True|Antivirus scan requested at|2020-08-02 21:30:55.487000+00:00|
|status|string|True|Antivirus scan status|requested|
  
Example output:

```
{
  "id": "999fd666-9666-4e66-a066-d66fd966ad66",
  "requested_at": "2020-08-02 21:30:55.487000+00:00",
  "status": "requested"
}
```

#### Blacklist

This action is used to blocks a hash across all systems

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|blacklist_state|boolean|None|True|Set true to blacklist hash, set false to unblacklist hash|None|True|None|None|
|description|string|Hash Blacklisted from InsightConnect|False|Description for why the hash is blacklisted|None|Hash Blacklisted from InsightConnect|None|None|
|hash|string|None|True|Create a blacklist item from a SHA256 hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|None|None|
  
Example input:

```
{
  "blacklist_state": true,
  "description": "Hash Blacklisted from InsightConnect",
  "hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Return true if blacklist item was created or deleted|True|
  
Example output:

```
{
  "success": true
}
```

#### Check Tamper Protection Status

This action is used to get tamper status by IP address, Hostname, MAC address or Device ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|True|Device ID, IPv4 address, IPv6 address, MAC address or hostname|None|198.51.100.100|None|None|
  
Example input:

```
{
  "agent": "198.51.100.100"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|tamper_status|check_tamper_protection_status|True|Tamper status for provided agent|{}|
  
Example output:

```
{
  "tamper_status": {
    "enabled": true
  }
}
```

#### Get Agent Details

This action is used to get details for an agent

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|True|Agent to retrieve device information from. Accepts IPv4 address, IPv6 address, MAC address, hostname, or device ID|None|198.51.100.100|None|None|
  
Example input:

```
{
  "agent": "198.51.100.100"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|agent|endpoint_entry|True|Details for the matched agent|{}|
  
Example output:

```
{
  "agent": {
    "associatedPerson": {
      "id": "999fd666-9666-4e66-a066-d66fd966ad66",
      "name": "Name\\crest",
      "viaLogin": "Name-log\\crest"
    },
    "capabilities": [],
    "encryption": {
      "volumes": [
        {
          "status": "notEncrypted",
          "volumeId": "999fd666-9666-4e66-a066-d66fd966ad66"
        }
      ]
    },
    "health": {
      "overall": "good",
      "services": {
        "serviceDetails": [
          {
            "name": "SophosMcsAgentD",
            "status": "running"
          },
          {
            "name": "SophosCleanD",
            "status": "running"
          },
          {
            "name": "SophosAntiVirus",
            "status": "running"
          },
          {
            "name": "SophosEncryptionCentralAdapter",
            "status": "running"
          },
          {
            "name": "SophosWebIntelligence",
            "status": "running"
          },
          {
            "name": "SophosEncryptionD",
            "status": "running"
          },
          {
            "name": "SophosHealthD",
            "status": "running"
          },
          {
            "name": "SophosScanD",
            "status": "running"
          },
          {
            "name": "SophosAutoUpdate",
            "status": "running"
          },
          {
            "name": "SophosSXLD",
            "status": "running"
          },
          {
            "name": "SophosConfigD",
            "status": "running"
          },
          {
            "name": "SophosEventMonitor",
            "status": "running"
          }
        ],
        "status": "good"
      },
      "threats": {
        "status": "good"
      }
    },
    "hostname": "Example_hostname",
    "id": "999fd666-9666-4e66-a066-d66fd966ad66",
    "ipv4Addresses": [
      "198.51.100.100"
    ],
    "ipv6Addresses": [
      "2001:db8:8:4::2"
    ],
    "lastSeenAt": "2020-07-31T07:19:37.306Z",
    "macAddresses": [
      "30:00:00:ba:00:00"
    ],
    "os": {
      "build": 6,
      "isServer": false,
      "majorVersion": 10,
      "minorVersion": 14,
      "platform": "macOS"
    },
    "tamperProtectionEnabled": false,
    "tenant": {
      "id": "999fd666-9666-4e66-a066-d66fd966ad66"
    },
    "type": "computer"
  }
}
```

#### Get Alerts

This action is used to get alerts for a customer based on the parameters provided

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|from_date|string|None|False|The starting date from which alerts will be retrieved defined as Unix timestamp in UTC. Must be within last 24 hours|None|2019-09-23 12:02:01.700000+00:00|None|None|
  
Example input:

```
{
  "from_date": "2019-09-23T12:02:01.700Z"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alerts|[]alert_entity|True|Alerts for specified time period|[]|
  
Example output:

```
{
  "alerts": [
    {
      "managedAgent": {},
      "severity": "LOW",
      "type": "Event::Mobile::ApnsCertificateRenewed",
      "allowedActions": [
        "acknowledge"
      ],
      "description": "Your APNs certificate was renewed",
      "id": "1ffcae82-97d2-46e8-83e8-469525c28513",
      "raisedAt": "2020-07-19T07:22:07.019Z",
      "tenant": {
        "id": "11f446c2-a094-427f-868e-bd13e2f5b27e",
        "name": "NinjaRMM LLC"
      },
      "category": "mobiles",
      "groupKey": "MyxFdmVudDo6TW9iaWxlOjpBcG5zQ2VydGlmaWNhdGVSZW5ld2...",
      "product": "mobile"
    }
  ]
}
```

#### Get Allowed Items

This action is used to get a list of allowed items

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page|integer|1|False|The page number to fetch|None|3|None|None|
|pageSize|integer|50|False|The size of the page requested|None|5|None|None|
|pageTotal|boolean|None|False|Whether the number of pages should be calculated and returned in the response|None|False|None|None|
  
Example input:

```
{
  "page": 3,
  "pageSize": 5,
  "pageTotal": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|items|[]item|False|List of allowed items|[]|
|pages|pages|False|Pages details|{}|
  
Example output:

```
{
  "items": [
    {
      "id": "f8d03561-90d1-4c18-b576-34509e843ee1",
      "createdAt": "2023-01-01T11:11:11.111Z",
      "updatedAt": "2023-01-01T11:11:11.111Z",
      "properties": {
        "path": "$path/sample.txt"
      },
      "comment": "Test comment",
      "type": "path"
    },
    {
      "id": "f8d03561-90d1-4c18-b576-34509e843ee2",
      "createdAt": "2023-01-01T11:11:11.111Z",
      "updatedAt": "2023-01-01T11:11:11.111Z",
      "properties": {
        "sha256": "ba7816bf8f01cfea414140de5dae2223b10361a396177a9cb410ff61f20015af"
      },
      "comment": "Test comment",
      "type": "sha256"
    },
    {
      "id": "f8d03561-90d1-4c18-b576-34509e843ee3",
      "createdAt": "2023-01-01T11:11:11.111Z",
      "updatedAt": "2023-01-01T11:11:11.111Z",
      "properties": {
        "certificateSigner": "Example signer"
      },
      "comment": "Test comment",
      "type": "certificateSigner"
    }
  ],
  "pages": {
    "current": 1,
    "size": 3,
    "maxSize": 100
  }
}
```

#### Get Blocked Items

This action is used to get a list of blocked items

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page|integer|1|False|The page number to fetch, starting with 1|None|1|None|None|
|pageSize|integer|50|False|The size of the page requested|None|50|None|None|
|pageTotal|boolean|False|False|Whether the number of pages should be calculated and returned in the response|None|False|None|None|
  
Example input:

```
{
  "page": 1,
  "pageSize": 50,
  "pageTotal": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|items|[]item|False|List of blocked items|[]|
|pages|pages|False|Pages details|{}|
  
Example output:

```
{
  "items": [
    {
      "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "createdAt": "2023-03-02T13:00:19.494Z",
      "updatedAt": "2023-03-02T13:00:19.494Z",
      "properties": {
        "fileName": "sample.txt",
        "path": "$path/sample.txt",
        "sha256": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
        "certificateSigner": "Example signer"
      },
      "comment": "Example comment",
      "type": "sha256",
      "createdBy": {
        "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
        "name": "Example name"
      },
      "originPerson": {
        "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
        "name": "Example name"
      },
      "originEndpoint": {
        "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c"
      }
    }
  ],
  "pages": {
    "current": 1,
    "size": 50,
    "total": 1,
    "items": 2,
    "maxSize": 100
  }
}
```

#### Get Endpoint Group

This action is used to get endpoint group by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|groupId|string|None|True|Endpoint group ID|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|None|None|
  
Example input:

```
{
  "groupId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|endpointGroup|endpointGroup|False|Information about the provided endpoint group|{}|
  
Example output:

```
{
  "endpointGroup": {
    "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
    "name": "Example Group",
    "description": "Example description",
    "type": "computer",
    "endpoints": {
      "total": 1,
      "itemsCount": 1,
      "items": [
        {
          "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
          "hostname": "Test"
        }
      ]
    },
    "tenant": {
      "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
    },
    "createdAt": "2023-03-24T07:45:29.813Z"
  }
}
```

#### Get Endpoint Groups

This action is used to get endpoint groups

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|endpointIds|[]string|None|False|Endpoint IDs. Must contain at most 50 items that must be unique|None|["9de5069c-5afe-602b-2ea0-a04b66beb2c0"]|None|None|
|fields|[]string|None|False|The fields to return in a partial response|None|["name", "createdAt"]|None|None|
|groupType|string|all|False|Endpoint group type. The following values are allowed: all, computer, server|["all", "computer", "server"]|computer|None|None|
|ids|[]string|None|False|Endpoint group IDs to match. Must contain at most 50 items that must be unique|None|["9de5069c-5afe-602b-2ea0-a04b66beb2c0"]|None|None|
|page|integer|1|False|The page number to fetch|None|5|None|None|
|pageSize|integer|50|False|The size of the page requested|None|10|None|None|
|pageTotal|boolean|None|False|Whether the number of pages should be calculated and returned in the response|None|False|None|None|
|search|string|None|False|Term to search for in the specified search fields|None|Example|None|None|
|searchFields|[]string|None|False|Search your specified fields. The default is to search group names only. The following values are allowed: name, description|None|["description", "name"]|None|None|
|sort|[]string|None|False|Sort criteria for endpoint groups. Valid sort fields are id, name, createdAt, and updatedAt. You can append ':asc' or ':desc' to each field to specify the sort direction. The default sort direction for each field is unspecified|None|["createdAt:desc", "name:asc"]|None|None|
  
Example input:

```
{
  "endpointIds": [
    "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
  ],
  "fields": [
    "name",
    "createdAt"
  ],
  "groupType": "computer",
  "ids": [
    "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
  ],
  "page": 5,
  "pageSize": 10,
  "pageTotal": false,
  "search": "Example",
  "searchFields": [
    "description",
    "name"
  ],
  "sort": [
    "createdAt:desc",
    "name:asc"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|endpointGroups|[]endpointGroup|False|List of endpoint groups|[]|
|pages|pages|False|Pages details|{}|
  
Example output:

```
{
  "endpointGroups": [
    {
      "id": "f8d03561-90d1-4c18-b576-34509e843ee1",
      "name": "Example Group",
      "description": "Example description",
      "type": "computer",
      "endpoints": {
        "total": 1,
        "itemsCount": 1,
        "items": [
          {
            "id": "f8d03561-90d1-4c18-b576-34509e843ee8",
            "hostname": "EXAMPLE-HOSTNAME"
          }
        ]
      },
      "tenant": {
        "id": "f8d03561-90d1-4c18-b576-34509e843ee8"
      },
      "createdAt": "2023-01-01T11:11:11.111Z",
      "updatedAt": "2023-01-01T11:11:11.111Z"
    },
    {
      "id": "f8d03561-90d1-4c18-b576-34509e843ee3",
      "name": "Test Group 3",
      "description": "Example description",
      "type": "computer",
      "endpoints": {
        "total": 0,
        "itemsCount": 0,
        "items": []
      },
      "tenant": {
        "id": "f8d03561-90d1-4c18-b576-34509e843ee8"
      },
      "createdAt": "2023-01-01T11:11:11.111Z"
    }
  ],
  "pages": {
    "current": 1,
    "size": 50,
    "maxSize": 1000
  }
}
```

#### Get Endpoints

This action is used to get endpoints for a customer based on the last seen after date and time

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|since|string|None|False|Last seen after date and time (UTC) or duration inclusive, eg. 2019-09-23T12:02:01.700Z, -P1D, PT20M, PT4H500S|None|2019-09-23 12:02:01.700000+00:00|None|None|
  
Example input:

```
{
  "since": "2019-09-23T12:02:01.700Z"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|items|[]endpoint_entry|True|Endpoint items|[]|
  
Example output:

```
{
  "items": [
    {
      "id": "1d65be44-e663-437c-949c-2057b73c5630",
      "type": "computer",
      "tenant": {
        "id": "11f446c2-a094-427f-868e-bd13e2f5b27e"
      },
      "hostname": "WIN-JJS9RP995G8",
      "health": {
        "overall": "suspicious",
        "threats": {
          "status": "good"
        },
        "services": {
          "status": "good",
          "serviceDetails": [
            {
              "name": "File Detection",
              "status": "running"
            }
          ]
        }
      },
      "os": {
        "isServer": false,
        "platform": "windows",
        "name": "Windows 8.1",
        "majorVersion": 6,
        "minorVersion": 3,
        "build": 9600
      },
      "ipv4Addresses": [
        "198.51.100.1"
      ],
      "ipv6Addresses": [
        "2001:db8:8:4::2"
      ],
      "macAddresses": [
        "00:0C:29:9B:2F:DF"
      ],
      "associatedPerson": {
        "name": "WIN-JJS9RP995G8\\User",
        "viaLogin": "WIN-JJS9RP995G8\\User",
        "id": "ceddc646-43b2-4b9f-835a-d1ecb9af8253"
      },
      "tamperProtectionEnabled": true,
      "assignedProducts": [
        {
          "code": "endpointProtection",
          "version": "10.8.6",
          "status": "installed"
        }
      ],
      "capabilities": [],
      "lastSeenAt": "2020-04-08T17:27:32.059Z",
      "encryption": {
        "volumes": []
      }
    }
  ]
}
```

#### Get Endpoints in Group

This action is used to retrieve endpoints in your specified group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fields|[]string|None|False|The fields to return in a partial response. All fields are returned by default|None|["id", "type"]|None|None|
|groupId|string|None|True|Endpoint group ID|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|None|None|
|pageFromKey|string|None|False|Key of the page to fetch|None|exampleKey|None|None|
|pageSize|integer|50|False|The size of the page requested. Value must be inclusively between 1 and 1000|None|50|None|None|
|pageTotal|boolean|False|False|Whether the number of pages should be calculated and returned in the response|None|False|None|None|
|search|string|None|False|Term to search for in the specified search fields|None|example|None|None|
|searchFields|[]string|None|False|List of search fields for finding the given search term. The following values are allowed: "hostname", "groupName", "associatedPersonName", "ipAddresses", "osName"|None|["hostname", "groupName", "associatedPersonName", "ipAddresses", "osName"]|None|None|
|sort|[]string|None|False|Defines how to sort the data. Matches (^[^:]+$)|(^[^:]+:(asc|desc)$)|None|["id:asc"]|None|None|
  
Example input:

```
{
  "fields": [
    "id",
    "os",
    "type"
  ],
  "groupId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
  "pageFromKey": "",
  "pageSize": 1,
  "pageTotal": true,
  "search": "DESKTOP-1234568",
  "searchFields": [
    "hostname"
  ],
  "sort": [
    "id:asc"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|items|[]endpointsItem|False|List of endpoints belonging to the given group|[]|
|pages|pagesDetails|False|Pages details|{}|
  
Example output:

```
{
  "items": [
    {
      "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "type": "computer",
      "hostname": "DESKTOP-1234568",
      "os": {
        "isServer": false,
        "platform": "windows",
        "name": "Windows 10 Home N",
        "majorVersion": 10,
        "minorVersion": 0,
        "build": 19042
      }
    }
  ],
  "pages": {
    "size": 1,
    "total": 1,
    "items": 1,
    "maxSize": 500
  }
}
```

#### Isolate Endpoint

This action is used to turn on or off endpoint isolation for multiple endpoints

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment|string|None|False|Reason the endpoints should be isolated or not|None|Example comment|None|None|
|enabled|boolean|True|True|Whether the endpoints should be isolated or not|None|True|None|None|
|ids|[]string|None|True|List of endpoints IDs|None|["9de5069c-5afe-602b-2ea0-a04b66beb2c0"]|None|None|
  
Example input:

```
{
  "comment": "Example comment",
  "enabled": true,
  "ids": [
    "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|endpoints|[]endpointIsolation|False|List of endpoints for which isolation has been updated|[]|
  
Example output:

```
{
  "endpoints": [
    {
      "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "isolation": {
        "enabled": true,
        "lastEnabledBy": {
          "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
        },
        "comment": "Example comment"
      }
    }
  ]
}
```

#### Remove Allowed Item

This action is used to deletes the specified allowed item

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|allowedItemId|string|None|True|The identifier of the allowed item|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|None|None|
  
Example input:

```
{
  "allowedItemId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Whether the action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Remove Blocked Item

This action is used to deletes the specified blocked item

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|blockedItemId|string|None|True|The identifier of the blocked item|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|None|None|
  
Example input:

```
{
  "blockedItemId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Whether the item was deleted. Returns success if can't find item or it has been successfully deleted|True|
  
Example output:

```
{
  "success": true
}
```

#### Remove Endpoint from Group

This action is used to remove endpoints from a group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|groupId|string|None|True|Endpoint group ID|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|None|None|
|ids|[]string|None|True|List of endpoint IDs|None|["9de5069c-5afe-602b-2ea0-a04b66beb2c0"]|None|None|
  
Example input:

```
{
  "groupId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
  "ids": [
    "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|errors|endpointRemovalErrors|False|Information about which endpoints could not be removed from the group|{}|
|removedEndpoints|[]endpointObject|False|Endpoints removed from a group|[]|
  
Example output:

```
{
  "removedEndpoints": [
    {
      "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "hostname": "test"
    }
  ],
  "errors": {}
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**date_time_zone**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|fixed|boolean|None|None|None|None|
|id|string|None|None|None|None|
  
**chronology**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|zone|date_time_zone|None|None|None|None|
  
**date_time**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|afterNow|boolean|None|None|None|None|
|beforeNow|boolean|None|None|None|None|
|centuryOfEra|integer|None|None|None|None|
|chronology|chronology|None|None|None|None|
|dayOfMonth|integer|None|None|None|None|
|dayOfWeek|integer|None|None|None|None|
|dayOfYear|integer|None|None|None|None|
|equalNow|boolean|None|None|None|None|
|era|integer|None|None|None|None|
|hourOfDay|integer|None|None|None|None|
|millis|integer|None|None|None|None|
|millisOfDay|integer|None|None|None|None|
|millisOfSecond|integer|None|None|None|None|
|minuteOfDay|integer|None|None|None|None|
|minuteOfHour|integer|None|None|None|None|
|monthOfYear|integer|None|None|None|None|
|secondOfDay|integer|None|None|None|None|
|secondOfMinute|integer|None|None|None|None|
|weekOfWeekyear|integer|None|None|None|None|
|weekyear|integer|None|None|None|None|
|year|integer|None|None|None|None|
|yearOfCentury|integer|None|None|None|None|
|yearOfEra|integer|None|None|None|None|
|zone|date_time_zone|None|None|None|None|
  
**object_id**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|counter|integer|None|None|None|None|
|date|string|None|None|None|None|
|machineIdentifier|integer|None|None|None|None|
|processIdentifier|integer|None|None|None|None|
|time|integer|None|None|None|None|
|timeSecond|integer|None|None|None|None|
|timestamp|integer|None|None|None|None|
  
**customer_license**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|expired|boolean|None|None|None|None|
|expires_on|date_time|None|None|None|None|
|id|object_id|None|None|None|None|
|license_code|string|None|None|None|None|
|license_id|string|None|None|None|None|
|license_type|string|None|None|None|None|
|quota|integer|None|None|None|None|
|starts_on|date_time|None|None|None|None|
|suspended|boolean|None|None|None|None|
  
**previous_password_entity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|invalidated|date|None|None|None|None|
|password|string|None|None|None|None|
  
**check_tamper_protection_status**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Enabled|boolean|None|True|Return true when tamper protection is enable|None|
  
**tamper_protection_entity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|enabled|boolean|None|None|None|None|
|globally_enabled|boolean|None|None|None|None|
|password|string|None|None|None|None|
|previous_passwords|[]previous_password_entity|None|None|None|None|
  
**assigned_product**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|code|string|None|None|None|None|
|status|string|None|None|None|None|
|version|string|None|None|None|None|
  
**endpoint_entry**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|adSyncInfo|object|None|None|None|None|
|alert_status|integer|None|None|None|None|
|assignedProducts|[]assigned_product|None|None|None|None|
|awsInfo|object|None|None|None|None|
|azureInfo|object|None|None|None|None|
|beta|boolean|None|None|None|None|
|decloned_from|string|None|None|None|None|
|deleted_at|string|None|None|None|None|
|device_encryption_status_unmanaged|boolean|None|None|None|None|
|early_access_program|string|None|None|None|None|
|endpoint_type|string|None|None|None|None|
|group_full_name|string|None|None|None|None|
|group_id|string|None|None|None|None|
|group_name|string|None|None|None|None|
|health_status|integer|None|None|None|None|
|heartbeat_utm_name|string|None|None|None|None|
|id|string|None|None|None|None|
|info|object|None|None|None|None|
|is_adsync_group|boolean|None|None|None|None|
|java_id|string|None|None|None|None|
|last_activity|string|None|None|None|None|
|last_user|string|None|None|None|None|
|last_user_id|string|None|None|None|None|
|license_codes|[]string|None|None|None|None|
|machine_id|string|None|None|None|None|
|name|string|None|None|None|None|
|registered_at|string|None|None|None|None|
|status|object|None|None|None|None|
|tamper_protection|tamper_protection_entity|None|None|None|None|
|transport|string|None|None|None|None|
  
**current_licenses_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|licenses|[]customer_license|None|None|None|None|
  
**endpoint_whitelist_properties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|property|string|None|None|None|None|
|type|string|None|None|None|None|
  
**alert_entity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|created_at|string|None|None|The date at which the alert was created|None|
|customer_id|string|None|None|The unique identifier of the customer linked with this record|None|
|data|object|None|None|None|None|
|description|string|None|None|The description of the alert that was generated|None|
|event_service_event_id|string|None|None|The Event Services event id|None|
|id|string|None|None|Identifier for the alert|None|
|location|string|None|None|The location captured for this record|None|
|severity|string|None|None|The severity for this alert|None|
|source|string|None|None|Describes the source from alert was generated|None|
|threat|string|None|None|The name of the threat responsible for the generation of alert|None|
|threat_cleanable|boolean|None|None|None|None|
|type|string|None|None|Describes the type of the device on which alert was generated|None|
|when|string|None|None|The date at which the alert was created|None|
  
**customer_feature**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|expirationProcessed|boolean|None|None|None|None|
|expired|boolean|None|None|None|None|
|expiresOn|date_time|None|None|None|None|
|featureCode|string|None|None|None|None|
|generatedFromLicenseId|string|None|None|None|None|
|licenseCode|string|None|None|None|None|
|protection|boolean|None|None|None|None|
|valid|boolean|None|None|None|None|
  
**core_remedy_item**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|descriptor|string|None|None|None|None|
|result|string|None|None|None|None|
|type|string|None|None|None|None|
  
**installer_info**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|beta|boolean|None|None|None|None|
|command|string|None|None|None|None|
|platform|string|None|None|None|None|
|productName|string|None|None|None|None|
|url|string|None|None|None|None|
  
**customer_featuresResponse**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|features|[]customer_feature|None|None|None|None|
  
**core_remedy_items**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|items|[]core_remedy_item|None|None|None|None|
|totalItems|integer|None|None|None|None|
  
**legacy_event_entity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|core_remedy_items|core_remedy_items|None|None|details of the items cleaned or restored|None|
|created_at|string|None|None|The date at which the event was created|None|
|customer_id|string|None|None|The identifier of the customer for which record is created|None|
|endpoint_id|string|None|None|The corresponding endpoint id associated with the record|None|
|endpoint_type|string|None|None|The corresponding endpoint type associated with the record|None|
|group|string|None|None|The group associated with the group|None|
|id|string|None|None|The Identifier for the event|None|
|location|string|None|None|The location captured for this record|None|
|name|string|None|None|The name of the record created|None|
|origin|string|None|None|originating component of a detection|None|
|severity|string|None|None|The severity for this alert|None|
|source|string|None|None|The source for this record|None|
|threat|string|None|None|The threat associated with the record|None|
|type|string|None|None|The type of this record|None|
|user_id|string|None|None|The identifier of the user for which record is created|None|
|when|string|None|None|The date at which the event was created|None|
|whitelist_properties|[]endpoint_whitelist_properties|None|None|The properties by which this event can be whitelisted on an endpoint, if applicable|None|
  
**event_aggregate**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|has_more|boolean|None|None|None|None|
|items|[]legacy_event_entity|None|None|None|None|
|next_cursor|string|None|None|Value of the next cursor. This will be used to make next call of API|None|
  
**hashes_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|hashes|object|None|None|None|None|
  
**installer_info_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|installer_info|[]installer_info|None|None|None|None|
  
**pages**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Current|integer|None|False|The 1-based page number being returned|1|
|Items|integer|None|False|The total number of items across all pages, if pageTotal=true was passed into the request|1|
|Max Size|integer|None|False|The maximum page size that can be requested|100|
|Size|integer|None|False|The size of the page being returned|50|
|Total|integer|None|False|The total number of pages that exist, if pageTotal=true in the request|1|
  
**objectId**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|The ID of the referenced object|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Account ID|string|None|False|ID of the account|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Account Type|string|None|False|Type of the account|tenant|
|ID|string|None|False|Principal email or client ID|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Name|string|None|False|User principal name|Example name|
|Type|string|None|False|Principal type|user|
  
**userObject**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Unique ID for the user|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Name|string|None|False|Person's name|Example name|
  
**properties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Certificate Signer|string|None|False|Value saved for the certificateSigner|Example signer|
|File Name|string|None|False|File name|sample.txt|
|Path|string|None|False|Path for the application|$path/sample.txt|
|SHA256|string|None|False|SHA256 value for the application|ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad|
  
**item**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Comment|string|None|False|Comment indicating why the item was blocked or allowed|Example comment|
|Created At|string|None|False|Date and time (UTC) when the item was created|2023-03-02 13:00:19.494000+00:00|
|Created By|userObject|None|False|Created by|{}|
|ID|string|None|False|Item ID|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Origin Endpoint|objectId|None|False|Represents a referenced object|{}|
|Origin Person|userObject|None|False|Origin person|{}|
|Properties|properties|None|False|Item properties|{}|
|Type|string|None|False|Property by which an item is blocked or allowed|sha256|
|Updated At|string|None|False|Date and time (UTC) when the item was updated|2023-03-02 13:00:19.494000+00:00|
  
**isolationState**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Admin Isolated|boolean|None|False|Whether isolation was triggered by an admin|False|
|Self Isolated|boolean|None|False|Whether isolation was triggered by the endpoint itself|False|
|Status|string|None|False|Isolation status reported by endpoint. The following values are allowed: isolated, notIsolated|isolated|
  
**cloud**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Instance ID|string|None|False|Unique ID for the cloud instance|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Provider|string|None|False|Cloud provider in which the endpoint is running. The following values are allowed: aws, azure|aws|
  
**lockdown**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Status|string|None|False|Endpoint lockdown status. The following values are allowed: creatingWhitelist, installing, locked, notInstalled, registering, starting, stopping, unavailable, uninstalled, unlocked|creatingWhitelist|
|Update Status|string|None|False|Endpoint lockdown update status. The following values are allowed: upToDate, updating, rebootRequired, notInstalled|upToDate|
  
**volume**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Status|string|None|False|Endpoint volume encryption status. The following values are allowed: notEncrypted, encrypted, encrypting, notSupported, suspended, unknown|notEncrypted|
|Volume ID|string|None|False|Endpoint volume ID|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
  
**encryption**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Volumes|[]volume|None|False|Endpoint volumes|[]|
  
**assignedProduct**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Code|string|None|False|Endpoint product. The following values are allowed: coreAgent, interceptX, xdr, endpointProtection, deviceEncryption, mtr, ztna|coreAgent|
|Status|string|None|False|Installation status of a product assigned to the endpoint. The following values are allowed: installed, notInstalled|installed|
|Version|string|None|False|Version of a product assigned to an endpoint|Example version|
  
**associatedPerson**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Unique ID for the Person|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Name|string|None|False|Person's name|Example name|
|Via Login|string|None|False|Person's login on the endpoint|Example login|
  
**group**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Unique ID for endpoint group|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Name|string|None|False|Endpoint group name|Example name|
  
**osObject**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Build|integer|None|False|OS build|1|
|Is Server|boolean|None|False|Whether the OS is a server OS|False|
|Major Version|integer|None|False|OS major version|1|
|Minor Version|integer|None|False|OS minor version|1|
|Name|string|None|False|OS name as reported by the endpoint|Example name|
|Platform|string|None|False|OS platform type. The following values are allowed: windows, linux, macOS|windows|
  
**serviceDetails**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Service name|Service name|
|Status|string|None|False|Status of a service on an endpoint. The following values are allowed: running, stopped, missing|running|
  
**services**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Service Details|[]serviceDetails|None|False|Details of services on the endpoint|[]|
|Status|string|None|False|Health status of an endpoint or a service running on an endpoint. The following values are allowed: good, suspicious, bad, unknown|good|
  
**threats**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Status|string|None|False|Health status of an endpoint or a service running on an endpoint. The following values are allowed: good, suspicious, bad, unknown|good|
  
**health**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Overall|string|None|False|Health status of an endpoint or a service running on an endpoint. The following values are allowed: good, suspicious, bad, unknown|good|
|Services|services|None|False|Status of services on the endpoint|{}|
|Threats|threats|None|False|Threats on the endpoint|{}|
  
**endpointObject**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Hostname|string|None|False|Endpoint hostname|example-hostname|
|ID|string|None|False|Unique endpoint ID|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
  
**endpoints**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Items|[]endpointObject|None|False|List of endpoints belonging to the group|[]|
|Items Count|integer|None|False|Total number of items in the list|5|
|Total|integer|None|False|Total number of endpoints in this group|10|
  
**endpointGroup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created At|string|None|False|When the group was created|2023-03-02 13:00:19.494000+00:00|
|Description|string|None|False|Endpoint group description|Example description|
|Endpoints|endpoints|None|False|Associated endpoints|{}|
|ID|string|None|False|Endpoint group ID|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Name|string|None|False|Endpoint group name|Example Group|
|Tenant|objectId|None|False|Reference to a tenant|{}|
|Type|string|None|False|Endpoint group type|computer|
|Updated At|string|None|False|When the group was last updated|2023-03-02 13:00:19.494000+00:00|
  
**isolation**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Comment|string|None|False|Reason endpoint should be isolated or not|Example Comment|
|Enabled|boolean|None|False|Whether the endpoint should be isolated or not|True|
|Last Disabled At|string|None|False|When isolation was last disabled for the endpoint|2023-03-02 13:00:19.494000+00:00|
|Last Disabled By|user|None|False|Last disabled by|{}|
|Last Enabled At|string|None|False|When isolation was last enabled for the endpoint|2023-03-02 13:00:19.494000+00:00|
|Last Enabled By|user|None|False|Last enabled by|{}|
  
**endpointIsolation**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Endpoint ID|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Isolation|isolation|None|False|Isolation state of an endpoint|{}|
  
**endpointRemovalErrors**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Endpoints Not Found|[]string|None|False|Endpoints not found|["9de5069c-5afe-602b-2ea0-a04b66beb2c0"]|
  
**endpointsItem**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assigned Products|[]assignedProduct|None|False|Products assigned to the endpoint|[]|
|Associated Person|associatedPerson|None|False|Person associated with an endpoint|{}|
|Cloud|cloud|None|False|Endpoint cloud|{}|
|Encryption|encryption|None|False|Endpoint encryption state|{}|
|Group|group|None|False|Endpoint group|{}|
|Health|health|None|False|Endpoint health status|{}|
|Hostname|string|None|False|Hostname of the endpoint|example-hostname|
|ID|string|None|False|Unique ID of the endpoint|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|IPv4 Addresses|[]string|None|False|List of IPv4 addresses|["198.51.100.1"]|
|IPv6 Addresses|[]string|None|False|List of IPv6 addresses|["198.51.100.1"]|
|Isolation|isolationState|None|False|Endpoint isolation state as reported by an endpoint|{}|
|Last Seen At|string|None|False|Date and time (UTC) when the endpoint last communicated with Sophos Central|2023-03-02 13:00:19.494000+00:00|
|Lockdown|lockdown|None|False|Server lockdown status|{}|
|MAC Addresses|[]string|None|False|List of MAC addresses|["00-B0-D0-63-C2-26"]|
|Online|boolean|None|False|Whether endpoint is currently online|False|
|OS|osObject|None|False|OS information|{}|
|Tamper Protection Enabled|boolean|None|False|Whether Tamper Protection is turned on|False|
|Tenant|objectId|None|False|Represents a referenced object|{}|
|Type|string|None|False|Endpoint type. The following values are allowed: computer, server, securityVm|computer|
  
**pagesDetails**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|From Key|string|None|False|The key of the first item in the returned page|exampleKey|
|Items|integer|None|False|The total number of items across all pages, if pageTotal=true was passed into the request|1|
|Max Size|integer|None|False|The maximum page size that can be requested|100|
|Next Key|string|None|False|The key to use when fetching the next page|exampleKey|
|Size|integer|None|False|The size of the page being returned|50|
|Total|integer|None|False|The total number of pages that exist, if pageTotal=true in the request|1|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 4.4.1 - Bumping requirements.txt | SDK bump to 6.2.0
* 4.4.0 - Add new actions: `Isolate Endpoint`, `Get Endpoint Groups`, `Add Endpoint Group`, `Get Endpoint Group`, `Add Endpoint to Group`, `Remove Endpoint from Group`, `Get Allowed Items`, `Add Allowed Item`, `Remove Allowed Item`, `Get Blocked Items`, `Add Blocked Item`, `Remove Blocked Item`, `Get Endpoints in Group` | `Check Tamper Protection Status`, `Antivirus Scan`: fix issue with handling pagination in retrieving endpoint id
* 4.3.1 - Add custom User-Agent string to API calls to identify API request
* 4.3.0 - Add new action Check Tamper Protection Status
* 4.2.0 - Add new action Get Agent Details
* 4.1.0 - Add new action Antivirus Scan
* 4.0.0 - Add new action Blacklist | Update 'API region' title in connection to 'API Region'
* 3.0.0 - Rewrite Sophos Central in Python 3
* 2.0.0 - Update type for Invalidated to date
* 1.0.3 - New spec and help.md format for the Extension Library
* 1.0.2 - Regenerate with latest Go SDK to solve bug with triggers
* 1.0.0 - Support web server mode | Update to new credential types | Rename 'Download hashes' action to 'Download Hashes' | Rename 'Get endpoints' action to 'Get Endpoints' | Rename 'Get alerts' action to 'Get Alerts' | Rename 'Get SIEM events' action to 'Get SIEM Events'
* 0.1.0 - Initial plugin

# Links

* [Sophos Central](https://www.sophos.com)

## References

* [Sophos Central APIs](https://developer.sophos.com/apis)