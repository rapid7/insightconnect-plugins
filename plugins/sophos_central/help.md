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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|client_id|credential_secret_key|None|True|Client ID for Sophos Central instance|None|8a9jbad0-12ab-88be-cad4-3b4cad6f78e0|
|client_secret|credential_secret_key|None|True|Client secret key that allows access to Sophos Central|None|a1e263620c12382b36054cf34512ef836854e61d27ab2d079dda27af903a5b6eec396416b2dc40aabce6edfg670b0790d9a90|
|region|string|US East|False|API region|['US West', 'US East', 'EU Ireland', 'DE Germany']|US East|
|tenant_id|credential_secret_key|None|False|Tenant ID for Sophos Central instance|None|5b0eba20-ab12-34cd-88be-3a4cdc6a70f8|

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

#### Get Endpoints in Group

This action endpoints in your specified group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fields|[]string|None|False|The fields to return in a partial response. All fields are returned by default|None|["id", "type"]|
|groupId|string|None|True|Endpoint group ID|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|pageFromKey|string|None|False|The key of the item from where to fetch a page|None|exampleKey|
|pageSize|integer|50|False|The size of the page requested. Value must be inclusively between 1 and 1000|None|50|
|pageTotal|boolean|False|False|Whether the number of pages should be calculated and returned in the response|None|False|
|search|string|None|False|Term to search for in the specified search fields|None|example|
|searchFields|[]string|None|False|List of search fields for finding the given search term. The following values are allowed: "hostname", "groupName", "associatedPersonName", "ipAddresses", "osName"|None|["hostname", "groupName", "associatedPersonName", "ipAddresses", "osName"]|
|sort|[]string|None|False|Defines how to sort the data. Matches (^[^:]+$)|(^[^:]+:(asc|desc)$)|None|["id:asc"]|

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
|----|----|--------|-----------|-------|
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

#### Remove Endpoint from Group

This action is used to remove endpoints from a group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|groupId|string|None|True|Endpoint group ID|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|ids|[]string|None|True|List of endpoint IDs|None|["9de5069c-5afe-602b-2ea0-a04b66beb2c0"]|

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
|----|----|--------|-----------|-------|
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

#### Isolate Endpoint

This action is used to turn on or off endpoint isolation for multiple endpoints.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|False|Reason the endpoints should be isolated or not|None|Example comment|
|enabled|boolean|True|True|Whether the endpoints should be isolated or not|None|True|
|ids|[]string|None|True|List of endpoints IDs|None|["9de5069c-5afe-602b-2ea0-a04b66beb2c0"]|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|endpoints|[]endpointIsolation|False|List of endpoints for which isolation has been updated|

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

#### Get Endpoint Group

This action is used to get endpoint group by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|groupId|string|None|True|Endpoint group ID|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|

Example input:

