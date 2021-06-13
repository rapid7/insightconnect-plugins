# Description

[Zoom](https://zoom.us) is a cloud platform for video and audio conferencing, chat, and webinars. The Zoom plugin allows 
you to add and remove users as part of of workflow, while also providing the ability to trigger workflows on new user 
sign-in and sign-out activity events.

This plugin uses the [Zoom API](https://marketplace.zoom.us/docs/api-reference/introduction) and requires a Pro, 
Business, or Enterprise plan.

# Key Features

* Trigger workflows on user sign-in and sign-out activity events
* Add and remove user accounts to automate provisioning/deprovisioning of users

# Requirements

* Must have Zoom Pro, Business, or Enterprise plan to support REST API
* Requires JWT credentials from Zoom App marketplace

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|JWT API Key|None|abcdefgABCDEFG12345678|
|secret|credential_secret_key|None|True|JWT Secret|None|abcdefgABCDEFG123456789abcdefgABCDEF|

Example input:

```
{
  "api_key": "abcdefgABCDEFG12345678",
  "secret": "abcdefgABCDEFG123456789abcdefgABCDEF"
}
```

See the Zoom [Create a JWT App](https://marketplace.zoom.us/docs/guides/build/jwt-app) documentation for generating a 
JWT App and obtaining your API key and secret.

## Technical Details

### Actions

#### Create User

This action is used to create user associated to account.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|create|True|Specify how to create the new user|['create', 'autoCreate', 'custCreate', 'ssoCreate']|create|
|email|string|None|True|Email address of user|None|user@example.com|
|first_name|string|None|False|First name of user|None|John|
|last_name|string|None|True|Last name of user|None|Smith|
|type|string|None|True|User type|['Basic', 'Licensed', 'On-prem']|Basic|

Example input:

```
{
  "action": "create",
  "email": "user@example.com",
  "first_name": "John",
  "last_name": "Smith",
  "type": "Basic"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|email|string|True|Email address of user|
|first_name|string|False|First name of user|
|id|string|True|User identifier|
|last_name|string|True|Last name of user|
|type|integer|True|User type|

Example output:

```
{
  "id": "oZSx8rYaTPW8Ibjzy8nKFA",
  "last_name": "John",
  "type": 1,
  "email": "user@example.com",
  "first_name": "Smith"
}
```

#### Delete User

This action is used to delete or disassociate user from account.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|None|True|Specify how to delete the user. To delete pending user, use disassocaite|['delete', 'disassociate']|delete|
|id|string|None|True|The user identifier or email address|None|user@example.com|
|transfer_email|string|None|False|Email to transfer meetings, webinars, or recordings|None|user@example.com|
|transfer_meetings|boolean|False|False|Whether to transfer meetings to defined transfer email|None|False|
|transfer_recordings|boolean|False|False|Whether to transfer recordings to defined transfer email|None|False|
|transfer_webinars|boolean|False|False|Whether to transfer webinars to defined transfer email|None|False|

Example input:

```
{
  "action": "delete",
  "id": "user@example.com",
  "transfer_email": "user@example.com",
  "transfer_meetings": false,
  "transfer_recordings": false,
  "transfer_webinars": false
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Success|

Example output:

```
{
  "success": true
}
```

#### Get User

This action is used to get user in Zoom account.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|user_id|string|None|True|The user identifier or email address|None|user@example.com|

Example input:

```
{
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|user|True|User details|

Example output:

```
{
  "user": {
    "account_id": "",
    "role_name": "",
    "id": "oZSx8rYaTPW8Ibjzy8nKFA",
    "im_group_ids": [],
    "phone_country": "",
    "type": 1,
    "verified": 0,
    "created_at": "2020-06-03T21:30:52Z",
    "first_name": "",
    "language": "",
    "phone_number": "",
    "group_ids": [],
    "last_name": "",
    "status": "pending"
  }
}
```

### Triggers

#### User Activity Event

This trigger is used to poll for user activity events.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|activity_type|string|None|True|Type of user activity to match event|['Sign in', 'Sign out', 'All']|All|

Example input:

```
{
  "activity_type": "All"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user_activity|user_activity|False|User Activity|

Example output:

```
{
  "user_activity": {
    "email": "user@example.com", 
    "time": "2020-06-05T16:51:28Z", 
    "type": "Sign in", 
    "ip_address": "198.51.100.100", 
    "client_type": "Browser", 
    "version": "-"
  }
}
```

### Custom Output Types

#### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Account ID|string|False|Account ID of user|
|Created At|string|False|Creation datetime of user|
|Department|string|False|Department of user|
|Email|string|False|Email address of user|
|First Name|string|False|First name of user|
|Web Group IDs|[]string|False|IDs of the web groups user belongs to|
|Host Key|string|False|User's host key|
|ID|string|True|User identifier|
|IM Group IDs|[]string|False|IM IDs of the groups user belongs to|
|JID|string|False|JID of user|
|Language|string|False|Language of user|
|Last Login Time|string|False|Last login datetime of user|
|Last Name|string|False|Last name of user|
|Personal Meeting URL|string|False|Personal meeting URL of user|
|Phone Country|string|False|Phone country of user|
|Phone Number|string|False|Phone number of user|
|Personal Meeting ID|integer|False|Personal meeting ID|
|Role Name|string|False|Role name of user|
|Status|string|False|Status of user|
|Timezone|string|False|Timezone of user|
|Type|integer|False|User type|
|Use Personal Meeting ID|boolean|False|Use Personal meeting ID for instant meetings|
|Verified|integer|False|Whether the user is verified or not|

#### user_activity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Client Type|string|False|The type of client of the user's device|
|Email|string|True|Email address of the user used for the activity|
|IP Address|string|True|The IP address of the user's device|
|Time|string|True|Time during which the activity occurred|
|Type|string|True|The type of activity|
|Version|string|False|The version of the client of the user's device|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Zoom](https://zoom.us/)
* [Zoom API Documentation](https://marketplace.zoom.us/docs/api-reference/introduction)
* [Zoom JWT Auth Documentation](https://marketplace.zoom.us/docs/guides/auth/jwt)
