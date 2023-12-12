# Description

Confluence is an open and shared workspace for managing documents and files within an organization. Using the Confluence plugin for Rapid7 InsightConnect, users can view and update pages dynamically within automation workflows

# Key Features
  
* Update pages
* View pages

# Requirements
  
* Confluence URL
* Confluence username and API token

# Supported Product Versions
  
* 2023-12-12

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_token|credential_secret_key|None|True|API token|None|9de5069c5afe602b2ea0a04b66beb2c0|
|cloud|boolean|None|True|Is this a cloud instance|None|True|
|url|string|None|True|Connection URL|None|https://example.atlassian.net|
|username|string|None|True|Account username (Atlassian account email)|None|user@example.com|
  
Example input:

```
{
  "api_token": "9de5069c5afe602b2ea0a04b66beb2c0",
  "cloud": true,
  "url": "https://example.atlassian.net",
  "username": "user@example.com"
}
```

## Technical Details

### Actions


#### Get Page
  
Get Page

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page|string|None|True|Page Name|None|Example Page|
|space|string|None|True|Space|None|Example Space|
  
Example input:

```
{
  "page": "Example Page",
  "space": "Example Space"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|False|True if found|True|
|page|page|False|Page|{ "content": "<p>Example Content</p>", "contentStatus": "current", "created": "2000-01-01T00:00:00.000Z", "creator": "Example User", "current": true, "homePage": false, "id": "100001", "modified": "2000-01-01T00:00:00.000Z", "space": "Example Space", "title": "Example Page", "url": "https://test.atlassian.net/wiki/spaces/~1111111a111aaaaa11a1aa111aaaaaa1aa1aaaa/pages/100001/Example+Page", "version": "2" }|
  
Example output:

```
{
  "found": true,
  "page": {
    "content": "<p>Example Content</p>",
    "contentStatus": "current",
    "created": "2000-01-01T00:00:00.000Z",
    "creator": "Example User",
    "current": true,
    "homePage": false,
    "id": "100001",
    "modified": "2000-01-01T00:00:00.000Z",
    "space": "Example Space",
    "title": "Example Page",
    "url": "https://test.atlassian.net/wiki/spaces/~1111111a111aaaaa11a1aa111aaaaaa1aa1aaaa/pages/100001/Example+Page",
    "version": "2"
  }
}
```

#### Get Page By ID
  
Get Page By ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page_id|string|None|True|Page ID|None|100001|
  
Example input:

```
{
  "page_id": 100001
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|False|True if found|True|
|page|page|False|Page|{ "content": "<p>Example Content</p>", "contentStatus": "current", "created": "2000-01-01T00:00:00.000Z", "creator": "Example User", "current": true, "homePage": false, "id": "100001", "modified": "2000-01-01T00:00:00.000Z", "space": "Example Space", "title": "Example Page", "url": "https://test.atlassian.net/wiki/spaces/~1111111a111aaaaa11a1aa111aaaaaa1aa1aaaa/pages/100001/Example+Page", "version": "2" }|
  
Example output:

```
{
  "found": true,
  "page": {
    "content": "<p>Example Content</p>",
    "contentStatus": "current",
    "created": "2000-01-01T00:00:00.000Z",
    "creator": "Example User",
    "current": true,
    "homePage": false,
    "id": "100001",
    "modified": "2000-01-01T00:00:00.000Z",
    "space": "Example Space",
    "title": "Example Page",
    "url": "https://test.atlassian.net/wiki/spaces/~1111111a111aaaaa11a1aa111aaaaaa1aa1aaaa/pages/100001/Example+Page",
    "version": "2"
  }
}
```

#### Get Page Content
  
Get Page Content

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page|string|None|True|Page Name|None|Example Page|
|space|string|None|True|Space|None|Example Space|
  
Example input:

```
{
  "page": "Example Page",
  "space": "Example Space"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|content|string|False|Content|<p>Example Content</p>|
|found|boolean|False|True if found|True|
  
Example output:

```
{
  "content": "<p>Example Content</p>",
  "found": true
}
```

#### Get Page Content By ID
  
Get Page Content by Page ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page_id|string|None|True|Page ID|None|100001|
  
Example input:

```
{
  "page_id": 100001
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|content|string|False|Content|<p>Example Content</p>|
|found|boolean|False|True if found|True|
  
Example output:

```
{
  "content": "<p>Example Content</p>",
  "found": true
}
```

#### Store Page Content
  
Store Page Content

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|content|string|None|True|Content To Store|None|<p>Example Content</p>|
|page|string|None|True|Page Name|None|Example page|
|space|string|None|True|Space|None|Example Space|
  
Example input:

```
{
  "content": "<p>Example Content</p>",
  "page": "Example page",
  "space": "Example Space"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|page|page|False|Page Stored|{ "content": "<p>Example Content</p>", "contentStatus": "current", "created": "2000-01-01T00:00:00.000Z", "creator": "Example User", "current": true, "homePage": false, "id": "100001", "modified": "2000-01-01T00:00:00.000Z", "space": "Example Space", "title": "Example Page", "url": "https://test.atlassian.net/wiki/spaces/~1111111a111aaaaa11a1aa111aaaaaa1aa1aaaa/pages/100001/Example+Page", "version": "2" }|
  
Example output:

```
{
  "page": {
    "content": "<p>Example Content</p>",
    "contentStatus": "current",
    "created": "2000-01-01T00:00:00.000Z",
    "creator": "Example User",
    "current": true,
    "homePage": false,
    "id": "100001",
    "modified": "2000-01-01T00:00:00.000Z",
    "space": "Example Space",
    "title": "Example Page",
    "url": "https://test.atlassian.net/wiki/spaces/~1111111a111aaaaa11a1aa111aaaaaa1aa1aaaa/pages/100001/Example+Page",
    "version": "2"
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
  
* [Vendor](https://www.atlassian.com)