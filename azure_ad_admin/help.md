# Azure AD Admin

## About

[Azure](https://azure.microsoft.com) AD Admin will perform administrative tasks in Azure AD.
It uses the [User](https://docs.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0) endpoint in
the [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/overview?view=graph-rest-1.0).

NOTE: The application this plugin connects to needs the following permissions:

* Directory.AccessAsUser.All
* Directory.ReadWrite.All
* User.ReadWrite.All

The application will need to be added to the Global Administrator role. This can be done in `Roles and administrators`
in Azure Active directory via the Azure Portal.

## Actions

### Create User and Notify

This action is used to create a user with a randomly generated password and send out an email with the password.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|account_enabled|boolean|True|False|true if the account is enabled; otherwise, false|None|
|display_name|string|None|True|The name to display in the address book for the user e.g. displayName-value|None|
|mail_nickname|string|None|False|The mail alias for the user e.g. mailNickname-value|None|
|notify_email_body|string|None|False|Body of the email to be sent out. Use $password to place the generated password|None|
|notify_from|string|None|True|User from which email notifcation will be sent|None|
|notify_recipient|string|None|True|Email address of the account to be notified of user creation|None|
|user_principal_name|string|None|True|The user principal name e.g. someuser@contoso.com|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Did the step succeed|

Example output:

```
{
  "success": true
}
```

### Disable User Account

This action is used to disable a user account. This action will not disable an administrative account.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|True|User ID to disable e.g. bob@hotmail.com|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "success": true
}
```

### Enable User Account

This action is used to enable a user account.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|True|User ID to enable e.g. bob@hotmail.com|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "success": true
}
```

### Force User to Change Password

This action forces a user to change their password on their next successful login.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|True|User ID|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "success": true
}
```

### Get User Info

This action is used to get user information.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_id|string|None|True|User ID e.g. bob@hotmail.com|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user_information|object|True|Information about a user|

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
    "userPrincipalName": "bob@hotmail.com",
    "id": "08290005-23ba-46b4-a377-b381d651a2fb",
    "accountEnabled": true
  }
}
```

### Get Group by Name

This action is used to get a group by it's name.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name|string|None|True|Name|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|group|object|False|Group|

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
    "mail": "AzureADTestGroup@komanddev.onmicrosoft.com",
    "mailEnabled": true,
    "mailNickname": "AzureADTestGroup",
    "onPremisesLastSyncDateTime": null,
    "onPremisesSecurityIdentifier": null,
    "onPremisesSyncEnabled": null,
    "preferredDataLocation": null,
    "proxyAddresses": [
      "SPO:SPO_618d645a-541b-4349-a7c0-3bb73eedd701@SPO_5c824599-dc8c-4d31-96fb-3b886d4f8f10",
      "SMTP:AzureADTestGroup@komanddev.onmicrosoft.com"
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

### Add User to Group

This action is used to add a user to a group.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|group_name|string|None|True|Group Name e.g. My Azure Group|None|
|user_id|string|None|True|User ID e.g. bob@hotmail.com|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Was operation successful|

Example output:

```
{
  "success": true
}
```

### Remove User from Group

This action is used to remove a user from a group.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|group_name|string|None|True|Group Name e.g. My Azure Group|None|
|user_id|string|None|True|User ID e.g. bob@hotmail.com|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Was operation successful|

Example output:

```
{
  "success": true
}
```

## Triggers

_This plugin does not contain any triggers._

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|app_id|string|None|True|The ID of the registered app that obtained the refresh token|None|
|app_secret|credential_secret_key|None|True|The secret of the registered app that obtained the refresh token|None|
|tenant_id|string|None|True|The ID of the directory that identifies the tenant|None|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

## Workflows

Examples:

* Disable a user
* Enable a user
* Get user information

## Versions

* 1.0.0 - Initial plugin
* 1.1.0 - New action Force User to Change Password
* 1.2.0 - New actions Get Group by Name, Add User to Group, and Remove User from Group
* 1.3.0 - New action Create User

## References

* [Azure AD Admin](https://azure.microsoft.com)
* [User API](https://docs.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0)
* [Microsoft Graph API](https://docs.microsoft.com/en-us/graph/overview?view=graph-rest-1.0)

## Custom Output Types

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
|officeLocation|string|False|Office Location|
|preferredLanguage|string|False|Preferred language|
|surname|string|False|Surname|
|userPrincipalName|string|False|User Principal Name|

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


