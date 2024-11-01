# Description

ManageEngine's Service Desk has the ability to centralize and capture reported issues, allowing security and IT administrators to track and manage all incidents in an easy manner. The numerous help desk tickets raised are organized and tracked in the Requests module. The Requests module enables you to handle tickets promptly, assign tickets to technicians, merge similar requests, and so on

# Key Features

* Manage requests - add, edit, add resolution, assign, close, delete, pickup, get details and get list of requests
* Manage request notes - add, edit, delete, get list of notes

# Requirements

The authentication between ServiceDesk Plus and an Insight Connect application is through an API key. A unique key is generated for a technician with login permission in the ServiceDesk Plus application.
* To generate the API Key, click Admin -> Technicians under User block.
* If you want to generate the API key for an existing technician, then click the edit icon beside the technician.
* If you want to generate the API key for a new technician, click Add New Technician link, enter the technician details and provide login permission.

# Supported Product Versions

* ServiceDesk Plus 13008

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|Manage Engine Service Desk Technican's API key|None|EXAMPLE1-API2-KEY3-HDFS-48GS24WSA6GE|None|None|
|sdp_base_url|string|None|True|Service Desk Plus Base URL|None|http://me-sdeskplus.dev.example.com:8080|None|None|
|ssl_verify|boolean|True|True|SSL verify|None|True|None|None|

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
  
This action is used to add a new request. Subject and requester parameters are required, others are optional. In every 
parameter containing `ID` and `Name` fields please provide at least one of them

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assets|[]asset|None|False|Array of asset objects associated with this request|None|["{\"name\": \"Software\", \"barcode\": \"test-barcode\"}"]|None|None|
|category|category|None|False|Category to which this request belongs|None|{"name": "Operating System"}|None|None|
|description|string|None|False|Description of this request|None|Example description|None|None|
|email_ids_to_notify|[]string|None|False|Array of Email ids, which needs to be notified about the happenings of this request|None|["user@example.com"]|None|None|
|group|group|None|False|The group to which the request belongs|None|{"name": "Network"}|None|None|
|impact|impact|None|False|Impact of this request|None|{"name": "High"}|None|None|
|is_fcr|boolean|None|False|Boolean value indicating if the request has been marked as First Call Resolution|None|True|None|None|
|item|item|None|False|Item of this request|None|{"name": "Install"}|None|None|
|level|level|None|False|Level of the request|None|{"name": "Tier 4"}|None|None|
|mode|mode|None|False|The mode in which this request is created|None|{"name": "Web Form"}|None|None|
|priority|priority|None|False|Priority of the request|None|{"name": "High"}|None|None|
|request_type|request_type|None|False|Type of this request|None|{"name" "Incident"}|None|None|
|requester|user_input|None|True|The requester of the request|None|{"name": "John"}|None|None|
|service_category|service_category|None|False|Service category to which this request belongs|None|{"name": "User Management"}|None|None|
|site|site|None|False|Denotes the site to which this request belongs|None|{"name": "Custom Site"}|None|None|
|status|status|None|False|Indicates the current status of this request|None|{"name": "Open"}|None|None|
|subcategory|subcategory|None|False|Subcategory to which this request belongs|None|{"name": "Mac OS X"}|None|None|
|subject|string|None|True|Subject of this request|None|Need a Monitor|None|None|
|technician|technician|None|False|The technician that was assigned to the request|None|{"name": "John"}|None|None|
|urgency|urgency|None|False|Urgency of the request|None|{"name": "Low"}|None|None|
  
Example input:

