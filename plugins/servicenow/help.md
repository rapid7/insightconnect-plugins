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

# Supported Product Versions

* 2020-03-11 Orlando

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|client_login|credential_username_password|None|True|The ServiceNow username and password for basic authentication API interaction|None|{"username":"user1", "password":"mypassword"}|
|timeout|integer|30|False|The interval in seconds before abandoning an attempt to access ServiceNow|None|30|
|url|string|None|True|The full URL for your instance of ServiceNow, e.g. https://instance.servicenow.com|None|https://instance.servicenow.com|

Example input:

```
{
  "client_login": {
    "username": "user1",
    "password": "mypassword"
  },
  "timeout": 30,
  "url": "https://instance.servicenow.com"
}
```

## Technical Details

### Actions

#### Get Attachments for an Incident

This action is used to search for attachments for a given incident ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|incident_id|string|None|False|ID of the incident|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "incident_id": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident_attachments|[]attachment_file|False|List of attachments for a given incident ID|

Example output:

```
{
  "incident_attachments": [
    {
      "content": "9de5069c5afe602b2ea0a04b66beb2c0",
      "content_type": "text/plain",
      "file_name": "example.txt"
    }
  ]
}
```

#### Create CI

This action is used to create a new ServiceNow CI record.

For more information about the **query** input, please refer to [InsightConnect ServiceNow Query Syntax documentation](http://docs.rapid7.com/insightconnect/servicenow#query-syntax).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|create_data|object|None|True|JSON object containing the fields and values to create a new CI|None|{"Description": "Bug report", "ID": "58", "date": "2021-08-20 18:12:00"}|
|table|string|None|True|The ServiceNow table where the new CI record will be inserted|None|catalog_category_request|

Example input:

```
{
  "create_data": {
    "Description": "Bug report",
    "ID": "58",
    "date": "2021-08-20 18:12:00"
  },
  "table": "catalog_category_request"
}
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
|additional_fields|object|None|False|JSON object containing the additional fields and values to create incident|None|{"description": "incident description"}|
|assigned_to|string|None|False|User ID of person assigned to the incident|None|user|
|assignment_group|string|None|False|Assignment group name of the incident|None|Team Development Code Reviewers|
|business_service|string|None|False|Name of business service|None|All|
|caller|string|None|False|User ID of incident caller|None|user|
|category|string|None|False|Category code of incident|None|software|
|configuration_item|string|None|False|Configuration item code of the incident|None|int-jenkins|
|contact_type|string|None|False|Contact type of the incident|None|email|
|description|string|None|False|Full description of incident|None|Full details about new employee hire|
|impact|string|None|False|Impact of the indicent|None|Medium|
|priority|string|None|False|Priority of the incident|None|Planning|
|short_description|string|None|False|Short description of incident|None|New employee hire|
|state|string|None|False|State name of the incident|None|In Progress|
|subcategory|string|None|False|Subcategory code of incident (available values depends on the `Category` field)|None|email|
|urgency|string|None|False|Urgency of the incident|None|Medium|

Example input:

```
{
  "additional_fields": "{"description": "incident description"}",
  "assigned_to": "user",
  "assignment_group": "Team Development Code Reviewers",
  "business_service": "All",
  "caller": "user",
  "category": "software",
  "configuration_item": "int-jenkins",
  "contact_type": "email",
  "description": "Full details about new employee hire",
  "impact": "Medium",
  "priority": "Planning",
  "short_description": "New employee hire",
  "state": "In Progress",
  "subcategory": "email",
  "urgency": "Medium"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|incident_url|string|True|URL to newly created incident|
|number|string|True|Incident ticket number|
|system_id|string|True|System ID of the new Incident created|

Example output:

```
{
  "number": "123"
  "system_id": "daa10e5ddb5ef7002e12ff00ba9619db"
}
```

#### Delete Incident

This action is used to remove the given ServiceNow Incident from the instance.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|system_id|string|None|True|System ID of the Incident record to delete|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "system_id": "9de5069c5afe602b2ea0a04b66beb2c0"
}
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
|attachment_id|string|None|True|System ID of the attachment to delete|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "system_id": "9de5069c5afe602b2ea0a04b66beb2c0"
}
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
|system_id|string|None|True|The system ID of the record to retrieve|None|9de5069c5afe602b2ea0a04b66beb2c0|
|table|string|None|True|The ServiceNow table to retrieve the CI from|None|catalog_category_request|

