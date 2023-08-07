# Description

TheHive is a scalable, open source security incident response solution designed for SOCs & CERTs to collaborate, 
elaborate, analyze and get their job done

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
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|False|An optional API key for authentication via bearer token|None|9de5069c5afe602b2ea0a04b66beb2c0|
|credentials|credential_username_password|None|False|Username and password|None|{}|
|host|string|None|True|TheHive host|None|thehive.company.com or 10.3.4.50|
|port|string|9000|True|TheHive API port|None|9000|
|protocol|string|None|True|HTTP Protocol|['http', 'https']|http|
|proxy|object|None|False|An optional dictionary containing proxy data, with HTTP or HTTPS as the key, and the proxy URL as the value|None|{}|
|verify|boolean|True|True|Verify the certificate|None|True|
  
Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "credentials": {},
  "host": "thehive.company.com or 10.3.4.50",
  "port": 9000,
  "protocol": "http",
  "proxy": {},
  "verify": true
}
```

## Technical Details

### Actions

#### Close Case
  
Close a case by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|force|boolean|False|False|True to physically delete the case, False to mark the case as delete|None|False|
|id|string|None|True|ID for the case|None|50|
  
Example input:

```
{
  "force": false,
  "id": 50
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Boolean to indicate if the operation was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Create Case
  
Create a new case

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|customFields|object|None|False|Case custom fields|None|{}|
|description|string|None|False|Description of the case, supports markdown|None|Case description|
|flag|boolean|False|False|Case's flag, True to mark case as important|None|True|
|jsonData|object|None|False|If the field is not equal to None, the case is instantiated using the JSON value instead of the arguements|None|{}|
|metrics|object|None|False|Case metrics collection. A JSON object where keys are defining metric name, and values are defining metric value|None|{}|
|owner|string|None|False|Case's assignee|None|admin|
|pap|integer|2|False|Password Authentication Protocol|[0, 1, 2, 3]|2|
|severity|integer|2|False|Case severity|[1, 2, 3, 4]|2|
|startDate|integer|None|False|Case start date (datetime in ms) (will default to now if left blank)|None|1684170163000|
|summary|string|None|False|Case summary|None|Case summary|
|tags|[]string|None|False|List of case tags|None|['case_tag_1', 'case_tag_2']|
|template|string|None|False|Case template's name. If specified then the case is created using the given template|None|Case template name|
|title|string|None|True|Name of the case|None|Case title|
|tlp|integer|2|False|Traffic Light Protocol level|[0, 1, 2, 3]|2|
  
Example input:

```
{
  "customFields": {},
  "description": "Case description",
  "flag": false,
  "jsonData": {},
  "metrics": {},
  "owner": "admin",
  "pap": 2,
  "severity": 2,
  "startDate": 1684170163000,
  "summary": "Case summary",
  "tags": "case_tag_1",
  "template": "Case template name",
  "title": "Case title",
  "tlp": 2
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|case|createCase|False|Create case output|{'owner': 'string', 'summary': 'string', 'severity': 2, '_routing': 'case_id', 'flag': False, 'endDate': 1640000000000, 'customFields': {}, '_type': 'case', 'description': 'string', 'title': 'string', 'tags': ['string'], 'createdAt': 1684188238010, '_parent': None, 'createdBy': 'admin', 'caseId': 54, 'tlp': 2, 'metrics': {}, '_id': 'case_id', 'id': 'case_id', '_version': 1, 'pap': 2, 'startDate': 1640000000000, 'status': 'Open'}|
  
Example output:

```
{
  "case": {
    "_id": "case_id",
    "_parent": null,
    "_routing": "case_id",
    "_type": "case",
    "_version": 1,
    "caseId": 54,
    "createdAt": 1684188238010,
    "createdBy": "admin",
    "customFields": {},
    "description": "string",
    "endDate": 1640000000000,
    "flag": false,
    "id": "case_id",
    "metrics": {},
    "owner": "string",
    "pap": 2,
    "severity": 2,
    "startDate": 1640000000000,
    "status": "Open",
    "summary": "string",
    "tags": [
      "string"
    ],
    "title": "string",
    "tlp": 2
  }
}
```

#### Create Observable
  
Create a new case observable

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|data|string|None|False|Observable's data|None|Test data for observable|
|datatype|string|None|False|Observables Data Type|None|domain, ip, url, fqdn, uri_path, user-agent, hash, email, mail, mail_subject, registry, regexp, other|
|id|string|None|False|ID for the case|None|AYgQXmjbfMffAh_St-fk|
|ignoreSimilarity|boolean|False|False|Observable's similarity ignore flag. True to ignore the observable during similarity computing|None|False|
|ioc|boolean|False|False|Observable's IOC, True to mark an observable as IOC|None|False|
|jsonData|object|None|False|All fields included in one JSON object. If using this, all other fields will be ignored|None|json object containing all necessary fields|
|message|string|None|False|Observable's description. If tags is empty, this is required|None|Observable message|
|pap|integer|2|False|Case's PAP|[0, 1, 2, 3]|2|
|sighted|boolean|False|False|Observable's sighted flag, True to mark the observable as sighted|None|False|
|startDate|integer|None|False|Observable start date (datetime in ms) (will default to now if left blank)|None|1640000000000|
|tags|[]string|None|False|List of observable tags, required if message is None|None|['tag_one', 'tag_two']|
|tlp|integer|2|False|Case's TLP|[0, 1, 2, 3]|2|
  
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
  "tags": "tag_one",
  "tlp": 2
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|case|observable|False|Create case observable output|{'data': 'Test data for observable', 'datatype': 'domain, ip, url, fqdn, uri_path, user-agent, hash, email, mail, mail_subject, registry, regexp, other', 'id': 'AYgQXmjbfMffAh_St-fk', 'ignoreSimilarity': False, 'ioc': False, 'jsonData': 'json object containing all necessary fields', 'message': 'Observable message', 'pap': 2, 'sighted': False, 'startDate': 1640000000000, 'tags': 'tag_one', 'tlp': 2}|
  
Example output:

```
{
  "case": {
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
    "tags": "tag_one",
    "tlp": 2
  }
}
```

#### Create Task
  
Create a new case task

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|False|Task's description|None|Task description|
|flag|boolean|False|False|Task's flag, 'True' to mark the task as important|None|False|
|id|string|None|False|ID for the case|None|AYgQXmjbfMffAh_St-fk|
|jsonData|object|None|False|If the field is not equal to None, the Task is instantiated using the JSON value instead of the arguements|None|json object containing all necessary fields|
|owner|string|None|False|Task's assignee|None|admin|
|startDate|integer|None|False|Task's start date (datetime in ms) (will default to now if left blank)|None|1684170163000|
|status|string|Waiting|False|Task's status|['Waiting', 'InProgress', 'Cancel', 'Completed']|Waiting|
|title|string|None|False|Task's title|None|Task title|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|case|task|False|Create case task output|{'Created At': {}, 'Created By': {}, 'ID': {}, 'Start Date': 0, 'Type': {}, 'description': {}, 'flag': 'true', 'order': {}, 'owner': {}, 'status': 'Waiting', 'title': {}, 'user': {}}|
  
Example output:

```
{
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
```

#### Get Case
  
Retrieve a case by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|ID for the case|None|50|
  
Example input:

```
{
  "id": 50
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|case|case|True|Get case output|{}|
  
Example output:

```
{
  "case": {
    "Alert Date": {},
    "Alert Imported Date": {},
    "Alert In Progress Date": {},
    "Alert New Date": {},
    "Assignee": {},
    "Case title": {},
    "Closed Date": {},
    "Created At": 0,
    "Created By": {},
    "Custom Fields": {},
    "Description": {},
    "End Date": {},
    "Extra Data": {},
    "Flag": "true",
    "Handling Duration": {},
    "ID": "",
    "Impact Status": {},
    "In Progress Date": {},
    "New Date": {},
    "Number": {},
    "PAP": {},
    "Severity": {},
    "Stage": {},
    "Start Date": {},
    "Status": {},
    "Summary": {},
    "TLP": {},
    "Tags": [
      {}
    ],
    "Time To Acknowledge": {},
    "Time To Detect": {},
    "Time To Qualify": {},
    "Time To Resolve": {},
    "Time To Triage": {},
    "Type": {},
    "Updated At": {},
    "Updated By": {},
    "User Permissions": {}
  }
}
```

#### Get Cases
  
Retrieve list of cases

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|[]case|False|List of cases|{}|
  
Example output:

```
{
  "success": [
    {
      "Alert Date": {},
      "Alert Imported Date": {},
      "Alert In Progress Date": {},
      "Alert New Date": {},
      "Assignee": {},
      "Case title": {},
      "Closed Date": {},
      "Created At": 0,
      "Created By": {},
      "Custom Fields": {},
      "Description": {},
      "End Date": {},
      "Extra Data": {},
      "Flag": "true",
      "Handling Duration": {},
      "ID": "",
      "Impact Status": {},
      "In Progress Date": {},
      "New Date": {},
      "Number": {},
      "PAP": {},
      "Severity": {},
      "Stage": {},
      "Start Date": {},
      "Status": {},
      "Summary": {},
      "TLP": {},
      "Tags": [
        {}
      ],
      "Time To Acknowledge": {},
      "Time To Detect": {},
      "Time To Qualify": {},
      "Time To Resolve": {},
      "Time To Triage": {},
      "Type": {},
      "Updated At": {},
      "Updated By": {},
      "User Permissions": {}
    }
  ]
}
```

#### Get Current User
  
Get information about the current user

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|userObject|False|A user object containing all related fields|{}|
  
Example output:

```
{
  "success": {}
}
```

#### Get User by ID
  
Get information about a specific user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|The ID of the user|None|50|
  
Example input:

```
{
  "id": 50
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|userObject|False|A user object containing all related fields|{}|
  
Example output:

```
{
  "success": {}
}
```

### Triggers
  
*This plugin does not contain any triggers.*

### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**userObject**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|_ID|string|None|False|User ID|None|
|Type|string|None|False|User type|None|
|Created At|integer|None|False|Time the user was created at in milliseconds or epoch|1496561862924|
|Updated By|string|None|False|Created by|None|
|hasKey|boolean|None|False|User has a key|None|
|ID|string|None|False|ID|None|
|name|string|None|False|Name|None|
|preferences|object|None|False|User preferences|None|
|roles|[]string|None|False|Roles|None|
|status|string|None|False|Get user status|None|
|Updated At|integer|None|False|Time the user was updated in milliseconds or epoch|1496561862924|
|Updated By|string|None|False|Updated by|None|
|user|string|None|False|User|None|
  
**case**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created At|integer|None|False|Datetime in ms the case was created at|None|
|Created By|string|None|False|Who the case was created by|None|
|Type|string|None|False|Case type|None|
|Updated At|integer|None|False|Datetime in ms the case was updated at|None|
|Updated By|string|None|False|Who the case was updated by|None|
|Alert Date|integer|None|False|Case alert date (datetime in ms)|None|
|Alert Imported Date|integer|None|False|Case alert imported date (datetime in ms)|None|
|Alert In Progress Date|integer|None|False|Case alert in progress data (datetime in ms)|None|
|Alert New Date|integer|None|False|Case alert new date (datetime in ms)|None|
|Assignee|string|None|False|None|None|
|Closed Date|integer|None|False|Case closed date (datetime in ms)|None|
|Custom Fields|object|None|False|Case custom fields|None|
|Description|string|None|False|The description of the case|None|
|End Date|integer|None|False|Case end date (datetime in ms)|None|
|Extra Data|object|None|False|None|None|
|Flag|boolean|None|False|Something here|None|
|Handling Duration|integer|None|False|Case handling duration|None|
|ID|string|None|False|ID|None|
|Impact Status|string|None|False|None|None|
|In Progress Date|integer|None|False|None|None|
|New Date|integer|None|False|None|None|
|Number|integer|None|False|An incremental number to reference the case|None|
|PAP|integer|None|False|Password Authenitcation Protocol|None|
|Severity|integer|None|False|Severity of the case|None|
|Stage|string|None|False|The value of the stage depends on the status of the case|None|
|Start Date|integer|None|False|Case start date (datetime in ms)|None|
|Status|string|None|False|Status of the case|None|
|Summary|string|None|False|Summary of the case|None|
|Tags|[]string|None|False|Case tags|None|
|Time To Acknowledge|integer|None|False|Case time to acknowledge|None|
|Time To Detect|integer|None|False|Case time to detect|None|
|Time To Qualify|integer|None|False|Case time to qualify|None|
|Time To Resolve|integer|None|False|Case time to resolve|None|
|Time To Triage|integer|None|False|None|None|
|Case title|string|None|False|Title of the case|None|
|TLP|integer|None|False|Traffic Light Protocol level|None|
|User Permissions|[]string|None|False|A list of permissions the current user has access on the case|None|
  
**createCase**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assignee|string|None|False|User to assign the case to|None|
|Case Template|string|None|False|Name or ID of the case template to use|None|
|Custom Fields|object|None|False|Custom fields|None|
|Description|string|None|False|Case description|None|
|End Date|integer|None|False|Case end date (datetime in ms)|None|
|Flag|boolean|False|False|Case flags|None|
|Observable Rule|string|None|False|Case observable rule|None|
|Password Authentication Protocol|integer|2|False|Case password authentication protocol|None|
|Severity|integer|2|False|Case severity|None|
|Sharing Parameters|[]string|None|False|Case sharing parameters|None|
|Start Date|integer|None|False|Case start date (datetime in ms)|None|
|Status|string|New|False|Case status|None|
|Summary|string|None|False|Case summary|None|
|Tags|[]string|None|False|Case tags|None|
|Task Rule|string|None|False|Case task rule|None|
|Tasks|[]string|None|False|Tasks to create. If null, tasks from the case template will be used|None|
|Title|string|None|False|Case title|None|
|Traffic Light Protocol|integer|2|False|Case traffic light protocol|None|
  
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
|Created At|integer|None|None|Time the observable was created at in milliseconds or epoch|1496561862924|
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

* 4.0.1 - Connection: Added a functional test | Permissions: Changed permissions to `root` and pointed to SSL certs folder in `Dockerfile`.
* 4.0.0 - Added additional error handling for issues that occur outside the expected status codes | Action: `create_case` remade to not include task input
* 3.0.0 - Refactored plugin | Removed `thehive4py` dependency | Action: Split `get_user` into two new actions, `get_user_by_id` & `get_current_user`
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

* [TheHive](https://thehive-project.org/)

## References

* [thehive4py docs](https://github.com/TheHive-Project/TheHive4py/blob/master/thehive4py/api.py)
