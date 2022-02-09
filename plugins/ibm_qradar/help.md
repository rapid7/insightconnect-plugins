# Description

IBM QRadar reduces billions of events and flows into a manageable number of actionable offenses that are prioritized by their impact on your business operations. This plugin allows you to use IBM QRadar to orchestrate and automate Ariel search queries and automate offense management

# Key Features

- Start Ariel search
- Get Ariel search by ID
- Get offenses
- Get offense closing reasons
- Get assets
- Get offense notes
- Get offense note by ID
- Add note to offense
- Update offense
- Watch for new offenses

# Requirements


# Supported Product Versions

* 7.3.3

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Auth object consisting of username of type string and password of type password|None|{ 'username': 'user1', 'password': 'password'}|
|host_url|string|None|True|Host URL of the QRadar instance.|None|https://example.com|
|verify_ssl|boolean|None|False|Whether to verify the SSL for QRadar connection|None|True|

Example input:

```
{
  "credentials": "{ 'username': 'user1', 'password': 'password'}",
  "host_url": "https://127.0.0.1",
  "verify_ssl": true
}
```

## Technical Details

### Actions

#### Get Offense Notes by ID

This action is used to get Offense Notes by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fields|string|None|False|Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, create_time, username, note_text. More information about the fields can be found in plugin documentation|None|id, note_text|
|note_id|integer|None|True|The ID of the offense note to get|None|100|
|offense_id|integer|None|True|The ID of the offense to get notes for|None|100|

Example input:

```
{
  "fields": "id, note_text",
  "filter": "id=100",
  "offense_id": 100,
  "range": "1-2"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|note|False|JSON data of the Offense Notes for given ID|

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
      "username": "API_user: admin",
      "create_time": 1641451278329,
      "id": 209,
      "note_text": "New Note text"
    }
  ]
}
```

#### Add Notes to Offense

This action is used to add Notes to Offense.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fields|string|None|False|Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, create_time, username, note_text. More information about the fields can be found in plugin documentation|None|id, note_text|
|note_text|string|None|True|The note text to add to the offense|None|note_text|
|offense_id|integer|None|True|The ID of the offense in which to add a note|None|100|

Example input:

```
{
  "fields": "id, note_text",
  "note_text": "note_text",
  "offense_id": 100
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|note|False|JSON data of the newly added Offense Notes |

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

This action is used to get ariel search by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search|False|JSON data of the Search|

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

This action is used to list all assets found in the model.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fields|string|None|False|Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, domain_id, hostnames(id), interfaces, products. More information about the fields can be found in plugin documentation|None|id, hostnames(id)|
|filter|string|None|False|Restrict the elements in a list based on the contents of various fields|None|id = 1001 and vulnerability_count >= 0|
|range|string|1-50|False|Paging requests are specified with the Range parameter. E.g. the example default range returns the first 50 records, a custom range of 6-10 returns the 6th to 10th records|None|1-2|

Example input:

```
{
  "fields": "id, hostnames(id)",
  "filter": "id = 1001 and vulnerability_count \u003e= 0",
  "range": "1-2"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]assets|False|JSON data of the Assets|

Example output:

```
{
  "data": [
    {
      "vulnerability_count": 0,
      "id": 1002,
      "interfaces": [
        {
          "created": 1640265476716,
          "id": 1002,
          "ip_addresses": [
            {
              "type": "IPV4",
              "value": "192.10.10.179",
              "created": 1640265476716,
              "id": 1002,
              "network_id": 2
            }
          ]
        }
      ],
      "risk_score_sum": 0,
      "properties": [
        {
          "name": "Unified Name",
          "type_id": 1002,
          "value": "192.10.10.179",
          "id": 1003,
          "last_reported": 1640265476727,
          "last_reported_by": "USER:admin"
        }
      ],
      "users": [],
      "domain_id": 0,
      "host_urls": [],
      "products": []
    }
  ]
}
```

#### Get Offense's Closing Reasons

