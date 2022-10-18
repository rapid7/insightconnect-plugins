# Description

ManageEngine's Service Desk has the ability to centralize and capture reported issues, allowing security and IT administrators to track and manage all incidents in an easy manner. The numerous help desk tickets raised are organized and tracked in the Requests module. The Requests module enables you to handle tickets promptly, assign tickets to technicians, merge similar requests, and so on.

# Key Features

* Manage requests - add, edit, add resolution, assign, close, delete, pickup, get details and get list of requests
* Manage request notes - add, edit, delete, get list of notes

# Requirements

The authentication between ServiceDesk Plus and an Insight Connect application is through an API key. A unique key is generated for a technician with login permission in the ServiceDesk Plus application.
* To generate the API Key, click Admin -> Technicians under User block.
* If you want to generate the API key for an existing technician, then click the edit icon beside the technician.
* If you want to generate the API key for a new technician, click Add New Technician link, enter the technician details and provide login permission.
* Click Generate link under the API key details block. You can select a time frame for the key to expire using the calendar icon or simply retain the same key indefinitely.
* If a key is already generated for the technician, a Re-generate link appears.

# Supported Product Versions

* ServiceDesk Plus 13008

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Manage Engine Service Desk Technican's API key|None|EXAMPLE1-API2-KEY3-HDFS-48GS24WSA6GE|
|sdp_base_url|string|None|True|Service Desk Plus Base URL|None|https://example.com|
|ssl_verify|boolean|True|True|SSL verify|None|True|

Example input:

```
{
  "api_key": "EXAMPLE1-API2-KEY3-HDFS-48GS24WSA6GE",
  "sdp_base_url": "http://me-sdeskplus.dev.example.com:8080",
  "ssl_verify": true
}
```

## Technical Details

### Actions

#### Add Request

Add new a request. Subject and requester parameters are required, others are optional. In every parameter containing `ID` and `Name` fields please provide at least one of them.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assets|[]asset|None|False|Array of asset objects associated with this request|None|["{"name": "Software", "barcode": "test-barcode"}"]|
|category|category|None|False|Category to which this request belongs|None|{"name": "Operating System"}|
|description|string|None|False|Description of this request|None|Example description|
|email_ids_to_notify|[]string|None|False|Array of Email ids, which needs to be notified about the happenings of this request|None|["user@example.com"]|
|group|group|None|False|The group to which the request belongs|None|{"name": "Network"}|
|impact|impact|None|False|Impact of this request|None|{"name": "High"}|
|is_fcr|boolean|None|False|Boolean value indicating if the request has been marked as First Call Resolution|None|True|
|item|item|None|False|Item of this request|None|{"name": "Install"}|
|level|level|None|False|Level of the request|None|{"name": "Tier 4"}|
|mode|mode|None|False|The mode in which this request is created|None|{"name": "Web Form"}|
|priority|priority|None|False|Priority of the request|None|{"name": "High"}|
|request_type|request_type|None|False|Type of this request|None|{"name" "Incident"}|
|requester|user_input|None|True|The requester of the request|None|{"name": "John"}|
|service_category|service_category|None|False|Service category to which this request belongs|None|{"name": "User Management"}|
|site|site|None|False|Denotes the site to which this request belongs|None|{"name": "Custom Site"}|
|status|status|None|False|Indicates the current status of this request|None|{"name": "Open"}|
|subcategory|subcategory|None|False|Subcategory to which this request belongs|None|{"name": "Mac OS X"}|
|subject|string|None|True|Subject of this request|None|Need a Monitor|
|technician|technician|None|False|The technician that was assigned to the request|None|{"name": "John"}|
|urgency|urgency|None|False|Urgency of the request|None|{"name": "Low"}|

Example input:

