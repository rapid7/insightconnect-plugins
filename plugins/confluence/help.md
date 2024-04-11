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
|cloud|boolean|None|True|Indicates whether the instance is cloud or not|None|True|
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

This action is used to retrieve confluence page by name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page|string|None|True|Page Name|None|ExamplePage|
|space|string|None|True|The name of a space|None|ExampleSpace|
  
Example input:

```
{
  "page": "ExamplePage",
  "space": "ExampleSpace"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|False|Indicates whether the page content was found or not, true if found|True|
|page|page|False|Returned page object data|{"content":"<p>ExampleContent</p>","contentStatus":"current","created":"2000-01-01T00:00:00.000Z","creator":"ExampleUser","current":true,"homePage":false,"id":"100001","modified":"2000-01-01T00:00:00.000Z","space":"ExampleSpace","title":"ExamplePage","url":"https://test.atlassian.net/wiki/spaces/~1111111a111aaaaa11a1aa111aaaaaa1aa1aaaa/pages/100001/Example+Page","version":"2"}|
  
Example output:

```
{
  "found": true,
  "page": {
    "content": "<p>ExampleContent</p>",
    "contentStatus": "current",
    "created": "2000-01-01T00:00:00.000Z",
    "creator": "ExampleUser",
    "current": true,
    "homePage": false,
    "id": "100001",
    "modified": "2000-01-01T00:00:00.000Z",
    "space": "ExampleSpace",
    "title": "ExamplePage",
    "url": "https://test.atlassian.net/wiki/spaces/~1111111a111aaaaa11a1aa111aaaaaa1aa1aaaa/pages/100001/Example+Page",
    "version": "2"
  }
}
```

#### Get Page By ID

This action is used to retrieve confluence page by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page_id|string|None|True|The ID of a page for content to be returned|None|100001|
  
Example input:

```
{
  "page_id": 100001
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|False|Indicates whether the page content was found or not, true if found|True|
|page|page|False|Returned page object data|{"content":"<p>ExampleContent</p>","contentStatus":"current","created":"2000-01-01T00:00:00.000Z","creator":"ExampleUser","current":true,"homePage":false,"id":"100001","modified":"2000-01-01T00:00:00.000Z","space":"ExampleSpace","title":"ExamplePage","url":"https://test.atlassian.net/wiki/spaces/~1111111a111aaaaa11a1aa111aaaaaa1aa1aaaa/pages/100001/Example+Page","version":"2"}|
  
Example output:

```
{
  "found": true,
  "page": {
    "content": "<p>ExampleContent</p>",
    "contentStatus": "current",
    "created": "2000-01-01T00:00:00.000Z",
    "creator": "ExampleUser",
    "current": true,
    "homePage": false,
    "id": "100001",
    "modified": "2000-01-01T00:00:00.000Z",
    "space": "ExampleSpace",
    "title": "ExamplePage",
    "url": "https://test.atlassian.net/wiki/spaces/~1111111a111aaaaa11a1aa111aaaaaa1aa1aaaa/pages/100001/Example+Page",
    "version": "2"
  }
}
```

#### Get Page Content

This action is used to retrieve the content of a page by its name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page|string|None|True|The page name of the content to be retrieved|None|ExamplePageName|
|space|string|None|True|The name of a space|None|ExampleSpace|
  
Example input:

```
{
  "page": "ExamplePageName",
  "space": "ExampleSpace"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|content|string|False|The content of a page|<p>Example Content</p>|
|found|boolean|False|Indicates whether the page content was found or not, true if found|True|
  
Example output:

```
{
  "content": "<p>Example Content</p>",
  "found": true
}
```

#### Get Page Content By ID

This action is used to retrieve confluence page content by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page_id|string|None|True|The ID of a page for content to be returned|None|100001|
  
Example input:

```
{
  "page_id": 100001
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|content|string|False|The content of a page|<p>Example Content</p>|
|found|boolean|False|Indicates whether the page content was found or not, true if found|True|
  
Example output:

```
{
  "content": "<p>Example Content</p>",
  "found": true
}
```

#### Store Page Content

This action is used to store Page Content, will create a new page if the existing page cannot be found

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|content|string|None|True|Content To Store|None|<p>Example Content</p>|
|page|string|None|True|The page name of the content to be stored|None|ExamplePageName|
|space|string|None|True|The name of a space|None|ExampleSpace|
  
Example input:

```
{
  "content": "<p>Example Content</p>",
  "page": "ExamplePageName",
  "space": "ExampleSpace"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|page|page|False|Returned page object data|{"content":"<p>ExampleContent</p>","contentStatus":"current","created":"2000-01-01T00:00:00.000Z","creator":"ExampleUser","current":true,"homePage":false,"id":"100001","modified":"2000-01-01T00:00:00.000Z","space":"ExampleSpace","title":"ExamplePage","url":"https://test.atlassian.net/wiki/spaces/~1111111a111aaaaa11a1aa111aaaaaa1aa1aaaa/pages/100001/Example+Page","version":"2"}|
  
Example output:

```
{
  "page": {
    "content": "<p>ExampleContent</p>",
    "contentStatus": "current",
    "created": "2000-01-01T00:00:00.000Z",
    "creator": "ExampleUser",
    "current": true,
    "homePage": false,
    "id": "100001",
    "modified": "2000-01-01T00:00:00.000Z",
    "space": "ExampleSpace",
    "title": "ExamplePage",
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

* 2.0.1 - Fixed issue where connection test would fail even if credentials entered were correct
* 2.0.0 - Updated `Connection` input to use `Username`, `API Token` and `Cloud` | Replaced existing Atlassian API library | Added new actions `Get Page By ID` and `Get Page Content By ID`
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.3 - Pin Confluence python library at 0.2
* 0.1.2 - SSL bug fix in SDK
* 0.1.1 - Fix bug dumping credentials to log
* 0.1.0 - Initial plugin

# Links

* [Vendor](https://www.atlassian.com)

## References

* [Vendor](https://www.atlassian.com)