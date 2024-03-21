# Description

IBM QRadar reduces billions of events and flows into a manageable number of actionable offenses that are prioritized by their impact on your business operations. This plugin allows you to use IBM QRadar to orchestrate and automate Ariel search queries and automate offense management

# Key Features

* Start Ariel search
* Get Ariel search by ID
* Get offenses
* Get offense closing reasons
* Get assets
* Get offense notes
* Get offense note by ID
* Add note to offense
* Update offense
* Watch for new offenses

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 7.3.3

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|True|Auth object consisting of username of type string and password of type password|None|{ 'username': 'user1', 'password': 'password'}|
|host_url|string|None|True|Host URL of the QRadar instance.|None|https://127.0.0.1/|
|verify_ssl|boolean|None|False|Whether to verify the SSL for QRadar connection|None|True|

Example input:

```
{
  "credentials": "{ 'username': 'user1', 'password': 'password'}",
  "host_url": "https://127.0.0.1/",
  "verify_ssl": true
}
```

## Technical Details

### Actions


#### Add Notes to Offense

This action is used to add Notes to Offense

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fields|string|None|False|Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, create_time, username, note_text. More information about the fields can be found in plugin documentation|None|id, note_text|
|filter|string|None|False|Restrict the elements in a list based on the contents of various fields.|None|id=1000|
|note_text|string|None|True|The note text to add to the offense|None|note_text|
|offense_id|integer|None|True|The ID of the offense in which to add a note|None|100|
  
Example input:

