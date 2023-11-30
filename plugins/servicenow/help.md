# Description

ServiceNow is a tool for managing incidents and configuration management. Using the ServiceNow plugin for Rapid7 InsightConnect, users can manage all aspects of incidents including creation, search, updates, as well as monitor them for changes

# Key Features
  
*This plugin does not contain any key features.*

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions
  
* 2020-03-11 Orlando

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|client_id|string|None|False|Client ID for an application within your application registry|None|ad0bc2109c2642106907050c2ca6ef0c|
|client_login|credential_username_password|None|True|The ServiceNow username and password for basic authentication API interaction|None|{"username":"user1", "password":"mypassword"}|
|client_secret|credential_secret_key|None|False|Client secret for an application within your application registry|None|ad0bc2109c2642106907050c2ca6ef0c|
|instance|string|None|True|The instance of ServiceNow from the URL, e.g. https://{instance}.service-now.com|None|instance|
|timeout|integer|30|False|The interval in seconds before abandoning an attempt to access ServiceNow|None|30|
  
Example input:

```
{
  "client_id": "ad0bc2109c2642106907050c2ca6ef0c",
  "client_login": {
    "password": "mypassword",
    "username": "user1"
  },
  "client_secret": "ad0bc2109c2642106907050c2ca6ef0c",
  "instance": "instance",
  "timeout": 30
}
```

## Technical Details

### Actions


#### Create Change Request
  
This action is used to creates a change request record based on the default change request record

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_fields|object|None|False|JSON object containing name-value pairs for the field(s) to update in the associated change request|None|{"short_description": "My example short description"}|
  
Example input:

