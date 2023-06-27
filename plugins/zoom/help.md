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
* API credentials for OAuth 2.0:
  * Requires account ID as well as client ID and secret from a Server-to-Server OAuth app in the Zoom Marketplace.
  * Server-to-Server OAuth app has the `report:read:admin` scope enabled.
    
# Supported Product Versions
  
* Zoom API v2.10  

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|account_id|string|None|True|Zoom app account ID, required for OAuth authentication|None|dBs0x4Kf7HuIK0LLbzMduW|
|authentication_retry_limit|integer|5|True|How many times to retry authentication to Zoom before failing, required for OAuth authentication|None|5|
|client_id|string|None|True|Zoom app client ID, required for OAuth authentication|None|{"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"}|
|client_secret|credential_secret_key|None|True|Zoom app client secret, required for OAuth authentication|None|9de5069c5afe602b2ea0a04b66beb2c0|
  
Example input:

```
{
  "account_id": "dBs0x4Kf7HuIK0LLbzMduW",
  "authentication_retry_limit": 5,
  "client_id": "{"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"}",
  "client_secret": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```  

## Technical Details

### Actions
  

#### Create User
  
Create user associated to account  

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|create|True|Specify how to create the new user|['create', 'autoCreate', 'custCreate', 'ssoCreate']|create|
|email|string|None|True|Email address of user|None|user@example.com|
|first_name|string|None|False|First name of user|None|John|
|last_name|string|None|True|Last name of user|None|Smith|
|type|string|None|True|User type|['Basic', 'Licensed']|Basic|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|email|string|True|Email address of user|user@example.com|
|first_name|string|False|First name of user|John|
|id|string|True|User identifier|T9ti3NBxR42swGKrqABGig|
|last_name|string|True|Last name of user|Smith|
|type|integer|True|User type|1|

Example output:

```
{
  "email": "user@example.com",
  "first_name": "John",
  "id": "T9ti3NBxR42swGKrqABGig",
  "last_name": "Smith",
  "type": 1
}
```  

#### Delete User
  
Delete or disassociate user from account  

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Success|True|

Example output:

```
{
  "success": true
}
```  

#### Get User
  
Get user in Zoom account  

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|user_id|string|None|True|The user identifier or email address|None|user@example.com|
  
Example input:

```
{
  "user_id": "user@example.com"
}
```  

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|user|True|User details|{}|

Example output:

```
{
  "user": {}
}
```
### Triggers
  

#### User Activity Event
  
Poll for user activity events  

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|activity_type|string|None|True|Type of user activity to match event|['Sign in', 'Sign out', 'All']|All|
  
Example input:

```
{
  "activity_type": "All"
}
```  

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user_activity|user_activity|False|User Activity|{}|

Example output:

```
{
  "user_activity": {}
}
```
### Tasks
  

#### Monitor Sign in and out Activity
  
Monitor sign in and out activity  

##### Input
  
*This task does not contain any inputs.*  

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|activity_logs|[]user_activity|True|All activity logs within the specified time range|[]|

Example output:

```
[
  {
    "client_type": "Browser",
    "email": "user@example.com",
    "ip_address": "192.0.2.1",
    "time": "2019-09-15T19:13:41Z",
    "type": "Sign out",
    "version": "5.9.1.2581"
  }
]
```

### Custom Types
  
**user_activity**  

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Client Type|string|None|False|The type of client of the user's device|Browser|
|Email|string|None|True|Email address of the user used for the activity|user@example.com|
|IP Address|string|None|True|The IP address of the user's device|192.0.2.0|
|Time|string|None|True|Time during which the activity occurred in 'yyyy-mm-ddThh:mm:ssZ' format|2023-05-21 20:15:01+00:00|
|Type|string|None|True|The type of activity|Sign in|
|Version|string|None|False|The version of the client of the user's device|-|
  
**user**  

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Account ID|string|None|False|Account ID of user|T9ti3NBxR42swGKrqABGig|
|Created At|string|None|False|Creation datetime of user|2023-06-22 12:26:02+00:00|
|Department|string|None|False|Department of user|example department|
|Email|string|None|False|Email address of user|user@example.com|
|First Name|string|None|False|First name of user|John|
|Web Group IDs|[]string|None|False|IDs of the web groups user belongs to|[]|
|Host Key|string|None|False|User's host key|123321|
|ID|string|None|True|User identifier|T9ti3NBxR42swGKrqABGig|
|IM Group IDs|[]string|None|False|IM IDs of the groups user belongs to|[]|
|JID|string|None|False|JID of user|T9ti3NBxR42swGKrqABGig@xmpp.zoom.us|
|Language|string|None|False|Language of user|en-US|
|Last Login Time|string|None|False|Last login datetime of user|2023-06-21 13:41:14+00:00|
|Last Name|string|None|False|Last name of user|Smith|
|Personal Meeting URL|string|None|False|Personal meeting URL of user|https://zoom.us/j/2315556661?pwd=SGDgdgGRG434w5SvVre09|
|Phone Country|string|None|False|Phone country of user|US|
|Phone Number|string|None|False|Phone number of user|555-0100|
|Personal Meeting ID|integer|None|False|Personal meeting ID|2315556661|
|Role Name|string|None|False|Role name of user|Member|
|Status|string|None|False|Status of user|active|
|Timezone|string|None|False|Timezone of user|Europe/London|
|Type|integer|None|False|User type|1|
|Use Personal Meeting ID|boolean|None|False|Use Personal meeting ID for instant meetings|False|
|Verified|integer|None|False|Whether the user is verified or not|1|
  

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 4.0.2 - Reordered status checks to avoid JSON parsing issue with 204s | Added examples to spec file and help.md
* 4.0.1 - Return Zoom API status codes in Monitor Sign in And Out Activity task state
* 4.0.0 - Fix time boundary checking in Monitor Sign in And Out Activity task by tracking last request time instead of latest event time | Remove JWT authentication
* 3.0.0 - Add back JWT authentication in addition to OAuth (please note JWT will be removed from the Zoom API in June 2023) | Improve OAuth logic to help prevent infinite looping
* 2.1.0 - Create user: Removed redundant enum option from `type` input | Added unit tests | Improve authentication logic
* 2.0.0 - Update connection for latest Zoom API authentication | Add Monitor Sign In and Out Activity task
* 1.0.0 - Initial plugin

# Links

* [Zoom](https://zoom.us/)

## References

* [Zoom](https://zoom.us/)
* [Zoom API Documentation](https://marketplace.zoom.us/docs/api-reference/introduction)
