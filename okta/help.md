# Description

[Okta](https://www.okta.com/) is a SSO and account lifecycle management provider that allows companies
to integrate their central user account system with a wide variety of other applications and services.

# Key Features

* Single Sign On User management

# Requirements

* API Key
* Okta server

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|okta_key|credential_secret_key|None|True|Okta key|None|
|okta_url|string|None|True|Okta Domain e.g. dev-114295-admin.oktapreview.com|None|

## Technical Details

### Actions

#### Get Okta User Factors

This action returns an object containing all of a user's factors for MFA.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|True|User ID to get factors for|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|factors|[]object|False|Obbject containing all the factors of a user for MFA|

Example output:

```
[
    {
        "id": "opfpfac5jbFkZppdt0h7",
        "factorType": "push",
        "provider": "OKTA",
        "vendorName": "OKTA",
        "status": "ACTIVE",
        "created": "2020-01-24T14:52:55.000Z",
        "lastUpdated": "2020-01-24T14:55:18.000Z",
        "profile": {
            "credentialId": "user@example.com",
            "deviceType": "SmartPhone_IPhone",
            "keys": [
                {
                    "kty": "EC",
                    "use": "sig",
                    "kid": "default",
                    "x": "Oec4otjngqynTnI37AncY4tWeSE2WxpG98s5sQXxnUM",
                    "y": "zVlJEuKcq8LphPIFS5A-4OMkfHTviLImx7WBsDd7E14",
                    "crv": "P-256"
                }
            ],
            "name": "iPhone XR",
            "platform": "IOS",
            "version": "13.3"
        },
        "_links": {
            "self": {
                "href": "https://company.oktapreview.com/api/v1/users/00up95jz8uU1Zs6T60h7/factors/opfpfac5jbFkZppdt0h7",
                "hints": {
                    "allow": [
                        "GET",
                        "DELETE"
                    ]
                }
            },
            "verify": {
                "href": "https://company.oktapreview.com/api/v1/users/00up95jz8uU1Zs6T60h7/factors/opfpfac5jbFkZppdt0h7/verify",
                "hints": {
                    "allow": [
                        "POST"
                    ]
                }
            },
            "user": {
                "href": "https://company.oktapreview.com/api/v1/users/00up93jz8uU1Zs6T60h7",
                "hints": {
                    "allow": [
                        "GET"
                    ]
                }
            }
        }
    }
]
```

#### Push MFA Challenge

This action pushes a MFA challenge to a user's device and waits for a success or rejection.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|factor_id|string|None|True|Factor ID of the user to push verification to|None|
|user_id|string|None|True|User ID to push verification to|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|factor_status|string|False|User factor status|

Example Output:

```
{
  "factor_status": "SUCCESS"
}
```

#### Suspend User

This action can be used to suspend a user from the Okta system. The user will retain
membership and permissions as currently configured, but be unable to access the system
as a whole.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|The email of the employee to suspend|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|email|string|False|The email of the Okta user|
|success|boolean|True|Whether suspension was successful|
|user_id|string|False|The user ID of the Okta user|

Example output:

```
{
  "user_id": "00uftwxx6wj9AripB0h7",
  "email": "user@example.com",
  "success": true
}
```

When the user is not found, the action returns:

```
{
  "success": false
}
```

#### Reset Factors

This action is used to reset all multifactors for a user by email.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|The email of the employee to reset factors|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|email|string|False|The email of the Okta user|
|success|boolean|True|Whether the reset was successful|
|user_id|string|False|The user ID of the Okta user|

Example output:

```
{
  "user_id": "00uftwxx6wj9AripB0h7",
  "email": "user@example.com",
  "success": true
}
```

When the user is not found or the user has no enrolled factors:

```
{
  "success": false
}
```

#### Deactivate User

This action can be used to deactivate / deprovision a user from the Okta system. In addition
to losing the ability to log in, the user will be removed from all configured applications
and lose all configured settings. This is a non-reversible, destructive operation. This
action is also considered asynchronous by the Okta API, meaning there is some delay between
the API returning a successful result and the actual deactivation / deprovisioning of a user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|The email of the employee to deactivate|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|email|string|False|The email of the Okta user|
|success|boolean|True|Whether deactivation was successful|
|user_id|string|False|The user ID of the Okta user|

Example output:

```
{
  "user_id": "00uftwxx6wj9AripB0h7",
  "email": "user@example.com",
  "success": true
}
```

When the user is not found, the action returns:

```
{
  "success": false
}
```

#### Delete User

This action is used to delete a user. If a user is not deprovisioned, this will deprovision a user, a second delete will be needed to remove the user. Warning: This action annot be recovered from.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|send_admin_email|boolean|False|True|Sends a deactivation email to the administrator if true. Default value is false|None|
|user_email|string|None|True|The email of the user to delete|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether deactivation was successful|

Example output:

```
{
  "success": false
}
```

#### Unsuspend User

This action is used to unsuspend a user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|The email of the Okta user|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|email|string|False|The email of the Okta user|
|success|boolean|True|Whether unsuspension was successful|
|user_id|string|False|The user ID of the Okta user|

Example output:

```
{
  "user_id": "00uftwxx6wj9AripB0h7",
  "email": "user@example.com",
  "success": true
}
```

When the user is not found, the action returns:

```
{
  "success": false
}
```

#### Get User

This action is used to obtain information about a user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|The email of the user to obtain information about|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|_links|_links|False|Links|
|activated|string|False|When the user was activated, e.g. 2013-07-02T21:36:25.344Z|
|created|string|False|When the user was created, e.g. 2013-07-02T21:36:25.344Z|
|credentials|credentials|False|Credentials|
|found|boolean|True|Whether user was found|
|id|string|False|User ID|
|lastLogin|string|False|When the last login for the user was, e.g. 2013-07-02T21:36:25.344Z|
|lastUpdated|string|False|When the user was last updated, e.g. 2013-07-02T21:36:25.344Z|
|passwordChanged|string|False|When the password was changed, e.g. 2013-07-02T21:36:25.344Z|
|profile|profile|False|Profile|
|status|string|False|Status|
|statusChanged|string|False|When the status of the user changed, e.g. 2013-07-02T21:36:25.344Z|

Example output:

```
{
  "found": True
  "status": "ACTIVE",
  "profile": {
    "firstName": "Jon",
    "lastName": "Schipp",
    "login": "user@example.com",
    "email": "user@example.com"
  },
  "passwordChanged": "2018-07-28T18:48:52.000Z",
  "created": "2018-07-28T17:24:41.000Z",
  "activated": "2018-07-28T18:47:24.000Z",
  "lastUpdated": "2018-07-28T18:58:06.000Z",
  "_links": {
    "suspend": {
      "href": "https://dev-114295.oktapreview.com/api/v1/users/00uftwxx6wj9AripB0h7/lifecycle/suspend",
      "method": "POST"
    },
    "forgotPassword": {
      "href": "https://dev-114295.oktapreview.com/api/v1/users/00uftwxx6wj9AripB0h7/credentials/forgot_password",
      "method": "POST"
    },
    "self": {
      "href": "https://dev-114295.oktapreview.com/api/v1/users/00uftwxx6wj9AripB0h7"
    },
    "expirePassword": {
      "href": "https://dev-114295.oktapreview.com/api/v1/users/00uftwxx6wj9AripB0h7/lifecycle/expire_password",
      "method": "POST"
    },
    "deactivate": {
      "href": "https://dev-114295.oktapreview.com/api/v1/users/00uftwxx6wj9AripB0h7/lifecycle/deactivate",
      "method": "POST"
    },
    "changePassword": {
      "href": "https://dev-114295.oktapreview.com/api/v1/users/00uftwxx6wj9AripB0h7/credentials/change_password",
      "method": "POST"
    },
    "changeRecoveryQuestion": {
      "href": "https://dev-114295.oktapreview.com/api/v1/users/00uftwxx6wj9AripB0h7/credentials/change_recovery_question",
      "method": "POST"
    },
    "resetPassword": {
      "href": "https://dev-114295.oktapreview.com/api/v1/users/00uftwxx6wj9AripB0h7/lifecycle/reset_password",
      "method": "POST"
    }
  },
  "lastLogin": "2018-07-28T18:48:52.000Z",
  "credentials": {
    "recovery_question": {
      "question": "What is the food you least liked as a child?"
    },
    "password": {},
    "emails": [
      {
        "status": "VERIFIED",
        "type": "PRIMARY",
        "value": "user@example.com"
      }
    ],
    "provider": {
      "type": "OKTA",
      "name": "OKTA"
    }
  },
  "id": "00uftwxx6wj9AripB0h7",
  "statusChanged": "2018-07-28T18:58:06.000Z"
}
```

When the user is not found, the action returns:

```
{
  "found": false
}
```

#### Remove User from Group

This action is used to remove a user from an existing group.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|The email of the Okta user|None|
|group_id|string|None|True|The ID of the group to which the user should be added|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether the add was successful|
|user_id|string|False|The user ID of the Okta user|

Example output:

```
{
  "user_id": "00uftx2ontnpbTJ4M0h7",
  "success": true
}
```

#### Add User to Group

This action is used to add a user to an existing group.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|The email of the Okta user|None|
|group_id|string|None|True|The ID of the group to which the user should be added|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether the add was successful|
|user_id|string|False|The user ID of the Okta user|

Example output:

```
{
  "user_id": "00uftx2ontnpbTJ4M0h7",
  "success": true
}
```

#### List Groups

This action is used to list available groups.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|string|None|False|Query to list groups, otherwise all groups will be returned|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|groups|[]group|False|List of groups|
|success|boolean|True|Whether groups were found|

Example output:

```
{
  "success": true,
  "groups": [
    {
      "name": "Cool",
      "created": "2018-07-28T20:28:20.000Z",
      "objectClass": [
        "okta:user_group"
      ],
      "lastUpdated": "2018-07-28T20:28:20.000Z",
      "_links": {
        "logo": [
          {
            "href": "https://op1static.oktacdn.com/assets/img/logos/groups/okta-medium.d7fb831bc4e7e1a5d8bd35dfaf405d9e.png",
            "type": "image/png",
            "name": "medium"
          },
          {
            "href": "https://op1static.oktacdn.com/assets/img/logos/groups/okta-large.511fcb0de9da185b52589cb14d581c2c.png",
            "type": "image/png",
            "name": "large"
          }
        ],
        "apps": {
          "href": "https://dev-114295.oktapreview.com/api/v1/groups/00gftwyoqyVBvcpdn0h7/apps"
        },
        "users": {
          "href": "https://dev-114295.oktapreview.com/api/v1/groups/00gftwyoqyVBvcpdn0h7/users"
        }
      },
      "lastMembershipUpdated": "2018-07-28T21:15:17.000Z",
      "type": "OKTA_GROUP",
      "id": "00gftwyoqyVBvcpdn0h7",
      "description": "Cool people"
    }
  ]
}
```

When no groups are found, the action returns:

```
{
  "success": false,
  "groups": []
}
```

#### Assign User to Application for Provisioning

This action is used to assign a user to an application for SSO and provisioning.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|applicationId|string|None|True|Application ID|None|
|appuser|object|None|False|Application user model as JSON object, see https://developer.okta.com/docs/api/resources/apps#application-user-model|None|

`appuser` accepts a [application user model](https://developer.okta.com/docs/api/resources/apps#application-user-model) JSON object.

Example input:

```
{
  "id": "00u15s1KDETTQMQYABRL",
  "scope": "USER",
  "credentials": {
    "userName": "user@example.com"
  },
  "profile": {
      "salesforceGroups": [
        "Employee"
      ],
      "role": "Developer",
      "profile": "Standard User"
  }
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|object|True|Result|

Example output:

```
```

#### Create User

This action is used to create a new user.

##### Input

The profile object is a required input and is defined by Okta as [profile properties for a user](https://developer.okta.com/docs/api/resources/users#profile-object).
e.g.: `{ "firstName": "Isaac", "lastName": "Brock", "email": "user@example.com", "login": "user@example.com", "mobilePhone": "555-415-1337" }`

If configuring the `provider` and/or `recovery_question` inputs, for each used, their respective fields must be completed otherwise Okta will return an error.
This action will attempt to prevent that be removing the entire input if it detects a missing field in that input.

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|activate|boolean|True|True|Executes activation lifecycle operation when creating the user|None|
|credentials|credentials_input|None|False|Credentials for user|None|
|groupIds|[]string|None|False|IDs of groups that user will be immediately added to at time of creation|None|
|nextLogin|boolean|None|True|Change password next time the user logs in|None|
|profile|object|None|True|Profile properties for user|None|
|provider|boolean|False|True|Indicates whether to create a user with a specified authentication provider|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|_links|_links|False|Links|
|activated|string|False|When the user was activated, e.g. 2013-07-02T21:36:25.344Z|
|created|string|False|When the user was created, e.g. 2013-07-02T21:36:25.344Z|
|credentials|credentials|False|Credentials|
|id|string|False|User ID|
|lastLogin|string|False|When the last login for the user was, e.g. 2013-07-02T21:36:25.344Z|
|lastUpdated|string|False|When the user was last updated, e.g. 2013-07-02T21:36:25.344Z|
|passwordChanged|string|False|When the password was changed, e.g. 2013-07-02T21:36:25.344Z|
|profile|profile|False|Profile|
|status|string|False|Status|
|statusChanged|string|False|When the status of the user changed, e.g. 2013-07-02T21:36:25.344Z|

Example output:

```
{
  "id": "00ug5xak4uqrOrj8Q0h7",
  "status": "STAGED",
  "created": "2018-09-06T19:00:06.000Z",
  "lastUpdated": "2018-09-06T19:00:06.000Z",
  "profile": {
    "firstName": "Isaac",
    "lastName": "Brock",
    "mobilePhone": "555-415-1337",
    "login": "user@example.com",
    "email": "user@example.com"
  },
  "credentials": {
    "emails": [
      {
        "value": "user@example.com",
        "status": "VERIFIED",
        "type": "PRIMARY"
      }
    ],
    "provider": {
      "type": "OKTA",
      "name": "OKTA"
    }
  },
  "_links": {
    "activate": {
      "href": "https://dev-114295.oktapreview.com/api/v1/users/00ug5xak4uqrOrj8Q0h7/lifecycle/activate",
      "method": "POST"
    },
    "self": {
      "href": "https://dev-114295.oktapreview.com/api/v1/users/00ug5xak4uqrOrj8Q0h7"
    }
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Actions may fail depending on the state of the resource you attempt to operate over.
They will return a best-effort message indicating why the Okta API responded the way it
did when possible. Depending on the API endpoint, this message is either provided
by Okta themselves, or constructed by the plugin based on the information it has at hand.

# Version History

* 3.3.0 - New actions Get Factors and Send Push
* 3.2.2 - Change docker image from `komand/python-2-plugin:2` to `komand/python-3-37-slim-plugin:3` | Use input and output constants | Changed variables names to more readable | Added "f" strings | Removed duplicated code
* 3.2.1 - New spec and help.md format for the Hub
* 3.2.0 - New action Delete User
* 3.1.2 - Update connection test
* 3.1.1 - Update descriptions
* 3.1.0 - New action Reset Factors
* 3.0.0 - Rename "Remove User to Group" action to "Remove User from Group"
* 2.1.0 - Improved connection code | New action Create User
* 2.0.0 - Update to new secret key credential type
* 1.1.0 - Added new Get User, Unsuspend User, Add User to Group, and List Groups actions
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Okta API Spec](http://developer.okta.com/docs/api/resources)
