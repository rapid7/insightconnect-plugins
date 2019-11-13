# Description

This plugin utilizes Active Directory to run LDAP queries.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

To connect, you must have NTLM credentials.

Please make sure you enter your credentials with the DOMAIN\username format.

The hostname should start with the URI prefix of `ldap://` for an unencrypted connection or `ldaps://` for an encrypted connection using SSL.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|use_ssl|boolean|None|True|Use SSL?|None|
|host|string|None|True|Server Host, e.g. ldap\://192.5.5.5. Must use either ldap\:// or ldaps\:// for SSL prefix|None|
|port|integer|389|True|Port, e.g. 389|None|
|username_password|credential_username_password|None|True|Username and password|None|

## Technical Details

### Actions

#### Modify Groups

This action is used to add or remove a user from an Active Directory group.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|distinguished_name|string|None|True|The distinguished name of the user whose membership will be modified e.g. CN=user,OU=domain_users,DC=mydomain,DC=com|None|
|group_dn|string|None|True|The Distinguished Name of the group to add or remove|None|
|add_remove|string|None|True|Add or remove the group|['add', 'remove']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Operation status|

Example output:

```

{
  "success": true
}

```

#### Add

This action is used to add the specified Active Directory user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|first_name|string|None|True|User's first name|None|
|last_name|string|None|True|User's last name|None|
|additional_parameters|object|None|False|Add additional user parameters in JSON format e.g. {'telephoneNumber'\: '(617)555-1234'}|None|
|domain_name|string|None|True|The domain name this user will belong to, e.g. mydomain.com|None|
|user_ou|string|Users|True|The OU that the user account will be created in|None|
|logon_name|string|None|True|The logon name for the account|None|
|account_disabled|string|true|True|Set this to true to disable the user account at creation|['true', 'false']|
|password|password|None|True|The account's starting password|None|
|user_principal_name|string|None|True|The users principal name, e.g. jdoe@example.com|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Operation status|

Example output:

```

{
  "success": true
}

```

#### Query

This action is used to run an LDAP query.

For more information on LDAP queries see https://ldap3.readthedocs.io/tutorial_searches.html

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|search_filter|string|None|True|The filter of the search request. It must conform to the LDAP filter syntax specified in RFC4515. Example\: (accountName=joesmith)|None|
|search_base|string|None|True|The base of the search request|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]result|False|Results returned|

Example output:

```

{
  "results": [
    {
      "dn": string,
      "attributes": {
        "pwdLastSet": date,
        "objectClass": [
          string,
          string,
          string,
          string
        ],
        "memberOf": [
          string
        ],
        "sAMAccountType": int,
        "uSNChanged": int,
        "givenName": string,
        "userPrincipalName": string,
        "countryCode": int,
        "lastLogon": date,
        "sAMAccountName": string,
        "name": string,
        "primaryGroupID": int,
        "dSCorePropagationData": [
          date
        ],
        "displayName": string,
        "logonCount": int,
        "cn": string,
        "objectSid": string,
        "codePage": int,
        "badPwdCount": int,
        "objectGUID": string,
        "distinguishedName": string,
        "whenChanged": date,
        "badPasswordTime": date,
        "instanceType": int,
        "uSNCreated": int,
        "sn": string,
        "whenCreated": date,
        "accountExpires": date,
        "userAccountControl": int,
        "lastLogoff": date,
        "objectCategory": "string"
      }
    }
  ]
}

```

#### Enable

This action is used to enable an account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|distinguished_name|string|None|True|The distinguished name of the user to enable e.g. CN=user,OU=domain_users,DC=mydomain,DC=com|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Operation status|

Example output:

```

{
  "success": true
}

```

#### Move Object

This action is used to move an Active Directory object from one organizational unit to another.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|distinguished_name|string|None|True|The distinguished name of the user whose membership will be modified e.g. CN=user,OU=domain_users,DC=mydomain,DC=com|None|
|new_ou|string|None|True|The distinguished name of the OU to move the object to e.g. OU=disabled_users,DC=mydomain,DC=com|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Operation status|

 ```

{
  "success": true
}

```

#### Reset Password

This action is used to reset a users password.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|distinguished_name|string|None|True|The distinguished name of the user whose membership will be modified e.g. CN=user,OU=domain_users,DC=mydomain,DC=com|None|
|new_password|password|None|True|The new password|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Operation status|

 ```

{
  "success": true
}

```

#### Disable

This action is used to disable an account.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|distinguished_name|string|None|True|The distinguished name of the user to disable e.g. CN=user,OU=domain_users,DC=mydomain,DC=com|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Operation status|

Example output:

```

{
  "success": true
}

```

#### Delete

This action is used to delete the LDAP object specified.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|distinguished_name|string|None|True|The distinguished name of the object to delete. Example CN=user,OU=domain_users,DC=mydomain,DC=com|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Operation status|

Example output:

```

{
  "success": true
}

```

#### Force Password Reset

This action is used to force a user to reset their password on next login.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|distinguished_name|string|None|True|The distinguished name of the user who will be forced to reset their password  e.g. CN=user,OU=domain_users,DC=mydomain,DC=com|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Operation status|

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

If you cannot connect, ensure that network access is available, and view the logs to identify any auth errors.

For the Add User action it is recommended that SSL be enabled. Without SSL the action is only partially functional.
It will create the user, but it will not be able to assign a password or enable the account.

SSL must be enabled for the Reset Password action to function.

To look up a Distinguished Name (DN) in Microsoft AD use the query action. Use the search filter (sAMAccountName=objectname ) where
objectname is the logon name of the user you are looking for. The DN can then be fed into another action by Repeating a collection for
the query results, and then using the variable step $item.dn

For the Query action, this plugin does not support objects that use `*`, `\`, or an unpaired `\(\)` as part of their names.
paired `\(\)` are supported

# Version History

* 3.2.5 - Clean connection test output
* 3.2.4 - Fix issue with Query where some output was not unescaped properly | Update to exception handling to leverage PluginException
* 3.2.3 - Fix issue with Add User action disable and enable flags | Update Query action to allow for `<=` and `>=` searches
* 3.2.2 - Fix issue regarding escaping of `(` and `)` in the Query action
* 3.2.1 - Fix issue regarding escaping Distinguished Names containing commas
* 3.2.0 - New action Force Password Reset
* 3.1.4 - Add Connection test | Improve error handling in Connection
* 3.1.3 - Update action descriptions
* 3.1.2 - Update help to clarify use of LDAP URI prefix
* 3.1.1 - Bug fix for normalizing Distinguished Name
* 3.1.0 - Add user action expanded to allow setting of all attributes
* 3.0.1 - Bug fix preventing successful connections
* 3.0.0 - Support web server mode | Update to new credential types
* 2.2.0 - Add actions for move object, reset password and improved error logging
* 2.1.0 - Add actions for account add/delete, disable/enable, modify
* 2.0.2 - SSL bug fix in SDK
* 2.0.1 - Update host input description
* 2.0.0 - Simplify output to "attributes" and "dn", return attributes fixed, and major code cleanup
* 1.0.1 - Bugfix for potentially non-existent raw_attributes
* 1.0.0 - Revise input names, bugfixes for missing attributes and character escaping, fix security issue
* 0.1.0 - Initial plugin

# Links

## References

[Python LDAP3 Search](https://ldap3.readthedocs.io/searches.html)
[Python LDAP3](https://ldap3.readthedocs.io)
[RFC4515](https://tools.ietf.org/search/rfc4515)

