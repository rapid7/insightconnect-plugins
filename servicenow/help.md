# Description

[ServiceNow](https://www.servicenow.com/) is a tool for managing incidents and configuration management. This plugin allows users to manage all aspects of incidents including creation, search, and updates. Additionally, incident changes can be monitored and processed for use in a Rapid7 InsightConnect workflow.

Note: This plugin affects only the underlying tables in a ServiceNow instance, not its UI. Hence, this plugin will work seamlessly with Virtual Task Boards.

# Key Features

* Search, Read, Create, Delete, and Update incidents to accelerate ticketing operations
* Search, Get, Put, and Delete incident attachments to update tickets with additional context
* Search, Get, Create, and Update CI records to manage your configuration items

# Requirements

* ServiceNow username and password
* ServiceNow instance URL

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|client_login|credential_username_password|None|True|The ServiceNow username and password for basic authentication API interaction|None|None|
|timeout|integer|30|False|The interval in seconds before abandoning an attempt to access ServiceNow|None|None|
|url|string|None|True|The full URL for your instance of ServiceNow, e.g. https://instance.servicenow.com|None|None|

Example input:

```
```

## Technical Details

### Actions

#### Create CI

This action is used to create a new ServiceNow CI record.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|create_data|object|None|True|JSON object containing the fields and values to create a new CI|None|None|
|table|string|None|True|The ServiceNow table where the new CI record will be inserted|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|system_id|string|True|System ID of the new CI created|

Example output:

```
{
  "system_id": "45dd2115db1ebf00a7e99b3c8a9619da"
}
```

#### Create Incident

This action is used to create a new ServiceNow Incident record.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|create_data|object|None|False|JSON object containing the fields and values to create a new incident|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|number|string|True|Incident ticket number|
|system_id|string|True|System ID of the new Incident created|

Example output:

```
{
  "system_id": "daa10e5ddb5ef7002e12ff00ba9619db"
}
```

#### Delete Incident

This action is used to remove the given ServiceNow Incident from the instance.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|system_id|string|None|True|System ID of the Incident record to delete|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|True if the deletion was successful, false otherwise|

Example output:

```
{
  "success": true
}
```

#### Delete Incident Attachment

This action is used to remove the given attachment from the ServiceNow instance.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|attachment_id|string|None|True|System ID of the attachment to delete|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|True if the deletion was successful, false otherwise|

Example output:

```
{
  "success": true
}
```

#### Get CI

This action is used to retrieve a ServiceNow CI record based on provided query.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|system_id|string|None|True|The system ID of the record to retrieve|None|None|
|table|string|None|True|The ServiceNow table to retrieve the CI from|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|servicenow_ci|object|True|JSON object representing the CI record returned|

Example output:

```
{
  "servicenow_ci": {
    "firewall_status": "Intranet",
    "operational_status": "1",
    "sys_updated_on": "2019-06-26 20:45:21",
    "first_discovered": "2018-05-14 18:07:23",
    "used_for": "Production",
    "sys_created_by": "admin",
    "classification": "Production",
    "can_print": "false",
    "last_discovered": "2019-03-24 11:25:56",
    "sys_class_name": "cmdb_ci_server",
    "asset": {
      "link": "https://example.service-now.com/api/now/table/alm_asset/ff5a6a55dbdef7002e12ff00ba9619d6",
      "value": "ff5a6a55dbdef7002e12ff00ba9619d6"
    },
    "sys_updated_by": "admin",
    "sys_created_on": "2019-06-26 20:45:21",
    "sys_domain": {
      "link": "https://example.service-now.com/api/now/table/sys_user_group/sysdomain",
      "value": "sysdomain"
    },
    "fqdn": "fqdntest",
    "hardware_status": "installed",
    "install_status": "1",
    "name": "TEST NAME",
    "subcategory": "Computer",
    "u_restricted_access": "false",
    "sys_id": "375a6a55dbdef7002e12ff00ba9619d6",
    "sys_class_path": "/!!/!G/!!/!$",
    "mac_address": "234324234342",
    "u_automated_patching": "false",
    "sys_mod_count": "0",
    "monitor": "false",
    "ip_address": "10.0.0.1",
    "model_id": {
      "link": "https://example.service-now.com/api/now/table/cmdb_model/59d4c676db0fc700553363835b961949",
      "value": "59d4c676db0fc700553363835b961949"
    },
    "cost_cc": "USD",
    "location": {
      "link": "https://example.service-now.com/api/now/table/cmn_location/US-East",
      "value": "US-East"
    },
    "category": "Hardware",
    "fault_count": "0"
  }
}
```

#### Get Incident Attachment

This action is used to download the Base64-encoded contents of the given attachment.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|attachment_id|string|None|True|System ID of the attachment to copy|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|attachment_contents|string|True|The Base64-encoded contents of the downloaded attachment|

Example output:

```
{
  "attachment_contents": [base-64 contents]
}
```

#### Put Incident Attachment

This action is used to associate a file with a ServiceNow Incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|attachment_name|string|None|True|Name of the attachment in the ServiceNow instance|None|None|
|base64_content|bytes|None|True|Content of the attachment, encoded into Base64|None|None|
|mime_type|string|None|True|MIME type (a.k.a. content type) of the file to be attached|['text/plain (.txt)', 'text/html (.html)', 'application/rtf (.rtf)', 'application/pdf (.pdf)', 'application/msword (.doc)', 'application/vnd.ms-powerpoint (.ppt)', 'image/bmp (.bmp)', 'image/gif (.gif)', 'image/jpeg (.jpg)', 'image/png (.png)', 'image/tiff (.tiff)', 'OTHER']|None|
|other_mime_type|string|None|False|User-specified MIME type not in the enumerated list|None|None|
|system_id|string|None|True|System ID of the Incident record to which the file will be attached|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|attachment_id|string|True|System ID of the newly created attachment|

Example output:

```
{
  "attachment_id": "b5b24a5ddb1ebf00a7e99b3c8a96197d"
}
```

#### Read Incident

This action is used to populate a JSON object with the specified fields of the given Incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filtering_fields|string|None|True|Comma-separated list of fields desired in output object (e.g. opened_by,number)|None|None|
|system_id|string|None|True|System ID of the Incident record from which to read|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|filtered_incident|object|True|JSON object representing the incident containing the given fields|

Example output:

```
{
  "filtered_incident": {
    "short_description": "Short description test",
    "description": "Description test"
  }
}
```

#### Search CI

This action is used to retrieve CI record(s) from ServiceNow based on the provided query.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|Non-encoded query string for retrieving ServiceNow CI record(s) (e.g. number=INC0000055^ORshort_description=New bug)|None|None|
|table|string|None|True|The ServiceNow table to execute the query against|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|servicenow_cis|[]object|True|List of JSON objects representing the CI record(s) returned by the query|

Example output:

```
{
  "servicenow_cis": [
    {
      "firewall_status": "Intranet",
      "operational_status": "1",
      "sys_updated_on": "2019-06-26 20:45:21",
      "first_discovered": "2018-05-14 18:07:23",
      "used_for": "Production",
      "sys_created_by": "admin",
      "classification": "Production",
      "can_print": "false",
      "last_discovered": "2019-03-24 11:25:56",
      "sys_class_name": "cmdb_ci_server",
      "cd_rom": "false",
      "unverified": "false",
      "asset": {
        "link": "https://example.service-now.com/api/now/table/alm_asset/ff5a6a55dbdef7002e12ff00ba9619d6",
        "value": "ff5a6a55dbdef7002e12ff00ba9619d6"
      },
      "skip_sync": "false",
      "sys_updated_by": "admin",
      "sys_created_on": "2019-06-26 20:45:21",
      "sys_domain": {
        "link": "https://example.service-now.com/api/now/table/sys_user_group/sysdomain",
        "value": "sysdomain"
      },
      "fqdn": "fqdntest",
      "hardware_status": "installed",
      "install_status": "1",
      "name": "TEST NAME",
      "subcategory": "Computer",
      "u_restricted_access": "false",
      "virtual": "false",
      "sys_id": "375a6a55dbdef7002e12ff00ba9619d6",
      "sys_class_path": "/!!/!G/!!/!$",
      "mac_address": "234324234342",
      "u_automated_patching": "false",
      "sys_mod_count": "0",
      "monitor": "false",
      "ip_address": "10.0.0.1",
      "model_id": {
        "link": "https://example.service-now.com/api/now/table/cmdb_model/59d4c676db0fc700553363835b961949",
        "value": "59d4c676db0fc700553363835b961949"
      },
      "cost_cc": "USD",
      "location": {
        "link": "https://example.service-now.com/api/now/table/cmn_location/US-East",
        "value": "US-East"
      },
      "category": "Hardware",
      "fault_count": "0"
    }
  ]
```

#### Search Incident

This action is used to search for Incidents satisfying the given query.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|Non-encoded query string (e.g. number=INC0000055^ORshort_description=New bug)|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|system_ids|[]string|True|List of System IDs of Incidents satisfying the given query|

Example output:

```
{
  "system_ids": [
    "b5aadf6cdb16b7002e12ff00ba96193c",
    "90db5f20db967f00a7e99b3c8a96190c",
    "28869809db12bf00a7e99b3c8a9619de",
    "e5a14141db92f7002e12ff00ba961962",
    "38aa01d9dbdaf7002e12ff00ba96196a",
    "daa10e5ddb5ef7002e12ff00ba9619db"
  ]
}
```

#### Search Incident Attachment

This action is used to search for attachment files with the given name.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|Name of the attachment, i.e. the base file name used to create it|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|attachment_ids|[]string|True|List of System IDs of attachment records with the given name|

Example output:

```
{
  "attachment_ids": [
    "7bbbc15ddbdaf7002e12ff00ba96196c",
    "b5b24a5ddb1ebf00a7e99b3c8a96197d",
    "46c14941db92bf00a7e99b3c8a9619b6"
  ]
}
```

#### Update CI

This action is used to update an existing ServiceNow CI record.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|system_id|string|None|True|System ID of the CI record to update|None|None|
|table|string|None|True|The ServiceNow table where the CI record will be updated|None|None|
|update_data|object|None|True|JSON object containing the fields and values to perform a CI update|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|True if the update was successful|

Example output:

```
{
  "success": true
}
```

#### Update Incident

This action is used to update a ServiceNow Incident with the given data.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|system_id|string|None|True|System ID of the Incident record to update|None|None|
|update_data|object|None|True|JSON object containing the fields and values to update|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|True if the update was successful|

Example output:

```
{
  "success": true
}
```

#### Get Incident Comments and Work Notes

This action is used to get comments and work notes for an incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|system_id|string|None|True|System ID of Incident record for which comments and work notes will be retrieved|None|None|
|type|string|None|True|Type of output to be retrieved|['all', 'comments', 'work notes']|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident_comments_worknotes|[]comments_worknotes|True|List of comments and work notes for an incident|

Example output:

```
    {
      "incident_comments_worknotes": [
        {
          "sys_id": "2c6420c31b0000506a4a85507e4bcb82",
          "sys_created_on": "2019-09-26 21:19:11",
          "name": "incident",
          "element_id": "965f140bdb4c8c105f6f00b5ca961922",
          "sys_tags": "",
          "value": "Team is actively looking into it.",
          "sys_created_by": "admin",
          "element": "work_notes"
        },
        {
          "sys_id": "4db0e8cb1bcccc106a4a85507e4bcba2",
          "sys_created_on": "2019-09-26 21:03:07",
          "name": "incident",
          "element_id": "965f140bdb4c8c105f6f00b5ca961922",
          "sys_tags": "",
          "value": "This is Sev1 incident.",
          "sys_created_by": "admin",
          "element": "comments"
        },
        {
          "sys_id": "f92024471b0000506a4a85507e4bcb78",
          "sys_created_on": "2019-09-26 21:00:43",
          "name": "incident",
          "element_id": "965f140bdb4c8c105f6f00b5ca961922",
          "sys_tags": "",
          "value": "Testing comments",
          "sys_created_by": "admin",
          "element": "comments"
        }
      ]
    }
```

### Triggers

#### Incident Added

This trigger identifies if a new incident has been added.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|interval|integer|5|False|How often to detect new incidents (in seconds)|None|5|
|query|string|None|False|Non-encoded query string to match incident records|None|short_description=Newbug|

Example input:

```
{
  "interval": 5,
  "query": "short_description=Newbug"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|system_id|string|True|System ID of new incident|

Example output:

```
{
  "system_id": "45dd2115db1ebf00a7e99b3c8a9619da"
}
```

#### Incident Changed

This trigger reports changes of the given fields in the given Incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|interval|integer|5|False|How often to detect changes to the given Incident (in minutes)|None|None|
|monitored_fields|string|None|True|Comma-separated list of fields to be monitored (e.g. resolved,resolved_by)|None|None|
|system_id|string|None|True|System ID of the Incident record to monitor|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|changed_fields|object|True|JSON object representing changed fields (map of field name to previous and current values)|

Example output:

```
{
  "changed_fields": {
    "description": {
      "previous": "Description 1",
      "current": "Description 2"}
    }
}
```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 4.1.0 - Add trigger Incident Added
* 4.0.0 - New Number output to create incidient action
* 3.1.1 - New spec and help.md format for the Extension Library
* 3.1.0 - Add action Get Incident Comments and Work Notes
* 3.0.0 - Rewrite in Python | Renamed incident specific actions | New actions Create CI, Get CI, Update CI, Search CI
* 2.0.5 - Update descriptions
* 2.0.4 - Regenerate with latest Go SDK to solve bug with triggers
* 2.0.3 - Fixing the loss of metadata in action messages
* 2.0.2 - Disable Connection Caching
* 2.0.1 - Pull the ConnectionCacheKey update from SDK 2.6.3
* 2.0.0 - Update to new credential types
* 1.0.0 - Support web server mode
* 0.1.1 - Bug fix for CI tool incorrectly uploading plugins
* 0.1.0 - Initial plugin

# Links

## References

* [ServiceNow](https://www.servicenow.com/)
* [ServiceNow API](https://developer.servicenow.com/app.do#!/rest_api_doc?v=fuji&id=c_TableAPI)
* [ServiceNow User Administration](http://wiki.servicenow.com/index.php?title=User_Administration)
* [ServiceNow Operators](http://wiki.servicenow.com/index.php?title=Operators_Available_for_Filters_and_Queries)