```
{
  "subject": "Install xyz",
  "requester": {
    "name": Mike"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|--------|
|request_id|integer|False|The id of newly created request|55|
|status|string|True|Status of the request|success|
|status_code|integer|False|Status code of the request|2000|

Example output:

```
{
  "request_id": 55,
  "status": "success",
  "status_code": 2000
}
```

#### Add Request Note

Add a note to an existing request.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|add_to_linked_request|boolean|None|False|Whether to add the note to the linked requests|None|False|
|description|string|None|True|Note description (the content of the note) in HTML format|None|Additional information required...|
|mark_first_response|boolean|None|False|Whether to set the responded date of the request/ticket|None|True|
|notify_technician|boolean|None|False|Whether to notify the technician or not|None|True|
|request_id|integer|None|True|The id of the request|None|55|
|show_to_requester|boolean|None|False|Whether to show the note to requester or not|None|False|

Example input:

```
{
  "add_to_linked_request": false,
  "description": "Additional information required...",
  "mark_first_response": true,
  "notify_technician": true,
  "request_id": 55,
  "show_to_requester": false
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|request_id|integer|False|The id of the request|55|
|request_note_id|integer|False|The id of the request note|209|
|status|string|True|Status of the request|success|
|status_code|integer|False|Status code of the request|2000|

Example output:

```
{
  "request_id": 55,
  "request_note_id": 336,
  "status": "success",
  "status_code": 2000
}
```

#### Add Resolution

Add or update the resolution of a request.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|request_id|integer|None|True|The id of the request|None|27|
|content|string|None|True|Resolution content|None|Sample resolution|
|add_to_linked_requests|boolean|None|True|Whether the resolution should be added to linked requests|None|True|

Example input:

```
{
  "add_to_linked_requests": true,
  "content": "Sample resolution",
  "request_id": 27
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|--------|
|request_id|integer|False|The id of the request|27|
|status|string|True|Status of the request|success|
|status_code|integer|False|Status code of the request|2000|

Example output:

```
{
  "request_id": 27,
  "status": "success",
  "status_code": 2000
}
```

#### Assign Request

Assign a request to a technician or group. Request ID is required, as well as at least one of Group or Technician. In every parameter containing `ID` and `Name` fields please provide only one or the other.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|group|group|None|False|The group to which the request belongs|None|{"name": "Network"}|
|request_id|integer|None|True|The request id that should be assigned|None|27|
|technician|technician|None|False|The technician that was assigned to the request|None|{"name": "John"}|

Example input:

```
{
  "group": {
    "name": "Network"
  },
  "request_id": 27,
  "technician": {
    "name": "John"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|--------|
|request_id|integer|False|The id of the assigned request|27|
|status|string|True|Status of the request|success|
|status_code|integer|False|Status code of the request|2000|

Example output:

```
{
  "request_id": 27,
  "status": "success",
  "status_code": 2000
}
```

#### Close Request

Close the given request.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|closure_code|closure_code|None|False|Closure code to add to the request|None|{"name": "Success"}|
|closure_comments|string|None|False|The comments that should be added when closing the request|None|Reset the password solved the issue|
|request_id|integer|None|True|The request id that should be closed|None|54|
|requester_ack_comments|string|None|False|The requester comments|None|Mail fetching is up and running now|
|requester_ack_resolution|boolean|None|False|The requester resolution|None|True|

Example input:

```
{
  "closure_code": {
    "name": "Success"
  },
  "closure_comments": "Reset the password solved the issue",
  "request_id": 54,
  "requester_ack_comments": "Mail fetching is up and running now",
  "requester_ack_resolution": true
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|--------|
|request_id|integer|False|The id of the closed request|54|
|status|string|True|Status of the request|success|
|status_code|integer|False|Status code of the request|2000|

Example output:

```
{
  "request_id": 54,
  "status": "success",
  "status_code": 2000
}
```

#### Delete Request

Delete the given request (move it to the trash).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|request_id|integer|None|True|The ID of a request to delete|None|54|

Example input:

```
{
  "request_id": 54
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|--------|
|request_id|integer|False|The id of deleted request|54|
|status|string|True|Status of the request|success|
|status_code|integer|False|Status code of the request|2000|

Example output:

```
{
  "request_id": 54,
  "status": "success",
  "status_code": 2000
}
```

#### Delete Request Note

Delete a given request note on a specific request.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|request_id|integer|None|True|The id of the request|None|55|
|request_note_id|integer|None|True|The id of the request note to delete|None|208|

Example input:

```
{
  "request_id": 55,
  "request_note_id": 208
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|--------|
|request_id|integer|False|The id of the request|55|
|status|string|True|Status of the request|success|
|status_code|integer|False|Status code of the request|2000|

Example output:

```
{
  "request_id": 55,
  "status": "success",
  "status_code": 2000
}
```

#### Edit Request

Update the given request. At least one parameter other than Request ID is required. In every parameter containing `ID` and `Name` fields please provide only one or the other.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|assets|[]asset|None|False|Array of asset objects associated with this request|None|["{"name": "Software", "barcode": "test-barcode"}"]|
|category|category|None|False|Category to which this request belongs|None|{"name": "Operating System"}|
|description|string|None|False|Description of this request|None|Example description|
|email_ids_to_notify|[]string|None|False|Array of Email ids, which needs to be notified about the happenings of this request|None|["user@example.com"]|
|group|group|None|False|The group to which the request belongs|None|{"name": "Network"}|
|impact|impact|None|False|Impact of this request|None|{"name": "High"}|
|is_fcr|boolean|None|False|Boolean value indicating if the request has been marked as First Call Resolution|None|True|
|item|item|None|False|Item of this request|None|{"name": "Install"}|
|level|level|None|False|Level of the request|None|{"name": "Tier 4"}|
|mode|mode|None|False|The mode in which this request is created|None|{"name": "Web Form"}|
|priority|priority|None|False|Priority of the request|None|{"name": "High"}|
|request_id|integer|None|True|The ID of a request to edit|None|54|
|request_type|request_type|None|False|Type of this request|None|{"name" "Incident"}|
|requester|user_input|None|False|The requester of the request|None|{"name": "John"}|
|service_category|service_category|None|False|Service category to which this request belongs|None|{"name": "User Management"}|
|site|site|None|False|Denotes the site to which this request belongs|None|{"name": "Custom Site"}|
|status|status|None|False|Indicates the current status of this request|None|{"name": "Open"}|
|subcategory|subcategory|None|False|Subcategory to which this request belongs|None|{"name": "Mac OS X"}|
|subject|string|None|False|Subject of this request|None|Need a Monitor|
|technician|technician|None|False|The technician that was assigned to the request|None|{"name": "John"}|
|urgency|urgency|None|False|Urgency of the request|None|{"name": "Low"}|

Example input:

```
{
  "request_id": 54,
  "subject": "Install xyz",
  "requester": {
    "name": Mike"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|--------|
|request_id|integer|False|The id of edited request|54|
|status|string|True|Status of the request|success|
|status_code|integer|False|Status code of the request|2000|

Example output:

```
{
  "request_id": 54,
  "status": "success",
  "status_code": 2000
}
```

#### Edit Request Note

Update a note on the given request. At least one parameter other than Request ID and Note ID is required.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|add_to_linked_request|boolean|None|False|Whether to add the note to the linked requests|None|False|
|description|string|None|False|Note description in HTML format|None|Need help|
|mark_first_response|boolean|None|False|Whether to set the responded date of the request/ticket|None|True|
|notify_technician|boolean|None|False|Whether to notify the technician or not|None|True|
|request_id|integer|None|True|The id of the request|None|55|
|request_note_id|integer|None|True|The id of the request note|None|209|
|show_to_requester|boolean|None|False|Whether to show the note to requester or not|None|False|

Example input:

```
{
  "add_to_linked_request": false,
  "description": "Need help",
  "mark_first_response": true,
  "notify_technician": true,
  "request_id": 55,
  "request_note_id": 209,
  "show_to_requester": false
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|--------|
|request_id|integer|False|The id of the request|55|
|status|string|True|Status of the request|success|
|status_code|integer|False|Status code of the request|2000|

Example output:

```
{
  "request_id": 55,
  "status": "success",
  "status_code": 2000
}
```

#### Get List Request

View the details of a list of requests matching a search.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|page_size|integer|10|False|By default, will return only the first 10 requests|None|15|
|search_fields|object|None|False|The column name and value to be searched|None|{"subject": "test","priority.name": "Low"}|
|sort_field|string|subject|False|FieldName for sorting|None|subject|
|sort_order|string|asc|False|Sort order for the results|['asc', 'desc', 'None']|asc|
|start_index|integer|None|False|Use this to get a list of tasks starting from this index|None|2|

Example input:

```
{
  "page_size": 15,
  "search_fields": {
    "subject": "test",
    "priority.name": "Low"
  },
  "sort_field": "subject",
  "sort_order": "asc",
  "start_index": 2
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|--------|
|requests|[]request_output|False|List of requests|["{"subject": "Install xyz", "requester": {"name": "Mike"}}"]|
|status|string|True|Status of the request|success|

Example output:

```
{
  "requests": [
    {
      "created_by": {
        "id": 4,
        "name": "administrator",
        "is_vipuser": false
      },
      "created_time": "Aug 9, 2022 06:06 AM",
      "due_by_time": "Aug 9, 2022 05:00 PM",
      "id": 71,
      "is_overdue": true,
      "is_service_request": false,
      "priority": {
        "name": "Low",
        "id": 1
      },
      "requester": {
        "id": 4,
        "name": "administrator",
        "is_vipuser": false
      },
      "site": {
        "name": "Test Site",
        "id": 301
      },
      "status": {
        "name": "Open",
        "id": 2
      },
      "subject": "Plugin action test add request 2",
      "technician": {
        "id": 4,
        "name": "administrator",
        "is_vipuser": false
      }
    },
    {
      "created_by": {
        "id": 4,
        "name": "administrator",
        "is_vipuser": false
      },
      "created_time": "Aug 8, 2022 04:54 AM",
      "due_by_time": "Aug 8, 2022 05:00 PM",
      "id": 61,
      "is_overdue": true,
      "is_service_request": false,
      "priority": {
        "name": "Low",
        "id": 1
      },
      "requester": {
        "id": 4,
        "name": "administrator",
        "is_vipuser": false
      },
      "site": {
        "name": "Test Site",
        "id": 301
      },
      "status": {
        "name": "Open",
        "id": 2
      },
      "subject": "Plugin action test add request 2",
      "technician": {
        "id": 4,
        "name": "administrator",
        "is_vipuser": false
      }
    },
    {
      "created_by": {
        "id": 4,
        "name": "administrator",
        "is_vipuser": false
      },
      "created_time": "Aug 8, 2022 04:41 AM",
      "due_by_time": "Aug 8, 2022 05:00 PM",
      "id": 60,
      "is_overdue": true,
      "is_service_request": false,
      "priority": {
        "name": "Low",
        "id": 1
      },
      "requester": {
        "id": 4,
        "name": "administrator",
        "is_vipuser": false
      },
      "site": {
        "name": "Test Site",
        "id": 301
      },
      "status": {
        "name": "Open",
        "id": 2
      },
      "subject": "Plugin action test add request 2",
      "technician": {
        "id": 4,
        "name": "administrator",
        "is_vipuser": false
      }
    },
    {
      "created_by": {
        "id": 4,
        "name": "administrator",
        "is_vipuser": false
      },
      "created_time": "Jul 13, 2022 01:20 AM",
      "due_by_time": "Jul 15, 2022 05:00 PM",
      "id": 27,
      "is_overdue": true,
      "is_service_request": false,
      "priority": {
        "name": "Low",
        "id": 1
      },
      "requester": {
        "id": 4,
        "name": "administrator",
        "is_vipuser": false
      },
      "site": {
        "name": "Test Site",
        "id": 301
      },
      "status": {
        "name": "Open",
        "id": 2
      },
      "subject": "Plugin action test add request 2",
      "technician": {
        "id": 4,
        "name": "administrator",
        "is_vipuser": false
      }
    }
  ],
  "status": "success"
}
```

#### Get List Request Notes

Get the list of all notes associated with the given request.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|request_id|integer|None|True|The id of the request|None|55|

Example input:

```
{
  "request_id": 55
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|--------|
|request_id|integer|True|The id of the request|55|
|notes|[]note|False|Notes assigned to the request|["{"note_id": "312", "added_time": "Jul 8, 2022 02:02 AM", "added_by": {"name": "John", "id": "71"}}"]|
|status|string|True|Status of the request|success|
|status_code|integer|False|Status code of the request|2000|

Example output:

```
{
  "request_id": 55,
  "notes": [
    {
      "last_updated_by": {
        "name": "administrator",
        "id": 4
      },
      "added_time": "Aug 3, 2022 12:55 AM",
      "last_updated_time": "Aug 3, 2022 12:55 AM",
      "added_by": {
        "name": "administrator",
        "id": 4
      },
      "show_to_requester": true
    },
    {
      "last_updated_by": {
        "name": "administrator",
        "id": 4
      },
      "added_time": "Aug 3, 2022 12:55 AM",
      "last_updated_time": "Aug 3, 2022 12:55 AM",
      "added_by": {
        "name": "administrator",
        "id": 4
      },
      "show_to_requester": true
    }
  ],
  "status": "success",
  "status_code": 2000
}
```

#### Get Request

View the details of a request given the request id.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|request_id|integer|None|True|The request id that should be returned|None|54|

Example input:

```
{
  "request_id": 54
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|--------|
|request|request_output|False|Request|{"subject": "Install xyz", "requester": {"name": "Mike"}}|
|status|string|True|Status of the request|success|
|status_code|integer|False|Status code of the request|2000|

Example output:

```
{
  "request": {
    "subject": "Plugin action test add request 2",
    "requester": {
      "id": 4,
      "name": "administrator",
      "is_vipuser": false
    },
    "description": "dessssc",
    "request_type": {
      "name": "Incident",
      "id": 1
    },
    "impact": {
      "name": "Medium",
      "id": 2
    },
    "status": {
      "name": "Open",
      "id": 2
    },
    "mode": {
      "name": "Web Form",
      "id": 2
    },
    "level": {
      "name": "Tier 4",
      "id": 4
    },
    "urgency": {
      "name": "Urgent",
      "id": 1
    },
    "priority": {
      "name": "Normal",
      "id": 2
    },
    "service_category": {
      "name": "User Management",
      "id": 8
    },
    "id": 54,
    "assets": [
      {
        "name": "keyboardMC",
        "id": 301
      }
    ],
    "site": {
      "name": "Test Site",
      "id": 301
    },
    "technician": {
      "id": 4,
      "name": "administrator",
      "is_vipuser": false
    },
    "category": {
      "name": "Software",
      "id": 3
    },
    "subcategory": {
      "name": "MS Office",
      "id": 5
    },
    "email_ids_to_notify": [
      "user@example.com"
    ],
    "udf_fields": {},
    "created_time": "Aug 3, 2022 01:11 AM",
    "due_by_time": "Aug 3, 2022 01:00 PM",
    "created_by": {
      "id": 4,
      "name": "administrator",
      "is_vipuser": false
    },
    "is_service_request": false,
    "has_notes": false,
    "is_overdue": true
  },
  "status": "success"
}
```

#### Get Resolution

Get the resolution of the given request.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|request_id|integer|None|True|The id of the request|None|27|

Example input:

```
{
  "request_id": 27
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|request_id|integer|False|The id of the request|27|
|status|string|True|Status of the request|success|
|status_code|integer|False|Status code of the request|2000|
|content|string|False|Resolution content|Sample resolution|

Example output:

```
{
  "request_id": 27,
  "content": "asd",
  "status": "success",
  "status_code": 2000
}
```

#### Pickup Request

Pick up (assign) a given request in your name as a technician.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|request_id|integer|None|True|The request id that should be assigned|None|27|

Example input:

```
{
  "request_id": 27
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|--------|
|request_id|integer|False|The id of the picked up request|27|
|status|string|True|Status of the request|success|
|status_code|integer|False|Status code of the request|2000|

Example output:

```
{
  "request_id": 27,
  "status": "success",
  "status_code": 2000
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### added_by

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|False|Id of the creator|
|Name|string|False|Name of the creator|

#### asset

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Barcode|string|False|Barcode of the asset|
|Id|integer|False|Id of the asset|
|Name|string|False|Name of the asset|

#### category

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|integer|False|ID of the category|
|Name|string|False|Name of the category|

#### closure_code

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|integer|False|Closure Code ID|
|Name|string|False|Closure Code name|

#### group

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|False|Group's id|
|Name|string|False|Group's name|

#### impact

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|integer|False|ID of the impact|
|Name|string|False|Name impact|

#### item

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|integer|False|ID of the item|
|Name|string|False|Name of the item|

#### last_updated_by

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|False|Id of the last editor|
|Name|string|False|Name of the last editor|

#### level

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|integer|False|Id of the level|
|Name|string|False|Name of the level|

#### mode

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|integer|False|Id of the mode|
|Name|string|False|Name of the mode|

#### note

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Added by|added_by|False|Added by details|
|Added time|date|False|The time the request note was added|
|ID|integer|False|Note ID|
|Last updated by|last_updated_by|False|Last updated by details|
|Last updated time|date|False|The time the request note was updated|
|Show to Requester|boolean|False|Whether to show the note to requester or not|

#### priority

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|integer|False|ID of the priority|
|Name|string|False|Name of the priority|

#### request_output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Assets|[]asset|False|Array of asset objects associated with this request|
|Category|category|False|Category to which this request belongs|
|Created By|user_output|False|Creator of the request|
|Created Time|date|False|Time the request was created|
|Description|string|False|Description of this request|
|Due By Time|date|False|The due date of the request|
|email_ids_to_notify|[]string|False|Array of Email ids, which needs to be notified about the happenings of this request|
|Group|group|False|The group to which the request belongs|
|Has Notes|boolean|False|Indicates whether the request has notes|
|Id|integer|False|Id of the request|
|Impact|impact|False|Impact of this request|
|is_fcr|boolean|False|Boolean value indicating if the request has been marked as First Call Resolution|
|Is Overdue|boolean|False|Indicates if the request is overdue|
|Is Service Request|boolean|False|Indicates whether the request is a service request or not|
|item|item|False|Item of this request|
|Level|level|False|Level of the request|
|mode|mode|False|The mode in which this request is created|
|Priority|priority|False|Priority of the request|
|Request Type|request_type|False|Type of this request|
|Requester|user_output|True|The requester of the request|
|Service Category|service_category|False|Service category to which this request belongs|
|site|site|False|Denotes the site to which this request belongs|
|status|status|False|Indicates the current status of this request|
|subcategory|subcategory|False|Subcategory to which this request belongs|
|Subject|string|True|Subject of this request|
|Technician|technician|False|The technician that was assigned to the request|
|Udf Fields|object|False|Holds udf fields values associated with the request|
|Urgency|urgency|False|Urgency of the request|

#### request_type

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|integer|False|ID of the request type|
|Name|string|False|Name of the request type|

#### service_category

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|integer|False|ID of the service category|
|Name|string|False|Name of the service category|

#### site

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|False|Site's id|
|Name|string|False|Site's name|

#### status

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|integer|False|ID of the current status|
|Name|string|False|Name of the current status|

#### subcategory

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|integer|False|ID of the subcategory|
|Name|string|False|Name of the subcategory|

#### technician

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|False|Technician ID|
|Name|string|False|Technician Name|

#### urgency

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|integer|False|Id of the urgency|
|Name|string|False|Name of the urgency|

#### user_input

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|False|User ID|
|Name|string|False|User name|

#### user_output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|False|User ID|
|Is Vipuser|boolean|False|Whether the user is a vip user or not|
|Name|string|False|User name|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - Fix `int` conversion issue in `Get List Request` and `Get Request` actions
* 1.0.0 - Initial plugin - Create actions: `Add Request`, `Add Request Note`, `Add Resolution`, `Assign Request`, `Close Request`, `Delete Request`, `Delete Request Note`, `Edit Request`, `Edit Request Note`, `Get List Request`, `Get List Request Notes`, `Get Request`, `Get Resolution`, `Pickup Request`

# Links

* [Manage Engine Service Desk API Docs](https://www.manageengine.com/products/service-desk/sdpod-v3-api)

## References

* [Manage Engine Service Desk](https://manageengine.com/products/service-desk)

