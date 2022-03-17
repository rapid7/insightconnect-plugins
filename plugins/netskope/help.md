# Description

This plugin allows users to create, read, update, and delete URL list

# Key Features

* Apple currently pending changes for URL lists
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

* 2022-02-11

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key_v1|credential_secret_key|None|True|Netskope authorization token for v1 API|None|9de5069c5afe602b2ea0a04b66beb2c0|
|api_key_v2|credential_secret_key|None|True|Netskope authorization token for v2 API|None|ef50c6bx9umaik9agvoxtoqec2fg9f0y|
|tenant|string|None|True|Owner's name that is included in URL|None|exampletenant|

Example input:

```
{
  "api_key_v1": "9de5069c5afe602b2ea0a04b66beb2c0",
  "api_key_v2": "ef50c6bx9umaik9agvoxtoqec2fg9f0y",
  "tenant": "exampletenant"
}
```

## Technical Details

### Actions

#### Update URL List by ID

This action is used to update the name, URLs, and/or type of a URL list object.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|None|True|Replace or append to current URLs|['replace', 'append']|append|
|id|integer|None|True|ID of the URL list|None|1|
|name|string|None|False|Name of replaced URL list|None|ExampleName|
|type|string|None|False|Category of URL list|['', 'exact', 'regex']|exact|
|urls|[]string|None|False|List of URLs|None|["https://example.com", "https://example.com"]|

Example input (type exact):

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

Example input (type regex):