```
{
  "fields": "id, note_text",
  "filter": "id=1000",
  "note_text": "note_text",
  "offense_id": 100
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|note|False|JSON data of the newly added Offense Notes |{'create_time': 1642056336657, 'id': 404, 'note_text': 'New Note text', 'username': 'API_user: admin'}|
  
Example output:

```
{
  "data": {
    "create_time": 1642056336657,
    "id": 404,
    "note_text": "New Note text",
    "username": "API_user: admin"
  }
}
```

#### Get Ariel Search by ID

This action is used to get an ariel search by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|poll_interval|number|1|False|Number of seconds to recheck until the search is completed|None|1|
|search_id|string|None|True|ID of the Ariel search to get|None|9102cb1d-5994-4f78-8f08-16c6f6991015|
  
Example input:

```
{
  "poll_interval": 1,
  "search_id": "9102cb1d-5994-4f78-8f08-16c6f6991015"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|search|False|JSON data of the Search|{'completed': True, 'compressed_data_file_count': 0, 'compressed_data_total_size': 0, 'cursor_id': '0ab77680-d6a5-4944-9eda-9cb95171c86f', 'data_file_count': 2, 'data_total_size': 371376, 'desired_retention_time_msec': 86400000, 'index_file_count': 0, 'index_total_size': 0, 'processed_record_count': 28752, 'progress': 100, 'progress_details': [], 'query_execution_time': 117, 'query_string': 'Select * from events', 'record_count': 28752, 'save_results': False, 'search_id': '0ab77680-d6a5-4944-9eda-9cb95171c86f', 'size_on_disk': 10809724, 'status': 'COMPLETED', 'subsearch_ids': []}|
  
Example output:

```
{
  "data": {
    "completed": true,
    "compressed_data_file_count": 0,
    "compressed_data_total_size": 0,
    "cursor_id": "0ab77680-d6a5-4944-9eda-9cb95171c86f",
    "data_file_count": 2,
    "data_total_size": 371376,
    "desired_retention_time_msec": 86400000,
    "index_file_count": 0,
    "index_total_size": 0,
    "processed_record_count": 28752,
    "progress": 100,
    "progress_details": [],
    "query_execution_time": 117,
    "query_string": "Select * from events",
    "record_count": 28752,
    "save_results": false,
    "search_id": "0ab77680-d6a5-4944-9eda-9cb95171c86f",
    "size_on_disk": 10809724,
    "status": "COMPLETED",
    "subsearch_ids": []
  }
}
```

#### Get Assets

This action is used to list all assets found in the model

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fields|string|None|False|Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, domain_id, hostnames(id), interfaces, products. More information about the fields can be found in plugin documentation|None|id, hostnames(id)|
|filter|string|None|False|Restrict the elements in a list based on the contents of various fields|None|id = 1001 and vulnerability_count >= 0|
|range|string|1-50|False|Paging requests are specified with the Range parameter. E.g. the example default range returns the first 50 records, a custom range of 6-10 returns the 6th to 10th records|None|1-2|
  
Example input:

```
{
  "fields": "id, hostnames(id)",
  "filter": "id = 1001 and vulnerability_count >= 0",
  "range": "1-50"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|[]assets|False|JSON data of the Assets|[{"vulnerability_count": 0, "id": 1002, "interfaces": [{"created": 1640265476716, "id": 1002, "ip_addresses": [{"type": "IPV4", "value": "192.10.10.179", "created": 1640265476716, "id": 1002, "network_id": 2}]}], "risk_score_sum": 0, "properties": [{"name": "Unified Name", "type_id": 1002, "value": "192.10.10.179", "id": 1003, "last_reported": 1640265476727, "last_reported_by": "USER:admin"}], "users": [], "domain_id": 0, "host_urls": [], "products": []}]|
  
Example output:

```
{
  "data": [
    {
      "domain_id": 0,
      "host_urls": [],
      "id": 1002,
      "interfaces": [
        {
          "created": 1640265476716,
          "id": 1002,
          "ip_addresses": [
            {
              "created": 1640265476716,
              "id": 1002,
              "network_id": 2,
              "type": "IPV4",
              "value": "192.10.10.179"
            }
          ]
        }
      ],
      "products": [],
      "properties": [
        {
          "id": 1003,
          "last_reported": 1640265476727,
          "last_reported_by": "USER:admin",
          "name": "Unified Name",
          "type_id": 1002,
          "value": "192.10.10.179"
        }
      ],
      "risk_score_sum": 0,
      "users": [],
      "vulnerability_count": 0
    }
  ]
}
```

#### Get Offense's Closing Reasons

This action is used to get Offense's Closing Reasons

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fields|string|None|False|Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, text, is_deleted, is_reserved. More information about the fields can be found in plugin documentation|None|id, is_deleted|
|filter|string|None|False|Restrict the elements in a list based on the contents of various fields.|None|id=1000|
|include_deleted|boolean|None|False|If true, deleted closing reasons are included in the response. Defaults to false. Deleted closing reasons cannot be used to close an offense|None|False|
|include_reserved|boolean|None|False|If true, reserved closing reasons are included in the response. Defaults to false. Reserved closing reasons cannot be used to close an offense|None|False|
|range|string|1-50|False|Paging requests are specified with the Range parameter. E.g. the example default range returns the first 50 records, a custom range of 6-10 returns the 6th to 10th records|None|1-2|
  
Example input:

```
{
  "fields": "id, is_deleted",
  "filter": "id=1000",
  "include_deleted": false,
  "include_reserved": false,
  "range": "1-50"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|[]closing_reason|False|JSON data of the Offense Closing Reasons|[ { "id": 1, "is_deleted": False, "is_reserved": False, "text": "Non-Issue" },{"id": 3,"is_deleted": False,"is_reserved": False,"text": "Policy Violation"}]|
  
Example output:

```
{
  "data": "[ { \"id\": 1, \"is_deleted\": False, \"is_reserved\": False, \"text\": \"Non-Issue\" },{\"id\": 3,\"is_deleted\": False,\"is_reserved\": False,\"text\": \"Policy Violation\"}]"
}
```

#### Get Offense Notes

This action is used to get Offense Notes

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fields|string|None|False|Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, create_time, username, note_text. More information about the fields can be found in plugin documentation|None|id, note_text|
|filter|string|None|False|Restrict the elements in a list based on the contents of various fields.|None|id=100|
|offense_id|integer|None|True|The ID of the offense to get notes for|None|100|
|range|string|1-50|False|Paging requests are specified with the Range parameter. E.g. the example default range returns the first 50 records, a custom range of 6-10 returns the 6th to 10th records|None|1-2|
  
Example input:

```
{
  "fields": "id, note_text",
  "filter": "id=100",
  "offense_id": 100,
  "range": "1-50"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|[]note|False|JSON data of the Offense Notes|[{"create_time": 1641385946573, "id": 159, "note_text": "New Note text", "username": "API_user: admin"}, {"create_time": 1641451278329, "id": 209, "note_text": "New Note text", "username": "API_user: admin"}]|
  
Example output:

```
{
  "data": [
    {
      "create_time": 1641385946573,
      "id": 159,
      "note_text": "New Note text",
      "username": "API_user: admin"
    },
    {
      "create_time": 1641451278329,
      "id": 209,
      "note_text": "New Note text",
      "username": "API_user: admin"
    }
  ]
}
```

#### Get Offense Notes by ID

This action is used to get Offense Notes by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fields|string|None|False|Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, create_time, username, note_text. More information about the fields can be found in plugin documentation|None|id, note_text|
|filter|string|None|False|Restrict the elements in a list based on the contents of various fields.|None|id=1000|
|note_id|integer|None|True|The ID of the offense note to get|None|100|
|offense_id|integer|None|True|The ID of the offense to get notes for|None|100|
  
Example input:

```
{
  "fields": "id, note_text",
  "filter": "id=1000",
  "note_id": 100,
  "offense_id": 100
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|note|False|JSON data of the Offense Notes for given ID|[{"create_time": 1641385946573, "id": 159, "note_text": "New Note text", "username": "API_user: admin"}, {"username": "API_user: admin", "create_time": 1641451278329, "id": 209, "note_text": "New Note text"}]|
  
Example output:

```
{
  "data": [
    {
      "create_time": 1641385946573,
      "id": 159,
      "note_text": "New Note text",
      "username": "API_user: admin"
    },
    {
      "create_time": 1641451278329,
      "id": 209,
      "note_text": "New Note text",
      "username": "API_user: admin"
    }
  ]
}
```

#### Get Offenses

This action is used to list all offenses

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fields|string|None|False|Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, assigned_to, inactive, offense_source,  offense_type, rules(id), protected, follow_up, status, domain_id, rules, log_sources. More information about the fields can be found in plugin documentation|None|id, rules(id)|
|filter|string|None|False|Restrict the elements in a list based on the contents of various fields.|None|id=1000|
|range|string|1-50|False|Paging requests are specified with the Range parameter. E.g. the example default range returns the first 50 records, a custom range of 6-10 returns the 6th to 10th records|None|1-2|
|sort|string|None|False|Apply sorting order to result sets, e.g. +id to sort the result in ascending order of id value|None|+id,-status|
  
Example input:

```
{
  "fields": "id, rules(id)",
  "filter": "id=1000",
  "range": "1-50",
  "sort": "+id,-status"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|[]offense|False|JSON data of the Offense|[{"source_network": "Net-10-172-192.Net_172_16_0_0","domain_id": 0,"inactive": false,"last_updated_time": 1642054761525,"magnitude": 4,"offense_source": "172.31.34.93","protected": false,"start_time": 1641970465643,"category_count": 2,"rules": [{"id": 100033,"type": "CRE_RULE"},{"id": 100626,"type": "CRE_RULE"}],"event_count": 13493550,"id": 42,"remote_destination_count": 1,"username_count": 2,"first_persisted_time": 1641970466000,"offense_type": 0,"security_category_count": 2,"source_count": 1,"credibility": 2,"description": "Excessive Firewall Denies Between Hosts\n","flow_count": 0,"local_destination_address_ids": [14],"severity": 5,"categories": ["Access Denied","ACL Deny"],"device_count": 1,"last_persisted_time": 1642054764000,"log_sources": [{"type_name": "EventCRE","id": 63,"name": "Custom Rule Engine-8 :: ip-172-31-34-93","type_id": 18}],"policy_category_count": 0,"relevance": 5,"source_address_ids": [19],"destination_networks": ["Net-10-172-192.Net_172_16_0_0","other"],"local_destination_count": 1,"status": "OPEN","follow_up": false},{"event_count": 2429,"flow_count": 0,"magnitude": 3,"offense_type": 0,"source_network": "other","username_count": 1,"close_time": 1641970533000,"first_persisted_time": 1641968803000,"id": 41,"last_updated_time": 1641970524788,"destination_networks": ["Net-10-172-192.Net_172_16_0_0"],"device_count": 1,"domain_id": 0,"local_destination_address_ids": [14],"policy_category_count": 0,"protected": false,"start_time": 1641968802643,"follow_up": false,"log_sources": [{"id": 63,"name": "Custom Rule Engine-8 :: ip-172-31-34-93","type_id": 18,"type_name": "EventCRE"}],"offense_source": "183.82.206.22","source_address_ids": [22],"source_count": 1,"categories": ["Access Denied","ACL Deny"],"closing_user": "admin","credibility": 2,"remote_destination_count": 0,"rules": [{"id": 100625,"type": "CRE_RULE"},{"id": 100033,"type": "CRE_RULE"}],"security_category_count": 2,"closing_reason_id": 54,"description": "Excessive Firewall Denies Between Hosts\n","last_persisted_time": 1641970583000,"relevance": 3,"category_count": 2,"inactive": true,"local_destination_count": 1,"severity": 5,"status": "CLOSED"}]|
  
Example output:

```
{
  "data": [
    {
      "categories": [
        "Access Denied",
        "ACL Deny"
      ],
      "category_count": 2,
      "credibility": 2,
      "description": "Excessive Firewall Denies Between Hosts\n",
      "destination_networks": [
        "Net-10-172-192.Net_172_16_0_0",
        "other"
      ],
      "device_count": 1,
      "domain_id": 0,
      "event_count": 13493550,
      "first_persisted_time": 1641970466000,
      "flow_count": 0,
      "follow_up": false,
      "id": 42,
      "inactive": false,
      "last_persisted_time": 1642054764000,
      "last_updated_time": 1642054761525,
      "local_destination_address_ids": [
        14
      ],
      "local_destination_count": 1,
      "log_sources": [
        {
          "id": 63,
          "name": "Custom Rule Engine-8 :: ip-172-31-34-93",
          "type_id": 18,
          "type_name": "EventCRE"
        }
      ],
      "magnitude": 4,
      "offense_source": "172.31.34.93",
      "offense_type": 0,
      "policy_category_count": 0,
      "protected": false,
      "relevance": 5,
      "remote_destination_count": 1,
      "rules": [
        {
          "id": 100033,
          "type": "CRE_RULE"
        },
        {
          "id": 100626,
          "type": "CRE_RULE"
        }
      ],
      "security_category_count": 2,
      "severity": 5,
      "source_address_ids": [
        19
      ],
      "source_count": 1,
      "source_network": "Net-10-172-192.Net_172_16_0_0",
      "start_time": 1641970465643,
      "status": "OPEN",
      "username_count": 2
    },
    {
      "categories": [
        "Access Denied",
        "ACL Deny"
      ],
      "category_count": 2,
      "close_time": 1641970533000,
      "closing_reason_id": 54,
      "closing_user": "admin",
      "credibility": 2,
      "description": "Excessive Firewall Denies Between Hosts\n",
      "destination_networks": [
        "Net-10-172-192.Net_172_16_0_0"
      ],
      "device_count": 1,
      "domain_id": 0,
      "event_count": 2429,
      "first_persisted_time": 1641968803000,
      "flow_count": 0,
      "follow_up": false,
      "id": 41,
      "inactive": true,
      "last_persisted_time": 1641970583000,
      "last_updated_time": 1641970524788,
      "local_destination_address_ids": [
        14
      ],
      "local_destination_count": 1,
      "log_sources": [
        {
          "id": 63,
          "name": "Custom Rule Engine-8 :: ip-172-31-34-93",
          "type_id": 18,
          "type_name": "EventCRE"
        }
      ],
      "magnitude": 3,
      "offense_source": "183.82.206.22",
      "offense_type": 0,
      "policy_category_count": 0,
      "protected": false,
      "relevance": 3,
      "remote_destination_count": 0,
      "rules": [
        {
          "id": 100625,
          "type": "CRE_RULE"
        },
        {
          "id": 100033,
          "type": "CRE_RULE"
        }
      ],
      "security_category_count": 2,
      "severity": 5,
      "source_address_ids": [
        22
      ],
      "source_count": 1,
      "source_network": "other",
      "start_time": 1641968802643,
      "status": "CLOSED",
      "username_count": 1
    }
  ]
}
```

#### Start Ariel Search

This action is used to start an Ariel search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|aql|string|None|True|AQL query to perform the search|None|Select * from events|
  
Example input:

```
{
  "aql": "Select * from events"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|search|False|JSON data for the Search|{'completed': False, 'compressed_data_file_count': 0, 'index_file_count': 0, 'progress_details': [], 'record_count': 0, 'compressed_data_total_size': 0, 'data_total_size': 0, 'query_execution_time': 0, 'save_results': False, 'status': 'WAIT', 'cursor_id': '6eaa0819-8d37-452b-bf28-d48acd2adf32', 'data_file_count': 0, 'progress': 0, 'size_on_disk': 0, 'desired_retention_time_msec': 86400000, 'index_total_size': 0, 'processed_record_count': 0, 'query_string': 'Select * from events last 10 MINUTES', 'search_id': '6eaa0819-8d37-452b-bf28-d48acd2adf32', 'subsearch_ids': []}|
  
Example output:

```
{
  "data": {
    "completed": false,
    "compressed_data_file_count": 0,
    "compressed_data_total_size": 0,
    "cursor_id": "6eaa0819-8d37-452b-bf28-d48acd2adf32",
    "data_file_count": 0,
    "data_total_size": 0,
    "desired_retention_time_msec": 86400000,
    "index_file_count": 0,
    "index_total_size": 0,
    "processed_record_count": 0,
    "progress": 0,
    "progress_details": [],
    "query_execution_time": 0,
    "query_string": "Select * from events last 10 MINUTES",
    "record_count": 0,
    "save_results": false,
    "search_id": "6eaa0819-8d37-452b-bf28-d48acd2adf32",
    "size_on_disk": 0,
    "status": "WAIT",
    "subsearch_ids": []
  }
}
```

#### Update Offenses

This action is used to update Offenses

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assigned_to|string|None|False|A user to assign the offense to|None|admin|
|closing_reason_id|string|None|False|The ID of a closing reason. A valid Closing Reason ID must be provided when closing an offense|None|100|
|fields|string|None|False|Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, assigned_to, inactive, offense_source,  offense_type, rules(id), protected, follow_up, status, domain_id, rules, log_sources. More information about the fields can be found in plugin documentation|None|id, rules(id)|
|follow_up|boolean|None|False|Set to true to set the follow up flag on the offense|None|False|
|offense_id|integer|None|True|The ID of the offense to update|None|100|
|protected|boolean|None|False|The ID of a closing reason. A valid Closing Reason ID must be provided when closing an offense|None|False|
|status|string|None|False|The new status for the offense. Set to either open, hidden, or closed. When the status of an offense is being set to closed, a valid Closing Reason ID must be provided. To hide an offense, use the hidden status. To show a previously hidden offense, use the open status|["Open", "Hidden", "Closed", ""]|Open|
  
Example input:

```
{
  "assigned_to": "admin",
  "closing_reason_id": 100,
  "fields": "id, rules(id)",
  "follow_up": false,
  "offense_id": 100,
  "protected": false,
  "status": "Open"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|offense|False|JSON data of the Offense|{'event_count': 4, 'last_updated_time': 1640155212603, 'magnitude': 3, 'start_time': 1640155212500, 'description': 'Multiple Exploit/Malware Types Targeting a Single ...', 'first_persisted_time': 1640155213000, 'follow_up': False, 'inactive': True, 'relevance': 0, 'source_count': 1, 'device_count': 2, 'rules': [{'id': 100113, 'type': 'CRE_RULE'}], 'security_category_count': 3, 'policy_category_count': 0, 'source_network': 'other', 'credibility': 3, 'flow_count': 0, 'local_destination_count': 0, 'offense_type': 1, 'remote_destination_count': 1, 'source_address_ids': [18], 'categories': ['Command Execution', 'Input Validation Exploit'], 'id': 33, 'offense_source': '49.206.13.49', 'protected': False, 'domain_id': 0, 'last_persisted_time': 1642054784000, 'category_count': 3, 'destination_networks': ['other'], 'local_destination_address_ids': [], 'log_sources': [{'type_name': 'VirsecSecurityPlatformCustom', 'id': 23312, 'name': 'Virsec Security Platform', 'type_id': 4013}, {'type_id': 18, 'type_name': 'EventCRE', 'id': 63, 'name': 'Custom Rule Engine-8 :: ip-172-31-34-93'}], 'severity': 9, 'status': 'OPEN', 'username_count': 0}|
  
Example output:

```
{
  "data": {
    "categories": [
      "Command Execution",
      "Input Validation Exploit"
    ],
    "category_count": 3,
    "credibility": 3,
    "description": "Multiple Exploit/Malware Types Targeting a Single ...",
    "destination_networks": [
      "other"
    ],
    "device_count": 2,
    "domain_id": 0,
    "event_count": 4,
    "first_persisted_time": 1640155213000,
    "flow_count": 0,
    "follow_up": false,
    "id": 33,
    "inactive": true,
    "last_persisted_time": 1642054784000,
    "last_updated_time": 1640155212603,
    "local_destination_address_ids": [],
    "local_destination_count": 0,
    "log_sources": [
      {
        "id": 23312,
        "name": "Virsec Security Platform",
        "type_id": 4013,
        "type_name": "VirsecSecurityPlatformCustom"
      },
      {
        "id": 63,
        "name": "Custom Rule Engine-8 :: ip-172-31-34-93",
        "type_id": 18,
        "type_name": "EventCRE"
      }
    ],
    "magnitude": 3,
    "offense_source": "49.206.13.49",
    "offense_type": 1,
    "policy_category_count": 0,
    "protected": false,
    "relevance": 0,
    "remote_destination_count": 1,
    "rules": [
      {
        "id": 100113,
        "type": "CRE_RULE"
      }
    ],
    "security_category_count": 3,
    "severity": 9,
    "source_address_ids": [
      18
    ],
    "source_count": 1,
    "source_network": "other",
    "start_time": 1640155212500,
    "status": "OPEN",
    "username_count": 0
  }
}
```
### Triggers


#### Get New Offenses

This trigger is used to watch for new offenses to trigger on

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fields|string|None|False|Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, assigned_to, inactive, offense_source,  offense_type, rules(id), protected, follow_up, status, domain_id, rules, log_sources. More information about the fields can be found in plugin documentation|None|id, rules(id)|
|filter|string|None|False|Restrict the elements in a list based on the contents of various fields.|None|id=100|
|interval|integer|15|True|How frequently (in seconds) to trigger a greeting|None|15|
|range|string|1-50|False|Paging requests are specified with the Range parameter. E.g. the example default range returns the first 50 records, a custom range of 6-10 returns the 6th to 10th records|None|1-2|
|sort|string|None|False|Apply sorting order to result sets, e.g. +id to sort the result in ascending order of id value|None|+id,-status|
  
Example input:

```
{
  "fields": "id, rules(id)",
  "filter": "id=100",
  "interval": 15,
  "range": "1-50",
  "sort": "+id,-status"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|[]offense|False|JSON data of the Offense|{'create_time': 1642056336657, 'id': 404, 'note_text': 'New Note text', 'username': 'API_user: admin'}|
  
Example output:

```
{
  "data": {
    "create_time": 1642056336657,
    "id": 404,
    "note_text": "New Note text",
    "username": "API_user: admin"
  }
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**error_messages**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Code|string|None|False|Error Code|None|
|Contexts|[]string|None|False|Contexts|None|
|Message|string|None|False|Error message|None|
|Severity|string|None|False|Severity|None|
  
**events**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|QID|integer|None|False|Qid|None|
|Source IP|string|None|False|Source IP|None|
|Source Port|integer|None|False|Source port|None|
|Start Time|integer|None|False|Start time|None|
  
**search**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Compressed Data File Count|integer|None|False|Compressed data file count|None|
|Compressed Data Total Size|integer|None|False|Compressed data total size|None|
|Cursor ID|string|None|False|Cursor ID|None|
|Data File Count|integer|None|False|Data file count|None|
|Data Total Size|integer|None|False|Data total size|None|
|Desired Retention Time Milliseconds|integer|None|False|Desired retention time Milliseconds|None|
|Error Messages|[]error_messages|None|False|Error messages|None|
|Index File Count|integer|None|False|Index file count|None|
|Index Total Size|integer|None|False|Index total size|None|
|Processed Record Count|integer|None|False|Processed record count|None|
|Progress|integer|None|False|Progress|None|
|Progress Details|[]integer|None|False|Progress details|None|
|Query Execution Time|integer|None|False|Query execution time|None|
|Query String|string|None|False|Query string|None|
|Record Count|integer|None|False|Record count|None|
|Save Results|boolean|None|False|Save results|None|
|Search ID|string|None|False|Search ID|None|
|Status|string|None|False|Status|None|
|Sub search IDs|[]string|None|False|Sub search IDs|None|
  
**ip_addresses**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created|integer|None|False|Created|None|
|First Seen Profiler|string|None|False|First seen profiler|None|
|First Seen Scanner|string|None|False|First seen scanner|None|
|ID|integer|None|False|ID|None|
|Last Seen Profiler|string|None|False|Last seen profiler|None|
|Last Seen Scanner|string|None|False|Last seen scanner|None|
|Network ID|integer|None|False|Network ID|None|
|Type|string|None|False|Type|None|
|Value|string|None|False|Value|None|
  
**interfaces**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created|integer|None|False|Created|None|
|First Seen Profiler|string|None|False|First seen profiler|None|
|First Seen Scanner|string|None|False|First seen scanner|None|
|ID|integer|None|False|ID|None|
|IP Addresses|[]ip_addresses|None|False|IP addresses|None|
|Last Seen Profiler|string|None|False|Last seen profiler|None|
|Last Seen Scanner|string|None|False|Last seen scanner|None|
|MAC Address|string|None|False|MAC address|None|
  
**properties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID|None|
|Last Reported|integer|None|False|Last reported|None|
|Last Reported By|string|None|False|Last reported by|None|
|Name|string|None|False|Name|None|
|Type ID|integer|None|False|Type ID|None|
|Value|string|None|False|Value|None|
  
**products**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|First Seen Profiler|string|None|False|First seen profiler|None|
|First Seen Scanner|string|None|False|First seen scanner|None|
|ID|integer|None|False|ID|None|
|Last Scanned For|string|None|False|Last scanned for|None|
|Last Seen Profiler|string|None|False|Last seen profiler|None|
|Last Seen Scanner|string|None|False|Last seen scanner|None|
|Product Variant ID|integer|None|False|Product variant ID|None|
  
**host_urls**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created|integer|None|False|Created|None|
|First Seen Profiler|string|None|False|First seen profiler|None|
|First Seen Scanner|string|None|False|First seen scanner|None|
|ID|integer|None|False|ID|None|
|Last Seen Profiler|string|None|False|Last seen profiler|None|
|Last Seen Scanner|string|None|False|Last seen scanner|None|
|Name|string|None|False|Name|None|
|Type|string|None|False|Type|None|
  
**rules**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID|None|
|Type|string|None|False|Type|None|
  
**log_sources**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID|None|
|Name|string|None|False|Name|None|
|Type ID|integer|None|False|Type ID|None|
|Type Name|string|None|False|Type name|None|
  
**assets**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Domain ID|integer|None|False|Domain ID|None|
|Hostnames|[]host_urls|None|False|Hostnames|None|
|ID|integer|None|False|ID|None|
|Interfaces|[]interfaces|None|False|Interfaces|None|
|Products|[]products|None|False|Products|None|
|Properties|[]properties|None|False|Properties|None|
|Risk Score Sum|float|None|False|Risk score sum|None|
|Users|[]object|None|False|Users|None|
|Vulnerability Count|integer|None|False|Vulnerability count|None|
  
**closing_reason**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID|None|
|Is Deleted|boolean|None|False|Is deleted|None|
|Is Reserved|boolean|None|False|Is reserved|None|
|Text|string|None|False|text|None|
  
**note**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created Time|integer|None|False|Created time|None|
|ID|integer|None|False|ID|None|
|Note Text|string|None|False|Note text|None|
|Username|string|None|False|Username|None|
  
**offense**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assigned To|string|None|False|Assigned to|None|
|Categories|[]string|None|False|Categories|None|
|Category Count|integer|None|False|Category count|None|
|Close Time|integer|None|False|Close time|None|
|Closing Reason ID|integer|None|False|Closing reason ID|None|
|Closing User|string|None|False|Closing user|None|
|Credibility|integer|None|False|Credibility|None|
|Description|string|None|False|Description|None|
|Destination Networks|[]string|None|False|Destination networks|None|
|Device Count|integer|None|False|Device count|None|
|Domain ID|integer|None|False|Domain ID|None|
|Event Count|integer|None|False|Event count|None|
|First Persisted Time|integer|None|False|First persisted time|None|
|Flow Count|integer|None|False|Flow count|None|
|Follow Up|boolean|None|False|Follow up|None|
|ID|integer|None|False|ID|None|
|Inactive|boolean|None|False|Inactive|None|
|Last Persisted Time|integer|None|False|Last persisted time|None|
|Last Updated Time|integer|None|False|Last updated time|None|
|Local Destination Address IDs|[]integer|None|False|Local destination address IDs|None|
|Local Destination Count|integer|None|False|Local destination count|None|
|Log Sources|[]log_sources|None|False|Log sources|None|
|Magnitude|integer|None|False|Magnitude|None|
|Offense Source|string|None|False|Offense source|None|
|Offense Type|integer|None|False|Offense type|None|
|Policy Category Count|integer|None|False|Policy category count|None|
|Protected|boolean|None|False|Protected|None|
|Relevance|integer|None|False|Relevance|None|
|Remote Destination Count|integer|None|False|Remote destination count|None|
|Rules|[]rules|None|False|Rules|None|
|Security Category Count|integer|None|False|Security category count|None|
|Severity|integer|None|False|Severity|None|
|Source Address IDs|[]integer|None|False|Source address IDs|None|
|Source Count|integer|None|False|Source count|None|
|Source Network|string|None|False|Source network|None|
|Start Time|integer|None|False|Start time|None|
|Status|string|None|False|Status|None|
|Username Count|integer|None|False|Username count|None|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History

* 1.1.0 - Adding in new connection test | Updated the SDK to version 5.4.5 | Ran refresh to update all schemas and unit tests
* 1.0.0 - Initial plugin

# Links

* [IBM QRadar](https://www.ibm.com/docs/en/qsip)

## References

* [IBM QRadar API Documentation](https://www.ibm.com/docs/en/qradar-common?topic=170-whats-new-in-rest-api-version)
* [AQL](https://www.ibm.com/docs/en/qradar-on-cloud?topic=structure-sample-aql-queries)