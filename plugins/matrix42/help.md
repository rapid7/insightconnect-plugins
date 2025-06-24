# Description

[Matrix42](https://www.matrix42.com/) is a platform for IT service and asset management. This plugin allows users to create incidents and service requests within Matrix42


# Key Features

* Create new incidents in Matrix42.

# Requirements

* Matrix42 API URL
* Matrix42 API key

# Supported Product Versions

* Matrix42 Service Desk

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|Matrix42 API key for authentication|None|eyJhbGciOiJodHR...|None|None|
|api_url|string|None|True|The base URL for your Matrix42 API (e.g. https://testsrv.imagoverum.com/m42Services/api/)|None|https://testsrv.imagoverum.com/m42Services/api/|None|None|

Example input:

```
{
  "api_key": "eyJhbGciOiJodHR...",
  "api_url": "https://testsrv.imagoverum.com/m42Services/api/"
}
```

## Technical Details

### Actions


#### Create Ticket

This action is used to create a new Matrix42 Ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|activity_type|string|None|True|Type of the ticket. (Incident or Service Request)|["Incident", "Service Request"]|Service Request|None|None|
|additional_fields|object|None|False|JSON object containing additional fields and values to create the ticket|None|{ "Impact": 1, "Subject": Replace Subject, "Urgency": 1 }|None|None|
|description_html|string|None|True|HTML formatted description|None|<h1>New Ticket</h1><p>This is an example ticket description.</p>|None|None|
|subject|string|None|True|Title of the ticket|None|Example Ticket Title|None|None|
  
Example input:

```
{
  "activity_type": "Service Request",
  "additional_fields": "{ \"Impact\": 1, \"Subject\": Replace Subject, \"Urgency\": 1 }",
  "description_html": "<h1>New Ticket</h1><p>This is an example ticket description.</p>",
  "subject": "Example Ticket Title"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|string|True|ID of the new ticket|3cd186d8-3f46-f021-1687-000f2aed481c|
  
Example output:

```
{
  "id": "3cd186d8-3f46-f021-1687-000f2aed481c"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.0.0 - Initial plugin

# Links

* [Matrix42](https://www.matrix42.com/)

## References

* [Matrix42](https://www.matrix42.com/)
* [Matrix42 API Documentation](https://help.matrix42.com/030_ESMP/030_INT/Business_Processes_and_API_Integrations/Public_API_reference_documentation)