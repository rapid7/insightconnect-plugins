# Description

[Azure](https://azure.microsoft.com) AD Admin performs administrative tasks in Azure AD.

It uses the [User](https://docs.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0) endpoint in
the [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/overview?view=graph-rest-1.0).

# Key Features

* Add and remove users
* Disable and enable users
* Force users to change their password

# Requirements

* The application this plugin connects to needs the following permissions:
  * Directory.AccessAsUser.All
  * Directory.ReadWrite.All
  * User.ReadWrite.All
* The application will need to be added to the Global Administrator role. This can be done in `Roles and administrators` in Azure Active directory via the Azure Portal.

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|application_id|string|None|True|The ID of the registered application that obtained the refresh token|None|None|
|application_secret|credential_secret_key|None|True|The secret of the registered application that obtained the refresh token|None|None|
|tenant_id|string|None|True|The ID of the directory that identifies the tenant|None|None|

## Technical Details

### Actions

#### Add User to Groups by ID

This action is used to add a user to a groups by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|group_id|[]string|None|True|IDs of Groups to Add User to|None|\["b4d41d4-eb13-4a33-99b5-7d7290df22e9"\]|
|user_id|string|None|True|User ID e.g. user@example.com|None|user@example.com|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Was operation successful|

Example output:

```
```

#### Update User Information

This action is used to update a users information.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|city|string|None|False|The city in which the user is located|None|Boston|
|country|string|None|False|The country or region in which the user is located; for example, US or UK|None|US|
|department|string|None|False|The name for the department in which the user works|None|IT|
|job_title|string|None|False|The user’s job title|None|Desktop Technician|
|state|string|None|False|The state or province in the users address|None|MA|
|user_id|string|None|True|User to updates ID|None|user@example.com|
|user_type|string|None|False|A string value that can be used to classify user types in your directory, such as Member and Guest|None|Member|

Example input:

```
{
  "city": "Boston",
  "country": "US",
  "department": "Engineering",
  "job_title": "Software Engineer",
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
|account_enabled|boolean|True|False|True if the account is enabled; otherwise, false|None|None|
|display_name|string|None|True|The name to display in the address book for the user e.g. displayName-value|None|None|
|mail_nickname|string|None|False|The mail alias for the user e.g. mailNickname-value|None|None|
|notify_email_body|string|None|False|Body of the email to be sent out. Use $password to place the generated password|None|None|
|notify_from|string|None|True|User from which email notifcation will be sent|None|None|
|notify_recipient|string|None|True|Email address of the account to be notified of user creation|None|None|
|user_principal_name|string|None|True|The user principal name e.g. user@example.com|None|None|

Example input:

```
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
|user_id|string|None|True|User ID to disable e.g. user@example.com|None|None|

Example input:

```
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
|user_id|string|None|True|User ID to enable e.g. user@example.com|None|None|

Example input:

```
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
|user_id|string|None|True|User ID|None|None|

Example input:

```
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
|user_id|string|None|True|User ID e.g. user@example.com|None|None|

Example input:

```
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
|name|string|None|True|Name|None|None|

Example input:

```
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
|group_name|string|None|True|Group Name e.g. My Azure Group|None|None|
|user_id|string|None|True|User ID e.g. user@example.com|None|None|

Example input:

```
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
|group_name|string|None|True|Group Name e.g. My Azure Group|None|None|
|user_id|string|None|True|User ID e.g. user@example.com|None|None|

Example input:

```
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
|frequency|integer|60|False|Poll frequency in seconds|None|None|
|risk_level|string|None|True|Risk level|['low', 'medium', 'high', 'hidden', 'none', 'all']|None|

Example input:

```
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

### user_information

|Name|Type|Required|Description|
|----|----|--------|-----------|
|@odata.context|string|False|@odata.context|
|accountEnabled|boolean|False|Account enabled|
|businessPhones|[]string|False|Business phones|
|displayName|string|False|Display name|
|givenName|string|False|Given Name|
|id|string|False|ID|
|jobTitle|string|False|Job title|
|mail|string|False|Mail|
|mobilePhone|string|False|Mobile phone|
|officeLocation|string|False|Office location|
|preferredLanguage|string|False|Preferred language|
|surname|string|False|Surname|
|userPrincipalName|string|False|User principal name|

### group

|Name|Type|Required|Description|
|----|----|--------|-----------|
|createdDateTime|string|False|Created date time|
|description|string|False|Description|
|displayName|string|False|Display name|
|groupTypes|[]string|False|Group types|
|id|string|False|ID|
|isAssignableToRole|boolean|False|Is assignable to role|
|mail|string|False|Mail|
|mailEnabled|boolean|False|Mail enabled|
|mailNickname|string|False|Mail nickname|
|proxyAddresses|[]string|False|Proxy addresses|
|renewedDateTime|string|False|Renewed date time|
|securityEnabled|boolean|False|Security enabled|
|visibility|string|False|Visibility|

### geo_coordinates

|Name|Type|Required|Description|
|----|----|--------|-----------|
|altitude|string|False|The altitude (height), in feet, above sea level|
|latitude|string|False|The latitude, in decimal|
|longitude|string|False|The longitude, in decimal|

### sign_in_location

|Name|Type|Required|Description|
|----|----|--------|-----------|
|city|string|False|City where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity|
|country_or_region|string|False|Country code info (2 letter code) where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity|
|geo_coordinates|geo_coordinates|False|Geo coordinates|
|state|string|False|State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity|

### risk

|Name|Type|Required|Description|
|----|----|--------|-----------|
|activity|string|False|Indicates the activity type the detected risk is linked to. The possible values are signin, user, unknownFutureValue|
|activity_date_time|string|False|Date and time that the risky activity occurred|
|additional_info|string|False|Additional information associated with the risk detection|
|correlation_id|string|False|Correlation ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in|
|detected_date_time|string|False|Date and time that the risk was detected|
|detection_timing_type|string|False|Timing of the detected risk (real-time/offline). The possible values are notDefined, realtime, nearRealtime, offline, unknownFutureValue|
|id|string|True|Unique ID of the risk detection|
|ip_address|string|False|IP address of the client from where the risk occurred|
|last_updated_date_time|string|False|Date and time that the risk detection was last updated|
|location|sign_in_location|False|Location of the client from where the risk occurred|
|request_id|string|False|Request ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in|
|risk_detail|string|False|Details of the detected risk. Details for this property are only available for Azure AD Premium P2 customers. P1 customers will be returned hidden|
|risk_level|string|False|Level of the detected risk|
|risk_state|string|False|The state of a detected risky user or sign-in|
|risk_type|string|False|The type of risk event detected|
|source|string|False|Source of the risk detection. For example, activeDirectory|
|token_issuer_type|string|False|Indicates the activity type the detected risk is linked to. The possible values are signin, user, unknownFutureValue|
|user_display_name|string|False|User display name|
|user_id|string|False|User ID|
|user_principal_name|string|False|The user principal name (UPN) of the user|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

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

## References

* [Azure AD Admin](https://azure.microsoft.com)
* [User API](https://docs.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)
* [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/overview?view=graph-rest-1.0)
