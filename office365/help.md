
# Office 365

## About

**This plugin is deprecated in favor of the Office365 Email plugin**

The Office 365 plugin allows access to Outlook email, email folders, email attachments, and contact lists, as well as offering a trigger
when email arrives via the [Microsoft Graph API](https://developer.microsoft.com/en-us/graph).

For documentation on setting up an Office 365 connection, please refer to [Configuring an Office365 Connection](https://docs.komand.com/docs/configuring-an-office-365-connection).

## Actions

### Get Attachments

This action is used to get a list of attachments for the given message.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id_principal|string|None|True|Identifies the user|None|
|pagination_token|string|None|False|Token to request the next 50 attachments|None|
|message_id|string|None|True|ID of the message with attachment|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|attachments|[]attachment|False|List of attachments to the given message|
|pagination_token|string|False|Token to request the next 50 attachments|

Example output:

```

{
      "attachments": [{
              "IsInline": false,
              "Name": "32105676_10216101849685309_8418589745059201024_o.jpg",
              "Id": "AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwBGAAAAAAAxDvrPc8q6SqGLTJ9iB-SGBwC8UQDN7ObVSLWQuxHJ-dDTAAAUtfMmAAC8UQDN7ObVSLWQuxHJ-dDTAAAUtgyJAAABEgAQAMRZrVj9g6FEsjox_bYKKs8=",
              "ContentLocation": "",
              "LastModifiedDateTime": "2018-05-23T20:26:41Z",
              "@odata.type": "#microsoft.graph.fileAttachment",
              "ContentBytes": "",
              "ContentType": "image/jpeg",
              "Size": 200713
      }],
      "pagination_token": ""
}

```

### Copy Folder

This action is used to copy a mailbox folder underneath the given parent.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|other_parent_id|string|None|False|ID of the new parent folder (if not well-known)|None|
|well_known_parent_id|string|None|True|Well-known ID of the new parent folder (e.g. Inbox)|['Inbox', 'Drafts', 'SentItems', 'DeletedItems', '<other folder>']|
|user_id_principal|string|None|True|Identifies the user|None|
|folder_id|string|None|True|ID of the folder to copy|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|new_folder_id|string|False|ID of the newly copied folder|

Example output:

```

{
  "new_folder_id": "AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwAuAAAAAAAxDvrPc8q6SqGLTJ9iB-SGAQC8UQDN7ObVSLWQuxHJ-dDTAAAUtfMpAAA="
}

```

### Most Recently Sent

This action is used to get the most recent message in the sentitems folder.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id_principal|string|None|True|Identifies the user|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|most_recent_message|message|False|The most recent message in the SentItems folder|

Example output:

```

{
      "most_recent_message": {
              "BccRecipients": [],
              "Body": {
                      "ContentType": "html",
                      "Content": "Test"
              },
              "ParentFolderId": "AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwAuAAAAAAAxDvrPc8q6SqGLTJ9iB-SGAQC8UQDN7ObVSLWQuxHJ-dDTAAAUtfMmAAA=",
              "Subject": "Test Email 2",
              "ToRecipients": [{
                      "EmailAddress": {
                              "Name": "Tester1",
                              "Address": "test@test.com"
                      }
              }],
              "Attachments": null,
              "Importance": "normal",
              "ReplyTo": [],
              "SentDateTime": "2018-05-23T20:26:50Z",
              "ConversationId": "AAQkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwAQADZLwG6j1HNChIz3Jg9cbl4=",
              "CcRecipients": [],
              "CreatedDateTime": "2018-05-23T20:26:51Z",
              "From": {
                      "EmailAddress": {
                              "Name": "Tester1",
                              "Address": "test@test.com"
                      }
              },
              "HasAttachments": true,
              "LastModifiedDateTime": "2018-05-23T20:26:54Z",
              "Sender": {
                      "EmailAddress": {
                              "Name": "Tester1",
                              "Address": "test @test.com"
                      }
              },
              "Id": "AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwBGAAAAAAAxDvrPc8q6SqGLTJ9iB-SGBwC8UQDN7ObVSLWQuxHJ-dDTAAAUtfMmAAC8UQDN7ObVSLWQuxHJ-dDTAAAUtgyJAAA=",
              "IsRead": false,
              "ReceivedDateTime": "2018-05-23T20:26:51Z",
              "BodyPreview": "Test body"
      }
}

```

### Move Folder

This action is used to move a mailbox folder to a new parent.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|other_parent_id|string|None|False|ID of the new parent folder (if not well-known)|None|
|well_known_parent_id|string|None|True|Well-known ID of the new parent folder (e.g. Inbox)|['Inbox', 'Drafts', 'SentItems', 'DeletedItems', '<other folder>']|
|user_id_principal|string|None|True|Identifies the user|None|
|folder_id|string|None|True|ID of the folder to move|None|

#### Output

This action does not contain any outputs.

### Copy Message

This action is used to copy an email message to a folder.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|well_known_folder_id|string|None|True|Well-known folder ID (e.g. Inbox) to which to copy the message|['Inbox', 'Drafts', 'SentItems', 'DeletedItems', '<other folder>']|
|other_folder_id|string|None|False|Folder ID to which to copy the message (if not well-known)|None|
|user_id_principal|string|None|True|Identifies the user|None|
|message_id|string|None|True|ID of the message to copy|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|new_message_id|string|False|ID of the newly copied message|

Example output:

```

{
  "new_message_id": "AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwBGAAAAAAAxDvrPc8q6SqGLTJ9iB-SGBwC8UQDN7ObVSLWQuxHJ-dDTAAAUtfMmAAC8UQDN7ObVSLWQuxHJ-dDTAAAUtgyLAAA="
}

```

### Create Attachment

This action is used to create an attachment for the given message.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|other_attachment_type|string|None|False|User-specified content type not in the enumerated list|None|
|attachment_name|string|None|True|Name of the new attachment|None|
|attachment_content|string|None|True|Content of the new attachment (base64 encoded)|None|
|attachment_type|string|None|False|MIME type of the email attachment (if any)|['text/plain (.txt)', 'text/html (.html)', 'application/rtf (.rtf)', 'application/pdf (.pdf)', 'application/msword (.doc)', 'application/vnd.ms-powerpoint (.ppt)', 'image/bmp (.bmp)', 'image/gif (.gif)', 'image/jpeg (.jpg)', 'image/png (.png)', 'image/tiff (.tiff)', 'OTHER']|
|user_id_principal|string|None|True|Identifies the user|None|
|message_id|string|None|True|ID of the message in which to create the attachment|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|attachment_id|string|False|ID of the new attachment|

Example output:

```

{
  "attachment_id": "AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwBGAAAAAAAxDvrPc8q6SqGLTJ9iB-SGBwC8UQDN7ObVSLWQuxHJ-dDTAAAAAAEMAAC8UQDN7ObVSLWQuxHJ-dDTAAAUtetcAAABEgAQAIIZJ3rcXqlDiO98vCM9hJc="
}

```

### Get Contacts

This action is used to get a list of contacts for user or principal.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id_principal|string|None|True|Identifies the user|None|
|pagination_token|string|None|False|Token to request the next 50 contacts|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|pagination_token|string|False|Token to request the next 50 contacts|
|contacts|[]contact|False|List of all contacts under the email account|

Example output:

```

{
      "contacts": [{
              "MiddleName": "",
              "OfficeLocation": "",
              "Id": "AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwBGAAAAAAAxDvrPc8q6SqGLTJ9iB-SGBwC8UQDN7ObVSLWQuxHJ-dDTAAAAAAEOAAC8UQDN7ObVSLWQuxHJ-dDTAAAUthhFAAA=",
              "DisplayName": "Mike Rinehart",
              "Surname": "Rinehart",
              "AssistantName": "",
              "JobTitle": "",
              "Department": "",
              "HomeAddress": {
                      "CountryOrRegion": "",
                      "PostalCode": "",
                      "Street": "",
                      "City": "",
                      "State": ""
              },
              "Manager": "",
              "YomiSurname": "",
              "BusinessAddress": {
                      "CountryOrRegion": "",
                      "PostalCode": "",
                      "Street": "",
                      "City": "",
                      "State": ""
              },
              "BusinessPhones": [],
              "Title": "",
              "YomiCompanyName": "",
              "HomePhones": [],
              "Profession": "",
              "Generation": "",
              "LastModifiedDateTime": "2018-05-23T20:52:34Z",
              "EmailAddresses": [{
                      "Name": "Mike",
                      "Address": "mrinehart@rapid7.com"
              }],
              "YomiGivenName": "",
              "Initials": "",
              "MobilePhone1": "",
              "FileAs": "Rinehart, Mike",
              "NickName": "",
              "OtherAddress": {
                      "CountryOrRegion": "",
                      "PostalCode": "",
                      "Street": "",
                      "City": "",
                      "State": ""
              },
              "CompanyName": "",
              "CreatedDateTime": "2018-05-23T20:52:34Z",
              "ImAddresses": [],
              "BusinessHomePage": "",
              "GivenName": "Mike"
      }],
      "pagination_token": ""
}

```

### Delete Attachment

This action is used to delete an attachment from a message.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|attachment_id|string|None|True|ID of the attachment to delete|None|
|user_id_principal|string|None|True|Identifies the user|None|
|message_id|string|None|True|ID of the message whose attachment will be deleted|None|

#### Output

This action does not contain any outputs.

### Reply To Message

This action is used to reply to an email message.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comment|string|None|True|Comment in the reply|None|
|user_id_principal|string|None|True|Identifies the user|None|
|message_id|string|None|True|ID of the message being replied to|None|

#### Output

This action does not contain any outputs.

### Delete Folder

This action is used to delete a mailbox folder.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id_principal|string|None|True|Identifies the user|None|
|folder_id|string|None|True|ID of the folder to delete|None|

#### Output

This action does not contain any outputs.

### Create Folder

This action is used to create a new mailbox folder.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|other_parent_id|string|None|False|ID of the parent folder of the new folder (if not well-known)|None|
|well_known_parent_id|string|None|True|Well-known ID of the parent folder (e.g. Inbox) of the new folder|['Inbox', 'Drafts', 'SentItems', 'DeletedItems', '<other folder>']|
|user_id_principal|string|None|True|Identifies the user|None|
|folder_name|string|None|True|Display name of the new folder|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|folder_id|string|False|ID of the new folder|

Example output:

```

{
  "folder_id": "AAMkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwAuAAAAAAAxDvrPc8q6SqGLTJ9iB-SGAQC8UQDN7ObVSLWQuxHJ-dDTAAAUtfMoAAA="
}

```

### Delete Message

This action is used to delete an email message.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id_principal|string|None|True|Identifies the user|None|
|message_id|string|None|True|ID of the message to delete|None|

#### Output

This action does not contain any outputs.

### Move Message

This action is used to move an email message to a different folder.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|well_known_folder_id|string|None|True|Well-known folder ID (e.g. Inbox) to which to move the message|['Inbox', 'Drafts', 'SentItems', 'DeletedItems', '<other folder>']|
|other_folder_id|string|None|False|Folder ID to which to move the message (if not well-known)|None|
|user_id_principal|string|None|True|Identifies the user|None|
|message_id|string|None|True|ID of the message to move|None|

#### Output

This action does not contain any outputs.

### Get Folders

This action is used to get a list of folders under a given email folder.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|other_parent_id|string|None|False|ID of the parent folder whose subfolders to list (if not well-known)|None|
|well_known_parent_id|string|None|True|Well-known ID of the parent folder (e.g. Inbox) whose subfolders to list|['Inbox', 'Drafts', 'SentItems', 'DeletedItems', '<other folder>']|
|user_id_principal|string|None|True|Identifies the user|None|
|pagination_token|string|None|False|Token to request the next 50 folders|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|folders|[]folder|False|List of folders|
|pagination_token|string|False|Token to request the next 50 folders|

Example output:

```

{
      "folders": [{
              "Messages": null,
              "ParentFolderId": "AQMkADI3Mzc1ZTg3LTIzYWEALTQzZjYtYWQ0OS0wYjIwM2MwN2U4YWMALgAAAzEO_s9zyrpKoYtMn2IH9IYBALxRAM3s5tVItZC7Ecn90NMAAAIBCAAAAA==",
              "TotalItemCount": 3,
              "UnreadItemCount": 0,
              "Id": "AQMkADI3Mzc1ZTg3LTIzYWEALTQzZjYtYWQ0OS0wYjIwM2MwN2U4YWMALgAAAzEO_s9zyrpKoYtMn2IH9IYBALxRAM3s5tVItZC7Ecn90NMAAAIBCQAAAA==",
              "ChildFolderCount": 0,
              "DisplayName": "Sent Items"
      }],
      "pagination_token": ""
}

```

### Forward Message

This action is used to forward an email message.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|comment|string|None|False|Comment in the forwarded message|None|
|message_id|string|None|True|ID of the message being forwarded|None|
|user_id_principal|string|None|True|Identifies the user|None|
|to_recipients|[]string|None|True|Emails of the recipients of the forwarded message|None|

#### Output

This action does not contain any outputs.

### Create And Send

This action is used to create and send a new email message.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|body|string|None|False|Body of the email|None|
|cc_recipients|[]string|None|False|Carbon-copied recipients of the email|None|
|save_to_sent_items|boolean|True|False|Save this message to the SentItems folder|None|
|to_recipients|[]string|None|True|Main recipients of the email|None|
|user_id_principal|string|None|True|Identifies the user|None|
|attachment_bytes|string|None|False|Bytes of the email attachment (in base-64 format)|None|
|other_attachment_type|string|None|False|User-specified content type not in the enumerated list|None|
|bcc_recipients|[]string|None|False|Blind carbon-copied recipients of the email|None|
|attachment_name|string|None|False|Name of the email attachment (if any)|None|
|body_is_html|boolean|None|False|True if the body of the message is in HTML format|None|
|attachment_type|string|None|False|MIME type of the email attachment (if any)|['text/plain (.txt)', 'text/html (.html)', 'application/rtf (.rtf)', 'application/pdf (.pdf)', 'application/msword (.doc)', 'application/vnd.ms-powerpoint (.ppt)', 'image/bmp (.bmp)', 'image/gif (.gif)', 'image/jpeg (.jpg)', 'image/png (.png)', 'image/tiff (.tiff)', 'OTHER']|
|subject|string|None|True|Subject of the email|None|

#### Output

This action does not contain any outputs.

### Get Messages

This action is used to get a list of messages in the given folder.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|well_known_folder_id|string|None|True|Well-known folder ID (e.g. Inbox) whose messages to list|['Inbox', 'Drafts', 'SentItems', 'DeletedItems', '<other folder>']|
|selected_fields|string|None|False|Comma-separated list of email fields to retrieve (if omitted, all fields)|None|
|other_folder_id|string|None|False|Folder ID whose messages to list (if not well-known)|None|
|user_id_principal|string|None|True|Identifies the user|None|
|pagination_token|string|None|False|Token to request the next 50 messages|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|messages|[]message|False|List of messages in the given folder|
|pagination_token|string|False|Token to request the next 50 messages|

Example output:

```

{
      "messages": [{
              "BccRecipients": [],
              "Body": {
                      "ContentType": "html",
                      "Content": "Test"
              },
              "ParentFolderId": "12344151451345",
              "Subject": "Test Email 2",
              "ToRecipients": [{
                      "EmailAddress": {
                              "Name": "Tester1",
                              "Address": "test@test.com"
                      }
              }],
              "Attachments": null,
              "Importance": "normal",
              "ReplyTo": [],
              "SentDateTime": "2018-05-23T20:26:50Z",
              "ConversationId": "AAQkADI3Mzc1ZTg3LTIzYWEtNDNmNi1hZDQ5LTBiMjAzYzA3ZThhYwAQADZLwG6j1HNChIz3Jg9cbl4=",
              "CcRecipients": [],
              "CreatedDateTime": "2018-05-23T20:26:51Z",
              "From": {
                      "EmailAddress": {
                              "Name": "Tester1",
                              "Address": "test@test.com"
                      }
              },
              "HasAttachments": true,
              "LastModifiedDateTime": "2018-05-23T20:26:54Z",
              "Sender": {
                      "EmailAddress": {
                              "Name": "Tester1",
                              "Address": "test@test.com"
                      }
              },
              "Id": "1234566789",
              "IsRead": false,
              "ReceivedDateTime": "2018-05-23T20:26:51Z",
              "BodyPreview": "Test body"
      }],
      "pagination_token": ""
}

```

## Triggers

### New Message

This trigger fires when a new message is received in a given folder.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|well_known_folder_id|string|None|True|Well-known folder ID (e.g. Inbox) to monitor for new messages|['Inbox', 'Drafts', 'SentItems', 'DeletedItems', '<other folder>']|
|interval|integer|300|True|Interval of time between mailbox polling in seconds (defaults to 300)|None|
|other_folder_id|string|None|False|Folder ID to monitor for new messages (if not well-known)|None|
|user_id_principal|string|None|True|Identifies the user|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|most_recent_message|message|False|Most recent message (empty if mailbox is empty)|
|new_message_received|boolean|False|True if a new message was received in this interval|

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tenant_id|string|None|True|The ID of the directory that identifies the tenant|None|
|app_secret|password|None|True|The secret of the registered app that obtained the refresh token|None|
|app_id|string|None|True|The ID of the registered app that obtained the refresh token|None|

## Troubleshooting

### Pagination

The get_XXX actions may produce an arbitrarily large number of
objects. Pagination offers a flow control technique to address this
use case, by dividing the output into chunks of 50.

* The first time, invoke the action with the pagination_token
  parameter omitted.

* Subsequent times, use the previous output's pagination_token as
  the input pagination_token parameter.

### A not about user_id_principal

When using an action that requires user_id_principal it referring to the account
that will be used for the action or trigger. Meaning if I wanted to use the create_and_send action
and I have the user_id_principal set to testuser@testdomain.onmicrosoft.com, the email will be created
and sent from that user.

### A note about delete_folder

Deleting a folder moves it to the Deleted Items folder.  If you then
create a folder of the same name and attempt to delete it, the
action will fail because a folder of the same name exists in the
Deleted Items folder. You will need to delete the first folder from
Deleted Items, then delete the second folder.

### A note about create_and_send

The other create_XXX actions return the ID of the newly created
item, while create_and_send only returns success.  This is an
intentional feature of the Office 365 system, possibly a throttling
technique.

If you need the ID of the newly sent message, you can set the
save_to_sent_items parameter to true in the create_and_send action,
then use the most_recently_sent action to retrieve that message.

### A note about well-known folder IDs

For convenience, the Office 365 API offers the following
"well-known" folder IDs:

Inbox
Drafts
SentItems
DeletedItems

When an action requires a folder ID as input, you can either:

1. Choose a well-known folder ID from the well_known_XXX dropdown

2. Choose <other folder> in the well_known_XXX dropdown and enter
    an actual folder ID in the other_XXX field.

As a special case, note that get_folders action will get the
top-level folder list if you choose "<other folder>" in the
well_known_parent_id dropdown and leave the other_parent_id field
empty.

### A note about attachments

The create_attachment action and the attachment-related inputs to
the create_and_send action requires specifying the attachment's MIME
type. This plugin enumerates common MIME types for text and image
documents, but allows the user to specify a MIME type not in that
list. Be aware that some MIME types, such as .zip and .exe, are
considered to be security risks.

### Known deficiencies

Setting IsInline to true in an attachment does not seem to work.

## Workflows

Examples:

* Delete spam emails
* Send emails

## Versions

* 1.0.0 - Initial plugin
* 1.0.1 - Bug fix for attachments on trigger
* 2.0.0 - Updating to Go SDK 2.6.4
* 2.0.1 - Fix issue where session token expired by adding a refresh
* 2.0.2 - Regenerate with latest Go SDK to solve bug with triggers
* 2.0.3 - Fix issue where error handling was passing the wrong ouput | Update help for the parameter `user_id_principal` | Remove unused import
* 2.0.4 - Fix issue where users endpoint was out of sync with graph docs

## References

* [Microsoft Graph Users](https://developer.microsoft.com/en-us/graph/docs/api-reference/v1.0/resources/users)