Example input:

```
{
  "system_id": "9de5069c5afe602b2ea0a04b66beb2c0",
  "table": "catalog_category_request"
}
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
|attachment_id|string|None|True|System ID of the attachment to copy|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "attachment_id": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|attachment_contents|bytes|True|The Base64-encoded contents of the downloaded attachment|

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
|attachment_name|string|None|True|Name of the attachment in the ServiceNow instance|None|Example name|
|base64_content|bytes|None|True|Content of the attachment, encoded into Base64|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|
|mime_type|string|None|True|MIME type (a.k.a. content type) of the file to be attached|['text/plain (.txt)', 'text/html (.html)', 'application/rtf (.rtf)', 'application/pdf (.pdf)', 'application/msword (.doc)', 'application/vnd.ms-powerpoint (.ppt)', 'image/bmp (.bmp)', 'image/gif (.gif)', 'image/jpeg (.jpg)', 'image/png (.png)', 'image/tiff (.tiff)', 'OTHER']|text/plain (.txt)|
|other_mime_type|string|None|False|User-specified MIME type not in the enumerated list|None|.avi|
|system_id|string|None|True|System ID of the Incident record to which the file will be attached|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "attachment_name": "Example name",
  "base64_content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "mime_type": "text/plain (.txt)",
  "other_mime_type": ".avi",
  "system_id": "9de5069c5afe602b2ea0a04b66beb2c0"
}
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
|filtering_fields|string|None|True|Comma-separated list of fields desired in output object (e.g. opened_by,number)|None|opened_by,number|
|system_id|string|None|True|System ID of the Incident record from which to read|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "filtering_fields": "opened_by,number",
  "system_id": "9de5069c5afe602b2ea0a04b66beb2c0"
}
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
|query|string|None|True|Non-encoded query string for retrieving ServiceNow CI record(s) (e.g. number=INC0000055^ORshort_description=New bug)|None|number=INC0000055^ORshort_description=New bug|
|table|string|None|True|The ServiceNow table to execute the query against|None|catalog_category_request|

Example input:

```
{
  "query": "number=INC0000055^ORshort_description=New bug",
  "table": "catalog_category_request"
}
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

