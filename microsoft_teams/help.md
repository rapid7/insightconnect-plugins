# Microsoft Teams

## About

[Microsoft Teams](https://products.office.com/en-us/microsoft-teams/group-chat-software) is a unified communications platform that combines persistent workplace chat, video meetings, file storage, and application integration.

This plugin uses the [Microsoft Teams API](https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0) to interact with Microsoft Teams.

## Actions

### Send Message

This action is used to send a message.

Regular expressions used by this action are Python specific.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|channel_name|string|None|True|Regex-capable channel|None|
|message|string|None|True|Message to send|None|
|team_name|string|None|True|Regex-capable team name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|message|False|The message object that was created|

Example output:

```
{
  "message": {
    "@odata.context": "https://graph.microsoft.com/beta/$metadata#teams('xxxx')/channels('xxxxxxx')/messages/$entity",
    "id": "1571769574238",
    "etag": "1571769574238",
    "messageType": "message",
    "createdDateTime": "2019-10-22T18:39:34.238Z",
    "importance": "normal",
    "locale": "en-us",
    "webUrl": "https://teams.microsoft.com/l/message/xxxxxxxxxxxxxx/xxxxxx?groupId=xxxxx",
    "from": {
      "user": {
        "id": "xxxxxxx",
        "displayName": "Test User",
        "userIdentityType": "aadUser"
      }
    },
    "body": {
      "contentType": "text",
      "content": "Hello from InsightConnect!"
    },
    "attachments": [],
    "mentions": [],
    "reactions": []
  }
}
```

### Send HTML Message

This action is used to send HTML as a message.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|channel_name|string|None|True|Regex-capable channel|None|
|message_content|string|None|True|HTML content to send|None|
|team_name|string|None|True|Regex-capable team name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|message|False|The message object that was created|

Example output:

```
{
  "message": {
    "@odata.context": "https://graph.microsoft.com/beta/$metadata#teams('xxxx')/channels('xxxxxxx')/messages/$entity",
    "id": "1571769574238",
    "etag": "1571769574238",
    "messageType": "message",
    "createdDateTime": "2019-10-22T18:39:34.238Z",
    "importance": "normal",
    "locale": "en-us",
    "webUrl": "https://teams.microsoft.com/l/message/xxxxxxxxxxxxxx/xxxxxx?groupId=xxxxx",
    "from": {
      "user": {
        "id": "xxxxxxx",
        "displayName": "Test User",
        "userIdentityType": "aadUser"
      }
    },
    "body": {
      "contentType": "text",
      "content": "Hello from InsightConnect!"
    },
    "attachments": [],
    "mentions": [],
    "reactions": []
  }
}
```

### Get Teams

This action returns all the teams the configured user is allowed to see.

This will only return Teams-provisioned teams.

Regular expressions used by this action are Python specific.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|team_name|string|None|False|Optional regex-capable optional team name to look for|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|teams|[]team|False|Array of team objects|

Example output:

```
{
  "teams": [
    {
      "id": "7af08a76-01fe-4a1d-bfa1-84d2b5509cdd",
      "createdDateTime": "2019-10-14T17:18:55Z",
      "description": "A test team of everyone",
      "displayName": "ICON-Test-Everyone",
      "externalGroupIds": [],
      "groupTypes": [
        "Unified"
      ],
      "mail": "xxxxx@xxxxx.xxxx",
      "mailEnabled": true,
      "mailNickname": "Test Nickname",
      "membershipTypes": [],
      "proxyAddresses": [
        "SPO:xxxxxx",
        "SMTP:xxxx@xxxxx.xxx"
      ],
      "renewedDateTime": "2019-10-14T17:18:55Z",
      "resourceBehaviorOptions": [
        "HideGroupInOutlook",
        "SubscribeMembersToCalendarEventsDisabled",
        "WelcomeEmailDisabled"
      ],
      "resourceProvisioningOptions": [
        "Team"
      ],
      "securityEnabled": false,
      "securityIdentifier": "S-1-12-1-2062584438-1243415038-3531907519-3718009013",
      "visibility": "Public",
      "onPremisesProvisioningErrors": []
    }
  ]
}
```

### Get Channels for Team

This action returns all the channels associated with a team.

Regular expressions used by this action are Python specific.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|channel_name|string|None|False|Optional regex-capable optional channel to look for|None|
|team_name|string|None|True|Regex-capable team name to look for|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|channels|[]channel|False|Array of channels|

Example output:

```
{
  "channels": [
    {
      "id": "19:0a48f53ea9484091aba13271dc418c2a@thread.skype",
      "displayName": "test123",
      "description": "komand rocks!",
      "webUrl": "https://teams.microsoft.com/l/channel/19%3a0a48f53ea9484091aba13271dc418c2a%40thread.skype/test123?groupId=d2cc6aa2-8071-44d9-a97a-0a758da420a8&tenantId=5c824599-dc8c-4d31-96fb-3b886d4f8f10",
      "membershipType": "standard"
    }
  ]
}
```

## Triggers

### New Message Received

This trigger is used to poll a channel for new messages.

Regular expressions used by this trigger are Python specific.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|channel_name|string|None|True|Regex-capable channel|None|
|message_content|string|None|False|Regex to match new messages against|None|
|team_name|string|None|True|Regex-capable team name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|message|False|The message object that was created|

Example output:

```
{
  "message": {
    "@odata.context": "https://graph.microsoft.com/beta/$metadata#teams('xxxx')/channels('xxxxxxx')/messages/$entity",
    "id": "1571769574238",
    "etag": "1571769574238",
    "messageType": "message",
    "createdDateTime": "2019-10-22T18:39:34.238Z",
    "importance": "normal",
    "locale": "en-us",
    "webUrl": "https://teams.microsoft.com/l/message/xxxxxxxxxxxxxx/xxxxxx?groupId=xxxxx",
    "from": {
      "user": {
        "id": "xxxxxxx",
        "displayName": "Test User",
        "userIdentityType": "aadUser"
      }
    },
    "body": {
      "contentType": "text",
      "content": "Hello from InsightConnect!"
    },
    "attachments": [],
    "mentions": [],
    "reactions": []
  }
}
```

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|application_id|string|None|True|Application (client) ID|None|
|application_secret|credential_secret_key|None|True|Application secret|None|
|directory_id|string|None|True|Directory (tenant) ID|None|
|username_password|credential_username_password|None|True|Username and password|None|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

## Workflows

Examples:

* Send message to Microsoft Teams

## Versions

* 1.0.0 - Initial plugin
* 1.0.1 - Fix issue where improper exception could be raised
* 1.1.0 - New trigger New Message Received | New action Send HTML Message 

## References

* [Microsoft Teams](https://products.office.com/en-us/microsoft-teams/group-chat-software)
* [Microsoft Teams API](https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0)
* [Adaptive Cards Actions](https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/cards/cards-actions#adaptive-cards-actions)
* [Python Regular Expression Library (Re)](https://docs.python.org/3.7/library/re.html)

## Custom Output Types

### team

|Name|Type|Required|Description|
|----|----|--------|-----------|
|description|string|False|Description|
|displayName|string|False|Display name|
|id|string|False|ID|

### channel

|Name|Type|Required|Description|
|----|----|--------|-----------|
|description|string|False|Description|
|displayName|string|False|Display name|
|id|string|False|ID|

### body

|Name|Type|Required|Description|
|----|----|--------|-----------|
|content|string|False|Content|
|contentType|string|False|Content Type|

### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|displayName|string|False|Display name|
|id|string|False|ID|

### from

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|user|False|User|

### message

|Name|Type|Required|Description|
|----|----|--------|-----------|
|body|body|False|Body|
|createdDateTime|string|False|Created date time|
|from|from|False|From|
|id|string|False|ID|
|importance|string|False|Importance|
|locale|string|False|Locale|
|messageType|string|False|Message type|
|webUrl|string|False|Web URL|
