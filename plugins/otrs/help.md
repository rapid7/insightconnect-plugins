# Description

Create and manage OTRS tickets

# Key Features

* Create tickets with articles, attachments, dynamic fields, pending time and SLA
* Update tickets, optionally without adding an article
* Search for tickets by queue, customer ID, dynamic fields and other ticket fields
* Retrieve a ticket with its articles, attachments and dynamic fields

# Requirements

* OTRS server URL and the username and password of an agent account
* The `GenericTicketConnectorREST` web service configured and enabled on the OTRS server

# Supported Product Versions

* OTRS 6
* OTRS 8
* OTRS 2026.1.2

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|True|OTRS username and password|None|{"username": "agent", "password": "mypassword"}|None|None|
|server|string|None|True|OTRS server URL|None|https://otrs.example.com|None|None|

Example input:

```
{
  "credentials": {
    "password": "mypassword",
    "username": "agent"
  },
  "server": "https://otrs.example.com"
}
```

## Technical Details

### Actions


#### Create Ticket

This action is used to create OTRS ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|CustomerUser|string|None|False|Customer user associated with the ticket e.g test_customer|None|test_customer|None|None|
|Lock|string|None|False|Lock name|None|unlock|None|None|
|Owner|string|None|False|Ticket owner|None|agent|None|None|
|PendingTime|date|None|False|Pending time field|None|2026-11-01 12:00:00+00:00|None|None|
|Priority|string|None|False|Ticket priority. 1=very low, 2=low, 3=normal, 4=high, 5=very high, etc|None|3 normal|None|None|
|Queue|string|None|False|Queue the ticket is to be inserted in|None|Raw|None|None|
|Responsible|string|None|False|User responsible for the ticket|None|agent|None|None|
|SLA|string|None|False|SLA name|None|Gold|None|None|
|Service|string|None|False|Service name|None|IT Security|None|None|
|State|string|new|False|Ticket state|None|new|None|None|
|Title|string|None|False|Ticket title|None|Suspicious login detected|None|None|
|Type|string|None|False|Ticket type e.g. Incident|None|Incident|None|None|
|article|new_article|None|False|Ticket article|None|{"Subject": "Suspicious login", "Body": "Suspicious login detected for user jdoe", "MimeType": "text/plain", "Charset": "UTF-8", "CommunicationChannel": "Internal", "SenderType": "agent"}|None|None|
|attachments|[]attachment|None|False|Attachments as array of objects e.g. [{"filename":"notes.txt","content":"VGhpcyBpcyBhIHRlc3QK"}]|None|[{"filename": "notes.txt", "content": "VGhpcyBpcyBhIHRlc3QK"}]|None|None|
|dynamic_fields|[]dynamic_field|None|False|Fields as array of objects e.g. [{"name":"TestName1","pattern":"TestValue1"},{"name":"TestName2","pattern":"TestValue2"}]|None|[{"name": "TestName1", "value": "TestValue1"}]|None|None|
  
Example input:

