# Description

[Azure](https://azure.microsoft.com) AD Admin performs administrative tasks in Azure AD.

It uses the [User](https://docs.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0) endpoint in the [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/overview?view=graph-rest-1.0)

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

All those permissions can be set in Azure Portal. Under `App registrations` -> `<SELECT_YOUR_AZURE_AD_ADMIN_APP>` -> `API permissions`.

* The application will need to be added to the `Global Administrator` role. This can be done in `Roles and administrators` in Microsoft Entra ID (Azure Active Directory) via the Azure Portal. 

To set this up, go to `Microsoft Entra ID` -> `Application Registrations`. Select the application to which you want to add the role and open the `Roles and Administrators` tab. Above the `Roles` table you will see a note saying `[...] this resource and can only be assigned here at directory level`. Click on this `here` link. 

This should open the `All Roles' tab. Locate `Global Administrator` and click on it. To add your application to the role, you'll need to click the `Add assignments` button. Browse and select your application and click `Add`.

# Supported Product Versions

* 2022-05-30

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|application_id|string|None|True|The ID of the registered application that obtained the refresh token|None|6731de76-14a6-49ae-97bc-6eba6914391e|None|None|
|application_secret|credential_secret_key|None|True|The secret of the registered application that obtained the refresh token|None|JqQX2PNo9bpM0uEihUPzyrh|None|None|
|tenant_id|string|None|True|The ID of the directory that identifies the tenant|None|5ceea899-ae8c-4ff1-fffe-353646eeeff0|None|None|

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


#### Add User to Group

This action is used to add a user to a group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|group_name|string|None|True|Name of the group to add a user to|None|Example Group Name|None|None|
|user_id|string|None|True|User ID|None|user@example.com|None|None|
  
Example input:

```
{
  "group_name": "Example Group Name",
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Was operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Add User to Groups by ID

This action is used to add a user to a set of groups by group ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|group_id|[]string|None|True|IDs of Groups to Add User to|None|["b4d41d4-eb13-4a33-99b5-7d7290df22e9"]|None|None|
|user_id|string|None|True|User ID to add|None|user@example.com|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Was operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Change User Password

This action is used to change a user password by an administrator with appropriate permissions

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|new_password|password|None|True|The new password|None|newPassword|None|None|
|user_id|string|None|True|User ID to password change|None|user@example.com|None|None|
  
Example input:

```
{
  "new_password": "newPassword",
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Create User and Notify

This action is used to create a user with a randomly generated password and send out an email with the password

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|account_enabled|boolean|True|False|True if the account is enabled; otherwise, false|None|True|None|None|
|display_name|string|None|True|The name to display in the address book for the user|None|displayName-value|None|None|
|mail_nickname|string|None|False|The mail alias for the user|None|user@example.com|None|None|
|notify_email_body|string|None|False|Body of the email to be sent out. Use $password to place the generated password|None|Example message to send|None|None|
|notify_from|string|None|True|User from which email notifcation will be sent|None|user@example.com|None|None|
|notify_recipient|string|None|True|Email address of the account to be notified of user creation|None|user@example.com|None|None|
|user_principal_name|string|None|True|The user principal name|None|user@example.com|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Did the step succeed|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete Device

This action is used to delete the device with the given ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|deviceId|string|None|True|ID of the device|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|None|None|
  
Example input:

```
{
  "deviceId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Disable Device

This action is used to disable the device with the given ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|deviceId|string|None|True|ID of the device|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|None|None|
  
Example input:

```
{
  "deviceId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Disable User Account

This action is used to disable a user account. This action will not disable an administrative account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|user_id|string|None|True|User ID to disable|None|user@example.com|None|None|
  
Example input:

```
{
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Enable Device

This action is used to enable the device with the given ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|deviceId|string|None|True|ID of the device|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|None|None|
  
Example input:

```
{
  "deviceId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Enable User Account

This action is used to enable a user account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|user_id|string|None|True|User ID to enable|None|user@example.com|None|None|
  
Example input:

```
{
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Force User to Change Password

This action is used to forces a user to change their password on their next successful login

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|user_id|string|None|True|User ID to password change|None|user@example.com|None|None|
  
Example input:

```
{
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Get Device

This action is used to get the device with the given ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|deviceId|string|None|True|ID of the device|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|None|None|
  
Example input:

```
{
  "deviceId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|device|device|False|Information about the device|{"id":"9de5069c-5afe-602b-2ea0-a04b66beb2c0","accountEnabled":true,"approximateLastSignInDateTime":"2020-06-20T21:15:48Z","createdDateTime":"2020-06-10T23:11:21Z","deviceId":"9de5069c-5afe-602b-2ea0-a04b66beb2c0","deviceOwnership":"Company","deviceVersion":2,"displayName":"DESKTOP-D10L83K","enrollmentType":"AzureDomainJoined","exchangeActiveSyncIds":["eas:415F14BD1A98FEA919DF00327EA5DC81:9de5069c-5afe-602b-2ea0-a04b66beb2c0:20200610T231818"],"isCompliant":false,"isManaged":true,"isRooted":false,"managementType":"MDM","manufacturer":"innotek GmbH","mdmAppId":"0000000a-0000-0000-c000-000000000000","model":"VirtualBox","operatingSystem":"Windows","operatingSystemVersion":"10.0.19041.329","physicalIds":["[USER-GID]:9de5069c-5afe-602b-2ea0-a04b66beb2c0:6755416654410028","[GID]:g:6755416654410028","[USER-HWID]:9de5069c-5afe-602b-2ea0-a04b66beb2c0:6755416654410025","[HWID]:h:6755416654410025"],"profileType":"RegisteredDevice","registrationDateTime":"2020-06-10T23:11:20Z","trustType":"AzureAd","alternativeSecurityIds":[{"type":2,"key":"WAA1ADAAOQA6ADwAUwBIAEEAM"}]}|
  
Example output:

```
{
  "device": {
    "accountEnabled": true,
    "alternativeSecurityIds": [
      {
        "key": "WAA1ADAAOQA6ADwAUwBIAEEAM",
        "type": 2
      }
    ],
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
    "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
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
    "trustType": "AzureAd"
  }
}
```

#### Get Group by Name

This action is used to get a group by its name

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|True|Display name to filter|None|displayName|None|None|
  
Example input:

```
{
  "name": "displayName"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|group|group|False|Group|{"id":"bb4d41d4-eb13-4a33-99b5-7d7290df22e9","deletedDateTime":null,"classification":null,"createdDateTime":"2019-09-20T12:15:21Z","creationOptions":[],"description":"Azure AD Test Group","displayName":"Azure AD Test Group","groupTypes":["Unified"],"isAssignableToRole":false,"mail":"user@example.com","mailEnabled":true,"mailNickname":"AzureADTestGroup","onPremisesLastSyncDateTime":null,"onPremisesSecurityIdentifier":null,"onPremisesSyncEnabled":null,"preferredDataLocation":null,"proxyAddresses":["SPO:SPO_618d645a-541b-4349-a7c0-3bb73eedd701@SPO_5c824599-dc8c-4d31-96fb-3b886d4f8f10","SMTP:user@example.com"],"renewedDateTime":"2019-09-20T12:15:21Z","resourceBehaviorOptions":[],"resourceProvisioningOptions":[],"securityEnabled":true,"visibility":"Public","onPremisesProvisioningErrors":[]}|
  
Example output:

```
{
  "group": {
    "classification": null,
    "createdDateTime": "2019-09-20T12:15:21Z",
    "creationOptions": [],
    "deletedDateTime": null,
    "description": "Azure AD Test Group",
    "displayName": "Azure AD Test Group",
    "groupTypes": [
      "Unified"
    ],
    "id": "bb4d41d4-eb13-4a33-99b5-7d7290df22e9",
    "isAssignableToRole": false,
    "mail": "user@example.com",
    "mailEnabled": true,
    "mailNickname": "AzureADTestGroup",
    "onPremisesLastSyncDateTime": null,
    "onPremisesProvisioningErrors": [],
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
    "visibility": "Public"
  }
}
```

#### Get User Info

This action is used to get user information

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|user_id|string|None|True|Retrieve information about specific User ID|None|user@example.com|None|None|
  
Example input:

```
{
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|user_information|user_information|True|Information about a user|{"@odata.context":"https://graph.microsoft.com/v1.0/$metadata#users/$entity","businessPhones":[],"displayName":"Joey McAdams","givenName":"Joey","jobTitle":"Sr. Software Engineer","mail":"","mobilePhone":"","officeLocation":"","preferredLanguage":"","surname":"McAdams","userPrincipalName":"user@example.com","id":"08290005-23ba-46b4-a377-b381d651a2fb","accountEnabled":true}|
  
Example output:

```
{
  "user_information": {
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users/$entity",
    "accountEnabled": true,
    "businessPhones": [],
    "displayName": "Joey McAdams",
    "givenName": "Joey",
    "id": "08290005-23ba-46b4-a377-b381d651a2fb",
    "jobTitle": "Sr. Software Engineer",
    "mail": "",
    "mobilePhone": "",
    "officeLocation": "",
    "preferredLanguage": "",
    "surname": "McAdams",
    "userPrincipalName": "user@example.com"
  }
}
```

#### List Group Members

This action is used to get a list of the group's direct members. A group can have users, organizational contacts, 
devices, service principals and other groups as members

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|group_id|string|None|True|ID of group to search for|None|bb4d41d4-eb13-4a33-99b5-7d7290df22e9|None|None|
  
Example input:

```
{
  "group_id": "bb4d41d4-eb13-4a33-99b5-7d7290df22e9"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|False|Count of members in group|5|
|members|[]user_information|False|Members|[{"@odata.context":"https://graph.microsoft.com/v1.0/$metadata#users/$entity","businessPhones":[],"displayName":"Joey McAdams","givenName":"Joey","jobTitle":"Sr. Software Engineer","mail":"","mobilePhone":"","officeLocation":"","preferredLanguage":"","surname":"McAdams","userPrincipalName":"user@example.com","id":"08290005-23ba-46b4-a377-b381d651a2fb","accountEnabled":true}]|
  
Example output:

```
{
  "count": 5,
  "members": [
    {
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users/$entity",
      "accountEnabled": true,
      "businessPhones": [],
      "displayName": "Joey McAdams",
      "givenName": "Joey",
      "id": "08290005-23ba-46b4-a377-b381d651a2fb",
      "jobTitle": "Sr. Software Engineer",
      "mail": "",
      "mobilePhone": "",
      "officeLocation": "",
      "preferredLanguage": "",
      "surname": "McAdams",
      "userPrincipalName": "user@example.com"
    }
  ]
}
```

#### Remove User from Group

This action is used to remove a user from a group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|group_name|string|None|True|Group Name to manage|None|Example Group Name|None|None|
|user_id|string|None|True|User ID to remove from group|None|user@example.com|None|None|
  
Example input:

```
{
  "group_name": "Example Group Name",
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Was operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Revoke Sign-In Sessions

This action is used to this will require the user to log back in after any page they are on is refreshed by 
invalidating all refresh tokens and cookies

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|user_id|string|None|True|User ID to revoke|None|user@example.com|None|None|
  
Example input:

```
{
  "user_id": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was the operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Search Device

This action is used to search for devices using a given query. For more information about queries visit 
https://learn.microsoft.com/en-us/graph/filter-query-parameter?tabs=http; https://learn.microsoft.com/en-
us/graph/search-query-parameter?tabs=http; https://learn.microsoft.com/en-us/graph/aad-advanced-
queries?tabs=http#device-properties

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|string|None|False|Filter devices by query. See details about query in action description|None|approximateLastSignInDateTime le 2021-06-11T18:01:51Z|None|None|
|orderBy|string|None|False|Sorts list results by the provided device parameter|None|displayName|None|None|
|search|string|None|False|Search parameters by query. See details about query in action description|None|displayName:INTUNE|None|None|
|select|[]string|None|False|Fields to be included in the output|None|["id", "createdDateTime"]|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|devices|[]device|False|Information about the devices|[{"id":"9de5069c-5afe-602b-2ea0-a04b66beb2c0","accountEnabled":true,"approximateLastSignInDateTime":"2020-06-20T21:15:48Z","createdDateTime":"2020-06-10T23:11:21Z","deviceId":"9de5069c-5afe-602b-2ea0-a04b66beb2c0","deviceOwnership":"Company","deviceVersion":2,"displayName":"DESKTOP-D10L83K","enrollmentType":"AzureDomainJoined","exchangeActiveSyncIds":["eas:415F14BD1A98FEA919DF00327EA5DC81:9de5069c-5afe-602b-2ea0-a04b66beb2c0:20200610T231818"],"isCompliant":false,"isManaged":true,"isRooted":false,"managementType":"MDM","manufacturer":"innotek GmbH","mdmAppId":"0000000a-0000-0000-c000-000000000000","model":"VirtualBox","operatingSystem":"Windows","operatingSystemVersion":"10.0.19041.329","physicalIds":["[USER-GID]:9de5069c-5afe-602b-2ea0-a04b66beb2c0:6755416654410028","[GID]:g:6755416654410028","[USER-HWID]:9de5069c-5afe-602b-2ea0-a04b66beb2c0:6755416654410025","[HWID]:h:6755416654410025"],"profileType":"RegisteredDevice","registrationDateTime":"2020-06-10T23:11:20Z","systemLabels":[],"trustType":"AzureAd","alternativeSecurityIds":[{"type":2,"key":"WAA1ADAAOQA6ADwAUwBIAEEAM"}]}]|
  
Example output:

```
{
  "devices": [
    {
      "accountEnabled": true,
      "alternativeSecurityIds": [
        {
          "key": "WAA1ADAAOQA6ADwAUwBIAEEAM",
          "type": 2
        }
      ],
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
      "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
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
      "trustType": "AzureAd"
    }
  ]
}
```

#### Update User Information

This action is used to update a users information

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|city|string|None|False|The city in which the user is located|None|Boston|None|None|
|country|string|None|False|The country or region in which the user is located; for example, US or UK|None|US|None|None|
|department|string|None|False|The name for the department in which the user works|None|IT|None|None|
|job_title|string|None|False|The user's job title|None|Desktop Technician|None|None|
|state|string|None|False|The state or province in the users address|None|MA|None|None|
|user_id|string|None|True|User to updates ID|None|user@example.com|None|None|
|user_type|string|None|False|A string value that can be used to classify user types in your directory, such as Member and Guest|None|Member|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "success": true
}
```
### Triggers


#### Risk Detection

This trigger is used to provides list of both user and sign-in linked risk detections and associated information about 
the detection

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|60|False|Poll frequency in seconds|None|60|None|None|
|risk_level|string|None|True|Risk level|["low", "medium", "high", "hidden", "none", "all"]|all|None|None|
  
Example input:

```
{
  "frequency": 60,
  "risk_level": "all"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|risk|risk|True|Risk|{"id":"04da6f53cd292d990314fd05b2ba6cc06b3acc3a2eb85bf2fe6d48f2edbec301","requestId":"04c82f8e-f0c0-4971-a546-c18125fa3300","correlationId":"0977e5da-93a4-4e97-b1a2-bb03b8007e93","riskType":"unfamiliarFeatures","riskState":"atRisk","riskLevel":"low","riskDetail":"none","source":"IdentityProtection","detectionTimingType":"realtime","activity":"signin","tokenIssuerType":"AzureAD","ipAddress":"66.207.205.214","activityDateTime":"2019-11-25T14:09:08.6953666Z","detectedDateTime":"2019-11-25T14:09:08.6953666Z","lastUpdatedDateTime":"2019-11-25T14:12:04.5431877Z","userId":"ac785ffe-530a-45a1-bbf4-e275457e464b","userDisplayName":"User Name","userPrincipalName":"user@domain","additionalInfo":"[{\"Key\":\"userAgent\",\"Value\":\"python-requests/2.22.0\"}]","location":{"city":"Toronto","state":"Ontario","countryOrRegion":"CA","geoCoordinates":{"latitude":43.63831,"longitude":-79.42555}}}|
  
Example output:

```
{
  "risk": {
    "activity": "signin",
    "activityDateTime": "2019-11-25T14:09:08.6953666Z",
    "additionalInfo": "[{\"Key\":\"userAgent\",\"Value\":\"python-requests/2.22.0\"}]",
    "correlationId": "0977e5da-93a4-4e97-b1a2-bb03b8007e93",
    "detectedDateTime": "2019-11-25T14:09:08.6953666Z",
    "detectionTimingType": "realtime",
    "id": "04da6f53cd292d990314fd05b2ba6cc06b3acc3a2eb85bf2fe6d48f2edbec301",
    "ipAddress": "66.207.205.214",
    "lastUpdatedDateTime": "2019-11-25T14:12:04.5431877Z",
    "location": {
      "city": "Toronto",
      "countryOrRegion": "CA",
      "geoCoordinates": {
        "latitude": 43.63831,
        "longitude": -79.42555
      },
      "state": "Ontario"
    },
    "requestId": "04c82f8e-f0c0-4971-a546-c18125fa3300",
    "riskDetail": "none",
    "riskLevel": "low",
    "riskState": "atRisk",
    "riskType": "unfamiliarFeatures",
    "source": "IdentityProtection",
    "tokenIssuerType": "AzureAD",
    "userDisplayName": "User Name",
    "userId": "ac785ffe-530a-45a1-bbf4-e275457e464b",
    "userPrincipalName": "user@domain"
  }
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**manager**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|@odata.type|string|None|False|@odata.type|None|
|Account Enabled|boolean|None|False|Account Enabled|None|
|Age Group|string|None|False|Age Group|None|
|Assigned Licenses|[]object|None|False|Assigned Licenses|None|
|Assigned Plans|[]object|None|False|Assigned Plans|None|
|Authorization Info|object|None|False|Authorization Info|None|
|Business Phones|[]string|None|False|Business phones|None|
|Company Name|string|None|False|Company Name|None|
|Consent Provided For Minor|string|None|False|Consent Provided For Minor|None|
|Country|string|None|False|Country|None|
|Created Date Time|date|None|False|Created Date Time|None|
|Creation Type|string|None|False|Creation Type|None|
|Deleted Date Time|date|None|False|Deleted Date Time|None|
|Department|string|None|False|Department|None|
|Display Name|string|None|False|Display Name|None|
|Employee Hire Date|date|None|False|Employee Hire Date|None|
|Employee ID|string|None|False|Employee ID|None|
|Employee Org Data|string|None|False|Employee Org Data|None|
|Employee Type|string|None|False|Employee Type|None|
|External User State|string|None|False|External User State|None|
|External User State Change Date Time|string|None|False|External User State Change Date Time|None|
|Fax Number|string|None|False|Fax Number|None|
|Given Name|string|None|False|Given Name|None|
|ID|string|None|False|Manager ID|None|
|Identities|[]object|None|False|Identities|None|
|Im Addresses|[]string|None|False|Im Addresses|None|
|Is Resource Account|boolean|None|False|Is Resource Account|None|
|Job Title|string|None|False|Job Title|None|
|Legal Age Group Classification|string|None|False|Legal Age Group Classification|None|
|Mail|string|None|False|Mail|None|
|Mail Nickname|string|None|False|Mail Nickname|None|
|Mobile Phone|string|None|False|Mobile Phone|None|
|Office Location|string|None|False|Office Location|None|
|On Premises Distinguished Name|string|None|False|On Premises Distinguished Name|None|
|On Premises Domain Name|string|None|False|On Premises Domain Name|None|
|On Premises Extension Attributes|object|None|False|On Premises Extension Attributes|None|
|On Premises Immutable ID|string|None|False|On Premises Immutable ID|None|
|On Premises Last Sync Date Time|date|None|False|On Premises Last Sync Date Time|None|
|On Premises Provisioning Errors|[]string|None|False|On Premises Provisioning Errors|None|
|On Premises Sam Account Name|string|None|False|On Premises Sam Account Name|None|
|On Premises Security Identifier|string|None|False|On Premises Security Identifier|None|
|On Premises Sync Enabled|boolean|None|False|On Premises Sync Enabled|None|
|On Premises User Principal Name|string|None|False|On Premises User Principal Name|None|
|Other Mails|[]string|None|False|Other Mails|None|
|Password Policies|string|None|False|Password Policies|None|
|Password Profile|object|None|False|Password Profile|None|
|Postal Code|string|None|False|Postal Code|None|
|Preferred Data Location|string|None|False|Preferred Data Location|None|
|Provisioned Plans|[]object|None|False|Provisioned Plans|None|
|Proxy Addresses|[]string|None|False|Proxy Addresses|None|
|Refresh Tokens Valid From Date Time|date|None|False|Refresh Tokens Valid From Date Time|None|
|Show In Address List|boolean|None|False|Show In Address List|None|
|Sign In Sessions Valid From Date Time|date|None|False|Sign In Sessions Valid From Date Time|None|
|State|string|None|False|State|None|
|Street Address|string|None|False|Street Address|None|
|Surname|string|None|False|Surname|None|
|Usage Location|string|None|False|Usage Location|None|
|User Principal Name|string|None|False|User Principal Name|None|
|User Type|string|None|False|User Type|None|
  
**user_information**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|@odata.Context|string|None|False|@odata.context|None|
|Account Enabled|boolean|None|False|Account enabled|None|
|Business Phones|[]string|None|False|Business phones|None|
|Display Name|string|None|False|Display name|None|
|Given Name|string|None|False|Given Name|None|
|ID|string|None|False|ID|None|
|Job Title|string|None|False|Job title|None|
|Mail|string|None|False|Mail|None|
|Manager|manager|None|False|Manager|None|
|Mobile Phone|string|None|False|Mobile phone|None|
|Office Location|string|None|False|Office location|None|
|Preferred Language|string|None|False|Preferred language|None|
|Surname|string|None|False|Surname|None|
|User Principal Name|string|None|False|User principal name|None|
  
**group**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created Date Time|string|None|False|Created date time|None|
|Description|string|None|False|Description|None|
|Display Name|string|None|False|Display name|None|
|Group Types|[]string|None|False|Group types|None|
|ID|string|None|False|ID|None|
|Is Assignable to Role|boolean|None|False|Is assignable to role|None|
|Mail|string|None|False|Mail|None|
|Mail Enabled|boolean|None|False|Mail enabled|None|
|Mail Nickname|string|None|False|Mail nickname|None|
|Proxy Addresses|[]string|None|False|Proxy addresses|None|
|Renewed Date Time|string|None|False|Renewed date time|None|
|Security Enabled|boolean|None|False|Security enabled|None|
|Visibility|string|None|False|Visibility|None|
  
**geoCoordinates**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Altitude|string|None|False|The altitude (height), in feet, above sea level|None|
|Latitude|string|None|False|The latitude, in decimal|None|
|Longitude|string|None|False|The longitude, in decimal|None|
  
**signInLocation**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|City|string|None|False|City where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity|None|
|Country Or Region|string|None|False|Country code info (2 letter code) where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity|None|
|Geo Coordinates|geoCoordinates|None|False|Geo coordinates|None|
|State|string|None|False|State where the sign-in originated. This is calculated using latitude/longitude information from the sign-in activity|None|
  
**risk**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Activity|string|None|False|Indicates the activity type the detected risk is linked to. The possible values are signin, user, unknownFutureValue|None|
|Activity Date Time|string|None|False|Date and time that the risky activity occurred|None|
|Additional Information|string|None|False|Additional information associated with the risk detection|None|
|Correlation ID|string|None|False|Correlation ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in|None|
|Detected Date Time|string|None|False|Date and time that the risk was detected|None|
|Detection Timimg Type|string|None|False|Timing of the detected risk (real-time/offline). The possible values are notDefined, realtime, nearRealtime, offline, unknownFutureValue|None|
|ID|string|None|True|Unique ID of the risk detection|None|
|IP Address|string|None|False|IP address of the client from where the risk occurred|None|
|Last Updated Date Time|string|None|False|Date and time that the risk detection was last updated|None|
|Location|sign_in_location|None|False|Location of the client from where the risk occurred|None|
|Request ID|string|None|False|Request ID of the sign-in associated with the risk detection. This property is null if the risk detection is not associated with a sign-in|None|
|Risk Detail|string|None|False|Details of the detected risk. Details for this property are only available for Azure AD Premium P2 customers. P1 customers will be returned hidden|None|
|Risk Event Type|string|None|False|The type of risk event detected|None|
|Risk Level|string|None|False|Level of the detected risk|None|
|Risk State|string|None|False|The state of a detected risky user or sign-in|None|
|Risk Type|string|None|False|The type of risk event detected|None|
|Risk Level|string|None|False|Source of the risk detection. For example, activeDirectory|None|
|Token Issuer Type|string|None|False|Indicates the type of token issuer for the detected sign-in risk. The possible values are AzureAD, ADFederationServices, and unknownFutureValue|None|
|User Display Name|string|None|False|User display name|None|
|User ID|string|None|False|User ID|None|
|User Principal Name|string|None|False|The user principal name (UPN) of the user|None|
  
**alternativeSecurityId**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Identity Provider|string|None|False|Identity provider|example_provider|
|Key|string|None|False|Key|["WAA1ADAAOQA6ADwAUwBIAEEAMQAtAFQAUAAtAFAAVQBC"]|
|Type|integer|None|False|Type|2|
  
**extensionAttributes**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Extension Attribute 1|string|None|False|First customizable extension attribute|example1|
|Extension Attribute 10|string|None|False|Tenth customizable extension attribute|example10|
|Extension Attribute 11|string|None|False|Eleventh customizable extension attribute|example11|
|Extension Attribute 12|string|None|False|Twelfth customizable extension attribute|example12|
|Extension Attribute 13|string|None|False|Thirteenth customizable extension attribute|example13|
|Extension Attribute 14|string|None|False|Fourteenth customizable extension attribute|example14|
|Extension Attribute 15|string|None|False|Fifteenth customizable extension attribute|example15|
|Extension Attribute 2|string|None|False|Second customizable extension attribute|example2|
|Extension Attribute 3|string|None|False|Third customizable extension attribute|example3|
|Extension Attribute 4|string|None|False|Fourth customizable extension attribute|example4|
|Extension Attribute 5|string|None|False|Fifth customizable extension attribute|example5|
|Extension Attribute 6|string|None|False|Sixth customizable extension attribute|example6|
|Extension Attribute 7|string|None|False|Seventh customizable extension attribute|example7|
|Extension Attribute 8|string|None|False|Eighth customizable extension attribute|example8|
|Extension Attribute 9|string|None|False|Ninth customizable extension attribute|example9|
  
**device**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Account Enabled|boolean|None|False|True if the account is enabled; otherwise, false|True|
|Alternative Security IDs|[]alternativeSecurityId|None|False|List of alternative security IDs|[]|
|Approximate Last Sign In Datetime|string|None|False|The timestamp of last login in ISO 8601 format and in UTC time|2023-06-08 13:08:47+00:00|
|Compliant Expiration Datetime|string|None|False|The timestamp when the device is no longer deemed compliant|2023-06-08 13:08:47+00:00|
|Device Category|string|None|False|User-defined property set by Intune to automatically add devices to groups and simplify managing devices|my-device-category|
|Device ID|string|None|False|Unique identifier set by Azure Device Registration Service at the time of registration|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Device Metadata|string|None|False|Metadata of the device|Example metadata|
|Device Ownership|string|None|False|Ownership of the device|Personal|
|Device Version|integer|None|False|Version of the device|2|
|Display Name|string|None|False|The display name for the device|DESKTOP-123456|
|Enrollment Profile Name|string|None|False|Enrollment profile name of the device|Apple Device Enrollment Profile|
|Enrollment Type|string|None|False|Enrollment type of the device|UserEnrollment|
|Exchange Active Sync IDs|[]string|None|False|Exchange active sync IDs of the device|["eas::9de5069c-5afe-602b-2ea0-a04b66beb2c0"]|
|Extension Attributes|extensionAttributes|None|False|Contains extension attributes 1-15 for the device|{}|
|ID|string|None|False|The unique identifier for the device|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Is Compliant|boolean|None|False|Whether the device complies with Mobile Device Management (MDM) policies|False|
|Is Managed|boolean|None|False|Whether the device is managed by Mobile Device Management (MDM)|False|
|Is Rooted|boolean|None|False|Whether the device is rooted|True|
|Management Type|string|None|False|Management type of the device|MDM|
|Manufacturer|string|None|False|Manufacturer of the device|Google|
|Mobile Device Management App ID|string|None|False|Application identifier used to register device into MDM|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Model|string|None|False|Model of the device|Android SDK built for x86|
|On Premises Last Sync Date Time|string|None|False|The last time at which the object was synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time.|2014-01-01 00:00:00+00:00|
|On Premises Sync Enabled|boolean|None|False|Whether the object is synced from an on-premises directory|False|
|Operating System|string|None|False|The type of operating system on the device|Android|
|Operating System Version|string|None|False|The version of the operating system on the device|9|
|Physical IDs|[]string|None|False|List of physical IDs|["[GID]:g:6966545952520216"]|
|Profile Type|string|None|False|The profile type of the device|RegisteredDevice|
|Registration Date Time|string|None|False|Date and time of when the device was registered. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time|2014-01-01 00:00:00+00:00|
|System Labels|[]string|None|False|List of labels applied to the device by the system|["test"]|
|Trust Type|string|None|False|Type of trust for the joined device|Workplace|


## Troubleshooting


# Version History

* 5.0.0 - Update SDK to the latest version | Update the output type of `risk` for the `risk_detection` trigger to include all fields
* 4.2.0 - New action | List Group Members
* 4.1.2 - Updated SDK to the latest version | Added additional details in requirements section | `Risk Detection`: Fixed issue where detections were triggered randomly
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