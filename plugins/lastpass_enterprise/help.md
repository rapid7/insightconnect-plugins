# Description

[LastPass Enterprise](https://www.lastpass.com/products/enterprise-password-management-and-sso) is a password management solution for businesses that protects every access point through an all-in-one single sign-on and password manager solution. This plugin utilizes the [LastPass API](https://enterprise.lastpass.com/users/set-up-create-new-user-2/lastpass-provisioning-api/) to automate administration of users and groups.

# Key Features

* Provision and deprovision users in your LastPass Enterprise account
* Add and remove users from groups in your LastPass Enterprise account

# Requirements

* Lastpass Account Number
* Provisioning Hash (API Key)

# Documentation

## Setup

The connection requires a LastPass Enterprise account number and provisioning hash.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|account|integer|None|True|Account number|None|
|provhash|credential_secret_key|None|True|Provisioning hash|None|

## Technical Details

### Actions

#### Change Group

This action is used to add or remove a users group.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|action|string|None|True|Add or delete group|['add', 'delete']|
|user_name|string|None|True|User name for account to edit|None|
|groups|[]string|None|True|Array of groups|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|Status|

#### Deprovision User

This action can be used to deprovision a user with one of the following status: `delete`, `deactivated`, or `remove`.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_name|string|None|True|User name to delete|None|
|delete_action|string|None|True|Delete action|['deactivate', 'remove', 'delete']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|Status|

#### Provision User

This action can be used to provision or change a user's account settings.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|password_reset_required|boolean|None|False|Password reset required|None|
|password|string|None|False|Password for the user|None|
|user_name|string|None|True|User name to add|None|
|full_name|string|None|False|Full name of user to add|None|
|groups|[]string|None|False|Array of groups|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|Status|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.2 - New spec and help.md format for the Extension Library
* 1.0.1 - Update to fix connection test
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [LastPass Enterprise](https://www.lastpass.com/enterprise)
* [LastPass Provisioning API](https://enterprise.lastpass.com/users/set-up-create-new-user-2/lastpass-provisioning-api/)