```
{
  "additional_fields": {
    "short_description": "My example short description"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Indicates whether the change request has been created|True|
  
Example output:

```
{
  "success": true
}
```

#### Create CI
  
This action is used to create a new ServiceNow CI record

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|system_id|string|True|System ID of the new CI created|45dd2115db1ebf00a7e99b3c8a9619da|
  
Example output:

```
{
  "system_id": "45dd2115db1ebf00a7e99b3c8a9619da"
}
```

#### Create Incident
  
This action is used to create a new ServiceNow Incident record

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_fields|object|None|False|JSON object containing the additional fields and values to create incident|None|{"description": "incident description"}|
|assigned_to|string|None|False|User ID of person assigned to the incident|None|user|
|assignment_group|string|None|False|Assignment group name of the incident|None|Team Development Code Reviewers|
|business_service|string|None|False|Name of business service|None|All|
|caller|string|None|False|User ID of incident caller|None|user|
|category|string|None|False|Category code of incident|None|software|
|configuration_item|string|None|False|Configuration item code of the incident|None|int-jenkins|
|contact_type|string|None|False|Contact type of the incident|None|email|
|description|string|None|False|Full description of incident|None|Full details about new employee hire|
|impact|string|None|False|Impact of the incident|None|Medium|
|priority|string|None|False|Priority of the incident|None|Planning|
|short_description|string|None|False|Short description of incident|None|New employee hire|
|state|string|None|False|State name of the incident|None|In Progress|
|subcategory|string|None|False|Subcategory code of incident (available values depends on the `Category` field)|None|email|
|urgency|string|None|False|Urgency of the incident|None|Medium|
  
Example input:

```
{
  "additional_fields": {
    "description": "incident description"
  },
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident_url|string|True|URL to newly created incident|https://example.service-now.com/task.do?sys_id=daa10e5ddb5ef7002e12ff00ba9619db|
|number|string|True|Incident ticket number|123|
|system_id|string|True|System ID of the new Incident created|daa10e5ddb5ef7002e12ff00ba9619db|
  
Example output:

```
{
  "incident_url": "https://example.service-now.com/task.do?sys_id=daa10e5ddb5ef7002e12ff00ba9619db",
  "number": 123,
  "system_id": "daa10e5ddb5ef7002e12ff00ba9619db"
}
```

#### Create Security Incident
  
This action is used to create a new security incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_fields|object|None|False|JSON object containing the additional fields and values to create security incident|None|{"risk_score": 40, "risk_score_override": true, "parent_security_incident": "SIR0010010"}|
|affected_user|string|None|False|The user ID, email or system ID of the user related to this security incident|None|jsmith|
|assigned_to|string|None|False|The name, user ID, email or system id of the person primarily responsible for working this task|None|test_user|
|assignment_group|string|None|False|The name or system id of the assignment group|None|Example Group|
|caller|string|None|False|The user ID, email or system ID of the person requesting the work to be done|None|user@example.com|
|category|string|None|False|The code of the security incident category|None|malware|
|cmdb_ci|string|None|False|The name or system ID of the configuration item|None|Example CI|
|contact_type|string|None|False|The code of the security incident source|None|email|
|description|string|None|False|Description of the created security incident|None|Full description|
|location|string|None|False|The name or system ID of the location|None|Example location|
|priority|integer|None|False|The code of the priority in which an Incident needs to be resolved, based on impact and urgency|None|3|
|short_description|string|None|True|Short description of the created security incident|None|Example description|
|state|integer|None|False|The code of the security incident state|None|18|
|subcategory|string|None|False|The code of the security incident subcategory (available values depends on the `Category` field)|None|ransomware|
|substate|integer|None|False|The code of the security incident substate|None|2|
  
Example input:

```
{
  "additional_fields": {
    "parent_security_incident": "SIR0010010",
    "risk_score": 40,
    "risk_score_override": true
  },
  "affected_user": "jsmith",
  "assigned_to": "test_user",
  "assignment_group": "Example Group",
  "caller": "user@example.com",
  "category": "malware",
  "cmdb_ci": "Example CI",
  "contact_type": "email",
  "description": "Full description",
  "location": "Example location",
  "priority": 3,
  "short_description": "Example description",
  "state": 18,
  "subcategory": "ransomware",
  "substate": 2
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|number|string|False|Number of the security incident|SIR0010044|
|system_id|string|False|System ID of the security incident|9de5069c5afe602b2ea0a04b66beb2c0|
  
Example output:

```
{
  "number": "SIR0010044",
  "system_id": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

#### Create Vulnerability
  
This action is used to creates a new vulnerability item record

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_fields|object|None|False|JSON object containing the additional fields and values to create the vulnerability|None|{"description": "Example description"}|
|assigned_to|string|None|False|User ID of person assigned to the vulnerability|None|ExampleUserID|
|dns|string|None|False|The name of source DNS where the vulnerability was found|None|dns.example.com|
|first_found|date|None|False|The time that represents the vulnerability was first found, in ISO format|None|2023-04-28 15:48:07|
|ip_address|string|None|False|The IP address of the source where the vulnerability was found|None|192.168.0.1|
|last_found|date|None|False|The time that represents when the vulnerability was last found, in ISO format|None|2023-04-30 12:14:10|
|risk_score|integer|None|False|The risk score of the vulnerability, from 0 to 100|None|30|
|short_description|string|None|False|Short description of the vulnerability|None|Example short description|
|source|string|None|False|The vulnerability source|None|ExampleSource|
|state|string|None|False|The state of the vulnerability|['Open', 'Under Investigation']|Open|
|vulnerability|string|None|False|The reference of the found vulnerability (third-party vulnerability entry)|None|9de5069c5afe602b2ea0a04b66beb2c0|
  
Example input:

```
{
  "additional_fields": {
    "description": "Example description"
  },
  "assigned_to": "ExampleUserID",
  "dns": "dns.example.com",
  "first_found": "2023-04-28 15:48:07",
  "ip_address": "192.168.0.1",
  "last_found": "2023-04-30 12:14:10",
  "risk_score": 30,
  "short_description": "Example short description",
  "source": "ExampleSource",
  "state": "Open",
  "vulnerability": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|number|string|True|Vulnerability ticket number|1|
|system_id|string|True|System ID of the new vulnerability created|9de5069c5afe602b2ea0a04b66beb2c0|
|vulnerability_url|string|True|URL to newly created vulnerability|https://example.service-now.com/sn_vul_vulnerable_item.do?sys_id=61...|
  
Example output:

```
{
  "number": 1,
  "system_id": "9de5069c5afe602b2ea0a04b66beb2c0",
  "vulnerability_url": "https://example.service-now.com/sn_vul_vulnerable_item.do?sys_id=61..."
}
```

#### Delete Incident
  
This action is used to remove the given ServiceNow Incident from the instance

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|system_id|string|None|True|System ID of the Incident record to delete|None|9de5069c5afe602b2ea0a04b66beb2c0|
  
Example input:

```
{
  "system_id": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|True if the deletion was successful, false otherwise|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete Incident Attachment
  
This action is used to remove the given attachment from the ServiceNow instance

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|attachment_id|string|None|True|System ID of the attachment to delete|None|9de5069c5afe602b2ea0a04b66beb2c0|
  
Example input:

```
{
  "attachment_id": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|True if the deletion was successful, false otherwise|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete Security Incident
  
This action is used to deletes a security incident by sys_id

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|sys_id|string|None|True|The unique system ID of the security incident to delete|None|7dbc4d558bbe4c6cb635b73b5f4a2e27|
  
Example input:

```
{
  "sys_id": "7dbc4d558bbe4c6cb635b73b5f4a2e27"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Whether the action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete Vulnerability
  
This action is used to delete the vulnerability by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|system_id|string|None|True|System ID of the vulnerability to be retrieved|None|9de5069c5afe602b2ea0a04b66beb2c0|
  
Example input:

```
{
  "system_id": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|True if the deletion was successful, false otherwise|True|
  
Example output:

```
{
  "success": true
}
```

#### Get Attachments for an Incident
  
This action is used to search for attachments for a given incident ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|incident_id|string|None|False|ID of the incident|None|9de5069c5afe602b2ea0a04b66beb2c0|
  
Example input:

```
{
  "incident_id": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident_attachments|[]attachment_file|False|List of attachments for a given incident ID|[{"content":"9de5069c5afe602b2ea0a04b66beb2c0","content_type":"text/plain","file_name":"example.txt"}]|
  
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

#### Get CI
  
This action is used to retrieve a CI record from ServiceNow

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|servicenow_ci|object|True|JSON object representing the CI record returned|{"firewall_status":"Intranet","operational_status":"1","sys_updated_on":"2019-06-26 20:45:21","first_discovered":"2018-05-14 18:07:23","used_for":"Production","sys_created_by":"admin","classification":"Production","can_print":"false","last_discovered":"2019-03-24 11:25:56","sys_class_name":"cmdb_ci_server","asset":{"link":"https://example.service-now.com/api/now/table/alm_asset/ff5a6a55dbdef7002e12ff00ba9619d6","value":"ff5a6a55dbdef7002e12ff00ba9619d6"},"sys_updated_by":"admin","sys_created_on":"2019-06-26 20:45:21","sys_domain":{"link":"https://example.service-now.com/api/now/table/sys_user_group/sysdomain","value":"sysdomain"},"fqdn":"fqdntest","hardware_status":"installed","install_status":"1","name":"TEST NAME","subcategory":"Computer","u_restricted_access":"false","sys_id":"375a6a55dbdef7002e12ff00ba9619d6","sys_class_path":"/!!/!G/!!/!$","mac_address":"234324234342","u_automated_patching":"false","sys_mod_count":"0","monitor":"false","ip_address":"10.0.0.1","model_id":{"link":"https://example.service-now.com/api/now/table/cmdb_model/59d4c676db0fc700553363835b961949","value":"59d4c676db0fc700553363835b961949"},"cost_cc":"USD","location":{"link":"https://example.service-now.com/api/now/table/cmn_location/US-East","value":"US-East"},"category":"Hardware","fault_count":"0"}|
  
Example output:

```
{
  "servicenow_ci": {
    "asset": {
      "link": "https://example.service-now.com/api/now/table/alm_asset/ff5a6a55dbdef7002e12ff00ba9619d6",
      "value": "ff5a6a55dbdef7002e12ff00ba9619d6"
    },
    "can_print": "false",
    "category": "Hardware",
    "classification": "Production",
    "cost_cc": "USD",
    "fault_count": "0",
    "firewall_status": "Intranet",
    "first_discovered": "2018-05-14 18:07:23",
    "fqdn": "fqdntest",
    "hardware_status": "installed",
    "install_status": "1",
    "ip_address": "10.0.0.1",
    "last_discovered": "2019-03-24 11:25:56",
    "location": {
      "link": "https://example.service-now.com/api/now/table/cmn_location/US-East",
      "value": "US-East"
    },
    "mac_address": "234324234342",
    "model_id": {
      "link": "https://example.service-now.com/api/now/table/cmdb_model/59d4c676db0fc700553363835b961949",
      "value": "59d4c676db0fc700553363835b961949"
    },
    "monitor": "false",
    "name": "TEST NAME",
    "operational_status": "1",
    "subcategory": "Computer",
    "sys_class_name": "cmdb_ci_server",
    "sys_class_path": "/!!/!G/!!/!$",
    "sys_created_by": "admin",
    "sys_created_on": "2019-06-26 20:45:21",
    "sys_domain": {
      "link": "https://example.service-now.com/api/now/table/sys_user_group/sysdomain",
      "value": "sysdomain"
    },
    "sys_id": "375a6a55dbdef7002e12ff00ba9619d6",
    "sys_mod_count": "0",
    "sys_updated_by": "admin",
    "sys_updated_on": "2019-06-26 20:45:21",
    "u_automated_patching": "false",
    "u_restricted_access": "false",
    "used_for": "Production"
  }
}
```

#### Get Incident Attachment
  
This action is used to download the Base64-encoded contents of the given attachment

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|attachment_id|string|None|True|System ID of the attachment to copy|None|9de5069c5afe602b2ea0a04b66beb2c0|
  
Example input:

```
{
  "attachment_id": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|attachment_contents|bytes|True|The Base64-encoded contents of the downloaded attachment|[base-64 contents]|
  
Example output:

```
{
  "attachment_contents": "[base-64 contents]"
}
```

#### Get Incident Comments and Work Notes
  
This action is used to get comments and work notes for an incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|incident_comments_worknotes|[]comments_worknotes|True|List of comments and work notes for an incident|[{"sys_id":"2c6420c31b0000506a4a85507e4bcb82","sys_created_on":"2019-09-26 21:19:11","name":"incident","element_id":"965f140bdb4c8c105f6f00b5ca961922","sys_tags":"","value":"Team is actively looking into it.","sys_created_by":"admin","element":"work_notes"},{"sys_id":"4db0e8cb1bcccc106a4a85507e4bcba2","sys_created_on":"2019-09-26 21:03:07","name":"incident","element_id":"965f140bdb4c8c105f6f00b5ca961922","sys_tags":"","value":"This is Sev1 incident.","sys_created_by":"admin","element":"comments"},{"sys_id":"f92024471b0000506a4a85507e4bcb78","sys_created_on":"2019-09-26 21:00:43","name":"incident","element_id":"965f140bdb4c8c105f6f00b5ca961922","sys_tags":"","value":"Testing comments","sys_created_by":"admin","element":"comments"}]|
  
Example output:

```
{
  "incident_comments_worknotes": [
    {
      "element": "work_notes",
      "element_id": "965f140bdb4c8c105f6f00b5ca961922",
      "name": "incident",
      "sys_created_by": "admin",
      "sys_created_on": "2019-09-26 21:19:11",
      "sys_id": "2c6420c31b0000506a4a85507e4bcb82",
      "sys_tags": "",
      "value": "Team is actively looking into it."
    },
    {
      "element": "comments",
      "element_id": "965f140bdb4c8c105f6f00b5ca961922",
      "name": "incident",
      "sys_created_by": "admin",
      "sys_created_on": "2019-09-26 21:03:07",
      "sys_id": "4db0e8cb1bcccc106a4a85507e4bcba2",
      "sys_tags": "",
      "value": "This is Sev1 incident."
    },
    {
      "element": "comments",
      "element_id": "965f140bdb4c8c105f6f00b5ca961922",
      "name": "incident",
      "sys_created_by": "admin",
      "sys_created_on": "2019-09-26 21:00:43",
      "sys_id": "f92024471b0000506a4a85507e4bcb78",
      "sys_tags": "",
      "value": "Testing comments"
    }
  ]
}
```

#### Get Security Incident
  
This action is used to retrieves a security incident by sys_id

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|sys_id|string|None|True|The unique system ID of the security incident|None|7dbc4d558bbe4c6cb635b73b5f4a2e27|
  
Example input:

```
{
  "sys_id": "7dbc4d558bbe4c6cb635b73b5f4a2e27"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|security_incident|security_incident|False|Details of the security incident|{}|
  
Example output:

```
{
  "security_incident": {}
}
```

#### Get Vulnerability
  
This action is used to retrieve the vulnerability by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filtering_fields|string|None|True|Comma-separated list of fields desired in output object (e.g. opened_by,number)|None|opened_by,number|
|system_id|string|None|True|System ID of the vulnerability to be retrieved|None|9de5069c5afe602b2ea0a04b66beb2c0|
  
Example input:

```
{
  "filtering_fields": "opened_by,number",
  "system_id": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|filtered_vulnerability|object|True|JSON object representing the vulnerability containing the given fields|{"number":"1","opened_by":{"link":"https://example.service-now.com/api/now/table/sys...","value":""},"state":"1"}|
  
Example output:

```
{
  "filtered_vulnerability": {
    "number": "1",
    "opened_by": {
      "link": "https://example.service-now.com/api/now/table/sys...",
      "value": ""
    },
    "state": "1"
  }
}
```

#### Put Incident Attachment
  
This action is used to associate a file with a ServiceNow Incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|attachment_id|string|True|System ID of the newly created attachment|b5b24a5ddb1ebf00a7e99b3c8a96197d|
  
Example output:

```
{
  "attachment_id": "b5b24a5ddb1ebf00a7e99b3c8a96197d"
}
```

#### Read Incident
  
This action is used to populate a JSON object with the specified fields of the given Incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|filtered_incident|object|True|JSON object representing the incident containing the given fields|{"short_description":"Short description test","description":"Description test"}|
  
Example output:

```
{
  "filtered_incident": {
    "description": "Description test",
    "short_description": "Short description test"
  }
}
```

#### Search CI
  
This action is used to retrieve CI record(s) from ServiceNow based on the provided query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|servicenow_cis|[]object|True|List of JSON objects representing the CI record(s) returned by the query|[{"firewall_status":"Intranet","operational_status":"1","sys_updated_on":"2019-06-26 20:45:21","first_discovered":"2018-05-14 18:07:23","used_for":"Production","sys_created_by":"admin","classification":"Production","can_print":"false","last_discovered":"2019-03-24 11:25:56","sys_class_name":"cmdb_ci_server","cd_rom":"false","unverified":"false","asset":{"link":"https://example.service-now.com/api/now/table/alm_asset/ff5a6a55dbdef7002e12ff00ba9619d6","value":"ff5a6a55dbdef7002e12ff00ba9619d6"},"skip_sync":"false","sys_updated_by":"admin","sys_created_on":"2019-06-26 20:45:21","sys_domain":{"link":"https://example.service-now.com/api/now/table/sys_user_group/sysdomain","value":"sysdomain"},"fqdn":"fqdntest","hardware_status":"installed","install_status":"1","name":"TEST NAME","subcategory":"Computer","u_restricted_access":"false","virtual":"false","sys_id":"375a6a55dbdef7002e12ff00ba9619d6","sys_class_path":"/!!/!G/!!/!$","mac_address":"234324234342","u_automated_patching":"false","sys_mod_count":"0","monitor":"false","ip_address":"10.0.0.1","model_id":{"link":"https://example.service-now.com/api/now/table/cmdb_model/59d4c676db0fc700553363835b961949","value":"59d4c676db0fc700553363835b961949"},"cost_cc":"USD","location":{"link":"https://example.service-now.com/api/now/table/cmn_location/US-East","value":"US-East"},"category":"Hardware","fault_count":"0"}]|
  
Example output:

```
{
  "servicenow_cis": [
    {
      "asset": {
        "link": "https://example.service-now.com/api/now/table/alm_asset/ff5a6a55dbdef7002e12ff00ba9619d6",
        "value": "ff5a6a55dbdef7002e12ff00ba9619d6"
      },
      "can_print": "false",
      "category": "Hardware",
      "cd_rom": "false",
      "classification": "Production",
      "cost_cc": "USD",
      "fault_count": "0",
      "firewall_status": "Intranet",
      "first_discovered": "2018-05-14 18:07:23",
      "fqdn": "fqdntest",
      "hardware_status": "installed",
      "install_status": "1",
      "ip_address": "10.0.0.1",
      "last_discovered": "2019-03-24 11:25:56",
      "location": {
        "link": "https://example.service-now.com/api/now/table/cmn_location/US-East",
        "value": "US-East"
      },
      "mac_address": "234324234342",
      "model_id": {
        "link": "https://example.service-now.com/api/now/table/cmdb_model/59d4c676db0fc700553363835b961949",
        "value": "59d4c676db0fc700553363835b961949"
      },
      "monitor": "false",
      "name": "TEST NAME",
      "operational_status": "1",
      "skip_sync": "false",
      "subcategory": "Computer",
      "sys_class_name": "cmdb_ci_server",
      "sys_class_path": "/!!/!G/!!/!$",
      "sys_created_by": "admin",
      "sys_created_on": "2019-06-26 20:45:21",
      "sys_domain": {
        "link": "https://example.service-now.com/api/now/table/sys_user_group/sysdomain",
        "value": "sysdomain"
      },
      "sys_id": "375a6a55dbdef7002e12ff00ba9619d6",
      "sys_mod_count": "0",
      "sys_updated_by": "admin",
      "sys_updated_on": "2019-06-26 20:45:21",
      "u_automated_patching": "false",
      "u_restricted_access": "false",
      "unverified": "false",
      "used_for": "Production",
      "virtual": "false"
    }
  ]
}
```

#### Search Incident
  
This action is used to search for Incidents satisfying the given query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|True|Non-encoded query string (e.g. number=INC0000055^ORshort_description=New bug)|None|number=INC0000055^ORshort_description=Newbug|
  
Example input:

```
{
  "query": "number=INC0000055^ORshort_description=Newbug"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|system_ids|[]string|True|List of System IDs of Incidents satisfying the given query|["b5aadf6cdb16b7002e12ff00ba96193c","90db5f20db967f00a7e99b3c8a96190c","28869809db12bf00a7e99b3c8a9619de","e5a14141db92f7002e12ff00ba961962","38aa01d9dbdaf7002e12ff00ba96196a","daa10e5ddb5ef7002e12ff00ba9619db"]|
  
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
  
This action is used to search for attachment files with the given name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|True|Name of the attachment, i.e. the base file name used to create it|None|Example name|
  
Example input:

```
{
  "name": "Example name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|attachment_ids|[]string|True|List of System IDs of attachment records with the given name|["7bbbc15ddbdaf7002e12ff00ba96196c","b5b24a5ddb1ebf00a7e99b3c8a96197d","46c14941db92bf00a7e99b3c8a9619b6"]|
  
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

#### Search Security Incident
  
This action is used to returns security incidents that match the search criteria

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fields|string|None|False|A comma-separated list of fields to return in the response|None|number,sys_id|
|limit|integer|None|False|Maximum number of records to return|None|10|
|offset|integer|None|False|Starting record index for which to begin retrieving records|None|5|
|query|string|None|False|An encoded query string used to filter the results|None|number=SIR0000001|
  
Example input:

```
{
  "fields": "number,sys_id",
  "limit": 10,
  "offset": 5,
  "query": "number=SIR0000001"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|security_incidents|[]security_incident|False|Details of the matching security incidents|[]|
  
Example output:

```
{
  "security_incidents": []
}
```

#### Update CI
  
This action is used to update an existing ServiceNow CI record

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|True if the update was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Update Incident
  
This action is used to update a ServiceNow Incident with the given data

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_fields|object|None|False|JSON object containing the additional fields and values to update incident|None|{"description": "incident description"}|
|assigned_to|string|None|False|User ID of person assigned to the incident|None|user|
|assignment_group|string|None|False|Assignment group name of the incident|None|Recommendation Admin|
|business_service|string|None|False|Name of business service|None|All|
|caller|string|None|False|User ID of incident caller|None|user|
|category|string|None|False|Category code of incident|None|hardware|
|configuration_item|string|None|False|Configuration item code of the incident|None|int-jenkins|
|contact_type|string|None|False|Contact type of the incident|None|phone|
|description|string|None|False|Full description of incident|None|Full details about new employee hire update|
|impact|string|None|False|Impact of the incident|None|Medium|
|priority|string|None|False|Priority of the incident|None|Planning|
|short_description|string|None|False|Short description of incident|None|New employee hire update|
|state|string|None|False|State name of the incident|None|On Hold|
|subcategory|string|None|False|Subcategory code of incident (available values depends on the `Category` field)|None|monitor|
|system_id|string|None|True|System ID of the Incident record to update|None|ee7e6b24dbf4e450e9faa5730596192b|
|urgency|string|None|False|Urgency of the incident|None|Medium|
  
Example input:

```
{
  "additional_fields": {
    "description": "incident description"
  },
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|True if the update was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Update Security Incident
  
This action is used to update an existing security incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_fields|object|None|False|JSON object containing the additional fields and values to update security incident|None|{"risk_score": 40, "risk_score_override": true, "parent_security_incident": "SIR0010010"}|
|affected_user|string|None|False|The user ID, email or system ID of the user related to this security incident|None|jsmith|
|assigned_to|string|None|False|The name, user ID, email or system id of the person primarily responsible for working this task|None|test_user|
|assignment_group|string|None|False|The name or system id of the assignment group|None|Example Group|
|caller|string|None|False|The user ID, email or system ID of the person requesting the work to be done|None|user@example.com|
|category|string|None|False|The code of the security incident category|None|malware|
|close_code|string|None|False|The code of the incident closure reason|None|Not resolved|
|close_notes|string|None|False|Incident closure notes|None|Example notes|
|cmdb_ci|string|None|False|The name or system ID of the configuration item|None|Example CI|
|contact_type|string|None|False|The code of the security incident source|None|email|
|description|string|None|False|Description of the security incident|None|Full description|
|location|string|None|False|The name or system ID of the location|None|Example location|
|priority|integer|None|False|The code of the priority in which an Incident needs to be resolved, based on impact and urgency|None|3|
|short_description|string|None|False|Short description of the security incident|None|Example description|
|state|integer|None|False|The code of the security incident state|None|18|
|subcategory|string|None|False|The code of the security incident subcategory (available values depends on the `Category` field)|None|ransomware|
|substate|integer|None|False|The code of the security incident substate|None|2|
|sys_id|string|None|True|The system ID of the security incident to be updated|None|9de5069c5afe602b2ea0a04b66beb2c0|
  
Example input:

```
{
  "additional_fields": {
    "parent_security_incident": "SIR0010010",
    "risk_score": 40,
    "risk_score_override": true
  },
  "affected_user": "jsmith",
  "assigned_to": "test_user",
  "assignment_group": "Example Group",
  "caller": "user@example.com",
  "category": "malware",
  "close_code": "Not resolved",
  "close_notes": "Example notes",
  "cmdb_ci": "Example CI",
  "contact_type": "email",
  "description": "Full description",
  "location": "Example location",
  "priority": 3,
  "short_description": "Example description",
  "state": 18,
  "subcategory": "ransomware",
  "substate": 2,
  "sys_id": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|number|string|False|Number of the security incident|SIR0010044|
|system_id|string|False|System ID of the security incident|9de5069c5afe602b2ea0a04b66beb2c0|
  
Example output:

```
{
  "number": "SIR0010044",
  "system_id": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

#### Update Vulnerability
  
This action is used to update the vulnerability by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|additional_fields|object|None|False|JSON object containing the additional fields and values to update the vulnerability item|None|{"description": "Example description"}|
|assigned_to|string|None|False|User ID of person assigned to the vulnerability|None|ExampleUserID|
|dns|string|None|False|The name of the source DNS where the vulnerability was found|None|dns.example.com|
|first_found|date|None|False|The time that represents the vulnerability was first found, in ISO format|None|2023-04-28 15:48:07|
|ip_address|string|None|False|The IP address of the source where the vulnerability was found|None|192.168.0.1|
|last_found|date|None|False|The time that represents when the vulnerability was last found, in ISO format|None|2023-04-30 12:14:10|
|short_description|string|None|False|Short description of the vulnerability|None|Example short description|
|source|string|None|False|The vulnerability source|None|ExampleSource|
|state|string|None|False|The state of the vulnerability|['', 'Open', 'Under Investigation']|Open|
|system_id|string|None|True|System ID of the vulnerability to be retrieved|None|9de5069c5afe602b2ea0a04b66beb2c0|
|vulnerability|string|None|False|The reference of the found vulnerability|None|9de5069c5afe602b2ea0a04b66beb2c0|
  
Example input:

```
{
  "additional_fields": {
    "description": "Example description"
  },
  "assigned_to": "ExampleUserID",
  "dns": "dns.example.com",
  "first_found": "2023-04-28 15:48:07",
  "ip_address": "192.168.0.1",
  "last_found": "2023-04-30 12:14:10",
  "short_description": "Example short description",
  "source": "ExampleSource",
  "state": "Open",
  "system_id": "9de5069c5afe602b2ea0a04b66beb2c0",
  "vulnerability": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|True if the update was successful, false otherwise|True|
  
Example output:

```
{
  "success": true
}
```
### Triggers


#### Incident Changed
  
This action is used to reports changes of the given fields in the given Incident

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|changed_fields|object|True|JSON object representing changed fields (map of field name to previous and current values)|{"description":{"previous":"Description 1","current":"Description 2"}}|
  
Example output:

```
{
  "changed_fields": {
    "description": {
      "current": "Description 2",
      "previous": "Description 1"
    }
  }
}
```

#### Incident Created
  
This action is used to identifies if a new incident has been created

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|5|True|How often to poll for new incidents (in seconds)|None|5|
|query|string|None|False|Non-encoded query string to match new incident records (will poll for any new incident if query is omitted)|None|short_description=Newbug|
  
Example input:

```
{
  "frequency": 5,
  "query": "short_description=Newbug"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|system_id|string|True|System ID of new incident|280b3cb71b9f1450c9768622dd4bcb32|
  
Example output:

```
{
  "system_id": "280b3cb71b9f1450c9768622dd4bcb32"
}
```

#### Vulnerability Updated
  
This action is used to identifies if a vulnerability has been updated

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|interval|integer|5|True|How often to detect changes to the given Incident (in seconds)|None|5|
|monitored_fields|string|None|True|Comma-separated list of fields to be monitored (e.g. resolved,resolved_by)|None|resolved,resolved_by|
|system_ids|[]string|None|True|List of system IDs of the vulnerability record to monitor|None|["9de5069c5afe602b2ea0a04b66beb2c0"]|
  
Example input:

```
{
  "interval": 5,
  "monitored_fields": "resolved,resolved_by",
  "system_ids": [
    "9de5069c5afe602b2ea0a04b66beb2c0"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|updated_vulnerabilities|[]updated_vulnerability|True|List of JSON objects containing the system ID of the updated vulnerability and representation of the changed fields (map of field name from previous to current values)|{"updated_vulnerabilities": [{"system_id": "9de5069c5afe602b2ea0a04b66beb2c0", "changed_fields": {"description":{"previous":"Description 1","current":"Description 2"}}}]}|
  
Example output:

```
{
  "updated_vulnerabilities": {
    "updated_vulnerabilities": [
      {
        "changed_fields": {
          "description": {
            "current": "Description 2",
            "previous": "Description 1"
          }
        },
        "system_id": "9de5069c5afe602b2ea0a04b66beb2c0"
      }
    ]
  }
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**updated_vulnerability**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Changed Fields|object|None|True|JSON object representing changed fields (map of field name to previous and current values)|None|
|System ID|string|None|True|System ID of the vulnerability|None|
  
**comments_worknotes**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Element|string|None|True|Either 'comments' or 'work_notes'|None|
|Element ID|string|None|True|System ID of an incident|None|
|Name|string|None|True|Type of record|None|
|Created By|string|None|True|User who added the comment|None|
|Creation date|string|None|True|Comment or work notes creation date|None|
|System ID|string|None|True|System ID of comment or worknotes|None|
|System Tags|string|None|True|System tags|None|
|Value|string|None|True|Value of comment or worknotes|None|
  
**attachment_file**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Content|string|None|False|File content encoded with base64|None|
|Content Type|string|None|False|Content type|None|
|File Name|string|None|False|File name|None|
  
**link_value**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Link|string|None|False|Link to the resource|None|
|Value|string|None|False|Identifier of the resource|None|
  
**security_incident**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Active|boolean|None|False|Whether the security incident is active|None|
|Activity Due|string|None|False|Date by which the Inactivity Monitor expects the task to be updated|None|
|Affected User|link_value|None|False|The user related to this security incident|None|
|Alert ID|string|None|False|The identifier of the alert|None|
|Alert Rule|string|None|False|The rule of the alert|None|
|Assigned To|link_value|None|False|Person primarily responsible for working this task|None|
|Assignment Group|link_value|None|False|Group responsible for working this task|None|
|Business Impact|integer|None|False|The business impact of this incident|None|
|Requested By|link_value|None|False|Person requesting the work to be done. Determines suggested Location if no Affected CI is defined|None|
|Category|string|None|False|Category of the incident|None|
|Change Request|link_value|None|False|The change request related to this security incident|None|
|Close Code|integer|None|False|Code indicating why the incident is being closed|None|
|Close Notes|string|None|False|Notes explaining why the incident is being closed|None|
|Closed At|string|None|False|Time when the security incident was closed|None|
|Closed By|link_value|None|False|The person who closed the security incident|None|
|Configuration Item|link_value|None|False|Item or service affected|None|
|Source|string|None|False|Source of the security incident|None|
|Description|string|None|False|Description of the security incident|None|
|Incident|link_value|None|False|The incident related to this security incident|None|
|Location|link_value|None|False|Where the caller or service is located|None|
|Number|string|None|False|Identification number of the security incident|None|
|Opened At|string|None|False|Time when the security incident was opened|None|
|Opened By|link_value|None|False|The person who opened the security incident|None|
|Opened For|link_value|None|False|Person this request was opened for|None|
|Parent|link_value|None|False|The parent of this security incident|None|
|Parent Security Incident|link_value|None|False|The parent security incident to this security incident|None|
|Priority|integer|None|False|Sequence in which the security incident needs to be resolved, based on impact and urgency|None|
|Problem|link_value|None|False|The problem related to this security incident|None|
|Risk Score|integer|None|False|Score of the risk|None|
|Risk Score Override|boolean|None|False|When checked, risk score will not be updated automatically|None|
|Secure Notes|string|None|False|Encrypted note of the security incident|None|
|Security Tags|string|None|False|Security tags applied to this security incident|None|
|Short Description|string|None|False|Short description of the security incident|None|
|Special Access Write|string|None|False|Users in the 'Privileged access' list will be able to see the Security Incident, data related to it and edit all data fields on it|None|
|State|integer|None|False|State of the security incident|None|
|Subcategory|string|None|False|Subcategory of the security incident|None|
|Substate|integer|None|False|Substate of the security incident|None|
|System Created By|string|None|False|Person this security incident was created by|None|
|System Created On|string|None|False|Time when the security incident was created|None|
|System ID|string|None|False|The unique system ID of the security incident|None|
|System Updated By|string|None|False|Person this security incident was updated by|None|
|System Updated On|string|None|False|Time when the security incident was updated|None|
|Watch List|string|None|False|List of users that are interested on the security incident|None|
|Work Notes List|string|None|False|Users interested in work notes|None|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History
  
*This plugin does not contain a version history.*

# Links


## References
  
*This plugin does not contain any references.*