This action is used to get Offense's Closing Reasons.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fields|string|None|False|Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, text, is_deleted, is_reserved. More information about the fields can be found in plugin documentation|None|id, is_deleted|
|filter|string|None|False|Restrict the elements in a list based on the contents of various fields. E.g. id=55 and is_deleted = false|None|id=1000|
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
  "range": "1-2"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]closing_reason|False|JSON data of the Offense Closing Reasons|

Example output:

```
{
  "data": [
    {
      "id": 1,
      "is_deleted": false,
      "is_reserved": false,
      "text": "Non-Issue"
    },
    {
      "id": 3,
      "is_deleted": false,
      "is_reserved": false,
      "text": "Policy Violation"
    }
  ]
}
```

#### Get Offense Notes

This action is used to get Offense Notes.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fields|string|None|False|Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, create_time, username, note_text. More information about the fields can be found in plugin documentation|None|id, note_text|
|filter|string|None|False|Restrict the elements in a list based on the contents of various fields. E.g. id=55 and username = admin|None|id=100|
|offense_id|integer|None|True|The ID of the offense to get notes for|None|100|
|range|string|1-50|False|Paging requests are specified with the Range parameter. E.g. the example default range returns the first 50 records, a custom range of 6-10 returns the 6th to 10th records|None|1-2|

Example input:

```
{
  "fields": "id, note_text",
  "filter": "id=100",
  "offense_id": 100,
  "range": "1-2"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]note|False|JSON data of the Offense Notes|

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

This action is used to list all Offenses.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fields|string|None|False|Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, assigned_to, inactive, offense_source,  offense_type, rules(id), protected, follow_up, status, domain_id, rules, log_sources. More information about the fields can be found in plugin documentation|None|id, rules(id)|
|filter|string|None|False|Restrict the elements in a list based on the contents of various fields. E.g.  id=55 and follow_up = false|None|id=1000|
|range|string|1-50|False|Paging requests are specified with the Range parameter. E.g. the example default range returns the first 50 records, a custom range of 6-10 returns the 6th to 10th records|None|1-2|
|sort|string|None|False|Apply sorting order to result sets, e.g. +id to sort the result in ascending order of id value|None|+id,-status|

Example input:

```
{
  "fields": "id, rules(id)",
  "filter": "id=1000",
  "range": "1-2",
  "sort": "+id,-status"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]offense|False|JSON data of the Offense|

Example output:

```
{
  "data": [
    {
      "source_network": "Net-10-172-192.Net_172_16_0_0",
      "domain_id": 0,
      "inactive": false,
      "last_updated_time": 1642054761525,
      "magnitude": 4,
      "offense_source": "172.31.34.93",
      "protected": false,
      "start_time": 1641970465643,
      "category_count": 2,
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
      "event_count": 13493550,
      "id": 42,
      "remote_destination_count": 1,
      "username_count": 2,
      "first_persisted_time": 1641970466000,
      "offense_type": 0,
      "security_category_count": 2,
      "source_count": 1,
      "credibility": 2,
      "description": "Excessive Firewall Denies Between Hosts\n",
      "flow_count": 0,
      "local_destination_address_ids": [
        14
      ],
      "severity": 5,
      "categories": [
        "Access Denied",
        "ACL Deny"
      ],
      "device_count": 1,
      "last_persisted_time": 1642054764000,
      "log_sources": [
        {
          "type_name": "EventCRE",
          "id": 63,
          "name": "Custom Rule Engine-8 :: ip-172-31-34-93",
          "type_id": 18
        }
      ],
      "policy_category_count": 0,
      "relevance": 5,
      "source_address_ids": [
        19
      ],
      "destination_networks": [
        "Net-10-172-192.Net_172_16_0_0",
        "other"
      ],
      "local_destination_count": 1,
      "status": "OPEN",
      "follow_up": false
    },
    {
      "event_count": 2429,
      "flow_count": 0,
      "magnitude": 3,
      "offense_type": 0,
      "source_network": "other",
      "username_count": 1,
      "close_time": 1641970533000,
      "first_persisted_time": 1641968803000,
      "id": 41,
      "last_updated_time": 1641970524788,
      "destination_networks": [
        "Net-10-172-192.Net_172_16_0_0"
      ],
      "device_count": 1,
      "domain_id": 0,
      "local_destination_address_ids": [
        14
      ],
      "policy_category_count": 0,
      "protected": false,
      "start_time": 1641968802643,
      "follow_up": false,
      "log_sources": [
        {
          "id": 63,
          "name": "Custom Rule Engine-8 :: ip-172-31-34-93",
          "type_id": 18,
          "type_name": "EventCRE"
        }
      ],
      "offense_source": "183.82.206.22",
      "source_address_ids": [
        22
      ],
      "source_count": 1,
      "categories": [
        "Access Denied",
        "ACL Deny"
      ],
      "closing_user": "admin",
      "credibility": 2,
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
      "closing_reason_id": 54,
      "description": "Excessive Firewall Denies Between Hosts\n",
      "last_persisted_time": 1641970583000,
      "relevance": 3,
      "category_count": 2,
      "inactive": true,
      "local_destination_count": 1,
      "severity": 5,
      "status": "CLOSED"
    }
  ]
}
```

