##



# Description
  
TheHive is a scalable, open source security incident response solution designed for SOCs & CERTs to collaborate, 
elaborate, analyze and get their job done. Handle your case management needs with TheHive plugin for Rapid7 
InsightConnect
# Key Features

* Retrieve a list of cases or a specific case by ID
* Create a new case and close an existing case
* Create new tasks within a case
* Create new observables within a case
* Get user information

# Requirements

* TheHive instance hostname
* TheHive username and password

# Supported Product Versions

_There are no supported product versions listed._

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|False|An optional API key for authentication via bearer token|None|None|
|credentials|credential_username_password|None|False|Username and password|None|None|
|host|string|None|True|TheHive host e.g. thehive.company.com or 10.3.4.50|None|None|
|port|string|9000|True|TheHive API port e.g. 9000|None|None|
|protocol|string|None|True|HTTP Protocol|['http', 'https']|None|
|proxy|object|None|False|An optional dictionary containing proxy data, with HTTP or HTTPS as the key, and the proxy URL as the value|None|None|
|verify|boolean|True|True|Verify the certificate|None|None|

Example input:

```
```
## Technical Details

### Actions

#### Close Case
Close a case by ID
##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Case ID e.g. AV_ajI_oYMfcbXhqb9tS|None|None|
|impact_status|string|None|False|Case impact status|['low', 'medium', 'high']|None|
|resolution_status|string|None|False|Case resolution status|['low', 'medium', 'high']|None|
|summary|string|None|False|Case Summary|None|None|

```
{
  "id": "",
  "impact_status": "low",
  "resolution_status": "low",
  "summary": ""
}
```
Example input:

```
```

##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|message|string|None|True|Closed case message|None|None|
|type|string|None|True|Closed case type|None|None|
  
Example output:

```
{
  "message": "",
  "type": ""
}
```
#### Create Case
Create a new case
##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assignee|string|None|False|User to assign the case to|None|None|
|caseTemplate|string|None|False|Name or id of the case template to use|None|None|
|customFields|object|None|False|Case custom fields|None|None|
|description|string|None|True|Description of the case, supports markdown|None|None|
|endDate|integer|None|False|Case end date (datetime in ms)|None|None|
|flag|boolean|False|False|Flag, default is false|None|None|
|observableRule|string|None|False|Case observable rule|None|None|
|pap|integer|2|False|Password Authentication Protocol|[0, 1, 2, 3]|None|
|severity|integer|2|False|Case severity|[1, 2, 3, 4]|None|
|startDate|integer|None|False|Case start date (datetime in ms)|None|None|
|status|string|New|False|Case status|None|None|
|summary|string|None|False|Case summary|None|None|
|tags|[]string|None|False|List of tags|None|None|
|taskRule|string|None|False|Case task rule|None|None|
|tasks|itask|None|False|Case task|None|None|
|title|string|None|True|Name of the case|None|None|
|tlp|integer|2|False|Traffic Light Protocol level|[0, 1, 2, 3]|None|

```
{
  "customFields": {},
  "description": "",
  "flag": false,
  "tags": [
    ""
  ],
  "task": {
    "description": {},
    "flag": false,
    "owner": {},
    "status": {},
    "title": ""
  },
  "title": "",
  "tlp": 2
}
```
Example input:

```
```

##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|case|case|None|False|Create case output|None|None|
  
Example output:

```
{
  "case": {
    "Case ID e.g. AV_ajI_oYMfcbXhqb9tS": {},
    "Created At": {},
    "Created By": {},
    "Custom Fields": {},
    "ID": {},
    "Start Date": 0,
    "TLP": {},
    "Type": {},
    "description": {},
    "flag": "true",
    "metrics": {},
    "owner": {},
    "severity": {},
    "status": "",
    "tags": [
      {}
    ],
    "title": {},
    "user": {}
  }
}
```
#### Create Observable
Create a new case observable
##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Case ID e.g. AV_ajI_oYMfcbXhqb9tS|None|None|
|observable|iobservable|None|True|Observable|None|None|

