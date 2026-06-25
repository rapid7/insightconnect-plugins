# Description

Zscaler is a SaaS security platform that provides fast, secure connections between client applications, regardless of device, location, or network

# Key Features

* Lookup categories for a given URL
* Blacklist or unblacklist URLs
* Create user
* Delete user
* Get users
* Get URL category by name
* Update URLs of URL category
* Manage DLP incidents
* Manage firewall rules
* Retrieve web and firewall logs
* Submit threat feed IoCs
* Manage ZPA application segments and server groups

# Requirements

* Requires a Zscaler OneAPI OAuth 2.0 Client ID from ZIdentity
* Requires a PEM private key for JWT signing (RS256)
* Requires the customer vanity domain (e.g., mycompany)

# Supported Product Versions

* Zscaler OneAPI 2024

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|client_id|string|None|True|OAuth Client ID from ZIdentity|None|abc123-client-id|None|None|
|cloud|string|zsapi.net|False|Zscaler cloud domain|None|zsapi.net|None|None|
|private_key|credential_asymmetric_key|None|True|PEM private key for JWT signing (RS256)|None|{"privateKey": "-----BEGIN RSA PRIVATE KEY-----..."}|None|None|
|vanity_domain|string|None|True|Customer vanity domain (e.g., mycompany)|None|mycompany|None|None|

Example input:

```
{
  "client_id": "abc123-client-id",
  "cloud": "zsapi.net",
  "private_key": {
    "privateKey": "-----BEGIN RSA PRIVATE KEY-----..."
  },
  "vanity_domain": "mycompany"
}
```

## Technical Details

### Actions


#### Blacklist URL

This action is used to add or remove URLs from a blacklist. These URLs will appear in the 'Blocked Malicious URLs' 
section on the Advanced Threats Policy page

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|activate_configuration|boolean|False|True|Set to true to activate configuration changes|None|False|None|None|
|blacklist_state|boolean|True|False|True to blacklist a URL, false to unblacklist a URL|None|True|None|None|
|urls|[]string|None|True|A given set of one or more URLs or domains to update in the blacklist|None|["www.example.com", "http://rapid7.com"]|None|None|
  
Example input:

