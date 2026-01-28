# Description

[Microsoft Teams](https://products.office.com/en-us/microsoft-teams/group-chat-software) is a unified communications platform. The Microsoft Teams plugin allows you to send and trigger workflows on new messages. The plugin will also allow for teams management with the ability to add and remove teams, channels, and users. This plugin uses the [Microsoft Teams API](https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0) to interact with Microsoft Teams

# Key Features

* Communication Management for all microsoft products

# Requirements

* Username and Password
* Secret Key, similar to API Key

# Supported Product Versions

* Microsoft Graph API v1.0 2024-09-13

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|application_id|string|None|True|Application (client) ID|None|63a0cad6-ac64-435c-a221-5d37c97b763e|None|None|
|application_secret|credential_secret_key|None|True|Application secret|None|aMeCAEYdOLlK+qRcD9AjdyxLkCaqZH1UPm7adjJQ5Og=|None|None|
|directory_id|string|None|True|Directory (tenant) ID|None|9e538ff5-dcb2-46a9-9a28-f93b8250deb0|None|None|
|endpoint|string|None|True|The type of endpoint to connect to: normal service, GCC (government), GCC High (government), DoD (military)|["Normal", "GCC", "GCC High", "DoD"]|Normal|None|None|
|username_password|credential_username_password|None|True|Username and password|None|{ "username": "user", "password": "mypassword" }|None|None|

Example input:

```
{
  "application_id": "63a0cad6-ac64-435c-a221-5d37c97b763e",
  "application_secret": "aMeCAEYdOLlK+qRcD9AjdyxLkCaqZH1UPm7adjJQ5Og=",
  "directory_id": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0",
  "endpoint": "Normal",
  "username_password": {
    "password": "mypassword",
    "username": "user"
  }
}
```

## Technical Details

### Actions


#### Add Channel to Team

This action is used to add a channel to a team

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_description|string|None|True|Channel description|None|This is a test channel.|None|None|
|channel_name|string|None|True|Channel name|None|InsightConnect Channel|None|None|
|channel_type|string|Standard|True|Type of channel to be added|["Standard", "Private"]|Standard|None|None|
|team_name|string|None|True|Team name|None|InsightConnect Team|None|None|
  
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

This action is used to add a user to the group's list of owners

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|group_name|string|None|True|Name of the group or team to which the member is to be added as the owner|None|InsightConnect Team|None|None|
|member_login|string|None|True|The login of the group member to be added as the owner|None|user@example.com|None|None|
  
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

This action is used to add a conversation member to a private channel

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_name|string|None|True|Name of the channel to which the member is to be added|None|InsightConnect Channel|None|None|
|group_name|string|None|True|Name of the group in which the channel is located|None|InsightConnect Team|None|None|
|member_login|string|None|True|The login of the group member to be added to a channel|None|user@example.com|None|None|
|role|string|Member|True|Role of the member to add|["Owner", "Member"]|Owner|None|None|
  
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

This action is used to add a member to a team

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|member_login|string|None|True|Member login e.g. user@example.com|None|user@example.com|None|None|
|team_name|string|None|True|Team name|None|InsightConnect Team|None|None|
  
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

#### Create Teams Chat

This action is used to create a chat in Microsoft Teams

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|members|[]itemMember|None|True|A list of usernames to set as members|None|[{"user_info": "user@example.com", "role": "owner"}, {"user_info": "ab123bcd-123a-412a3-abc1-a123456b789c", "role": "owner"}]|None|None|
|topic|string|None|False|Topic of chat to be added (only available for group chats)|None|example_topic|None|None|
  
Example input:

```
{
  "members": [
    {
      "role": "owner",
      "user_info": "user@example.com"
    },
    {
      "role": "owner",
      "user_info": "ab123bcd-123a-412a3-abc1-a123456b789c"
    }
  ],
  "topic": "example_topic"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|chat|itemChat|False|Information about the chat that was created|{'@odata.context': 'https://graph.microsoft.com/beta/$metadata#chats/$entity', 'chatType': 'group', 'createdDateTime': '2023-11-09T12:07:43.167Z', 'id': '12:a12345bc678d901e12345f67890g1234_thread.v2', 'lastUpdatedDateTime': '2023-11-09T12:07:43.167Z', 'tenantId': '1a234567-bc8d-9e01-23fg-4h567i8j9k01', 'webUrl': 'https://teams.microsoft.com/l/chat/12%3AA12345BC678D901E12345F67890G1234%40thread.v2/0tenantId=1a234567-bc8d-9e01-23fg-4h567i8j9k01'}|
  
Example output:

```
{
  "chat": {
    "@odata.context": "https://graph.microsoft.com/beta/$metadata#chats/$entity",
    "chatType": "group",
    "createdDateTime": "2023-11-09T12:07:43.167Z",
    "id": "12:a12345bc678d901e12345f67890g1234_thread.v2",
    "lastUpdatedDateTime": "2023-11-09T12:07:43.167Z",
    "tenantId": "1a234567-bc8d-9e01-23fg-4h567i8j9k01",
    "webUrl": "https://teams.microsoft.com/l/chat/12%3AA12345BC678D901E12345F67890G1234%40thread.v2/0tenantId=1a234567-bc8d-9e01-23fg-4h567i8j9k01"
  }
}
```

#### Create Teams Enabled Group

This action is used to create a group in Azure and enable it for Microsoft Teams

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|group_description|string|None|True|Group description|None|A test group|None|None|
|group_name|string|None|True|Team name|None|test_group|None|None|
|mail_enabled|boolean|None|True|Should e-mail should be enabled for this group|None|True|None|None|
|mail_nickname|string|None|True|The nickname for the email address of this group in Outlook|None|TestGroup|None|None|
|members|[]string|None|False|A list of usernames to set as members|None|["user@example.com"]|None|None|
|owners|[]string|None|False|A list of usernames to set as owners|None|["user@example.com"]|None|None|
  
Example input:

```
{
  "group_description": "A test group",
  "group_name": "test_group",
  "mail_enabled": true,
  "mail_nickname": "TestGroup",
  "members": [
    "user@example.com"
  ],
  "owners": [
    "user@example.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|group|group|False|Information about the group that was created|{'Created Date Time': '2023-11-09T12:07:43.167Z', 'Description': 'test description', 'Display Name': 'test display name', 'ID': '12:a12345bc678d901e12345f67890g1234_thread.v2', 'Mail': 'General - test display name <user@example.com>', 'Mail Enabled': True, 'Mail Nickname': 'TestNickname', 'Security Enabled': True}|
  
Example output:

```
{
  "group": {
    "Created Date Time": "2023-11-09T12:07:43.167Z",
    "Description": "test description",
    "Display Name": "test display name",
    "ID": "12:a12345bc678d901e12345f67890g1234_thread.v2",
    "Mail": "General - test display name <user@example.com>",
    "Mail Enabled": true,
    "Mail Nickname": "TestNickname",
    "Security Enabled": true
  }
}
```

#### Delete Team

This action is used to delete a team and the associated group from Azure

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|team_name|string|None|True|Team Name|None|Test Team|None|None|
  
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

This action is used to returns all the channels associated with a team

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_name|string|None|False|Optional regex-capable channel to look for|None|InsightConnect Channel|None|None|
|team_name|string|None|True|Team name to look for|None|InsightConnect Team|None|None|
  
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
|channels|[]channel|False|Array of channels|[{"Description": "test description","Display Name": "test display name","ID": "12:a12345bc678d901e12345f67890g1234_thread.v2"}]|
  
Example output:

```
{
  "channels": [
    {
      "Description": "test description",
      "Display Name": "test display name",
      "ID": "12:a12345bc678d901e12345f67890g1234_thread.v2"
    }
  ]
}
```

#### Get Message in Channel

This action is used to retrieve a single message or a message reply in a channel

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_id|string|None|True|The ID of channel|None|11:examplechannel.name|None|None|
|message_id|string|None|True|The ID of message|None|1234567891|None|None|
|reply_id|string|None|False|The ID of reply message|None|1234567890|None|None|
|team_id|string|None|True|The ID of team|None|example-team-id|None|None|
  
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
|message|chatMessage|False|The message object that was created|{'id': '1234567891', 'replyToId': '1234567890', 'etag': '1234567891', 'messageType': 'message', 'createdDateTime': '2023-08-01T12:00:00.000Z', 'lastModifiedDateTime': '2023-08-01T12:00:00.000Z', 'importance': 'normal', 'locale': 'en-us', 'webUrl': 'https://teams.microsoft.com/l/message/11:examplechannel.name/1234567890groupId=example-team-id&tenantId=1&createdTime=1692623381&parentMessageId=1234567891', 'from': {'user': {'id': '3395856c-e81f-2b73-82de-e72602f798b6', 'displayName': 'Example User', 'userIdentityType': 'aadUser', 'tenantId': '9e538ff5-dcb2-46a9-9a28-f93b8250deb0'}}, 'body': {'contentType': 'text', 'content': 'tests_v1'}, 'channelIdentity': {'teamId': '9e538ff5-dcb2-46a9-9a28-f93b8250deb0', 'channelId': '11:examplechannel.name'}, 'attachments': [], 'mentions': [], 'reactions': []}|
  
Example output:

```
{
  "message": {
    "attachments": [],
    "body": {
      "content": "tests_v1",
      "contentType": "text"
    },
    "channelIdentity": {
      "channelId": "11:examplechannel.name",
      "teamId": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0"
    },
    "createdDateTime": "2023-08-01T12:00:00.000Z",
    "etag": "1234567891",
    "from": {
      "user": {
        "displayName": "Example User",
        "id": "3395856c-e81f-2b73-82de-e72602f798b6",
        "tenantId": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0",
        "userIdentityType": "aadUser"
      }
    },
    "id": "1234567891",
    "importance": "normal",
    "lastModifiedDateTime": "2023-08-01T12:00:00.000Z",
    "locale": "en-us",
    "mentions": [],
    "messageType": "message",
    "reactions": [],
    "replyToId": "1234567890",
    "webUrl": "https://teams.microsoft.com/l/message/11:examplechannel.name/1234567890groupId=example-team-id&tenantId=1&createdTime=1692623381&parentMessageId=1234567891"
  }
}
```

#### Get Message in Chat

This action is used to retrieve a single message or a message reply in a chat

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|chat_id|string|None|True|The ID of chat|None|11:examplechat.name|None|None|
|message_id|string|None|True|The ID of message|None|1234567890|None|None|
|username|string|None|True|The ID of user or his email|None|user@example.com|None|None|
  
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
|message|chatMessage|False|The message object that was created|{'message': {'id': '1234567891', 'replyToId': '1234567890', 'etag': '1234567891', 'messageType': 'message', 'createdDateTime': '2023-08-01T12:00:00.000Z', 'lastModifiedDateTime': '2023-08-01T12:00:00.000Z', 'importance': 'normal', 'locale': 'en-us', 'webUrl': 'https://teams.microsoft.com/l/message/11:examplechannel.name/1234567890groupId=example-team-id&tenantId=1&createdTime=1692623381&parentMessageId=1234567891', 'from': {'user': {'id': '3395856c-e81f-2b73-82de-e72602f798b6', 'displayName': 'Example User', 'userIdentityType': 'aadUser', 'tenantId': '9e538ff5-dcb2-46a9-9a28-f93b8250deb0'}}, 'body': {'contentType': 'text', 'content': 'tests_v1'}, 'channelIdentity': {'teamId': '9e538ff5-dcb2-46a9-9a28-f93b8250deb0', 'channelId': '11:examplechannel.name'}, 'attachments': [], 'mentions': [], 'reactions': []}}|
  
Example output:

```
{
  "message": {
    "message": {
      "attachments": [],
      "body": {
        "content": "tests_v1",
        "contentType": "text"
      },
      "channelIdentity": {
        "channelId": "11:examplechannel.name",
        "teamId": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0"
      },
      "createdDateTime": "2023-08-01T12:00:00.000Z",
      "etag": "1234567891",
      "from": {
        "user": {
          "displayName": "Example User",
          "id": "3395856c-e81f-2b73-82de-e72602f798b6",
          "tenantId": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0",
          "userIdentityType": "aadUser"
        }
      },
      "id": "1234567891",
      "importance": "normal",
      "lastModifiedDateTime": "2023-08-01T12:00:00.000Z",
      "locale": "en-us",
      "mentions": [],
      "messageType": "message",
      "reactions": [],
      "replyToId": "1234567890",
      "webUrl": "https://teams.microsoft.com/l/message/11:examplechannel.name/1234567890groupId=example-team-id&tenantId=1&createdTime=1692623381&parentMessageId=1234567891"
    }
  }
}
```

#### Get Reply List

This action is used to list all the replies to a message in a channel of a team

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_name|string|None|True|Channel|None|InsightConnect Channel|None|None|
|message_id|string|None|True|The ID of message|None|1234567891|None|None|
|team_name|string|None|True|Team name|None|InsightConnect Team|None|None|
  
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
|messages|[]chatMessage|False|The message object that was created|[{"attachments": [], "body": {"content": "Test message", "contentType": "text"}, "chatId": "12:a12345bc678d901e12345f67890g1234_thread.v2", "createdDateTime": "2023-11-08T10:38:18.048Z", "etag": "1234567890123", "from": {"user": {"@odata.type": "#microsoft.graph.teamworkUserIdentity", "displayName": "Test User", "id": "8a234567-bc8d-9e01-23fg-4h567i8j9k98", "tenantId": "1a234567-bc8d-9e01-23fg-4h567i8j9k01", "userIdentityType": "aadUser"}}, "id": "1234567890123", "importance": "normal", "lastModifiedDateTime": "2023-11-08T10:38:18.048Z", "locale": "en-us", "mentions": [], "messageType": "message", "reactions": []}]|
  
Example output:

```
{
  "messages": [
    {
      "attachments": [],
      "body": {
        "content": "Test message",
        "contentType": "text"
      },
      "chatId": "12:a12345bc678d901e12345f67890g1234_thread.v2",
      "createdDateTime": "2023-11-08T10:38:18.048Z",
      "etag": "1234567890123",
      "from": {
        "user": {
          "@odata.type": "#microsoft.graph.teamworkUserIdentity",
          "displayName": "Test User",
          "id": "8a234567-bc8d-9e01-23fg-4h567i8j9k98",
          "tenantId": "1a234567-bc8d-9e01-23fg-4h567i8j9k01",
          "userIdentityType": "aadUser"
        }
      },
      "id": "1234567890123",
      "importance": "normal",
      "lastModifiedDateTime": "2023-11-08T10:38:18.048Z",
      "locale": "en-us",
      "mentions": [],
      "messageType": "message",
      "reactions": []
    }
  ]
}
```

#### Get Teams

This action is used to returns all the teams the configured user is allowed to see

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|team_name|string|None|False|Optional regex-capable team name to look for|None|InsightConnect Team|None|None|
  
Example input:

```
{
  "team_name": "InsightConnect Team"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|teams|[]team|False|Array of team objects|[{"Description": "test description","Display Name": "test display name","ID": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0"}]|
  
Example output:

```
{
  "teams": [
    {
      "Description": "test description",
      "Display Name": "test display name",
      "ID": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0"
    }
  ]
}
```

#### List Messages from a Chat

This action is used to retrieve up to the last 50 messages in a chat

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|chat_id|string|None|True|The ID of chat|None|11:examplechat.name|None|None|
  
Example input:

```
{
  "chat_id": "11:examplechat.name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|messages|[]chatMessage|False|The message object that was created|[{"attachments": [], "body": {"content": "Test message", "contentType": "text"}, "chatId": "12:a12345bc678d901e12345f67890g1234_thread.v2", "createdDateTime": "2023-11-08T10:38:18.048Z", "etag": "1234567890123", "from": {"user": {"@odata.type": "#microsoft.graph.teamworkUserIdentity", "displayName": "Test User", "id": "8a234567-bc8d-9e01-23fg-4h567i8j9k98", "tenantId": "1a234567-bc8d-9e01-23fg-4h567i8j9k01", "userIdentityType": "aadUser"}}, "id": "1234567890123", "importance": "normal", "lastModifiedDateTime": "2023-11-08T10:38:18.048Z", "locale": "en-us", "mentions": [], "messageType": "message", "reactions": []}]|
  
Example output:

```
{
  "messages": [
    {
      "attachments": [],
      "body": {
        "content": "Test message",
        "contentType": "text"
      },
      "chatId": "12:a12345bc678d901e12345f67890g1234_thread.v2",
      "createdDateTime": "2023-11-08T10:38:18.048Z",
      "etag": "1234567890123",
      "from": {
        "user": {
          "@odata.type": "#microsoft.graph.teamworkUserIdentity",
          "displayName": "Test User",
          "id": "8a234567-bc8d-9e01-23fg-4h567i8j9k98",
          "tenantId": "1a234567-bc8d-9e01-23fg-4h567i8j9k01",
          "userIdentityType": "aadUser"
        }
      },
      "id": "1234567890123",
      "importance": "normal",
      "lastModifiedDateTime": "2023-11-08T10:38:18.048Z",
      "locale": "en-us",
      "mentions": [],
      "messageType": "message",
      "reactions": []
    }
  ]
}
```

#### Remove Channel from Team

This action is used to remove a channel from a team

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_name|string|None|True|Channel name|None|InsightConnect Channel|None|None|
|team_name|string|None|True|Team name|None|InsightConnect Team|None|None|
  
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

This action is used to remove a member from a team

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|member_login|string|None|True|Member Login e.g. user@example.com|None|user@example.com|None|None|
|team_name|string|None|True|Team name|None|InsightConnect Team|None|None|
  
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

This action is used to send HTML as a message

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_name|string|None|True|Channel name|None|InsightConnect Channel|None|None|
|message_content|string|None|True|HTML content to send|None|<b>Hello!</b>|None|None|
|team_name|string|None|True|Team name|None|InsightConnect Team|None|None|
|thread_id|string|None|False|To post in a thread, select parent message ID|None|1595889908700|None|None|
  
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
|message|message|False|The message object that was created|{'body': {'contentType': 'text', 'content': 'tests_v1'}, 'channelIdentity': {'teamId': '9e538ff5-dcb2-46a9-9a28-f93b8250deb0', 'channelId': '11:examplechannel.name'}, 'First Word': 'test', 'from': {'user': {'id': '3395856c-e81f-2b73-82de-e72602f798b6', 'displayName': 'Example User', 'userIdentityType': 'aadUser', 'tenantId': '9e538ff5-dcb2-46a9-9a28-f93b8250deb0'}}, 'ID': '1234567891', 'messageType': 'message', 'importance': 'normal', 'locale': 'en-us', 'webUrl': 'https://teams.microsoft.com/l/message/11:examplechannel.name/1234567890groupId=example-team-id&tenantId=1&createdTime=1692623381&parentMessageId=1234567891', 'Words': [{}]}|
  
Example output:

```
{
  "message": {
    "First Word": "test",
    "ID": "1234567891",
    "Words": [
      {}
    ],
    "body": {
      "content": "tests_v1",
      "contentType": "text"
    },
    "channelIdentity": {
      "channelId": "11:examplechannel.name",
      "teamId": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0"
    },
    "from": {
      "user": {
        "displayName": "Example User",
        "id": "3395856c-e81f-2b73-82de-e72602f798b6",
        "tenantId": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0",
        "userIdentityType": "aadUser"
      }
    },
    "importance": "normal",
    "locale": "en-us",
    "messageType": "message",
    "webUrl": "https://teams.microsoft.com/l/message/11:examplechannel.name/1234567890groupId=example-team-id&tenantId=1&createdTime=1692623381&parentMessageId=1234567891"
  }
}
```

#### Send Message

This action is used to send a message

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_name|string|None|False|Channel|None|InsightConnect Channel|None|None|
|chat_id|string|None|False|The ID of the chat|None|19:209856c0f3f847a28431deb8eb300807_thread.v2|None|None|
|message|string|None|True|Message to send|None|Hello!|None|None|
|team_name|string|None|False|Team name|None|InsightConnect Team|None|None|
|thread_id|string|None|False|To post in a thread, select parent message ID|None|1595889908700|None|None|
  
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
|message|message|False|The message object that was created|{'body': {'contentType': 'text', 'content': 'tests_v1'}, 'channelIdentity': {'teamId': '9e538ff5-dcb2-46a9-9a28-f93b8250deb0', 'channelId': '11:examplechannel.name'}, 'First Word': 'test', 'from': {'user': {'id': '3395856c-e81f-2b73-82de-e72602f798b6', 'displayName': 'Example User', 'userIdentityType': 'aadUser', 'tenantId': '9e538ff5-dcb2-46a9-9a28-f93b8250deb0'}}, 'ID': '1234567891', 'messageType': 'message', 'importance': 'normal', 'locale': 'en-us', 'webUrl': 'https://teams.microsoft.com/l/message/11:examplechannel.name/1234567890groupId=example-team-id&tenantId=1&createdTime=1692623381&parentMessageId=1234567891', 'Words': [{}]}|
  
Example output:

```
{
  "message": {
    "First Word": "test",
    "ID": "1234567891",
    "Words": [
      {}
    ],
    "body": {
      "content": "tests_v1",
      "contentType": "text"
    },
    "channelIdentity": {
      "channelId": "11:examplechannel.name",
      "teamId": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0"
    },
    "from": {
      "user": {
        "displayName": "Example User",
        "id": "3395856c-e81f-2b73-82de-e72602f798b6",
        "tenantId": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0",
        "userIdentityType": "aadUser"
      }
    },
    "importance": "normal",
    "locale": "en-us",
    "messageType": "message",
    "webUrl": "https://teams.microsoft.com/l/message/11:examplechannel.name/1234567890groupId=example-team-id&tenantId=1&createdTime=1692623381&parentMessageId=1234567891"
  }
}
```

#### Send Message by GUID

This action is used to sends a message using the GUID for the team and channel. This is more performant than send 
message

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_guid|string|None|True|Channel GUID|None|xxxxx-xxxxx-xxxx-xxxx|None|None|
|is_html|boolean|None|True|Is the message HTML|None|True|None|None|
|message|string|None|True|Message to send|None|Hello!|None|None|
|team_guid|string|None|True|Team GUID|None|xxxxx-xxxxx-xxxx-xxxx|None|None|
  
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
|message|message|False|The message object that was created|{'body': {'contentType': 'text', 'content': 'tests_v1'}, 'channelIdentity': {'teamId': '9e538ff5-dcb2-46a9-9a28-f93b8250deb0', 'channelId': '11:examplechannel.name'}, 'First Word': 'test', 'from': {'user': {'id': '3395856c-e81f-2b73-82de-e72602f798b6', 'displayName': 'Example User', 'userIdentityType': 'aadUser', 'tenantId': '9e538ff5-dcb2-46a9-9a28-f93b8250deb0'}}, 'ID': '1234567891', 'messageType': 'message', 'importance': 'normal', 'locale': 'en-us', 'webUrl': 'https://teams.microsoft.com/l/message/11:examplechannel.name/1234567890groupId=example-team-id&tenantId=1&createdTime=1692623381&parentMessageId=1234567891', 'Words': [{}]}|
  
Example output:

```
{
  "message": {
    "First Word": "test",
    "ID": "1234567891",
    "Words": [
      {}
    ],
    "body": {
      "content": "tests_v1",
      "contentType": "text"
    },
    "channelIdentity": {
      "channelId": "11:examplechannel.name",
      "teamId": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0"
    },
    "from": {
      "user": {
        "displayName": "Example User",
        "id": "3395856c-e81f-2b73-82de-e72602f798b6",
        "tenantId": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0",
        "userIdentityType": "aadUser"
      }
    },
    "importance": "normal",
    "locale": "en-us",
    "messageType": "message",
    "webUrl": "https://teams.microsoft.com/l/message/11:examplechannel.name/1234567890groupId=example-team-id&tenantId=1&createdTime=1692623381&parentMessageId=1234567891"
  }
}
```
### Triggers


#### New Message Received

This trigger is used to poll a channel for new messages

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|channel_name|string|None|True|Channel|None|InsightConnect Channel|None|None|
|message_content|string|None|False|Regex to match new messages against|None|[Tt]est|None|None|
|team_name|string|None|True|Team name|None|InsightConnect Team|None|None|
  
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
|indicators|indicators|False|The indicators object that was extracted from message|{'CVEs': ['CVE-2024-1234'], 'Domains': ['test.com'], 'Email Addresses': ['user@example.com'], 'Hashes': {'MD5 Hashes': ['938c2cc0dcc05f2b68c4287040cfcf71'], 'SHA1 Hashes': ['2aae6c35c94fcfb415dbe95f408b9ce91ee846ed'], 'SHA256 Hashes': ['ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad']}, 'IP Addressses': {'IPv4 Addressses': ['1.1.1.1'], 'IPv6 Addressses': ['1111:1111:1111:1111:1111:1111:1111:1111']}, 'MAC Addresses': ['00-00-00-00-00-00'], 'URLs': ['https://www.user@example.com'], 'UUIDs': ['123456789']}|
|message|message|False|The message object that was created|{'body': {'contentType': 'text', 'content': 'tests_v1'}, 'channelIdentity': {'teamId': '9e538ff5-dcb2-46a9-9a28-f93b8250deb0', 'channelId': '11:examplechannel.name'}, 'First Word': 'test', 'from': {'user': {'id': '3395856c-e81f-2b73-82de-e72602f798b6', 'displayName': 'Example User', 'userIdentityType': 'aadUser', 'tenantId': '9e538ff5-dcb2-46a9-9a28-f93b8250deb0'}}, 'ID': '1234567891', 'messageType': 'message', 'importance': 'normal', 'locale': 'en-us', 'webUrl': 'https://teams.microsoft.com/l/message/11:examplechannel.name/1234567890groupId=example-team-id&tenantId=1&createdTime=1692623381&parentMessageId=1234567891', 'Words': [{}]}|
|team_name|string|False|Name of the team to which the channel is assigned to|example_team|
  
Example output:

```
{
  "channel_name": "example_name",
  "indicators": {
    "CVEs": [
      "CVE-2024-1234"
    ],
    "Domains": [
      "test.com"
    ],
    "Email Addresses": [
      "user@example.com"
    ],
    "Hashes": {
      "MD5 Hashes": [
        "938c2cc0dcc05f2b68c4287040cfcf71"
      ],
      "SHA1 Hashes": [
        "2aae6c35c94fcfb415dbe95f408b9ce91ee846ed"
      ],
      "SHA256 Hashes": [
        "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
      ]
    },
    "IP Addressses": {
      "IPv4 Addressses": [
        "1.1.1.1"
      ],
      "IPv6 Addressses": [
        "1111:1111:1111:1111:1111:1111:1111:1111"
      ]
    },
    "MAC Addresses": [
      "00-00-00-00-00-00"
    ],
    "URLs": [
      "https://www.user@example.com"
    ],
    "UUIDs": [
      "123456789"
    ]
  },
  "message": {
    "First Word": "test",
    "ID": "1234567891",
    "Words": [
      {}
    ],
    "body": {
      "content": "tests_v1",
      "contentType": "text"
    },
    "channelIdentity": {
      "channelId": "11:examplechannel.name",
      "teamId": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0"
    },
    "from": {
      "user": {
        "displayName": "Example User",
        "id": "3395856c-e81f-2b73-82de-e72602f798b6",
        "tenantId": "9e538ff5-dcb2-46a9-9a28-f93b8250deb0",
        "userIdentityType": "aadUser"
      }
    },
    "importance": "normal",
    "locale": "en-us",
    "messageType": "message",
    "webUrl": "https://teams.microsoft.com/l/message/11:examplechannel.name/1234567890groupId=example-team-id&tenantId=1&createdTime=1692623381&parentMessageId=1234567891"
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
|Event Detail|object|None|False|Represents details of an event that happened in a chat|None|
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
  
**itemMember**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Role|string|None|True|The role of the user to be added to the chat|None|
|User Info|string|None|True|The ID or Email address|None|
  
**itemChat**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Data Context|string|None|False|The context of the newly created chat|None|
|Chat Type|string|None|False|The type of the newly created chat|None|
|Created Date Time|string|None|False|Created date time|None|
|Chat ID|string|None|False|The ID of the newly created chat|None|
|Last Updated Date Time|string|None|False|Last updated date time|None|
|Tenant ID|string|None|False|The ID the directory that he newly created chat is in|None|
|Web URL|string|None|False|The URL of the newly created chat|None|


## Troubleshooting

* If there is more than one team with the same name in your organization, the oldest team between the two will be used.

# Version History

* 7.0.4 - Updated SDK to the latest version (6.4.2)
* 7.0.3 - Updated SDK to the latest version (6.3.10)
* 7.0.2 - Updated SDK to the latest version (6.3.3)
* 7.0.1 - Updated SDK to the latest version (6.2.5)
* 7.0.0 - Updated SDK to the latest version | Initial updates for fedramp compliance
* 6.0.1 - Using exact match on channel names rather than search, from user input channel names when getting the channel id | using urllib to encode any team names in API calls to avoid symbols not being parsed correctly
* 6.0.0 - New actions - `create_teams_chat` | `list_messages_in_chat` | update type of `Event Detail` to type object
* 5.1.0 - New actions - Get Reply List | Improve typing on message
* 5.0.0 - New actions - Get Message in Chat, Get Message in Channel | Update to latest SDK version | Change required fields in message schema
* 4.2.0 - New Message Received - Fixed issue where `font-size` value appeared in the `urls`, and `domains` output fields | Can choose the role of a member when adding them to a channel | Fix bug where case-sensitive URLs were returned in lower case | Improved reliability of domains output value
* 4.1.0 - Cloud enabled | Add Channel to Team The user has the option to select the type of channel to be created. The available types are `Standard`, and `Private`
* 4.0.0 - Fix issue with Create Teams Enabled Group actions members, and owners input field types
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
* 2.0.5 - Fix issue where auth token was not properly renewed
* 2.0.4 - Fix issue where a message that only had an image in it could break the "New Message Received" trigger
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

* [MicrosoftTeams in Extension Library](https://extensions.rapid7.com/extension/microsoft-teams)

## References

* [Microsoft Teams](https://products.office.com/en-us/microsoft-teams/group-chat-software)
* [Microsoft Teams API](https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0)
* [Adaptive Cards Actions](https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/cards/cards-actions#adaptive-cards-actions)
* [Python Regular Expression Library (Re)](https://docs.python.org/3.7/library/re.html)