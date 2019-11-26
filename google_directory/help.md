# Description

The Google Directory plugin allows you to suspend and unsuspend users.

# Key Features

* Suspend and unsuspend users
* list all users

# Requirements

* A JWT with administrative permissions
* Google Directory API must be enabled

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|admin_user|string|None|True|Admin user to impersonate, e.g. admin@domain.com|None|
|project_id|string|None|True|Project ID from service credentials|None|
|private_key_id|string|None|True|Private Key ID from service credentials|None|
|private_key|credential_asymmetric_key|None|True|Private Key from service credentials|None|
|client_email|string|None|True|Client email from service credentials|None|
|client_id|string|None|True|Client ID|None|
|client_x509_cert_url|string|None|True|x509 cert URL from service credentials|None|
|auth_uri|string|https\://accounts.google.com/o/oauth2/auth|True|None|None|
|token_uri|string|https\://accounts.google.com/o/oauth2/token|True|OAUTH2 Token URI|None|
|auth_provider_x509_cert_url|string|https\://www.googleapis.com/oauth2/v1/certs|True|OAUTH2 Auth Provider x509 Cert URL|None|
|oauth_scope|string|`https\://www.googleapis.com/auth/admin.directory.user`|True|Google Admin Directory OAuth scope to use for the connection, note that read only will result in some actions not working.|[`https://www.googleapis.com/auth/admin.directory.user`, `https://www.googleapis.com/auth/admin.directory.user.readonly`]|

## Technical Details

### Actions

#### Get All Domain Users

This action is used to get all domain users.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain to retrieve users from|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|users|[]user|True|Users in the domain|

Example output:

```

{
  "users": [{
      "email": "admin@test.org",
      "name": "Joe Tester"
  }, {
      "email": "Bob@test.org",
      "name": "Bob Testerson"
  }]
}

```

#### Suspend User

This action is used to suspend a user account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|Email of user to suspend|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether or not the suspend was successful|

Example output:

```

{
  "success": true
}

```

#### Unsuspend User

This action is used to unsuspend a user account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|Email of user to unsuspend|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether or not the unsuspend was successful|

Example output:

```

{
  "success": true
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.1 - New spec and help.md format for the Hub
* 2.0.0 - Update connection to add support for the read-only Google Admin Directory OAuth scope
* 1.2.1 - Fix typo in plugin spec
* 1.2.0 - Add pagination to Get All Domain Users actions to support domains with 500+ users
* 1.1.0 - Add actions: suspend user, unsuspend user
* 1.0.0 - Initial plugin

# Links

## References

* [Directory API](https://developers.google.com/admin-sdk/directory/)

