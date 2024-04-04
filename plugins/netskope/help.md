# Description

This plugin allows users to create, read, update, and delete URL lists in their Netskope environment

# Key Features

* Apply currently pending changes for URL lists
* Create a new URL list
* Delete specific URL list by ID
* Get all applied or pending URL lists
* Get single user confidence index
* Get URL list by ID
* Update specific URL list by ID
* Replace specific URL list by ID
* Update the file hash list
* Upload JSON config file

# Requirements

* Requires an API Keys for versions v1 and v2, tenant name from the Netskope. Note: Both API Keys are required.

# Supported Product Versions

* 2024-04-02

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key_v1|credential_secret_key|None|True|Netskope authorization token for v1 API|None|9de5069c5afe602b2ea0a04b66beb2c0|
|api_key_v2|credential_secret_key|None|True|Netskope authorization token for v2 API|None|ef50c6bx9umaik9agvoxtoqec2fg9f0y|
|tenant|string|None|True|Owner's name that is included in URL|None|ExampleTenant|

Example input:

```
{
  "api_key_v1": "9de5069c5afe602b2ea0a04b66beb2c0",
  "api_key_v2": "ef50c6bx9umaik9agvoxtoqec2fg9f0y",
  "tenant": "ExampleTenant"
}
```

## Technical Details

### Actions


#### Apply Pending URL List Changes

This action is used to applies currently pending changes for URL lists

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|deployed_urllists|[]urllist|True|Contains list of deployed URL lists|[{"id":1,"name":"ExampleName","data":{"urls":["https://example.com","https://example.com"],"type":"exact"},"modify_by":"Netskope REST API","modify_time":"2022-01-03T00:00:00.000Z","modify_type":"Created","pending":0}]|
  
Example output:

```
{
  "deployed_urllists": [
    {
      "data": {
        "type": "exact",
        "urls": [
          "https://example.com",
          "https://example.com"
        ]
      },
      "id": 1,
      "modify_by": "Netskope REST API",
      "modify_time": "2022-01-03T00:00:00.000Z",
      "modify_type": "Created",
      "name": "ExampleName",
      "pending": 0
    }
  ]
}
```

#### Create a New URL List

This action is used to create a new URL list configuration

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|True|Name of new URL list|None|ExampleName|
|type|string|None|True|Category of URL list|["exact", "regex"]|exact|
|urls|[]string|None|True|List of URLs|None|["https://example.com", "https://example.com"]|
  
Example input:

