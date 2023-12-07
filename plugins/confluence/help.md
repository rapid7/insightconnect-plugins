# Description

Confluence is an open and shared workspace for managing documents and files within an organization. Using the Confluence plugin for Rapid7 InsightConnect, users can view and update pages dynamically within automation workflows

# Key Features
  
*This plugin does not contain any key features.*

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions
  
*This plugin does not contain any supported product versions.*

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|True|Username and password|None|None|
|url|string|None|True|Connection URL|None|None|
  
Example input:

```
{
  "credentials": {
    "password": "",
    "username": ""
  },
  "url": ""
}
```

## Technical Details

### Actions


#### Get Page
  
Get Page

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page|string|None|True|Page Name|None|None|
|space|string|None|True|Space|None|None|
  
Example input:

```
{
  "page": "",
  "space": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|False|True if found|None|
|page|page|False|Page|None|
  
Example output:

```
{
  "found": true,
  "page": {
    "content": {},
    "contentStatus": {},
    "created": "",
    "creator": {},
    "current": {},
    "homePage": "true",
    "id": {},
    "modified": {},
    "modifier": {},
    "parentId": {},
    "permissions": {},
    "space": {},
    "title": "",
    "url": {},
    "version": {}
  }
}
```

#### Get Page By ID
  
Get Page By ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page_id|string|None|True|Page ID|None|None|
  
Example input:

```
{
  "page_id": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|False|True if found|None|
|page|page|False|Page|None|
  
Example output:

```
{
  "found": true,
  "page": {
    "content": {},
    "contentStatus": {},
    "created": "",
    "creator": {},
    "current": {},
    "homePage": "true",
    "id": {},
    "modified": {},
    "modifier": {},
    "parentId": {},
    "permissions": {},
    "space": {},
    "title": "",
    "url": {},
    "version": {}
  }
}
```

#### Get Page Content
  
Get Page Content

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page|string|None|True|Page Name|None|None|
|space|string|None|True|Space|None|None|
  
Example input:

```
{
  "page": "",
  "space": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|content|string|False|Content|None|
|found|boolean|False|True if found|None|
  
Example output:

```
{
  "content": "",
  "found": true
}
```

#### Get Page Content By ID
  
Get Page Content by Page ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page_id|string|None|True|Page ID|None|None|
  
Example input:

```
{
  "page_id": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|content|string|False|Content|None|
|found|boolean|False|True if found|None|
  
Example output:

```
{
  "content": "",
  "found": true
}
```

#### Store Page Content
  
Store Page Content

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|content|string|None|True|Content To Store|None|None|
|page|string|None|True|Page Name|None|None|
|space|string|None|True|Space|None|None|
  
Example input:

```
{
  "content": "",
  "page": "",
  "space": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|page|page|False|Page Stored|None|
  
Example output:

```
{
  "page": {
    "content": {},
    "contentStatus": {},
    "created": "",
    "creator": {},
    "current": {},
    "homePage": "true",
    "id": {},
    "modified": {},
    "modifier": {},
    "parentId": {},
    "permissions": {},
    "space": {},
    "title": "",
    "url": {},
    "version": {}
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**page**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|content|string|None|False|Page Content|None|
|contentStatus|string|None|False|Content Status|None|
|created|date|None|False|Created Date|None|
|creator|string|None|False|Creator User|None|
|current|boolean|None|False|True if current version|None|
|homePage|boolean|None|False|Home Page|None|
|id|string|None|False|Page ID|None|
|modified|date|None|False|Modified Date|None|
|modifier|string|None|False|Modifier User|None|
|parentId|string|None|False|Parent Page ID|None|
|permissions|string|None|False|Permissions|None|
|space|string|None|False|Space|None|
|title|string|None|False|Page Title|None|
|url|string|None|False|URL|None|
|version|string|None|False|Page Version|None|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History
  
*This plugin does not contain a version history.*

# Links


## References
  
*This plugin does not contain any references.*