```
{
  "activate_configuration": false,
  "blacklist_state": true,
  "urls": [
    "www.example.com",
    "http://rapid7.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|string|True|Activation status for a configuration change|ACTIVE|
|success|boolean|True|Whether or not the request succeeded|True|
  
Example output:

```
{
  "status": "ACTIVE",
  "success": true
}
```

#### Create Firewall Rule

This action is used to create a new firewall filtering rule

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|rule_data|object|None|True|The firewall rule configuration object containing rule properties such as name, state, action, and conditions|None|{'name': 'Block Malware', 'state': 'ENABLED', 'action': 'BLOCK_RESET', 'order': 1}|None|None|
  
Example input:

```
{
  "rule_data": {
    "action": "BLOCK_RESET",
    "name": "Block Malware",
    "order": 1,
    "state": "ENABLED"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|rule|firewallRule|False|The created firewall filtering rule|{'id': 12345, 'name': 'Block Malware', 'state': 'ENABLED', 'action': 'BLOCK_RESET', 'order': 1}|
  
Example output:

```
{
  "rule": {
    "action": "BLOCK_RESET",
    "id": 12345,
    "name": "Block Malware",
    "order": 1,
    "state": "ENABLED"
  }
}
```

#### Create User

This action is used to adds a new user. A user can belong to multiple groups, but can only belong to one department

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comments|string|None|False|Additional information about this user|None|Example comment|None|None|
|departmentName|string|None|True|Department a user belongs to|None|Department Name|None|None|
|email|string|None|True|User email consists of a user name and domain name. It does not have to be a valid email address, but it must be unique and its domain must belong to the organization|None|user@example.com|None|None|
|groupNames|[]string|None|True|List of groups a user belongs to|None|["Group Name"]|None|None|
|name|string|None|True|User name|None|John|None|None|
|password|password|None|True|User's password. Applicable only when authentication type is Hosted DB. Password strength must follow what is defined in the auth settings|None|password12!|None|None|
|tempAuthEmail|string|None|False|If you enabled one-time tokens or links, enter the email address to which the Zscaler service sends the tokens or links. If this is empty, the service sends the email to the User email|None|user@example.com|None|None|
  
Example input:

```
{
  "comments": "Example comment",
  "departmentName": "Department Name",
  "email": "user@example.com",
  "groupNames": [
    "Group Name"
  ],
  "name": "John",
  "password": "password12!",
  "tempAuthEmail": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|user|False|An organization user|{'id': 123456789, 'name': 'Sample user', 'email': 'user@example.com', 'groups': [{'id': 123456789, 'name': 'Test Group', 'idpId': 123456789, 'comments': 'Sample comment'}], 'department': {'id': 123456789, 'name': 'Test Department', 'idpId': 123456789, 'comments': 'Sample comment', 'deleted': False}, 'comments': 'Sample comment', 'tempAuthEmail': 'user@example.com', 'adminUser': False}|
  
Example output:

```
{
  "user": {
    "adminUser": false,
    "comments": "Sample comment",
    "department": {
      "comments": "Sample comment",
      "deleted": false,
      "id": 123456789,
      "idpId": 123456789,
      "name": "Test Department"
    },
    "email": "user@example.com",
    "groups": [
      {
        "comments": "Sample comment",
        "id": 123456789,
        "idpId": 123456789,
        "name": "Test Group"
      }
    ],
    "id": 123456789,
    "name": "Sample user",
    "tempAuthEmail": "user@example.com"
  }
}
```

#### Delete User

This action is used to deletes the user for the specified ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|userId|integer|None|True|The unique identifier for the user|None|12345678|None|None|
  
Example input:

```
{
  "userId": 12345678
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Whether or not the request succeeded|True|
  
Example output:

```
{
  "success": true
}
```

#### Get Application Segment

This action is used to get a specific ZPA application segment by its ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|segment_id|string|None|True|The unique identifier of the ZPA application segment to retrieve|None|123456|None|None|
  
Example input:

```
{
  "segment_id": 123456
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|segment|applicationSegment|False|The ZPA application segment details|{'id': '123456', 'name': 'Internal App', 'enabled': True, 'domainNames': ['app.internal.com'], 'serverGroups': [{'id': '789'}]}|
  
Example output:

```
{
  "segment": {
    "domainNames": [
      "app.internal.com"
    ],
    "enabled": true,
    "id": "123456",
    "name": "Internal App",
    "serverGroups": [
      {
        "id": "789"
      }
    ]
  }
}
```

#### Get Blacklist URL

This action is used to get blacklisted URLs

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|blacklisted_urls|[]string|False|URLs added to the blacklist|["domain.com", "example.com", "example1.com", "example2.com", "example3.com", "example4.com", "example5.com"]|
  
Example output:

```
{
  "blacklisted_urls": [
    "domain.com",
    "example.com",
    "example1.com",
    "example2.com",
    "example3.com",
    "example4.com",
    "example5.com"
  ]
}
```

#### Get DLP Incidents

This action is used to retrieve DLP incident data from Zscaler OneAPI with time range filtering and pagination support

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|end_time|string|None|True|The end time for the DLP incidents query in ISO 8601 format (e.g., 2024-01-02T00:00:00+00:00)|None|2024-01-02T00:00:00+00:00|None|None|
|next_link|string|None|False|Pagination token from a previous response to retrieve the next page of results|None|eyJwYWdlIjogMn0=|None|None|
|start_time|string|None|True|The start time for the DLP incidents query in ISO 8601 format (e.g., 2024-01-01T00:00:00+00:00)|None|2024-01-01T00:00:00+00:00|None|None|
  
Example input:

```
{
  "end_time": "2024-01-02T00:00:00+00:00",
  "next_link": "eyJwYWdlIjogMn0=",
  "start_time": "2024-01-01T00:00:00+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incidents|[]dlpIncident|False|List of DLP incidents matching the query|[{"id": 1, "eventTime": "2024-01-01T12:00:00+00:00", "dlpPolicy": "PCI", "severity": "HIGH"}]|
|next_link|string|False|Pagination token to retrieve the next page of results. Empty if no more pages|eyJwYWdlIjogMn0=|
  
Example output:

```
{
  "incidents": [
    {
      "dlpPolicy": "PCI",
      "eventTime": "2024-01-01T12:00:00+00:00",
      "id": 1,
      "severity": "HIGH"
    }
  ],
  "next_link": "eyJwYWdlIjogMn0="
}
```

#### Get Firewall Logs

This action is used to retrieve firewall logs from Zscaler with time range filtering and pagination support

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|end_time|string|None|True|The end time for the log query in ISO 8601 format (e.g., 2024-01-02T00:00:00+00:00)|None|2024-01-02T00:00:00+00:00|None|None|
|next_link|string|None|False|Pagination token from a previous response to retrieve the next page of results|None|eyJwYWdlIjogMn0=|None|None|
|start_time|string|None|True|The start time for the log query in ISO 8601 format (e.g., 2024-01-01T00:00:00+00:00)|None|2024-01-01T00:00:00+00:00|None|None|
  
Example input:

```
{
  "end_time": "2024-01-02T00:00:00+00:00",
  "next_link": "eyJwYWdlIjogMn0=",
  "start_time": "2024-01-01T00:00:00+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|logs|[]firewallLogEntry|False|List of firewall log entries|[{"datetime": "2024-01-01T12:00:00+00:00", "sourceIP": "192.168.1.1", "destIP": "10.0.0.1", "action": "BLOCKED", "rule": "Block Malware"}]|
|next_link|string|False|Pagination token to retrieve the next page of results. Empty if no more pages|eyJwYWdlIjogMn0=|
  
Example output:

```
{
  "logs": [
    {
      "action": "BLOCKED",
      "datetime": "2024-01-01T12:00:00+00:00",
      "destIP": "10.0.0.1",
      "rule": "Block Malware",
      "sourceIP": "192.168.1.1"
    }
  ],
  "next_link": "eyJwYWdlIjogMn0="
}
```

#### Get Firewall Rule

This action is used to get a specific firewall filtering rule by its ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|rule_id|integer|None|True|The unique identifier of the firewall rule to retrieve|None|12345|None|None|
  
Example input:

```
{
  "rule_id": 12345
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|rule|firewallRule|False|The firewall filtering rule details|{'id': 12345, 'name': 'Block Malware', 'state': 'ENABLED', 'action': 'BLOCK_RESET', 'order': 1}|
  
Example output:

```
{
  "rule": {
    "action": "BLOCK_RESET",
    "id": 12345,
    "name": "Block Malware",
    "order": 1,
    "state": "ENABLED"
  }
}
```

#### Get Sandbox Report for Hash

This action is used to get a full report for an MD5 hash of a file that was analyzed by Sandbox

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|hash|string|None|True|MD5 hash to get report|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
  
Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|full_report|full_report|True|Full report of an analyzed MD5 hash|{'Full Details': {'Summary': {'Status': 'COMPLETED', 'Category': 'EXECS', 'FileType': 'EXE', 'StartTime': 1520333667, 'Duration': 520797}, 'Classification': {'Type': 'MALICIOUS', 'Category': 'ADWARE', 'Score': 76, 'DetectedMalware': 'Adware.Generic.48627'}, 'FileProperties': {'FileType': 'EXE', 'FileSize': 23323, 'MD5': 'afcb861561f7416c5e852001d31f8921', 'SHA1': '1dce4aacf1e17418ebc05d6d2e9034a8271185f9', 'Sha256': 'fc9003461e52006be0188e1fc1b7656c81e930ec78a93eb7ab21fdff3e566314', 'Issuer': '', 'DigitalCerificate': '', 'SSDeep': '384:YcBdTF8O3Fnp7JWmbiV2SBsJmnnB76RF/ewf4XXI9volVL9EFlfnvY1NvJml7Wc:lZF8OXJWmbLW0mnnp6X6rfLC3Osl6c', 'RootCA': ''}, 'SystemSummary': [{'Risk': 'LOW', 'Signature': 'Binary contains paths to debug symbols', 'SignatureSources': ['Not_a_virus.pdb source: 5A9E736319EE0000_5A9E736E00000000.exe']}], 'SecurityBypass': [{'Risk': 'LOW', 'Signature': 'Entrypoint lies outside standard sections', 'SignatureSources': ['section where entry point is pointing to: .Stone']}], 'Persistence': [{'Risk': 'LOW', 'Signature': 'PE file contains sections with non-standard names', 'SignatureSources': ['', 'section name: .Stone']}]}}|
  
Example output:

```
{
  "full_report": {
    "Full Details": {
      "Classification": {
        "Category": "ADWARE",
        "DetectedMalware": "Adware.Generic.48627",
        "Score": 76,
        "Type": "MALICIOUS"
      },
      "FileProperties": {
        "DigitalCerificate": "",
        "FileSize": 23323,
        "FileType": "EXE",
        "Issuer": "",
        "MD5": "afcb861561f7416c5e852001d31f8921",
        "RootCA": "",
        "SHA1": "1dce4aacf1e17418ebc05d6d2e9034a8271185f9",
        "SSDeep": "384:YcBdTF8O3Fnp7JWmbiV2SBsJmnnB76RF/ewf4XXI9volVL9EFlfnvY1NvJml7Wc:lZF8OXJWmbLW0mnnp6X6rfLC3Osl6c",
        "Sha256": "fc9003461e52006be0188e1fc1b7656c81e930ec78a93eb7ab21fdff3e566314"
      },
      "Persistence": [
        {
          "Risk": "LOW",
          "Signature": "PE file contains sections with non-standard names",
          "SignatureSources": [
            "",
            "section name: .Stone"
          ]
        }
      ],
      "SecurityBypass": [
        {
          "Risk": "LOW",
          "Signature": "Entrypoint lies outside standard sections",
          "SignatureSources": [
            "section where entry point is pointing to: .Stone"
          ]
        }
      ],
      "Summary": {
        "Category": "EXECS",
        "Duration": 520797,
        "FileType": "EXE",
        "StartTime": 1520333667,
        "Status": "COMPLETED"
      },
      "SystemSummary": [
        {
          "Risk": "LOW",
          "Signature": "Binary contains paths to debug symbols",
          "SignatureSources": [
            "Not_a_virus.pdb source: 5A9E736319EE0000_5A9E736E00000000.exe"
          ]
        }
      ]
    }
  }
}
```

#### Get Server Group

This action is used to get a specific ZPA server group by its ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|group_id|string|None|True|The unique identifier of the ZPA server group to retrieve|None|789|None|None|
  
Example input:

```
{
  "group_id": 789
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|group|serverGroup|False|The ZPA server group details|{'id': '789', 'name': 'App Server Group', 'enabled': True, 'servers': [{'address': '10.0.0.1'}], 'applications': [{'id': '123456'}]}|
  
Example output:

```
{
  "group": {
    "applications": [
      {
        "id": "123456"
      }
    ],
    "enabled": true,
    "id": "789",
    "name": "App Server Group",
    "servers": [
      {
        "address": "10.0.0.1"
      }
    ]
  }
}
```

#### Get URL Category by Name

This action is used to get the URL category information for the specified name. Supports both predefined Zscaler 
categories and custom categories

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|urlCategoryName|string|None|True|Name of the URL category to retrieve. Can be a predefined Zscaler category name or a custom category name|None|News and Media|None|None|
  
Example input:

```
{
  "urlCategoryName": "News and Media"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|urlCategory|urlCategory|False|Information about the given URL category|{'id': 'CUSTOM_01', 'configuredName': 'Custom Category Example', 'superCategory': 'USER_DEFINED', 'keywords': ['key1'], 'keywordsRetainingParentCategory': ['test1'], 'urls': ['example.com'], 'dbCategorizedUrls': [], 'customCategory': True, 'scopes': [{'type': 'ORGANIZATION'}, {'type': 'DEPARTMENT', 'scopeEntities': [{'id': 12345678, 'name': 'Test Department'}]}, {'type': 'LOCATION', 'scopeEntities': [{'id': 12345678, 'name': 'Location Example'}]}, {'scopeGroupMemberEntities': [], 'type': 'LOCATION', 'scopeEntities': [{'id': 12345678, 'name': 'Location Group Example'}]}], 'editable': True, 'description': 'Example Description', 'type': 'URL_CATEGORY', 'val': 123, 'customUrlsCount': 1, 'urlsRetainingParentCategoryCount': 0, 'customIpRangesCount': 0, 'ipRangesRetainingParentCategoryCount': 0}|
  
Example output:

```
{
  "urlCategory": {
    "configuredName": "Custom Category Example",
    "customCategory": true,
    "customIpRangesCount": 0,
    "customUrlsCount": 1,
    "dbCategorizedUrls": [],
    "description": "Example Description",
    "editable": true,
    "id": "CUSTOM_01",
    "ipRangesRetainingParentCategoryCount": 0,
    "keywords": [
      "key1"
    ],
    "keywordsRetainingParentCategory": [
      "test1"
    ],
    "scopes": [
      {
        "type": "ORGANIZATION"
      },
      {
        "scopeEntities": [
          {
            "id": 12345678,
            "name": "Test Department"
          }
        ],
        "type": "DEPARTMENT"
      },
      {
        "scopeEntities": [
          {
            "id": 12345678,
            "name": "Location Example"
          }
        ],
        "type": "LOCATION"
      },
      {
        "scopeEntities": [
          {
            "id": 12345678,
            "name": "Location Group Example"
          }
        ],
        "scopeGroupMemberEntities": [],
        "type": "LOCATION"
      }
    ],
    "superCategory": "USER_DEFINED",
    "type": "URL_CATEGORY",
    "urls": [
      "example.com"
    ],
    "urlsRetainingParentCategoryCount": 0,
    "val": 123
  }
}
```

#### Get Users

This action is used to gets a list of all users and allows user filtering by name, department, or group. The name 
search parameter performs a partial match. The dept and group parameters perform a 'starts with' match

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|department|string|None|False|Filters by department name|None|Department Name|None|None|
|group|string|None|False|Filters by group name|None|Group Name|None|None|
|name|string|None|False|Filters by user name|None|John|None|None|
|page|integer|None|False|Specifies the page offset|None|1|None|None|
|pageSize|integer|None|False|Specifies the page size|None|100|None|None|
  
Example input:

```
{
  "department": "Department Name",
  "group": "Group Name",
  "name": "John",
  "page": 1,
  "pageSize": 100
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|users|[]user|False|List of organization users|[{"id": 123456789, "name": "Sample user", "email": "user@example.com", "groups": [{"id": 123456789, "name": "Test Group"}], "department": {"id": 123456789, "name": "Test Department"}, "adminUser": False, "isNonEditable": False, "deleted": False}]|
  
Example output:

```
{
  "users": [
    {
      "adminUser": false,
      "deleted": false,
      "department": {
        "id": 123456789,
        "name": "Test Department"
      },
      "email": "user@example.com",
      "groups": [
        {
          "id": 123456789,
          "name": "Test Group"
        }
      ],
      "id": 123456789,
      "isNonEditable": false,
      "name": "Sample user"
    }
  ]
}
```

#### Get Web Logs

This action is used to retrieve web transaction logs from Zscaler with time range filtering and pagination support

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|end_time|string|None|True|The end time for the log query in ISO 8601 format (e.g., 2024-01-02T00:00:00+00:00)|None|2024-01-02T00:00:00+00:00|None|None|
|next_link|string|None|False|Pagination token from a previous response to retrieve the next page of results|None|eyJwYWdlIjogMn0=|None|None|
|start_time|string|None|True|The start time for the log query in ISO 8601 format (e.g., 2024-01-01T00:00:00+00:00)|None|2024-01-01T00:00:00+00:00|None|None|
  
Example input:

```
{
  "end_time": "2024-01-02T00:00:00+00:00",
  "next_link": "eyJwYWdlIjogMn0=",
  "start_time": "2024-01-01T00:00:00+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|logs|[]webLogEntry|False|List of web transaction log entries|[{"datetime": "2024-01-01T12:00:00+00:00", "user": "user@example.com", "url": "https://example.com", "action": "ALLOWED"}]|
|next_link|string|False|Pagination token to retrieve the next page of results. Empty if no more pages|eyJwYWdlIjogMn0=|
  
Example output:

```
{
  "logs": [
    {
      "action": "ALLOWED",
      "datetime": "2024-01-01T12:00:00+00:00",
      "url": "https://example.com",
      "user": "user@example.com"
    }
  ],
  "next_link": "eyJwYWdlIjogMn0="
}
```

#### List Application Segments

This action is used to list ZPA application segments with pagination support

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|next_link|string|None|False|Pagination token from a previous response to retrieve the next page of results|None|eyJwYWdlIjogMn0=|None|None|
  
Example input:

```
{
  "next_link": "eyJwYWdlIjogMn0="
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|next_link|string|False|Pagination token to retrieve the next page of results. Empty if no more pages|eyJwYWdlIjogMn0=|
|segments|[]applicationSegment|False|List of ZPA application segments|[{"id": "123456", "name": "Internal App", "enabled": True, "domainNames": ["app.internal.com"]}]|
  
Example output:

```
{
  "next_link": "eyJwYWdlIjogMn0=",
  "segments": [
    {
      "domainNames": [
        "app.internal.com"
      ],
      "enabled": true,
      "id": "123456",
      "name": "Internal App"
    }
  ]
}
```

#### List Firewall Rules

This action is used to list all firewall filtering rules with pagination support

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|next_link|string|None|False|Pagination token from a previous response to retrieve the next page of results|None|eyJwYWdlIjogMn0=|None|None|
|search|string|None|False|Filter rules by name (case-insensitive partial match). If provided, only rules whose name contains this string will be returned|None|Block|None|None|
  
Example input:

```
{
  "next_link": "eyJwYWdlIjogMn0=",
  "search": "Block"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|next_link|string|False|Pagination token to retrieve the next page of results. Empty if no more pages|eyJwYWdlIjogMn0=|
|rules|[]firewallRule|False|List of firewall filtering rules|[{"id": 1, "name": "Block Malware", "state": "ENABLED", "action": "BLOCK_RESET"}]|
  
Example output:

```
{
  "next_link": "eyJwYWdlIjogMn0=",
  "rules": [
    {
      "action": "BLOCK_RESET",
      "id": 1,
      "name": "Block Malware",
      "state": "ENABLED"
    }
  ]
}
```

#### List Server Groups

This action is used to list ZPA server groups with pagination support

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|next_link|string|None|False|Pagination token from a previous response to retrieve the next page of results|None|eyJwYWdlIjogMn0=|None|None|
  
Example input:

```
{
  "next_link": "eyJwYWdlIjogMn0="
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|groups|[]serverGroup|False|List of ZPA server groups|[{"id": "789", "name": "App Server Group", "enabled": True, "servers": [{"address": "10.0.0.1"}]}]|
|next_link|string|False|Pagination token to retrieve the next page of results. Empty if no more pages|eyJwYWdlIjogMn0=|
  
Example output:

```
{
  "groups": [
    {
      "enabled": true,
      "id": "789",
      "name": "App Server Group",
      "servers": [
        {
          "address": "10.0.0.1"
        }
      ]
    }
  ],
  "next_link": "eyJwYWdlIjogMn0="
}
```

#### Lookup URL

This action is used to look up the categorization of a given set of URLs

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|urls|[]string|None|True|The given set of URLs or domains to be looked up|None|["example.com", "https://rapid7.com"]|None|None|
  
Example input:

```
{
  "urls": [
    "example.com",
    "https://rapid7.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|url_categorization|[]url_categorization|True|Information about given URLs|[{"url": "example.com", "urlClassifications": ["REFERENCE_SITES", "INTERNET_SERVICES"], "urlClassificationsWithSecurityAlert": []}, {"url": "rapid7.com", "urlClassifications": ["CORPORATE_MARKETING", "PROFESSIONAL_SERVICES"], "urlClassificationsWithSecurityAlert": []}]|
  
Example output:

```
{
  "url_categorization": [
    {
      "url": "example.com",
      "urlClassifications": [
        "REFERENCE_SITES",
        "INTERNET_SERVICES"
      ],
      "urlClassificationsWithSecurityAlert": []
    },
    {
      "url": "rapid7.com",
      "urlClassifications": [
        "CORPORATE_MARKETING",
        "PROFESSIONAL_SERVICES"
      ],
      "urlClassificationsWithSecurityAlert": []
    }
  ]
}
```

#### Submit Threat Feed

This action is used to submit custom threat indicators (IoCs) to a Zscaler threat feed

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|False|Optional description for the submitted threat indicators|None|Malicious IPs from incident response|None|None|
|feed_type|string|None|True|The type of threat indicators to submit|["IP", "DOMAIN", "URL"]|IP|None|None|
|indicators|[]string|None|True|List of threat indicators to submit to the feed|None|["192.168.1.100", "10.0.0.50"]|None|None|
  
Example input:

```
{
  "description": "Malicious IPs from incident response",
  "feed_type": "IP",
  "indicators": [
    "192.168.1.100",
    "10.0.0.50"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|submitted_count|integer|True|The number of indicators successfully submitted|2|
|success|boolean|True|Whether the threat feed submission was successful|True|
  
Example output:

```
{
  "submitted_count": 2,
  "success": true
}
```

#### Update Firewall Rule

This action is used to update an existing firewall filtering rule

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|rule_data|object|None|True|The updated firewall rule configuration object containing rule properties to modify|None|{'name': 'Block Malware Updated', 'state': 'ENABLED', 'action': 'BLOCK_RESET', 'order': 1}|None|None|
|rule_id|integer|None|True|The unique identifier of the firewall rule to update|None|12345|None|None|
  
Example input:

```
{
  "rule_data": {
    "action": "BLOCK_RESET",
    "name": "Block Malware Updated",
    "order": 1,
    "state": "ENABLED"
  },
  "rule_id": 12345
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|rule|firewallRule|False|The updated firewall filtering rule|{'id': 12345, 'name': 'Block Malware Updated', 'state': 'ENABLED', 'action': 'BLOCK_RESET', 'order': 1}|
  
Example output:

```
{
  "rule": {
    "action": "BLOCK_RESET",
    "id": 12345,
    "name": "Block Malware Updated",
    "order": 1,
    "state": "ENABLED"
  }
}
```

#### Update URLs of URL Category

This action is used to adds or removes URLs for the specified URL category. Supports both predefined Zscaler categories
 and custom categories

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|None|True|The action applied to the URLs|["Add to the list", "Remove from the list"]|Add to the list|None|None|
|urlCategoryName|string|None|True|Name of the URL category to update. Can be a predefined Zscaler category name or a custom category name|None|News and Media|None|None|
|urlList|[]string|None|True|List of the URLs to be updated|None|["example.com", "example1.com"]|None|None|
  
Example input:

```
{
  "action": "Add to the list",
  "urlCategoryName": "News and Media",
  "urlList": [
    "example.com",
    "example1.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|urlCategory|urlCategory|False|Information about the updated URL category|{'id': 'CUSTOM_01', 'configuredName': 'Custom Category Example', 'superCategory': 'USER_DEFINED', 'keywords': ['key1'], 'keywordsRetainingParentCategory': ['test1'], 'urls': ['example.com'], 'dbCategorizedUrls': [], 'customCategory': True, 'scopes': [{'type': 'ORGANIZATION'}, {'type': 'DEPARTMENT', 'scopeEntities': [{'id': 12345678, 'name': 'Test Department'}]}, {'type': 'LOCATION', 'scopeEntities': [{'id': 12345678, 'name': 'Location Example'}]}, {'scopeGroupMemberEntities': [], 'type': 'LOCATION_GROUP', 'scopeEntities': [{'id': 12345678, 'name': 'Location Group Example'}]}], 'editable': True, 'description': 'Example Description', 'type': 'URL_CATEGORY', 'val': 123, 'customUrlsCount': 1, 'urlsRetainingParentCategoryCount': 0, 'customIpRangesCount': 0, 'ipRangesRetainingParentCategoryCount': 0}|
  
Example output:

```
{
  "urlCategory": {
    "configuredName": "Custom Category Example",
    "customCategory": true,
    "customIpRangesCount": 0,
    "customUrlsCount": 1,
    "dbCategorizedUrls": [],
    "description": "Example Description",
    "editable": true,
    "id": "CUSTOM_01",
    "ipRangesRetainingParentCategoryCount": 0,
    "keywords": [
      "key1"
    ],
    "keywordsRetainingParentCategory": [
      "test1"
    ],
    "scopes": [
      {
        "type": "ORGANIZATION"
      },
      {
        "scopeEntities": [
          {
            "id": 12345678,
            "name": "Test Department"
          }
        ],
        "type": "DEPARTMENT"
      },
      {
        "scopeEntities": [
          {
            "id": 12345678,
            "name": "Location Example"
          }
        ],
        "type": "LOCATION"
      },
      {
        "scopeEntities": [
          {
            "id": 12345678,
            "name": "Location Group Example"
          }
        ],
        "scopeGroupMemberEntities": [],
        "type": "LOCATION_GROUP"
      }
    ],
    "superCategory": "USER_DEFINED",
    "type": "URL_CATEGORY",
    "urls": [
      "example.com"
    ],
    "urlsRetainingParentCategoryCount": 0,
    "val": 123
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**url_categorization**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|URL|string|None|False|Checked URL|None|
|URL Classifications|[]string|None|False|URL classifications|None|
|URL classifications with security alert|[]string|None|False|URL classifications with security alert|None|
  
**Classification**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Category|string|None|False|Category|None|
|Detected Malware|string|None|False|Detected malware|None|
|Score|integer|None|False|Score|None|
|Type|string|None|False|Type|None|
  
**FileProperties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Digital Certificate|string|None|False|Digital certificate|None|
|File Size|integer|None|False|File size|None|
|File Type|string|None|False|File type|None|
|Issuer|string|None|False|Issuer|None|
|MD5|string|None|False|MD5|None|
|Root CA|string|None|False|Root CA|None|
|SHA1|string|None|False|SHA1|None|
|SS Deep|string|None|False|SS deep|None|
|SHA256|string|None|False|SHA256|None|
  
**PersistenceSummary**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Risk|string|None|False|Risk|None|
|Signature|string|None|False|Signature|None|
|Signature Sources|[]string|None|False|Signature sources|None|
  
**Summary**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Category|string|None|False|Category|None|
|Duration|integer|None|False|Duration|None|
|File Type|string|None|False|File type|None|
|Start Time|integer|None|False|Start time|None|
|Status|string|None|False|Status|None|
  
**FullDetails**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Classification|Classification|None|False|Classification|None|
|File Properties|FileProperties|None|False|File properties|None|
|Networking|[]PersistenceSummary|None|False|Networking|None|
|Persistence|[]PersistenceSummary|None|False|Persistence|None|
|Security Bypass|[]PersistenceSummary|None|False|Security bypass|None|
|Stealth|[]PersistenceSummary|None|False|Stealth|None|
|Summary|Summary|None|False|Summary|None|
|System Summary|[]PersistenceSummary|None|False|System summary|None|
  
**full_report**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Full Details|FullDetails|None|False|Full details|None|
  
**department**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Comments|string|None|False|Additional information about this department|Example comment|
|Deleted|boolean|None|False|Is department deleted|False|
|ID|integer|None|False|Department ID|123456789|
|IdpId|integer|None|False|Identity provider (IdP) ID|123456789|
|Name|string|None|False|Department name|Department Name|
  
**group**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Comments|string|None|False|Additional information about the group|Example comment|
|ID|integer|None|False|Unique identifier for the group|123456789|
|IdpId|integer|None|False|Unique identifier for the identity provider (IdP)|123456789|
|Name|string|None|False|Group name|Group Name|
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Admin User|boolean|None|False|True if this user is an Admin user|False|
|Comments|string|None|False|Additional information about this user|Example comment|
|Deleted|boolean|None|False|Is user deleted|False|
|Department|department|None|False|Department a user belongs to|{}|
|Email|string|None|False|User email consists of a user name and domain name. It does not have to be a valid email address, but it must be unique and its domain must belong to the organization|user@example.com|
|Groups|[]group|None|False|List of groups a user belongs to|[]|
|ID|integer|None|False|User ID|123456789|
|Is Non Editable|boolean|None|False|Is user non-editable|False|
|Name|string|None|False|User name|John|
|Temporary Authentication Email|string|None|False|If you enabled one-time tokens or links, enter the email address to which the Zscaler service sends the tokens or links. If this is empty, the service sends the email to the User email|user@example.com|
|Type|string|None|False|User type. Provided only if this user is not an end user|ADMIN|
  
**urlKeywordCounts**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Retain Parent Keyword Count|integer|None|False|Count of total keywords with retain parent category|0|
|Retain Parent URL Count|integer|None|False|Count of URLs with retain parent category|0|
|Total Keyword Count|integer|None|False|Total keyword count for the category|1|
|Total URL Count|integer|None|False|Custom URL count for the category|1|
  
**entityReference**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Extensions|object|None|False|Extensions|{}|
|ID|integer|None|False|Identifier that uniquely identifies an entity|12345678|
|Name|string|None|False|The configured name of the entity|Entity Name|
  
**adminScope**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Scope Entities|[]entityReference|None|False|Based on the admin scope type, the entities can be the ID/name pair of departments, locations, or location groups|[]|
|Scope Group Member Entities|[]entityReference|None|False|List of ID/name pairs of locations within the location group|[]|
|Type|string|None|False|The admin scope type|ORGANIZATION|
  
**urlCategory**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Configured Name|string|None|False|Name of the URL category|Example Name|
|Custom Category|boolean|None|False|Whether the URL category is custom. Up to 48 custom URL categories can be added per organization|True|
|Custom IP Ranges Count|integer|None|False|The number of custom IP address ranges associated to the URL category|0|
|Custom URLs Count|integer|None|False|The number of custom URLs associated to the URL category|1|
|DB Categorized URLs|[]string|None|False|URLs added to a custom URL category are also retained under the original parent URL category (i.e., the predefined category the URL previously belonged to). The URLs entered are covered by policies that reference the original parent URL category as well as those that reference the custom URL category|[]|
|Description|string|None|False|Description of the URL category. Contains tag name and needs to be localized on client side in case of predefined category, else it contains the user-entered description which does not have localization support|Example description|
|Editable|boolean|None|False|Value is set to false for custom URL category when due to scope user does not have edit permission|True|
|ID|string|None|False|The identifier of the URL category|CUSTOM_01|
|IP Ranges|[]string|None|False|Custom IP address ranges associated with a URL category. Up to 2000 custom IP address ranges and retaining parent custom IP address ranges can be added, per organization, across all categories|[]|
|IP Ranges Retaining Parent Category|[]string|None|False|The retaining parent custom IP address ranges associated with a URL category. Up to 2000 custom IP ranges and retaining parent custom IP address ranges can be added, per organization, across all categories|[]|
|IP Ranges Retaining Parent Category Count|integer|None|False|The number of custom IP address ranges associated to the URL category, that also need to be retained under the original parent category|0|
|Keywords|[]string|None|False|Custom keywords associated with a URL category. Up to 2048 custom keywords can be added per organization across all categories|[]|
|Keywords Retaining Parent Category|[]string|None|False|Retained custom keywords from the parent URL category that is associated to a URL category. Up to 2048 retained parent keywords can be added per organization across all categories (including bandwidth classes)|[]|
|Scopes|[]adminScope|None|False|Scope of the custom categories|[]|
|Super Category|string|None|False|Super Category of the URL category|Games|
|Type|string|None|False|Type of the URL category|URL_CATEGORY|
|URL Keyword Counts|urlKeywordCounts|None|False|URL and keyword counts for the URL category|{}|
|URLs|[]string|None|False|Custom URLs to add to a URL category. Up to 25,000 custom URLs can be added per organization across all categories (including bandwidth classes)|[]|
|URLs Retaining Parent Category Count|integer|None|False|The number of custom URLs associated to the URL category, that also need to be retained under the original parent category|0|
  
**idNameReference**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|Unique identifier|12345|
|Name|string|None|False|Name of the resource|Example Name|
  
**firewallRule**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action|string|None|False|Action taken when packets match the rule|BLOCK_RESET|
|Default Rule|boolean|None|False|Whether this is the default rule|False|
|Departments|[]idNameReference|None|False|Departments to which the rule applies|[]|
|Description|string|None|False|Additional information about the rule|Block known malware destinations|
|Destination Addresses|[]string|None|False|Destination IP addresses for which the rule is applicable|[]|
|Groups|[]idNameReference|None|False|Groups to which the rule applies|[]|
|ID|integer|None|False|Unique identifier for the firewall rule|12345|
|Locations|[]idNameReference|None|False|Locations to which the rule applies|[]|
|Name|string|None|False|Name of the firewall filtering rule|Block Malware|
|Network Applications|[]string|None|False|Network service applications on which the rule is applied|[]|
|Order|integer|None|False|Rule order number|1|
|Predefined|boolean|None|False|Whether this is a predefined rule|False|
|Rank|integer|None|False|Admin rank of the rule|7|
|Source IPs|[]string|None|False|Source IP addresses for which the rule is applicable|[]|
|State|string|None|False|Whether the rule is enabled or disabled|ENABLED|
|Users|[]idNameReference|None|False|Users to which the rule applies|[]|
  
**dlpIncident**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Department|string|None|False|Department of the user|Engineering|
|DLP Policy|string|None|False|Name of the DLP policy that triggered the incident|PCI Data Protection|
|Event Time|string|None|False|Time the DLP incident occurred|2024-01-01T12:00:00Z|
|ID|integer|None|False|Unique identifier for the DLP incident|12345|
|Severity|string|None|False|Severity level of the incident|HIGH|
|User|string|None|False|User associated with the incident|user@example.com|
  
**webLogEntry**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action|string|None|False|Action taken on the request|ALLOWED|
|Date Time|string|None|False|Timestamp of the web transaction|2024-01-01T12:00:00Z|
|Department|string|None|False|Department of the user|Engineering|
|Location|string|None|False|Location of the user|Headquarters|
|URL|string|None|False|Requested URL|https://example.com/path|
|User|string|None|False|User who made the request|user@example.com|
  
**firewallLogEntry**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action|string|None|False|Action taken by the firewall|BLOCKED|
|Date Time|string|None|False|Timestamp of the firewall event|2024-01-01T12:00:00Z|
|Destination IP|string|None|False|Destination IP address|10.0.0.1|
|Destination Port|integer|None|False|Destination port|443|
|Rule|string|None|False|Firewall rule that was matched|Block Malware|
|Source IP|string|None|False|Source IP address|192.168.1.100|
  
**applicationSegment**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|Description of the application segment|Internal application|
|Domain Names|[]string|None|False|Domain names associated with the segment|["app.internal.com"]|
|Enabled|boolean|None|False|Whether the application segment is enabled|True|
|ID|string|None|False|Unique identifier for the application segment|123456|
|Name|string|None|False|Name of the application segment|Internal App|
  
**serverGroup**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|Description of the server group|Production server pool|
|Enabled|boolean|None|False|Whether the server group is enabled|True|
|ID|string|None|False|Unique identifier for the server group|654321|
|Name|string|None|False|Name of the server group|Production Servers|


## Troubleshooting

* To configure OneAPI access:
 1. Log in to ZIdentity at https://{vanity_domain}.zsapi.net.
 2. Navigate to **Administration > API Clients** and create a new OAuth client.
 3. Generate an RSA private key and upload the corresponding public key to the API client.
* Ensure the OAuth client has the required scopes for the actions you intend to use (ZIA, ZPA). For more information see the [Zscaler OneAPI documentation](https://help.zscaler.com/oneapi/understanding-oneapi).

# Version History

* 2.0.0 - Major version bump: migrate to Zscaler OneAPI with OAuth 2.0 Private Key authentication | Add DLP, firewall, logs, threat feed, and ZPA actions | SDK bump to 6.6.0
* 1.5.2 - SDK Bump to 6.3.10 | Update connection test
* 1.5.1 - Requirements.txt bumped | SDK Bump to 6.1.4
* 1.5.0 - Add Actions: `Create User`, `Delete User`, `Get Users`, `Get URL Category by Name`, `Update URLs of URL Category`
* 1.4.0 - Add Activate Configuration input in Blacklist URL action
* 1.3.0 - Add Get Blacklist URL action
* 1.2.1 - Usability updates and updated icon
* 1.2.0 - New action Get Sandbox Report for Hash
* 1.1.2 - Support both domains and URL inputs in the Blacklist URL and Lookup URL actions
* 1.1.1 - Improve documentation around action inputs
* 1.1.0 - New action Blacklist URL
* 1.0.0 - Initial plugin

# Links

* [Zscaler](https://www.zscaler.com/)

## References

* [Zscaler](https://www.zscaler.com/)