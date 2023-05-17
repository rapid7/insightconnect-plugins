########################################################################################



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

* 2023-05-17

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|False|An optional API key for authentication via bearer token|None|9de5069c5afe602b2ea0a04b66beb2c0|
|credentials|credential_username_password|None|False|Username and password|None|None|
|host|string|None|True|TheHive host|None|https://example.com or https://example.com|
|port|string|9000|True|TheHive API port|None|9000|
|protocol|string|None|True|HTTP Protocol|['http', 'https']|http|
|proxy|object|None|False|An optional dictionary containing proxy data, with HTTP or HTTPS as the key, and the proxy URL as the value|None|None|
|verify|boolean|True|True|Verify the certificate|None|True|

Example input:

```

```
## Technical Details

### Actions

#### Get User by ID

This action is used to get information about a specific user.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|The ID of the user|None|50|

Example input:

```
{
  "id": 50
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|userObject|False|A user object containing all related fields|

Example output:

```
```

#### Get Current User

This action is used to get information about the current user.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|userObject|False|A user object containing all related fields|

Example output:

```
```

#### Close Case
Close a case by ID
##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|force|boolean|False|False|True to physically delete the case, False to mark the case as delete|None|False|
|id|string|None|True|ID for the case|None|50|

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
|customFields|object|None|False|Case custom fields|None|None|
|description|string|None|False|Description of the case, supports markdown|None|Case description|
|flag|boolean|False|False|Case's flag, True to mark case as important|None|True|
|jsonData|object|None|False|If the field is not equal to None, the case is instantiated using the JSON value instead of the arguements|None|None|
|metrics|object|None|False|Case metrics collection. A JSON object where keys are defining metric name, and values are defining metric value|None|None|
|owner|string|None|False|Case's assignee|None|admin|
|pap|integer|2|False|Password Authentication Protocol|[0, 1, 2, 3]|2|
|severity|integer|2|False|Case severity|[1, 2, 3, 4]|2|
|startDate|integer|None|False|Case start date (datetime in ms) (will default to now if left blank)|None|1684170163000|
|summary|string|None|False|Case summary|None|Case summary|
|tags|[]string|None|False|List of case tags|None|["case_tag_1", "case_tag_2"]|
|tasks|[]itask|None|False|Case task|None|None|
|template|string|None|False|Case template's name. If specified then the case is created using the given template|None|Case template name|
|title|string|None|False|Name of the case|None|Case title|
|tlp|integer|2|False|Traffic Light Protocol level|[0, 1, 2, 3]|2|

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
|data|string|None|False|Observable's data|None|Test data for observable|
|datatype|string|None|False|Observables Data Type|None|domain, ip, url, fqdn, uri_path, user-agent, hash, email, mail, mail_subject, registry, regexp, other|
|id|string|None|False|ID for the case|None|AYgQXmjbfMffAh_St-fk|
|ignoreSimilarity|boolean|False|False|Observable's similarity ignore flag. True to ignore the observable during similarity computing|None|False|
|ioc|boolean|False|False|Observable's IOC, True to mark an observable as IOC|None|False|
|jsonData|object|None|False|All fields included in one JSON object. If using this, all other fields will be ignored|None|json object containing all necessary fields|
|message|string|None|False|Observable's description. If tags is empty, this is required|None|Observable message|
|pap|integer|2|False|Case's PAP|[0, 1, 2, 3]|2|
|sighted|boolean|False|False|Observable's sighted flag, True to mark the observable as sighted|None|False|
|startDate|integer|None|False|Observable start date (timestamp in ms)|None|1640000000000|
|tags|[]string|None|False|List of observable tags, required if message is None|None|["tag_one", "tag_two"]|
|tlp|integer|2|False|Case's TLP|[0, 1, 2, 3]|2|

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
{
  "data": "Test data for observable",
  "datatype": "domain, ip, url, fqdn, uri_path, user-agent, hash, email, mail, mail_subject, registry, regexp, other",
  "id": "AYgQXmjbfMffAh_St-fk",
  "ignoreSimilarity": false,
  "ioc": false,
  "jsonData": "json object containing all necessary fields",
  "message": "Observable message",
  "pap": 2,
  "sighted": false,
  "startDate": 1640000000000,
  "tags": [
    "tag_one",
    "tag_two"
  ],
  "tlp": 2
}
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
|description|string|None|False|Task's description|None|Task description|
|flag|boolean|False|False|Task's flag, 'True' to mark the task as important|None|False|
|id|string|None|False|ID for the case|None|AYgQXmjbfMffAh_St-fk|
|jsonData|object|None|False|If the field is not equal to None, the Task is instantiated using the JSON value instead of the arguements|None|json object containing all necessary fields|
|owner|string|None|False|Task's assignee|None|admin|
|startDate|integer|None|False|Task's start date, the date the task started at|None|1684170163000|
|status|string|Waiting|False|Task's status|['Waiting', 'InProgress', 'Cancel', 'Completed']|Waiting|
|title|string|None|False|Task's title|None|Task title|

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
{
  "description": "Task description",
  "flag": false,
  "id": "AYgQXmjbfMffAh_St-fk",
  "jsonData": "json object containing all necessary fields",
  "owner": "admin",
  "startDate": 1684170163000,
  "status": "Waiting",
  "title": "Task title"
}
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
|id|string|None|True|ID for the case|None|50|

```
{
  "id": ""
}
```
Example input:

```
{
  "id": 50
}
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

* 3.0.0 - Action: `Get Cases` removed. | Action: `Get User` made into two new actions, `Get User By ID` & `Get Current User`. | Refactor: All code refactored & thehive4py dependency removed. | Connection: Fixed issue where connection fails on SSL verify & added API key input.
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

