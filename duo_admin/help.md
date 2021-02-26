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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hostname|string|None|True|Duo API hostname|None|None|
|integration_key|credential_secret_key|None|True|API integration key|None|None|
|secret_key|credential_secret_key|None|True|API secret key|None|None|

Example input:

```
```

## Technical Details

### Actions

#### Get User by ID

This action is used to retrieve user information by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|user_id|string|None|True|User ID, e.g. DUCUULF6HBMZ43IG9MBH|None|None|

Example input:

```
```

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
    "email": "user@example.com",
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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|username|string|None|True|Username, e.g. jdoe|None|None|

Example input:

```
```

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
    "email": "user@example.com",
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

If the user is found, the action returns one of the following statuses: active, bypass, disabled, or locked out, and the user's ID. The user's ID can be used as input to actions in the plugin that require a User ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|user|string|None|True|The user account to check status, e.g. jdoe|None|None|

Example input:

```
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|status|string|None|True|New status|['active', 'disabled', 'bypass']|None|
|user_id|string|None|True|User ID, e.g. DUCUULF6HBMZ43IG9MBH|None|None|

Example input:

```
```

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
    "email": "user@example.com"
  }
}

```

#### Get Users

This action is used to retrieve information on users.

##### Input

_This action does not contain any inputs._

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
      "email": "user@example.com",
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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|user_id|string|None|True|User ID to remove, e.g. DUCUULF6HBMZ43IG9MBH|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|string|False|Response|


#### Get Authentication Logs

