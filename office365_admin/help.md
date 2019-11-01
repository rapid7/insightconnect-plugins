
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
|account_enabled|boolean|None|True|If true, the account will be enabled|None|
|display_name|string|None|True|The user's display name e.g. John Doe|None|
|force_change_password|boolean|None|True|If true, the user will have to change their password at login|None|
|mail_nickname|string|None|True|The mail alias for the user|None|
|office_location|string|None|False|User Office Location|None|
|password|password|None|True|Set the user's password|None|
|user_principal_name|string|None|True|The user principal name e.g. jdoe@mydomain.com|None|

#### Output

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

### Assign License To User

This action assigns a license to a given user.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|sku_id|string|None|True|ID for SKU to be applied|None|
|user_principal_name|string|None|True|The user principal name to delete|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Return true if it worked|

Example output:

```
{
  "success": true
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



```

### Update Usage Location

This action updates usage location for a given user.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|location|string|None|True|A two letter country code (ISO standard 3166)|None|
|user_principal_name|string|None|True|The user principal name to update e.g. bob@hotmail.com|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|True if successful|

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

### Get Subscribed SKUs

This action gets a list of commercial subscriptions that an organization has acquired.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sku_item|[]skuItem|True|SKU item containing all information about a given SKU|

Example output:

```
[
  {
    "capabilityStatus": "Enabled",
    "consumedUnits": 14,
    "id": "48a80680-7326-48cd-9935-b556b81d3a4e_c7df2760-2c81-4ef7-b578-5b5392b571df",
    "prepaidUnits": {
        "enabled": 25,
        "suspended": 0,
        "warning": 0
    },
    "servicePlans": [
        {
            "servicePlanId": "8c098270-9dd4-4350-9b30-ba4703f3b36b",
            "servicePlanName": "ADALLOM_S_O365",
            "provisioningStatus": "Success",
            "appliesTo": "User"
        },
        {
            "servicePlanId": "9f431833-0334-42de-a7dc-70aa40db46db",
            "servicePlanName": "LOCKBOX_ENTERPRISE",
            "provisioningStatus": "Success",
            "appliesTo": "User"
        }
    ],
    "skuId": "c7df2760-2c81-4ef7-b578-5b5392b571df",
    "skuPartNumber": "ENTERPRISEPREMIUM",
    "appliesTo": "User"
  }
]
```

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Versions

* 1.0.0 - Initial plugin
* 1.1.0 - Add new Add User action
* 1.1.1 - Fix security bug where `password` field in Create User action was not masked
* 1.2.0 - New actions Get Subscribed SKUs and Assign License
* 1.2.1 - Fix issue where input was undefined in Add and Delete User actions | Add office location to Add User action

## Workflows

Examples:

* Add a user as part of the onboarding process
* Remove a user as part of the offboarding process

## References

* [Graph API](https://developer.microsoft.com/en-us/graph/docs/concepts/use_the_api)

## Custom Output Types

### serviceItem

|Name|Type|Required|Description|
|----|----|--------|-----------|
|appliesTo|string|True|Entity SKU applies to|
|servicePlanId|string|False|Service Plan ID|
|servicePlanName|string|False|Service Plan Name|

### skuItem

|Name|Type|Required|Description|
|----|----|--------|-----------|
|appliesTo|string|True|Entity SKU applies to|
|capabilityStatus|string|False|Availability of SKU|
|consumedUnits|integer|False|Consumed Units|
|id|string|False|SKU item ID|
|servicePlans|[]serviceItem|True|List of service plans|
|skuId|string|True|SkuID|
|skuPartNumber|string|True|SKU Part Number|