```
{
  "id": "",
  "observable": {
    "Data Type": "",
    "ID": {},
    "IOC": false,
    "TLP": 2,
    "message": {},
    "tags": [
      {}
    ]
  }
}
```
Example input:

```
```

##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|case|observable|None|False|Create case observable output|None|None|
  
Example output:

```
{
  "case": {
    "Created At": {},
    "Created By": {},
    "Data Type": {},
    "ID": {},
    "IOC": "true",
    "Start Date": 0,
    "TLP": {},
    "Type": {},
    "data": {},
    "message": {},
    "reports": {},
    "status": "",
    "tags": [
      {}
    ],
    "user": {}
  }
}
```
#### Create Task
Create a new case task
##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Case ID e.g. AV_ajI_oYMfcbXhqb9tS|None|None|
|task|itask|None|True|Task name|None|None|

```
{
  "id": "",
  "task": {
    "description": {},
    "flag": false,
    "owner": {},
    "status": {},
    "title": ""
  }
}
```
Example input:

```
```

##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|case|task|None|False|Create case task output|None|None|
  
Example output:

```
{
  "case": {
    "Created At": {},
    "Created By": {},
    "ID": {},
    "Start Date": 0,
    "Type": {},
    "description": {},
    "flag": "true",
    "order": {},
    "owner": {},
    "status": "Waiting",
    "title": {},
    "user": {}
  }
}
```
#### Get Case
Retrieve a case by ID
##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Case ID e.g. AV_ajI_oYMfcbXhqb9tS|None|None|

```
{
  "id": ""
}
```
Example input:

```
```

##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|case|case|None|True|Get case output|None|None|
  
Example output:

```
{
  "case": {
    "Case ID e.g. AV_ajI_oYMfcbXhqb9tS": {},
    "Created At": {},
    "Created By": {},
    "Custom Fields": {},
    "ID": {},
    "Start Date": 0,
    "TLP": {},
    "Type": {},
    "description": {},
    "flag": "true",
    "metrics": {},
    "owner": {},
    "severity": {},
    "status": "",
    "tags": [
      {}
    ],
    "title": {},
    "user": {}
  }
}
```
#### Get Cases
Retrieve list of cases
##### Input
  
*This action does not contain any inputs.*
Example input:

```
```

##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|list|[]case|None|False|List of cases|None|None|
  
Example output:

```
{
  "list": [
    {
      "Case ID e.g. AV_ajI_oYMfcbXhqb9tS": {},
      "Created At": {},
      "Created By": {},
      "Custom Fields": {},
      "ID": {},
      "Start Date": 0,
      "TLP": {},
      "Type": {},
      "description": {},
      "flag": "true",
      "metrics": {},
      "owner": {},
      "severity": {},
      "status": "",
      "tags": [
        {}
      ],
      "title": {},
      "user": {}
    }
  ]
}
```
#### Get User
Get information about a user
##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|False|User ID. If empty, the current user is used|None|None|

```
{
  "id": ""
}
```
Example input:

```
```

##### Output

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|_id|string|None|False|User _ID|None|None|
|_type|string|None|False|User type|None|None|
|createdAt|integer|None|False|Time the user was created at in milliseconds or epoch, e.g. 1496561862924|None|None|
|createdBy|string|None|False|Created by|None|None|
|hasKey|boolean|None|False|User has a key|None|None|
|id|string|None|False|ID|None|None|
|name|string|None|False|Name|None|None|
|preferences|object|None|False|User preferences|None|None|
|roles|[]string|None|False|Roles|None|None|
|status|string|None|False|Get user status|None|None|
|updatedAt|integer|None|False|Time the user was updated in milliseconds or epoch, e.g. 1496561862924|None|None|
|updatedBy|string|None|False|Updated by|None|None|
|user|string|None|False|User|None|None|
  
Example output:

```
{
  "_id": "",
  "_type": "",
  "createdAt": 0,
  "createdBy": "",
  "hasKey": true,
  "id": "",
  "name": "",
  "preferences": {},
  "roles": [
    ""
  ],
  "status": "",
  "updatedAt": 0,
  "updatedBy": "",
  "user": ""
}
```
### Triggers

