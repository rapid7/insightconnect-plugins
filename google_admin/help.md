# Description

[Gsuite](https://gsuite.google.com/) administrative functions allow you to manage users. The InsightConnect plugin can retrieve existing user details and suspend users as part of containment or deprovisioning workflows.

# Key Features

* Retrieve Gsuite user information
* Disable Gsuite users

# Requirements

* A JWT with administrative permissions
* API access to Gsuite administrative functions enabled

# Documentation

## Setup

To authenticate to Google admin, you will need to create a service account on your Google apps domain that is capable of delegation. See [https://developers.google.com/admin-sdk/directory/v1/guides/delegation](https://developers.google.com/admin-sdk/directory/v1/guides/delegation)

You will also need to modify Google apps security settings to allow for the following scopes on your service credentials:

* `https://www.googleapis.com/auth/admin.directory.user`
* `https://www.googleapis.com/auth/admin.directory.group`

To add these settings, from the Admin Home page navigate to Security > Advanced Settings > Manage API client access.
You'll need to provide the client ID and the above URL, comma separated.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|private_key|credential_asymmetric_key|None|True|Private Key from service credentials|None|
|admin_user|string|None|True|Admin user to impersonate, e.g. user@example.com|None|
|private_key_id|string|None|True|Private Key ID from service credentials|None|
|token_uri|string|https://accounts.google.com/o/oauth2/token|True|OAUTH2 Token URI|None|
|auth_provider_x509_cert_url|string|https://www.googleapis.com/oauth2/v1/certs|True|OAUTH2 Auth Provider x509 Cert URL|None|
|auth_uri|string|https://accounts.google.com/o/oauth2/auth|True|None|None|
|client_email|string|None|True|Client email from service credentials|None|
|client_id|string|None|True|Client ID|None|
|project_id|string|None|True|Project ID from service credentials|None|
|client_x509_cert_url|string|None|True|x509 cert URL from service credentials|None|

## Technical Details

### Actions

#### Get User

This action is used to retrieve information about a user by their primary email address, unique ID, or alias email.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user|string|None|True|The user's primary email address, unique ID, or alias email|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|True if found|
|user|user|False|User Response Returned|

#### Suspend User

This action is used to suspend a user by their primary email address, unique ID, or alias email.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user|string|None|True|The user's primary email address, unique ID, or alias email|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|user|user|False|User Response Returned|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

#

# Version History

* 1.0.3 - New spec and help.md format for the Extension Library
* 1.0.2 - Fix typo in plugin spec
* 1.0.1 - Update to connection and troubleshooting documentation
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Google Admin API](https://developers.google.com/admin-sdk)