```
{
  "CustomerUser": "test_customer",
  "Lock": "unlock",
  "Owner": "agent",
  "PendingTime": "2026-11-01 12:00:00+00:00",
  "Priority": "3 normal",
  "Queue": "Raw",
  "Responsible": "agent",
  "SLA": "Gold",
  "Service": "IT Security",
  "State": "new",
  "Title": "Suspicious login detected",
  "Type": "Incident",
  "article": {
    "Body": "Suspicious login detected for user jdoe",
    "Charset": "UTF-8",
    "CommunicationChannel": "Internal",
    "MimeType": "text/plain",
    "SenderType": "agent",
    "Subject": "Suspicious login"
  },
  "attachments": [
    {
      "content": "VGhpcyBpcyBhIHRlc3QK",
      "filename": "notes.txt"
    }
  ],
  "dynamic_fields": [
    {
      "name": "TestName1",
      "value": "TestValue1"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ticket_id|integer|False|ID of the created ticket|1|
|ticket_number|integer|False|Number of the created ticket|2026101910000011|
  
Example output:

```
{
  "ticket_id": 1,
  "ticket_number": 2026101910000011
}
```

#### Retrieve Ticket

This action is used to retrieve OTRS ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ticket_id|integer|None|False|Ticket ID|None|7|None|None|
  
Example input:

```
{
  "ticket_id": 7
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|Ticket|Ticket|False|Ticket details with articles, attachments and dynamic fields|{"TicketID": 1, "TicketNumber": "2026101910000011", "Title": "Suspicious login", "Queue": "Raw", "State": "new", "Priority": "3 normal", "Article": [{"ArticleID": "1", "TicketID": 1, "Subject": "Suspicious login", "Body": "Investigate login from new location", "IsVisibleForCustomer": 1}], "DynamicField": [{"Name": "Severity", "Value": ["High"]}]}|
  
Example output:

```
{
  "Ticket": {
    "Article": [
      {
        "ArticleID": "1",
        "Body": "Investigate login from new location",
        "IsVisibleForCustomer": 1,
        "Subject": "Suspicious login",
        "TicketID": 1
      }
    ],
    "DynamicField": [
      {
        "Name": "Severity",
        "Value": [
          "High"
        ]
      }
    ],
    "Priority": "3 normal",
    "Queue": "Raw",
    "State": "new",
    "TicketID": 1,
    "TicketNumber": "2026101910000011",
    "Title": "Suspicious login"
  }
}
```

#### Ticket Search

This action is used to search for OTRS tickets

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cust_id|string|None|False|Customer ID|None|example-customer|None|None|
|dynamic_fields|[]search_dynamic_field|None|False|Fields as array of objects e.g. [{"name":"TestName1","value":"TestValue1", "operation":"Equals"},{"name":"TestName2","value":"TestValue2"}]. The value field is what will be searched for|None|[{"name": "TestName1", "value": "TestValue1", "operator": "Equals"}]|None|None|
|external_params|[]external_param|None|False|A key value object that is not a Dynamic Field e.g [{"Title":"Test Ticket"}]|None|[{"Title": "Test Ticket"}]|None|None|
|queue|string|None|False|Queue to search in|None|Raw|None|None|
  
Example input:

```
{
  "cust_id": "example-customer",
  "dynamic_fields": [
    {
      "name": "TestName1",
      "operator": "Equals",
      "value": "TestValue1"
    }
  ],
  "external_params": [
    {
      "Title": "Test Ticket"
    }
  ],
  "queue": "Raw"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ticket_ids|[]string|False|IDs of tickets matching search criteria|["1", "2"]|
  
Example output:

```
{
  "ticket_ids": [
    "1",
    "2"
  ]
}
```

#### Update Ticket

This action is used to update OTRS ticket

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|Article|new_article|None|False|New article (gets appended)|None|{"Subject": "Suspicious login", "Body": "Suspicious login detected for user jdoe", "MimeType": "text/plain", "Charset": "UTF-8", "CommunicationChannel": "Internal", "SenderType": "agent"}|None|None|
|Attachments|[]attachment|None|False|New attachments as array of objects e.g. [{"filename":"notes.txt","content":"VGhpcyBpcyBhIHRlc3QK"}]|None|[{"filename": "notes.txt", "content": "VGhpcyBpcyBhIHRlc3QK"}]|None|None|
|CustomerUser|string|None|False|Updated customer user|None|test_customer|None|None|
|DynamicFields|[]dynamic_field|None|False|Updated dynamic fields e.g. [{"name":"TestName1","value":"TestValue1"},{"name":"TestName2","value":"TestValue2"}]|None|[{"name": "TestName1", "value": "TestValue1"}]|None|None|
|Lock|string|None|False|Lock|None|lock|None|None|
|NoArticle|boolean|None|True|Will not add article to ticket|None|False|None|None|
|PendingTime|date|None|False|Pending time|None|2026-11-01 12:00:00+00:00|None|None|
|Priority|string|None|False|Updated ticket priority e.g. 1 very low, 2 low, 3 normal, 4 high, 5 very high and so on|None|4 high|None|None|
|Queue|string|None|False|Updated queue|None|Junk|None|None|
|Responsible|string|None|False|Responsible|None|agent|None|None|
|SLA|string|None|False|SLA|None|Gold|None|None|
|Service|string|None|False|Service|None|IT Security|None|None|
|TicketID|integer|None|False|Ticket ID|None|7|None|None|
|Title|string|None|False|Updated title|None|Suspicious login confirmed|None|None|
|Type|string|None|False|Updated type e.g. Incident|None|Incident|None|None|
  
Example input:

```
{
  "Article": {
    "Body": "Suspicious login detected for user jdoe",
    "Charset": "UTF-8",
    "CommunicationChannel": "Internal",
    "MimeType": "text/plain",
    "SenderType": "agent",
    "Subject": "Suspicious login"
  },
  "Attachments": [
    {
      "content": "VGhpcyBpcyBhIHRlc3QK",
      "filename": "notes.txt"
    }
  ],
  "CustomerUser": "test_customer",
  "DynamicFields": [
    {
      "name": "TestName1",
      "value": "TestValue1"
    }
  ],
  "Lock": "lock",
  "NoArticle": false,
  "PendingTime": "2026-11-01 12:00:00+00:00",
  "Priority": "4 high",
  "Queue": "Junk",
  "Responsible": "agent",
  "SLA": "Gold",
  "Service": "IT Security",
  "TicketID": 7,
  "Title": "Suspicious login confirmed",
  "Type": "Incident"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ticket_id|integer|False|ID of the updated ticket|1|
|ticket_number|integer|False|Number of the updated ticket|2026101910000011|
  
Example output:

```
{
  "ticket_id": 1,
  "ticket_number": 2026101910000011
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**new_article**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Auto Response Type|string|None|False|Auto response type|None|
|Body|string|None|False|Ticket body|None|
|Charset|string|UTF-8|True|Character set e.g. UTF-8|None|
|Communication Channel|string|None|False|Communication channel|None|
|Communication Channel ID|integer|None|False|Communication channel ID|None|
|Content Type|string|None|False|Content type|None|
|Exclude Mute Notification|[]integer|None|False|Exclude mute notification to user ID |None|
|Exclude Notification|[]integer|None|False|Exclude notification to user ID|None|
|Force Notification|[]integer|None|False|Force notification to user ID|None|
|From|string|None|False|From|None|
|History Comment|string|None|False|History comment|None|
|History Type|string|None|False|History type|None|
|Is Visible For Customer|integer|None|False|Is visible for customer|None|
|MIME Type|string|None|False|MIME type e.g. plain/text|None|
|No Agent Notify|integer|None|False|No agent notify|None|
|Sender Type|string|None|False|Sender type|None|
|Sender Type ID|integer|None|False|Sender type ID|None|
|Subject|string|None|False|Ticket subject|None|
|Time Unit|number|None|False|Time Unit|None|
  
**Attachment**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Content|string|None|None|Content|None|
|Content Alternative|string|None|None|Content alternative|None|
|Content ID|string|None|None|Content ID|None|
|Content Type|string|None|None|Content type|None|
|Disposition|string|None|None|Disposition|None|
|File ID|string|None|None|File ID|None|
|Filename|string|None|None|Filename|None|
|File Size Raw|integer|None|None|File size raw|None|
  
**Article**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Article ID|string|None|None|Article ID|None|
|Article Number|integer|None|None|Article number|None|
|Attachment|[]Attachment|None|None|Attachment|None|
|BCC|string|None|None|BCC|None|
|Body|string|None|None|Body|None|
|CC|string|None|None|CC|None|
|Change By|string|None|None|Change by|None|
|Change Time|string|None|None|Change time|None|
|Chartset|string|None|None|Charset|None|
|Communication Channel ID|string|None|None|Communication channel ID|None|
|Content Charset|string|None|None|Content charset|None|
|Content Type|string|None|None|Content type|None|
|Create By|string|None|None|Create by|None|
|Create Time|string|None|None|Create time|None|
|From|string|None|None|From|None|
|In Reply To|string|None|None|In reply to|None|
|Incoming Time|string|None|None|Incoming time|None|
|Is Visible For Customer|integer|None|None|Is visible For customer|None|
|Message ID|string|None|None|Message ID|None|
|MIME Type|string|None|None|MIME type|None|
|References|string|None|None|References|None|
|Reply To|string|None|None|Reply to|None|
|Sender type|string|None|None|Sender type|None|
|Sender Type ID|string|None|None|Sender type ID|None|
|Subject|string|None|None|Subject|None|
|Ticket ID|integer|None|None|Ticket ID|None|
|Time Unit|number|None|None|Time unit|None|
|To|string|None|None|To|None|
  
**DynamicField**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|None|Name|None|
|Value|[]string|None|None|Value|None|
  
**Ticket**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Age|integer|None|None|Age|None|
|Archive Flag|string|None|None|Archive flag|None|
|Article|[]Article|None|None|Article|None|
|Change By|string|None|None|Change by|None|
|Changed|string|None|None|Changed|None|
|Create By|string|None|None|Create by|None|
|Created|string|None|None|Created|None|
|Customer ID|string|None|None|Customer ID|None|
|Customer User ID|string|None|None|Customer user ID|None|
|Dynamic Field|[]DynamicField|None|None|Dynamic field|None|
|Escalation Response Time|integer|None|None|Escalation response time|None|
|Escalation Solution Time|integer|None|None|Escalation solution time|None|
|Escalation Time|integer|None|None|Escalation time|None|
|Escalation Update Time|integer|None|None|Escalation update time|None|
|Group ID|string|None|None|Group ID|None|
|Lock|string|None|None|Lock|None|
|Lock ID|string|None|None|Lock ID|None|
|Owner|string|None|None|Owner|None|
|Owner ID|string|None|None|Owner ID|None|
|Priority|string|None|None|Priority|None|
|Priority ID|string|None|None|Priority ID|None|
|Queue|string|None|None|Queue|None|
|Queue ID|string|None|None|Queue ID|None|
|Real Till Time Not Used|string|None|None|Real till time not used|None|
|Responsible|string|None|None|Responsible|None|
|Responsible ID|string|None|None|Responsible ID|None|
|SLAID|string|None|None|SLAID|None|
|Service ID|string|None|None|Service ID|None|
|State|string|None|None|State|None|
|State ID|string|None|None|State ID|None|
|State Type|string|None|None|State type|None|
|Ticket ID|integer|None|None|Ticket ID|None|
|Ticket Number|string|None|None|Ticket number|None|
|Time Unit|number|None|None|Time unit|None|
|Title|string|None|None|Title|None|
|Type|string|None|None|Type|None|
|Type ID|string|None|None|Type ID|None|
|Unlock Timeout|string|None|None|Unlock timeout|None|
|Until Time|integer|None|None|Until time|None|
  
**article**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Article ID|string|None|False|Article ID|None|
|Article Number|string|None|False|Article number|None|
|BCC|string|None|False|Blind carbon copy|None|
|Body|string|None|False|Ticket body|None|
|CC|string|None|False|Carbon copy|None|
|Change By|string|None|False|Changed by|None|
|Change Time|string|None|False|Change time|None|
|Charset|string|None|False|Character set e.g. UTF-8|None|
|Communication Channel|string|None|False|Communication channel|None|
|Communication Channel ID|string|None|False|Communication channel ID|None|
|Content Charset|string|None|False|Content charset|None|
|Content Type|string|None|False|Content type|None|
|Created At|string|None|False|Create time|None|
|Created By|string|None|False|Created by|None|
|Exclude Mute Notification|[]integer|None|False|Exclude mute notification to user ID |None|
|Exclude Notification|[]integer|None|False|Exclude notification to user ID|None|
|Force Notification|[]integer|None|False|Force notification to user ID|None|
|From|string|None|False|From|None|
|History Comment|string|None|False|History comment|None|
|History Type|string|None|False|History type|None|
|In Reply To|string|None|False|In reply to|None|
|Incoming Time|string|None|False|Incoming time|None|
|Is Visible For Customer|integer|None|False|Is visible for customer|None|
|Message ID|string|None|False|Message ID|None|
|MIME Type|string|None|False|MIME type e.g. plain/text|None|
|No Agent Notify|integer|None|False|No agent notify|None|
|References|string|None|False|References|None|
|Reply To|string|None|False|Reply to|None|
|Sender Type|string|None|False|Sender type|None|
|Sender Type ID|string|None|False|Sender type ID|None|
|Subject|string|None|False|Ticket subject|None|
|Ticket ID|integer|None|False|Ticket ID|None|
|Time Unit|number|None|False|Time Unit|None|
|To|string|None|False|To|None|
  
**dynamic_field**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|True|Dynamic field name|None|
|Operator|string|None|False|Dynamic field operator|None|
|Pattern|[]string|None|False|Search pattern|None|
|Value|string|None|True|Dynamic field value|None|
  
**search_dynamic_field**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|True|Dynamic field name|None|
|Operator|string|None|False|Dynamic field operator|None|
|Pattern|[]string|None|False|Search pattern|None|
|Value|string|None|False|Dynamic field value|None|
  
**attachment**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Content|bytes|None|False|Attachment Content|None|
|Filename|string|None|False|Attachment filename|None|
  
**external_param**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Name of parameter to search on|None|
|Value|string|None|False|Value to search for|None|


## Troubleshooting

* The plugin uses the OTRS `GenericTicketConnectorREST` web service. Make sure it is imported and enabled in the OTRS admin interface under Web Services, and that the `Session`, `Ticket` and `TicketSearch` routes are configured
* OTRS 8 and later issue access tokens instead of session IDs. The plugin requests an access token first and falls back to a session ID on older OTRS versions automatically, so no extra configuration is needed

# Version History

* 5.0.3 - Fixed connection to OTRS 8 and later | Updated SDK to the latest version (6.6.0)
* 5.0.2 - Correct spelling in help.md
* 5.0.1 - Update dependency to PyOTRS 0.9 for authorization bug [PyOTRS issue 27](https://gitlab.com/rhab/PyOTRS/-/issues/27)
* 5.0.0 - New spec and help.md format for the Extension Library | Fix spelling of variable titled Disposition and Service in Create Ticket log message
* 4.0.1 - Fix issue in Retrieve action to handle Escalation parameters being returned as strings | Adds new parameter No Article to update, this will submit updates to a ticket without adding a generated article
* 4.0.0 - Updated the Web Service configuration file | Update dependency on PyOTRS | Fixed issue where Article and Attachment was required to update a ticket in action `update` | Added an External Parameters field to action `search` | Fixed issue with action `search` where dynamic fields were not used correctly for searching | Fixed issue where Escalation parameters where not set to the right type
* 3.0.5 - Update dependency to PyOTRS v2.1 for security bug [CWE-601](https://cwe.mitre.org/data/definitions/601.html)
* 3.0.4 - Fixed issue where SLA and Service would be set if passed as a parameter for the action Create
* 3.0.3 - Fixed issue where FilesizeRaw schema is returning a string when it needs to return an integer for Retrieve action
* 3.0.2 - Fixed retrieve action to process dynamic fields containing multiselect values
* 3.0.1 - Bug fix for dynamic fields missing values | Update web service to KomandConnectorREST
* 3.0.0 - Update all actions | Moved OTRS web service to REST | Added support for pending time to actions Create and Update
* 2.0.0 - Support web server mode | Update to new credential types | Bug fix for creating article and ticket fields
* 1.0.0 - Bug fix for creating and updating article fields
* 0.1.2 - Update to v2 Python plugin architecture | Fix bug with schema, spec, and retrieve action
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [OTRS](https://github.com/OTRS/otrs)

## References

* [OTRS](https://github.com/OTRS/otrs)
* [PyOTRS library](https://pyotrs.readthedocs.io/en/latest/)