```
{
  "name": "ExampleName",
  "type": "exact",
  "urls": [
    "https://example.com",
    "https://example.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|data|True|Data containing URLs and type|{"urls": ["https://example.com", "https://example.com"], "type": "exact"}|
|id|integer|True|URL list identifier|0|
|modify_by|string|True|Name of the URL list modifier|Netskope API|
|modify_time|date|True|Last URL list modification time|1997-01-01 00:00:00|
|modify_type|string|True|Shows last modification type. Expected values are Created, Edited, Deleted|Created|
|name|string|True|URL list name|ExampleName|
|pending|integer|True|URL list status of pending (1) and applied (0)|0|
  
Example output:

```
{
  "data": {
    "type": "exact",
    "urls": [
      "https://example.com",
      "https://example.com"
    ]
  },
  "id": 0,
  "modify_by": "Netskope API",
  "modify_time": "1997-01-01 00:00:00",
  "modify_type": "Created",
  "name": "ExampleName",
  "pending": 0
}
```

#### Delete a URL List by ID

This action is used to mark a URL list as pending deletion

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the URL list|None|1|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|data|True|Data containing URLs and type|{"urls": ["https://example.com", "https://example.com"], "type": "exact"}|
|id|integer|True|URL list identifier|0|
|modify_by|string|True|Name of the URL list modifier|Netskope API|
|modify_time|date|True|Last URL list modification time|1997-01-01 00:00:00|
|modify_type|string|True|Shows last modification type. Expected values are Created, Edited, Deleted|Deleted|
|name|string|True|URL list name|ExampleName|
|pending|integer|True|URL list status of pending (1) and applied (0)|0|
  
Example output:

```
{
  "data": {
    "type": "exact",
    "urls": [
      "https://example.com",
      "https://example.com"
    ]
  },
  "id": 0,
  "modify_by": "Netskope API",
  "modify_time": "1997-01-01 00:00:00",
  "modify_type": "Deleted",
  "name": "ExampleName",
  "pending": 0
}
```

#### Get All URL Lists

This action is used to get all applied or pending URL lists

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|status|string|any|True|Status of URL lists to be received|["any", "applied", "pending"]|applied|
  
Example input:

```
{
  "status": "any"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|urllists|[]urllist|True|Contains list of URL list objects|[{"id":1,"name":"ExampleName","data":{"urls":["https://example.com","https://example.com"],"type":"exact"},"modify_by":"Netskope REST API","modify_time":"2022-01-03T00:00:00.000Z","modify_type":"Created","pending":0}]|
  
Example output:

```
{
  "urllists": [
    {
      "data": {
        "type": "exact",
        "urls": [
          "https://example.com",
          "https://example.com"
        ]
      },
      "id": 1,
      "modify_by": "Netskope REST API",
      "modify_time": "2022-01-03T00:00:00.000Z",
      "modify_type": "Created",
      "name": "ExampleName",
      "pending": 0
    }
  ]
}
```

#### Get Single User's Confidence Index

This action is used to get the confidence index for a user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fromTime|integer|None|True|Numeric value representing the time in epoch timestamp from the beginning of which confidence score values are taken until now (in miliseconds)|None|1647357793000|
|username|string|None|True|Username of an existing user|None|ExampleUser|
  
Example input:

```
{
  "fromTime": 1647357793000,
  "username": "ExampleUser"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|confidences|[]confidence|True|Contains User Confidence Index with starting score and confidence score|[{"start": 0, "confidenceScore": 0}]|
|userId|string|True|Identifier of user|ExampleUser|
  
Example output:

```
{
  "confidences": [
    {
      "confidenceScore": 0,
      "start": 0
    }
  ],
  "userId": "ExampleUser"
}
```

#### Get URL List by ID

This action is used to retrieve the configuration of a URL list by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the URL list|None|1|
  
Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|data|True|Data containing URLs and type|{"urls": ["https://example.com", "https://example.com"], "type": "exact"}|
|id|integer|True|URL list identifier|0|
|modify_by|string|True|Name of the URL list modifier|Netskope API|
|modify_time|date|True|Last URL list modification time|1997-01-01 00:00:00|
|modify_type|string|True|Shows last modification type. Expected values are Created, Edited, Deleted|Created|
|name|string|True|URL list name|ExampleName|
|pending|integer|True|URL list status of pending (1) and applied (0)|0|
  
Example output:

```
{
  "data": {
    "type": "exact",
    "urls": [
      "https://example.com",
      "https://example.com"
    ]
  },
  "id": 0,
  "modify_by": "Netskope API",
  "modify_time": "1997-01-01 00:00:00",
  "modify_type": "Created",
  "name": "ExampleName",
  "pending": 0
}
```

#### Update URL List by ID

This action is used to update the name, URLs, and/or type of a URL list object

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|None|True|Replace or append to current URLs|["replace", "append"]|append|
|id|integer|None|True|ID of the URL list|None|1|
|name|string|None|False|Name of replaced URL list|None|ExampleName|
|type|string|None|False|Category of URL list (to update this value, URLs input must also be provided)|["", "exact", "regex"]|exact|
|urls|[]string|None|False|List of URLs (to update this value, URL List Category input must also be provided)|None|["https://example.com", "https://example.com"]|
  
Example input:

```
{
  "action": "append",
  "id": 1,
  "name": "ExampleName",
  "type": "exact",
  "urls": [
    "https://example.com",
    "https://example.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|data|True|Data containing URLs and type|{"urls": ["https://example.com", "https://example.com"], "type": "exact"}|
|id|integer|True|URL list identifier|0|
|modify_by|string|True|Name of the URL list modifier|Netskope API|
|modify_time|date|True|Last URL list modification time|1997-01-01 00:00:00|
|modify_type|string|True|Shows last modification type. Expected values are Created, Edited, Deleted|Edited|
|name|string|True|URL list name|ExampleName|
|pending|integer|True|URL list status of pending (1) and applied (0)|0|
  
Example output:

```
{
  "data": {
    "type": "exact",
    "urls": [
      "https://example.com",
      "https://example.com"
    ]
  },
  "id": 0,
  "modify_by": "Netskope API",
  "modify_time": "1997-01-01 00:00:00",
  "modify_type": "Edited",
  "name": "ExampleName",
  "pending": 0
}
```

#### Replace URL List Configuration by ID

This action is used to replace the configuration of the given URL list by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|integer|None|True|ID of the URL list|None|1|
|name|string|None|True|Name of replaced URL list|None|ExampleName|
|type|string|None|True|Category of URL list|["exact", "regex"]|exact|
|urls|[]string|None|True|List that contains URLs|None|["https://example.com", "https://example.com"]|
  
Example input:

```
{
  "id": 1,
  "name": "ExampleName",
  "type": "exact",
  "urls": [
    "https://example.com",
    "https://example.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|data|True|Data containing URLs and type|{"urls": ["https://example.com", "https://example.com"], "type": "exact"}|
|id|integer|True|URL list identifier|0|
|modify_by|string|True|Name of the URL list modifier|Netskope API|
|modify_time|date|True|Last URL list modification time|1997-01-01 00:00:00|
|modify_type|string|True|Shows last modification type. Expected values are Created, Edited, Deleted|Edited|
|name|string|True|URL list name|ExampleName|
|pending|integer|True|URL list status of pending (1) and applied (0)|0|
  
Example output:

```
{
  "data": {
    "type": "exact",
    "urls": [
      "https://example.com",
      "https://example.com"
    ]
  },
  "id": 0,
  "modify_by": "Netskope API",
  "modify_time": "1997-01-01 00:00:00",
  "modify_type": "Edited",
  "name": "ExampleName",
  "pending": 0
}
```

#### Update a File Hash List

This action is used to updates the File Hash List with the values provided

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|list|[]string|None|True|Comma-separated list of file hashes (MD5 or SHA256), with the maximum size of the list being 8MB|None|["e28eb9739b6e84d0f796e3acc0f5b71e", "e28eb9739b6e84d0f697e3acc0f5b71a", "e28eb9839b6e74d0f696e3acc0f6b710"]|
|name|string|None|True|Name of an existing File Hash List shown in the Netskope UI on the File Hash List page|None|ExampleExistingFileHashList|
  
Example input:

```
{
  "list": [
    "e28eb9739b6e84d0f796e3acc0f5b71e",
    "e28eb9739b6e84d0f697e3acc0f5b71a",
    "e28eb9839b6e74d0f696e3acc0f6b710"
  ],
  "name": "ExampleExistingFileHashList"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|string|True|API response message|File Filter Profile updated successfully|
|status|string|True|API response status|success|
  
Example output:

```
{
  "message": "File Filter Profile updated successfully",
  "status": "success"
}
```

#### Upload JSON File Configurations

This action is used to send multiple configurations via a JSON file

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|urllist|file|None|True|File that includes urllist in JSON format, which must have extension as *.json|None|{"items": [{"name": "string", "data": {"urls": ["https://example.com"], "type": "exact" }}]}|
  
Example input:

```
{
  "urllist": {
    "items": [
      {
        "data": {
          "type": "exact",
          "urls": [
            "https://example.com"
          ]
        },
        "name": "string"
      }
    ]
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|uploaded_urllist|[]urllist|True|Contains list of uploaded URL list objects|[{"id":1,"name":"ExampleName","data":{"urls":["https://example.com","https://example.com"],"type":"exact"},"modify_by":"Netskope REST API","modify_time":"2022-01-03T00:00:00.000Z","modify_type":"Created","pending":0}]|
  
Example output:

```
{
  "uploaded_urllist": [
    {
      "data": {
        "type": "exact",
        "urls": [
          "https://example.com",
          "https://example.com"
        ]
      },
      "id": 1,
      "modify_by": "Netskope REST API",
      "modify_time": "2022-01-03T00:00:00.000Z",
      "modify_type": "Created",
      "name": "ExampleName",
      "pending": 0
    }
  ]
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**data**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|URL List Category|string|None|True|Category of URL list|None|
|URLs|[]string|None|True|List of URLs|None|
  
**urllist**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Data|data|None|False|Data containing URLs and type|None|
|ID|integer|None|True|URL list identifier|None|
|Modify By|string|None|True|Name of the URL list modifier|None|
|Modify Time|date|None|True|Last URL list modification time|None|
|Modify Type|string|None|True|Shows last modification type. Expected values are Created, Edited, Deleted|None|
|Name|string|None|True|URL list name|None|
|Pending|integer|None|True|URL list status of pending (1) and applied (0)|None|
  
**confidence**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Confidence Score|integer|None|True|Numeric value representing user's confidence score|None|
|Start|integer|None|True|Numeric value representing epoch timestamp|None|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History

* 1.0.2 - Updated SDK to the latest version | Fixed issue related to API changes | Updated unittests
* 1.0.1 - Fix bug where Update URL List by ID did not support empty non-required Name field | Update Update URL List by ID input descriptions
* 1.0.0 - Initial plugin (Actions: Apply Pending URL List Changes, Create a New URL List, Delete a URL List by ID, Get All URL Lists, Get Single User's Confidence Index, Get URL List by ID, Replace URL List Configuration by ID, Update URL List by ID, Update a File Hash List, Upload JSON File Configurations)

# Links

* [Netskope](https://www.netskope.com/)

## References

* [Netskope API v1](https://docs.netskope.com/en/rest-api-v1-overview.html)
* [Netskope API v2](https://docs.netskope.com/en/rest-api-v2-overview-312207.html)