This action is used to get auth logs, limited to past 180 days.
[Currentmillis.com](https://currentmillis.com/) is useful for finding a usable UNIX timestamp.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|applications|[]string|None|False|List of application IDs to filter on|None|["DIV9C5V7T6L02DRWL4RU"]|
|event_types|[]string|None|False|List of event types(authentication, enrollment) to filter on, to include all leave this parameter empty|None|["authentication"]|
|factors|[]string|None|False|List of factors or methods used for an authentication attempt(duo_push, phone_call, u2f_token, hardware_token, bypass_code, sms_passcode, duo_mobile_passcode, yubikey_code, passcode, digipass_go_7_token, not_available, sms_refresh, remembered_device, trusted_network) to filter on, to include all leave this parameter empty|None|["duo_push", "sms_passcode"]|
|groups|[]string|None|False|List of group IDs to filter on|None|["DG67EON0I1QA2ZDUF32M"]|
|maxtime|integer|None|False|Maximum time in UNIX timestamp milliseconds. Must be 13 or more digits in length and greater than mintime. To use current time leave this parameter empty|None|1611069760000|
|mintime|integer|None|True|Minimum time in UNIX timestamp milliseconds. Must be 13 or more digits in length|None|1609377288936|
|phone_numbers|[]string|None|False|List of phone numbers to filter on|None|["+11111111111"]|
|reasons|[]string|None|False|List of reasons associated with an authentication attempt(user_marked_fraud, deny_unenrolled_user, error, locked_out, user_disabled, user_cancelled, invalid_passcode, no_response, no_keys_pressed, call_timed_out, location_restricted, factor_restricted, platform_restricted, version_restricted, rooted_device, no_screen_lock, touch_id_disabled, no_disk_encryption, anonymous_ip, out_of_date, denied_by_policy, software_restricted, no_duo_certificate_present, user_provided_invalid_certificate, could_not_determine_if_endpoint_was_trusted, invalid_management_certificate_collection_state, no_referring_hostname_provided, invalid_referring_hostname_provided, no_web_referer_match, endpoint_failed_google_verification, endpoint_is_not_trusted, invalid_device, anomalous_push,  endpoint_is_not_in_management_system, no_activated_duo_mobile_account, allow_unenrolled_user, bypass_user, trusted_network, remembered_device, trusted_location, user_approved, valid_passcode, allowed_by_policy, allow_unenrolled_user_on_trusted_network, user_not_in_permitted_group) to filter on, to include all leave this parameter empty|None|["user_disabled"]|
|registration_id|[]string|None|False|List of FIDO U2F token registration IDs to filter on|None|["D21RU6X1B1DF5P54B6PV"]|
|results|[]string|None|False|List of results of an authentication attempt(success, denied, fraud) to filter on, to include all leave this parameter empty|None|["denied"]|
|token_id|[]string|None|False|List of hardware OTP token IDs to filter on|None|["DHIZ34ALBA2445ND4AI2"]|
|users|[]string|None|False|List of user IDs to filter on|None|["DUW2DKA44RFYECTU8R1O"]|
|webauthnkey|[]string|None|False|List of WebAuthn security keys to filter on|None|["WA4ED9AUVMSWUF00KES4"]|

Example input:

```
{
  "applications": [
    "DIV9C5V7T6L02DRWL4RU"
  ],
  "event_types": [
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
  "phone_numbers": [
    "+11111111111"
  ],
  "reasons": [
    "user_disabled"
  ],
  "registration_id": [
    "D21RU6X1B1DF5P54B6PV"
  ],
  "results": [
    "denied"
  ],
  "token_id": [
    "DHIZ34ALBA2445ND4AI2"
  ],
  "users": [
    "DUW2DKA44RFYECTU8R1O"
  ],
  "webauthnkey": [
    "WA4ED9AUVMSWUF00KES4"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|authlogs|[]authlog|True|Logs|

Example output:

```

{
  "authlogs": [
    {
      "access_device": {
        "browser": "Chrome",
        "browser_version": "67.0.3396.99",
        "flash_version": "uninstalled",
        "hostname": "api-a22b2135.duosecurity.com",
        "ip": "98.226.218.52",
        "is_encryption_enabled": true,
        "is_firewall_enabled": true,
        "is_password_set": true,
        "java_version": "uninstalled",
        "location": {
          "city": "Bloomington",
          "country": "United States",
          "state": "Illinois"
        },
        "os": "Mac OS X",
        "os_version": "10.14.1",
        "security_agents": []
      },
      "alias": "",
      "application": {
        "key": "DIV9C5V7T6L02DRWL4RU",
        "name": "Microsoft Azure Active Directory"
      },
      "auth_device": {
        "ip": "192.168.220.245",
        "location": {
          "city": "Bloomington",
          "country": "United States",
          "state": "Illinois"
        },
        "name": "+11111111111"
      },
      "email": "user@example.com",
      "event_type": "authentication",
      "factor": "duo_push",
      "isotimestamp": "2021-01-19T14:47:24.309957+00:00",
      "ood_software": "null",
      "reason": "user_disabled",
      "result": "denied",
      "timestamp": 1611067644,
      "txid": "340a23e3-23f3-23c1-87dc-1491a23dfdbb",
      "user": {
        "groups": [
          "InsightConnect Group",
        ],
        "key": "DUW2DKA44RFYECTU8R1O",
        "name": "user@example.com"
      }
    }
  ]
}

```

#### Add User

This action is used to add a user in Duo Admin.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alias|[]string|None|False|User alias. May have up to 4 unique amongst users|None|None|
|email|string|None|False|Email of the user|None|None|
|firstname|string|None|False|The users given name. Required for Duo's ID Proofing feature|None|None|
|lastname|string|None|False|The users surname. Required for Duo's ID Proofing feature|None|None|
|notes|string|None|False|An optional description or notes field. Can be viewed in the Admin Panel|None|None|
|realname|string|None|False|User's real name|None|None|
|status|string|disabled|False|User status, e.g. active, bypass, disabled|['active', 'bypass', 'disabled']|None|
|username|string|None|True|The name of the user to create|None|None|

Example input:

```
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|user_id|string|None|True|User ID, e.g. DUCUULF6HBMZ43IG9MBH|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|phone_list|[]phone_user|False|List of phones associated with the user's ID|

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|Email address to send enrollment email to|None|None|
|time_to_expiration|number|0|True|Amount of time in seconds until enrollment email expires. Use '0' for no expiration|None|None|
|username|string|None|True|Username for user to enroll|None|None|

Example input:

```
```

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

_This plugin does not contain any triggers._

### Custom Output Types

#### access_device

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Browser|string|False|None|
|Browser Version|string|False|None|
|Flash Version|string|False|None|
|Hostname|string|False|None|
|IP Address|string|False|None|
|Is Encryption Enabled|string|False|None|
|Is Firewall Enabled|string|False|None|
|Is Password Set|string|False|None|
|Java Version|string|False|None|
|Location|location|False|None|
|Operating System|string|False|None|
|Operating System Version|string|False|None|
|Security Agents|[]string|False|None|

#### application

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Key|string|False|None|
|Name|string|False|None|

#### auth_device

|Name|Type|Required|Description|
|----|----|--------|-----------|
|IP Address|string|False|None|
|Location|location|False|None|
|Name|string|False|None|

#### authlog

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access Device|access_device|True|None|
|Alias|string|False|None|
|Application|application|True|None|
|Auth Device|auth_device|True|None|
|Email|string|False|None|
|Event Type|string|False|None|
|Eventtype|string|False|None|
|Factor|string|False|None|
|Host|string|False|None|
|ISO8601 Timestamp|number|False|None|
|OOD Software|string|False|None|
|Reason|string|False|None|
|Result|string|False|None|
|Timestamp|number|False|None|
|Transaction ID|string|False|None|
|User|authlog_user|True|None|

#### authlog_user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Groups|[]string|False|None|
|Key|string|False|None|
|Name|string|False|None|

#### group

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Desc|string|False|None|
|Name|string|False|None|

#### location

|Name|Type|Required|Description|
|----|----|--------|-----------|
|City|string|False|None|
|Country|string|False|None|
|State|string|False|None|

#### phone

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Activated|boolean|False|None|
|Capabilities|[]string|False|None|
|Extension|string|False|None|
|Number|string|False|None|
|Phone ID|string|False|None|
|Platform|string|False|None|
|Postdelay|string|False|None|
|Predelay|string|False|None|
|SMS Passcodes Sent|boolean|False|None|

#### phone_user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Activated|boolean|False|Activated|
|Capabilities|[]string|False|Capabilities|
|Extension|string|False|Extension|
|Name|string|False|Name|
|Number|string|False|Number|
|Phone ID|string|False|Phone ID|
|Platform|string|False|Platform|
|Post delay|string|False|Post delay|
|Predelay|string|False|Predelay|
|SMS Passcodes Sent|boolean|False|SMS passcodes sent|
|Type|string|False|Type|

#### response

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Alias 1|string|False|Alias 1|
|Alias 2|string|False|Alias 2|
|Alias 3|string|False|Alias 3|
|Alias 4|string|False|Alias 4|
|Email|string|False|Email|
|First Name|string|False|First name|
|Groups|[]group|False|Groups|
|Last Login|integer|False|Last login|
|Last Name|string|False|Last name|
|Notes|string|False|Notes|
|Phones|[]phone_user|False|Phones|
|Real Name|string|False|Real name|
|Status|string|False|Status|
|Tokens|[]token|False|Tokens|
|User ID|string|False|User ID|
|Username|string|False|Username|

#### token

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Serial|string|False|Serial|
|Token ID|string|False|Token ID|
|Type|string|False|Type|

#### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Email|string|False|None|
|Groups|[]group|False|None|
|Last Login|integer|False|None|
|Notes|string|False|None|
|Phones|[]phone|False|None|
|Realname|string|False|None|
|Status|string|False|None|
|Tokens|[]token|False|None|
|User ID|string|True|None|
|Username|string|False|None|

## Troubleshooting

Many actions in this plugin take a User ID as input. A User ID is not the username - instead it's a unique identifier e.g. DU9I6T0F7R2S1J4XZHHA.
A User ID can be obtained by passing a username to the Get User Status action.

# Version History

* 3.4.0 - Add `maxtime`, `applications`, `users`, `event_types`, `factors`, `groups`, `phone_numbers`, `reasons`, `results`, `registration_id`, `token_id`, `webauthnkey` inputs in `Get Logs` action | Update custom type for `authlogs` output
* 3.3.4 - Correct spelling in help.md
* 3.3.3 - Changed `Exception` to `PluginException` | Moved constants to class init | Use fstring instead of concatenation
* 3.3.2 - New spec and help.md format for the Extension Library
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