_This plugin does not contain any triggers._

### Custom Types
  
**itask**  

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|None|Task description|None|
|flag|boolean|False|None|Task flag, default is false|None|
|owner|string|None|None|Task owner|None|
|status|string|Waiting|None|Task status|None|
|title|string|None|None|Task title|None|
  
**iobservable**  

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|None|The observable's value e.g. badguy.com|None|
|Data Type|string|None|None|Observable data type e.g. domain, ip, url, fqdn, uri_path, user-agent, hash, email, mail, mail_subject, registry, regexp, other|None|
|IOC|boolean|False|None|Indicator of Compromise, default is 2|None|
|message|string|None|None|Observable message|None|
|tags|[]string|None|None|List of observable tags|None|
|TLP|integer|2|None|Traffic Light Protocol level, default is 2|None|
  
**case**  

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Type|string|None|None|Case type|None|
|Case ID e.g. AV_ajI_oYMfcbXhqb9tS|integer|None|None|Case ID|None|
|Created At|integer|None|None|Created at|None|
|Created By|string|None|None|Case created by|None|
|Custom Fields|object|None|None|Case custom fields|None|
|description|string|None|None|None|None|
|flag|boolean|None|None|Case flags|None|
|ID|string|None|None|ID|None|
|metrics|object|None|None|Case metrics|None|
|owner|string|None|None|Case owner|None|
|severity|integer|None|None|Case severity|None|
|Start Date|integer|None|None|Case start date|None|
|status|string|None|None|Case status|None|
|tags|[]string|None|None|Case tags|None|
|title|string|None|None|Case title|None|
|TLP|integer|None|None|Traffic Light Protocol level|None|
|user|string|None|None|Case user|None|
  
**task**  

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Type|string|None|None|Task type|None|
|Created At|integer|None|None|Task created at|None|
|Created By|string|None|None|Task created by|None|
|description|string|None|None|Task description|None|
|flag|boolean|None|None|Task flag|None|
|ID|string|None|None|Task ID|None|
|order|integer|None|None|Task order|None|
|owner|string|None|None|Task owner|None|
|Start Date|integer|None|None|Task start date|None|
|status|string|None|False|Task status|None|
|title|string|None|None|Task title|None|
|user|string|None|None|Task user|None|
  
**observable**  

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|None|Observable _ID|None|
|Type|string|None|None|Observable type|None|
|Created At|integer|None|None|Time the observable was created at in milliseconds or epoch, e.g. 1496561862924|None|
|Created By|string|None|None|Observable created by|None|
|data|string|None|None|Observable data|None|
|Data Type|string|None|None|Observable data type|None|
|ID|string|None|None|Observable ID|None|
|IOC|boolean|None|None|Indicators of Compromise|None|
|message|string|None|None|Observable message|None|
|reports|object|None|None|Observable reports|None|
|Start Date|integer|None|None|Observable start date|None|
|status|string|None|None|Observable status|None|
|tags|[]string|None|None|Observable tags|None|
|TLP|integer|None|None|Traffic Light Protocol level|None|
|user|string|None|None|Observable user|None|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.5 - New spec and help.md format for the Extension Library. Update help key features and fix description capitalisation
* 2.0.4 - Update to use the `komand/python-2-27-slim-plugin` Docker image to reduce plugin size and to support SSL Verify
* 2.0.3 - Fix issue where SSL Verify was not used in actions that utilize requests | Updated test method and moved it to connection
* 2.0.2 - Fix issue where SSL Verify was not used in the connection
* 2.0.1 - Update descriptions
* 2.0.0 - Update to new credential types
* 1.0.0 - Custom Field support added to Create Case action | Support web server mode
* 0.2.0 - Bug fix, add more input variables for Close Case action
* 0.1.2 - Bug fix for constant "waiting" in Status field | Updated to v2 architecture
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [TheHive](https://thehive-project.org/)
* [thehive4py](https://github.com/CERT-BDF/TheHive4py)
* [TheHive API](https://github.com/CERT-BDF/TheHiveDocs/tree/master/api)