```
{
  "name": "ExampleName",
  "type": "regex",
  "urls": [
    "https://example.com/*",
    "example",
    "example.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|object|True|Data containing and type|
|id|integer|True|URL list identifier|
|modify_by|string|True|Name of the URL list modifier|
|modify_time|date|True|Last URL list modification time|
|modify_type|string|True|Shows last modification type. Expected values are Created, Edited, Deleted|
|name|string|True|URL list name|
|pending|integer|True|URL list status of pending (1) and applied (0)|

Example output:

```
{
	"id": 1,
	"name": "ExampleName",
  "data": {
    "urls": [
      "https://example.com",
      "https://example.com"
    ],
    "type": "exact"
  },
	"modify_by": "Netskope REST API",
	"modify_time": "1997-01-01 00:00:00",
  "modify_type": "Edited",
  "pending": 0
}
```

#### Replace URL List Configuration by ID

This action is used to replace the configuration of the given URL list by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|integer|None|True|ID of the URL list|None|1|
|name|string|None|True|Name of replaced URL list|None|ExampleName|
|type|string|None|True|Category of URL list|['exact', 'regex']|exact|
|urls|[]string|None|True|List that contains URLs|None|["https://example.com", "https://example.com"]|

Example input (type exact):

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

Example input (type regex):

```
{
  "name": "ExampleName",
  "type": "regex",
  "urls": [
    "https://example.com/*",
    "example",
    "example.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|data|True|Data containing URLs and type|
|id|integer|True|URL list identifier|
|modify_by|string|True|Name of the URL list modifier|
|modify_time|date|True|Last URL list modification time|
|modify_type|string|True|Shows last modification type. Expected values are Created, Edited, Deleted|
|name|string|True|URL list name|
|pending|integer|True|URL list status of pending (1) and applied (0)|

Example output:

```
{
	"id": 1,
	"name": "ExampleName",
  "data": {
    "urls": [
      "https://example.com",
      "https://example.com"
    ],
    "type": "exact"
  },
	"modify_by": "Netskope REST API",
	"modify_time": "1997-01-01 00:00:00",
  "modify_type": "Edited",
  "pending": 0
}
```

#### Get All URL Lists

This action is used to get all applied or pending URL lists.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|status|string|any|True|Status of URL lists to be received|['any', 'applied', 'pending']|applied|

Example input:

```
{
  "status": "applied"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|urllists|[]urllist|True|Contains list of URL list objects|

Example output:

```
{
  "urllists": [
    {
      "id": 1,
      "name": "ExampleName",
      "data": {
        "urls": [
          "https://example.com",
          "https://example.com"
        ],
        "type": "exact"
      },
      "modify_by": "Netskope REST API",
      "modify_time": "2022-01-03T00:00:00.000Z",
      "modify_type": "Created",
      "pending": 0
    }
  ]
}
```

#### Delete a URL List by ID

This action is used to mark a URL list as pending deletion.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|integer|None|True|ID of the URL list|None|1|

Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|data|True|Data containing URLs and type|
|id|integer|True|URL list identifier|
|modify_by|string|True|Name of the URL list modifier|
|modify_time|date|True|Last URL list modification time|
|modify_type|string|True|Shows last modification type. Expected values are Created, Edited, Deleted|
|name|string|True|URL list name|
|pending|integer|True|URL list status of pending (1) and applied (0)|

Example output:

```
{
  "id": 1,
  "name": "ExampleName",
  "data": {
    "urls": [
      "https://example.com",
      "https://example.com"
    ],
    "type": "exact"
  },
  "modify_by": "Netskope REST API",
  "modify_time": "1997-01-01 00:00:00",
  "modify_type": "Deleted",
  "pending": 0
}
```

#### Apply Pending URL List Changes

This action applies currently pending changes for URL lists.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|deployed_urllists|[]urllist|True|Contains list of deployed URL lists|

Example output:

```
{
	"deployed_urllists": [
		{
			"id": 1,
			"name": "ExampleName",
			"data": {
				"urls": [
					"https://example.com",
					"https://example.com"
				], 
			"type": "exact"
			},
			"modify_by": "Netskope REST API",
			"modify_time": "1997-01-01 00:00:00",
			"modify_type": "Created",
			"pending": 0
		}
	]
}
```

#### Create a New URL List

This action is used to create a new URL list configuration.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|Name of new URL list|None|ExampleName|
|type|string|None|True|Category of URL list|['exact', 'regex']|exact|
|urls|[]string|None|True|List of URLs|None|["https://example.com", "https://example.com"]|

Example input (type exact):

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

Example input (type regex):

```
{
  "name": "ExampleName",
  "type": "regex",
  "urls": [
    "https://example.com/*",
    "example",
    "example.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|data|True|Data containing URLs and type|
|id|integer|True|URL list identifier|
|modify_by|string|True|Name of the URL list modifier|
|modify_time|date|True|Last URL list modification time|
|modify_type|string|True|Shows last modification type. Expected values are Created, Edited, Deleted|
|name|string|True|URL list name|
|pending|integer|True|URL list status of pending (1) and applied (0)|

Example output:

```
{
  "id": 1,
      "name": "ExampleName",
      "data": {
        "urls": [
          "https://example.com",
          "https://example.com"
        ],
    "type": "exact"
      },
  "modify_by": "Netskope REST API",
			"modify_time": "1997-01-01 00:00:00",
  "modify_type": "Created",
      "pending": 0
    }
```

#### Get Single User's Confidence Index

This action is used to get single user's confidence index.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|confidences|[]confidence|True|Contains User Confidence Index with starting score and confidence score|
|userId|string|True|Identifier of user|

Example output:

```
{
  "userId": "ExampleUser",
  "confidences": [
    {
      "start": 0,
      "confidenceScore": 0
    }
  ]
}
```

#### Get URL List by ID

This action is used to get the configuration of the given URL list ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|integer|None|True|ID of the URL list|None|1|

Example input:

```
{
  "id": 1
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|data|True|Data containing URLs and type|
|id|integer|True|URL list identifier|
|modify_by|string|True|Name of the URL list modifier|
|modify_time|date|True|Last URL list modification time|
|modify_type|string|True|Shows last modification type. Expected values are Created, Edited, Deleted|
|name|string|True|URL list name|
|pending|integer|True|URL list status of pending (1) and applied (0)|

Example output:

```
{
  "id": 1,
  "name": "ExampleName",
  "data": {
    "urls": [
      "https://example.com",
      "https://example.com"
    ],
    "type": "exact"
  },
  "modify_by": "Netskope REST API",
  "modify_time": "1997-01-01 00:00:00",
  "modify_type": "Created",
  "pending": 0
}
```

#### Update a File Hash List

This action updates the File Hash List with the values provided. This replaces the existing values with the new values, so include the existing values you want to keep in the list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|API response message|
|status|string|True|API response status|

Example output:

```
{
  "status": "success",
  "msg": "File Filter Profile updated successfully"
}
```

#### Upload JSON File Configurations

This action is used to upload multiple configurations via a JSON file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|urllist|file|None|True|File that includes urllist in JSON format, which must have extension as *.json|None|{"items": [{"name": "string", "data": {"urls": ["https://example.com"], "type": "exact" }}]}|

Example input:

```
{
  "urllist": {
    "items": [
      {
        "name": "string",
        "data": {
          "urls": [
            "https://example.com"
          ],
          "type": "exact"
        }
      }
    ]
  }
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|uploaded_urllist|[]urllist|True|Contains list of uploaded URL list objects|

Example output:

```
{
  "uploaded_urllist": [
    {
      "id": 1,
      "name": "string",
      "data": {
        "urls": [
          "https://example.com"
        ],
        "type": "exact"
      },
      "modify_by": "Netskope REST API",
      "modify_time": "2022-02-01T12:20:23.000Z",
      "modify_type": "Created",
      "pending": 1
    }
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin (Actions: Apply Pending URL List Changes, Create a New URL List, Delete a URL List by ID, Get All URL Lists, Get Single User's Confidence Index, Get URL List by ID, Replace URL List Configuration by ID, Update URL List by ID, Update a File Hash List, Upload JSON File Configurations)

# Links

## References

* [Netskope](https://www.netskope.com/)
* [Netskope API v1](https://docs.netskope.com/en/rest-api-v1-overview.html)
* [Netskope API v2](https://docs.netskope.com/en/rest-api-v2-overview-312207.html)

