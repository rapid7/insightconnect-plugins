# Description

[Okta](https://www.okta.com/) is a SSO and account lifecycle management provider that allows companies
to integrate their central user account system with a wide variety of other applications and services.

# Key Features

* Single Sign On User management

# Requirements

* API Key
* Okta server

# Supported Product Versions

* Okta API 25-04-2023

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|oktaKey|credential_secret_key|None|True|Okta key|None|{"secretKey": "123456789abcdef987654321GHIjklm0123456789A"}|
|oktaUrl|string|None|True|Okta Domain e.g. example.okta.com|None|example.com|

Example input:

```
{
  "oktaKey": {
    "secretKey": "123456789abcdef987654321GHIjklm0123456789A"
  },
  "oktaUrl": "example.com"
}
```

## Technical Details

### Actions

#### Reset Password

This action resets password for Okta user and transitions user status to PASSWORD_EXPIRED, so that the user is required to change their password at their next login.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|tempPassword|boolean|False|False|If set to true, sets the user's password to a temporary password and returns it|None|True|
|userId|string|None|True|User ID whose password will be reset|None|00ub0oNGTSWTBKOLGLNR|

Example input:

```
{
  "tempPassword": true,
  "userId": "00ub0oNGTSWTBKOLGLNR"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Whether the reset was successful|True|
|tempPassword|string|False|The temporary password of the Okta user, if true was set in Temporary Password input|kYC452u2|
Example output:

```
{
  "success": true,
  "tempPassword": "Ur2BUQ2w"
}
```

#### Update Blacklist Zones

This action is used to block or unblock address or network by adding or removing from a blacklist network zone.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|IP address, Network range, or CIDR to block or unblock|None|198.51.100.1|
|blacklistState|boolean|True|False|True to block, false to unblock|None|True|
|name|string|None|True|Name of blacklist zone|None|InsightConnect Blacklist Zone|

Example input:

```
{
  "address": "198.51.100.1",
  "blacklistState": true,
  "name": "InsightConnect Blacklist Zone"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|zone|zone|True|Information about the updated zone|{}|

Example output:

```
{
  "zone": {
    "links": {
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
|userId|string|None|True|User ID to get factors for|None|00a0a1qwertYUIoplK0j6|

Example input:

```
{
  "userId": "00a0a1qwertYUIoplK0j6"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|factors|[]factor|False|Object containing all the factors of a user for MFA|[]|

Example output:

```
[
    {
        "id": "00a0a1qwertYUIoplK0j7",
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
                    "x": "abcdef",
                    "y": "qwerty",
                    "crv": "P-256"
                }
            ],
            "name": "iPhone XR",
            "platform": "IOS",
            "version": "13.3"
        },
        "links": {
            "self": {
                "href": "https://example.com/api/v1/users/00a0a1qwertYUIoplK0j6/factors/00a0a1qwertYUIoplK0j7",
                "hints": {
                    "allow": [
                        "GET",
                        "DELETE"
                    ]
                }
            },
            "verify": {
                "href": "https://example.com/api/v1/users/00a0a1qwertYUIoplK0j6/factors/00a0a1qwertYUIoplK0j7/verify",
                "hints": {
                    "allow": [
                        "POST"
                    ]
                }
            },
            "user": {
                "href": "https://example.com/api/v1/users/00a0a1qwertYUIoplK0j6",
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
|factorId|string|None|True|Factor ID of the user to push verification to|None|00a0a1qwertYUIoplK0j7|
|userId|string|None|True|User ID to push verification to|None|00a0a1qwertYUIoplK0j6|

Example input:

```
{
  "factorId": "00a0a1qwertYUIoplK0j7",
  "userId": "00a0a1qwertYUIoplK0j6"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|factorStatus|string|False|User factor status|SUCCESS|

Example Output:

```
{
  "factorStatus": "SUCCESS"
}
```

#### Suspend User

This action can be used to suspend a user from the Okta system. The user will retain
membership and permissions as currently configured, but be unable to access the system
as a whole.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|login|string|None|True|The login of the employee to suspend|None|user@example.com|

Example input:

```
{
  "login": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|login|string|False|The login of the Okta user|user@example.com|
|success|boolean|True|Whether suspension was successful|true|
|userId|string|False|The user ID of the Okta user|00a0a1qwertYUIoplK0j6|

Example output:

```
{
  "userId": "00a0a1qwertYUIoplK0j6",
  "login": "user@example.com",
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
|login|string|None|True|The login of the employee to reset factors|None|user@example.com|

Example input:

```
{
  "login": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|login|string|False|The login of the Okta user|user@example.com|
|success|boolean|True|Whether suspension was successful|True|
|userId|string|False|The user ID of the Okta user|00g1m22m1230eZXxe5r8|

Example output:

```
{
  "userId": "00a0a1qwertYUIoplK0j6",
  "login": "user@example.com",
  "success": true
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
|login|string|None|True|The login of the employee to deactivate|None|user@example.com|

Example input:

```
{
  "login": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|login|string|False|The login of the Okta user|user@example.com|
|success|boolean|True|Whether deactivation was successful|True|
|userId|string|False|The user ID of the Okta user|00a0a1qwertYUIoplK0j6|

Example output:

```
{
  "userId": "00a0a1qwertYUIoplK0j6",
  "login": "user@example.com",
  "success": true
}
```

#### Delete User

This action is used to delete a user. If a user is not deprovisioned, this will deprovision a user, a second delete will be needed to remove the user. Warning: This action cannot be recovered from.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|sendAdminEmail|boolean|False|True|Sends a deactivation email to the administrator if true. Default value is false|None|False|
|userLogin|string|None|True|The login of the user to delete|None|user@example.com|

Example input:

```
{
  "sendAdminEmail": false,
  "userLogin": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Whether deactivation was successful|True|

Example output:

```
{
  "success": true
}
```

#### Unsuspend User

This action is used to unsuspend a user.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|login|string|None|True|The login of the Okta user|None|user@example.com|

Example input:

```
{
  "login": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|login|string|False|The login of the Okta user|user@example.com|
|success|boolean|True|Whether suspension was successful|True|
|userId|string|False|The user ID of the Okta user|00a0a1qwertYUIoplK0j6|

Example output:

```
{
  "userId": "00a0a1qwertYUIoplK0j6",
  "email": "user@example.com",
  "success": true
}
```

#### Get User

This action is used to obtain information about a user.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|login|string|None|True|The login of the user to obtain information about|None|user@example.com|

Example input:

```
{
  "login": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|user|user|False|User details|{}|

Example output:

```
{
  "status": "ACTIVE",
  "profile": {
    "firstName": "User",
    "lastName": "Test",
    "login": "user@example.com",
    "email": "user@example.com"
  },
  "passwordChanged": "2018-07-28T18:48:52.000Z",
  "created": "2018-07-28T17:24:41.000Z",
  "activated": "2018-07-28T18:47:24.000Z",
  "lastUpdated": "2018-07-28T18:58:06.000Z",
  "links": {
    "suspend": {
      "href": "https://example.com/api/v1/users/00a0a1qwertYUIoplK0j6/lifecycle/suspend",
      "method": "POST"
    },
    "forgotPassword": {
      "href": "https://example.com/api/v1/users/00a0a1qwertYUIoplK0j6/credentials/forgot_password",
      "method": "POST"
    },
    "self": {
      "href": "https://example.com/api/v1/users/00a0a1qwertYUIoplK0j6"
    },
    "expirePassword": {
      "href": "https://example.com/api/v1/users/00a0a1qwertYUIoplK0j6/lifecycle/expire_password",
      "method": "POST"
    },
    "deactivate": {
      "href": "https://example.com/api/v1/users/00a0a1qwertYUIoplK0j6/lifecycle/deactivate",
      "method": "POST"
    },
    "changePassword": {
      "href": "https://example.com/api/v1/users/00a0a1qwertYUIoplK0j6/credentials/change_password",
      "method": "POST"
    },
    "changeRecoveryQuestion": {
      "href": "https://example.com/api/v1/users/00a0a1qwertYUIoplK0j6/credentials/change_recovery_question",
      "method": "POST"
    },
    "resetPassword": {
      "href": "https://example.com/api/v1/users/00a0a1qwertYUIoplK0j6/lifecycle/reset_password",
      "method": "POST"
    }
  },
  "lastLogin": "2018-07-28T18:48:52.000Z",
  "credentials": {
    "recoveryQuestion": {
      "question": "What is the food you least liked as a child?"
    },
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
  "id": "00a0a1qwertYUIoplK0j6",
  "statusChanged": "2018-07-28T18:58:06.000Z"
}
```

#### Remove User from Group

This action is used to remove a user from an existing group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|groupId|string|None|True|The ID of the group to which the user should be added|None|00g1m22m1230eZXxe5r8|
|login|string|None|True|The login of the Okta user|None|user@example.com|

Example input:

```
{
  "groupId": "00g1m22m1230eZXxe5r8",
  "login": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Whether the add was successful|True|
|userId|string|False|The user ID of the Okta user|00g1m22m1230eZXxe5r8|

Example output:

```
{
  "userId": "00a0a1qwertYUIoplK0j6",
  "success": true
}
```

#### Add User to Group

This action is used to add a user to an existing group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|groupId|string|None|True|The ID of the group to which the user should be added|None|00a0a1qwertYUIoplK0j9|
|login|string|None|True|The login of the Okta user|None|user@example.com|

Example input:

```
{
  "groupId": "00a0a1qwertYUIoplK0j9",
  "login": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Whether the add was successful|True|
|userId|string|False|The user ID of the Okta user|00a0a1qwertYUIoplK0j6|

Example output:

```
{
  "userId": "00a0a1qwertYUIoplK0j6",
  "success": true
}
```

#### List Groups

This action is used to list available groups.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|False|Query to list groups. Finds a group that matches the name property. Search currently performs a startsWith match. If this parameter is not given, all groups are returned|None|Example|

Example input:

```
{
  "query": "Example"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|groups|[]group|False|List of groups|[]|
|success|boolean|True|Whether groups were found|True|

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
      "links": {
        "logo": [
          {
            "href": "https://example.com/assets/img/logos/groups/okta-medium.abcdef.png",
            "type": "image/png",
            "name": "medium"
          },
          {
            "href": "https://example.com/assets/img/logos/groups/okta-large.qwerty.png",
            "type": "image/png",
            "name": "large"
          }
        ],
        "apps": {
          "href": "https://example.com/api/v1/groups/00a0a1qwertYUIoplK0g3/apps"
        },
        "users": {
          "href": "https://example.com/api/v1/groups/00a0a1qwertYUIoplK0g3/users"
        }
      },
      "lastMembershipUpdated": "2018-07-28T21:15:17.000Z",
      "type": "OKTA_GROUP",
      "id": "00a0a1qwertYUIoplK0g3",
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
|applicationId|string|None|True|ID of the application|None|00g1m22m1230eZXxe5r8|
|appuser|object|None|False|Application user model as JSON object, see https://developer.okta.com/docs/reference/api/apps/#application-user-object|None|{"id": "00ud4tVDDXYVKPXKVLCO"}|

`appuser` accepts a [application user model](https://developer.okta.com/docs/reference/api/apps/#application-user-object) JSON object.

Example input:

```
{
  "applicationId": "00a0a1qwertYUIoplK0a2",
  "appuser": {
    "id": "00ud4qWERTYUIOPasdf"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|result|applicationUser|True|Information about the application user|{}|

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
|activate|boolean|True|True|Executes activation lifecycle operation when creating the user|None|True|
|provider|boolean|False|True|Indicates whether to create a user with a specified authentication provider|None|False|
|profile|object|None|True|Profile properties for user|None|{}|
|credentials|credentials|None|False|Credentials for user|None|{}|
|groupIds|[]string|None|False|IDs of groups that user will be immediately added to at time of creation|None|["00a0a1qwertYUIoplK0j9"]|
|nextLogin|boolean|None|True|Change password next time the user logs in|None|True|

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
    "00a0a1qwertYUIoplK0j9"
  ],
  "nextLogin": false,
  "profile": {
    "city": "San Francisco",
    "costCenter": "10",
    "countryCode": "US",
    "department": "Engineering",
    "displayName": "Test Tester",
    "division": "R&D",
    "email": "user@example.com",
    "employeeNumber": "187",
    "firstName": "Test",
    "lastName": "Tester",
    "login": "user@example.com",
    "mobilePhone": "+1-555-415-1337",
    "nickName": "tester",
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

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|user|user|False|User object|{}|

Example output:

```
{
  "user": {
    "id": "00a0a1qwertYUIoplK0j9",
    "status": "STAGED",
    "created": "2018-09-06T19:00:06.000Z",
    "lastUpdated": "2018-09-06T19:00:06.000Z",
    "profile": {
      "firstName": "Test",
      "lastName": "Tester",
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
    "links": {
      "activate": {
        "href": "https://example.com/api/v1/users/00a0a1qwertYUIoplK0j9/lifecycle/activate",
        "method": "POST"
      },
      "self": {
        "href": "https://example.com/api/v1/users/00a0a1qwertYUIoplK0j9"
      }
    }
  }
}
```

### Triggers

#### Monitor User Groups

This trigger monitors a list of groups for user membership changes.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|groupIds|[]string|None|True|A list of group ID's|None|["00g41ix8hKbsu74Ca4x6", "00g41ieu5y7i9XEYE4x6"]|
|interval|integer|300|True|The time in seconds between checks for changes to the groups users|None|100|

Example input:

```
{
  "groupIds": [
    "00g41ix8hKbsu74Ca4x6",
    "00g41ieu5y7i9XEYE4x6"
  ],
  "interval": 100
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|usersAddedToGroups|[]user_group|True|Users added to a group since the last check|[]|
|usersRemovedFromGroups|[]user_group|True|Users removed from a group since the last check|[]|

Example output:

```
{
  "usersAddedFromGroups": [
    {
      "groupName": "test1",
      "groupId": "00g41ix8hKbsu74Ca4x6",
      "users": [
        {
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
          "links": {
            "self": {
              "href": "https://example.okta.com/api/v1/users/00u44z4o0JgUYC0OO4x6"
            }
          }
        }
      ]
    }
  ],
  "usersRemovedFromGroups": [
    {
      "group_name": "test1",
      "group_id": "00g41ix8hKbsu74Ca4x6",
      "users": [
        {
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
          "links": {
            "self": {
              "href": "https://example.okta.com/api/v1/users/00u44xracEYPXjhwy4x6"
            }
          }
        }
      ]
    }
  ]
}
```

### Tasks

#### Monitor Logs

This task is used to monitor system logs.

##### Input

_This task does not contain any inputs._

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|logs|[]log|True|All system logs within the specified time range|[]|

Example output:

```
{
  "logs": [
    {
      "actor": {
        "id": "12345",
        "type": "User",
        "alternateId": "user@example.com",
        "displayName": "User"
      },
      "client": {
        "userAgent": {
          "rawUserAgent": "python-requests/2.26.0",
          "os": "Unknown",
          "browser": "UNKNOWN"
        },
        "zone": "null",
        "device": "Unknown",
        "ipAddress": "198.51.100.1"
      },
      "authenticationContext": {
        "externalSessionId": "12345"
      },
      "displayMessage": "Suspend Okta user",
      "eventType": "user.lifecycle.suspend",
      "outcome": {
        "result": "SUCCESS"
      },
      "published": "2023-04-27T07:49:21.764Z",
      "securityContext": {
        "asNumber": 123456,
        "asOrg": "test",
        "isp": "test",
        "domain": "example.com",
        "isProxy": false
      },
      "severity": "INFO",
      "debugContext": {
        "debugData": {
          "requestId": "12345",
          "dtHash": "111111cd0ecfb444ee1fcb9687ba8b174a3c8d251ce927e6016b871bc222222",
          "requestUri": "/api/v1/users/12345/lifecycle/suspend",
          "url": "/api/v1/users/12345/lifecycle/suspend?"
        }
      },
      "legacyEventType": "core.user.config.user_status.suspended",
      "transaction": {
        "type": "WEB",
        "id": "12345",
        "detail": {
          "requestApiTokenId": "12345"
        }
      },
      "uuid": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "version": "0",
      "request": {
        "ipChain": [
          {
            "ip": "198.51.100.1",
            "version": "V4"
          }
        ]
      },
      "target": [
        {
          "id": "12345",
          "type": "User",
          "alternateId": "user@example.com",
          "displayName": "Test User"
        }
      ]
    }
  ]
}
```

### Custom Output Types

#### appCredentials

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Password|password|False|Password for application|
|Username|string|False|Username for application|

#### appUserLinks

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Application|link|False|Provides a link to the application|
|User|link|False|Provides a link to the user|

#### appUserProfile

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Email|string|False|User email|
|First Name|string|False|User first name|
|Last Name|string|False|User last name|
|Mobile Phone|string|False|User mobile phone|
|Profile|string|False|User profile|
|Role|string|False|User role|
|Second Email|string|False|User second email|

#### applicationUser

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created|string|False|Timestamp when app user was created|
|Credentials|appCredentials|False|Credentials for the assigned application|
|External ID|string|False|User ID in the target application|
|ID|string|False|User ID|
|Last Synchronization|string|False|Timestamp when last sync operation was executed|
|Last Updated|string|False|Timestamp when app user was last updated|
|Links|appUserLinks|False|Links to related resources|
|Password Changed|string|False|Timestamp when app password last changed|
|Profile|appUserProfile|False|App-specific profile for the user|
|Scope|string|False|Scope|
|Status|string|False|Status of app user|
|Status Changed|string|False|Timestamp when status was last changed|
|Synchronization state|string|False|Synchronization state for app user|

#### authenticationContext

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Authentication Provider|string|False|The system that proves the identity of an actor using the credentials provided to it|
|Authentication Step|integer|False|The zero-based step number in the authentication pipeline. Currently unused and always set to 0|
|Credential Provider|string|False|A credential provider is a software service that manages identities and their associated credentials. When authentication occurs through credentials provided by a credential provider, the credential provider is recorded here|
|Credential Type|string|False|The underlying technology/scheme used in the credential|
|External Session ID|string|False|A proxy for the actor's session ID|
|Interface|string|False|The third-party user interface that the actor authenticates through, if any|
|Issuer|issuer|False|The specific software entity that creates and issues the credential|

#### clientObject

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Device|string|False|Type of device that the client operates from|
|Geographical Context|geographicalContext|False|The physical location where the client is making its request from|
|ID|string|False|For OAuth requests, this is the ID of the OAuth client making the request. For SSWS token requests, this is the ID of the agent making the request|
|IP Address|string|False|IP address that the client is making its request from|
|User Agent|userAgent|False|The user agent that is used by an actor to perform an action|
|Zone|string|False|The name of the zone that the client's location is mapped to|

#### credentials

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Password|password|False|Password details|
|Provider|provider|False|Provider details|
|Recovery Question|recoveryQuestion|False|Recovery question details|

#### deactivate

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Hints|hints|False|Hints|
|HREF|string|False|HREF|

#### debugContext

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Debug Data|object|False|Dynamic field that contains miscellaneous information that is dependent on the event type|

#### entityObject

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Alternate ID|string|False|Alternative ID of the object|
|Display Name|object|False|Details about the object|
|Display Name|string|False|Display name of the object|
|ID|string|False|ID of the object|
|Type|string|False|Type of the object|

#### factor

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created|string|False|Timestamp when the factor was created|
|Embedded|object|False|Embedded resources related to the Factor|
|Factor Type|string|False|Type of the factor|
|ID|string|False|Unique key for the factor, a 20 character long system-generated ID|
|Last Updated|string|False|Timestamp when the factor was last updated|
|Factor Links|factorLinks|False|Discoverable resources related to the Factor|
|Profile|object|False|Profile credentials|
|Factor Provider|string|False|Provider of the factor|
|Factor Status|string|False|Status of the factor|
|Vendor Name|string|False|Factor Vendor Name (Same as provider but for On-Prem MFA it depends on Administrator Settings)|
|Verify|factorVerificationObject|False|Specifies additional verification data for 'token' or 'token:hardware' factors|

#### factorLink

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Hints|hints|False|Hints for the hyperlink|
|Href|string|False|Hyperlink to the resource|

#### factorLinks

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Activate Link|factorLink|False|Polls factor for completion of the activation of verification|
|Poll Link|factorLink|False|Lifecycle action to transition the factor to ACTIVE status|
|Questions Link|factorLink|False|List of questions for the question factor type|
|Resend Link|factorLink|False|List of delivery options to resend activation or factor challenge|
|Self Link|factorLink|False|The actual factor|
|Send Link|factorLink|False|List of delivery options to send an activation or factor challenge|
|Verify Link|factorLink|False|Verify the factor|

#### factorVerificationObject

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Next Pass Code|string|False|OTP for current time window|
|Pass Code|string|False|OTP for next time window|

#### gateways

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Type|string|False|Type|
|Value|string|False|Value|

#### geographicalContext

|Name|Type|Required|Description|
|----|----|--------|-----------|
|City|string|False|The city that encompasses the area that contains the geolocation coordinates, if available|
|Country|string|False|Full name of the country that encompasses the area that contains the geolocation coordinates|
|Geolocation|geolocation|False|Contains the geolocation coordinates|
|Postal Code|string|False|Postal code of the area that encompasses the geolocation coordinates|
|State|string|False|Full name of the state or province that encompasses the area that contains the geolocation coordinates|

#### geolocation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Latitude|float|False|Latitude|
|Longitude|float|False|Longitude|

#### group

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created|string|False|Timestamp when group was created|
|Description|string|False|Group description|
|ID|string|False|Group ID|
|Last Membership Updated|string|False|Timestamp when group's memberships were last updated|
|Last Updated|string|False|Timestamp when group's profile was last updated|
|Links|groupLinks|False|Links to related resources|
|Name|string|False|Group name|
|Object Class|[]string|False|Determines the group's profile|
|Type|string|False|Type of the group|

#### groupLinks

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Applications|link|False|Provides link to all applications that are assigned to the group|
|Logo|[]logo|False|Provides links to logo images for the group if available|
|Users|link|False|Provides link to group members|

#### hints

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Allowed Methods|[]string|False|Allowed Methods|

#### ipAddress

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Geographical Context|geographicalContext|False|Geographical context of the IP address|
|IP|string|False|IP address|
|Source|string|False|Details regarding the source|
|Version|string|False|IP address version|

#### issuer

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Varies depending on the type of authentication. If authentication is SAML 2.0, id is the issuer in the SAML assertion. For social login, id is the issuer of the token|
|Type|string|False|Information on the issuer and source of the SAML assertion or token|

#### link

|Name|Type|Required|Description|
|----|----|--------|-----------|
|HREF|string|False|HREF|

#### log

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Actor|entityObject|False|Describes the entity that performs an action|
|Authentication Context|authenticationContext|False|The authentication data of an action|
|Client|clientObject|False|The client that requests an action|
|Debug Context|debugContext|False|The debug request data of an action|
|Display Message|string|False|The display message for an event|
|Event Type|string|False|Type of event that is published|
|Legacy Event Type|string|False|Type of legacy event|
|Outcome|outcome|False|The outcome of an action|
|Published|string|False|Timestamp when the event is published|
|Request|request|False|The request that initiates an action|
|Security Context|securityContext|False|The security data of an action|
|Severity|string|False|Indicates how severe the event is: DEBUG, INFO, WARN, ERROR|
|Target|[]entityObject|False|Zero or more targets of an action|
|Transaction|transaction|False|The transaction details of an action|
|UUID|string|False|Unique identifier for an individual event|
|Version|string|False|Versioning indicator|

#### logo

|Name|Type|Required|Description|
|----|----|--------|-----------|
|HREF|string|False|HREF|
|Name|string|False|Name of the logo|
|Type|string|False|Type of the file|

#### outcome

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Reason|string|False|Reason for the result|
|Result|string|False|Result of the action: SUCCESS, FAILURE, SKIPPED, ALLOW, DENY, CHALLENGE, UNKNOWN|

#### password

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Value|string|False|Password value|

#### provider

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Name|string|False|Provider name|
|Type|string|False|Provider type|

#### recoveryQuestion

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Answer|string|False|Answer for the recovery question|
|Recovery Question|string|False|Question used for account recovery|

#### request

|Name|Type|Required|Description|
|----|----|--------|-----------|
|IP Chain|[]ipAddress|False|If the incoming request passes through any proxies, the IP addresses of those proxies are stored here in the format: clientIp, proxy1, proxy2, and so on. This field is useful when working with trusted proxies|

#### securityContext

|Name|Type|Required|Description|
|----|----|--------|-----------|
|AS Number|integer|False|The Autonomous system number that is associated with the autonomous system that the event request was sourced to|
|AS Organization|string|False|The organization that is associated with the autonomous system that the event request is sourced to|
|Domain|string|False|The domain name that is associated with the IP address of the inbound event request|
|Is Proxy|boolean|False|Specifies whether an event's request is from a known proxy|
|ISP|string|False|The Internet service provider that is used to send the event's request|

#### transaction

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Detail|object|False|Details for this transaction|
|ID|string|False|Unique identifier for this transaction|
|Type|string|False|Describes the kind of transaction. WEB indicates a web request. JOB indicates an asynchronous task|

#### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Activated|string|False|When the user was activated|
|Created|string|False|When the user was created|
|Credentials|credentials|False|User's primary authentication and recovery credentials|
|ID|string|False|User ID|
|Last Login|string|False|When the last login for the user was|
|Last Updated|string|False|When the user was last updated|
|Links|userLinks|False|Link relations for the user's current status|
|Password Changed|string|False|When the password was changed|
|Profile|userProfile|False|User profile properties|
|Status|string|False|Current status of the user|
|Status Changed|string|False|When the status of the user changed|
|User Type|userType|False|Type of the user|

#### userAgent

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Browser|string|False|If the client is a web browser, this field identifies the type of web browser|
|OS|string|False|The operating system that the client runs on|
|Raw User Agent|string|False|A raw string representation of the user agent|

#### userLink

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Href|string|False|Hyperlink to the operation|
|Method|string|False|Method of the request for the operation|

#### userLinks

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Activate Link|userLink|False|Lifecycle action to activate the user|
|Change Password Link|userLink|False|Changes a user's password validating the user's current password|
|Change Recovery Question Link|userLink|False|Changes a user's recovery credential by validating the user's current password|
|Deactivate Link|userLink|False|Lifecycle action to deactivate the user|
|Expire Password Link|userLink|False|Lifecycle action to expire the user's password|
|Forgot Password Link|userLink|False|Resets a user's password by validating the user's recovery credential|
|Reset Factors Link|userLink|False|Lifecycle action to reset all MFA factors|
|Reset Password Link|userLink|False|Lifecycle action to trigger a password reset|
|Self Link|userLink|False|A self-referential link to this user|
|Suspend Link|userLink|False|Lifecycle action to suspend the user|
|Unlock Link|userLink|False|Lifecycle action to unlock a locked-out user|
|Unsuspend Link|userLink|False|Lifecycle action to unsuspend the user|

#### userProfile

|Name|Type|Required|Description|
|----|----|--------|-----------|
|City|string|False|City or locality component of user's address|
|Cost Center|string|False|Name of a cost center assigned to user|
|Country Code|string|False|Country name component of user's address|
|Department|string|False|Name of user's department|
|Display Name|string|False|Name of the user, suitable for display to end users|
|Division|string|False|Name of user's division|
|Email|string|False|Primary email address of the user|
|Employee Number|string|False|Organization or company assigned unique identifier for the user|
|First Name|string|False|First name of the user|
|Honorific Prefix|string|False|Honorific prefix(es) of the user, or title in most Western languages|
|Honorific Suffix|string|False|Honorific suffix(es) of the user|
|Last Name|string|False|Last name of the user|
|Locale|string|False|User's default location for purposes of localizing items such as currency, date time format, numerical representations, and so on|
|Login|string|False|Login of the user|
|Manager|string|False|Name of the user's manager, suitable for display to end users|
|Manager ID|string|False|The identifier of a user's manager|
|Middle Name|string|False|Middle name(s) of the user|
|Mobile Phone|string|False|Mobile phone number of user|
|Nick Name|string|False|Casual way to address the user in real life|
|Organization|string|False|Name of user's organization|
|Postal Address|string|False|Mailing address component of user's address|
|Preferred Language|string|False|User's preferred written or spoken languages|
|Primary Phone|string|False|Primary phone number of user such as home number|
|Profile URL|string|False|URL of user's online profile|
|Secondary Email|string|False|Secondary email address of user typically used for account recovery|
|State|string|False|State or region component of user's address|
|Street Address|string|False|Full street address component of user's address|
|Time Zone|string|False|User's time zone|
|Title|string|False|Title of the user|
|User Type|string|False|Used to describe the organization to user relationship such as 'Employee' or 'Contractor'|
|ZIP Code|string|False|ZIP code or postal code component of user's address|

#### userType

|Name|Type|Required|Description|
|----|----|--------|-----------|
|The identifier of the type|string|False|ID|

#### user_group

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Group ID|string|False|ID of the group|
|Group Name|string|False|Name of the group|
|Users|[]user|False|List of users|

#### zone

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created|string|False|Created|
|Gateways|[]gateways|False|Gateways|
|ID|string|False|ID|
|Last Updated|string|False|Last updated|
|Zone Links|zoneLinks|False|Zone links|
|Name|string|False|Name|
|Proxies|[]gateways|False|Proxies|
|Status|string|False|Status|
|System|boolean|False|System|
|Type|string|False|Type|

#### zoneLinks

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Deactivate|deactivate|False|Deactivate|
|Self|deactivate|False|Self|

## Troubleshooting

Actions may fail depending on the state of the resource you attempt to operate over.
They will return a best-effort message indicating why the Okta API responded the way it
did when possible. Depending on the API endpoint, this message is either provided
by Okta themselves, or constructed by the plugin based on the information it has at hand.

# Version History

* 4.0.0 - Add Monitor Logs task | Code refactor
* 3.6.3 - Add Reset Password action
* 3.5.3 - Correct spelling in help.md
* 3.5.2 - Fix issue where Monitor User Groups trigger would be limited to 1000 users
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

* [Okta API Spec](http://developer.okta.com/docs/api/resources)

## References

* [Okta API Spec](http://developer.okta.com/docs/api/resources)
