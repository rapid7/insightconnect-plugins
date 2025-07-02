# Description

[Okta](https://www.okta.com/) is a SSO and account lifecycle management provider that allows companies to integrate their central user account system with a wide variety of other applications and services

# Key Features

* Single Sign On User management

# Requirements

* API Key
* Okta server

# Supported Product Versions

* Okta API 22-05-2023

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|oktaKey|credential_secret_key|None|True|Okta key|None|{"secretKey": "123456789abcdef987654321GHIjklm0123456789A"}|None|None|
|oktaUrl|string|None|True|Okta Domain. Please ensure your subdomain is present if the second-level domain is 'okta', e.g. 'example.okta.com'|None|example.okta.com|None|None|

Example input:

```
{
  "oktaKey": {
    "secretKey": "123456789abcdef987654321GHIjklm0123456789A"
  },
  "oktaUrl": "example.okta.com"
}
```

## Technical Details

### Actions


#### Add User to Group

This action is used to add a user to an existing group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|groupId|string|None|True|The ID of the group to which the user should be added|None|00a0a1qwertYUIoplK0j9|None|None|
|login|string|None|True|The login of the Okta user|None|user@example.com|None|None|
  
Example input:

```
{
  "groupId": "00a0a1qwertYUIoplK0j9",
  "login": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the add was successful|True|
|userId|string|False|The user ID of the Okta user|00a0a1qwertYUIoplK0j6|
  
Example output:

```
{
  "success": true,
  "userId": "00a0a1qwertYUIoplK0j6"
}
```

#### Assign User to Application for Provisioning

This action is used to assign user to application for SSO and provisioning

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|applicationId|string|None|True|ID of the application|None|00g1m22m1230eZXxe5r8|None|None|
|appuser|object|None|False|Application user model as JSON object, see https://developer.okta.com/docs/reference/api/apps/#application-user-object|None|{"id": "00ud4tVDDXYVKPXKVLCO"}|None|None|
  
Example input:

```
{
  "applicationId": "00g1m22m1230eZXxe5r8",
  "appuser": {
    "id": "00ud4tVDDXYVKPXKVLCO"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|applicationUser|True|Information about the application user|{"id":"00u15s1KDETTQMQYABRL","scope":"USER","credentials":{"userName":"user@example.com"},"profile":{"salesforceGroups":["Employee"],"role":"Developer","profile":"Standard User"}}|
  
Example output:

```
{
  "result": {
    "credentials": {
      "userName": "user@example.com"
    },
    "id": "00u15s1KDETTQMQYABRL",
    "profile": {
      "profile": "Standard User",
      "role": "Developer",
      "salesforceGroups": [
        "Employee"
      ]
    },
    "scope": "USER"
  }
}
```

#### Create User

This action is used to create a new user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|activate|boolean|True|True|Executes activation lifecycle operation when creating the user|None|True|None|None|
|credentials|credentials|None|False|Credentials for user. If configuring the `provider` and/or `recovery_question` inputs, for each used, their respective fields must be completed otherwise Okta will return an error. This action will attempt to prevent that be removing the entire input if it detects a missing field in that input|None|{"password":{"value":"blah"},"provider":{"name":"OKTA","type":"OKTA"},"recovery_question":{"answer":"Q","question":"A"}}|None|None|
|groupIds|[]string|None|False|IDs of groups that user will be immediately added to at time of creation|None|["00a0a1qwertYUIoplK0j9"]|None|None|
|nextLogin|boolean|None|True|Change password next time the user logs in|None|False|None|None|
|profile|object|None|True|Profile properties for user|None|{"city":"San Francisco","costCenter":"10","countryCode":"US","department":"Engineering","displayName":"Test Tester","division":"R&D","email":"user@example.com","employeeNumber":"187","firstName":"Test","lastName":"Tester","login":"user@example.com","mobilePhone":"+1-555-415-1337","nickName":"tester","organization":"Okta","preferredLanguage":"en-US","primaryPhone":"+1-555-514-1337","profileUrl":"https://example.com","secondEmail":"user@example.com","state":"CA","streetAddress":"301 Brannan St.","title":"Director","userType":"Employee","zipCode":"94107"}|None|None|
|provider|boolean|False|True|Indicates whether to create a user with a specified authentication provider|None|False|None|None|
  
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
    "profileUrl": "https://example.com",
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
| :--- | :--- | :--- | :--- | :--- |
|user|user|False|User details|{"id":"00a0a1qwertYUIoplK0j9","status":"STAGED","created":"2018-09-06T19:00:06.000Z","lastUpdated":"2018-09-06T19:00:06.000Z","profile":{"firstName":"Test","lastName":"Tester","mobilePhone":"555-415-1337","login":"user@example.com","email":"user@example.com"},"credentials":{"emails":[{"value":"user@example.com","status":"VERIFIED","type":"PRIMARY"}],"provider":{"type":"OKTA","name":"OKTA"}},"links":{"activate":{"href":"https://example.com","method":"POST"},"self":{"href":"https://example.com"}}}|
  
Example output:

```
{
  "user": {
    "created": "2018-09-06T19:00:06.000Z",
    "credentials": {
      "emails": [
        {
          "status": "VERIFIED",
          "type": "PRIMARY",
          "value": "user@example.com"
        }
      ],
      "provider": {
        "name": "OKTA",
        "type": "OKTA"
      }
    },
    "id": "00a0a1qwertYUIoplK0j9",
    "lastUpdated": "2018-09-06T19:00:06.000Z",
    "links": {
      "activate": {
        "href": "https://example.com",
        "method": "POST"
      },
      "self": {
        "href": "https://example.com"
      }
    },
    "profile": {
      "email": "user@example.com",
      "firstName": "Test",
      "lastName": "Tester",
      "login": "user@example.com",
      "mobilePhone": "555-415-1337"
    },
    "status": "STAGED"
  }
}
```

#### Deactivate User

This action is used to deactivate / deprovision a user from the Okta system. In addition to losing the ability to log 
in, the user will be removed from all configured applications and lose all configured settings. This is a non-
reversible, destructive operation. This action is also considered asynchronous by the Okta API, meaning there is some 
delay between the API returning a successful result and the actual deactivation / deprovisioning of a user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|login|string|None|True|The login of the employee to deactivate|None|user@example.com|None|None|
  
Example input:

```
{
  "login": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|login|string|False|The login of the Okta user|user@example.com|
|success|boolean|True|Whether deactivation was successful|True|
|userId|string|False|The user ID of the Okta user|00a0a1qwertYUIoplK0j6|
  
Example output:

```
{
  "login": "user@example.com",
  "success": true,
  "userId": "00a0a1qwertYUIoplK0j6"
}
```

#### Delete User

This action is used to delete a user. This operation on a user that hasn't been deactivated causes that user to be 
deactivated. A second delete operation is required to delete the user. Warning, this action cannot be recovered

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|sendAdminEmail|boolean|False|True|Sends a deactivation email to the administrator if true. Default value is false|None|False|None|None|
|userLogin|string|None|True|The login of the user to delete|None|user@example.com|None|None|
  
Example input:

```
{
  "sendAdminEmail": false,
  "userLogin": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether deactivation was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Get Okta User Factors

This action is used to return an object containing all of a user's factors for MFA

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|userId|string|None|True|User ID to get factors for|None|00a0a1qwertYUIoplK0j6|None|None|
  
Example input:

```
{
  "userId": "00a0a1qwertYUIoplK0j6"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|factors|[]factor|False|Object containing all the factors of a user for MFA|[{"id":"00a0a1qwertYUIoplK0j7","factorType":"push","provider":"OKTA","vendorName":"OKTA","status":"ACTIVE","created":"2020-01-24T14:52:55.000Z","lastUpdated":"2020-01-24T14:55:18.000Z","profile":{"credentialId":"user@example.com","deviceType":"SmartPhone_IPhone","keys":[{"kty":"EC","use":"sig","kid":"default","x":"abcdef","y":"qwerty","crv":"P-256"}],"name":"iPhone XR","platform":"IOS","version":"13.3"},"links":{"self":{"href":"https://example.com","hints":{"allow":["GET","DELETE"]}},"verify":{"href":"https://example.com","hints":{"allow":["POST"]}},"user":{"href":"https://example.com","hints":{"allow":["GET"]}}}}]|
  
Example output:

```
{
  "factors": [
    {
      "created": "2020-01-24T14:52:55.000Z",
      "factorType": "push",
      "id": "00a0a1qwertYUIoplK0j7",
      "lastUpdated": "2020-01-24T14:55:18.000Z",
      "links": {
        "self": {
          "hints": {
            "allow": [
              "GET",
              "DELETE"
            ]
          },
          "href": "https://example.com"
        },
        "user": {
          "hints": {
            "allow": [
              "GET"
            ]
          },
          "href": "https://example.com"
        },
        "verify": {
          "hints": {
            "allow": [
              "POST"
            ]
          },
          "href": "https://example.com"
        }
      },
      "profile": {
        "credentialId": "user@example.com",
        "deviceType": "SmartPhone_IPhone",
        "keys": [
          {
            "crv": "P-256",
            "kid": "default",
            "kty": "EC",
            "use": "sig",
            "x": "abcdef",
            "y": "qwerty"
          }
        ],
        "name": "iPhone XR",
        "platform": "IOS",
        "version": "13.3"
      },
      "provider": "OKTA",
      "status": "ACTIVE",
      "vendorName": "OKTA"
    }
  ]
}
```

#### Get User

This action is used to obtain information about a user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|login|string|None|True|The login of the user to obtain information about|None|user@example.com|None|None|
  
Example input:

```
{
  "login": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user|user|False|User details|{"status":"ACTIVE","profile":{"firstName":"User","lastName":"Test","login":"user@example.com","email":"user@example.com"},"passwordChanged":"2018-07-28T18:48:52.000Z","created":"2018-07-28T17:24:41.000Z","activated":"2018-07-28T18:47:24.000Z","lastUpdated":"2018-07-28T18:58:06.000Z","links":{"suspend":{"href":"https://example.com","method":"POST"},"forgotPassword":{"href":"https://example.com","method":"POST"},"self":{"href":"https://example.com"},"expirePassword":{"href":"https://example.com","method":"POST"},"deactivate":{"href":"https://example.com","method":"POST"},"changePassword":{"href":"https://example.com","method":"POST"},"changeRecoveryQuestion":{"href":"https://example.com","method":"POST"},"resetPassword":{"href":"https://example.com","method":"POST"}},"lastLogin":"2018-07-28T18:48:52.000Z","credentials":{"recoveryQuestion":{"question":"What is the food you least liked as a child?"},"emails":[{"status":"VERIFIED","type":"PRIMARY","value":"user@example.com"}],"provider":{"type":"OKTA","name":"OKTA"}},"id":"00a0a1qwertYUIoplK0j6","statusChanged":"2018-07-28T18:58:06.000Z"}|
  
Example output:

```
{
  "user": {
    "activated": "2018-07-28T18:47:24.000Z",
    "created": "2018-07-28T17:24:41.000Z",
    "credentials": {
      "emails": [
        {
          "status": "VERIFIED",
          "type": "PRIMARY",
          "value": "user@example.com"
        }
      ],
      "provider": {
        "name": "OKTA",
        "type": "OKTA"
      },
      "recoveryQuestion": {
        "question": "What is the food you least liked as a child?"
      }
    },
    "id": "00a0a1qwertYUIoplK0j6",
    "lastLogin": "2018-07-28T18:48:52.000Z",
    "lastUpdated": "2018-07-28T18:58:06.000Z",
    "links": {
      "changePassword": {
        "href": "https://example.com",
        "method": "POST"
      },
      "changeRecoveryQuestion": {
        "href": "https://example.com",
        "method": "POST"
      },
      "deactivate": {
        "href": "https://example.com",
        "method": "POST"
      },
      "expirePassword": {
        "href": "https://example.com",
        "method": "POST"
      },
      "forgotPassword": {
        "href": "https://example.com",
        "method": "POST"
      },
      "resetPassword": {
        "href": "https://example.com",
        "method": "POST"
      },
      "self": {
        "href": "https://example.com"
      },
      "suspend": {
        "href": "https://example.com",
        "method": "POST"
      }
    },
    "passwordChanged": "2018-07-28T18:48:52.000Z",
    "profile": {
      "email": "user@example.com",
      "firstName": "User",
      "lastName": "Test",
      "login": "user@example.com"
    },
    "status": "ACTIVE",
    "statusChanged": "2018-07-28T18:58:06.000Z"
  }
}
```

#### Get User Groups

This action is used to fetch the groups of which the user is a member

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|User ID or login|None|00g1m22m1230eZXxe5r8|None|None|
  
Example input:

```
{
  "id": "00g1m22m1230eZXxe5r8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|userGroups|[]group|False|List of user groups|[{"id":"123456","created":"2018-07-28T20:28:20.000Z","lastUpdated":"2018-07-28T20:28:20.000Z","lastMembershipUpdated":"2023-04-26T09:53:11.000Z","objectClass":["okta:user_group"],"type":"OKTA_GROUP","name":"Example Group","description":"Example description","links":{"logo":[{"name":"medium","href":"https://example.com","type":"image/png"},{"name":"large","href":"https://example.com","type":"image/png"}],"users":{"href":"https://example.com"},"apps":{"href":"https://example.com"}}},{"id":"123457","created":"2018-07-28T20:28:20.000Z","lastUpdated":"2018-07-28T20:28:20.000Z","lastMembershipUpdated":"2023-04-26T09:53:11.000Z","objectClass":["okta:user_group"],"type":"OKTA_GROUP","name":"Example Group1","description":"Example description","links":{"logo":[{"name":"medium","href":"https://example.com","type":"image/png"},{"name":"large","href":"https://example.com","type":"image/png"}],"users":{"href":"https://example.com"},"apps":{"href":"https://example.com"}}}]|
  
Example output:

```
{
  "userGroups": [
    {
      "created": "2018-07-28T20:28:20.000Z",
      "description": "Example description",
      "id": "123456",
      "lastMembershipUpdated": "2023-04-26T09:53:11.000Z",
      "lastUpdated": "2018-07-28T20:28:20.000Z",
      "links": {
        "apps": {
          "href": "https://example.com"
        },
        "logo": [
          {
            "href": "https://example.com",
            "name": "medium",
            "type": "image/png"
          },
          {
            "href": "https://example.com",
            "name": "large",
            "type": "image/png"
          }
        ],
        "users": {
          "href": "https://example.com"
        }
      },
      "name": "Example Group",
      "objectClass": [
        "okta:user_group"
      ],
      "type": "OKTA_GROUP"
    },
    {
      "created": "2018-07-28T20:28:20.000Z",
      "description": "Example description",
      "id": "123457",
      "lastMembershipUpdated": "2023-04-26T09:53:11.000Z",
      "lastUpdated": "2018-07-28T20:28:20.000Z",
      "links": {
        "apps": {
          "href": "https://example.com"
        },
        "logo": [
          {
            "href": "https://example.com",
            "name": "medium",
            "type": "image/png"
          },
          {
            "href": "https://example.com",
            "name": "large",
            "type": "image/png"
          }
        ],
        "users": {
          "href": "https://example.com"
        }
      },
      "name": "Example Group1",
      "objectClass": [
        "okta:user_group"
      ],
      "type": "OKTA_GROUP"
    }
  ]
}
```

#### List Groups

This action is used to list available groups

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|False|Query to list groups. Finds a group that matches the name property. Search currently performs a startsWith match. If this parameter is not given, all groups are returned|None|Example|None|None|
  
Example input:

```
{
  "query": "Example"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|groups|[]group|False|List of groups|[{"name":"Cool","created":"2018-07-28T20:28:20.000Z","objectClass":["okta:user_group"],"lastUpdated":"2018-07-28T20:28:20.000Z","links":{"logo":[{"href":"https://example.com","type":"image/png","name":"medium"},{"href":"https://example.com","type":"image/png","name":"large"}],"apps":{"href":"https://example.com"},"users":{"href":"https://example.com"}},"lastMembershipUpdated":"2018-07-28T21:15:17.000Z","type":"OKTA_GROUP","id":"00a0a1qwertYUIoplK0g3","description":"Cool people"}]|
|success|boolean|True|Whether groups were found|True|
  
Example output:

```
{
  "groups": [
    {
      "created": "2018-07-28T20:28:20.000Z",
      "description": "Cool people",
      "id": "00a0a1qwertYUIoplK0g3",
      "lastMembershipUpdated": "2018-07-28T21:15:17.000Z",
      "lastUpdated": "2018-07-28T20:28:20.000Z",
      "links": {
        "apps": {
          "href": "https://example.com"
        },
        "logo": [
          {
            "href": "https://example.com",
            "name": "medium",
            "type": "image/png"
          },
          {
            "href": "https://example.com",
            "name": "large",
            "type": "image/png"
          }
        ],
        "users": {
          "href": "https://example.com"
        }
      },
      "name": "Cool",
      "objectClass": [
        "okta:user_group"
      ],
      "type": "OKTA_GROUP"
    }
  ],
  "success": true
}
```

#### Remove User from Group

This action is used to remove a user from an existing group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|groupId|string|None|True|The ID of the group to which the user should be added|None|00g1m22m1230eZXxe5r8|None|None|
|login|string|None|True|The login of the Okta user|None|user@example.com|None|None|
  
Example input:

```
{
  "groupId": "00g1m22m1230eZXxe5r8",
  "login": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the add was successful|True|
|userId|string|False|The user ID of the Okta user|00g1m22m1230eZXxe5r8|
  
Example output:

```
{
  "success": true,
  "userId": "00g1m22m1230eZXxe5r8"
}
```

#### Reset Factors

This action is used to reset all multifactors for user by email

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|login|string|None|True|The login of the employee to reset factors|None|user@example.com|None|None|
  
Example input:

```
{
  "login": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|login|string|False|The login of the Okta user|user@example.com|
|success|boolean|True|Whether the reset was successful|True|
|userId|string|False|The user ID of the Okta user|00g1m22m1230eZXxe5r8|
  
Example output:

```
{
  "login": "user@example.com",
  "success": true,
  "userId": "00g1m22m1230eZXxe5r8"
}
```

#### Reset Password

This action is used to this action resets password for Okta user and transitions user status to PASSWORD_EXPIRED, so 
that the user is required to change their password at their next login

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|tempPassword|boolean|False|False|If set to true, sets the user's password to a temporary password and returns it|None|True|None|None|
|userId|string|None|True|User ID whose password will be reset|None|00ub0oNGTSWTBKOLGLNR|None|None|
  
Example input:

```
{
  "tempPassword": false,
  "userId": "00ub0oNGTSWTBKOLGLNR"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the reset was successful|True|
|tempPassword|string|False|The temporary password of the Okta user, if true was set in Temporary Password input|kYC452u2|
  
Example output:

```
{
  "success": true,
  "tempPassword": "kYC452u2"
}
```

#### Push MFA Challenge

This action is used to push an MFA challenge to a user's device and wait for a success or rejection

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|factorId|string|None|True|Factor ID of the user to push verification to|None|00a0a1qwertYUIoplK0j7|None|None|
|userId|string|None|True|User ID to push verification to|None|00a0a1qwertYUIoplK0j6|None|None|
  
Example input:

```
{
  "factorId": "00a0a1qwertYUIoplK0j7",
  "userId": "00a0a1qwertYUIoplK0j6"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|factorStatus|string|False|User factor status|SUCCESS|
  
Example output:

```
{
  "factorStatus": "SUCCESS"
}
```

#### Suspend User

This action is used to suspend a user from the Okta system. The user will retain membership and permissions as 
currently configured, but be unable to access the system as a whole

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|login|string|None|True|The login of the employee to suspend|None|user@example.com|None|None|
  
Example input:

```
{
  "login": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|login|string|False|The login of the Okta user|user@example.com|
|success|boolean|True|Whether suspension was successful|True|
|userId|string|False|The user ID of the Okta user|00a0a1qwertYUIoplK0j6|
  
Example output:

```
{
  "login": "user@example.com",
  "success": true,
  "userId": "00a0a1qwertYUIoplK0j6"
}
```

#### Unsuspend User

This action is used to unsuspend a user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|login|string|None|True|The login of the Okta user|None|user@example.com|None|None|
  
Example input:

```
{
  "login": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|login|string|False|The login of the Okta user|user@example.com|
|success|boolean|True|Whether unsuspension was successful|True|
|userId|string|False|The user ID of the Okta user|00a0a1qwertYUIoplK0j6|
  
Example output:

```
{
  "login": "user@example.com",
  "success": true,
  "userId": "00a0a1qwertYUIoplK0j6"
}
```

#### Update Blacklist Zones

This action is used to block or unblock address or network by adding or removing from a blacklist network zone

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|IP address, Network range, or CIDR to block or unblock|None|198.51.100.1|None|None|
|blacklistState|boolean|True|False|True to block, false to unblock|None|True|None|None|
|name|string|None|True|Name of blacklist zone|None|InsightConnect Blacklist Zone|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|zone|zone|True|Information about the updated zone|{"links":{"deactivate":{"hints":{"allow":["POST"]},"href":"https://example.com"},"self":{"hints":{"allow":["GET","PUT","DELETE"]},"href":"https://example.com"}},"created":"2020-11-01T01:00:47.000Z","gateways":[{"type":"RANGE","value":"1.1.1.1-1.1.1.1"},{"type":"RANGE","value":"1.1.2.3-1.1.2.5"}],"id":"nzohxvr9QzHuWqXI65d5","lastUpdated":"2020-11-01T23:36:53.000Z","name":"testzone","proxies":null,"status":"ACTIVE","system":false,"type":"IP"}|
  
Example output:

```
{
  "zone": {
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
    "links": {
      "deactivate": {
        "hints": {
          "allow": [
            "POST"
          ]
        },
        "href": "https://example.com"
      },
      "self": {
        "hints": {
          "allow": [
            "GET",
            "PUT",
            "DELETE"
          ]
        },
        "href": "https://example.com"
      }
    },
    "name": "testzone",
    "proxies": null,
    "status": "ACTIVE",
    "system": false,
    "type": "IP"
  }
}
```
### Triggers


#### Monitor User Groups

This trigger is used to monitors a list of groups for user membership changes

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|groupIds|[]string|None|True|A list of group ID's|None|["00g41ix8hKbsu74Ca4x6", "00g41ieu5y7i9XEYE4x6"]|None|None|
|interval|integer|300|True|The time in seconds between checks for changes to the groups users|None|100|None|None|
  
Example input:

```
{
  "groupIds": [
    "00g41ix8hKbsu74Ca4x6",
    "00g41ieu5y7i9XEYE4x6"
  ],
  "interval": 300
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|usersAddedToGroups|[]user_group|True|Users added to a group since the last check|[{"groupName":"test1","groupId":"00g41ix8hKbsu74Ca4x6","users":[{"id":"00u44z4o0JgUYC0OO4x6","status":"PASSWORD_EXPIRED","created":"2020-03-17T19:28:50.000Z","activated":"2020-03-17T19:28:50.000Z","statusChanged":"2020-03-17T19:28:50.000Z","lastUpdated":"2020-03-17T19:28:50.000Z","passwordChanged":"2020-03-17T19:28:50.000Z","profile":{"firstName":"doe","lastName":"test","login":"user@example.com","email":"user@example.com"},"credentials":{"password":{},"provider":{"type":"OKTA","name":"OKTA"}},"links":{"self":{"href":"https://example.com"}}}]}]|
|usersRemovedFromGroups|[]user_group|True|Users removed from a group since the last check|[{"group_name":"test1","group_id":"00g41ix8hKbsu74Ca4x6","users":[{"id":"00u44xracEYPXjhwy4x6","status":"PASSWORD_EXPIRED","created":"2020-03-17T19:28:27.000Z","activated":"2020-03-17T19:28:28.000Z","statusChanged":"2020-03-17T19:28:28.000Z","lastUpdated":"2020-03-17T19:28:28.000Z","passwordChanged":"2020-03-17T19:28:27.000Z","profile":{"firstName":"bob","lastName":"test","login":"user@example.com","email":"user@example.com"},"credentials":{"password":{},"provider":{"type":"OKTA","name":"OKTA"}},"links":{"self":{"href":"https://example.com"}}}]}]|
  
Example output:

```
{
  "usersAddedToGroups": [
    {
      "groupId": "00g41ix8hKbsu74Ca4x6",
      "groupName": "test1",
      "users": [
        {
          "activated": "2020-03-17T19:28:50.000Z",
          "created": "2020-03-17T19:28:50.000Z",
          "credentials": {
            "password": {},
            "provider": {
              "name": "OKTA",
              "type": "OKTA"
            }
          },
          "id": "00u44z4o0JgUYC0OO4x6",
          "lastUpdated": "2020-03-17T19:28:50.000Z",
          "links": {
            "self": {
              "href": "https://example.com"
            }
          },
          "passwordChanged": "2020-03-17T19:28:50.000Z",
          "profile": {
            "email": "user@example.com",
            "firstName": "doe",
            "lastName": "test",
            "login": "user@example.com"
          },
          "status": "PASSWORD_EXPIRED",
          "statusChanged": "2020-03-17T19:28:50.000Z"
        }
      ]
    }
  ],
  "usersRemovedFromGroups": [
    {
      "group_id": "00g41ix8hKbsu74Ca4x6",
      "group_name": "test1",
      "users": [
        {
          "activated": "2020-03-17T19:28:28.000Z",
          "created": "2020-03-17T19:28:27.000Z",
          "credentials": {
            "password": {},
            "provider": {
              "name": "OKTA",
              "type": "OKTA"
            }
          },
          "id": "00u44xracEYPXjhwy4x6",
          "lastUpdated": "2020-03-17T19:28:28.000Z",
          "links": {
            "self": {
              "href": "https://example.com"
            }
          },
          "passwordChanged": "2020-03-17T19:28:27.000Z",
          "profile": {
            "email": "user@example.com",
            "firstName": "bob",
            "lastName": "test",
            "login": "user@example.com"
          },
          "status": "PASSWORD_EXPIRED",
          "statusChanged": "2020-03-17T19:28:28.000Z"
        }
      ]
    }
  ]
}
```
### Tasks


#### Monitor Logs

This task is used to monitor system logs

##### Input
  
*This task does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|logs|object|True|All system logs within the specified time range|[{"actor":{"id":"12345","type":"User","alternateId":"user@example.com","displayName":"User"},"client":{"userAgent":{"rawUserAgent":"python-requests/2.26.0","os":"Unknown","browser":"UNKNOWN"},"zone":"null","device":"Unknown","geographicalContext":{},"ipAddress":"198.51.100.1"},"authenticationContext":{"externalSessionId":"12345"},"displayMessage":"Suspend Okta user","eventType":"user.lifecycle.suspend","outcome":{"result":"SUCCESS"},"published":"2023-04-27T07:49:21.764Z","securityContext":{"asNumber":123456,"asOrg":"test","isp":"test","domain":"example.com","isProxy":false},"severity":"INFO","debugContext":{"debugData":{"requestId":"12345","dtHash":"111111cd0ecfb444ee1fcb9687ba8b174a3c8d251ce927e6016b871bc222222","requestUri":"/api/v1/users/12345/lifecycle/suspend","url":"/api/v1/users/12345/lifecycle/suspend?"}},"legacyEventType":"core.user.config.user_status.suspended","transaction":{"type":"WEB","id":"12345","detail":{"requestApiTokenId":"12345"}},"uuid":"9de5069c-5afe-602b-2ea0-a04b66beb2c0","version":"0","request":{"ipChain":[{"ip":"198.51.100.1","geographicalContext":{},"version":"V4"}]},"target":[{"id":"12345","type":"User","alternateId":"user@example.com","displayName":"Test User"}]}]|
  
Example output:

```
{
  "logs": [
    {
      "actor": {
        "alternateId": "user@example.com",
        "displayName": "User",
        "id": "12345",
        "type": "User"
      },
      "authenticationContext": {
        "externalSessionId": "12345"
      },
      "client": {
        "device": "Unknown",
        "geographicalContext": {},
        "ipAddress": "198.51.100.1",
        "userAgent": {
          "browser": "UNKNOWN",
          "os": "Unknown",
          "rawUserAgent": "python-requests/2.26.0"
        },
        "zone": "null"
      },
      "debugContext": {
        "debugData": {
          "dtHash": "111111cd0ecfb444ee1fcb9687ba8b174a3c8d251ce927e6016b871bc222222",
          "requestId": "12345",
          "requestUri": "/api/v1/users/12345/lifecycle/suspend",
          "url": "/api/v1/users/12345/lifecycle/suspend?"
        }
      },
      "displayMessage": "Suspend Okta user",
      "eventType": "user.lifecycle.suspend",
      "legacyEventType": "core.user.config.user_status.suspended",
      "outcome": {
        "result": "SUCCESS"
      },
      "published": "2023-04-27T07:49:21.764Z",
      "request": {
        "ipChain": [
          {
            "geographicalContext": {},
            "ip": "198.51.100.1",
            "version": "V4"
          }
        ]
      },
      "securityContext": {
        "asNumber": 123456,
        "asOrg": "test",
        "domain": "example.com",
        "isProxy": false,
        "isp": "test"
      },
      "severity": "INFO",
      "target": [
        {
          "alternateId": "user@example.com",
          "displayName": "Test User",
          "id": "12345",
          "type": "User"
        }
      ],
      "transaction": {
        "detail": {
          "requestApiTokenId": "12345"
        },
        "id": "12345",
        "type": "WEB"
      },
      "uuid": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "version": "0"
    }
  ]
}
```

### Custom Types
  
**provider**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Provider name|OKTA|
|Type|string|None|False|Provider type|OKTA|
  
**recoveryQuestion**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Answer|string|None|False|Answer for the recovery question|Example Answer|
|Recovery Question|string|None|False|Question used for account recovery|Who's a major player in the cowboy scene?|
  
**custom_password**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Value|string|None|False|Password value|password-test-1234|
  
**credentials**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Password|custom_password|None|False|Password details|{}|
|Provider|provider|None|False|Provider details|{}|
|Recovery Question|recoveryQuestion|None|False|Recovery question details|{}|
  
**logo**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HREF|string|None|False|HREF|https://example.com|
|Name|string|None|False|Name of the logo|medium|
|Type|string|None|False|Type of the file|image/png|
  
**link**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HREF|string|None|False|HREF|https://example.com|
  
**groupLinks**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Applications|link|None|False|Provides link to all applications that are assigned to the group|{}|
|Logo|[]logo|None|False|Provides links to logo images for the group if available|[]|
|Users|link|None|False|Provides link to group members|{}|
  
**group**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created|string|None|False|Timestamp when group was created|2015-02-06 10:11:28+00:00|
|Description|string|None|False|Group description|Example description|
|ID|string|None|False|Group ID|00g1emaKYZTWRYYRRTSK|
|Last Membership Updated|string|None|False|Timestamp when group's memberships were last updated|2015-11-28 19:15:32+00:00|
|Last Updated|string|None|False|Timestamp when group's profile was last updated|2015-11-28 19:15:32+00:00|
|Links|groupLinks|None|False|Links to related resources|{}|
|Name|string|None|False|Group name|Example Group|
|Object Class|[]string|None|False|Determines the group's profile|["okta:user_group"]|
|Type|string|None|False|Type of the group|OKTA_GROUP|
  
**userType**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|The identifier of the type|string|None|False|ID|otyfnjfba4ye7pgjB0g4|
  
**userProfile**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|City|string|None|False|City or locality component of user's address|San Francisco|
|Cost Center|string|None|False|Name of a cost center assigned to user|Example Cost Center|
|Country Code|string|None|False|Country name component of user's address|US|
|Department|string|None|False|Name of user's department|Engineering|
|Display Name|string|None|False|Name of the user, suitable for display to end users|Test Tester|
|Division|string|None|False|Name of user's division|R&D|
|Email|string|None|False|Primary email address of the user|user@example.com|
|Employee Number|string|None|False|Organization or company assigned unique identifier for the user|123|
|First Name|string|None|False|First name of the user|Test|
|Honorific Prefix|string|None|False|Honorific prefix(es) of the user, or title in most Western languages|Mr.|
|Honorific Suffix|string|None|False|Honorific suffix(es) of the user|Jr.|
|Last Name|string|None|False|Last name of the user|Tester|
|Locale|string|None|False|User's default location for purposes of localizing items such as currency, date time format, numerical representations, and so on|en_US|
|Login|string|None|False|Login of the user|user@example.com|
|Manager|string|None|False|Name of the user's manager, suitable for display to end users|Example Manager|
|Manager ID|string|None|False|The identifier of a user's manager|00a0a1qwertYUIoplK0j2|
|Middle Name|string|None|False|Middle name(s) of the user|Example|
|Mobile Phone|string|None|False|Mobile phone number of user|+1-555-415-1337|
|Nick Name|string|None|False|Casual way to address the user in real life|test|
|Organization|string|None|False|Name of user's organization|Okta|
|Postal Address|string|None|False|Mailing address component of user's address|Test Tester, 301 Brannan St., San Francisco 94107|
|Preferred Language|string|None|False|User's preferred written or spoken languages|en-US|
|Primary Phone|string|None|False|Primary phone number of user such as home number|+1-555-514-1337|
|Profile URL|string|None|False|URL of user's online profile|https://example.com|
|Secondary Email|string|None|False|Secondary email address of user typically used for account recovery|user@example.com|
|State|string|None|False|State or region component of user's address|CA|
|Street Address|string|None|False|Full street address component of user's address|301 Brannan St.|
|Time Zone|string|None|False|User's time zone|UTC|
|Title|string|None|False|Title of the user|Professor|
|User Type|string|None|False|Used to describe the organization to user relationship such as 'Employee' or 'Contractor'|Employee|
|ZIP Code|string|None|False|ZIP code or postal code component of user's address|94107|
  
**userLink**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Href|string|None|False|Hyperlink to the operation|https://example.com|
|Method|string|None|False|Method of the request for the operation|POST|
  
**userLinks**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Activate Link|userLink|None|False|Lifecycle action to activate the user|{}|
|Change Password Link|userLink|None|False|Changes a user's password validating the user's current password|{}|
|Change Recovery Question Link|userLink|None|False|Changes a user's recovery credential by validating the user's current password|{}|
|Deactivate Link|userLink|None|False|Lifecycle action to deactivate the user|{}|
|Expire Password Link|userLink|None|False|Lifecycle action to expire the user's password|{}|
|Forgot Password Link|userLink|None|False|Resets a user's password by validating the user's recovery credential|{}|
|Reset Factors Link|userLink|None|False|Lifecycle action to reset all MFA factors|{}|
|Reset Password Link|userLink|None|False|Lifecycle action to trigger a password reset|{}|
|Self Link|userLink|None|False|A self-referential link to this user|{}|
|Suspend Link|userLink|None|False|Lifecycle action to suspend the user|{}|
|Unlock Link|userLink|None|False|Lifecycle action to unlock a locked-out user|{}|
|Unsuspend Link|userLink|None|False|Lifecycle action to unsuspend the user|{}|
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Activated|string|None|False|When the user was activated|2023-01-01T11:11:11.000Z|
|Created|string|None|False|When the user was created|2023-01-01T11:11:11.000Z|
|Credentials|credentials|None|False|User's primary authentication and recovery credentials|{}|
|ID|string|None|False|User ID|00a0a1qwertYUIoplK0j6|
|Last Login|string|None|False|When the last login for the user was|2023-01-01T11:11:11.000Z|
|Last Updated|string|None|False|When the user was last updated|2023-01-01T11:11:11.000Z|
|Links|userLinks|None|False|Link relations for the user's current status|{}|
|Password Changed|string|None|False|When the password was changed|2023-01-01T11:11:11.000Z|
|Profile|userProfile|None|False|User profile properties|{}|
|Status|string|None|False|Current status of the user|ACTIVE|
|Status Changed|string|None|False|When the status of the user changed|2023-01-01T11:11:11.000Z|
|User Type|userType|None|False|Type of the user|{}|
  
**user_group**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Group ID|string|None|None|ID of the group|123456|
|Group Name|string|None|None|Name of the group|Example Group|
|Users|[]user|None|None|List of users|[]|
  
**hints**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Allowed Methods|[]string|None|False|Allowed Methods|["POST"]|
  
**deactivate**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Hints|hints|None|False|Hints|{}|
|HREF|string|None|False|HREF|https://example.com|
  
**zoneLinks**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Deactivate|deactivate|None|False|Deactivate|{}|
|Self|deactivate|None|False|Self|{}|
  
**gateways**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Type|string|None|False|Type|RANGE|
|Value|string|None|False|Value|198.51.100.1-198.51.100.1|
  
**zone**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created|string|None|False|Created|2023-03-31 20:13:46.284000+00:00|
|Gateways|[]gateways|None|False|Gateways|[]|
|ID|string|None|False|ID|00a0a1qwertYUIoplK0j6|
|Last Updated|string|None|False|Last updated|2023-03-31 20:13:46.284000+00:00|
|Zone Links|zoneLinks|None|False|Zone links|{}|
|Name|string|None|False|Name|BlockedIpZone|
|Proxies|[]gateways|None|False|Proxies|[]|
|Status|string|None|False|Status|ACTIVE|
|System|boolean|None|False|System|True|
|Type|string|None|False|Type|IP|
  
**factorLink**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Hints|hints|None|False|Hints for the hyperlink|{}|
|Href|string|None|False|Hyperlink to the resource|https://example.com|
  
**factorLinks**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Activate Link|factorLink|None|False|Polls factor for completion of the activation of verification|{}|
|Poll Link|factorLink|None|False|Lifecycle action to transition the factor to ACTIVE status|{}|
|Questions Link|factorLink|None|False|List of questions for the question factor type|{}|
|Resend Link|factorLink|None|False|List of delivery options to resend activation or factor challenge|{}|
|Self Link|factorLink|None|False|The actual factor|{}|
|Send Link|factorLink|None|False|List of delivery options to send an activation or factor challenge|{}|
|Verify Link|factorLink|None|False|Verify the factor|{}|
  
**factorVerificationObject**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Next Pass Code|string|None|False|OTP for current time window|654321|
|Pass Code|string|None|False|OTP for next time window|123456|
  
**factor**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created|string|None|False|Timestamp when the factor was created|2023-01-01T11:11:11.000Z|
|Embedded|object|None|False|Embedded resources related to the Factor|{}|
|Factor Type|string|None|False|Type of the factor|question|
|ID|string|None|False|Unique key for the factor, a 20 character long system-generated ID|00a0a1qwertYUIoplK0j7|
|Last Updated|string|None|False|Timestamp when the factor was last updated|2023-01-01T11:11:11.000Z|
|Factor Links|factorLinks|None|False|Discoverable resources related to the Factor|{}|
|Profile|object|None|False|Profile credentials|{}|
|Factor Provider|string|None|False|Provider of the factor|OKTA|
|Factor Status|string|None|False|Status of the factor|ACTIVE|
|Vendor Name|string|None|False|Factor Vendor Name (Same as provider but for On-Prem MFA it depends on Administrator Settings)|OKTA|
|Verify|factorVerificationObject|None|False|Specifies additional verification data for 'token' or 'token:hardware' factors|{}|
  
**appUserLinks**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Application|link|None|False|Provides a link to the application|{}|
|User|link|None|False|Provides a link to the user|{}|
  
**appUserProfile**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Email|string|None|False|User email|user@example.com|
|First Name|string|None|False|User first name|Saml|
|Last Name|string|None|False|User last name|Jackson|
|Mobile Phone|string|None|False|User mobile phone|1111111|
|Profile|string|None|False|User profile|Standard User|
|Role|string|None|False|User role|CEO|
|Second Email|string|None|False|User second email|user@example.com|
  
**appCredentials**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Password|password|None|False|Password for application|{}|
|Username|string|None|False|Username for application|test|
  
**applicationUser**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created|string|None|False|Timestamp when app user was created|2014-06-24 15:27:59+00:00|
|Credentials|appCredentials|None|False|Credentials for the assigned application|{}|
|External ID|string|None|False|User ID in the target application|70c14cc17d3745e8a9f98d599a68329c|
|ID|string|None|False|User ID|00u11z6WHMYCGPCHCRFK|
|Last Synchronization|string|None|False|Timestamp when last sync operation was executed|2014-06-24 15:27:59+00:00|
|Last Updated|string|None|False|Timestamp when app user was last updated|2014-06-24 15:27:59+00:00|
|Links|appUserLinks|None|False|Links to related resources|{}|
|Password Changed|string|None|False|Timestamp when app password last changed|2014-06-24 15:27:59+00:00|
|Profile|appUserProfile|None|False|App-specific profile for the user|{}|
|Scope|string|None|False|Scope|USER|
|Status|string|None|False|Status of app user|ACTIVE|
|Status Changed|string|None|False|Timestamp when status was last changed|2014-06-24 15:27:59+00:00|
|Synchronization state|string|None|False|Synchronization state for app user|SYNCHRONIZED|
  
**entityObject**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alternate ID|string|None|False|Alternative ID of the object|user@example.com|
|Display Name|object|None|False|Details about the object|{"signOnModeType": "OPENID_CONNECT"}|
|Display Name|string|None|False|Display name of the object|Example User|
|ID|string|None|False|ID of the object|aA23dwvzR5tIZO33ek7W|
|Type|string|None|False|Type of the object|User|
  
**userAgent**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Browser|string|None|False|If the client is a web browser, this field identifies the type of web browser|CHROME|
|OS|string|None|False|The operating system that the client runs on|MAC OS X|
|Raw User Agent|string|None|False|A raw string representation of the user agent|Mozilla/5.0 (Macintosh; Intel MAC OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36|
  
**geolocation**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Latitude|float|None|False|Latitude|39.0469|
|Longitude|float|None|False|Longitude|-77.4903|
  
**geographicalContext**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|City|string|None|False|The city that encompasses the area that contains the geolocation coordinates, if available|Ashburn|
|Country|string|None|False|Full name of the country that encompasses the area that contains the geolocation coordinates|United States|
|Geolocation|geolocation|None|False|Contains the geolocation coordinates|{}|
|Postal Code|string|None|False|Postal code of the area that encompasses the geolocation coordinates|20149|
|State|string|None|False|Full name of the state or province that encompasses the area that contains the geolocation coordinates|Virginia|
  
**clientObject**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Device|string|None|False|Type of device that the client operates from|Computer|
|Geographical Context|geographicalContext|None|False|The physical location where the client is making its request from|{}|
|ID|string|None|False|For OAuth requests, this is the ID of the OAuth client making the request. For SSWS token requests, this is the ID of the agent making the request|okta.9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|IP Address|string|None|False|IP address that the client is making its request from|198.51.100.1|
|User Agent|userAgent|None|False|The user agent that is used by an actor to perform an action|{}|
|Zone|string|None|False|The name of the zone that the client's location is mapped to|none|
  
**ipAddress**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Geographical Context|geographicalContext|None|False|Geographical context of the IP address|{}|
|IP|string|None|False|IP address|198.51.100.1|
|Source|string|None|False|Details regarding the source|Example source|
|Version|string|None|False|IP address version|V4|
  
**request**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IP Chain|[]ipAddress|None|False|If the incoming request passes through any proxies, the IP addresses of those proxies are stored here in the format: clientIp, proxy1, proxy2, and so on. This field is useful when working with trusted proxies|[]|
  
**outcome**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Reason|string|None|False|Reason for the result|Sign-on policy evaluation resulted in ALLOW|
|Result|string|None|False|Result of the action: SUCCESS, FAILURE, SKIPPED, ALLOW, DENY, CHALLENGE, UNKNOWN|ALLOW|
  
**transaction**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Detail|object|None|False|Details for this transaction|{"requestApiTokenId": "00T94e3cn9kSEO3c51s5"}|
|ID|string|None|False|Unique identifier for this transaction|C56Z_q12BqKc99a-ZqyxAA563w|
|Type|string|None|False|Describes the kind of transaction. WEB indicates a web request. JOB indicates an asynchronous task|WEB|
  
**debugContext**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Debug Data|object|None|False|Dynamic field that contains miscellaneous information that is dependent on the event type|{"requestUri": "/api/v1/users/00u3gjksoiRGRAZHLSYV/factors/smsf8luacpZJAva10x45/verify", "smsProvider: "TELESIGN", "transactionId: "268632458E3C100F5F5F594C6DC689D4"}|
  
**issuer**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Varies depending on the type of authentication. If authentication is SAML 2.0, id is the issuer in the SAML assertion. For social login, id is the issuer of the token|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Type|string|None|False|Information on the issuer and source of the SAML assertion or token|Example issuer|
  
**authenticationContext**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Authentication Provider|string|None|False|The system that proves the identity of an actor using the credentials provided to it|ACTIVE_DIRECTORY|
|Authentication Step|integer|None|False|The zero-based step number in the authentication pipeline. Currently unused and always set to 0|0|
|Credential Provider|string|None|False|A credential provider is a software service that manages identities and their associated credentials. When authentication occurs through credentials provided by a credential provider, the credential provider is recorded here|OKTA_CREDENTIAL_PROVIDER|
|Credential Type|string|None|False|The underlying technology/scheme used in the credential|PASSWORD|
|External Session ID|string|None|False|A proxy for the actor's session ID|102N1EKyPFERROGvK9wizMAPQ|
|Interface|string|None|False|The third-party user interface that the actor authenticates through, if any|Example interface|
|Issuer|issuer|None|False|The specific software entity that creates and issues the credential|{}|
  
**securityContext**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|AS Number|integer|None|False|The Autonomous system number that is associated with the autonomous system that the event request was sourced to|14618|
|AS Organization|string|None|False|The organization that is associated with the autonomous system that the event request is sourced to|amazon technologies inc.|
|Domain|string|None|False|The domain name that is associated with the IP address of the inbound event request|amazonaws.com|
|Is Proxy|boolean|None|False|Specifies whether an event's request is from a known proxy|False|
|ISP|string|None|False|The Internet service provider that is used to send the event's request|amazon.co inc.|
  
**log**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Actor|entityObject|None|False|Describes the entity that performs an action|{}|
|Authentication Context|authenticationContext|None|False|The authentication data of an action|{}|
|Client|clientObject|None|False|The client that requests an action|{}|
|Debug Context|debugContext|None|False|The debug request data of an action|{}|
|Display Message|string|None|False|The display message for an event|User accessing Okta admin app|
|Event Type|string|None|False|Type of event that is published|user.authentication.verify|
|Legacy Event Type|string|None|False|Type of legacy event|app.admin.sso.login.success|
|Outcome|outcome|None|False|The outcome of an action|{}|
|Published|string|None|False|Timestamp when the event is published|2023-03-31 20:13:46.293000+00:00|
|Request|request|None|False|The request that initiates an action|{}|
|Security Context|securityContext|None|False|The security data of an action|{}|
|Severity|string|None|False|Indicates how severe the event is: DEBUG, INFO, WARN, ERROR|INFO|
|Target|[]entityObject|None|False|Zero or more targets of an action|[]|
|Transaction|transaction|None|False|The transaction details of an action|{}|
|UUID|string|None|False|Unique identifier for an individual event|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Version|string|None|False|Versioning indicator|0|


## Troubleshooting

* Actions may fail depending on the state of the resource you attempt to operate over. They will return a best-effort message indicating why the Okta API responded the way it did when possible. Depending on the API endpoint, this message is either provided by Okta themselves, or constructed by the plugin based on the information it has at hand.

# Version History

* 4.2.14 - Updated SDK to the latest version (6.3.7) | Add task delay monitoring | Update Monitor Log Search Start Time
* 4.2.14 - Updated SDK to the latest version (6.3.3)
* 4.2.13 - Updated SDK to the latest version (6.2.5)
* 4.2.12 - Updated SDK to the latest version (v6.2.2) | Address vulnerabilities
* 4.2.11 - Initial updates for fedramp compliance | Updated SDK to the latest version
* 4.2.10 - Monitor Logs Task: Add exception handling if invalid subdomain provided
* 4.2.9 - SDK Bump to 6.1.0 | Task Connection test added
* 4.2.8 - Connection: Set appropriate error code when domain is invalid
* 4.2.7 - Updated to include latest SDK v5.4.9 | Task `Monitor Logs` updated to increase max lookback cutoff to 7 days
* 4.2.6 - Connection: Update to ensure subdomain is entered correctly. Plugin will now raise an error if this value is not present
* 4.2.5 - Monitor Logs task: Update handing of custom_config parameter
* 4.2.4 - Monitor Logs task: Update to latest SDK which adds new task custom_config parameter | Update validators to 0.22.0
* 4.2.3 - Monitor Logs task: Added exception logging and use latest plugin SDK. Also Fixed schemas that contain passwords
* 4.2.2 - Monitor Logs task: log deduplication only applied when querying Okta using since and until parameters
* 4.2.1 - Monitor Logs task: filter previously returned log events | only update time checkpoint when an event is returned | update timestamp format | set cutoff time of 24 hours
* 4.2.0 - Monitor Logs task: return raw logs data without cleaning and use last log time as checkpoint in time for next run
* 4.1.1 - Monitor Logs task: strip http/https in hostname
* 4.1.0 - New action Get User Groups | Update to latest SDK version
* 4.0.0 - Add Monitor Logs task | Code refactor | Update plugin to be cloud enabled
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
* 3.2.2 - Change docker image from `komand/python-2-plugin:2` to `komand/python-3-37-slim-plugin:3` | Use input and output constants | Changed variables names to more readable | Added `f` strings | Removed duplicated code
* 3.2.1 - New spec and help.md format for the Extension Library
* 3.2.0 - New action Delete User
* 3.1.2 - Update connection test
* 3.1.1 - Update descriptions
* 3.1.0 - New action Reset Factors
* 3.0.0 - Rename `Remove User to Group` action to `Remove User from Group`
* 2.1.0 - Improved connection code | New action Create User
* 2.0.0 - Update to new secret key credential type
* 1.1.0 - Added new Get User, Unsuspend User, Add User to Group, and List Groups actions
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Okta API Spec](https://developer.okta.com/docs/api)

## References

* [Okta API Reference](https://developer.okta.com/docs/reference)