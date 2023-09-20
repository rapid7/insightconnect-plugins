# Description

[Microsoft Teams](https://products.office.com/en-us/microsoft-teams/group-chat-software) is a unified communications platform that combines persistent workplace chat, video meetings, file storage, and application integration. The Microsoft Teams plugin allows you to send and trigger workflows on new messages. The plugin will also allow for teams management with the ability to add and remove teams, channels, and users.

This plugin uses the [Microsoft Teams API](https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0) to interact with Microsoft Teams.

# Key Features

* Communication Management for all microsoft products

# Requirements

* Username and Password
* Secret Key, similar to API Key

# Supported Product Versions
  
* Microsoft Graph API v1.0 2021-11-28

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|application_id|string|None|True|Application (client) ID|None|63a0cad6-ac64-435c-a221-5d37c97b763e|
|application_secret|credential_secret_key|None|True|Application secret|None|aMeCAEYdOLlK+qRcD9AjdyxLkCaqZH1UPm7adjJQ5Og=|
|directory_id|string|None|True|Directory (tenant) ID|None|9e538ff5-dcb2-46a9-9a28-f93b8250deb0|
|username_password|credential_username_password|None|True|Username and password|None|{ "username": "user", "password": "mypassword" }|
  
Example input:

```
{
  "application_id": "63a0cad6-ac64-435c-a221-5d37c97b763e",
  "application_secret": "aMeCAEYdOLlK+qRcD9AjdyxLkCaqZH1UPm7adjJQ5Og=",
  "directory_id": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0",
  "username_password": {
    "password": "mypassword",
    "username": "user"
  }
}
```

## Technical Details

### Actions


#### Add Channel to Team
  
Add a channel to a team

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_description|string|None|True|Channel description|None|This is a test channel.|
|channel_name|string|None|True|Channel name|None|InsightConnect Channel|
|channel_type|string|Standard|True|Type of channel to be added|['Standard', 'Private']|Standard|
|team_name|string|None|True|Team name|None|InsightConnect Team|
  
Example input:

```
{
  "channel_description": "This is a test channel.",
  "channel_name": "InsightConnect Channel",
  "channel_type": "Standard",
  "team_name": "InsightConnect Team"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Boolean indicating if this action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Add Group Owner
  
Add a user to the group's list of owners

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|group_name|string|None|True|Name of the group or team to which the member is to be added as the owner|None|InsightConnect Team|
|member_login|string|None|True|The login of the group member to be added as the owner|None|user@example.com|
  
Example input:

```
{
  "group_name": "InsightConnect Team",
  "member_login": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Boolean indicating if this action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Add Member to Channel
  
Add a conversation member to a private channel

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_name|string|None|True|Name of the channel to which the member is to be added|None|InsightConnect Channel|
|group_name|string|None|True|Name of the group in which the channel is located|None|InsightConnect Team|
|member_login|string|None|True|The login of the group member to be added to a channel|None|user@example.com|
|role|string|Member|True|Role of the member to add|['Owner', 'Member']|Owner|
  
Example input:

```
{
  "channel_name": "InsightConnect Channel",
  "group_name": "InsightConnect Team",
  "member_login": "user@example.com",
  "role": "Member"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Boolean indicating if this action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Add Member to Team
  
Add a member to a team

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|member_login|string|None|True|Member login e.g. user@example.com|None|user@example.com|
|team_name|string|None|True|Team name|None|InsightConnect Team|
  
Example input:

```
{
  "member_login": "user@example.com",
  "team_name": "InsightConnect Team"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Boolean indicating if this action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Create Teams Enabled Group
  
Create a group in Azure and enable it for Microsoft Teams

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|group_description|string|None|True|Group description|None|A test group|
|group_name|string|None|True|Team name|None|test_group|
|mail_enabled|boolean|None|True|Should e-mail should be enabled for this group|None|True|
|mail_nickname|string|None|True|The nickname for the email address of this group in Outlook|None|TestGroup|
|members|[]string|None|False|A list of usernames to set as members|None|["user@example.com"]|
|owners|[]string|None|False|A list of usernames to set as owners|None|["user@example.com"]|
  
Example input:

```
{
  "group_description": "A test group",
  "group_name": "test_group",
  "mail_enabled": true,
  "mail_nickname": "TestGroup",
  "members": "user@example.com",
  "owners": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|group|group|False|Information about the group that was created|None|
  
Example output:

```
{
  "group": {
    "Created Date Time": {},
    "Description": {},
    "Display Name": {},
    "ID": {},
    "Mail": {},
    "Mail Enabled": {},
    "Mail Nickname": "",
    "Security Enabled": "true"
  }
}
```

#### Delete Team
  
Delete a team and the associated group from Azure

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|team_name|string|None|True|Team Name|None|Test Team|
  
Example input:

```
{
  "team_name": "Test Team"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Boolean indicating if this action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Get Channels for Team
  
Returns all the channels associated with a team

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_name|string|None|False|Optional regex-capable channel to look for|None|InsightConnect Channel|
|team_name|string|None|True|Team name to look for|None|InsightConnect Team|
  
Example input:

```
{
  "channel_name": "InsightConnect Channel",
  "team_name": "InsightConnect Team"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|channels|[]channel|False|Array of channels|None|
  
Example output:

```
{
  "channels": [
    {
      "Description": {},
      "Display Name": "",
      "ID": {}
    }
  ]
}
```

#### Get Message in Channel
  
Retrieve a single message or a message reply in a channel

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_id|string|None|True|The ID of channel|None|11:examplechannel.name|
|message_id|string|None|True|The ID of message|None|1234567891|
|reply_id|string|None|False|The ID of reply message|None|1234567890|
|team_id|string|None|True|The ID of team|None|example-team-id|
  
Example input:

```
{
  "channel_id": "11:examplechannel.name",
  "message_id": 1234567891,
  "reply_id": 1234567890,
  "team_id": "example-team-id"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|chatMessage|False|The message object that was created|None|
  
Example output:

```
{
  "message": {
    "id": "1234567891",
    "replyToId": "1234567890",
    "etag": "1234567891",
    "messageType": "message",
    "createdDateTime": "2023-08-01T12:00:00.000Z",
    "lastModifiedDateTime": "2023-08-01T12:00:00.000Z",
    "importance": "normal",
    "locale": "en-us",
    "webUrl": "https://teams.microsoft.com/l/message/11:examplechannel.name/1234567890?groupId=example-team-id&tenantId=1&createdTime=1692623381&parentMessageId=1234567891",
    "from": {
      "user": {
        "id": "3395856c-e81f-2b73-82de-e72602f798b6",
        "displayName": "Example User",
        "userIdentityType": "aadUser",
        "tenantId": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0"
      }
    },
    "body": {
      "contentType": "text",
      "content": "tests_v1"
    },
    "channelIdentity": {
      "teamId": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0",
      "channelId": "11:examplechannel.name"
    },
    "attachments": [],
    "mentions": [],
    "reactions": []
  }
}
```

#### Get Message in Chat
  
Retrieve a single message or a message reply in a chat

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|chat_id|string|None|True|The ID of chat|None|11:examplechat.name|
|message_id|string|None|True|The ID of message|None|1234567890|
|username|string|None|True|The ID of user or his email|None|user@example.com|
  
Example input:

```
{
  "chat_id": "11:examplechat.name",
  "message_id": 1234567890,
  "username": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|chatMessage|False|The message object that was created|None|
  
Example output:

```
{
  "message": {
    "id": "1234567891",
    "etag": "1234567891",
    "messageType": "message",
    "createdDateTime": "2023-08-01T12:00:00.000Z",
    "lastModifiedDateTime": "2023-08-01T12:00:00.000Z",
    "chatId": "11:examplechat.name",
    "importance": "normal",
    "locale": "en-us",
    "from": {
      "user": {
        "id": "3395856c-e81f-2b73-82de-e72602f798b6",
        "displayName": "Example User",
        "userIdentityType": "aadUser",
        "tenantId": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0"
      }
    },
    "body": {
      "contentType": "html",
      "content": "<p>test message</p>"
    },
    "attachments": [],
    "mentions": [],
    "reactions": []
  }
}
```

#### Get Reply List

List all the replies to a message in a channel of a team.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_name|string|None|True|Channel|None|InsightConnect Channel|
|message_id|string|None|True|The ID of message|None|1234567891|
|team_name|string|None|True|Team name|None|InsightConnect Team|

Example input:

```
{
  "channel_name": "InsightConnect Channel",
  "message_id": 1234567891,
  "team_name": "InsightConnect Team"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|messages|[]chatMessage|False|The message object that was created|None|

Example output:

```
{
  "messages": [
    {
      "id": "1234567891",
      "etag": "1234567891",
      "messageType": "message",
      "createdDateTime": "2023-08-01T12:00:00.000Z",
      "lastModifiedDateTime": "2023-08-01T12:00:00.000Z",
      "chatId": "11:examplechat.name",
      "importance": "normal",
      "locale": "en-us",
      "from": {
        "user": {
          "id": "3395856c-e81f-2b73-82de-e72602f798b6",
          "displayName": "Example User",
          "userIdentityType": "aadUser",
          "tenantId": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0"
        }
      },
      "body": {
        "contentType": "html",
        "content": "<p>test message</p>"
      },
      "attachments": [],
      "mentions": [],
      "reactions": []
    }
  ]
}
```

#### Get Teams
  
Returns all the teams the configured user is allowed to see

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|team_name|string|None|False|Optional regex-capable team name to look for|None|InsightConnect Team|
  
Example input:

```
{
  "team_name": "InsightConnect Team"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|teams|[]team|False|Array of team objects|None|
  
Example output:

```
{
  "teams": [
    {
      "Description": {},
      "Display Name": "",
      "ID": {}
    }
  ]
}
```

#### Remove Channel from Team
  
Remove a channel from a team

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_name|string|None|True|Channel name|None|InsightConnect Channel|
|team_name|string|None|True|Team name|None|InsightConnect Team|
  
Example input:

```
{
  "channel_name": "InsightConnect Channel",
  "team_name": "InsightConnect Team"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Boolean indicating if this action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Remove Member from Team
  
Remove a member from a team

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|member_login|string|None|True|Member Login e.g. user@example.com|None|user@example.com|
|team_name|string|None|True|Team name|None|InsightConnect Team|
  
Example input:

```
{
  "member_login": "user@example.com",
  "team_name": "InsightConnect Team"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Boolean indicating if this action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Send HTML Message
  
Send HTML as a message

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_name|string|None|True|Channel name|None|InsightConnect Channel|
|message_content|string|None|True|HTML content to send|None|<b>Hello!</b>|
|team_name|string|None|True|Team name|None|InsightConnect Team|
|thread_id|string|None|False|To post in a thread, select parent message ID|None|1595889908700|
  
Example input:

```
{
  "channel_name": "InsightConnect Channel",
  "message_content": "<b>Hello!</b>",
  "team_name": "InsightConnect Team",
  "thread_id": 1595889908700
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|message|False|The message object that was created|None|
  
Example output:

```
{
  "message": {
    "Body": {
      "Content": "",
      "Content Type": {}
    },
    "Created Date Time": {},
    "First Word": {},
    "From": {
      "User": {
        "Display name": {},
        "ID": {}
      }
    },
    "ID": {},
    "Importance": {},
    "Locale": {},
    "Message Type": {},
    "Web URL": {},
    "Words": [
      {}
    ]
  }
}
```

#### Send Message
  
Send a message

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_name|string|None|False|Channel|None|InsightConnect Channel|
|chat_id|string|None|False|The ID of the chat|None|19:209856c0f3f847a28431deb8eb300807_thread.v2|
|message|string|None|True|Message to send|None|Hello!|
|team_name|string|None|False|Team name|None|InsightConnect Team|
|thread_id|string|None|False|To post in a thread, select parent message ID|None|1595889908700|
  
Example input:

```
{
  "channel_name": "InsightConnect Channel",
  "chat_id": "19:209856c0f3f847a28431deb8eb300807_thread.v2",
  "message": "Hello!",
  "team_name": "InsightConnect Team",
  "thread_id": 1595889908700
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|message|False|The message object that was created|None|
  
Example output:

```
{
  "message": {
    "Body": {
      "Content": "",
      "Content Type": {}
    },
    "Created Date Time": {},
    "First Word": {},
    "From": {
      "User": {
        "Display name": {},
        "ID": {}
      }
    },
    "ID": {},
    "Importance": {},
    "Locale": {},
    "Message Type": {},
    "Web URL": {},
    "Words": [
      {}
    ]
  }
}
```

#### Send Message by GUID
  
Sends a message using the GUID for the team and channel. This is more performant than send message

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_guid|string|None|True|Channel GUID|None|xxxxx-xxxxx-xxxx-xxxx|
|is_html|boolean|None|True|Is the message HTML|None|True|
|message|string|None|True|Message to send|None|Hello!|
|team_guid|string|None|True|Team GUID|None|xxxxx-xxxxx-xxxx-xxxx|
  
Example input:

```
{
  "channel_guid": "xxxxx-xxxxx-xxxx-xxxx",
  "is_html": true,
  "message": "Hello!",
  "team_guid": "xxxxx-xxxxx-xxxx-xxxx"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|message|False|The message object that was created|None|
  
Example output:

```
{
  "message": {
    "Body": {
      "Content": "",
      "Content Type": {}
    },
    "Created Date Time": {},
    "First Word": {},
    "From": {
      "User": {
        "Display name": {},
        "ID": {}
      }
    },
    "ID": {},
    "Importance": {},
    "Locale": {},
    "Message Type": {},
    "Web URL": {},
    "Words": [
      {}
    ]
  }
}
```
### Triggers


#### New Message Received
  
Poll a channel for new messages

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_name|string|None|True|Channel|None|InsightConnect Channel|
|message_content|string|None|False|Regex to match new messages against|None|[Tt]est|
|team_name|string|None|True|Team name|None|InsightConnect Team|
  
Example input:

```
{
  "channel_name": "InsightConnect Channel",
  "message_content": "[Tt]est",
  "team_name": "InsightConnect Team"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|channel_name|string|False|Name of the channel where the message was posted|example_name|
|indicators|indicators|False|The indicators object that was extracted from message|None|
|message|message|False|The message object that was created|None|
|team_name|string|False|Name of the team to which the channel is assigned to|example_team|
  
Example output:

```
{
  "channel_name": "example_name",
  "indicators": {
    "CVEs": {},
    "Domains": [
      ""
    ],
    "Email Addresses": {},
    "Hashes": {
      "MD5 Hashes": {},
      "SHA1 Hashes": {},
      "SHA256 Hashes": {}
    },
    "IP Addressses": {
      "IPv4 Addressses": {},
      "IPv6 Addressses": {}
    },
    "MAC Addresses": {},
    "URLs": {},
    "UUIDs": {}
  },
  "message": {
    "Body": {
      "Content": "",
      "Content Type": {}
    },
    "Created Date Time": {},
    "First Word": {},
    "From": {
      "User": {
        "Display name": {},
        "ID": {}
      }
    },
    "ID": {},
    "Importance": {},
    "Locale": {},
    "Message Type": {},
    "Web URL": {},
    "Words": [
      {}
    ]
  },
  "team_name": "example_team"
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**team**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|Description|None|
|Display Name|string|None|False|Display name|None|
|ID|string|None|False|ID|None|
  
**hashes**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|MD5 Hashes|[]string|None|False|Extracted MD5 Hashes from message|None|
|SHA1 Hashes|[]string|None|False|Extracted SHA1 hashes from message|None|
|SHA256 Hashes|[]string|None|False|Extracted SHA256 hashes from message|None|
  
**ip_addresses**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IPv4 Addressses|[]string|None|False|Extracted IPv4 addressses from message|None|
|IPv6 Addressses|[]string|None|False|Extracted IPv6 addresses from message|None|
  
**indicators**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CVEs|[]string|None|False|Extracted CVEs from message|None|
|Domains|[]string|None|False|Extracted domains from message|None|
|Email Addresses|[]string|None|False|Extracted email addresses from message|None|
|Hashes|hashes|None|False|Extracted hashes from message|None|
|IP Addressses|ip_addresses|None|False|Extracted IP addresses from message|None|
|MAC Addresses|[]string|None|False|Extracted MAC addresses from message|None|
|URLs|[]string|None|False|Extracted URLs from message|None|
|UUIDs|[]string|None|False|Extracted UUIDs from message|None|
  
**channel**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|Description|None|
|Display Name|string|None|False|Display name|None|
|ID|string|None|False|ID|None|
  
**body**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Content|string|None|False|Content|None|
|Content Type|string|None|False|Content type|None|
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Display name|string|None|False|Display name|None|
|ID|string|None|False|ID|None|
  
**from**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|User|user|None|False|User|None|
  
**message**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Body|body|None|False|Body|None|
|Channel Identity|channelIdentity|None|False|Represents identity of the channel|None|
|Created Date Time|string|None|False|Created date time|None|
|First Word|string|None|False|Extracted first word from message (easy way to obtain a chat command)|None|
|From|from|None|False|From|None|
|ID|string|None|False|ID|None|
|Importance|string|None|False|Importance|None|
|Locale|string|None|False|Locale|None|
|Message Type|string|None|False|Message type|None|
|Web URL|string|None|False|Web URL|None|
|Words|[]string|None|False|The message split by spaces into a list of words. This list makes finding and using parameters in chat commands easier|None|
  
**group**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created Date Time|string|None|False|Created date time|None|
|Description|string|None|False|Description|None|
|Display Name|string|None|False|Display name|None|
|ID|string|None|False|ID|None|
|Mail|string|None|False|Mail|None|
|Mail Enabled|boolean|None|False|Mail enabled|None|
|Mail Nickname|string|None|False|Mail nickname|None|
|Security Enabled|boolean|None|False|Security enabled|None|
  
**itemBody**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Content|string|None|False|The content of the item|None|
|Content Type|string|None|False|The type of the content, possible values are text and HTML|None|
  
**channelIdentity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Channel ID|string|None|False|The identity of the channel in which the message was posted|None|
|Team ID|string|None|False|The identity of the team in which the message was posted|None|
  
**chatMessageReaction**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created Date Time|string|None|False|Created date time|None|
|Reaction Type|string|None|False|Reaction Type|None|
|User|user|None|False|The user who reacted to the message|None|
  
**chatMessage**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attachments|[]object|None|False|References to attached objects|None|
|Body|itemBody|None|False|Representation of the content of the chat message|None|
|Channel Identity|channelIdentity|None|False|Represents identity of the channel|None|
|Chat ID|string|None|False|Represents the identity of the chat|None|
|Created Date Time|string|None|False|Created date time|None|
|Deleted Date Time|string|None|False|Deleted date time|None|
|Etag|string|None|False|Version number of the chat message|None|
|Event Detail|string|None|False|Represents details of an event that happened in a chat|None|
|From|from|None|False|Details of the sender of the chat message|None|
|ID|string|None|False|Unique ID of the message|None|
|Importance|string|None|False|The importance of the chat message|None|
|Last Edited Date Time|string|None|False|Timestamp when edits to the chat message were made|None|
|Last Modified Date Time|string|None|False|Timestamp when the chat message is created (initial setting) or modified|None|
|Locale|string|None|False|Locale of the chat message set by the client|None|
|Mentions|[]object|None|False|List of entities mentioned in the chat message|None|
|Message History|[]object|None|False|List of activity history of a message item|None|
|Message Type|string|None|False|The type of chat message|None|
|Policy Violation|object|None|False|Defines the properties of a policy violation|None|
|Reactions|[]chatMessageReaction|None|False|Reactions for this chat message|None|
|Reply To ID|string|None|False|ID of the parent chat message or root chat message of the thread|None|
|Subject|string|None|False|The subject of the chat message, in plaintext|None|
|Summary|string|None|False|Summary text of the chat message that could be used for push notifications and summary views or fall back views|None|
|Web URL|string|None|False|Link to the message in Microsoft Teams|None|


## Troubleshooting

If there is more than one team with the same name in your organization, the oldest team between the two will be used.

# Version History

* 5.1.0 - New actions: Get Reply List | Improve typing on message
* 5.0.0 - New actions: Get Message in Chat, Get Message in Channel | Update to latest SDK version | Change required fields in message schema
* 4.2.0 - New Message Received: Fixed issue where `font-size` value appeared in the `urls`, and `domains` output fields | Can choose the role of a member when adding them to a channel | Fix bug where case-sensitive URLs were returned in lower case | Improved reliability of domains output value
* 4.1.0 - Cloud enabled | Add Channel to Team: The user has the option to select the type of channel to be created. The available types are `Standard`, and `Private` 
* 4.0.0 - Fix issue with Create Teams Enabled Group action's members, and owners input field types
* 3.2.0 - Send Message Action is updated to support chat messages via chat_id parameter, team_name is set to optional. | Update SDK to latest version.
* 3.1.5 - Add `microsoft_teams` and `office365` keywords | Removed `microsoft, teams, office 365` keywords
* 3.1.4 - Update help.md to include troubleshooting message about team names
* 3.1.3 - Update `docs_url` in plugin spec with a new link to [plugin setup guide](https://docs.rapid7.com/insightconnect/microsoft-teams/)
* 3.1.2 - Fix issue where a name with a bracket could crash the plugin
* 3.1.1 - Correct spelling in help.md
* 3.1.0 - New actions Add Group Owner and Add Member to Channel
* 3.0.1 - Fix import error in New Message Received trigger
* 3.0.0 - Update to make `words` and `first_word` required values in the `message` custom type
* 2.3.1 - Fix issue where the New Message Received trigger could crash on an HTML message
* 2.3.0 - Added `words` to message output type. This allows for easier use of parameters in Teams trigger messages
* 2.2.1 - Automatically extract UUIDs in the New Message Received trigger
* 2.2.0 - Extract and return command security and network indicators in the New Message Received trigger
* 2.1.0 - Update Send Message and Send HTML Message actions to accept `thread_id` input to support threaded replies | Update New Message Received trigger to output team and channel names so they can be passed into subsequent steps
* 2.0.5 - Fix issue where auth token wasn't properly renewed
* 2.0.4 - Fix issue where a message that only had an image in it could break the 'New Message Received' trigger
* 2.0.3 - Add `docs_url` to plugin spec with link to [plugin setup guide](https://insightconnect.help.rapid7.com/docs/microsoft-teams)
* 2.0.2 - Fix issue where unexpected HTML messages would not trigger workflows
* 2.0.1 - Update to Get Teams action to support more than 20 teams
* 2.0.0 - Fix issue where send message would not work if there were too many teams | Removed regex capability for team and channel inputs which will speed up Send Message and Send HTML Message actions
* 1.3.0 - New action Send Message by GUID
* 1.2.3 - New spec and help.md format for the Extension Library
* 1.2.2 - Fix issue where regular expressions would only match at the beginning of a string
* 1.2.1 - Fix issue where New Message Received trigger could receive an unauthorized error after sustained use
* 1.2.0 - New actions Add Member to Team, Remove Member from Team, Create Teams Enabled Group, Delete Team, Add Channel to Team, and Remove Channel from Team
* 1.1.0 - New trigger New Message Received | New action Send HTML Message
* 1.0.1 - Fix issue where improper exception could be raised
* 1.0.0 - Initial plugin

# Links

[MicrosoftTeams in Extension Library](https://extensions.rapid7.com/extension/microsoft-teams)

## References

* [Microsoft Teams](https://products.office.com/en-us/microsoft-teams/group-chat-software)
* [Microsoft Teams API](https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0)
* [Adaptive Cards Actions](https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/cards/cards-actions#adaptive-cards-actions)
* [Python Regular Expression Library (Re)](https://docs.python.org/3.7/library/re.html)