```
{
  "groupId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
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

#### Add Endpoint to Group

This action is used to add endpoints to your group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|groupId|string|None|True|Endpoint group ID|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|ids|[]string|None|True|List of endpoint IDs|None|["9de5069c-5afe-602b-2ea0-a04b66beb2c0"]|

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
|----|----|--------|-----------|-------|
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

#### Add Endpoint Group

This action is used to add a new endpoint group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|description|string|None|False|Group description|None|Example description|
|endpointIds|[]string|None|False|List of endpoint IDs that will be added to the group|None|["9de5069c-5afe-602b-2ea0-a04b66beb2c0"]|
|name|string|None|True|Endpoint group name|None|Example Group|
|type|string|computer|True|Group type|['computer', 'server']|computer|

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
|----|----|--------|-----------|-------|
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

#### Check Tamper Protection Status

This action is used to get tamper status by IP address, Hostname, MAC address or Device ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Device ID, IPv4 address, IPv6 address, MAC address or hostname|None|198.51.100.100|

Example input:

```
{
  "agent": "198.51.100.100"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|tamper_status|check_tamper_protection_status|True|Tamper status for provided agent|

Example output:

```
{
  "tamper_status": {
    "enabled": true
  }
}
```

#### Blacklist

This action blocks a hash across all systems.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|blacklist_state|boolean|None|True|Set true to blacklist hash, set false to unblacklist hash|None|True|
|description|string|Hash Blacklisted from InsightConnect|False|Description for why the hash is blacklisted|None|Hash Blacklisted from InsightConnect|
|hash|string|None|True|Create a blacklist item from a SHA256 hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|

Example input:

```
{
  "blacklist_state": true,
  "description": "Hash Blacklisted from InsightConnect",
  "hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Return true if blacklist item was created or deleted|

Example output:

```
{
  "success": true
}
```

#### Get Agent Details

This action is used to get details for an agent.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Agent to retrieve device information from. Accepts IPv4 address, IPv6 address, MAC address, hostname, or device ID|None|198.51.100.100|

Example input:

```
{
  "agent": "198.51.100.100"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agent|endpoint_entry|True|Details for the matched agent|

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
```

#### Antivirus Scan

This action sends a request to the specified endpoint to perform or configure a scan.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Agent ID, IPv4 address, IPv6 address, MAC address or hostname|None|198.51.100.100|

Example input:

```
{
  "agent": "198.51.100.100"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|True|Antivirus scan ID|
|requested_at|string|True|Antivirus scan requested at|
|status|string|True|Antivirus scan status|

Example output:

```
{
  "id": "999fd666-9666-4e66-a066-d66fd966ad66",
  "requested_at": "2020-08-02T21:30:55.487Z",
  "status": "requested"
}
```

#### Get Alerts

This action is used to get alerts for a customer based on the parameters provided.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|from_date|string|None|False|The starting date from which alerts will be retrieved defined as Unix timestamp in UTC. Must be within last 24 hours|None|2019-09-23 12:02:01.700000|

Example input:

```
{
  "from_date": "2019-09-23T12:02:01.700Z"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alerts|[]alert_entity|True|Alerts for specified time period|

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

#### Get Endpoints

This action is used to get endpoints for a customer based on the parameters provided.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|since|string|None|False|Last seen after date and time (UTC) or duration inclusive, eg. 2019-09-23T12:02:01.700Z, -P1D, PT20M, PT4H500S|None|2019-09-23T12:02:01.700Z|

Example input:

```
{
  "since": "2019-09-23T12:02:01.700Z"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|items|[]endpoint_entry|True|Endpoint items|

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

#### Add Blocked Item

This action is used to block an item from exoneration.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|True|Comment indicating why the item should be blocked|None|Example comment|
|propertiesCertificateSigner|string|None|False|Properties value saved for the certificateSigner|None|Example signer|
|propertiesFileName|string|None|False|Properties file name for the application|None|sample.txt|
|propertiesPath|string|None|False|Properties path for the application|None|$path/sample.txt|
|propertiesSha256|string|None|True|Properties SHA256 value for the application|None|ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad|
|type|string|sha256|True|Property by which an item is blocked. The following values are allowed: SHA256|None|sha256|

Example input:

```
{
  "comment": "This is comment",
  "propertiesCertificateSigner": "Example signer",
  "propertiesFileName": "sample.txt",
  "propertiesPath": "$path/sample.txt",
  "propertiesSha256": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
  "type": "sha256"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
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

#### Get Blocked Items

This action is used to get a list of blocked items.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|page|integer|1|False|The page number to fetch, starting with 1|None|1|
|pageSize|integer|50|False|The size of the page requested|None|50|
|pageTotal|boolean|False|False|Whether the number of pages should be calculated and returned in the response|None|False|

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
|----|----|--------|-----------|-------|
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

#### Remove Blocked Item

This action deletes the specified blocked item.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|blockedItemId|string|None|True|The identifier of the blocked item|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|

Example input:

```
{
  "blockedItemId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|False|Whether the item was deleted. Returns success if can't find item or it has been successfully deleted|True|

Example output:

```
{
  "success": true
}
```


#### Remove Allowed Item

This action deletes the specified allowed item.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|allowedItemId|string|None|True|The identifier of the allowed item|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|

Example input:

```
{
  "allowedItemId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Whether the action was successful|

Example output:

```
{
  "success": true
}
```

#### Get Endpoint Groups

This action is used to get endpoint groups.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|endpointIds|[]string|None|False|Endpoint IDs. Must contain at most 50 items that must be unique|None|["9de5069c-5afe-602b-2ea0-a04b66beb2c0"]|
|fields|[]string|None|False|The fields to return in a partial response|None|["name", "createdAt"]|
|groupType|string|all|False|Endpoint group type. The following values are allowed: all, computer, server|['all', 'computer', 'server']|computer|
|ids|[]string|None|False|Endpoint group IDs to match. Must contain at most 50 items that must be unique|None|["9de5069c-5afe-602b-2ea0-a04b66beb2c0"]|
|page|integer|1|False|The page number to fetch|None|5|
|pageSize|integer|50|False|The size of the page requested|None|10|
|pageTotal|boolean|None|False|Whether the number of pages should be calculated and returned in the response|None|False|
|search|string|None|False|Term to search for in the specified search fields|None|Example|
|searchFields|[]string|None|False|Search your specified fields. The default is to search group names only. The following values are allowed: name, description|None|["description", "name"]|
|sort|[]string|None|False|Sort criteria for endpoint groups. Valid sort fields are id, name, createdAt, and updatedAt. You can append ':asc' or ':desc' to each field to specify the sort direction. The default sort direction for each field is unspecified|None|["createdAt:desc", "name:asc"]|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|endpointGroups|[]endpointGroup|False|List of endpoint groups|
|pages|pages|False|Pages details|

Example output:

```
{
  "endpointGroups":[
    {
      "id":"f8d03561-90d1-4c18-b576-34509e843ee1",
      "name":"Example Group",
      "description":"Example description",
      "type":"computer",
      "endpoints":{
        "total":1,
        "itemsCount":1,
        "items":[
          {
            "id":"f8d03561-90d1-4c18-b576-34509e843ee8",
            "hostname":"EXAMPLE-HOSTNAME"
          }
        ]
      },
      "tenant":{
        "id":"f8d03561-90d1-4c18-b576-34509e843ee8"
      },
      "createdAt":"2023-01-01T11:11:11.111Z",
      "updatedAt":"2023-01-01T11:11:11.111Z"
    },
    {
      "id":"f8d03561-90d1-4c18-b576-34509e843ee3",
      "name":"Test Group 3",
      "description":"Example description",
      "type":"computer",
      "endpoints":{
        "total":0,
        "itemsCount":0,
        "items":[
        ]
      },
      "tenant":{
        "id":"f8d03561-90d1-4c18-b576-34509e843ee8"
      },
      "createdAt":"2023-01-01T11:11:11.111Z"
    }
  ],
  "pages":{
    "current":1,
    "size":50,
    "maxSize":1000
  }
```

#### Get Allowed Items

This action is used to get a list of allowed items.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|page|integer|1|False|The page number to fetch|None|3|
|pageSize|integer|50|False|The size of the page requested|None|5|
|pageTotal|boolean|None|False|Whether the number of pages should be calculated and returned in the response|None|False|

Example input:

```
{
  "page": 3,
  "pageSize": 5,
  "pageTotal": false
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|items|[]item|False|List of allowed items|
|pages|pages|False|Pages details|

Example output:

```
{
  "items":[
    {
      "id":"f8d03561-90d1-4c18-b576-34509e843ee1",
      "createdAt":"2023-01-01T11:11:11.111Z",
      "updatedAt":"2023-01-01T11:11:11.111Z",
      "properties":{
        "path":"$path/sample.txt"
      },
      "comment":"Test comment",
      "type":"path"
    },
    {
      "id":"f8d03561-90d1-4c18-b576-34509e843ee2",
      "createdAt":"2023-01-01T11:11:11.111Z",
      "updatedAt":"2023-01-01T11:11:11.111Z",
      "properties":{
        "sha256":"ba7816bf8f01cfea414140de5dae2223b10361a396177a9cb410ff61f20015af"
      },
      "comment":"Test comment",
      "type":"sha256"
    },
    {
      "id":"f8d03561-90d1-4c18-b576-34509e843ee3",
      "createdAt":"2023-01-01T11:11:11.111Z",
      "updatedAt":"2023-01-01T11:11:11.111Z",
      "properties":{
        "certificateSigner":"Example signer"
      },
      "comment":"Test comment",
      "type":"certificateSigner"
    }
  ],
  "pages":{
    "current":1,
    "size":3,
    "maxSize":100
  }
}
```

#### Add Allowed Item

This action is used to exempt an item from conviction.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|True|Comment indicating why the item should be allowed|None|Example comment|
|originEndpointId|string|None|False|Endpoint where the item to be allowed was last seen|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|originPersonId|string|None|False|Person associated with the endpoint where the item to be allowed was last seen|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|propertiesCertificateSigner|string|None|False|Properties value saved for the certificateSigner. Required if 'certificateSigner' is selected in the Type input|None|Example signer|
|propertiesFileName|string|None|False|Properties file name for the application|None|sample.txt|
|propertiesPath|string|None|False|Properties path for the application. Required if 'path' is selected in the Type input|None|$path/sample.txt|
|propertiesSha256|string|None|False|Properties SHA256 value for the application. Required if 'SHA256' is selected in the Type input|None|ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad|
|type|string|None|True|Property by which an item is allowed. You need to fill in the input starting with 'properties' for the selected type|['sha256', 'path', 'certificateSigner']|sha256|

Example input:

```
{
  "comment": "Example comment",
  "originEndpointId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
  "originPersonId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
  "propertiesCertificateSigner": "Example signer",
  "propertiesFileName": "sample.txt",
  "propertiesPath": "/sample.txt",
  "propertiesSha256": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
  "type": "sha256"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|allowedItem|item|False|Allowed item created|

Example output:

```
{
  "allowedItem":{
    "id":"714083d8-18eb-4f7d-b552-8ccd93e4e560",
    "createdAt":"2023-01-01T11:11:11.111Z",
    "updatedAt":"2023-01-01T11:11:11.111Z",
    "properties":{
      "sha256":"050c194cbbb"
    },
    "comment":"Test comment",
    "type":"sha256",
      "originEndpointId": {
        "id": "fde30644-050f-486d-a54e-06210b892dff"
      }
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### alert_entity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created At|string|False|The date at which the alert was created|
|Customer Id|string|False|The unique identifier of the customer linked with this record|
|Data|object|False|None|
|Description|string|False|The description of the alert that was generated|
|Event Service Event Id|string|False|The Event Services event id|
|Id|string|False|Identifier for the alert|
|Location|string|False|The location captured for this record|
|Severity|string|False|The severity for this alert|
|Source|string|False|Describes the source from alert was generated|
|Threat|string|False|The name of the threat responsible for the generation of alert|
|Threat Cleanable|boolean|False|None|
|Type|string|False|Describes the type of the device on which alert was generated|
|When|string|False|The date at which the alert was created|

#### assignedProduct

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Code|string|False|Endpoint product. The following values are allowed: coreAgent, interceptX, xdr, endpointProtection, deviceEncryption, mtr, ztna|
|Status|string|False|Installation status of a product assigned to the endpoint. The following values are allowed: installed, notInstalled|
|Version|string|False|Version of a product assigned to an endpoint|

#### assigned_product

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Code|string|False|None|
|Status|string|False|None|
|Version|string|False|None|

#### associatedPerson

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Unique ID for the Person|
|Name|string|False|Person's name|
|Via Login|string|False|Person's login on the endpoint|

#### check_tamper_protection_status

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Enabled|boolean|True|Return true when tamper protection is enable|

#### chronology

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Zone|date_time_zone|False|None|

#### cloud

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Instance ID|string|False|Unique ID for the cloud instance|
|Provider|string|False|Cloud provider in which the endpoint is running. The following values are allowed: aws, azure|

#### core_remedy_item

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Descriptor|string|False|None|
|Result|string|False|None|
|Type|string|False|None|

#### core_remedy_items

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Items|[]core_remedy_item|False|None|
|TotalItems|integer|False|None|

#### current_licenses_response

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Licenses|[]customer_license|False|None|

#### customer_feature

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ExpirationProcessed|boolean|False|None|
|Expired|boolean|False|None|
|ExpiresOn|date_time|False|None|
|FeatureCode|string|False|None|
|GeneratedFromLicenseId|string|False|None|
|LicenseCode|string|False|None|
|Protection|boolean|False|None|
|Valid|boolean|False|None|

#### customer_featuresResponse

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Features|[]customer_feature|False|None|

#### customer_license

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Expired|boolean|False|None|
|Expires On|date_time|False|None|
|Id|object_id|False|None|
|License Code|string|False|None|
|License Id|string|False|None|
|License Type|string|False|None|
|Quota|integer|False|None|
|Starts On|date_time|False|None|
|Suspended|boolean|False|None|

#### date_time

|Name|Type|Required|Description|
|----|----|--------|-----------|
|AfterNow|boolean|False|None|
|BeforeNow|boolean|False|None|
|CenturyOfEra|integer|False|None|
|Chronology|chronology|False|None|
|DayOfMonth|integer|False|None|
|DayOfWeek|integer|False|None|
|DayOfYear|integer|False|None|
|EqualNow|boolean|False|None|
|Era|integer|False|None|
|HourOfDay|integer|False|None|
|Millis|integer|False|None|
|MillisOfDay|integer|False|None|
|MillisOfSecond|integer|False|None|
|MinuteOfDay|integer|False|None|
|MinuteOfHour|integer|False|None|
|MonthOfYear|integer|False|None|
|SecondOfDay|integer|False|None|
|SecondOfMinute|integer|False|None|
|WeekOfWeekyear|integer|False|None|
|Weekyear|integer|False|None|
|Year|integer|False|None|
|YearOfCentury|integer|False|None|
|YearOfEra|integer|False|None|
|Zone|date_time_zone|False|None|

#### date_time_zone

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Fixed|boolean|False|None|
|Id|string|False|None|

#### encryption

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Volumes|[]volume|False|Endpoint volumes|

#### endpointGroup

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created At|string|False|When the group was created|
|Description|string|False|Endpoint group description|
|Endpoints|endpoints|False|Associated endpoints|
|ID|string|False|Endpoint group ID|
|Name|string|False|Endpoint group name|
|Tenant|objectId|False|Reference to a tenant|
|Type|string|False|Endpoint group type|
|Updated At|string|False|When the group was last updated|

#### endpointIsolation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Endpoint ID|
|Isolation|isolation|False|Isolation state of an endpoint|

#### endpointObject

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Hostname|string|False|Endpoint hostname|
|ID|string|False|Unique endpoint ID|

#### endpointRemovalErrors

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Endpoints Not Found|[]string|False|Endpoints not found|

#### endpoint_entry

|Name|Type|Required|Description|
|----|----|--------|-----------|
|AdSyncInfo|object|False|None|
|Alert Status|integer|False|None|
|AssignedProducts|[]assigned_product|False|None|
|AwsInfo|object|False|None|
|AzureInfo|object|False|None|
|Beta|boolean|False|None|
|Decloned From|string|False|None|
|Deleted At|string|False|None|
|Device Encryption Status Unmanaged|boolean|False|None|
|Early Access Program|string|False|None|
|Endpoint Type|string|False|None|
|Group Full Name|string|False|None|
|Group Id|string|False|None|
|Group Name|string|False|None|
|Health Status|integer|False|None|
|Heartbeat Utm Name|string|False|None|
|Id|string|False|None|
|Info|object|False|None|
|Is Adsync Group|boolean|False|None|
|Java Id|string|False|None|
|Last Activity|string|False|None|
|Last User|string|False|None|
|Last User Id|string|False|None|
|License Codes|[]string|False|None|
|Machine Id|string|False|None|
|Name|string|False|None|
|Registered At|string|False|None|
|Status|object|False|None|
|Tamper Protection|tamper_protection_entity|False|None|
|Transport|string|False|None|

#### endpoint_whitelist_properties

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Property|string|False|None|
|Type|string|False|None|

#### endpoints

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Items|[]endpointObject|False|List of endpoints belonging to the group|
|Items Count|integer|False|Total number of items in the list|
|Total|integer|False|Total number of endpoints in this group|

#### endpointsItem

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Assigned Products|[]assignedProduct|False|Products assigned to the endpoint|
|Associated Person|associatedPerson|False|Person associated with an endpoint|
|Cloud|cloud|False|Endpoint cloud|
|Encryption|encryption|False|Endpoint encryption state|
|Group|group|False|Endpoint group|
|Health|health|False|Endpoint health status|
|Hostname|string|False|Hostname of the endpoint|
|ID|string|False|Unique ID of the endpoint|
|IPv4 Addresses|[]string|False|List of IPv4 addresses|
|IPv6 Addresses|[]string|False|List of IPv6 addresses|
|Isolation|isolationState|False|Endpoint isolation state as reported by an endpoint|
|Last Seen At|string|False|Date and time (UTC) when the endpoint last communicated with Sophos Central|
|Lockdown|lockdown|False|Server lockdown status|
|MAC Addresses|[]string|False|List of MAC addresses|
|Online|boolean|False|Whether endpoint is currently online|
|OS|osObject|False|OS information|
|Tamper Protection Enabled|boolean|False|Whether Tamper Protection is turned on|
|Tenant|objectId|False|Represents a referenced object|
|Type|string|False|Endpoint type. The following values are allowed: computer, server, securityVm|

#### event_aggregate

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Has More|boolean|False|None|
|Items|[]legacy_event_entity|False|None|
|Next Cursor|string|False|Value of the next cursor. This will be used to make next call of API|

#### group

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Unique ID for endpoint group|
|Name|string|False|Endpoint group name|

#### hashes_response

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Hashes|object|False|None|

#### health

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Overall|string|False|Health status of an endpoint or a service running on an endpoint. The following values are allowed: good, suspicious, bad, unknown|
|Services|services|False|Status of services on the endpoint|
|Threats|threats|False|Threats on the endpoint|

#### installer_info

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Beta|boolean|False|None|
|Command|string|False|None|
|Platform|string|False|None|
|ProductName|string|False|None|
|Url|string|False|None|

#### installer_info_response

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Installer Info|[]installer_info|False|None|

#### isolation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Comment|string|False|Reason endpoint should be isolated or not|
|Enabled|boolean|False|Whether the endpoint should be isolated or not|
|Last Disabled At|string|False|When isolation was last disabled for the endpoint|
|Last Disabled By|user|False|Last disabled by|
|Last Enabled At|string|False|When isolation was last enabled for the endpoint|
|Last Enabled By|user|False|Last enabled by|

#### isolationState

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Admin Isolated|boolean|False|Whether isolation was triggered by an admin|
|Self Isolated|boolean|False|Whether isolation was triggered by the endpoint itself|
|Status|string|False|Isolation status reported by endpoint. The following values are allowed: isolated, notIsolated|

#### item

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Comment|string|False|Comment indicating why the item was blocked or allowed|
|Created At|string|False|Date and time (UTC) when the item was created|
|Created By|userObject|False|Created by|
|ID|string|False|Item ID|
|Origin Endpoint|objectId|False|Represents a referenced object|
|Origin Person|userObject|False|Origin person|
|Properties|properties|False|Item properties|
|Type|string|False|Property by which an item is blocked or allowed|
|Updated At|string|False|Date and time (UTC) when the item was updated|

#### legacy_event_entity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Core Remedy Items|core_remedy_items|False|details of the items cleaned or restored|
|Created At|string|False|The date at which the event was created|
|Customer Id|string|False|The identifier of the customer for which record is created|
|Endpoint Id|string|False|The corresponding endpoint id associated with the record|
|Endpoint Type|string|False|The corresponding endpoint type associated with the record|
|Group|string|False|The group associated with the group|
|Id|string|False|The Identifier for the event|
|Location|string|False|The location captured for this record|
|Name|string|False|The name of the record created|
|Origin|string|False|originating component of a detection|
|Severity|string|False|The severity for this alert|
|Source|string|False|The source for this record|
|Threat|string|False|The threat associated with the record|
|Type|string|False|The type of this record|
|User Id|string|False|The identifier of the user for which record is created|
|When|string|False|The date at which the event was created|
|Whitelist Properties|[]endpoint_whitelist_properties|False|The properties by which this event can be whitelisted on an endpoint, if applicable|

#### lockdown

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Status|string|False|Endpoint lockdown status. The following values are allowed: creatingWhitelist, installing, locked, notInstalled, registering, starting, stopping, unavailable, uninstalled, unlocked|
|Update Status|string|False|Endpoint lockdown update status. The following values are allowed: upToDate, updating, rebootRequired, notInstalled|

#### objectId

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|The ID of the referenced object|

#### object_id

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Counter|integer|False|None|
|Date|string|False|None|
|MachineIdentifier|integer|False|None|
|ProcessIdentifier|integer|False|None|
|Time|integer|False|None|
|TimeSecond|integer|False|None|
|Timestamp|integer|False|None|

#### osObject

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Build|integer|False|OS build|
|Is Server|boolean|False|Whether the OS is a server OS|
|Major Version|integer|False|OS major version|
|Minor Version|integer|False|OS minor version|
|Name|string|False|OS name as reported by the endpoint|
|Platform|string|False|OS platform type. The following values are allowed: windows, linux, macOS|

#### pages

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Current|integer|False|The 1-based page number being returned|
|Items|integer|False|The total number of items across all pages, if pageTotal=true was passed into the request|
|Max Size|integer|False|The maximum page size that can be requested|
|Size|integer|False|The size of the page being returned|
|Total|integer|False|The total number of pages that exist, if pageTotal=true in the request|

#### pagesDetails

|Name|Type|Required|Description|
|----|----|--------|-----------|
|From Key|string|False|The key of the first item in the returned page|
|Items|integer|False|The total number of items across all pages, if pageTotal=true was passed into the request|
|Max Size|integer|False|The maximum page size that can be requested|
|Next Key|string|False|The key to use when fetching the next page|
|Size|integer|False|The size of the page being returned|
|Total|integer|False|The total number of pages that exist, if pageTotal=true in the request|

#### previous_password_entity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Invalidated|date|False|None|
|Password|string|False|None|

#### properties

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Certificate Signer|string|False|Value saved for the certificateSigner|
|File Name|string|False|File name|
|Path|string|False|Path for the application|
|SHA256|string|False|SHA256 value for the application|

#### serviceDetails

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Name|string|False|Service name|
|Status|string|False|Status of a service on an endpoint. The following values are allowed: running, stopped, missing|

#### services

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Service Details|[]serviceDetails|False|Details of services on the endpoint|
|Status|string|False|Health status of an endpoint or a service running on an endpoint. The following values are allowed: good, suspicious, bad, unknown|

#### tamper_protection_entity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Enabled|boolean|False|None|
|Globally Enabled|boolean|False|None|
|Password|string|False|None|
|Previous Passwords|[]previous_password_entity|False|None|

#### threats

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Status|string|False|Health status of an endpoint or a service running on an endpoint. The following values are allowed: good, suspicious, bad, unknown|

#### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Account ID|string|False|ID of the account|
|Account Type|string|False|Type of the account|
|ID|string|False|Principal email or client ID|
|Name|string|False|User principal name|
|Type|string|False|Principal type|

#### userObject

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Unique ID for the user|
|Name|string|False|Person's name|

#### volume

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Status|string|False|Endpoint volume encryption status. The following values are allowed: notEncrypted, encrypted, encrypting, notSupported, suspended, unknown|
|Volume ID|string|False|Endpoint volume ID|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 4.4.0 - Add new actions: `Isolate Endpoint`, `Get Endpoint Groups`, `Add Endpoint Group`, `Get Endpoint Group`, `Add Endpoint to Group`, `Remove Endpoint from Group`, `Get Allowed Items`, `Add Allowed Item`, `Remove Allowed Item`, `Get Blocked Items`, `Add Blocked Item`, `Remove Blocked Item`, `Get Endpoints in Group`
* 4.3.1 - Add custom User-Agent string to API calls to identify API request
* 4.3.0 - Add new action Check Tamper Protection Status
* 4.2.0 - Add new action Get Agent Details
* 4.1.0 - Add new action Antivirus Scan
* 4.0.0 - Add new action Blacklist | Update "API region" title in connection to "API Region"
* 3.0.0 - Rewrite Sophos Central in Python 3
* 2.0.0 - Update type for Invalidated to date
* 1.0.3 - New spec and help.md format for the Extension Library
* 1.0.2 - Regenerate with latest Go SDK to solve bug with triggers
* 1.0.0 - Support web server mode | Update to new credential types | Rename "Download hashes" action to "Download Hashes" | Rename "Get endpoints" action to "Get Endpoints" | Rename "Get alerts" action to "Get Alerts" | Rename "Get SIEM events" action to "Get SIEM Events"
* 0.1.0 - Initial plugin

# Links

* [Sophos Central](https://www.sophos.com)

## References

* [Sophos Central](https://www.sophos.com)
