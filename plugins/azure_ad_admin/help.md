# Description

[Azure](https://azure.microsoft.com) AD Admin performs administrative tasks in Azure AD.

It uses the [User](https://docs.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0) endpoint in
the [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/overview?view=graph-rest-1.0).

# Key Features

* Add and remove users
* Disable and enable users
* Force users to change their password
* Enable, disable, get, search and delete devices

# Requirements

* The application this plugin connects to needs the following permissions:
  * Directory.AccessAsUser.All
  * Directory.ReadWrite.All
  * User.ReadWrite.All
  * IdentityRiskEvent.Read.All (Types: Delegated, Application)
  * Device.ReadWrite.All
* The application will need to be added to the Global Administrator role. This can be done in `Roles and administrators` in Azure Active directory via the Azure Portal.

# Supported Product Versions

* 2022-05-30

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|application_id|string|None|True|The ID of the registered application that obtained the refresh token|None|6731de76-14a6-49ae-97bc-6eba6914391e|
|application_secret|credential_secret_key|None|True|The secret of the registered application that obtained the refresh token|None|JqQX2PNo9bpM0uEihUPzyrh|
|tenant_id|string|None|True|The ID of the directory that identifies the tenant|None|5ceea899-ae8c-4ff1-fffe-353646eeeff0|

Example input:

```
{
  "application_id": "6731de76-14a6-49ae-97bc-6eba6914391e",
  "application_secret": "JqQX2PNo9bpM0uEihUPzyrh",
  "tenant_id": "5ceea899-ae8c-4ff1-fffe-353646eeeff0"
}
```


## Technical Details

### Actions

#### Search Device

This action is used to search for devices using a given query. For more information about queries visit https://learn.microsoft.com/en-us/graph/filter-query-parameter?tabs=http; https://learn.microsoft.com/en-us/graph/search-query-parameter?tabs=http; https://learn.microsoft.com/en-us/graph/aad-advanced-queries?tabs=http#device-properties.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filter|string|None|False|Filter devices by query. See details about query in action description|None|approximateLastSignInDateTime le 2021-06-11T18:01:51Z|
|orderBy|string|None|False|Sorts list results by the provided device parameter|None|displayName|
|search|string|None|False|Search parameters by query. See details about query in action description|None|displayName:INTUNE|
|select|[]string|None|False|Fields to be included in the output|None|["id", "createdDateTime"]|

Example input:

```
{
  "filter": "approximateLastSignInDateTime le 2021-06-11T18:01:51Z",
  "orderBy": "displayName",
  "search": "displayName:INTUNE",
  "select": [
    "id",
    "createdDateTime"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|devices|[]device|False|Information about the devices|[]|

Example output:

```
{
  "devices": [
    {
      "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "accountEnabled": true,
      "approximateLastSignInDateTime": "2020-06-20T21:15:48Z",
      "createdDateTime": "2020-06-10T23:11:21Z",
      "deviceId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "deviceOwnership": "Company",
      "deviceVersion": 2,
      "displayName": "DESKTOP-D10L83K",
      "enrollmentType": "AzureDomainJoined",
      "exchangeActiveSyncIds": [
        "eas:415F14BD1A98FEA919DF00327EA5DC81:9de5069c-5afe-602b-2ea0-a04b66beb2c0:20200610T231818"
      ],
      "isCompliant": false,
      "isManaged": true,
      "isRooted": false,
      "managementType": "MDM",
      "manufacturer": "innotek GmbH",
      "mdmAppId": "0000000a-0000-0000-c000-000000000000",
      "model": "VirtualBox",
      "operatingSystem": "Windows",
      "operatingSystemVersion": "10.0.19041.329",
      "physicalIds": [
        "[USER-GID]:9de5069c-5afe-602b-2ea0-a04b66beb2c0:6755416654410028",
        "[GID]:g:6755416654410028",
        "[USER-HWID]:9de5069c-5afe-602b-2ea0-a04b66beb2c0:6755416654410025",
        "[HWID]:h:6755416654410025"
      ],
      "profileType": "RegisteredDevice",
      "registrationDateTime": "2020-06-10T23:11:20Z",
      "systemLabels": [],
      "trustType": "AzureAd",
      "alternativeSecurityIds": [
        {
          "type": 2,
          "key": "WAA1ADAAOQA6ADwAUwBIAEEAM"
        }
      ]
    }
  ]
}
```

#### Get Device

This action is used to get the device with the given ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|deviceId|string|None|True|ID of the device|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|

Example input:

```
{
  "deviceId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|device|device|False|Information about the device|{}|

Example output:

```
{
  "device": {
    "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
    "accountEnabled": true,
    "approximateLastSignInDateTime": "2020-06-20T21:15:48Z",
    "createdDateTime": "2020-06-10T23:11:21Z",
    "deviceId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
    "deviceOwnership": "Company",
    "deviceVersion": 2,
    "displayName": "DESKTOP-D10L83K",
    "enrollmentType": "AzureDomainJoined",
    "exchangeActiveSyncIds": [
      "eas:415F14BD1A98FEA919DF00327EA5DC81:9de5069c-5afe-602b-2ea0-a04b66beb2c0:20200610T231818"
    ],
    "isCompliant": false,
    "isManaged": true,
    "isRooted": false,
    "managementType": "MDM",
    "manufacturer": "innotek GmbH",
    "mdmAppId": "0000000a-0000-0000-c000-000000000000",
    "model": "VirtualBox",
    "operatingSystem": "Windows",
    "operatingSystemVersion": "10.0.19041.329",
    "physicalIds": [
      "[USER-GID]:9de5069c-5afe-602b-2ea0-a04b66beb2c0:6755416654410028",
      "[GID]:g:6755416654410028",
      "[USER-HWID]:9de5069c-5afe-602b-2ea0-a04b66beb2c0:6755416654410025",
      "[HWID]:h:6755416654410025"
    ],
    "profileType": "RegisteredDevice",
    "registrationDateTime": "2020-06-10T23:11:20Z",
    "trustType": "AzureAd",
    "alternativeSecurityIds": [
      {
        "type": 2,
        "key": "WAA1ADAAOQA6ADwAUwBIAEEAM"
      }
    ]
  }
}
```

#### Enable Device

This action is used to enable the device with the given ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|deviceId|string|None|True|ID of the device|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|

Example input:

```
{
  "deviceId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Whether the action was successful|true|

Example output:

```
{
  "success": true
}
```

#### Disable Device

This action is used to disable the device with the given ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|deviceId|string|None|True|ID of the device|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|

Example input:

```
{
  "deviceId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Whether the action was successful|true|

Example output:

```
{
  "success": true
}
```

#### Delete Device

This action is used to delete the device with the given ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|deviceId|string|None|True|ID of the device|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|

Example input:

```
{
  "deviceId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Whether the action was successful|true|

Example output:

```
{
  "success": true
}
```

#### Change User Password

This action is used to change a user password by an administrator with appropriate permissions.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|new_password|password|None|True|The new password|None|newPassword|
|user_id|string|None|True|User ID to password change|None|user@example.com|

Example input:

```
{
  "new_password": "newPassword",
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "success": true
}
```

#### Revoke Sign-In Sessions

This action invalidates all the refresh tokens issued to applications for a user (as well as session cookies in a user's browser), by resetting the signInSessionsValidFromDateTime user property to the current date-time.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|user_id|string|None|True|User ID to revoke|None|user@example.com|

Example input:

```
{
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was the operation successful|

Example output:

```
{
  "success": true
}
```

#### Add User to Groups by ID

This action is used to add a user to a set of groups by group ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|group_id|[]string|None|True|IDs of Groups to Add User to|None|["b4d41d4-eb13-4a33-99b5-7d7290df22e9"]|
|user_id|string|None|True|User ID to add|None|user@example.com|

Example input:

```
{
  "group_id": [
    "b4d41d4-eb13-4a33-99b5-7d7290df22e9"
  ],
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Was operation successful|

Example output:

```
{
  "success": true
}
```

#### Update User Information

This action is used to update a users information.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|city|string|None|False|The city in which the user is located|None|Boston|
|country|string|None|False|The country or region in which the user is located; for example, US or UK|None|US|
|department|string|None|False|The name for the department in which the user works|None|IT|
|job_title|string|None|False|The user's job title|None|Desktop Technician|
|state|string|None|False|The state or province in the users address|None|MA|
|user_id|string|None|True|User to updates ID|None|user@example.com|
|user_type|string|None|False|A string value that can be used to classify user types in your directory, such as Member and Guest|None|Member|

Example input:

```
{
  "city": "Boston",
  "country": "US",
  "department": "IT",
  "job_title": "Desktop Technician",
  "state": "MA",
  "user_id": "user@example.com",
  "user_type": "Member"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "success": true
}
```

#### Create User and Notify

This action is used to create a user with a randomly generated password and send out an email with the password.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|account_enabled|boolean|True|False|True if the account is enabled; otherwise, false|None|True|
|display_name|string|None|True|The name to display in the address book for the user|None|displayName-value|
|mail_nickname|string|None|False|The mail alias for the user|None|user@example.com|
|notify_email_body|string|None|False|Body of the email to be sent out. Use $password to place the generated password|None|Example message to send|
|notify_from|string|None|True|User from which email notifcation will be sent|None|user@example.com|
|notify_recipient|string|None|True|Email address of the account to be notified of user creation|None|user@example.com|
|user_principal_name|string|None|True|The user principal name|None|user@example.com|

Example input:

```
{
  "account_enabled": true,
  "display_name": "displayName-value",
  "mail_nickname": "user@example.com",
  "notify_email_body": "Example message to send",
  "notify_from": "user@example.com",
  "notify_recipient": "user@example.com",
  "user_principal_name": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Did the step succeed|

Example output:

```
{
  "success": true
}
```

#### Disable User Account

This action is used to disable a user account. This action will not disable an administrative account.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|user_id|string|None|True|User ID to disable|None|user@example.com|

Example input:

```
{
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "success": true
}
```

#### Enable User Account

This action is used to enable a user account.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|user_id|string|None|True|User ID to enable|None|user@example.com|

Example input:

```
{
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "success": true
}
```

#### Force User to Change Password

This action forces a user to change their password on their next successful login.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|user_id|string|None|True|User ID to password change|None|user@example.com|

Example input:

```
{
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "success": true
}
```

#### Get User Info

This action is used to get user information.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|user_id|string|None|True|Retrieve information about specific User ID|None|user@example.com|

Example input:

```
{
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user_information|user_information|True|Information about a user|

Example output:

```
{
  "user_information": {
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users/$entity",
    "businessPhones": [],
    "displayName": "Joey McAdams",
    "givenName": "Joey",
    "jobTitle": "Sr. Software Engineer",
    "mail": "",
    "mobilePhone": "",
    "officeLocation": "",
    "preferredLanguage": "",
    "surname": "McAdams",
    "userPrincipalName": "user@example.com",
    "id": "08290005-23ba-46b4-a377-b381d651a2fb",
    "accountEnabled": true
  }
}
```

#### Get Group by Name

This action is used to get a group by it's name.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|Display name to filter|None|displayName|

Example input:

```
{
  "name": "displayName"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|group|group|False|Group|

Example output:

```
{
  "group": {
    "id": "bb4d41d4-eb13-4a33-99b5-7d7290df22e9",
    "deletedDateTime": null,
    "classification": null,
    "createdDateTime": "2019-09-20T12:15:21Z",
    "creationOptions": [],
    "description": "Azure AD Test Group",
    "displayName": "Azure AD Test Group",
    "groupTypes": [
      "Unified"
    ],
    "isAssignableToRole": false,
    "mail": "user@example.com",
    "mailEnabled": true,
    "mailNickname": "AzureADTestGroup",
    "onPremisesLastSyncDateTime": null,
    "onPremisesSecurityIdentifier": null,
    "onPremisesSyncEnabled": null,
    "preferredDataLocation": null,
    "proxyAddresses": [
      "SPO:SPO_618d645a-541b-4349-a7c0-3bb73eedd701@SPO_5c824599-dc8c-4d31-96fb-3b886d4f8f10",
      "SMTP:user@example.com"
    ],
    "renewedDateTime": "2019-09-20T12:15:21Z",
    "resourceBehaviorOptions": [],
    "resourceProvisioningOptions": [],
    "securityEnabled": true,
    "visibility": "Public",
    "onPremisesProvisioningErrors": []
  }
}
```

#### Add User to Group

This action is used to add a user to a group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|group_name|string|None|True|Name of the group to add a user to|None|Example Group Name|
|user_id|string|None|True|User ID|None|user@example.com|

Example input:

```
{
  "group_name": "Example Group Name",
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Was operation successful|

Example output:

```
{
  "success": true
}
```

#### Remove User from Group

This action is used to remove a user from a group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|group_name|string|None|True|Group Name to manage|None|Example Group Name|
|user_id|string|None|True|User ID to remove from group|None|user@example.com|

Example input:

```
{
  "group_name": "Example Group Name",
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Was operation successful|

Example output:

```
{
  "success": true
}
```

### Triggers

#### Risk Detection

This trigger provides list of both user and sign-in linked risk detections and associated information about the detection.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|frequency|integer|60|False|Poll frequency in seconds|None|60|
|risk_level|string|None|True|Risk level|['low', 'medium', 'high', 'hidden', 'none', 'all']|all|

Example input:

```
{
  "frequency": 60,
  "risk_level": "all"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk|risk|True|Risk|

Example output:

```
{
  "risk":
    {
      "id": "04da6f53cd292d990314fd05b2ba6cc06b3acc3a2eb85bf2fe6d48f2edbec301",
      "requestId": "04c82f8e-f0c0-4971-a546-c18125fa3300",
      "correlationId": "0977e5da-93a4-4e97-b1a2-bb03b8007e93",
      "riskType": "unfamiliarFeatures",
      "riskState": "atRisk",
      "riskLevel": "low",
      "riskDetail": "none",
      "source": "IdentityProtection",
      "detectionTimingType": "realtime",
      "activity": "signin",
      "tokenIssuerType": "AzureAD",
      "ipAddress": "66.207.205.214",
      "activityDateTime": "2019-11-25T14:09:08.6953666Z",
      "detectedDateTime": "2019-11-25T14:09:08.6953666Z",
      "lastUpdatedDateTime": "2019-11-25T14:12:04.5431877Z",
      "userId": "ac785ffe-530a-45a1-bbf4-e275457e464b",
      "userDisplayName": "User Name",
      "userPrincipalName": "user@domain",
      "additionalInfo": "[{\"Key\":\"userAgent\",\"Value\":\"python-requests/2.22.0\"}]",
      "location":
        {
          "city": "Toronto",
          "state": "Ontario",
          "countryOrRegion": "CA",
          "geoCoordinates":
            {
              "latitude": 43.63831,
              "longitude": -79.42555
            }
        }
    }
}
```

#### Risk Detection

This trigger provides a list of both user and sign-in linked risk detections and associated information about the detection.

### Custom Output Types

#### alternativeSecurityId

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Identity Provider|string|False|Identity provider|
|Key|string|False|Key|
|Type|integer|False|Type|

#### device

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Account Enabled|boolean|False|True if the account is enabled; otherwise, false|
|Alternative Security IDs|[]alternativeSecurityId|False|List of alternative security IDs|
|Approximate Last Sign In Datetime|string|False|The timestamp of last login in ISO 8601 format and in UTC time|
|Compliant Expiration Datetime|string|False|The timestamp when the device is no longer deemed compliant|
|Device Category|string|False|User-defined property set by Intune to automatically add devices to groups and simplify managing devices|
|Device ID|string|False|Unique identifier set by Azure Device Registration Service at the time of registration|
|Device Metadata|string|False|Metadata of the device|
|Device Ownership|string|False|Ownership of the device|
|Device Version|integer|False|Version of the device|
|Display Name|string|False|The display name for the device|
|Enrollment Profile Name|string|False|Enrollment profile name of the device|
|Enrollment Type|string|False|Enrollment type of the device|
|Exchange Active Sync IDs|[]string|False|Exchange active sync IDs of the device|
|Extension Attributes|extensionAttributes|False|Contains extension attributes 1-15 for the device|
|ID|string|False|The unique identifier for the device|
|Is Compliant|boolean|False|Whether the device complies with Mobile Device Management (MDM) policies|
|Is Managed|boolean|False|Whether the device is managed by Mobile Device Management (MDM)|
|Is Rooted|boolean|False|Whether the device is rooted|
|Management Type|string|False|Management type of the device|
|Manufacturer|string|False|Manufacturer of the device|
|Mobile Device Management App ID|string|False|Application identifier used to register device into MDM|
|Model|string|False|Model of the device|
|On Premises Last Sync Date Time|string|False|The last time at which the object was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time.|
|On Premises Sync Enabled|boolean|False|Whether the object is synced from an on-premises directory|
|Operating System|string|False|The type of operating system on the device|
|Operating System Version|string|False|The version of the operating system on the device|
|Physical IDs|[]string|False|List of physical IDs|
|Profile Type|string|False|The profile type of the device|
|Registration Date Time|string|False|Date and time of when the device was registered. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time|
|System Labels|[]string|False|List of labels applied to the device by the system|
|Trust Type|string|False|Type of trust for the joined device|

#### extensionAttributes

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Extension Attribute 1|string|False|First customizable extension attribute|
|Extension Attribute 10|string|False|Tenth customizable extension attribute|
|Extension Attribute 11|string|False|Eleventh customizable extension attribute|
|Extension Attribute 12|string|False|Twelfth customizable extension attribute|
|Extension Attribute 13|string|False|Thirteenth customizable extension attribute|
|Extension Attribute 14|string|False|Fourteenth customizable extension attribute|
|Extension Attribute 15|string|False|Fifteenth customizable extension attribute|
|Extension Attribute 2|string|False|Second customizable extension attribute|
|Extension Attribute 3|string|False|Third customizable extension attribute|
|Extension Attribute 4|string|False|Fourth customizable extension attribute|
|Extension Attribute 5|string|False|Fifth customizable extension attribute|
|Extension Attribute 6|string|False|Sixth customizable extension attribute|
|Extension Attribute 7|string|False|Seventh customizable extension attribute|
|Extension Attribute 8|string|False|Eighth customizable extension attribute|
|Extension Attribute 9|string|False|Ninth customizable extension attribute|

#### geo_coordinates

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Altitude|string|False|The altitude (height), in feet, above sea level|
|Latitude|string|False|The latitude, in decimal|
|Longitude|string|False|The longitude, in decimal|

#### group

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Created Date Time|string|False|Created date time|
|Description|string|False|Description|
|Display Name|string|False|Display name|
|Group Types|[]string|False|Group types|
|ID|string|False|ID|
|Is Assignable to Role|boolean|False|Is assignable to role|
|Mail|string|False|Mail|
|Mail Enabled|boolean|False|Mail enabled|
|Mail Nickname|string|False|Mail nickname|
|Proxy Addresses|[]string|False|Proxy addresses|
|Renewed Date Time|string|False|Renewed date time|
|Security Enabled|boolean|False|Security enabled|
|Visibility|string|False|Visibility|

#### manager

|Name|Type|Required|Description|
|----|----|--------|-----------|
|@odata.type|string|False|@odata.type|
|Account Enabled|boolean|False|Account Enabled|
|Age Group|string|False|Age Group|
|Assigned Licenses|[]object|False|Assigned Licenses|
|Assigned Plans|[]object|False|Assigned Plans|
|Authorization Info|object|False|Authorization Info|
|Business Phones|[]string|False|Business phones|
|Company Name|string|False|Company Name|
|Consent Provided For Minor|string|False|Consent Provided For Minor|
|Country|string|False|Country|
|Created Date Time|date|False|Created Date Time|
|Creation Type|string|False|Creation Type|
|Deleted Date Time|date|False|Deleted Date Time|
|Department|string|False|Department|
|Display Name|string|False|Display Name|
|Employee Hire Date|date|False|Employee Hire Date|
|Employee ID|string|False|Employee ID|
|Employee Org Data|string|False|Employee Org Data|
|Employee Type|string|False|Employee Type|
|External User State|string|False|External User State|
|External User State Change Date Time|string|False|External User State Change Date Time|
|Fax Number|string|False|Fax Number|
|Given Name|string|False|Given Name|
|ID|string|False|Manager ID|
|Identities|[]object|False|Identities|
|Im Addresses|[]string|False|Im Addresses|
|Is Resource Account|boolean|False|Is Resource Account|
|Job Title|string|False|Job Title|
|Legal Age Group Classification|string|False|Legal Age Group Classification|
|Mail|string|False|Mail|
|Mail Nickname|string|False|Mail Nickname|
|Mobile Phone|string|False|Mobile Phone|
|Office Location|string|False|Office Location|
|On Premises Distinguished Name|string|False|On Premises Distinguished Name|
|On Premises Domain Name|string|False|On Premises Domain Name|
|On Premises Extension Attributes|object|False|On Premises Extension Attributes|
|On Premises Immutable ID|string|False|On Premises Immutable ID|
|On Premises Last Sync Date Time|date|False|On Premises Last Sync Date Time|
|On Premises Provisioning Errors|[]string|False|On Premises Provisioning Errors|
|On Premises Sam Account Name|string|False|On Premises Sam Account Name|
|On Premises Security Identifier|string|False|On Premises Security Identifier|
|On Premises Sync Enabled|boolean|False|On Premises Sync Enabled|
|On Premises User Principal Name|string|False|On Premises User Principal Name|
|Other Mails|[]string|False|Other Mails|
|Password Policies|string|False|Password Policies|
|Password Profile|object|False|Password Profile|
|Postal Code|string|False|Postal Code|
|Preferred Data Location|string|False|Preferred Data Location|
|Provisioned Plans|[]object|False|Provisioned Plans|
|Proxy Addresses|[]string|False|Proxy Addresses|
|Refresh Tokens Valid From Date Time|date|False|Refresh Tokens Valid From Date Time|
|Show In Address List|boolean|False|Show In Address List|
|Sign In Sessions Valid From Date Time|date|False|Sign In Sessions Valid From Date Time|
|State|string|False|State|
|Street Address|string|False|Street Address|
|Surname|string|False|Surname|
|Usage Location|string|False|Usage Location|
|User Principal Name|string|False|User Principal Name|
|User Type|string|False|User Type|

#### risk

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Activity|string|False|Indicates the activity type the detected risk is linked to. The possible values are signin, user, unknownFutureValue|
|Activity Date Time|string|False|Date and time that the risky activity occurred|
|Additional Information|string|False|Additional information associated with the risk detection|
|Correlation ID|string|False|Correlation ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in|
|Detected Date Time|string|False|Date and time that the risk was detected|
|Detection Timimg Type|string|False|Timing of the detected risk (real-time/offline). The possible values are notDefined, realtime, nearRealtime, offline, unknownFutureValue|
|ID|string|True|Unique ID of the risk detection|
|IP Address|string|False|IP address of the client from where the risk occurred|
|Last Updated Date Time|string|False|Date and time that the risk detection was last updated|
|Location|sign_in_location|False|Location of the client from where the risk occurred|
|Request ID|string|False|Request ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in|
|Risk Detail|string|False|Details of the detected risk. Details for this property are only available for Azure AD Premium P2 customers. P1 customers will be returned hidden|
|Risk Level|string|False|Level of the detected risk|
|Risk State|string|False|The state of a detected risky user or sign-in|
|Risk Type|string|False|The type of risk event detected|
|Risk Level|string|False|Source of the risk detection. For example, activeDirectory|
|Token Issuer Type|string|False|Indicates the type of token issuer for the detected sign-in risk. The possible values are AzureAD, ADFederationServices, and unknownFutureValue|
|User Display Name|string|False|User display name|
|User ID|string|False|User ID|
|User Principal Name|string|False|The user principal name (UPN) of the user|

#### sign_in_location

|Name|Type|Required|Description|
|----|----|--------|-----------|
|City|string|False|City where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity|
|Country Or Region|string|False|Country code info (2 letter code) where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity|
|Geo Coordinates|geo_coordinates|False|Geo coordinates|
|State|string|False|State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity|

#### user_information

|Name|Type|Required|Description|
|----|----|--------|-----------|
|@odata.Context|string|False|@odata.context|
|Account Enabled|boolean|False|Account enabled|
|Business Phones|[]string|False|Business phones|
|Display Name|string|False|Display name|
|Given Name|string|False|Given Name|
|ID|string|False|ID|
|Job Title|string|False|Job title|
|Mail|string|False|Mail|
|Manager|manager|False|Manager|
|Mobile Phone|string|False|Mobile phone|
|Office Location|string|False|Office location|
|Preferred Language|string|False|Preferred language|
|Surname|string|False|Surname|
|User Principal Name|string|False|User principal name|

## Troubleshooting

Trigger `risk_detection` needs Application permission to set as `IdentityRiskEvent.Read.All` 

# Version History

* 4.1.1 - Update requirements in help.md
* 4.1.0 - New actions Enable Device, Disable Device, Get Device, Search Device, Delete Device
* 4.0.0 - Get User Info action: fix data validation | New action: Change User Password
* 3.0.1 - Enable cloud orchestrator
* 3.0.0 - Fix issue with incorrect data validation in Get User Info action
* 2.2.6 - Update SDK runtime | Adding additional manager response to Get User Info action
* 2.2.5 - Correct spelling in help.md
* 2.2.4 - Fix issue where Get User Info would fail on a disabled account
* 2.2.3 - Fix issue where Get User Info occasionally fails with an SSL error in secondary call for user status
* 2.2.2 - Fix issue where retry expected a valid response
* 2.2.1 - Fix issue where Get User Info occasionally fails with an SSL error
* 2.2.0 - New action Revoke Sign-In Sessions
* 2.1.1 - Update incorrect title of `user_type` to User Type  |  Return `group_id` in Add User to Groups By IDs action's error message to improve debugging
* 2.1.0 - New action Add User to Groups By IDs
* 2.0.0 - New action Update User Info
* 1.4.1 - Extension Library styling update
* 1.4.0 - New trigger Risk Detection
* 1.3.1 - New spec and help.md format for the Extension Library
* 1.3.0 - New action Create User
* 1.2.0 - New actions Get Group by Name, Add User to Group, and Remove User from Group
* 1.1.0 - New action Force User to Change Password
* 1.0.0 - Initial plugin

# Links

* [Azure AD Admin](https://azure.microsoft.com)

## References

* [User API](https://docs.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)
* [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/overview?view=graph-rest-1.0)
