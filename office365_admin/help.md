# Description

[Office 365](https://www.office.com/) is a SaaS version of Microsoft’s popular Microsoft Office productivity suite. This plugin utilizes the [Microsoft Graph API](https://developer.microsoft.com/en-us/graph/docs/concepts/overview) to manage Office 365 users and licenses.

# Key Features

* Add users, assign licenses, and update usage locations to automate the provisioning and management of user accounts in your Office 365 subscription
* Delete users from your Office 365 subscription
* Get a list of subscription SKUs to maintain licensing records

# Requirements

* Microsoft Office 365 Tenant ID
* Microsoft Office 365 App ID
* Microsoft Office 365 Admin API Token

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|app_id|string|None|True|The ID of the registered app that obtained the refresh token|None|
|app_secret|credential_token|None|True|The secret of the registered app that obtained the refresh token|None|
|tenant_id|string|None|True|The ID of the directory that identifies the tenant|None|

## Technical Details

### Actions

#### Lookup User by Email

This action is used to get contact details of a user from an email.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email_address|string|None|True|Email address to search on|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|object|False|Metadata of the user matching the search in JSON format|

Example output:

```
{
  "user": {
    "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users",
    "value": [
      {
        "businessPhones": [],
        "displayName": "Jane Doe",
        "givenName": "Jane",
        "id": "08383205-8s5r-3sk8-7s43-c8su7ffl48fb",
        "jobTitle": "Example Human"
        "mail": null,
        "mobilePhone": null,
        "officeLocation": null,
        "preferredLanguage": null,
        "surname": "Doe",
        "userPrincipalName": "user@example.com"
      }
    ]
  }
}
```

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
|user_principal_name|string|None|True|The user principal name e.g. user@example.com|None|

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
    "userPrincipalName": "user@example.com",
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
|success|boolean|False|True if successful|

Example output:

```
{
  "success": true
}
```

#### Delete User

This action is used to remove a user's access to Office365.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
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

#### Get Subscribed SKUs

This action gets a list of commercial subscriptions that an organization has acquired.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sku_item|[]skuItem|True|Information about a given SKU|

#### Update Usage Location

This action updates usage location for a given user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|location|string|None|True|A two letter country code (ISO standard 3166)|None|
|user_principal_name|string|None|True|The user principal name to update e.g. user@example.com|None|

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

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### serviceItem

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Applies To|string|True|Entity SKU applies to|
|Service Plan ID|string|True|Service plan ID|
|Service Plan Name|string|True|Service plan name|

#### skuItem

|Name|Type|Required|Description|
|----|----|--------|-----------|
|appliesTo|string|True|Entity SKU applies to|
|Capability Status|string|True|Availability of SKU|
|Consumed Units|integer|False|Consumed units|
|ID|string|False|SKU team ID|
|Service Plans|[]serviceItem|True|List of service plans|
|SKU ID|string|True|SKU ID|
|SKU Part Number|string|True|SKU part number|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.4.0 - Added action Lookup User By Email
* 1.3.1 - Spec file and help changes for the Hub
* 1.2.1 - Fix issue where input was undefined in Add and Delete User actions | Add office location to Add User action
* 1.2.0 - New actions Get Subscribed SKUs and Assign License
* 1.1.1 - Fix security bug where `password` field in Create User action was not masked
* 1.1.0 - Add new Add User action
* 1.0.0 - Initial plugin

# Links

## References

* [Graph API](https://developer.microsoft.com/en-us/graph/docs/concepts/use_the_api)