#### Start Ariel Search

This action is used to start Ariel Search.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|aql|string|None|True|AQL query to perform the search|None|Select * from events|

Example input:

```
{
  "aql": "Select * from events"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search|False|JSON data for the Search|

Example output:

```
{
  "data": {
    "completed": false,
    "compressed_data_file_count": 0,
    "index_file_count": 0,
    "progress_details": [],
    "record_count": 0,
    "compressed_data_total_size": 0,
    "data_total_size": 0,
    "query_execution_time": 0,
    "save_results": false,
    "status": "WAIT",
    "cursor_id": "6eaa0819-8d37-452b-bf28-d48acd2adf32",
    "data_file_count": 0,
    "progress": 0,
    "size_on_disk": 0,
    "desired_retention_time_msec": 86400000,
    "index_total_size": 0,
    "processed_record_count": 0,
    "query_string": "Select * from events last 10 MINUTES",
    "search_id": "6eaa0819-8d37-452b-bf28-d48acd2adf32",
    "subsearch_ids": []
  }
}
```

#### Update Offenses

This action is used to update Offenses.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assigned_to|string|None|False|A user to assign the offense to|None|admin|
|closing_reason_id|string|None|False|The ID of a closing reason. A valid Closing Reason ID must be provided when closing an offense|None|100|
|fields|string|None|False|Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, assigned_to, inactive, offense_source,  offense_type, rules(id), protected, follow_up, status, domain_id, rules, log_sources. More information about the fields can be found in plugin documentation|None|id, rules(id)|
|follow_up|boolean|None|False|Set to true to set the follow up flag on the offense|None|False|
|offense_id|integer|None|True|The ID of the offense to update|None|100|
|protected|boolean|None|False|The ID of a closing reason. A valid Closing Reason ID must be provided when closing an offense|None|False|
|status|string|None|False|The new status for the offense. Set to either open, hidden, or closed. When the status of an offense is being set to closed, a valid Closing Reason ID must be provided. To hide an offense, use the hidden status. To show a previously hidden offense, use the open status|['Open', 'Hidden', 'Closed', '']|Open|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|offense|False|JSON data of the Offense|

Example output:

```
{
  "data": {
    "event_count": 4,
    "last_updated_time": 1640155212603,
    "magnitude": 3,
    "start_time": 1640155212500,
    "description": "Multiple Exploit/Malware Types Targeting a Single ...",
    "first_persisted_time": 1640155213000,
    "follow_up": false,
    "inactive": true,
    "relevance": 0,
    "source_count": 1,
    "device_count": 2,
    "rules": [
      {
        "id": 100113,
        "type": "CRE_RULE"
      }
    ],
    "security_category_count": 3,
    "policy_category_count": 0,
    "source_network": "other",
    "credibility": 3,
    "flow_count": 0,
    "local_destination_count": 0,
    "offense_type": 1,
    "remote_destination_count": 1,
    "source_address_ids": [
      18
    ],
    "categories": [
      "Command Execution",
      "Input Validation Exploit"
    ],
    "id": 33,
    "offense_source": "49.206.13.49",
    "protected": false,
    "domain_id": 0,
    "last_persisted_time": 1642054784000,
    "category_count": 3,
    "destination_networks": [
      "other"
    ],
    "local_destination_address_ids": [],
    "log_sources": [
      {
        "type_name": "VirsecSecurityPlatformCustom",
        "id": 23312,
        "name": "Virsec Security Platform",
        "type_id": 4013
      },
      {
        "type_id": 18,
        "type_name": "EventCRE",
        "id": 63,
        "name": "Custom Rule Engine-8 :: ip-172-31-34-93"
      }
    ],
    "severity": 9,
    "status": "OPEN",
    "username_count": 0
  }
}
```

### Triggers

#### Get New Offenses

This trigger is used to list all New Offenses.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fields|string|None|False|Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, assigned_to, inactive, offense_source,  offense_type, rules(id), protected, follow_up, status, domain_id, rules, log_sources. More information about the fields can be found in plugin documentation|None|id, rules(id)|
|filter|string|None|False|Restrict the elements in a list based on the contents of various fields. E.g. id=55 and follow_up = false|None|id=100|
|interval|integer|15|True|How frequently (in seconds) to trigger a greeting|None|15|
|range|string|1-50|False|Paging requests are specified with the Range parameter. E.g. the example default range returns the first 50 records, a custom range of 6-10 returns the 6th to 10th records|None|1-2|
|sort|string|None|False|Apply sorting order to result sets, e.g. +id to sort the result in ascending order of id value|None|+id,-status|

Example input:

```
{
  "fields": "id, rules(id)",
  "filter": "id=100",
  "interval": 15,
  "range": "1-2",
  "sort": "+id,-status"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]offense|False|JSON data of the Offense|

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
      "event_count": 13961944,
      "first_persisted_time": 1641970466000,
      "flow_count": 0,
      "follow_up": false,
      "id": 42,
      "inactive": false,
      "last_persisted_time": 1642056328000,
      "last_updated_time": 1642056321285,
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
        },
        {
          "id": 100475,
          "type": "CRE_RULE"
        },
        {
          "id": 100426,
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

### Custom Output Types

#### assets

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Domain Id|integer|False|Domain id|
|Hostnames|[]host_urls|False|Hostnames|
|Id|integer|False|Id|
|Interfaces|[]interfaces|False|Interfaces|
|Products|[]products|False|Products|
|Properties|[]properties|False|Properties|
|Risk Score Sum|float|False|Risk score sum|
|Users|[]object|False|Users|
|Vulnerability Count|integer|False|Vulnerability count|

#### closing_reason

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|integer|False|Id|
|Is Deleted|boolean|False|Is Deleted|
|Is Reserved|boolean|False|Is Reserved|
|text|string|False|text|

#### error_messages

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Code|string|False|Code|
|Contexts|[]string|False|Contexts|
|Message|string|False|Message|
|Severity|string|False|Severity|

#### events

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Qid|integer|False|Qid|
|Sourceip|string|False|Sourceip|
|Sourceport|integer|False|Sourceport|
|Starttime|integer|False|Starttime|

#### host_urls

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created|integer|False|Created|
|First Seen Profiler|string|False|First seen profiler|
|First Seen Scanner|string|False|First seen scanner|
|Id|integer|False|Id|
|Last Seen Profiler|string|False|Last seen profiler|
|Last Seen Scanner|string|False|Last seen scanner|
|Name|string|False|Name|
|Type|string|False|Type|

#### interfaces

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created|integer|False|Created|
|First Seen Profiler|string|False|First seen profiler|
|First Seen Scanner|string|False|First seen scanner|
|Id|integer|False|Id|
|IP Addresses|[]ip_addresses|False|IP addresses|
|Last Seen Profiler|string|False|Last seen profiler|
|Last Seen Scanner|string|False|Last seen scanner|
|MAC Address|string|False|MAC address|

#### ip_addresses

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created|integer|False|Created|
|First Seen Profiler|string|False|First seen profiler|
|First Seen Scanner|string|False|First seen scanner|
|Id|integer|False|Id|
|Last Seen Profiler|string|False|Last seen profiler|
|Last Seen Scanner|string|False|Last seen scanner|
|Network Id|integer|False|Network id|
|Type|string|False|Type|
|Value|string|False|Value|

#### log_sources

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|integer|False|Id|
|Name|string|False|Name|
|Type Id|integer|False|Type id|
|Type Name|string|False|Type name|

#### note

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created Time|integer|False|Created Time|
|Id|integer|False|Id|
|Note text|string|False|Note text|
|Username|string|False|Username|

#### offense

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Assigned To|string|False|Assigned to|
|Categories|[]string|False|Categories|
|Category Count|integer|False|Category count|
|Close Time|integer|False|Close time|
|Closing Reason Id|integer|False|Closing reason id|
|Closing User|string|False|Closing user|
|Credibility|integer|False|Credibility|
|Description|string|False|Description|
|Destination Networks|[]string|False|Destination networks|
|Device Count|integer|False|Device count|
|Domain Id|integer|False|Domain id|
|Event Count|integer|False|Event count|
|First Persisted Time|integer|False|First persisted time|
|Flow Count|integer|False|Flow count|
|Follow Up|boolean|False|Follow up|
|Id|integer|False|Id|
|Inactive|boolean|False|Inactive|
|Last Persisted Time|integer|False|Last persisted time|
|Last Updated Time|integer|False|Last updated time|
|Local Destination Address Ids|[]integer|False|Local destination address ids|
|Local Destination Count|integer|False|Local destination count|
|Log Sources|[]log_sources|False|Log sources|
|Magnitude|integer|False|Magnitude|
|Offense Source|string|False|Offense source|
|Offense Type|integer|False|Offense type|
|Policy Category Count|integer|False|Policy category count|
|Protected|boolean|False|Protected|
|Relevance|integer|False|Relevance|
|Remote Destination Count|integer|False|Remote destination count|
|Rules|[]rules|False|Rules|
|Security Category Count|integer|False|Security category count|
|Severity|integer|False|Severity|
|Source Address Ids|[]integer|False|Source address ids|
|Source Count|integer|False|Source count|
|Source Network|string|False|Source network|
|Start Time|integer|False|Start time|
|Status|string|False|Status|
|Username Count|integer|False|Username count|

#### products

|Name|Type|Required|Description|
|----|----|--------|-----------|
|First Seen Profiler|string|False|First seen profiler|
|First Seen Scanner|string|False|First seen scanner|
|Id|integer|False|Id|
|Last Scanned For|string|False|Last scanned for|
|Last Seen Profiler|string|False|Last seen profiler|
|Last Seen Scanner|string|False|Last seen scanner|
|Product Variant Id|integer|False|Product variant id|

#### properties

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|integer|False|Id|
|Last Reported|integer|False|Last reported|
|Last Reported By|string|False|Last reported by|
|Name|string|False|Name|
|Type Id|integer|False|Type id|
|Value|string|False|Value|

#### rules

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|integer|False|Id|
|Type|string|False|Type|

#### search

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Compressed Data File Count|integer|False|Compressed data file count|
|Compressed Data Total Size|integer|False|Compressed data total size|
|Cursor Id|string|False|Cursor id|
|Data File Count|integer|False|Data file count|
|Data Total Size|integer|False|Data total size|
|Desired Retention Time Msec|integer|False|Desired retention time msec|
|Error Messages|[]error_messages|False|Error messages|
|Index File Count|integer|False|Index file count|
|Index Total Size|integer|False|Index total size|
|Processed Record Count|integer|False|Processed record count|
|Progress|integer|False|Progress|
|Progress Details|[]integer|False|Progress details|
|Query Execution Time|integer|False|Query execution time|
|Query String|string|False|Query string|
|Record Count|integer|False|Record count|
|Save Results|boolean|False|Save results|
|Search Id|string|False|Search id|
|Status|string|False|Status|
|Subsearch Ids|[]string|False|Subsearch ids|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [IBM QRadar](https://www.ibm.com/docs/en/qsip)
* [IBM QRadar API Documentation](https://www.ibm.com/docs/en/qradar-common?topic=170-whats-new-in-rest-api-version)
* [AQL](https://www.ibm.com/docs/en/qradar-on-cloud?topic=structure-sample-aql-queries)

