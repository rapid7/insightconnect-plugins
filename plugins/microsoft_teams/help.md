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
|----|----|-------|--------|-----------|----|-------|
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
    "username": "user",
    "password": "mypassword"
  }
}
```

## Technical Details

### Actions

#### Add Member to Channel

This action is used to add a conversation member to a channel. This operation is only supported on channels with a channelMembershipType of private. Calls with any other channelMembershipType will return a 400 Bad Request response.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|channel_name|string|None|True|Name of the channel to which the member is to be added|None|InsightConnect Channel|
|group_name|string|None|True|Name of the group in which the channel is located|None|InsightConnect Team|
|member_login|string|None|True|The login of the group member to be added to a channel|None|user@example.com|

Example input:

```
{
  "channel_name": "InsightConnect Channel",
  "group_name": "InsightConnect Team",
  "member_login": "user@example.com"
}
```

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

#### Add Group Owner

This action is used to add a user to a group's list of owners. The owners are a set of non-admin users who are allowed to modify the group object.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Boolean indicating if this action was successful|

Example output:

```
{
  "success": true
}
```

#### Send Message

This action is used to send a message.

Regular expressions used by this action are Python specific.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|channel_name|string|None|False|Channel|None|InsightConnect Channel|
|chat_id|string|None|False|The ID of the chat|None|19:209856c0f3f847a28431deb8eb300807@thread.v2|
|message|string|None|True|Message to send|None|Hello!|
|team_name|string|None|False|Team name|None|InsightConnect Team|
|thread_id|string|None|False|To post in a thread, select parent message ID|None|1595889908700|

Example input:

```
{
  "channel_name": "InsightConnect Channel",
  "chat_id": "19:209856c0f3f847a28431deb8eb300807@thread.v2",
  "message": "Hello!",
  "team_name": "InsightConnect Team",
  "thread_id": 1595889908700
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|channel_guid|string|None|True|Channel GUID|None|xxxxx-xxxxx-xxxx-xxxx|
|is_html|boolean|None|True|Is the message HTML|None|True|
|message|string|None|True|Message to send|None|Hello!|
|team_guid|string|None|True|Team GUID|None|xxxxx-xxxxx-xxxx-xxxx|

Example input:

```
{
  "channel_name": "InsightConnect Channel",
  "message": "Hello!",
  "team_name": "InsightConnect Team",
  "thread_id": 1595889908700
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|message|False|The message object that was created|

Example input:

```
{
  "channel_guid": "xxxxx-xxxxx-xxxx-xxxx",
  "is_html": false,
  "message": "Hello!",
  "team_guid": "xxxxx-xxxxx-xxxx-xxxx"
}
```

##### Output

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|message|message|False|The message object that was created|None|

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|team_name|string|None|False|Optional regex-capable team name to look for|None|InsightConnect Team|

Example input:

```
{
  "team_name": "InsightConnect Team"
}
```

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
      "displayName": "InsightConnect Team",
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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|channel_description|string|None|True|Channel description|None|This is a test channel.|
|channel_name|string|None|True|Channel name|None|InsightConnect Channel|
|team_name|string|None|True|Team name|None|InsightConnect Team|

Example input:

```
{
  "channel_description": "This is a test channel.",
  "channel_name": "InsightConnect Channel",
  "team_name": "InsightConnect Team"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|group_description|string|None|True|Group description|None|A test group|
|group_name|string|None|True|Team name|None|test_group|
|mail_enabled|boolean|None|True|Should e-mail should be enabled for this group|None|True|
|mail_nickname|string|None|True|The nickname for the email address of this group in Outlook|None|TestGroup|
|members|string[]|None|False|A list of usernames to set as members|None|["user@example.com"]|
|owners|string[]|None|False|A list of usernames to set as owners|None|["user@example.com"]|

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|team_name|string|None|True|Team Name|None|Test Team|

Example input:

```
{
  "team_name": "Test Team"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|channel_name|string|False|Name of the channel where the message was posted|
|indicators|indicators|False|The indicators object that was extracted from message|
|message|message|False|The message object that was created|
|team_name|string|False|Name of the team to which the channel is assigned to|

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
      "content": "extract-indicators www.rapid7.com user@example.com ..."
    },
    "attachments": [],
    "mentions": [],
    "reactions": [],
    "first_word": "extract-indicators"
  },
  "indicators": {
    "domains": [
      "www.rapid7.com"
    ],
    "urls": [
      "https://www.rapid7.com"
    ],
    "email_addresses": [
      "user@example.com"
    ],
    "hashes": {
      "md5_hashes": [
        "7cafac7ec5adaebf62257a4cf5aa63cb"
      ],
      "sha1_hashes": [
        "df5f8044e02c1e72967dd6eed70aeab2bab234c5"
      ],
      "sha256_hashes": [
        "711712cd0038f268a768fed960dacf57b6515d4ad3d1db2dfbca0be9680ed7d9"
      ]
    },
    "ip_addresses": {
      "ipv4_addresses": [
        "198.51.100.1"
      ],
      "ipv6_addresses": [
        "2001:db8:8:4::2"
      ]
    },
    "mac_addresses": [
      "00:00:0A:BB:28:FC"
    ],
    "cves": [
      "CVE-2015-3429"
    ],
    "uuids": [
      "0123d45a-a412-d124-d124-cb124856a94d"
    ]
  }
}
```

### Custom Output Types

#### body

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Content|string|False|Content|
|Content Type|string|False|Content type|

#### channel

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Description|string|False|Description|
|Display Name|string|False|Display name|
|ID|string|False|ID|

#### from

|Name|Type|Required|Description|
|----|----|--------|-----------|
|User|user|False|User|

#### group

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created Date Time|string|False|Created date time|
|Description|string|False|Description|
|Display Name|string|False|Display name|
|ID|string|False|ID|
|Mail|string|False|Mail|
|Mail Enabled|boolean|False|Mail enabled|
|Mail Nickname|string|False|Mail nickname|
|Security Enabled|boolean|False|Security enabled|

#### hashes

|Name|Type|Required|Description|
|----|----|--------|-----------|
|MD5 Hashes|[]string|False|Extracted MD5 Hashes from message|
|SHA1 Hashes|[]string|False|Extracted SHA1 hashes from message|
|SHA256 Hashes|[]string|False|Extracted SHA256 hashes from message|

#### indicators

|Name|Type|Required|Description|
|----|----|--------|-----------|
|CVEs|[]string|False|Extracted CVEs from message|
|Domains|[]string|False|Extracted domains from message|
|Email Addresses|[]string|False|Extracted email addresses from message|
|Hashes|hashes|False|Extracted hashes from message|
|IP Addresses|ip_addresses|False|Extracted IP addresses from message|
|MAC Addresses|[]string|False|Extracted MAC addresses from message|
|URLs|[]string|False|Extracted URLs from message|
|UUIDs|[]string|False|Extracted UUIDs from message|

#### ip_addresses

|Name|Type|Required|Description|
|----|----|--------|-----------|
|IPv4 Addresses|[]string|False|Extracted IPv4 addresses from message|
|IPv6 Addresses|[]string|False|Extracted IPv6 addresses from message|

#### message

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Body|body|False|Body|
|Created Date Time|string|False|Created date time|
|First Word|string|True|Extracted first word from message (easy way to obtain a chat command)|
|From|from|False|From|
|ID|string|False|ID|
|Importance|string|False|Importance|
|Locale|string|False|Locale|
|Message Type|string|False|Message type|
|Web URL|string|False|Web URL|
|Words|[]string|True|The message split by spaces into a list of words. This list makes finding and using parameters in chat commands easier|

#### team

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Description|string|False|Description|
|Display Name|string|False|Display name|
|ID|string|False|ID|

#### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Display name|string|False|Display name|
|ID|string|False|ID|

## Troubleshooting

If there is more than one team with the same name in your organization, the oldest team between the two will be used.

# Version History

* 3.2.0 - Support sending chat messages in Send Message action
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

## References

* [Microsoft Teams](https://products.office.com/en-us/microsoft-teams/group-chat-software)
* [Microsoft Teams API](https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview?view=graph-rest-1.0)
* [Adaptive Cards Actions](https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/cards/cards-actions#adaptive-cards-actions)
* [Python Regular Expression Library (Re)](https://docs.python.org/3.7/library/re.html)
