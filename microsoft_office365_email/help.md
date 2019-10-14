# Microsoft Office 365 Email V2

## About

Microsoft [Office365](https://products.office.com/en-US/?ms.url=office365com) is a cloud-based subscription service
that brings together the best tools for the way people work today. By combining best-in-class apps like Excel and
Outlook with powerful cloud services like OneDrive and Microsoft Teams, Office 365 lets anyone create and share
anywhere on any device. 

This plugin utilizes the [Microsoft Graph API](https://developer.microsoft.com/en-us/graph) to communicate with Office
365 Email services.

For more information on this plugin, please see our Office 365 setup documentation [here](https://insightconnect.help.rapid7.com/docs/office365).

## Actions

### Get Email from User

This action is used to get a list of emails from a user's mailbox matching search terms.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|body_contains|string|None|False|Body contains this word or phrase|None|
|from_contains|string|None|False|From address contains this (can be full e-mail address or just a domain) e.g. test@aol.com or aol.com|None|
|mailbox_id|string|None|True|Target user to retrieve email from e.g. bill.gates@hotmail.com|None|
|max_number_to_return|integer|250|False|Maximum number of emails to return. Max limit is 250 (default)|None|
|subject_contains|string|None|False|Subject contains this word or phrase|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|email_list|[]icon_email|False|List of emails|

Example output:

```
[
  {
     "icon_email":{
        "account":"bob@test.com",
        "attached_emails":[
        ],
        "attached_files":[
        ],
        "body":"This is some test body text",
        "categories":[
        ],
        "date_received":"2019-08-21T17:00:35Z",
        "flattened_attached_emails":[
        ],
        "flattened_attached_files":[
        ],
        "has_attachments":false,
        "headers":[
           {
              "name":"Received",
              "value":"from DM6PR12MB2603.namprd12.prod.outlook.com (2603:10b6:5:14c::32) by DM6PR12MB2603.namprd12.prod.outlook.com with HTTPS via DM6PR11CA0055.NAMPRD11.PROD.OUTLOOK.COM; Wed, 21 Aug 2019 17:00:35 +0000"
           },
           {
              "name":"Received",
              "value":"from CY4PR1201CA0007.namprd12.prod.outlook.com (2603:10b6:910:16::17) by DM6PR12MB2603.namprd12.prod.outlook.com (2603:10b6:5:49::20) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.2178.16; Wed, 21 Aug 2019 17:00:34 +0000"
           }
        ],
        "id":"AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwBGAAAAAAAxDvrPc8q6SqGLTJ9iB-SGBwC8UQDN7ObVSLWQuxHJ-dDTAAAAAAEMAAC8UQDN7ObVSLWQuxHJ-dDTAAFBpW1BAAA=",
        "is_read":false,
        "recipients":[
           "bob@test.com"
        ],
        "sender":"support@rapid7.com",
        "subject":"Test Subject"
     }
  }
]
```

### Delete Email

This action is used to delete an email by ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email_id|string|None|True|ID of email to delete|None|
|mailbox_id|string|None|True|User mailbox ID to delete from e.g. bobby.tables@hotmail.com|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was delete successful|

Example output:

```
{
    "success": true
}
```

### Move Email

This action is used to move an email to a destination folder.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email_id|string|None|True|The email ID to retrieve, e.g. ASDFXJALNASDFASDFweraswrreASDAFDASDF=|None|
|folder_name|string|None|True|The destination folder name, e.g. Inbox|None|
|mailbox_id|string|None|True|Mailbox ID e.g. test@rapid7.com|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Was move successful|

Example output:

```
{
  "success": true
}
```

### Send Email

This action is used to send an email.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|attachment|file|None|False|Attachment|None|
|bcc|[]string|None|False|Blind carbon copy recipients|None|
|body|string|None|True|Body of the email|None|
|cc|[]string|None|False|Carbon copy recipients|None|
|email_from|string|None|True|Email address this email will be sent from|None|
|email_to|string|None|True|Email address of recipients|None|
|is_html|boolean|None|True|Is the body of this email HTML|None|
|subject|string|None|True|Subject of the email|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Success|

Example output:

```
{
  "success": true
}
```

## Triggers

### Email Received

This trigger is used to poll mailbox for new email.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|flatten_attachments|boolean|False|True|Will return all attachments as flat lists instead of nested emails|None|
|folder_name|string|None|False|Common values are Calendar, Trash, Drafts, Inbox, Outbox, Sent, Junk, Tasks, Contacts. You can also use a completely custom value, for example python_mailing_list. Mailbox names are case-sensitive|None|
|interval|integer|15|False|How often to poll for new email in seconds|None|
|mailbox_id|string|None|True|The mailbox to monitor for incoming email e.g. bob@hotmail.com|None|
|subject_query|string||False|Query to search for in subject (regex capable). Only these email will activate this trigger|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|icon_email|icon_email|False|Email|

Example output:

```
{
   "icon_email":{
      "account":"bob@test.com",
      "attached_emails":[

      ],
      "attached_files":[

      ],
      "body":"This is some test body text",
      "categories":[

      ],
      "date_received":"2019-08-21T17:00:35Z",
      "flattened_attached_emails":[

      ],
      "flattened_attached_files":[

      ],
      "has_attachments":false,
      "headers":[
         {
            "name":"Received",
            "value":"from DM6PR12MB2603.namprd12.prod.outlook.com (2603:10b6:5:14c::32) by DM6PR12MB2603.namprd12.prod.outlook.com with HTTPS via DM6PR11CA0055.NAMPRD11.PROD.OUTLOOK.COM; Wed, 21 Aug 2019 17:00:35 +0000"
         },
         {
            "name":"Received",
            "value":"from CY4PR1201CA0007.namprd12.prod.outlook.com (2603:10b6:910:16::17) by DM6PR12MB2603.namprd12.prod.outlook.com (2603:10b6:5:49::20) with Microsoft SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.2178.16; Wed, 21 Aug 2019 17:00:34 +0000"
         }
      ],
      "id":"AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwBGAAAAAAAxDvrPc8q6SqGLTJ9iB-SGBwC8UQDN7ObVSLWQuxHJ-dDTAAAAAAEMAAC8UQDN7ObVSLWQuxHJ-dDTAAFBpW1BAAA=",
      "is_read":false,
      "recipients":[
         "bob@test.com"
      ],
      "sender":"support@rapid7.com",
      "subject":"Test Subject"
   }
}
```

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|app_id|string|None|True|The ID of the registered app that obtained the refresh token|None|
|app_secret|credential_secret_key|None|True|The secret of the registered app that obtained the refresh token|None|
|tenant_id|string|None|True|The ID of the directory that identifies the tenant|None|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

## Workflows

Examples:

* Receive email for analysis
* Send email with results of trigger or action

## Versions

* 1.0.0 - Initial plugin
* 1.0.1 - Fix issue in Email Received trigger where plugin crashes when new messages are not found
* 1.0.2 - Fix issue where `mailbox_name` was not working
* 1.0.3 - Update to add `only_new_email` to Email Received trigger
* 1.1.0 - Update to add delete email action
* 1.2.0 - Update to add get messages from user
* 1.2.1 - Update to support child folders
* 1.2.2 - Update to add better logging
* 1.3.0 - Update to add `raw_attachments` to email type
* 2.0.0 - Update to align output with standard email plugin signature | Fix issue to retrieve address attachments in attachments
* 2.0.1 - Fix issue where content_type_to_parse is undefined
* 2.0.2 - Fix issue where attachments were not flattened | Fix issue where correct account wasn't used in Get Message from User
* 2.0.3 - Fix issue where Microsoft .msg was not returned
* 2.0.4 - Fix issue in Email Received trigger where a soft newline in the body of the email causes a line break
* 2.1.0 - New trigger Email ID Received | New actions: Get Raw Email from ID, Get Microsoft Message from ID, Get Attachment IDs from Microsoft Message, Get Microsoft Attachment by ID, Get Microsoft Extended Item Attachment, Get Raw Attachment by ID
* 2.1.1 - Fix issue where Get Attachment IDs could fail with invalid output
* 2.1.2 - Fix issue where only the first ten folders were searched when looking for a specific folder
* 2.2.0 - New actions Get Folder ID by Name, Move Message and Get Folders
* 2.3.0 - New trigger Microsoft Message Received
* 2.4.0 - Update to make Microsoft Message Received trigger return attachments if available
* 2.5.0 - Update to make Get Microsoft Message from ID return attachments if available
* 3.0.0 - Fix issue where Email Received trigger could fail on a malformed attachment | Update to add option to remove Microsoft Newlines to Email Received | Update to add option to remove Microsoft Newlines to Get Raw Email by ID
* 4.0.0 - Update to unify Microsoft Message Received trigger and increase stability | Fixes issue where unicode emails could crash the trigger | Update for more robust error handling
* 4.0.1 - Fix issue where Email would break up URLs with quoted-printable characters

## References

* [Graph API](https://docs.microsoft.com/en-us/graph/api/resources/message?view=graph-rest-1.0)
* [Microsoft Office 365](https://products.office.com/)
* [Rapid7 Office 365 Setup Guide](https://insightconnect.help.rapid7.com/docs/office365)

## Custom Output Types

### header

|Name|Type|Required|Description|
|----|----|--------|-----------|
|name|string|False|None|
|value|string|False|None|

### attachment_file

|Name|Type|Required|Description|
|----|----|--------|-----------|
|content|string|False|None|
|content_type|string|False|None|
|name|string|False|None|

### attachment_email_nested_two

|Name|Type|Required|Description|
|----|----|--------|-----------|
|account|string|False|None|
|attached_emails|[]object|False|None|
|attached_files|[]attachment_file|False|None|
|body|string|False|None|
|categories|[]string|False|None|
|headers|[]header|False|None|
|id|string|False|None|
|sender|string|False|None|
|subject|string|False|None|

### attachment_email_nested

|Name|Type|Required|Description|
|----|----|--------|-----------|
|account|string|False|None|
|attached_emails|[]attachment_email_nested_two|False|None|
|attached_files|[]attachment_file|False|None|
|body|string|False|None|
|categories|[]string|False|None|
|headers|[]header|False|None|
|id|string|False|None|
|sender|string|False|None|
|subject|string|False|None|

### attachment_email

|Name|Type|Required|Description|
|----|----|--------|-----------|
|account|string|False|None|
|attached_emails|[]attachment_email_nested|False|None|
|attached_files|[]attachment_file|False|None|
|body|string|False|None|
|categories|[]string|False|None|
|headers|[]header|False|None|
|id|string|False|None|
|sender|string|False|None|
|subject|string|False|None|

### icon_email

|Name|Type|Required|Description|
|----|----|--------|-----------|
|account|string|False|Account for which the email was found on|
|attached_emails|[]attachment_email|False|None|
|attached_files|[]attachment_file|False|None|
|body|string|False|None|
|categories|[]string|False|None|
|flattened_attached_emails|[]attachment_email|False|None|
|flattened_attached_files|[]attachment_file|False|None|
|headers|[]header|False|None|
|id|string|False|None|
|is_read|boolean|False|Whether or not the email has been read|
|sender|string|False|None|
|subject|string|False|None|
