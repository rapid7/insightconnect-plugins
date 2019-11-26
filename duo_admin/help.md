# Description

[Duo](https://duo.com/)'s Trusted Access platform verifies the identity of your users with two-factor authentication and
security health of their devices before they connect to the apps they use. Using the Duo plugin for InsightConnect will allow Duo user management within automation workflows.

# Key Features

* Add and delete users
* Enroll users
* Get user information

# Requirements

* Requires two secret keys from Duo

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|secret_key|credential_secret_key|None|True|API secret key|None|
|hostname|string|None|True|Duo API hostname|None|
|integration_key|credential_secret_key|None|True|API integration key|None|

## Technical Details

### Actions

#### Get User by ID

This action is used to retrieve user information by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|True|User ID, e.g. DUCUULF6HBMZ43IG9MBH|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|user|False|User|

Example output:

```

{
  "user": {
    "created": 1111111111,
    "desktoptokens": [],
    "email": "john@example.org",
    "groups": [],
    "last_login": 1511423501,
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
        "last_seen": "2018-08-20T06:52:20",
        "number": "+11111111111",
        "phone_id": "1234ABCDEFG",
        "platform": "Apple iOS",
        "sms_passcodes_sent": false,
        "type": "Mobile"
      }
    ],
    "realname": "John Doe",
    "status": "active",
    "tokens": [],
    "u2ftokens": [],
    "user_id": "BUUUUUUUUUUUUUUUUUUZ",
    "username": "jdoe"
  }
}

```

#### Get User by Username

This action is used to retrieve information by username.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|Username, e.g. jdoe|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|user|False|User|

Example output:

```

{
  "user": {
    "created": 1462823674,
    "desktoptokens": [],
    "email": "jane@example.org",
    "groups": [],
    "last_login": 1534446415,
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
        "last_seen": "2018-08-21T15:57:34",
        "number": "+12222222222",
        "phone_id": "11111113RP6666666666",
        "platform": "Google Android",
        "sms_passcodes_sent": false,
        "type": "Mobile"
      }
    ],
    "status": "active",
    "tokens": [],
    "u2ftokens": [],
    "user_id": "A777777777777777777W",
    "username": "janedoe"
  }
}

```

#### Get User Status

This action is used to get the account status of a user. If no users exist this action returns 'No results', and if the specified user does not exist it returns 'No user'.
Also, for both these conditions `user_id` will return `None`.

If the user is found, the action returns one of the following statuses: active, bypass, disabled, or locked out, and the user's ID. The user's ID can be used as input to actions in thie plugin that require a User ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user|string|None|True|The user account to check status, e.g. jdoe|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|True|Status|
|user_id|string|True|User ID|

Example user:

```

{
  "status": "active"
  "user_id": "DU3RP9I2WOC59VZX672"
}

```

#### Modify User by ID

This action is used to modify a user by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|status|string|None|True|New status|['active', 'disabled', 'bypass']|
|user_id|string|None|True|User ID, e.g. DUCUULF6HBMZ43IG9MBH|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|user|False|User|

Example output:

```

{
  "user": {
    "status": "disabled",
    "username": "test",
    "realname": "Test",
    "tokens": [],
    "groups": [],
    "desktoptokens": [],
    "user_id": "DU9B7X097A3G9A4BABBA",
    "alias3": "Test Test",
    "phones": [],
    "email": "test@example.com"
  }
}

```

#### Get Users

This action is used to retrieve information on users.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|users|[]user|False|Users|

Example output:

```

{
  "users": [
    {
      "created": 1111111111,
      "desktoptokens": [],
      "email": "john@example.org",
      "groups": [],
      "last_login": 1511423501,
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
          "last_seen": "2018-08-20T06:52:20",
          "number": "+11111111111",
          "phone_id": "ABCDEFGHIJ",
          "platform": "Apple iOS",
          "sms_passcodes_sent": false,
          "type": "Mobile"
        }
      ],
      "realname": "John Doe",
      "status": "active",
      "tokens": [],
      "u2ftokens": [],
      "user_id": "BUUUUUUUUUUUUUUUUUUZ",
      "username": "jdoe"
    },
    ...
  ]
}

```

#### Delete User by ID

This action is used to delete a user by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|True|User ID to remove, e.g. DUCUULF6HBMZ43IG9MBH|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|string|False|Response|

Example output:

```
```

#### Get Authentication Logs

This action is used to get auth logs, limited to past 180 days.
[Currentmillis.com](https://currentmillis.com/) is useful for finding a usable UNIX timestamp.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|mintime|integer|None|False|Minimum time in UNIX timestamp milliseconds. Must be 13 or more digits in length|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|authlogs|[]authlog|True|Logs|

Example output:

```

{
  "logs": [
    {
      "factor": "Bypass Code",
      "integration": "UNIX Servers Login",
      "ip": "98.226.218.52",
      "location": {
        "city": "Bloomington",
        "country": "US",
        "state": "Illinois"
      },
      "new_enrollment": false,
      "reason": "Valid passcode",
      "result": "SUCCESS",
      "timestamp": 1466092180,
      "username": "centos",
      "eventtype": "authentication",
      "host": "api-a22b2135.duosecurity.com"
    },
  ]
}

```

#### Add User

This action is used to add a user in Duo Admin.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|The name of the user to create|None|
|status|string|disabled|False|User status, e.g. active, bypass, disabled|['active', 'bypass', 'disabled']|
|realname|string|None|False|User's real name|None|
|firstname|string|None|False|The users given name. Required for Duo's ID Proofing feature|None|
|lastname|string|None|False|The users surname. Required for Duo's ID Proofing feature|None|
|notes|string|None|False|An optional description or notes field. Can be viewed in the Admin Panel|None|
|alias|[]string|None|False|User alias. May have up to 4 unique amongst users|None|
|email|string|None|False|Email of the user|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|Response|

Example output:

```

{
  "response": {
    "created": 1538529180,
    "desktoptokens": [],
    "groups": [],
    "phones": [],
    "status": "active",
    "tokens": [],
    "u2ftokens": [],
    "user_id": "DUVSXMGU7NLM8H803W9L",
    "username": "testuser01"
}

```

#### Get Phones by User ID

This action is used to get a list of phones associated with the user ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|True|Duo users ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|phone_list|[]phone_user|False|Lost of phones associated with the user's ID|

Example output:

```
{
  "phone_list": [
    {
       "activated": true,
       "capabilities": [
         "auto",
         "push",
         "sms",
         "phone",
         "mobile_otp"
       ],
       "last_seen": "2019-01-15T23:02:20",
       "number": "+13093193442",
       "phone_id": "DP3WBHIG7HTOESVZ1IPZ",
       "platform": "Google Android",
       "sms_passcodes_sent": false,
       "type": "Mobile"
    }
  ]
}
```

#### Enroll User

This action is used to enroll a user and send an enrollment email to the specified email address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|Username for user to enroll|None|
|email|string|None|True|Email address to send enrollment email to|None|
|time_to_expiration|number|0|True|Amount of time in seconds until enrollment email expires. Use '0' for no expiration|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether or not the enrollment was successful|

Example output:

```
{
  "success": "true"
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Many actions in this plugin take a User ID as input. A User ID is not the username - instead it's a unique identifier e.g. DU9I6T0F7R2S1J4XZHHA.
A User ID can be obtained by passing a username to the Get User Status action.

# Version History

* 3.3.2 - New spec and help.md format for the Hub
* 3.3.1 - Update default `mintime` input and description for `Get Logs` action
* 3.3.0 - New action Enroll User | Support Duo Admin API v2 where applicable | Various bug fixes & improvements
* 3.2.0 - New action Get Phones by User ID
* 3.1.0 - New Action to Add User | Updated duo_client version to 3.3.0
* 3.0.0 - Rename "Get User By ID" action to "Get User by ID" | Rename "Get User By Username" action to "Get User by Username" | Rename "Delete User By ID" action to "Delete User by ID" | Rename "Modify User By ID" action to "Modify User by ID"
* 2.0.0 - Update to new credential types | Add example output
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Add action Get User By Username
* 0.1.6 - Fix `NameError: global name 'param' is not defined` in Delete action
* 0.1.5 - SSL bug fix in SDK
* 0.1.4 - Bug fix in modify user action where None value is present in response, invalid schema in run and test method
* 0.1.3 - Bug fix in user status action when user doesn't exist
* 0.1.2 - Add action to get user status
* 0.1.0 - Initial plugin

# Links

## References

* [Duo Security](https://duo.com/)
* [Duo Admin API](https://duo.com/docs/adminapi)

