# Description

[OTRS](https://github.com/OTRS/otrs) is the Open Source Ticket Request System.

This plugin utilizes the [OTRS Python library](https://pyotrs.readthedocs.io/en/latest/).

# Key Features

* Create tickets
* Manage tickets

# Requirements

* OTRS web server
* Update `FrameworkVersion` to the version of OTRS you're using, and import it to OTRS's web server

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|True|OTRS username and password|None|
|server|string|None|True|OTRS Server|None|

To create a REST web service please save a copy [GenericTicketConnectorREST.yml](https://gitlab.com/rhab/PyOTRS/raw/master/webservices_templates/GenericTicketConnectorREST.yml)

## Technical Details

### Actions

#### Ticket Search

This action is used to search for OTRS tickets.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cust_id|string|None|False|Customer ID|None|
|expernal_params|[]external_param|None|False|A key value object that's not a Dynamic Field e.g [{"Title"\:"Test Ticket"}]|None|
|queue|string|None|False|Queue to search in|None|
|dynamic_fields|[]dynamic_field|None|False|Fields as array of objects e.g. [{"name"\:"TestName1","pattern"\:"TestValue1", "operation"\:"Equals"},{"name"\:"TestName2","pattern"\:"TestValue2"}]. The value field is what will be searched for|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ticket_ids|[]string|False|IDs of tickets matching search criteria|

Example output:

```

{
  "ticket_ids": [
    5,
    4,
    3,
    2
  ]
}

```

#### Retrieve Ticket

This action is used to retrieve OTRS ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ticket_id|integer|None|False|Ticket ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Ticket|Ticket|False|Ticket returned|

Example output:

```

{
  "Ticket": {
    "Age": 9455,
    "PriorityID": "4",
    "Type": "Unclassified",
    "Responsible": "root@localhost",
    "StateID": "6",
    "ResponsibleID": "1",
    "ChangeBy": "1",
    "EscalationTime": "0",
    "OwnerID": "1",
    "Changed": "2018-08-29 20:20:00",
    "TimeUnit": 1,
    "RealTillTimeNotUsed": "1538241540",
    "GroupID": "1",
    "Owner": "root@localhost",
    "TypeID": "1",
    "Created": "2018-08-29 18:12:38",
    "Priority": "4 high",
    "UntilTime": 2665727,
    "EscalationUpdateTime": "0",
    "Queue": "Junk",
    "QueueID": "3",
    "State": "pending reminder",
    "Title": "Test",
    "CreateBy": "1",
    "TicketID": 52,
    "StateType": "pending reminder",
    "UnlockTimeout": "1535574000",
    "EscalationResponseTime": "0",
    "EscalationSolutionTime": "0",
    "LockID": "1",
    "TicketNumber": "2018082901000049",
    "ArchiveFlag": "n",
    "Lock": "unlock",
    "Article": [
      {
        "Attachment": [
          {
            "Filename": "dump.txt",
            "ContentType": "text/plain",
            "Disposition": "attachment",
            "FilesizeRaw": "15",
            "Content": "VGhpcyBpcyBhIHRlc3QK\n",
            "FileID": "1"
          }
        ],
        "ContentType": "text/plain; charset=iso-8859-15",
        "SenderTypeID": "1",
        "ContentCharset": "iso-8859-15",
        "SenderType": "agent",
        "CreateBy": "1",
        "TicketID": 52,
        "Body": "blah",
        "ChangeBy": "1",
        "ChangeTime": "2018-08-29 18:12:38",
        "MimeType": "text/plain",
        "Subject": "UnitTest",
        "IsVisibleForCustomer": 0,
        "CreateTime": "2018-08-29 18:12:38",
        "IncomingTime": "1535566358",
        "TimeUnit": 1,
        "Charset": "iso-8859-15",
        "CommunicationChannelID": "1",
        "ArticleNumber": 1,
        "ArticleID": "92",
        "To": "Junk",
        "From": "root@localhost"
      },
      {
        "Attachment": [
          {
            "Filename": "new_file.txt",
            "ContentType": "text/plain",
            "Disposition": "attachment",
            "FilesizeRaw": "28",
            "FileID": "1",
            "Content": "RGlkIHlvdSByZWFsbHkgZGVjb2RlIHRoaXM/Cg==\n"
          }
        ],
        "ContentType": "text/plain; charset=iso-8859-15",
        "SenderTypeID": "1",
        "ContentCharset": "iso-8859-15",
        "SenderType": "agent",
        "CreateBy": "1",
        "TicketID": 52,
        "Body": "API created Article Body",
        "ChangeBy": "1",
        "ChangeTime": "2018-08-29 18:13:07",
        "MimeType": "text/plain",
        "Subject": "UnitTest",
        "IsVisibleForCustomer": 0,
        "CreateTime": "2018-08-29 18:13:07",
        "IncomingTime": "1535566386",
        "TimeUnit": 0,
        "Charset": "iso-8859-15",
        "CommunicationChannelID": "1",
        "ArticleNumber": 2,
        "ArticleID": "94",
        "From": "root@localhost"
      },
      {
        "Attachment": [
          {
            "Filename": "new_file.txt",
            "ContentType": "text/plain",
            "Disposition": "attachment",
            "FilesizeRaw": "28",
            "FileID": "1",
            "Content": "RGlkIHlvdSByZWFsbHkgZGVjb2RlIHRoaXM/Cg==\n"
          }
        ],
        "ContentType": "text/plain; charset=iso-8859-15",
        "SenderTypeID": "1",
        "ContentCharset": "iso-8859-15",
        "SenderType": "agent",
        "CreateBy": "1",
        "TicketID": 52,
        "Body": "API created Article Body",
        "ChangeBy": "1",
        "ChangeTime": "2018-08-29 20:18:14",
        "MimeType": "text/plain",
        "Subject": "UnitTest",
        "IsVisibleForCustomer": 0,
        "CreateTime": "2018-08-29 20:18:14",
        "IncomingTime": "1535573894",
        "TimeUnit": 0,
        "Charset": "iso-8859-15",
        "CommunicationChannelID": "1",
        "ArticleNumber": 3,
        "ArticleID": "95",
        "From": "root@localhost"
      },
      {
        "Attachment": [
          {
            "Filename": "new_file.txt",
            "ContentType": "text/plain",
            "Disposition": "attachment",
            "FilesizeRaw": "28",
            "FileID": "1",
            "Content": "RGlkIHlvdSByZWFsbHkgZGVjb2RlIHRoaXM/Cg==\n"
          }
        ],
        "ContentType": "text/plain; charset=iso-8859-15",
        "SenderTypeID": "1",
        "ContentCharset": "iso-8859-15",
        "SenderType": "agent",
        "CreateBy": "1",
        "TicketID": 52,
        "Body": "API created Article Body",
        "ChangeBy": "1",
        "ChangeTime": "2018-08-29 20:19:22",
        "MimeType": "text/plain",
        "Subject": "UnitTest",
        "IsVisibleForCustomer": 0,
        "CreateTime": "2018-08-29 20:19:22",
        "IncomingTime": "1535573962",
        "TimeUnit": 0,
        "Charset": "iso-8859-15",
        "CommunicationChannelID": "1",
        "ArticleNumber": 4,
        "ArticleID": "96",
        "From": "root@localhost"
      },
      {
        "Attachment": [
          {
            "Filename": "new_file.txt",
            "ContentType": "text/plain",
            "Disposition": "attachment",
            "FilesizeRaw": "28",
            "FileID": "1",
            "Content": "RGlkIHlvdSByZWFsbHkgZGVjb2RlIHRoaXM/Cg==\n"
          }
        ],
        "ContentType": "text/plain; charset=iso-8859-15",
        "SenderTypeID": "1",
        "ContentCharset": "iso-8859-15",
        "SenderType": "agent",
        "CreateBy": "1",
        "TicketID": 52,
        "Body": "API created Article Body",
        "ChangeBy": "1",
        "ChangeTime": "2018-08-29 20:20:00",
        "MimeType": "text/plain",
        "Subject": "UnitTest",
        "IsVisibleForCustomer": 0,
        "CreateTime": "2018-08-29 20:20:00",
        "IncomingTime": "1535574000",
        "TimeUnit": 0,
        "Charset": "iso-8859-15",
        "CommunicationChannelID": "1",
        "ArticleNumber": 5,
        "ArticleID": "97",
        "From": "root@localhost"
      }
    ],
    "DynamicField": [
      {
        "Name": "NEWTEXTFIELD",
        "Value": "TestValue2"
      },
      {
        "Name": "NEWTEXTFIELD3"
      },
      {
        "Name": "ProcessManagementActivityID"
      },
      {
        "Name": "ProcessManagementProcessID"
      }
    ]
  }
}

```

#### Create Ticket

This action is used to create OTRS ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|Title|string|None|False|Ticket title|None|
|Queue|string|None|False|Queue the ticket is to be inserted in|None|
|Lock|string|None|False|Lock name|None|
|Type|string|None|False|Ticket type e.g. Incident|None|
|Service|string|None|False|Service name|None|
|SLA|string|None|False|SLA name|None|
|State|string|new|False|Ticket state|None|
|Priority|string|None|False|Ticket priority. 1=very low, 2=low, 3=normal, 4=high, 5=very high, etc|None|
|PendingTime|date|None|False|Pending time field|None|
|Owner|string|None|False|Ticket owner|None|
|Responsible|string|None|False|Whos responsible of the ticket|None|
|CustomerUser|string|None|False|Customer user associated with the ticket e.g test_customer|None|
|article|new_article|None|False|Ticket article|None|
|dynamic_fields|[]dynamic_field|None|False|Fields as array of objects e.g. [{"name"\:"TestName1","value"\:"TestValue1"},{"name"\:"TestName2","value"\:"TestValue2"}]|None|
|attachments|[]attachment|None|False|Attachments as array of objects e.g. [{"filename"\:"notes.txt","content"\:"VGhpcyBpcyBhIHRlc3QK"}]|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ticket_id|integer|False|Ticket ID|
|ticket_number|integer|False|Ticket number|

Exmple output:

```

{
  "ticket_id": 7,
  "ticket_number": 2018032601000027
}

```

#### Update Ticket

This action is used to update an OTRS ticket.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|TicketID|integer|None|False|Ticket ID|None|
|Priority|string|None|False|Updated ticket priority e.g. 1 very low, 2 low, 3 normal, 4 high, 5 very high and so on|None|
|PendingTime|date|None|False|Pending Time|None|
|Lock|string|None|False|Lock|None|
|Service|string|None|False|Service|None|
|SLA|string|None|False|SLA|None|
|Queue|string|None|False|Updated queue|None|
|Responsible|string|None|False|Responsible|None|
|Title|string|None|False|Updated title|None|
|CustomerUser|string|None|False|Updated customer user|None|
|Type|string|None|False|Updated type e.g. Incident|None|
|Article|new_article|None|False|New article (gets appended)|None|
|DynamicFields|[]dynamic_field|None|False|Updated dynamic fields e.g. [{"name"\:"TestName1","value"\:"TestValue1"},{"name"\:"TestName2","value"\:"TestValue2"}]|None|
|Attachments|[]attachment|None|False|New attachments as array of objects e.g. [{"filename"\:"notes.txt","content"\:"VGhpcyBpcyBhIHRlc3QK"}]|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ticket_id|integer|False|Ticket ID|
|ticket_number|integer|False|Ticket number|

Example output:

```

{
  "ticket_id": 7,
  "ticket_number": 2018032601000027
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 4.0.2 - New spec and help.md format for the Hub
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

## References

* [OTRS](https://github.com/OTRS/otrs)
* [pyotrs library](https://pyotrs.readthedocs.io/en/latest/)