```
{
  "subject": "Install xyz",
  "requester": {
    "name": "Mike"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
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

This action is used to add a note to an existing request

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|add_to_linked_request|boolean|None|False|Whether to add the note to the linked requests|None|False|None|None|
|description|string|None|True|Note description (the content of the note) in HTML format|None|Additional information required...|None|None|
|mark_first_response|boolean|None|False|Whether to set the responded date of the request/ticket|None|True|None|None|
|notify_technician|boolean|None|False|Whether to notify the technician or not|None|True|None|None|
|request_id|integer|None|True|The id of the request|None|55|None|None|
|show_to_requester|boolean|None|False|Whether to show the note to requester or not|None|False|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|request_id|integer|False|The id of the request|55|
|request_note_id|integer|False|The id of the request note|209|
|status|string|True|Status of the request|success|
|status_code|integer|False|Status code of the request|2000|
  
Example output:

```
{
  "request_id": 55,
  "request_note_id": 209,
  "status": "success",
  "status_code": 2000
}
```

#### Add Resolution

Add or update the resolution of a request

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|add_to_linked_requests|boolean|None|True|Whether the resolution should be added to linked requests|None|True|None|None|
|content|string|None|True|Resolution content|None|Sample resolution|None|None|
|request_id|integer|None|True|The id of the request|None|27|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
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

Assign a request to a technician or group. Request ID is required, as well as at least one of Group or Technician. In every parameter containing `ID` and `Name` fields please provide only one or the other

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|group|group|None|False|The group to which the request belongs|None|{"name": "Network"}|None|None|
|request_id|integer|None|True|The request id that should be assigned|None|27|None|None|
|technician|technician|None|False|The technician that was assigned to the request|None|{"name": "John"}|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
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

Close the given request

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|closure_code|closure_code|None|False|Closure code to add to the request|None|{"name": "Success"}|None|None|
|closure_comments|string|None|False|The comments that should be added when closing the request|None|Reset the password solved the issue|None|None|
|request_id|integer|None|True|The request id that should be closed|None|54|None|None|
|requester_ack_comments|string|None|False|The requester comments|None|Mail fetching is up and running now|None|None|
|requester_ack_resolution|boolean|None|False|The requester resolution|None|True|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
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

Delete the given request (move it to the trash)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|request_id|integer|None|True|The ID of a request to delete|None|54|None|None|
  
Example input:

```
{
  "request_id": 54
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
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

Delete a given request note on a specific request

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|request_id|integer|None|True|The id of the request|None|55|None|None|
|request_note_id|integer|None|True|The id of the request note to delete|None|208|None|None|
  
Example input:

```
{
  "request_id": 55,
  "request_note_id": 208
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
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

Update the given request. At least one parameter other than Request ID is required. In every parameter containing `ID` and `Name` fields please provide only one or the other

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assets|[]asset|None|False|Array of asset objects associated with this request|None|["{\"name\": \"Software\", \"barcode\": \"test-barcode\"}"]|None|None|
|category|category|None|False|Category to which this request belongs|None|{"name": "Operating System"}|None|None|
|description|string|None|False|Description of this request|None|Example description|None|None|
|email_ids_to_notify|[]string|None|False|Array of Email ids, which needs to be notified about the happenings of this request|None|["user@example.com"]|None|None|
|group|group|None|False|The group to which the request belongs|None|{"name": "Network"}|None|None|
|impact|impact|None|False|Impact of this request|None|{"name": "High"}|None|None|
|is_fcr|boolean|None|False|Boolean value indicating if the request has been marked as First Call Resolution|None|True|None|None|
|item|item|None|False|Item of this request|None|{"name": "Install"}|None|None|
|level|level|None|False|Level of the request|None|{"name": "Tier 4"}|None|None|
|mode|mode|None|False|The mode in which this request is created|None|{"name": "Web Form"}|None|None|
|priority|priority|None|False|Priority of the request|None|{"name": "High"}|None|None|
|request_id|integer|None|True|The ID of a request to edit|None|54|None|None|
|request_type|request_type|None|False|Type of this request|None|{"name" "Incident"}|None|None|
|requester|user_input|None|False|The requester of the request|None|{"name": "John"}|None|None|
|service_category|service_category|None|False|Service category to which this request belongs|None|{"name": "User Management"}|None|None|
|site|site|None|False|Denotes the site to which this request belongs|None|{"name": "Custom Site"}|None|None|
|status|status|None|False|Indicates the current status of this request|None|{"name": "Open"}|None|None|
|subcategory|subcategory|None|False|Subcategory to which this request belongs|None|{"name": "Mac OS X"}|None|None|
|subject|string|None|False|Subject of this request|None|Need a Monitor|None|None|
|technician|technician|None|False|The technician that was assigned to the request|None|{"name": "John"}|None|None|
|urgency|urgency|None|False|Urgency of the request|None|{"name": "Low"}|None|None|
  
Example input:

```
{
  "request_id": 54,
  "subject": "Install xyz",
  "requester": {
    "name": "Mike"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
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

Update a note on the given request. At least one parameter other than Request ID and Note ID is required

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|add_to_linked_request|boolean|None|False|Whether to add the note to the linked requests|None|False|None|None|
|description|string|None|False|Note description in HTML format|None|Need help|None|None|
|mark_first_response|boolean|None|False|Whether to set the responded date of the request/ticket|None|True|None|None|
|notify_technician|boolean|None|False|Whether to notify the technician or not|None|True|None|None|
|request_id|integer|None|True|The id of the request|None|55|None|None|
|request_note_id|integer|None|True|The id of the request note|None|209|None|None|
|show_to_requester|boolean|None|False|Whether to show the note to requester or not|None|False|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
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

View the details of a list of requests matching a search

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|page_size|integer|10|False|By default, will return only the first 10 requests|None|15|None|None|
|search_fields|object|None|False|The column name and value to be searched|None|{"subject": "test","priority.name": "Low"}|None|None|
|sort_field|string|subject|False|FieldName for sorting|None|subject|None|None|
|sort_order|string|asc|False|Sort order for the results|["asc", "desc", "None"]|asc|None|None|
|start_index|integer|None|False|Use this to get a list of tasks starting from this index|None|2|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|requests|[]request_output|False|List of requests|["{\"subject\": \"Install xyz\", \"requester\": {\"name\": \"Mike\"}}"]|
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

Get the list of all notes associated with the given request

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|request_id|integer|None|True|The id of the request|None|55|None|None|
  
Example input:

```
{
  "request_id": 55
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|notes|[]note|False|Notes assigned to the request|["{\"note_id\": \"312\", \"added_time\": \"Jul 8, 2022 02:02 AM\", \"added_by\": {\"name\": \"John\"}"]|
|request_id|integer|True|The id of the request|55|
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

View the details of a request given the request ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|request_id|integer|None|True|The request id that should be returned|None|54|None|None|
  
Example input:

```
{
  "request_id": 54
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
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

Get the resolution of the given request

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|request_id|integer|None|True|The id of the request|None|27|None|None|
  
Example input:

```
{
  "request_id": 27
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|content|string|False|Resolution content|Sample resolution|
|request_id|integer|False|The id of the request|27|
|status|string|True|Status of the request|success|
|status_code|integer|False|Status code of the request|2000|
  
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

Pick up (assign) a given request in your name as a technician

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|request_id|integer|None|True|The request id that should be assigned|None|27|None|None|
  
Example input:

```
{
  "request_id": 27
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
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
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**request_type**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID of the request type|1|
|Name|string|None|False|Name of the request type|Incident|
  
**impact**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID of the impact|1|
|Name|string|None|False|Name impact|High|
  
**status**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID of the current status|2|
|Name|string|None|False|Name of the current status|Open|
  
**mode**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|Id of the mode|2|
|Name|string|None|False|Name of the mode|Web Form|
  
**level**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|Id of the level|4|
|Name|string|None|False|Name of the level|Tier 4|
  
**urgency**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|Id of the urgency|2|
|Name|string|None|False|Name of the urgency|High|
  
**priority**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID of the priority|4|
|Name|string|None|False|Name of the priority|High|
  
**service_category**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID of the service category|8|
|Name|string|None|False|Name of the service category|User Management|
  
**user_output**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|User ID|71|
|Is Vipuser|boolean|None|False|Whether the user is a vip user or not|False|
|Name|string|None|False|User name|John|
  
**user_input**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|User ID|71|
|Name|string|None|False|User name|John|
  
**asset**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Barcode|string|None|False|Barcode of the asset|test-barcode|
|ID|integer|None|False|Id of the asset|4541563|
|Name|string|None|False|Name of the asset|Software|
  
**site**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|Site's id|2235435|
|Name|string|None|False|Site's name|Custom Site|
  
**group**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|Group's id|2|
|Name|string|None|False|Group's name|Network|
  
**technician**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|Technician ID|3|
|Name|string|None|False|Technician Name|Samuel|
  
**category**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID of the category|8|
|Name|string|None|False|Name of the category|Operating System|
  
**subcategory**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID of the subcategory|24|
|Name|string|None|False|Name of the subcategory|Mac OS X|
  
**item**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|ID of the item|1|
|Name|string|None|False|Name of the item|Install|
  
**request_output**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assets|[]asset|None|False|Array of asset objects associated with this request|["{\"name\": \"Software\", \"id\": 4541563, \"barcode\": \"test-barcode\"}"]|
|Category|category|None|False|Category to which this request belongs|{"name": "Operating System", "id": 8}|
|Created By|user_output|None|False|Creator of the request|{"name": "John", "id": 71}|
|Created Time|date|None|False|Time the request was created|Jul 9, 2022 04:02 AM|
|Description|string|None|False|Description of this request|Example description|
|Due By Time|date|None|False|The due date of the request|Jul 13, 2022 04:02 AM|
|Email IDs to Notify|[]string|None|False|Array of Email ids, which needs to be notified about the happenings of this request|["user@example.com"]|
|Group|group|None|False|The group to which the request belongs|{"name": "Network", "id": 2}|
|Has Notes|boolean|None|False|Indicates whether the request has notes|True|
|ID|integer|None|False|Id of the request|92|
|Impact|impact|None|False|Impact of this request|{"id": 1, "name": "High"}|
|Is Fcr|boolean|None|False|Boolean value indicating if the request has been marked as First Call Resolution|True|
|Is Overdue|boolean|None|False|Indicates if the request is overdue|True|
|Is Service Request|boolean|None|False|Indicates whether the request is a service request or not|True|
|Item|item|None|False|Item of this request|{"name": "Install", "id": 1}|
|Level|level|None|False|Level of the request|{"name": "Tier 4", "id": 4}|
|Mode|mode|None|False|The mode in which this request is created|{"name": "Web Form", "id": 4}|
|Priority|priority|None|False|Priority of the request|{"name": "High", "id": 4}|
|Request Type|request_type|None|False|Type of this request|{"id": 1, "name" "Incident"}|
|Requester|user_output|None|False|The requester of the request|{"name": "John", "id": 7, "is_vipuser": true}|
|Service Category|service_category|None|False|Service category to which this request belongs|{"name": "User Management", "id": 8}|
|Site|site|None|False|Denotes the site to which this request belongs|{"name": "Custom Site", "id": 71}|
|Status|status|None|False|Indicates the current status of this request|{"name": "Open", "id": 2}|
|Subcategory|subcategory|None|False|Subcategory to which this request belongs|{"name": "Mac OS X", "id": 24}|
|Subject|string|None|False|Subject of this request|Need a Monitor|
|Technician|technician|None|False|The technician that was assigned to the request|{"name": "John", "id": 71}|
|Udf Fields|object|None|False|Holds udf fields values associated with the request|{"udf_sline_51":"abc test.com","udf_pick_52":"Tony Stark"}|
|Urgency|urgency|None|False|Urgency of the request|{"name": "Low", "id": 1}|
  
**closure_code**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|Closure Code ID|1|
|Name|string|None|False|Closure Code name|Success|
  
**last_updated_by**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|Id of the last editor|3|
|Name|string|None|False|Name of the last editor|Samuel|
  
**added_by**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|integer|None|False|Id of the creator|3|
|Name|string|None|False|Name of the creator|Samuel|
  
**note**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Added By|added_by|None|False|Added by details|{"name": "John", "id": 71}|
|Added Time|date|None|False|The time the request note was added|Jul 8, 2022 02:01 AM|
|ID|integer|None|False|Note ID|543|
|Last Updated By|last_updated_by|None|False|Last updated by details|{"name": "John", "id": 71}|
|Last Updated Time|date|None|False|The time the request note was updated|Jul 9, 2022 04:02 AM|
|Show to Requester|boolean|None|False|Whether to show the note to requester or not|False|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.0.2 - Bumping requirements.txt | SDK bump to 6.1.4
* 1.0.1 - Fix `int` conversion issue in `Get List Request` and `Get Request` actions
* 1.0.0 - Initial plugin - Create actions: `Add Request`, `Add Request Note`, `Add Resolution`, `Assign Request`, `Close Request`, `Delete Request`, `Delete Request Note`, `Edit Request`, `Edit Request Note`, `Get List Request`, `Get List Request Notes`, `Get Request`, `Get Resolution`, `Pickup Request`

# Links

* [Manage Engine Service Desk](https://manageengine.com/products/service-desk)

## References

* [Manage Engine Service Desk API Docs](https://www.manageengine.com/products/service-desk/sdpod-v3-api)