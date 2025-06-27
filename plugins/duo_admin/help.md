# Description

[Duo](https://duo.com/)'s Trusted Access platform verifies the identity of your users with two-factor authentication and security health of their devices before they connect to the apps they use. Using the Duo plugin for InsightConnect will allow Duo user management within automation workflows

# Key Features

* Add user
* Delete user
* Enroll user
* Get logs
* Get phones by user ID
* Get user by ID
* Get user by username
* Get user status
* Get users
* Modify user

# Requirements

* Two secret keys - `integration key` and `secret key`
* `API hostname`

# Supported Product Versions

* Duo Admin API 2024-09-17

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|hostname|string|None|True|Duo API hostname|None|api-XXXXXXXX.duosecurity.com|None|None|
|integrationKey|credential_secret_key|None|True|API integration key|None|DUCUULF6HBMZ43IG9MBH|None|None|
|secretKey|credential_secret_key|None|True|API secret key|None|3rlCtQGBVpoCXkjP3pLslVWxO8b4W5j1|None|None|

Example input:

```
{
  "hostname": "api-XXXXXXXX.duosecurity.com",
  "integrationKey": "DUCUULF6HBMZ43IG9MBH",
  "secretKey": "3rlCtQGBVpoCXkjP3pLslVWxO8b4W5j1"
}
```

## Technical Details

### Actions


#### Add User

This action is used to add a user in Duo Admin

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|aliases|[]string|None|False|User aliases. May have up to 4 unique amongst users|None|["test-alias"]|None|None|
|email|string|None|False|Email of the user|None|user@example.com|None|None|
|notes|string|None|False|An optional description or notes field|None|Example note|None|None|
|realname|string|None|False|User's real name|None|Example User|None|None|
|status|string|active|False|User status|["active", "bypass", "disabled"]|active|None|None|
|username|string|None|True|The name of the user to create|None|example-user|None|None|
  
Example input:

```
{
  "aliases": [
    "test-alias"
  ],
  "email": "user@example.com",
  "notes": "Example note",
  "realname": "Example User",
  "status": "active",
  "username": "example-user"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|user|False|User|{'aliases': ['test-alias'], 'created': 1538529180, 'email': 'user@example.com', 'notes': 'Example note', 'realname': 'Example User', 'status': 'active', 'userId': 'DUVSXMGU7NLM8H803W9L', 'username': 'example-user'}|
  
Example output:

```
{
  "user": {
    "aliases": [
      "test-alias"
    ],
    "created": 1538529180,
    "email": "user@example.com",
    "notes": "Example note",
    "realname": "Example User",
    "status": "active",
    "userId": "DUVSXMGU7NLM8H803W9L",
    "username": "example-user"
  }
}
```

#### Delete User by ID

This action is used to delete a user by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|userId|string|None|True|User ID to remove|None|DUCUULF6HBMZ43IG9MBH|None|None|
  
Example input:

```
{
  "userId": "DUCUULF6HBMZ43IG9MBH"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Whether the action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Enroll User

This action is used to enrolls a user and sends an enrollment email to the specified email address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|email|string|None|True|Email address to send enrollment email to|None|user@example.com|None|None|
|timeToExpiration|number|0|False|Amount of time in seconds until enrollment email expires. Use '0' for no expiration|None|3600|None|None|
|username|string|None|True|Username for user to enroll|None|test-username|None|None|
  
Example input:

```
{
  "email": "user@example.com",
  "timeToExpiration": 0,
  "username": "test-username"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Whether or not the enrollment was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Get Authentication Logs
  
This action is used to get auth logs, limited to past 180 days.
[Currentmillis.com](https://currentmillis.com/) is 
useful for finding a usable UNIX timestamp.

Available inputs for parameters can be found in [Duo Admin API 
docs](https://duo.com/docs/adminapi#logs:~:text=The%20factor%20or%20method%20used%20for%20an%20authentication%20attempt.%20One%20of%3A)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|applications|[]string|None|False|List of application IDs to filter on|None|["DIV9C5V7T6L02DRWL4RU"]|None|None|
|eventTypes|[]string|None|False|List of event types(authentication, enrollment) to filter on, to include all leave this parameter empty|None|["authentication"]|None|None|
|factors|[]string|None|False|List of factors or methods used for an authentication attempt to filter on, to include all leave this parameter empty. Check the help documentation to see all available inputs|None|["duo_push", "sms_passcode"]|None|None|
|groups|[]string|None|False|List of group IDs to filter on|None|["DG67EON0I1QA2ZDUF32M"]|None|None|
|maxtime|integer|None|False|Maximum time in UNIX timestamp milliseconds. Must be 13 or more digits in length and greater than mintime. To use current time leave this parameter empty|None|1611069760000|None|None|
|mintime|integer|None|True|Minimum time in UNIX timestamp milliseconds. Must be 13 or more digits in length|None|1609377288936|None|None|
|phoneNumbers|[]string|None|False|List of phone numbers to filter on|None|["+11111111111"]|None|None|
|reasons|[]string|None|False|List of reasons associated with an authentication attempt to filter on, to include all leave this parameter empty. Check the help documentation to see all available inputs|None|["user_disabled"]|None|None|
|results|[]string|None|False|List of results of an authentication attempt(success, denied, fraud) to filter on, to include all leave this parameter empty|None|["denied"]|None|None|
|tokens|[]string|None|False|List of FIDO U2F token registration IDs or WebAuthn security keys to filter on|None|["WA4ED9AUVMSWUF00KES4"]|None|None|
|users|[]string|None|False|List of user IDs to filter on|None|["DUW2DKA44RFYECTU8R1O"]|None|None|
  
Example input:

```
{
  "applications": [
    "DIV9C5V7T6L02DRWL4RU"
  ],
  "eventTypes": [
    "authentication"
  ],
  "factors": [
    "duo_push",
    "sms_passcode"
  ],
  "groups": [
    "DG67EON0I1QA2ZDUF32M"
  ],
  "maxtime": 1611069760000,
  "mintime": 1609377288936,
  "phoneNumbers": [
    "+11111111111"
  ],
  "reasons": [
    "user_disabled"
  ],
  "results": [
    "denied"
  ],
  "tokens": [
    "WA4ED9AUVMSWUF00KES4"
  ],
  "users": [
    "DUW2DKA44RFYECTU8R1O"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|authLogs|[]authLog|True|Logs|[ { "accessDevice": { "browser": "Chrome", "browserVersion": "67.0.3396.99", "flashVersion": "uninstalled", "ip": "198.51.100.1", "isEncryptionEnabled": "true", "isFirewallEnabled": "true", "isPasswordSet": "true", "javaVersion": "uninstalled", "location": { "city": "Bloomington", "country": "United States", "state": "Illinois" }, "os": "Mac OS X", "osVersion": "10.14.1" }, "alias": "test", "application": { "key": "DIV9C5V7T6L02DRWL4RU", "name": "Microsoft Azure Active Directory" }, "authDevice": { "ip": "198.51.100.1", "location": { "city": "Bloomington", "country": "United States", "state": "Illinois" }, "name": "+11111111111" }, "email": "user@example.com", "eventType": "authentication", "factor": "duo_push", "isotimestamp": "2021-01-19T14:47:24.309957+00:00", "reason": "user_disabled", "result": "denied", "timestamp": 1611067644, "txid": "9de5069c-5afe-602b-2ea0-a04b66beb2c0", "user": { "groups": [ "InsightConnect Group" ], "key": "DUW2DKA44RFYECTU8R1O", "name": "user@example.com" } } ]|
  
Example output:

```
{
  "authLogs": [
    {
      "accessDevice": {
        "browser": "Chrome",
        "browserVersion": "67.0.3396.99",
        "flashVersion": "uninstalled",
        "ip": "198.51.100.1",
        "isEncryptionEnabled": "true",
        "isFirewallEnabled": "true",
        "isPasswordSet": "true",
        "javaVersion": "uninstalled",
        "location": {
          "city": "Bloomington",
          "country": "United States",
          "state": "Illinois"
        },
        "os": "Mac OS X",
        "osVersion": "10.14.1"
      },
      "alias": "test",
      "application": {
        "key": "DIV9C5V7T6L02DRWL4RU",
        "name": "Microsoft Azure Active Directory"
      },
      "authDevice": {
        "ip": "198.51.100.1",
        "location": {
          "city": "Bloomington",
          "country": "United States",
          "state": "Illinois"
        },
        "name": "+11111111111"
      },
      "email": "user@example.com",
      "eventType": "authentication",
      "factor": "duo_push",
      "isotimestamp": "2021-01-19T14:47:24.309957+00:00",
      "reason": "user_disabled",
      "result": "denied",
      "timestamp": 1611067644,
      "txid": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "user": {
        "groups": [
          "InsightConnect Group"
        ],
        "key": "DUW2DKA44RFYECTU8R1O",
        "name": "user@example.com"
      }
    }
  ]
}
```

#### Get Phones by User ID

This action is used to gets a list of phones associated with the user ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|userId|string|None|True|The identifier of the user|None|DUCUULF6HBMZ43IG9MBH|None|None|
  
Example input:

```
{
  "userId": "DUCUULF6HBMZ43IG9MBH"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|phoneList|[]phoneUser|False|List of phones associated with the user's ID|[{ "activated": true, "capabilities": [ "auto", "push", "sms", "phone", "mobile_otp" ], "lastSeen": "2019-01-15T23:02:20", "number": "123456789", "phoneId": "DUCUULF6HBMZ43IG9MBH", "platform": "Google Android", "smsPasscodesSent": false, "type": "Mobile" }]|
  
Example output:

```
{
  "phoneList": [
    {
      "activated": true,
      "capabilities": [
        "auto",
        "push",
        "sms",
        "phone",
        "mobile_otp"
      ],
      "lastSeen": "2019-01-15T23:02:20",
      "number": "123456789",
      "phoneId": "DUCUULF6HBMZ43IG9MBH",
      "platform": "Google Android",
      "smsPasscodesSent": false,
      "type": "Mobile"
    }
  ]
}
```

#### Get User by ID

This action is used to get a user by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|userId|string|None|True|User unique ID|None|DUCUULF6HBMZ43IG9MBH|None|None|
  
Example input:

```
{
  "userId": "DUCUULF6HBMZ43IG9MBH"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|user|False|User details|{'created': 1111111111, 'email': 'user@example.com', 'lastLogin': 1511423501, 'phones': [{'activated': True, 'capabilities': ['auto', 'push', 'sms', 'phone', 'mobile_otp'], 'lastSeen': '2018-08-20T06:52:20', 'number': '+11111111111', 'phoneId': '1234ABCDEFG', 'platform': 'Apple iOS', 'smsPasscodesSent': False, 'type': 'Mobile'}], 'realname': 'John Doe', 'status': 'active', 'userId': 'BUUUUUUUUUUUUUUUUUUZ', 'username': 'jdoe'}|
  
Example output:

```
{
  "user": {
    "created": 1111111111,
    "email": "user@example.com",
    "lastLogin": 1511423501,
    "phones": [
      {
        "activated": true,
        "capabilities": [
          "auto",
          "push",
          "sms",
          "phone",
          "mobile_otp"
        ],
        "lastSeen": "2018-08-20T06:52:20",
        "number": "+11111111111",
        "phoneId": "1234ABCDEFG",
        "platform": "Apple iOS",
        "smsPasscodesSent": false,
        "type": "Mobile"
      }
    ],
    "realname": "John Doe",
    "status": "active",
    "userId": "BUUUUUUUUUUUUUUUUUUZ",
    "username": "jdoe"
  }
}
```

#### Get User by Username

This action is used to get a user by username

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|username|string|None|True|Specify a username (or username alias) to look up a single user|None|jdoe|None|None|
  
Example input:

```
{
  "username": "jdoe"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|user|False|User details|{'created': 1462823674, 'email': 'user@example.com', 'lastLogin': 1534446415, 'phones': [{'activated': True, 'capabilities': ['auto', 'push', 'sms', 'phone', 'mobile_otp'], 'lastSeen': '2018-08-21T15:57:34', 'number': '+12222222222', 'phoneId': '11111113RP6666666666', 'platform': 'Google Android', 'smsPasscodesSent': False, 'type': 'Mobile'}], 'status': 'active', 'userId': 'A777777777777777777W', 'username': 'jdoe'}|
  
Example output:

```
{
  "user": {
    "created": 1462823674,
    "email": "user@example.com",
    "lastLogin": 1534446415,
    "phones": [
      {
        "activated": true,
        "capabilities": [
          "auto",
          "push",
          "sms",
          "phone",
          "mobile_otp"
        ],
        "lastSeen": "2018-08-21T15:57:34",
        "number": "+12222222222",
        "phoneId": "11111113RP6666666666",
        "platform": "Google Android",
        "smsPasscodesSent": false,
        "type": "Mobile"
      }
    ],
    "status": "active",
    "userId": "A777777777777777777W",
    "username": "jdoe"
  }
}
```

#### Get User Status

This action is used to get account status of a user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|username|string|None|True|The username or alias for which you want to get the status|None|user|None|None|
  
Example input:

```
{
  "username": "user"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|string|True|Status of the user|active|
|userId|string|True|ID of the user|DU0W79YFWZAJWJV6P00L|
  
Example output:

```
{
  "status": "active",
  "userId": "DU0W79YFWZAJWJV6P00L"
}
```

#### Get Users

This action is used to get list of users

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|users|[]user|False|List of users|[ { "created": 1111111111, "email": "user@example.com", "lastLogin": 1511423501, "phones": [ { "activated": true, "capabilities": [ "auto", "push", "sms", "phone", "mobile_otp" ], "lastSeen": "2018-08-20T06:52:20", "number": "+11111111111", "phoneId": "ABCDEFGHIJ", "platform": "Apple iOS", "smsPasscodesSent": false, "type": "Mobile" } ], "realname": "John Doe", "status": "active", "userId": "BUUUUUUUUUUUUUUUUUUZ", "username": "jdoe" } ]|
  
Example output:

```
{
  "users": [
    {
      "created": 1111111111,
      "email": "user@example.com",
      "lastLogin": 1511423501,
      "phones": [
        {
          "activated": true,
          "capabilities": [
            "auto",
            "push",
            "sms",
            "phone",
            "mobile_otp"
          ],
          "lastSeen": "2018-08-20T06:52:20",
          "number": "+11111111111",
          "phoneId": "ABCDEFGHIJ",
          "platform": "Apple iOS",
          "smsPasscodesSent": false,
          "type": "Mobile"
        }
      ],
      "realname": "John Doe",
      "status": "active",
      "userId": "BUUUUUUUUUUUUUUUUUUZ",
      "username": "jdoe"
    }
  ]
}
```

#### Modify User by ID

This action is used to modify a user by ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alias1|string|None|False|A username alias 1|None|alias1|None|None|
|alias2|string|None|False|A username alias 1|None|alias2|None|None|
|alias3|string|None|False|A username alias 3|None|alias3|None|None|
|alias4|string|None|False|A username alias 4|None|alias3|None|None|
|email|string|None|False|The new email address|None|user@example.com|None|None|
|notes|string|None|False|The new notes field|None|Example|None|None|
|realname|string|None|False|The new realname (or full name)|None|Example|None|None|
|status|string|None|False|The new status. Select 'None' to skip status change|["active", "disabled", "bypass", "None"]|active|None|None|
|userId|string|None|True|User unique ID|None|DUCUULF6HBMZ43IG9MBH|None|None|
|username|string|None|False|The new username|None|Example|None|None|
  
Example input:

```
{
  "alias1": "alias1",
  "alias2": "alias2",
  "alias3": "alias3",
  "alias4": "alias3",
  "email": "user@example.com",
  "notes": "Example",
  "realname": "Example",
  "status": "None",
  "userId": "DUCUULF6HBMZ43IG9MBH",
  "username": "Example"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|user|False|User details|{'alias1': 'alias1', 'alias2': 'alias2', 'alias3': 'alias3', 'alias4': 'alias4', 'aliases': {'alias1': 'alias1', 'alias2': 'alias2', 'alias3': 'alias3', 'alias4': 'alias4'}, 'created': 1684765611, 'email': 'user@example.com', 'isEnrolled': False, 'notes': 'Example', 'realname': 'Example', 'status': 'active', 'userId': 'DUCUULF6HBMZ43IG9MBH', 'username': 'Example'}|
  
Example output:

```
{
  "user": {
    "alias1": "alias1",
    "alias2": "alias2",
    "alias3": "alias3",
    "alias4": "alias4",
    "aliases": {
      "alias1": "alias1",
      "alias2": "alias2",
      "alias3": "alias3",
      "alias4": "alias4"
    },
    "created": 1684765611,
    "email": "user@example.com",
    "isEnrolled": false,
    "notes": "Example",
    "realname": "Example",
    "status": "active",
    "userId": "DUCUULF6HBMZ43IG9MBH",
    "username": "Example"
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks


#### Monitor Logs

This task is used to monitor administrator, authentication and trust monitor event logs

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|collectAdminLogs|boolean|True|False|Whether to collect Admin logs (note requires appropriate level of Duo Admin license)|None|False|None|None|
|collectTrustMonitorEvents|boolean|True|False|Whether to collect Trust Monitor events (note requires appropriate level of Duo Admin license)|None|False|None|None|
  
Example input:

```
{
  "collectAdminLogs": true,
  "collectTrustMonitorEvents": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|logs|[]object|True|List of administrator, authentication and trust monitor event logs within the specified time range|[ { "accessDevice": { "browser": "Chrome", "browserVersion": "113.0.0.0", "ip": "198.51.100.1", "isEncryptionEnabled": "unknown", "isFirewallEnabled": "unknown", "isPasswordSet": "unknown", "location": { "city": "Los Angeles", "country": "United States", "state": "California" }, "os": "Mac OS X", "osVersion": "10.15.7" }, "alias": "unknown", "application": { "key": "DI8CODQSMK4BXPLYS47K", "name": "User Portal" }, "authDevice": { "key": "DPAVQAJMU3BW0LV7OCX3", "name": "Generic Smartphone" }, "eventType": "enrollment", "factor": "not_available", "isotimestamp": "2023-05-29T10:07:38.631165+00:00", "result": "success", "timestamp": 1685354858, "trustedEndpointStatus": "unknown", "txid": "9de5069c-5afe-602b-2ea0-a04b66beb2c0", "user": { "groups": [ "Test Group" ], "key": "DUOR48RKV2AYN7YVS9BT", "name": "example-user" }, "logType": "authentication" }, { "action": "user_create", "description": "{\"status\": \"Active\", \"email\": \"user@example.com\", \"realname\": \"\", \"notes\": \"\", \"uname\": \"user\"}", "isotimestamp": "2023-04-30T07:52:18+00:00", "object": "user", "timestamp": 1682836490, "username": "API (Admin API)", "logType": "administrator" }, { "bypassStatusEnabled": 1682836486230, "enabledBy": { "key": "DEKU19BYSSJSOABCD123", "name": "Admin" }, "enabledFor": { "key": "DUM07ZQ4LY00TABCD123", "name": "example-user" }, "priorityEvent": false, "sekey": "SE80GVU5Z47F0ABCD123", "state": "new", "surfacedTimestamp": 1682836486232, "triagedAsInteresting": false, "type": "bypass_status", "logType": "trust_monitor_event" } ]|
  
Example output:

```
{
  "logs": [
    {
      "accessDevice": {
        "browser": "Chrome",
        "browserVersion": "113.0.0.0",
        "ip": "198.51.100.1",
        "isEncryptionEnabled": "unknown",
        "isFirewallEnabled": "unknown",
        "isPasswordSet": "unknown",
        "location": {
          "city": "Los Angeles",
          "country": "United States",
          "state": "California"
        },
        "os": "Mac OS X",
        "osVersion": "10.15.7"
      },
      "alias": "unknown",
      "application": {
        "key": "DI8CODQSMK4BXPLYS47K",
        "name": "User Portal"
      },
      "authDevice": {
        "key": "DPAVQAJMU3BW0LV7OCX3",
        "name": "Generic Smartphone"
      },
      "eventType": "enrollment",
      "factor": "not_available",
      "isotimestamp": "2023-05-29T10:07:38.631165+00:00",
      "logType": "authentication",
      "result": "success",
      "timestamp": 1685354858,
      "trustedEndpointStatus": "unknown",
      "txid": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "user": {
        "groups": [
          "Test Group"
        ],
        "key": "DUOR48RKV2AYN7YVS9BT",
        "name": "example-user"
      }
    },
    {
      "action": "user_create",
      "description": "{\"status\": \"Active\", \"email\": \"user@example.com\", \"realname\": \"\", \"notes\": \"\", \"uname\": \"user\"}",
      "isotimestamp": "2023-04-30T07:52:18+00:00",
      "logType": "administrator",
      "object": "user",
      "timestamp": 1682836490,
      "username": "API (Admin API)"
    },
    {
      "bypassStatusEnabled": 1682836486230,
      "enabledBy": {
        "key": "DEKU19BYSSJSOABCD123",
        "name": "Admin"
      },
      "enabledFor": {
        "key": "DUM07ZQ4LY00TABCD123",
        "name": "example-user"
      },
      "logType": "trust_monitor_event",
      "priorityEvent": false,
      "sekey": "SE80GVU5Z47F0ABCD123",
      "state": "new",
      "surfacedTimestamp": 1682836486232,
      "triagedAsInteresting": false,
      "type": "bypass_status"
    }
  ]
}
```

### Custom Types
  
**phoneUser**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Activated|boolean|None|False|Whether the phone has already been activated for Duo Mobile|True|
|Capabilities|[]string|None|False|List of factors that can be used with the phone|["push"]|
|Encrypted|string|None|False|The encryption status of an Android or iOS device file system|Encrypted|
|Extension|string|None|False|Extension of the phone|ExampleExtension|
|Fingerprint|string|None|False|Whether an Android or iOS phone is configured for biometric verification|Configured|
|Last Seen|string|None|False|An integer indicating the timestamp of the last contact between Duo's service and the activated Duo Mobile app installed on the phone|2023-05-12 07:34:09|
|Model|string|None|False|The phone's model|Apple iPhone 11 Pro|
|Name|string|None|False|Free-form label for the phone|ExampleName|
|Number|string|None|False|Number|123456789|
|Phone ID|string|None|False|The phone's ID|ABCDEABC00ABC00ABCDE|
|Platform|string|None|False|The phone platform|unknown|
|Postdelay|string|None|False|The time (in seconds) to wait after the extension is dialed and before the speaking the prompt|3600|
|Predelay|string|None|False|The time (in seconds) to wait after the number picks up and before dialing the extension|3600|
|Screen Lock|string|None|False|Whether screen lock is enabled on an Android or iOS phone|Locked|
|SMS Passcodes Sent|boolean|None|False|Whether the SMS passcodes has been sent to this phone|True|
|Type|string|None|False|Whether an iOS or Android device is jailbroken or rooted|Tampered|
|Type|string|None|False|The type of phone|mobile|
  
**group**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|The group's description|Example Description|
|Group ID|string|None|False|The group's ID|ABCDEABC00ABC00ABCDE|
|Name|string|None|False|The group's name|Example Group Name|
|Status|string|None|False|The group's authentication status|Active|
  
**token**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Admins|[]object|None|False|A list of administrators associated with this hardware token|[]|
|Serial|string|None|False|The serial number of the hardware token|123456|
|Token ID|string|None|False|The hardware token's unique ID|ABCDEABC00ABC00ABCDE|
|Type|string|None|False|The type of hardware token|type1|
|Users|[]object|None|False|A list of end users associated with this hardware token|[]|
  
**webauthnaredentials**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Credential Name|string|None|False|Free-form label for the WebAuthn credential|Key1|
|Credential Name|integer|None|False|The date the WebAuthn credential was registered in Duo|1550674764|
|Label|string|None|False|Indicates the type of WebAuthn credential|Security Key|
|User|object|None|False|Selected information about the end user attached to the WebAuthn credential|{}|
|WebAuthnKey|string|None|False|The WebAuthn credential's registration identifier|ABCDEABC00ABC00ABCDE|
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alias 1|string|None|False|The user's username alias 1|example-alias-1|
|Alias 2|string|None|False|The user's username alias 2|example-alias-2|
|Alias 3|string|None|False|The user's username alias 3|example-alias-3|
|Alias 4|string|None|False|The user's username alias 4|example-alias-4|
|Aliases|object|None|False|The user's aliases|{}|
|Created|integer|None|False|The user's creation date as a UNIX timestamp|1684238502|
|Email|string|None|False|The user's email address|user@example.com|
|Groups|[]group|None|False|List of groups to which this user belongs|[]|
|Is Enrolled|boolean|None|False|Whether the user has a phone, hardware token, U2F token, WebAuthn security key, or other WebAuthn method available for authentication|True|
|Last Directory Sync|integer|None|False|An integer indicating the last update to the user via directory sync as a Unix timestamp, or null if the user has never synced with an external directory or if the directory that originally created the user has been deleted from Duo|1234|
|Last Login|integer|None|False|An integer indicating the last time this user logged in, as a Unix timestamp, or null if the user has not logged in|1234|
|Notes|string|None|False|Notes about this user|Example Note|
|Phones|[]phoneUser|None|False|A list of phones that this user can use|[]|
|Real Name|string|None|False|The user's real name or full name|Test User|
|Status|string|None|False|The user's status|active|
|Tokens|[]token|None|False|A list of tokens that this user can use|[]|
|User ID|string|None|False|The user's ID|ABCDEABC00ABC00ABCDE|
|Username|string|None|False|The user's username|test-username|
|Web Auth Credentials|[]webauthnaredentials|None|False|A list of WebAuthn authenticators that this user can use|[]|
  
**location**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|City|string|None|False|The city name|Ann Arbor|
|Country|string|None|False|The country name|United States|
|State|string|None|False|The state, county, province, or prefecture|Michigan|
  
**keyNamePair**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Key|string|None|False|The integration key|DIY231J8BR23QK4UKBY8|
|Name|string|None|False|The name|Microsoft Azure Active Directory|
  
**authlogUser**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Groups|[]string|None|False|Duo group membership information for the user|["Duo Users"]|
|Key|string|None|False|The ID of the user|DU3KC77WJ06Y5HIV7XKQ|
|Name|string|None|False|The name of the user|user@example.com|
  
**authDevice**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IP Address|string|None|False|The IP address of the authentication device|198.51.100.1|
|Key|string|None|False|The Duo identifier of the authentication device|DP5BJ05HI4WRBVI4Q7JF|
|Location|location|None|False|The GeoIP location of the authentication device|{}|
|Name|string|None|False|The name of the authentication device|My iPhone X|
  
**accessDevice**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Access Device|string|None|False|The web browser used for access|Chrome|
|Browser Version|string|None|False|The browser version|67.0.3396.99|
|Flash Version|string|None|False|The Flash plugin version used|uninstalled|
|Hostname|string|None|False|The hostname|example-hostname|
|IP Address|string|None|False|The access device's IP address|198.51.100.1|
|Is Encryption Enabled|string|None|False|Reports the disk encryption state as detected by the Duo Device Health app. One of true, false, or unknown|True|
|Is Firewall Enabled|string|None|False|Reports the firewall state as detected by the Duo Device Health app. One of true, false, or unknown|True|
|Is Password Set|string|None|False|Reports the system password state as detected by the Duo Device Health app. One of true, false, or unknown|True|
|Java Version|string|None|False|The Java plugin version used|uninstalled|
|Location|location|None|False|The GeoIP location of the access device|{}|
|Operating System|string|None|False|The device operating system name|Mac OS X|
|Operating System Version|string|None|False|The device operating system version|10.14.1|
  
**trustAssessmentObject**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Features Version|string|None|False|The feature version for the risk-based authentication trust assessment|3.0|
|Model Version|string|None|False|The model version for the risk-based authentication trust assessment|2022.07.19.001|
|Policy Enabled|boolean|None|False|Denotes if risk-based authentication was enabled by the policy under which the trust assessment was evaluated|False|
|Reason|string|None|False|The reason behind the trust assessment level|Normal level of trust; no detection of known attack pattern|
|Trust Level|string|None|False|The trust assessment level. Can be one of: ERROR, LOW, NORMAL, UNKNOWN, or UNSET|NORMAL|
  
**adaptiveTrustAssessments**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|More Secure Auth|trustAssessmentObject|None|False|Trust assessment information for Risk-Based Factor Selection|{}|
|Remember Me|trustAssessmentObject|None|False|Trust assessment information for Risk-Based Remembered Devices|{}|
  
**authLog**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Access Device|accessDevice|None|False|Browser, plugin, and operating system information for the endpoint used to access the Duo-protected resource. Values present only when the application accessed features Duo's inline browser prompt|{}|
|Adaptive Trust Assessments|adaptiveTrustAssessments|None|False|Risk-based authentication information. Values present only when the application accessed features Duo's inline browser prompt and has a Duo Risk-Based Authentication policy applied|{}|
|Alias|string|None|False|The username alias used to log in. No value if the user logged in with their username instead of a username alias|test|
|Application|keyNamePair|None|False|Information about the application accessed|{}|
|Auth Device|authDevice|None|False|Information about the device used to approve or deny authentication|{}|
|Email|string|None|False|The email address of the user|user@example.com|
|Event Type|string|None|False|The type of activity logged|authentication|
|Factor|string|None|False|The authentication factor|duo_push|
|ISO8601 Timestamp|string|None|False|ISO8601 timestamp of the event|2020-02-13 18:56:20.351346+00:00|
|OOD Software|string|None|False|If authentication was denied due to out-of-date software, shows the name of the software|Chrome|
|Reason|string|None|False|The reason for the authentication attempt result|user_approved|
|Result|string|None|False|The result of the authentication attempt. One of: 'success', 'denied', 'failure', 'error', or 'fraud'|success|
|Timestamp|number|None|False|An integer indicating the Unix timestamp of the event|1581620180|
|Transaction ID|string|None|False|The transaction ID of the event|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|User|authlogUser|None|False|Information about the authenticating user|{}|
  
**explanation**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Summary|string|None|False|Summary of the event|example-user has not accessed this application recently|
|Type|string|None|False|Type of the event|NEW_IKEY|
  
**priorityReason**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Label|string|None|False|The label of the priority reason for the event's match|country|
|Type|string|None|False|The type of priority reason for the event's match|CN|
  
**log**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Access Device|accessDevice|None|False|Browser, plugin, and operating system information for the endpoint used to access the Duo-protected resource. Values present only when the application accessed features Duo's inline browser prompt|{}|
|Action|string|None|False|The type of change that was performed|user_update|
|Adaptive Trust Assessments|adaptiveTrustAssessments|None|False|Risk-based authentication information. Values present only when the application accessed features Duo's inline browser prompt and has a Duo Risk-Based Authentication policy applied|{}|
|Alias|string|None|False|The username alias used to log in. No value if the user logged in with their username instead of a username alias|test|
|Application|keyNamePair|None|False|Information about the application accessed|{}|
|Auth Device|authDevice|None|False|Information about the device used to approve or deny authentication|{}|
|Bypass Status Enabled|integer|None|False|An integer indicating the Unix timestamp in milliseconds when bypass status was enabled for the user or group|1604337058989|
|Description|string|None|False|String detailing what changed|{"notes": "Joe asked for their nickname to be displayed instead of Joseph.", "realname": "Joe Smith"}|
|Email|string|None|False|The email address of the user|user@example.com|
|Enabled By|keyNamePair|None|False|The application or the administrator that enabled bypass status|{}|
|Enabled For|keyNamePair|None|False|The user or group with bypass status|{}|
|Event Type|string|None|False|The type of activity logged|authentication|
|Explanations|[]explanation|None|False|An array of objects describing why Trust Monitor surfaced the event|[]|
|Factor|string|None|False|The authentication factor|duo_push|
|From Common Netblock|boolean|None|False|A boolean describing if this event was created from a common IP netblock|True|
|From New User|boolean|None|False|A boolean describing if this event was created for a new user|False|
|ISO8601 Timestamp|string|None|False|ISO8601 timestamp of the event|2020-02-13 18:56:20.351346+00:00|
|Log Type|string|None|False|Type of the log|auth|
|Low Risk IP|boolean|None|False|A boolean describing if this event was created from an IP address identified in the Risk Profile configuration as a low risk IP address|False|
|Object|string|None|False|The object that was acted on|jsmith|
|OOD Software|string|None|False|If authentication was denied due to out-of-date software, shows the name of the software|Chrome|
|Priority Event|boolean|None|False|A boolean describing if the event matches the Risk Profile configuration|False|
|Priority Reasons|[]priorityReason|None|False|An array of objects describing how the event matches the Trust Monitor Risk Profile configuration|[]|
|Reason|string|None|False|The reason for the authentication attempt result|user_approved|
|Result|string|None|False|The result of the authentication attempt. One of: 'success', 'denied', 'failure', 'error', or 'fraud'|success|
|Sekey|string|None|False|The unique identifier for this event|SEDOR9BP00L23C6YUH5|
|State|string|None|False|A string describing the state of the event|new|
|State Updated Timestamp|integer|None|False|An integer indicating the Unix timestamp in milliseconds of the last change to the state of the event|1675893605269|
|Surfaced Auth|authLog|None|False|An object which represents the actual authentication|{}|
|Surfaced Timestamp|integer|None|False|An integer indicating the Unix timestamp in milliseconds when the event was surfaced by Trust Monitor|1675893605269|
|Timestamp|number|None|False|An integer indicating the Unix timestamp of the event|1581620180|
|Triage Event URI|string|None|False|A string representing the URI of the security event, which a Duo administrator can use to view and process the surfaced event in the Duo Admin Panel|https://example.com|
|Triaged As Interesting|boolean|None|False|A boolean describing if this event was triaged as being interesting or not interesting|False|
|Transaction ID|string|None|False|The transaction ID of the event|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Type|string|None|False|The type of event|auth|
|User|authlogUser|None|False|Information about the authenticating user|{}|
|Username|string|None|False|The full name of the administrator who performed the action|admin|


## Troubleshooting

* Many actions in this plugin take a User ID as input. A User ID is not the username - instead it's a unique identifier e.g. DU9I6T0F7R2S1J4XZHHA. A User ID can be obtained by passing a username to the Get User Status action.

# Version History

* 5.0.6 - Update SDK to the latest version (6.3.6) | Update Task `Monitor Logs` for Task delay logging
* 5.0.5 - Updated SDK to the latest version (6.3.3)
* 5.0.4 - Updated SDK to the latest version (6.2.5)
* 5.0.3 - Bump the SDK to version 6.2.3 | Update Task `monitor_logs` to delay retry if a rate limit error is returned from Duo Admin
* 5.0.2 - Updated SDK to the latest version (v6.2.2) | Address vulnerabilities
* 5.0.1 - Update to enable Plugin as FedRAMP ready | Update SDK (`6.1.2`)
* 5.0.0 - Updated to include latest SDK v5.5.5 | Removing Unused fields from User Object
* 4.4.2 - Updated to include latest SDK v5.4.9 | Task `Monitor Logs` updated to increase max lookback cutoff to 7 days
* 4.4.1 - `Monitor Logs` task updated to stop logging of trust monitor events response
* 4.4.0 - `Monitor Logs` task updated to handle `custom_config` parameter for each log type separately | Apply lookback limit of 180 days due to Duo Admin API limitation
* 4.3.2 - Monitor Logs task: Update to latest SDK | `Monitor Logs` task updated to handle `custom_config` parameter
* 4.3.1 - Monitor Logs task: Added exception logging and use latest plugin SDK (`5.3.1`).
* 4.3.0 - Monitor Logs task: Added inputs for collecting events and logs. Updated 403 error handling
* 4.2.2 - Monitor Logs task: updated unit tests
* 4.2.1 - Monitor Logs task: updated timestamp handling
* 4.2.0 - Monitor Logs task: removed formatting of task output
* 4.1.1 - Monitor Logs task: strip http/https in hostname, fix problem with generating header signature
* 4.1.0 - Update to latest plugin SDK
* 4.0.0 - Add Monitor Logs task | Code refactor | Update plugin to be cloud enabled
* 3.4.0 - Add `maxtime`, `applications`, `users`, `event_types`, `factors`, `groups`, `phone_numbers`, `reasons`, `results`, `registration_id`, `token_id`, `webauthnkey` inputs in `Get Logs` action | Update custom type for `authlogs` output
* 3.3.4 - Correct spelling in help.md
* 3.3.3 - Changed `Exception` to `PluginException` | Moved constants to class init | Use fstring instead of concatenation
* 3.3.2 - New spec and help.md format for the Extension Library
* 3.3.1 - Update default `mintime` input and description for `Get Logs` action
* 3.3.0 - New action Enroll User | Support Duo Admin API v2 where applicable | Various bug fixes & improvements
* 3.2.0 - New action Get Phones by User ID
* 3.1.0 - New Action to Add User | Updated duo_client version to 3.3.0
* 3.0.0 - Rename `Get User By ID` action to `Get User by ID` | Rename `Get User By Username` action to `Get User by Username` | Rename `Delete User By ID` action to `Delete User by ID` | Rename `Modify User By ID` action to `Modify User by ID`
* 2.0.0 - Update to new credential types | Add example output
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Add action Get User By Username
* 0.1.6 - Fix `NameError: global name 'param' is not defined` in Delete action
* 0.1.5 - SSL bug fix in SDK
* 0.1.4 - Bug fix in modify user action where None value is present in response, invalid schema in run and test method
* 0.1.3 - Bug fix in user status action when user doesn't exist
* 0.1.2 - Add action to get user status
* 0.1.0 - Initial plugin

# Links

* [Duo Security](https://duo.com/)

## References

* [Duo Admin API](https://duo.com/docs/adminapi)