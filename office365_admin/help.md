# Description

The [Office365 Admin](https://www.office.com/) plugin enables user management in Office 365.

This plugin utilizes the [Microsoft Graph API](https://developer.microsoft.com/en-us/graph/docs/concepts/overview).

# Key Features

* Add and remove users
* Assign licenses

# Requirements

* An Azure application with administrative permissions (User.ReadWrite.All)
* Azure application credentials

# Documentation

## Setup

The connection configuration accepts the following parameters:


|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tenant_id|string|None|True|The ID of the directory that identifies the tenant|None|
|app_secret|password|None|True|The secret of the registered app that obtained the refresh token|None|
|app_id|string|None|True|The ID of the registered app that obtained the refresh token|None|

## Technical Details

### Actions

#### Add User

This action is used to add a user to Office365.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|account_enabled|boolean|None|True|If true, the account will be enabled|None|
|display_name|string|None|True|The user's display name e.g. John Doe|None|
|force_change_password|boolean|None|True|If true, the user will have to change their password at login|None|
|mail_nickname|string|None|True|The mail alias for the user|None|
|office_location|string|None|False|User Office Location|None|
|password|password|None|True|Set the user's password|None|
|user_principal_name|string|None|True|The user principal name e.g. jdoe@mydomain.com|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|object|False|Return a user object in JSON format|

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

#### Assign License To User

This action assigns a license to a given user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sku_id|string|None|True|ID for SKU to be applied|None|
|user_principal_name|string|None|True|The user principal name to delete|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Return true if it worked|

Example output:

```
{
  "success": true
}
```

#### Delete User

This action is used to remove a user from Office365.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_principal_name|string|None|True|The user principal name to delete|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|return true if it worked|

Example output:

```
{
  "success": true
}
```

#### Update Usage Location

This action updates usage location for a given user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|location|string|None|True|A two letter country code (ISO standard 3166)|None|
|user_principal_name|string|None|True|The user principal name to update e.g. bob@hotmail.com|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|True if successful|

Example output:

```

{
  "success": true
}

```

#### Get Subscribed SKUs

This action gets a list of commercial subscriptions that an organization has acquired.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sku_item|[]skuItem|True|Information about a given SKU|

Example output:

```
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.2.1 - Fix issue where input was undefined in Add and Delete User actions | Add office location to Add User action
* 1.2.0 - New actions Get Subscribed SKUs and Assign License
* 1.1.1 - Fix security bug where `password` field in Create User action was not masked
* 1.1.0 - Add new Add User action
* 1.0.0 - Initial plugin

# Links

## References

* [Graph API](https://developer.microsoft.com/en-us/graph/docs/concepts/use_the_api)

