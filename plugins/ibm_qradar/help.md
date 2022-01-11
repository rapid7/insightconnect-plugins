# Description

IBM QRadar reduces billions of events and flows into a manageable number of actionable offenses that are prioritized by their impact on your business operations. This plugin allows you to use IBM QRadar to orchestrate and automate Ariel search queries and automate offense management.

# Key Features

- Start Ariel Search
- Get Ariel Search By ID
- Get Offenses
- Get offense Closing Reasons
- Get Assets
- Get Offense Notes
- Get Offense Note By ID
- Add Note To Offense
- Update Offense
- Trigger : Get New Offenses


# Requirements

# Supported Product Versions

* 7.3.3

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hostname|string|None|True|Hostname for the QRadar application|None|None|
|password|password|None|True|QRadar Password|None|None|
|username|string|None|True|QRadar Username|None|None|

Example input:

```
"connection": {
      "hostname": "hostname",
      "password": "password",
      "username": "username"
    },
```

## Technical Details

### Actions

#### Add Notes to Offense

This action is used to add Notes to Offense.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fields|string|None|False|Use this parameter to specify which fields you would like to get back in the response. fields that are not named are excluded. Specify subfields in brackets and multiple fields in the same object are separated by commas.|None|None|
|note_text|string|None|True|The Note Text to add to offense.|None|None|
|offense_id|integer|None|True|The ID of the offense in which you want to add note.|None|None|

Example input:

```
{
  "body": {
    "action": "add_notes_to_offense",
    "connection": {
      "hostname": "hostname",
      "password": "password",
      "username": "username"
    },
    "input": {
      "fields": "",
      "note_text": "New Note text",
      "offense_id": 33
    },
    "meta": {}
  },
  "type": "action_start",
  "version": "v1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|note|False|Json Data of the newly added Offense Notes |

Example output:

```
{
  "data": {
    "create_time": 1641447330657,
    "id": 201,
    "note_text": "New Note text",
    "username": "API_user: admin"
  }
}

