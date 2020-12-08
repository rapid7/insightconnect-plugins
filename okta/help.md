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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|okta_key|credential_secret_key|None|True|Okta key|None|None|
|okta_url|string|None|True|Okta Domain e.g. example.okta.com|None|None|

## Technical Details

### Actions

#### Update Blacklist Zones

This action is used to block or unblock address or network by adding or removing from a blacklist network zone.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|IP address, Network range, or CIDR to block or unblock|None|198.51.100.1|
|blacklist_state|boolean|True|False|True to block, false to unblock|None|True|
|name|string|None|True|Name of blacklist zone|None|InsightConnect Blacklist Zone|

Example input:

```
{
  "address": "198.51.100.1",
  "blacklist_state": true,
  "name": "InsightConnect Blacklist Zone"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|zone_list|zone_list|True|Updated zone list|

Example output:

```
{
  "zone_list": {
    "_links": {
      "deactivate": {
        "hints": {
          "allow": [
            "POST"
          ]
        },
        "href": "https://example.okta.com/api/v1/zones/nzohxvr9QzHuWqXI65d7/lifecycle/deactivate"
      },
      "self": {
        "hints": {
          "allow": [
            "GET",
            "PUT",
            "DELETE"
          ]
        },
        "href": "https://example.okta.com/api/v1/zones/nzohxvr9QzHuWqXI65d7"
      }
    },
    "created": "2020-11-01T01:00:47.000Z",
    "gateways": [
      {
        "type": "RANGE",
        "value": "1.1.1.1-1.1.1.1"
      },
      {
        "type": "RANGE",
        "value": "1.1.2.3-1.1.2.5"
      }
    ],
    "id": "nzohxvr9QzHuWqXI65d5",
    "lastUpdated": "2020-11-01T23:36:53.000Z",
    "name": "testzone",
    "proxies": null,
    "status": "ACTIVE",
    "system": false,
    "type": "IP"
  }
}

