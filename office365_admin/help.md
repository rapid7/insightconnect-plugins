
# Office365 Admin

## About

The [Office365 Admin](https://www.office.com/) plugin allows control of the administrative functions for Office365.
This plugin utilizes the [Microsoft Graph API](https://developer.microsoft.com/en-us/graph/docs/concepts/overview).

## Actions

### Add User

This action is used to add a user to Office365.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|mail_nickname|string|None|True|The mail alias for the user|None|
|password|string|None|True|set the users password|None|
|display_name|string|None|True|The users display name e.g. john doe|None|
|force_change_password|boolean|None|True|If true the user will have to change their password at login|None|
|account_enabled|boolean|None|True|If true the account will be enabled|None|
|user_principal_name|string|None|True|The user principal name e.g. jdoe@mydomain.com|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|object|False|Return a user object in json format|

Example output:

```

{
  "user": {
    "@odata.context": "https://graph.microsoft.com/beta/$metadata#users/$entity",
    "id": "bb4c122c-cf16-443e-a1bf-bd1533a7033c",
    "deletedDateTime": null,
    "accountEnabled": false,
    "ageGroup": null,
    "businessPhones": [],
    "city": null,
    "createdDateTime": null,
    "companyName": null,
    "consentProvidedForMinor": null,
    "country": null,
    "department": null,
    "displayName": "john doe",
    "employeeId": null,
    "givenName": null,
    "jobTitle": null,
    "legalAgeGroupClassification": null,
    "mail": null,
    "mailNickname": "john",
    "mobilePhone": null,
    "onPremisesDomainName": null,
    "onPremisesImmutableId": null,
    "onPremisesLastSyncDateTime": null,
    "onPremisesSecurityIdentifier": null,
    "onPremisesSamAccountName": null,
    "onPremisesSyncEnabled": null,
    "onPremisesUserPrincipalName": null,
    "passwordPolicies": null,
    "officeLocation": null,
    "postalCode": null,
    "preferredDataLocation": null,
    "preferredLanguage": null,
    "proxyAddresses": [],
    "refreshTokensValidFromDateTime": "2018-07-25T18:00:21.5620544Z",
    "showInAddressList": null,
    "imAddresses": [],
    "isResourceAccount": null,
    "state": null,
    "streetAddress": null,
    "surname": null,
    "usageLocation": null,
    "userPrincipalName": "jdoe@komanddev.onmicrosoft.com",
    "userType": "Member",
    "assignedLicenses": [],
    "assignedPlans": [],
    "deviceKeys": [],
    "onPremisesExtensionAttributes": {
      "extensionAttribute1": null,
      "extensionAttribute2": null,
      "extensionAttribute3": null,
      "extensionAttribute4": null,
      "extensionAttribute5": null,
      "extensionAttribute6": null,
      "extensionAttribute7": null,
      "extensionAttribute8": null,
      "extensionAttribute9": null,
      "extensionAttribute10": null,
      "extensionAttribute11": null,
      "extensionAttribute12": null,
      "extensionAttribute13": null,
      "extensionAttribute14": null,
      "extensionAttribute15": null
      },
    "onPremisesProvisioningErrors": [],
    "passwordProfile": {
      "password": null,
      "forceChangePasswordNextSignIn": true
    },
    "provisionedPlans": []
  }
}

```

### Delete User

This action is used to remove a user from Office365.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_principal_name|string|None|True|The user principal name to delete|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|return true if it worked|

Example output:

```

{
  "success": true
}

```

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tenant_id|string|None|True|The ID of the directory that identifies the tenant|None|
|app_secret|password|None|True|The secret of the registered app that obtained the refresh token|None|
|app_id|string|None|True|The ID of the registered app that obtained the refresh token|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Versions

* 1.0.0 - Initial plugin
* 1.1.0 - Add new Add User action
* 1.1.1 - Fix security bug where `password` field in Create User action was not masked

## Workflows

Examples:

* Add a user as part of the onboarding process
* Remove a user as part of the offboarding process

## References

* [Graph API](https://developer.microsoft.com/en-us/graph/docs/concepts/use_the_api)
