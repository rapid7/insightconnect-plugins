# Description

[Duo](https://duo.com/)'s Trusted Access platform verifies the identity of your users with two-factor authentication and
security health of their devices before they connect to the apps they use. Using the Duo plugin for InsightConnect will 
allow Duo user management within automation workflows.

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

The following information are required for using `Duo Admin` plugin:
* Two secret keys - `integration key` and `secret key`
* `API hostname`

Read more [here](https://duo.com/docs/adminapi#first-steps).

# Supported Product Versions

* Duo Admin API 2023-05-19

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hostname|string|None|True|Duo API hostname|None|api-XXXXXXXX.duosecurity.com|
|integrationKey|credential_secret_key|None|True|API integration key|None|DUCUULF6HBMZ43IG9MBH|
|secretKey|credential_secret_key|None|True|API secret key|None|3rlCtQGBVpoCXkjP3pLslVWxO8b4W5j1|

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

#### Get User by ID

This action is used to retrieve user information by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|userId|string|None|True|User unique ID|None|DUCUULF6HBMZ43IG9MBH|

Example input:

```
{
  "userId": "DUCUULF6HBMZ43IG9MBH"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|user|user|False|User details|{}|

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

This action is used to retrieve information by username.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|username|string|None|True|Specify a username (or username alias) to look up a single user|None|jdoe|

Example input:

```
{
  "username": "jdoe"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|user|user|False|User details|{}|

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

This action is used to get the account status of a user.

If the user is found, the action returns one of the following statuses: active, bypass, disabled, or locked out, and the user's ID. The user's ID can be used as input to actions in the plugin that require a User ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|username|string|None|True|The username or alias for which you want to get the status|None|user|

Example input:

```
{
  "username": "user"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|status|string|True|Status of the user|active|
|userId|string|True|ID of the user|DU0W79YFWZAJWJV6P00L|

Example user:

```
{
  "status": "active"
  "userId": "DU3RP9I2WOC59VZX672"
}
```

#### Modify User by ID

This action is used to modify a user by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alias1|string|None|False|A username alias 1|None|alias1|
|alias2|string|None|False|A username alias 1|None|alias2|
|alias3|string|None|False|A username alias 3|None|alias3|
|alias4|string|None|False|A username alias 4|None|alias3|
|email|string|None|False|The new email address|None|user@example.com|
|firstname|string|None|False|The user's new given name|None|Example|
|lastname|string|None|False|The user's new surname|None|Example|
|notes|string|None|False|The new notes field|None|Example|
|realname|string|None|False|The new realname (or full name)|None|Example|
|status|string|None|False|The new status. Select 'None' to skip status change|['active', 'disabled', 'bypass', 'None']|active|
|userId|string|None|True|User unique ID|None|DUCUULF6HBMZ43IG9MBH|
|username|string|None|False|The new username|None|Example|

Example input:

```
{
  "alias1": "alias1",
  "alias2": "alias2",
  "alias3": "alias3",
  "alias4": "alias3",
  "email": "user@example.com",
  "firstname": "Example",
  "lastname": "Example",
  "notes": "Example",
  "realname": "Example",
  "status": "active",
  "userId": "DUCUULF6HBMZ43IG9MBH",
  "username": "Example"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|user|user|False|User details|{}|

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
    "firstname": "Example",
    "isEnrolled": false,
    "lastname": "Example",
    "notes": "Example",
    "realname": "Example",
    "status": "active",
    "userId": "DUCUULF6HBMZ43IG9MBH",
    "username": "Example"
  }
}
```

#### Get Users

This action is used to retrieve information on users.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|users|[]user|False|List of users|[]|

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
|userId|string|None|True|User ID to remove|None|DUCUULF6HBMZ43IG9MBH|

Example input:

```
{
  "userId": "DUCUULF6HBMZ43IG9MBH"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|False|Whether the action was successful|True|

Example output:

```
{
  "success": true
}
```

#### Get Authentication Logs

This action is used to get auth logs, limited to past 180 days.
[Currentmillis.com](https://currentmillis.com/) is useful for finding a usable UNIX timestamp.

Available inputs for parameters:

* `factors` - a comma-separated list of factors, if left empty, the action returns the authentication logs for all factors used for an authentication attempt
    * bypass_code
    * digipass_go_7_token
    * duo_mobile_passcode
    * duo_push
    * hardware_token
    * not_available
    * passcode
    * phone_call
    * remembered_device
    * sms_passcode
    * sms_refresh
    * trusted_network
    * u2f_token
    * yubikey_code
* `reasons` - a comma-separated list of reasons, if left empty, the action returns the authentication logs for all reasons associated with an authentication attempt
    * allow_unenrolled_user
    * allow_unenrolled_user_on_trusted_network
    * allowed_by_policy
    * anomalous_push
    * anonymous_ip
    * bypass_user
    * call_timed_out
    * could_not_determine_if_endpoint_was_trusted
    * denied_by_policy
    * deny_unenrolled_user
    * endpoint_failed_google_verification
    * endpoint_is_not_in_management_system
    * endpoint_is_not_trusted
    * error
    * factor_restricted
    * invalid_device
    * invalid_management_certificate_collection_state
    * invalid_passcode
    * invalid_referring_hostname_provided
    * location_restricted
    * locked_out
    * no_activated_duo_mobile_account
    * no_disk_encryption
    * no_duo_certificate_present
    * no_keys_pressed
    * no_referring_hostname_provided
    * no_response
    * no_screen_lock
    * no_web_referer_match
    * out_of_date
    * platform_restricted
    * remembered_device
    * rooted_device
    * software_restricted
    * touch_id_disabled
    * trusted_location
    * trusted_network
    * user_approved
    * user_cancelled
    * user_disabled
    * user_marked_fraud
    * user_not_in_permitted_group
    * user_provided_invalid_certificate
    * valid_passcode
    * version_restricted

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|applications|[]string|None|False|List of application IDs to filter on|None|["DIV9C5V7T6L02DRWL4RU"]|
|eventTypes|[]string|None|False|List of event types(authentication, enrollment) to filter on, to include all leave this parameter empty|None|["authentication"]|
|factors|[]string|None|False|List of factors or methods used for an authentication attempt to filter on, to include all leave this parameter empty. Check the help documentation to see all available inputs|None|["duo_push", "sms_passcode"]|
|groups|[]string|None|False|List of group IDs to filter on|None|["DG67EON0I1QA2ZDUF32M"]|
|maxtime|integer|None|False|Maximum time in UNIX timestamp milliseconds. Must be 13 or more digits in length and greater than mintime. To use current time leave this parameter empty|None|1611069760000|
|mintime|integer|None|True|Minimum time in UNIX timestamp milliseconds. Must be 13 or more digits in length|None|1609377288936|
|phoneNumbers|[]string|None|False|List of phone numbers to filter on|None|["+11111111111"]|
|reasons|[]string|None|False|List of reasons associated with an authentication attempt to filter on, to include all leave this parameter empty. Check the help documentation to see all available inputs|None|["user_disabled"]|
|results|[]string|None|False|List of results of an authentication attempt(success, denied, fraud) to filter on, to include all leave this parameter empty|None|["denied"]|
|tokens|[]string|None|False|List of FIDO U2F token registration IDs or WebAuthn security keys to filter on|None|["WA4ED9AUVMSWUF00KES4"]|
|users|[]string|None|False|List of user IDs to filter on|None|["DUW2DKA44RFYECTU8R1O"]|

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
|----|----|--------|-----------|-------|
|authLogs|[]authLog|True|Logs|[]|

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

#### Add User

This action is used to add a user in Duo Admin.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|aliases|[]string|None|False|User aliases. May have up to 4 unique amongst users|None|["test-alias"]|
|email|string|None|False|Email of the user|None|user@example.com|
|firstname|string|None|False|The user's given name. Required for Duo's ID Proofing feature|None|Test|
|lastname|string|None|False|The user's surname. Required for Duo's ID Proofing feature|None|User|
|notes|string|None|False|An optional description or notes field|None|Example note|
|realname|string|None|False|User's real name|None|Example User|
|status|string|active|False|User status|['active', 'bypass', 'disabled']|active|
|username|string|None|True|The name of the user to create|None|example-user|

Example input:

```
{
  "aliases": [
    "test-alias"
  ],
  "email": "user@example.com",
  "firstname": "Test",
  "lastname": "User",
  "notes": "Example note",
  "realname": "Example User",
  "status": "active",
  "username": "example-user"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|user|user|False|User|{}|

Example output:

```
{
  "user": {
    "aliases": [
      "test-alias"
    ],
    "created": 1538529180,
    "email": "user@example.com",
    "firstname": "Test",
    "lastname": "User",
    "notes": "Example note",
    "realname": "Example User",
    "status": "active",
    "userId": "DUVSXMGU7NLM8H803W9L",
    "username": "example-user"
  }
}
```

#### Get Phones by User ID

This action is used to get a list of phones associated with the user ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|userId|string|None|True|The identifier of the user|None|DUCUULF6HBMZ43IG9MBH|

Example input:

```
{
  "userId": "DUCUULF6HBMZ43IG9MBH"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|phoneList|[]phoneUser|False|List of phones associated with the user's ID|[]|

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

#### Enroll User

This action is used to enroll a user and send an enrollment email to the specified email address.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|Email address to send enrollment email to|None|user@example.com|
|timeToExpiration|number|0|False|Amount of time in seconds until enrollment email expires. Use '0' for no expiration|None|3600|
|username|string|None|True|Username for user to enroll|None|test-username|

Example input:

```
{
  "email": "user@example.com",
  "timeToExpiration": 3600,
  "username": "test-username"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|False|Whether or not the enrollment was successful|True|

Example output:

```
{
  "success": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Tasks

#### Monitor Logs

This task is used to monitor administrator, authentication and trust monitor event logs.

##### Input

_This task does not contain any inputs._

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|logs|[]log|True|List of administrator, authentication and trust monitor event logs within the specified time range|[]|

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
      },
      "logType": "authentication"
    },
    {
      "action": "user_create",
      "description": "{\"status\": \"Active\", \"email\": \"user@example.com\", \"realname\": \"\", \"notes\": \"\", \"uname\": \"user\"}",
      "isotimestamp": "2023-04-30T07:52:18+00:00",
      "object": "user",
      "timestamp": 1682836490,
      "username": "API (Admin API)",
      "logType": "administrator"
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
      "priorityEvent": false,
      "sekey": "SE80GVU5Z47F0ABCD123",
      "state": "new",
      "surfacedTimestamp": 1682836486232,
      "triagedAsInteresting": false,
      "type": "bypass_status",
      "logType": "trust_monitor_event"
    }
  ]
}
```

### Custom Output Types

#### accessDevice

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access Device|string|False|The web browser used for access|
|Browser Version|string|False|The browser version|
|Flash Version|string|False|The Flash plugin version used|
|Hostname|string|False|The hostname|
|IP Address|string|False|The access device's IP address|
|Is Encryption Enabled|string|False|Reports the disk encryption state as detected by the Duo Device Health app. One of true, false, or unknown|
|Is Firewall Enabled|string|False|Reports the firewall state as detected by the Duo Device Health app. One of true, false, or unknown|
|Is Password Set|string|False|Reports the system password state as detected by the Duo Device Health app. One of true, false, or unknown|
|Java Version|string|False|The Java plugin version used|
|Location|location|False|The GeoIP location of the access device|
|Operating System|string|False|The device operating system name|
|Operating System Version|string|False|The device operating system version|

#### adaptiveTrustAssessments

|Name|Type|Required|Description|
|----|----|--------|-----------|
|More Secure Auth|trustAssessmentObject|False|Trust assessment information for Risk-Based Factor Selection|
|Remember Me|trustAssessmentObject|False|Trust assessment information for Risk-Based Remembered Devices|

#### authDevice

|Name|Type|Required|Description|
|----|----|--------|-----------|
|IP Address|string|False|The IP address of the authentication device|
|Key|string|False|The Duo identifier of the authentication device|
|Location|location|False|The GeoIP location of the authentication device|
|Name|string|False|The name of the authentication device|

#### authLog

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access Device|accessDevice|False|Browser, plugin, and operating system information for the endpoint used to access the Duo-protected resource. Values present only when the application accessed features Duo's inline browser prompt|
|Adaptive Trust Assessments|adaptiveTrustAssessments|False|Risk-based authentication information. Values present only when the application accessed features Duo's inline browser prompt and has a Duo Risk-Based Authentication policy applied|
|Alias|string|False|The username alias used to log in. No value if the user logged in with their username instead of a username alias|
|Application|keyNamePair|False|Information about the application accessed|
|Auth Device|authDevice|False|Information about the device used to approve or deny authentication|
|Email|string|False|The email address of the user|
|Event Type|string|False|The type of activity logged|
|Factor|string|False|The authentication factor|
|ISO8601 Timestamp|string|False|ISO8601 timestamp of the event|
|OOD Software|string|False|If authentication was denied due to out-of-date software, shows the name of the software|
|Reason|string|False|The reason for the authentication attempt result|
|Result|string|False|The result of the authentication attempt. One of: 'success', 'denied', 'failure', 'error', or 'fraud'|
|Timestamp|number|False|An integer indicating the Unix timestamp of the event|
|Transaction ID|string|False|The transaction ID of the event|
|User|authlogUser|False|Information about the authenticating user|

#### authlogUser

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Groups|[]string|False|Duo group membership information for the user|
|Key|string|False|The ID of the user|
|Name|string|False|The name of the user|

#### explanation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Summary|string|False|Summary of the event|
|Type|string|False|Type of the event|

#### group

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Description|string|False|The group's description|
|Group ID|string|False|The group's ID|
|Name|string|False|The group's name|
|Status|string|False|The group's authentication status|

#### keyNamePair

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Key|string|False|The integration key|
|Name|string|False|The name|

#### location

|Name|Type|Required|Description|
|----|----|--------|-----------|
|City|string|False|The city name|
|Country|string|False|The country name|
|State|string|False|The state, county, province, or prefecture|

#### log

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access Device|accessDevice|False|Browser, plugin, and operating system information for the endpoint used to access the Duo-protected resource. Values present only when the application accessed features Duo's inline browser prompt|
|Action|string|False|The type of change that was performed|
|Adaptive Trust Assessments|adaptiveTrustAssessments|False|Risk-based authentication information. Values present only when the application accessed features Duo's inline browser prompt and has a Duo Risk-Based Authentication policy applied|
|Alias|string|False|The username alias used to log in. No value if the user logged in with their username instead of a username alias|
|Application|keyNamePair|False|Information about the application accessed|
|Auth Device|authDevice|False|Information about the device used to approve or deny authentication|
|Bypass Status Enabled|integer|False|An integer indicating the Unix timestamp in milliseconds when bypass status was enabled for the user or group|
|Description|string|False|String detailing what changed|
|Email|string|False|The email address of the user|
|Enabled By|keyNamePair|False|The application or the administrator that enabled bypass status|
|Enabled For|keyNamePair|False|The user or group with bypass status|
|Event Type|string|False|The type of activity logged|
|Explanations|[]explanation|False|An array of objects describing why Trust Monitor surfaced the event|
|Factor|string|False|The authentication factor|
|From Common Netblock|boolean|False|A boolean describing if this event was created from a common IP netblock|
|From New User|boolean|False|A boolean describing if this event was created for a new user|
|ISO8601 Timestamp|string|False|ISO8601 timestamp of the event|
|Log Type|string|False|Type of the log|
|Low Risk IP|boolean|False|A boolean describing if this event was created from an IP address identified in the Risk Profile configuration as a low risk IP address|
|Object|string|False|The object that was acted on|
|OOD Software|string|False|If authentication was denied due to out-of-date software, shows the name of the software|
|Priority Event|boolean|False|A boolean describing if the event matches the Risk Profile configuration|
|Priority Reasons|[]priorityReason|False|An array of objects describing how the event matches the Trust Monitor Risk Profile configuration|
|Reason|string|False|The reason for the authentication attempt result|
|Result|string|False|The result of the authentication attempt. One of: 'success', 'denied', 'failure', 'error', or 'fraud'|
|Sekey|string|False|The unique identifier for this event|
|State|string|False|A string describing the state of the event|
|State Updated Timestamp|integer|False|An integer indicating the Unix timestamp in milliseconds of the last change to the state of the event|
|Surfaced Auth|authLog|False|An object which represents the actual authentication|
|Surfaced Timestamp|integer|False|An integer indicating the Unix timestamp in milliseconds when the event was surfaced by Trust Monitor|
|Timestamp|number|False|An integer indicating the Unix timestamp of the event|
|Triage Event URI|string|False|A string representing the URI of the security event, which a Duo administrator can use to view and process the surfaced event in the Duo Admin Panel|
|Triaged As Interesting|boolean|False|A boolean describing if this event was triaged as being interesting or not interesting|
|Transaction ID|string|False|The transaction ID of the event|
|Type|string|False|The type of event|
|User|authlogUser|False|Information about the authenticating user|
|Username|string|False|The full name of the administrator who performed the action|

#### phoneUser

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Activated|boolean|False|Whether the phone has already been activated for Duo Mobile|
|Capabilities|[]string|False|List of factors that can be used with the phone|
|Encrypted|string|False|The encryption status of an Android or iOS device file system|
|Extension|string|False|Extension of the phone|
|Fingerprint|string|False|Whether an Android or iOS phone is configured for biometric verification|
|Last Seen|string|False|An integer indicating the timestamp of the last contact between Duo's service and the activated Duo Mobile app installed on the phone|
|Model|string|False|The phone's model|
|Name|string|False|Free-form label for the phone|
|Number|string|False|Number|
|Phone ID|string|False|The phone's ID|
|Platform|string|False|The phone platform|
|Postdelay|string|False|The time (in seconds) to wait after the extension is dialed and before the speaking the prompt|
|Predelay|string|False|The time (in seconds) to wait after the number picks up and before dialing the extension|
|Screen Lock|string|False|Whether screen lock is enabled on an Android or iOS phone|
|SMS Passcodes Sent|boolean|False|Whether the SMS passcodes has been sent to this phone|
|Type|string|False|Whether an iOS or Android device is jailbroken or rooted|
|Type|string|False|The type of phone|

#### priorityReason

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Label|string|False|The label of the priority reason for the event's match|
|Type|string|False|The type of priority reason for the event's match|

#### token

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Admins|[]object|False|A list of administrators associated with this hardware token|
|Serial|string|False|The serial number of the hardware token|
|Token ID|string|False|The hardware token's unique ID|
|Type|string|False|The type of hardware token|
|Users|[]object|False|A list of end users associated with this hardware token|

#### trustAssessmentObject

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Features Version|string|False|The feature version for the risk-based authentication trust assessment|
|Model Version|string|False|The model version for the risk-based authentication trust assessment|
|Policy Enabled|boolean|False|Denotes if risk-based authentication was enabled by the policy under which the trust assessment was evaluated|
|Reason|string|False|The reason behind the trust assessment level|
|Trust Level|string|False|The trust assessment level. Can be one of: ERROR, LOW, NORMAL, UNKNOWN, or UNSET|

#### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Alias 1|string|False|The user's username alias 1|
|Alias 2|string|False|The user's username alias 2|
|Alias 3|string|False|The user's username alias 3|
|Alias 4|string|False|The user's username alias 4|
|Aliases|object|False|The user's aliases|
|Created|integer|False|The user's creation date as a UNIX timestamp|
|Email|string|False|The user's email address|
|First Name|string|False|The user's given name|
|Groups|[]group|False|List of groups to which this user belongs|
|Is Enrolled|boolean|False|Whether the user has a phone, hardware token, U2F token, WebAuthn security key, or other WebAuthn method available for authentication|
|Last Directory Sync|integer|False|An integer indicating the last update to the user via directory sync as a Unix timestamp, or null if the user has never synced with an external directory or if the directory that originally created the user has been deleted from Duo|
|Last Login|integer|False|An integer indicating the last time this user logged in, as a Unix timestamp, or null if the user has not logged in|
|Last Name|string|False|The user's surname|
|Notes|string|False|Notes about this user|
|Phones|[]phoneUser|False|A list of phones that this user can use|
|Real Name|string|False|The user's real name or full name|
|Status|string|False|The user's status|
|Tokens|[]token|False|A list of tokens that this user can use|
|User ID|string|False|The user's ID|
|Username|string|False|The user's username|
|Web Auth Credentials|[]webauthnaredentials|False|A list of WebAuthn authenticators that this user can use|

#### webauthnaredentials

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Credential Name|string|False|Free-form label for the WebAuthn credential|
|Credential Name|integer|False|The date the WebAuthn credential was registered in Duo|
|Label|string|False|Indicates the type of WebAuthn credential|
|User|object|False|Selected information about the end user attached to the WebAuthn credential|
|WebAuthnKey|string|False|The WebAuthn credential's registration identifier|


## Troubleshooting

Many actions in this plugin take a User ID as input. A User ID is not the username - instead it's a unique identifier e.g. DU9I6T0F7R2S1J4XZHHA.
A User ID can be obtained by passing a username to the Get User Status action.

# Version History

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

* [Duo Security](https://duo.com/)
* [Duo Admin API](https://duo.com/docs/adminapi)

## References

* [Duo Security](https://duo.com/)
* [Duo Admin API](https://duo.com/docs/adminapi)
