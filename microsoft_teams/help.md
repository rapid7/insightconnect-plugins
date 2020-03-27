# Description

[Microsoft Teams](https://products.office.com/en-us/microsoft-teams/group-chat-software) is a unified communications platform that combines persistent workplace chat, video meetings, file storage, and application integration. The Microsoft Teams plugin allows you to send and trigger workflows on new messages. The plugin will also allow for teams management with the ability to add and remove teams, channels, and users.

This plugin uses the [Microsoft Teams API](https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0) to interact with Microsoft Teams.

# Key Features

* Communication Management for all microsoft products

# Requirements

* Username and Password
* Secret Key, similar to API Key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|application_id|string|None|True|Application (client) ID|None|
|application_secret|credential_secret_key|None|True|Application secret|None|
|directory_id|string|None|True|Directory (tenant) ID|None|
|username_password|credential_username_password|None|True|Username and password|None|

## Technical Details

### Actions

#### Send Message

This action is used to send a message.

Regular expressions used by this action are Python specific.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|channel_name|string|None|True|Channel|None|
|message|string|None|True|Message to send|None|
|team_name|string|None|True|Team name|None|

##### Output

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

#### Send HTML Message

This action is used to send HTML as a message.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|channel_name|string|None|True|Channel name|None|
|message_content|string|None|True|HTML content to send|None|
|team_name|string|None|True|Team name|None|

##### Output

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

#### Send Message by GUID

This action sends a message using the GUID for the team and channel. This is more performant than send message.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|channel_guid|string|None|True|Channel GUID|None|
|is_html|boolean|None|True|Is the message HTML|None|
|message|string|None|True|Message to send|None|
|team_guid|string|None|True|Team GUID|None|

##### Output

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
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

#### Get Teams

This action returns all the teams the configured user is allowed to see.

This will only return Teams-provisioned teams.

Regular expressions used by this action are Python specific.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|team_name|string|None|False|Optional regex-capable team name to look for|None|

##### Output

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
      "mail": "user@example.com",
      "mailEnabled": true,
      "mailNickname": "Test Nickname",
      "membershipTypes": [],
      "proxyAddresses": [
        "SPO:xxxxxx",
        "SMTP:user@example.com"
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

#### Get Channels for Team

This action returns all the channels associated with a team.

Regular expressions used by this action are Python specific.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|channel_name|string|None|False|Optional regex-capable channel to look for|None|
|team_name|string|None|True|Team name to look for|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|channels|[]channel|False|Array of channels|

Example output:

```
{
  "channels": [
    {
      "id": "XXXXXXXXXXX",
      "displayName": "test123",
      "description": "komand rocks!",
      "webUrl": "https://teams.microsoft.com/l/channel/19%3a0a48f53ea9484091aba13271dc418c2a%40thread.skype/test123?groupId=d2cc6aa2-8071-44d9-a97a-0a758da420a8&tenantId=5c824599-dc8c-4d31-96fb-3b886d4f8f10",
      "membershipType": "standard"
    }
  ]
}
```

#### Add Member to Team

This action is used to add a member to a team.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|member_login|string|None|True|Member login e.g. user@example.com|None|
|team_name|string|None|True|Team name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Boolean indicating if this action was successful|

Example output:

```
{
  "success": true
}
```

#### Add Channel to Team

This action is used to add a channel to a team.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|channel_description|string|None|True|Channel description|None|
|channel_name|string|None|True|Channel name|None|
|team_name|string|None|True|Team name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Boolean indicating if this action was successful|

Example output:

```
{
  "success": true
}
```

#### Remove Channel from Team

This action is used to remove a channel from a team.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|channel_name|string|None|True|Channel name|None|
|team_name|string|None|True|Team name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Boolean indicating if this action was successful|

Example output:

```
{
  "success": true
}
```

#### Remove Member from Team

This action is used to remove a member from a team.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|member_login|string|None|True|Member Login e.g. user@example.com|None|
|team_name|string|None|True|Team name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Boolean indicating if this action was successful|

Example output:

```
{
  "success": true
}
```

#### Create Teams Enabled Group

This action is used to create a group in Azure and enable it for Microsoft Teams.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|group_description|string|None|True|Group description|None|
|group_name|string|None|True|Team name|None|
|mail_enabled|boolean|None|True|Should e-mail should be enabled for this group|None|
|mail_nickname|string|None|True|The nickname for the email address of this group in Outlook|None|
|members|string[]|None|False|A list of usernames to set as members|None|
|owners|string[]|None|False|A list of usernames to set as owners|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|group|group|False|Information about the group that was created|

Example output:

```
{
  "group": {
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#groups/$entity",
    "id": "xxxxx-xxxx-xxx-xxxxx",
    "createdDateTime": "2019-11-05T19:34:21Z",
    "creationOptions": [],
    "description": "Superheros",
    "displayName": "Avengers",
    "groupTypes": [
      "Unified"
    ],
    "mail": "user@example.com",
    "mailEnabled": true,
    "mailNickname": "CMDTestDeleteMe",
    "proxyAddresses": [
      "SMTP:XXXXXXXXX"
    ],
    "renewedDateTime": "2019-11-05T19:34:21Z",
    "resourceBehaviorOptions": [],
    "resourceProvisioningOptions": [],
    "securityEnabled": false,
    "securityIdentifier": "xxxx-xxxx-xxxx-xxxx",
    "visibility": "Public",
    "onPremisesProvisioningErrors": []
  }
}
```

#### Delete Team

This action is used to delete a team and the associated group from Azure.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|team_name|string|None|True|Team Name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Boolean indicating if this action was successful|

Example output:

```
{
  "success": true
}
```

### Triggers

#### New Message Received

This trigger is used to poll a channel for new messages.

Regular expressions used by this trigger are Python specific.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|channel_name|string|None|True|Channel|None|
|message_content|string|None|False|Regex to match new messages against|None|
|team_name|string|None|True|Team name|None|

##### Output

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

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.0 - Fix issue where send message would not work if there were too many teams | Removed regex capability for team and channel inputs which will speed up Send Message and Send HTML Message actions
* 1.3.0 - New action Send Message by GUID
* 1.2.3 - New spec and help.md format for the Hub
* 1.2.2 - Fix issue where regular expressions would only match at the beginning of a string
* 1.2.1 - Fix issue where New Message Received trigger could receive an unauthorized error after sustained use
* 1.2.0 - New actions Add Member to Team, Remove Member from Team, Create Teams Enabled Group, Delete Team, Add Channel to Team, and Remove Channel from Team
* 1.1.0 - New trigger New Message Received | New action Send HTML Message
* 1.0.1 - Fix issue where improper exception could be raised
* 1.0.0 - Initial plugin

# Links

## References

* [Microsoft Teams](https://products.office.com/en-us/microsoft-teams/group-chat-software)
* [Microsoft Teams API](https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0)
* [Adaptive Cards Actions](https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/cards/cards-actions#adaptive-cards-actions)
* [Python Regular Expression Library (Re)](https://docs.python.org/3.7/library/re.html)