For more information about the **query** input, please refer to [InsightConnect ServiceNow Query Syntax documentation](http://docs.rapid7.com/insightconnect/servicenow#query-syntax).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|Non-encoded query string (e.g. number=INC0000055^ORshort_description=New bug)|None|number=INC0000055^ORshort_description=Newbug|

Example input:

```
{
  "query": "number=INC0000055^ORshort_description=Newbug"
}
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
|name|string|None|True|Name of the attachment, i.e. the base file name used to create it|None|Example name|

Example input:

```
{
  "name": "Example name"
}
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
|system_id|string|None|True|System ID of the CI record to update|None|9de5069c5afe602b2ea0a04b66beb2c0|
|table|string|None|True|The ServiceNow table where the CI record will be updated|None|catalog_category_request|
|update_data|object|None|True|JSON object containing the fields and values to perform a CI update|None|{"Description": "Bug report", "ID": "58"}|

Example input:

```
{
  "system_id": "9de5069c5afe602b2ea0a04b66beb2c0",
  "table": "catalog_category_request",
  "update_data": {
    "Description": "Bug report",
    "ID": "58"
  }
}
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
|additional_fields|object|None|False|JSON object containing the additional fields and values to update incident|None|{"description": "incident description"}|
|assigned_to|string|None|False|User ID of person assigned to the incident|None|user|
|assignment_group|string|None|False|Assignment group name of the incident|None|Recommendation Admin|
|business_service|string|None|False|Name of business service|None|All|
|caller|string|None|False|User ID of incident caller|None|user|
|category|string|None|False|Category code of incident|None|hardware|
|configuration_item|string|None|False|Configuration item code of the incident|None|int-jenkins|
|contact_type|string|None|False|Contact type of the incident|None|phone|
|description|string|None|False|Full description of incident|None|Full details about new employee hire update|
|impact|string|None|False|Impact of the indicent|None|Medium|
|priority|string|None|False|Priority of the incident|None|Planning|
|short_description|string|None|False|Short description of incident|None|New employee hire update|
|state|string|None|False|State name of the incident|None|On Hold|
|subcategory|string|None|False|Subcategory code of incident (available values depends on the `Category` field)|None|monitor|
|system_id|string|None|True|System ID of the Incident record to update|None|ee7e6b24dbf4e450e9faa5730596192b|
|urgency|string|None|False|Urgency of the incident|None|Medium|

Example input:

```
{
  "additional_fields": "{"description": "incident description"}",
  "assigned_to": "user",
  "assignment_group": "Recommendation Admin",
  "business_service": "All",
  "caller": "user",
  "category": "hardware",
  "configuration_item": "int-jenkins",
  "contact_type": "phone",
  "description": "Full details about new employee hire update",
  "impact": "Medium",
  "priority": "Planning",
  "short_description": "New employee hire update",
  "state": "On Hold",
  "subcategory": "monitor",
  "system_id": "ee7e6b24dbf4e450e9faa5730596192b",
  "urgency": "Medium"
}
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
|system_id|string|None|True|System ID of Incident record for which comments and work notes will be retrieved|None|9de5069c5afe602b2ea0a04b66beb2c0|
|type|string|None|True|Type of output to be retrieved|['all', 'comments', 'work notes']|all|

Example input:

```
{
  "system_id": "9de5069c5afe602b2ea0a04b66beb2c0",
  "type": "all"
}
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

#### Incident Created

This trigger identifies if a new incident has been created.

For more information about the **query** input, please refer to [InsightConnect ServiceNow Query Syntax documentation](http://docs.rapid7.com/insightconnect/servicenow#query-syntax).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|frequency|integer|5|True|How often to poll for new incidents (in seconds)|None|5|
|query|string|None|False|Non-encoded query string to match new incident records (will poll for any new incident if query is omitted)|None|short_description=Newbug|

Example input:

```
{
  "frequency": 5,
  "query": "short_description=Newbug"
}
```

Example input (advanced query):
```
{
  "frequency": 10,
  "query": "short_description='Description with quotes'^active=true^priority=5"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|system_id|string|True|System ID of new incident|

Example output:

```
{
  "system_id": "280b3cb71b9f1450c9768622dd4bcb32"
}
```

#### Incident Changed

This trigger reports changes of the given fields in the given Incident.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|interval|integer|5|False|How often to detect changes to the given Incident (in minutes)|None|5|
|monitored_fields|string|None|True|Comma-separated list of fields to be monitored (e.g. resolved,resolved_by)|None|resolved,resolved_by|
|system_id|string|None|True|System ID of the Incident record to monitor|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "interval": 5,
  "monitored_fields": "resolved,resolved_by",
  "system_id": "9de5069c5afe602b2ea0a04b66beb2c0"
}
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
      "current": "Description 2"
    }
  }
}
```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 6.0.1 - Fix base64 decoding in Put Incident Attachment action
* 6.0.0 - Add additional file information in output for Get Attachments for an Incident
* 5.2.0 - Add new action Get Attachments for an Incident | Add unit test for action Get Attachments for an Incident and Get Incident Attachment
* 5.1.1 - Fix output parsing bug in Get Incident Attachment action
* 5.1.0 - Add new Incident URL output for Create Incident action
* 5.0.1 - Add new Additional Fields input for Create Incident and Update Incident actions
* 5.0.0 - Add input fields to Create Incident and Update Incident action instead of JSON object
* 4.1.2 - Fix input parameter in Incident Created trigger
* 4.1.1 - Add `docs_url` to plugin spec with link to plugin setup guide
* 4.1.0 - Add trigger Incident Created
* 4.0.0 - New Number output to create incident action
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
* [ServiceNow API](https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/)
* [ServiceNow User Administration](https://docs.servicenow.com/bundle/rome-platform-administration/page/administer/roles/concept/c_UserAdministration.html)
* [ServiceNow Operators](https://docs.servicenow.com/bundle/quebec-platform-user-interface/page/use/common-ui-elements/reference/r_OpAvailableFiltersQueries.html)
* [ServiceNow Plugin Setup Guide](https://docs.rapid7.com/insightconnect/servicenow)