```

#### Get Okta User Factors

This action returns an object containing all of a user's factors for MFA.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|user_id|string|None|True|User ID to get factors for|None|None|

Example input:

```
{
  "user_id" : "opfpfac5jbFkZppdt0h7"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|factor_id|string|None|True|Factor ID of the user to push verification to|None|None|
|user_id|string|None|True|User ID to push verification to|None|None|

Example input:

```
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|The email of the employee to suspend|None|None|

Example input:

```
{
  "email" : "user@example.com"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|The email of the employee to reset factors|None|None|

Example input:

```
{
  "email" : "user@example.com"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|The email of the employee to deactivate|None|None|

Example input:

```
{
  "email": "user@example.com"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|send_admin_email|boolean|False|True|Sends a deactivation email to the administrator if true. Default value is false|None|None|
|user_email|string|None|True|The email of the user to delete|None|None|

Example input:

```
{
  "send_admin_email": True
  "user_email": "user@example.com"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|The email of the Okta user|None|None|

Example input:

```
{
  "email": "user@example.com"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|The email of the user to obtain information about|None|None|

Example input:

```
{
  "email": "user@example.com"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|The email of the Okta user|None|None|
|group_id|string|None|True|The ID of the group to which the user should be added|None|None|

Example input:

```
{
  "email": "user@example.com"
  "group_id": "00g41ix8hKbsu74Ca4x6"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|email|string|None|True|The email of the Okta user|None|None|
|group_id|string|None|True|The ID of the group to which the user should be added|None|None|

Example input:

```
{
  "email": "user@example.com"
  "group_id": "00g41ix8hKbsu74Ca4x6"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|False|Query to list groups, otherwise all groups will be returned|None|None|

Example input:

```
{
  "query": "group name here"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|applicationId|string|None|True|Application ID|None|None|
|appuser|object|None|False|Application user model as JSON object, see https://developer.okta.com/docs/api/resources/apps#application-user-model|None|None|

`appuser` accepts a [application user model](https://developer.okta.com/docs/api/resources/apps#application-user-model) JSON object.

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|object|True|Result|

Example output:

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

#### Create User

This action is used to create a new user.

##### Input

The profile object is a required input and is defined by Okta as [profile properties for a user](https://developer.okta.com/docs/api/resources/users#profile-object).
e.g.: `{ "firstName": "Isaac", "lastName": "Brock", "email": "user@example.com", "login": "user@example.com", "mobilePhone": "555-415-1337" }`

If configuring the `provider` and/or `recovery_question` inputs, for each used, their respective fields must be completed otherwise Okta will return an error.
This action will attempt to prevent that be removing the entire input if it detects a missing field in that input.

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|activate|boolean|True|True|Executes activation lifecycle operation when creating the user|None|None|
|credentials|credentials_input|None|False|Credentials for user|None|None|
|groupIds|[]string|None|False|IDs of groups that user will be immediately added to at time of creation|None|None|
|nextLogin|boolean|None|True|Change password next time the user logs in|None|None|
|profile|object|None|True|Profile properties for user|None|None|
|provider|boolean|False|True|Indicates whether to create a user with a specified authentication provider|None|None|

Example input:

```
{
  "activate": true,
  "credentials": {
    "password": {
      "value": "blah"
    },
    "provider": {
       "name": "OKTA",
       "type": "OKTA"
    },
    "recovery_question": {
      "answer": "Q",
      "question": "A"
    }
  },
  "groupIds": [
    "00gftwyoqyVBvcpdn0h7"
  ],
  "nextLogin": false,
  "profile": {
    "city": "San Francisco",
    "costCenter": "10",
    "countryCode": "US",
    "department": "Engineering",
    "displayName": "Isaac Brock",
    "division": "R&D",
    "email": "user@example.com",
    "employeeNumber": "187",
    "firstName": "Isaac",
    "lastName": "Brock",
    "login": "user@example.com",
    "mobilePhone": "+1-555-415-1337",
    "nickName": "issac",
    "organization": "Okta",
    "preferredLanguage": "en-US",
    "primaryPhone": "+1-555-514-1337",
    "profileUrl": "http://www.example.com/profile",
    "secondEmail": "user@example.com",
    "state": "CA",
    "streetAddress": "301 Brannan St.",
    "title": "Director",
    "userType": "Employee",
    "zipCode": "94107"
  },
  "provider": false
}
```

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
```

### Triggers

#### Monitor User Groups

This trigger monitors a list of groups for user membership changes.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|group_ids|[]string|None|True|A list of group ID's|None|['00g41ix8hKbsu74Ca4x6', '00g41ieu5y7i9XEYE4x6']|
|interval|integer|300|True|The time in seconds between checks for changes to the groups users|None|100|

Example input:

```
{
  "group_ids": ["00g41ix8hKbsu74Ca4x6", "00g41ieu5y7i9XEYE4x6"],
  "interval": 100
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|users_added_from_groups|[]user_group|True|Users added to a group since the last check|
|users_removed_from_groups|[]user_group|True|Users removed from a group since the last check|

Example output:

```
{
  "users_added_from_groups": [{
    "group_name": "test1",
    "group_id": "00g41ix8hKbsu74Ca4x6",
    "users": [{
      "id": "00u44z4o0JgUYC0OO4x6",
      "status": "PASSWORD_EXPIRED",
      "created": "2020-03-17T19:28:50.000Z",
      "activated": "2020-03-17T19:28:50.000Z",
      "statusChanged": "2020-03-17T19:28:50.000Z",
      "lastUpdated": "2020-03-17T19:28:50.000Z",
      "passwordChanged": "2020-03-17T19:28:50.000Z",
      "profile": {
        "firstName": "doe",
        "lastName": "test",
        "login": "user@example.com",
        "email": "user@example.com"
      },
      "credentials": {
        "password": {},
        "provider": {
          "type": "OKTA",
          "name": "OKTA"
        }
      },
      "_links": {
        "self": {
          "href": "https://example.okta.com/api/v1/users/00u44z4o0JgUYC0OO4x6"
        }
      }
    }]
  }],
  "users_removed_from_groups": [{
    "group_name": "test1",
    "group_id": "00g41ix8hKbsu74Ca4x6",
      "users": [{
        "id": "00u44xracEYPXjhwy4x6",
        "status": "PASSWORD_EXPIRED",
        "created": "2020-03-17T19:28:27.000Z",
        "activated": "2020-03-17T19:28:28.000Z",
        "statusChanged": "2020-03-17T19:28:28.000Z",
        "lastUpdated": "2020-03-17T19:28:28.000Z",
        "passwordChanged": "2020-03-17T19:28:27.000Z",
        "profile": {
          "firstName": "bob",
          "lastName": "test",
          "login": "user@example.com",
          "email": "user@example.com"
        },
        "credentials": {
          "password": {},
          "provider": {
            "type": "OKTA",
            "name": "OKTA"
          }
        },
        "_links": {
        "self": {
          "href": "https://example.okta.com/api/v1/users/00u44xracEYPXjhwy4x6"
        }
      }
    }]
  }]
}
```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Actions may fail depending on the state of the resource you attempt to operate over.
They will return a best-effort message indicating why the Okta API responded the way it
did when possible. Depending on the API endpoint, this message is either provided
by Okta themselves, or constructed by the plugin based on the information it has at hand.

# Version History

* 3.5.1 - Update to add additional logging to Monitor User Groups trigger
* 3.5.0 - New action Update Blacklist Zones
* 3.4.3 - Fix issue where trigger did not return empty arrays when users were removed or added to group
* 3.4.2 - Fix issue where Monitor User Groups trigger would erroneously detect logins as an addition/removal of a group member
* 3.4.1 - Fix issue where Monitor User Groups trigger would continually detect the same new group addition
* 3.4.0 - New trigger Monitor User Groups
* 3.3.0 - New actions Get Factors and Send Push
* 3.2.2 - Change docker image from `komand/python-2-plugin:2` to `komand/python-3-37-slim-plugin:3` | Use input and output constants | Changed variables names to more readable | Added "f" strings | Removed duplicated code
* 3.2.1 - New spec and help.md format for the Extension Library
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