```

#### Get Ariel Search By Id

This action is used to get Ariel Search By Id.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|poll_interval|number|None|False|Poll interval is the number of seconds to recheck until the search gets COMPLETED.|None|None|
|search_id|string|None|True|Specific Search Id|None|None|

Example input:

```
{
  "body": {
    "action": "get_ariel_search_by_id",
    "connection": {
      "hostname": "hostname",
      "password": "password",
      "username": "username"
    },
    "input": {
      "poll_interval": 0,
      "search_id": "74b4f184-6e03-41be-8494-2a1c9f6f2faa"
    },
    "meta": {}
  },
  "type": "action_start",
  "version": "v1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search|False|Json Data of the Search|

Example output:

```
{
  "data": {
    "desired_retention_time_msec": 86400000,
    "progress": 100,
    "search_id": "74b4f184-6e03-41be-8494-2a1c9f6f2faa",
    "cursor_id": "74b4f184-6e03-41be-8494-2a1c9f6f2faa",
    "status": "COMPLETED",
    "completed": true,
    "data_total_size": 830,
    "index_file_count": 0,
    "processed_record_count": 10,
    "query_string": "SELECT \"Flow Source\", avg(\"AVG_Flows per Second - ...",
    "record_count": 1,
    "subsearch_ids": [],
    "compressed_data_file_count": 0,
    "data_file_count": 10,
    "index_total_size": 0,
    "progress_details": [],
    "query_execution_time": 16,
    "save_results": false,
    "size_on_disk": 61,
    "compressed_data_total_size": 0
  }
}
```

#### Get Assets

This action is used to list all assets found in the model.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fields|string|None|False|Use this parameter to specify which fields you would like to get back in the response. Fields that are not named are excluded. Specify subfields in brackets and multiple fields in the same object are separated by commas.|None|None|
|filter|string|None|False|This parameter is used to restrict the elements in a list base on the contents of various fields.|None|None|
|range|string|None|False|Use this parameter to restrict the number of elements that are returned in the list to a specified range. The list is indexed starting at zero.|None|None|

Example input:

```
{
  "body": {
    "action": "get_assets",
    "connection": {
      "hostname": "hostname",
      "password": "password",
      "username": "username"
    },
    "input": {
      "fields": "",
      "filter": "",
      "range": ""
    },
    "meta": {}
  },
  "type": "action_start",
  "version": "v1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]assets|False|Json Data of the Assets|

Example output:

```
{
  "data": [
    {
      "users": [],
      "domain_id": 0,
      "interfaces": [],
      "properties": [],
      "risk_score_sum": 0,
      "hostnames": [],
      "id": 0,
      "products": [],
      "vulnerability_count": 0
    },
    {
      "properties": [
        {
          "value": "TEst",
          "id": 1000,
          "last_reported": 1640264696400,
          "last_reported_by": "USER:admin",
          "name": "Given Name",
          "type_id": 1001
        },
        {
          "last_reported_by": "USER:admin",
          "name": "Unified Name",
          "type_id": 1002,
          "value": "TEst",
          "id": 1001,
          "last_reported": 1640264698711
        }
      ],
      "users": [],
      "products": [
        {
          "id": 1000,
          "product_variant_id": 40335
        }
      ],
      "hostnames": [
        {
          "id": 1001,
          "name": "example.com",
          "type": "DNS",
          "created": 1640582726381
        }
      ],
      "id": 1001,
      "interfaces": [
        {
          "created": 1640264696400,
          "id": 1001,
          "ip_addresses": [
            {
              "created": 1640264696400,
              "id": 1001,
              "network_id": 2,
              "type": "IPV4",
              "value": "192.10.10.178"
            }
          ]
        }
      ],
      "risk_score_sum": 0,
      "vulnerability_count": 0,
      "domain_id": 0
    }
  ]
}
```

#### Get Offense's Closing Reasons

This action is used to get Offense's Closing Reasons.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fields|string|None|False|Use this parameter to specify which fields you would like to get back in the response. Fields that are not named are excluded. Specify subfields in brackets and multiple fields in the same object are separated by commas.|None|None|
|filter|string|None|False|This parameter is used to restrict the elements in a list base on the contents of various fields.|None|None|
|include_deleted|boolean|None|False|If true, deleted closing reasons are included in the response. Defaults to false. Deleted closing reasons cannot be used to close an offense.|None|None|
|include_reserved|boolean|None|False|If true, reserved closing reasons are included in the response. Defaults to false. Reserved closing reasons cannot be used to close an offense.|None|None|
|range|string|None|False|Use this parameter to restrict the number of elements that are returned in the list to a specified range. The list is indexed starting at zero.|None|None|

Example input:

```
{
  "body": {
    "action": "get_offense_closing_reasons",
    "connection": {
      "hostname": "hostname",
      "password": "password",
      "username": "username"
    },
    "input": {
      "fields": "",
      "filter": "",
      "include_deleted": false,
      "include_reserved": false,
      "range": "1-2"
    },
    "meta": {}
  },
  "type": "action_start",
  "version": "v1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]closing_reason|False|Json Data of the Offense Closing Reasons|

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
|fields|string|None|False|Use this parameter to specify which fields you would like to get back in the response. Fields that are not named are excluded. Specify subfields in brackets and multiple fields in the same object are separated by commas.|None|None|
|filter|string|None|False|This parameter is used to restrict the elements in a list base on the contents of various fields.|None|None|
|offense_id|integer|None|True|The ID of the offense to get its notes.|None|None|
|range|string|None|False|Use this parameter to restrict the number of elements that are returned in the list to a specified range. The list is indexed starting at zero.|None|None|

Example input:

```
{
  "body": {
    "action": "get_offense_note",
    "connection": {
      "hostname": "hostname",
      "password": "password",
      "username": "username"
    },
    "input": {
      "fields": "",
      "filter": "",
      "offense_id": 33,
      "range": ""
    },
    "meta": {}
  },
  "type": "action_start",
  "version": "v1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]note|False|Json Data of the Offense Notes|

Example output:

```
{
  "data": [
    {
      "create_time": 1641385258725,
      "id": 157,
      "note_text": "New Note text",
      "username": "API_user: admin"
    },
    {
      "id": 159,
      "note_text": "New Note text",
      "username": "API_user: admin",
      "create_time": 1641385946573
    }
  ]
}
```

#### Get Offense Notes By Id

This action is used to get Offense Notes By Id.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fields|string|None|False|Use this parameter to specify which fields you would like to get back in the response. Fields that are not named are excluded. Specify subfields in brackets and multiple fields in the same object are separated by commas.|None|None|
|note_id|integer|None|True|The ID of the offense note to get.|None|None|
|offense_id|integer|None|True|The ID of the offense to get its notes.|None|None|

Example input:

```
{
  "body": {
    "action": "get_offense_note_by_id",
    "connection": {
      "hostname": "hostname",
      "password": "password",
      "username": "username"
    },
    "input": {
      "fields": "",
      "note_id": 51,
      "offense_id": 33
    },
    "meta": {}
  },
  "type": "action_start",
  "version": "v1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|note|False|Json Data of the Offense Notes for given id.|

Example output:

```
{
  "data": {
    "create_time": 1640936459993,
    "id": 51,
    "note_text": "Test ",
    "username": "API_user: admin"
  }
}

```

#### Get Offenses

This action is used to list all Offenses.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fields|string|None|False|Use this parameter to specify which fields you would like to get back in the response. Fields that are not named are excluded. Specify subfields in brackets and multiple fields in the same object are separated by commas.|None|None|
|filter|string|None|False|This parameter is used to restrict the elements in a list base on the contents of various fields.|None|None|
|range|string|None|False|Use this parameter to restrict the number of elements that are returned in the list to a specified range. The list is indexed starting at zero.|None|None|
|sort|string|None|False|Use parameter to sort the elements in a list.|None|None|

Example input:

```
{
  "body": {
    "action": "get_offenses",
     "connection": {
      "hostname": "hostname",
      "password": "password",
      "username": "username"
    },
    "input": {
      "fields": "",
      "filter": "",
      "range": "",
      "sort": ""
    },
    "meta": {}
  },
  "type": "action_start",
  "version": "v1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]offense|False|Json Data of the Offense|

Example output:

```
{
  "data": [
    {
      "offense_source": "127.0.0.1",
      "policy_category_count": 0,
      "rules": [
        {
          "id": 100475,
          "type": "CRE_RULE"
        }
      ],
      "severity": 6,
      "description": "Access Denied\n",
      "follow_up": false,
      "inactive": true,
      "local_destination_count": 0,
      "source_address_ids": [
        21
      ],
      "source_network": "other",
      "remote_destination_count": 1,
      "start_time": 1641362102216,
      "security_category_count": 1,
      "destination_networks": [
        "other"
      ],
      "flow_count": 0,
      "id": 40,
      "status": "OPEN",
      "relevance": 2,
      "source_count": 1,
      "categories": [
        "Access Denied"
      ],
      "domain_id": 0,
      "log_sources": [
        {
          "id": 63,
          "name": "Custom Rule Engine-8 :: ip-172-31-34-93",
          "type_id": 18,
          "type_name": "EventCRE"
        }
      ],
      "magnitude": 3,
      "offense_type": 0,
      "category_count": 1,
      "first_persisted_time": 1641362102000,
      "last_persisted_time": 1641364295000,
      "last_updated_time": 1641362102216,
      "protected": false,
      "username_count": 0,
      "credibility": 3,
      "device_count": 1,
      "event_count": 1,
      "local_destination_address_ids": []
    },
    {
      "flow_count": 0,
      "last_updated_time": 1641381314500,
      "offense_type": 0,
      "security_category_count": 1,
      "source_address_ids": [
        20
      ],
      "categories": [
        "Access Denied"
      ],
      "credibility": 3,
      "first_persisted_time": 1641359712000,
      "last_persisted_time": 1641383499000,
      "source_count": 1,
      "local_destination_address_ids": [
        14
      ],
      "magnitude": 4,
      "rules": [
        {
          "id": 100425,
          "type": "CRE_RULE"
        }
      ],
      "category_count": 1,
      "domain_id": 0,
      "local_destination_count": 1,
      "log_sources": [
        {
          "name": "Custom Rule Engine-8 :: ip-172-31-34-93",
          "type_id": 18,
          "type_name": "EventCRE",
          "id": 63
        }
      ],
      "policy_category_count": 0,
      "description": "Access Denied\n",
      "relevance": 3,
      "severity": 6,
      "source_network": "other",
      "status": "OPEN",
      "event_count": 308,
      "follow_up": false,
      "username_count": 2,
      "destination_networks": [
        "Net-10-172-192.Net_172_16_0_0",
        "other"
      ],
      "id": 39,
      "inactive": true,
      "protected": false,
      "remote_destination_count": 1,
      "device_count": 1,
      "offense_source": "169.254.3.3",
      "start_time": 1641359711660
    }
  ]
}
```

#### Start Ariel Search

This action is used to start Ariel Search.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|aql|string|None|True|AQL query to perform the search.|None|None|

Example input:

```
{
  "body": {
    "action": "start_ariel_search",
    "connection": {
      "hostname": "hostname",
      "password": "password",
      "username": "username"
    },
    "input": {
      "aql": "Select * from events last 10 MINUTES"
    },
    "meta": {}
  },
  "type": "action_start",
  "version": "v1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|search|False|Json Data of the Search|

Example output:

```
{
  "data": {
    "save_results": false,
    "search_id": "9102cb1d-5994-4f78-8f08-16c6f6991015",
    "status": "WAIT",
    "subsearch_ids": [],
    "data_file_count": 8,
    "query_execution_time": 0,
    "data_total_size": 1553001,
    "index_total_size": 0,
    "record_count": 0,
    "size_on_disk": 0,
    "completed": false,
    "cursor_id": "9102cb1d-5994-4f78-8f08-16c6f6991015",
    "query_string": "Select * from events last 10 MINUTES",
    "compressed_data_file_count": 0,
    "progress": 0,
    "index_file_count": 0,
    "processed_record_count": 0,
    "progress_details": [],
    "compressed_data_total_size": 0,
    "desired_retention_time_msec": 86400000
  }
}
```

#### Update Offenses

This action is used to update Offenses.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assigned_to|string|None|False|A user to assign the offense to.|None|None|
|closing_reason_id|string|None|False|The ID of a closing reason. You must provide a valid closing_reason_id when you close an offense.|None|None|
|fields|string|None|False|Use this parameter to specify which fields you would like to get back in the response. Fields that are not named are excluded. Specify subfields in brackets and multiple fields in the same object are separated by commas.|None|None|
|follow_up|boolean|None|False|Set to true to set the follow up flag on the offense.|None|None|
|offense_id|integer|None|True|The ID of the offense to update.|None|None|
|protected|boolean|None|False|The ID of a closing reason. You must provide a valid closing_reason_id when you close an offense.|None|None|
|status|string|None|False|The new status for the offense. Set to one of the OPEN, HIDDEN, CLOSED. When the status of an offense is being set to CLOSED, a valid closing_reason_id must be provided. To hide an offense, use the HIDDEN status. To show a previously hidden offense, use the OPEN status.|['OPEN', 'HIDDEN', 'CLOSED', '']|None|

Example input:

```
{
  "body": {
    "action": "update_offense",
    "connection": {
      "hostname": "hostname",
      "password": "password",
      "username": "username"
    },
    "input": {
      "assigned_to:": "",
      "fields": "",
      "follow_up": false,
      "offense_id": 33,
      "protected": false,
      "status" : "OPEN"
    },
    "meta": {}
  },
  "type": "action_start",
  "version": "v1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|offense|False|Json Data of the Offense|

Example output:

```
{
  "data": {
    "category_count": 3,
    "description": "Multiple Exploit/Malware Types Targeting a Single ...",
    "inactive": true,
    "magnitude": 3,
    "remote_destination_count": 1,
    "device_count": 2,
    "flow_count": 0,
    "local_destination_address_ids": [],
    "source_network": "other",
    "follow_up": false,
    "id": 33,
    "protected": false,
    "relevance": 0,
    "username_count": 0,
    "last_persisted_time": 1641447357000,
    "last_updated_time": 1640155212603,
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
    "offense_source": "49.206.13.49",
    "offense_type": 1,
    "credibility": 3,
    "local_destination_count": 0,
    "severity": 9,
    "source_address_ids": [
      18
    ],
    "source_count": 1,
    "start_time": 1640155212500,
    "categories": [
      "Command Execution",
      "Input Validation Exploit"
    ],
    "domain_id": 0,
    "event_count": 4,
    "policy_category_count": 0,
    "security_category_count": 3,
    "destination_networks": [
      "other"
    ],
    "first_persisted_time": 1640155213000,
    "rules": [
      {
        "id": 100113,
        "type": "CRE_RULE"
      }
    ],
    "status": "OPEN"
  }
}
```

### Triggers

#### Get New Offenses

This trigger is used to list all New Offenses.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fields|string|None|False|Use this parameter to specify which fields you would like to get back in the response. Fields that are not named are excluded. Specify subfields in brackets and multiple fields in the same object are separated by commas.|None|None|
|filter|string|None|False|This parameter is used to restrict the elements in a list base on the contents of various fields.|None|None|
|interval|integer|15|True|How frequently (in seconds) to trigger a greeting|None|None|
|range|string|None|False|Use this parameter to restrict the number of elements that are returned in the list to a specified range. The list is indexed starting at zero.|None|None|
|sort|string|None|False|Use parameter to sort the elements in a list.|None|None|

Example input:

```
{
  "body": {
    "connection": {
      "hostname": "hostname",
      "password": "password",
      "username": "username"
    },
    "dispatcher": {
      "url": "http://localhost:8000",
      "webhook_url": ""
    },
    "input": {
      "fields": "",
      "filter": "",
      "range": "",
      "sort": "",
      "interval": 15
    },
    "meta": {},
    "trigger": "get_new_offense"
  },
  "type": "trigger_start",
  "version": "v1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]offense|False|Json Data of the Offense|

Example output:

```
{
  "data": [
    {
      "categories": [
        "Access Denied"
      ],
      "category_count": 1,
      "credibility": 3,
      "description": "Access Denied\n",
      "destination_networks": [
        "other"
      ],
      "device_count": 1,
      "domain_id": 0,
      "event_count": 1,
      "first_persisted_time": 1641362102000,
      "flow_count": 0,
      "follow_up": false,
      "id": 40,
      "inactive": true,
      "last_persisted_time": 1641364295000,
      "last_updated_time": 1641362102216,
      "local_destination_address_ids": [],
      "local_destination_count": 0,
      "log_sources": [
        {
          "id": 63,
          "name": "Custom Rule Engine-8 :: ip-172-31-34-93",
          "type_id": 18,
          "type_name": "EventCRE"
        }
      ],
      "magnitude": 3,
      "offense_source": "127.0.0.1",
      "offense_type": 0,
      "policy_category_count": 0,
      "protected": false,
      "relevance": 2,
      "remote_destination_count": 1,
      "rules": [
        {
          "id": 100475,
          "type": "CRE_RULE"
        }
      ],
      "security_category_count": 1,
      "severity": 6,
      "source_address_ids": [
        21
      ],
      "source_count": 1,
      "source_network": "other",
      "start_time": 1641362102216,
      "status": "OPEN",
      "username_count": 0
    },
    {
      "categories": [
        "Access Denied"
      ],
      "category_count": 1,
      "credibility": 3,
      "description": "Access Denied\n",
      "destination_networks": [
        "Net-10-172-192.Net_172_16_0_0",
        "other"
      ],
      "device_count": 1,
      "domain_id": 0,
      "event_count": 308,
      "first_persisted_time": 1641359712000,
      "flow_count": 0,
      "follow_up": false,
      "id": 39,
      "inactive": true,
      "last_persisted_time": 1641383499000,
      "last_updated_time": 1641381314500,
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
      "offense_source": "169.254.3.3",
      "offense_type": 0,
      "policy_category_count": 0,
      "protected": false,
      "relevance": 3,
      "remote_destination_count": 1,
      "rules": [
        {
          "id": 100425,
          "type": "CRE_RULE"
        }
      ],
      "security_category_count": 1,
      "severity": 6,
      "source_address_ids": [
        20
      ],
      "source_count": 1,
      "source_network": "other",
      "start_time": 1641359711660,
      "status": "OPEN",
      "username_count": 2
    },
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
      "event_count": 60839680,
      "first_persisted_time": 1640866551000,
      "flow_count": 0,
      "follow_up": false,
      "id": 38,
      "inactive": false,
      "last_persisted_time": 1641447333000,
      "last_updated_time": 1641447324141,
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
          "id": 100376,
          "type": "CRE_RULE"
        },
        {
          "id": 100426,
          "type": "CRE_RULE"
        },
        {
          "id": 100475,
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
      "start_time": 1640866550800,
      "status": "OPEN",
      "username_count": 2
    },
    {
      "assigned_to": "admin",
      "categories": [
        "Access Denied"
      ],
      "category_count": 1,
      "close_time": 1641283132000,
      "closing_reason_id": 3,
      "closing_user": "API_user: admin",
      "credibility": 3,
      "description": "Access Denied\n",
      "destination_networks": [
        "Net-10-172-192.Net_172_16_0_0",
        "other"
      ],
      "device_count": 1,
      "domain_id": 0,
      "event_count": 23023,
      "first_persisted_time": 1640847826000,
      "flow_count": 0,
      "follow_up": true,
      "id": 37,
      "inactive": true,
      "last_persisted_time": 1641283171000,
      "last_updated_time": 1640954519128,
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
      "magnitude": 2,
      "offense_source": "169.254.3.3",
      "offense_type": 0,
      "policy_category_count": 0,
      "protected": true,
      "relevance": 0,
      "remote_destination_count": 1,
      "rules": [
        {
          "id": 100425,
          "type": "CRE_RULE"
        }
      ],
      "security_category_count": 1,
      "severity": 6,
      "source_address_ids": [
        20
      ],
      "source_count": 1,
      "source_network": "other",
      "start_time": 1640847826007,
      "status": "CLOSED",
      "username_count": 1
    },
    {
      "assigned_to": "admin",
      "categories": [
        "Access Denied",
        "ACL Deny"
      ],
      "category_count": 2,
      "close_time": 1640866535000,
      "closing_reason_id": 2,
      "closing_user": "API_user: admin",
      "credibility": 2,
      "description": "Excessive Firewall Denies Between Hosts\n",
      "destination_networks": [
        "Net-10-172-192.Net_172_16_0_0",
        "other"
      ],
      "device_count": 1,
      "domain_id": 0,
      "event_count": 10546223,
      "first_persisted_time": 1640776031000,
      "flow_count": 0,
      "follow_up": false,
      "id": 36,
      "inactive": true,
      "last_persisted_time": 1640866575000,
      "last_updated_time": 1640866517848,
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
      "magnitude": 2,
      "offense_source": "172.31.34.93",
      "offense_type": 0,
      "policy_category_count": 0,
      "protected": true,
      "relevance": 0,
      "remote_destination_count": 1,
      "rules": [
        {
          "id": 100033,
          "type": "CRE_RULE"
        },
        {
          "id": 100376,
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
      "start_time": 1640776030467,
      "status": "CLOSED",
      "username_count": 2
    },
    {
      "categories": [
        "Access Denied"
      ],
      "category_count": 1,
      "close_time": 1640776007000,
      "closing_reason_id": 2,
      "closing_user": "API_user: admin",
      "credibility": 3,
      "description": "Access Denied\n",
      "destination_networks": [
        "other"
      ],
      "device_count": 1,
      "domain_id": 0,
      "event_count": 18558,
      "first_persisted_time": 1640775851000,
      "flow_count": 0,
      "follow_up": true,
      "id": 35,
      "inactive": true,
      "last_persisted_time": 1640776050000,
      "last_updated_time": 1640776000385,
      "local_destination_address_ids": [],
      "local_destination_count": 0,
      "log_sources": [
        {
          "id": 63,
          "name": "Custom Rule Engine-8 :: ip-172-31-34-93",
          "type_id": 18,
          "type_name": "EventCRE"
        }
      ],
      "magnitude": 2,
      "offense_source": "172.31.34.93",
      "offense_type": 0,
      "policy_category_count": 0,
      "protected": false,
      "relevance": 0,
      "remote_destination_count": 1,
      "rules": [
        {
          "id": 100033,
          "type": "CRE_RULE"
        },
        {
          "id": 100376,
          "type": "CRE_RULE"
        }
      ],
      "security_category_count": 1,
      "severity": 5,
      "source_address_ids": [
        19
      ],
      "source_count": 1,
      "source_network": "Net-10-172-192.Net_172_16_0_0",
      "start_time": 1640775850743,
      "status": "CLOSED",
      "username_count": 0
    },
    {
      "assigned_to": "Mike_TM",
      "categories": [
        "Access Denied",
        "ACL Deny"
      ],
      "category_count": 2,
      "close_time": 1640775830000,
      "closing_reason_id": 1,
      "closing_user": "API_user: admin",
      "credibility": 2,
      "description": "Excessive Firewall Denies Between Hosts\n",
      "destination_networks": [
        "Net-10-172-192.Net_172_16_0_0",
        "other"
      ],
      "device_count": 1,
      "domain_id": 0,
      "event_count": 2165067,
      "first_persisted_time": 1640758015000,
      "flow_count": 0,
      "follow_up": true,
      "id": 34,
      "inactive": true,
      "last_persisted_time": 1640778017000,
      "last_updated_time": 1640775819770,
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
      "magnitude": 2,
      "offense_source": "172.31.34.93",
      "offense_type": 0,
      "policy_category_count": 0,
      "protected": false,
      "relevance": 0,
      "remote_destination_count": 1,
      "rules": [
        {
          "id": 100033,
          "type": "CRE_RULE"
        },
        {
          "id": 100376,
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
      "start_time": 1640758014341,
      "status": "CLOSED",
      "username_count": 1
    },
    {
      "categories": [
        "Command Execution",
        "Input Validation Exploit",
        "Misc Exploit"
      ],
      "category_count": 3,
      "credibility": 3,
      "description": "Multiple Exploit/Malware Types Targeting a Single Destination\n containing Command Injection\n",
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
      "last_persisted_time": 1641400827000,
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
    },
    {
      "categories": [
        "Code Injection",
        "Buffer Overflow",
        "SQL Injection",
        "Cross Site Scripting",
        "Input Validation Exploit",
        "Command Execution",
        "Misc Exploit"
      ],
      "category_count": 7,
      "close_time": 1640756435000,
      "closing_reason_id": 54,
      "closing_user": "admin",
      "credibility": 3,
      "description": "Multiple Exploit/Malware Types Targeting a Single Destination\n containing CSRF\n",
      "destination_networks": [
        "other"
      ],
      "device_count": 2,
      "domain_id": 0,
      "event_count": 17,
      "first_persisted_time": 1640075633000,
      "flow_count": 0,
      "follow_up": false,
      "id": 32,
      "inactive": true,
      "last_persisted_time": 1640756436000,
      "last_updated_time": 1640075632599,
      "local_destination_address_ids": [],
      "local_destination_count": 0,
      "log_sources": [
        {
          "id": 63,
          "name": "Custom Rule Engine-8 :: ip-172-31-34-93",
          "type_id": 18,
          "type_name": "EventCRE"
        },
        {
          "id": 23312,
          "name": "Virsec Security Platform",
          "type_id": 4013,
          "type_name": "VirsecSecurityPlatformCustom"
        }
      ],
      "magnitude": 4,
      "offense_source": "49.36.68.146",
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
      "security_category_count": 7,
      "severity": 10,
      "source_address_ids": [
        17
      ],
      "source_count": 1,
      "source_network": "other",
      "start_time": 1640075632388,
      "status": "CLOSED",
      "username_count": 2
    }
  ]
}

```

### Custom Output Types

#### assets

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Domain Id|integer|False|Domain id|
|Hostnames|[]hostnames|False|Hostnames|
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

#### hostnames

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
|Ip Addresses|[]ip_addresses|False|Ip addresses|
|Last Seen Profiler|string|False|Last seen profiler|
|Last Seen Scanner|string|False|Last seen scanner|
|Mac Address|string|False|Mac address|

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
* [AQL](https://www.ibm.com/docs/en/qradar-on-cloud?topic=structure-sample-aql-queries)
