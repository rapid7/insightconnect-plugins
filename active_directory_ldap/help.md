# Description

[AD LDAP](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/3c5916a9-f1a0-429d-b937-f8fe672d777c) (Active Directory Lightweight Directory Access Protocol) is an application protocol for querying and modifying items in Active Directory. This plugin queries [Microsoft's Active Directory service](https://social.technet.microsoft.com/wiki/contents/articles/5392.active-directory-ldap-syntax-filters.aspx) to programmatically manage and query an Active Directory environment.

# Key Features

* Add and remove user accounts to automate provisioning/deprovisioning of users
* Disable and enable user accounts to contain security risks
* Reset user passwords when a user forgets their login information
* Modify user groups to add or remove users from custom and built-in groups
* Run a custom LDAP query to retrieve, add, modify, or delete Active Directory objects

# Requirements

* Host name and port number (the default TCP/UDP port for LDAP is 389, and 636 for LDAP over SSL)
* Administrative credentials
* To connect, you must have NTLM credentials.
* Please make sure you enter your credentials with the DOMAIN\username format.

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|host|string|None|True|Server Host, e.g. ldap://example.com. Must use either ldap:// or ldaps:// for SSL prefix|None|ldaps://example.com|
|port|integer|389|True|Port, e.g. 389|None|389|
|use_ssl|boolean|None|True|Use SSL?|None|True|
|username_password|credential_username_password|None|True|Username and password|None|{"username":"user1", "password":"mypassword"}|

Example input:

```
{
  "host": "ldaps://example.com",
  "port": 389,
  "use_ssl": true,
  "username_password": {"username":"user1", "password":"mypassword"}
}
```

## Technical Details

### Actions

#### Modify Object

This action is used to modify an Active Directory objects attributes.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|attribute_to_modify|string|None|True|The name of the attribute to modify|None|postalCode|
|attribute_value|string|None|True|The value of the attribute|None|02114|
|distinguished_name|string|None|True|The distinguished name of the object to modify|None|CN=user,OU=domain_users,DC=example,DC=com|

Example input:

```
{
  "attribute_to_modify": "postalCode",
  "attribute_value": 1100,
  "distinguished_name": "CN=user,OU=domain_users,DC=example,DC=com"
}
```

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

#### Add or Remove an Object from Group

This action is used to add or remove an object from an Active Directory group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|add_remove|string|None|True|Add or remove the group|['add', 'remove']|add|
|distinguished_name|string|None|True|The distinguished name of the object whose membership will be modified|None|CN=user,OU=domain_users,DC=mydomain,DC=com|
|group_dn|string|None|True|The Distinguished Name of the group to add or remove|None|CN=group_name,OU=domain_groups,DC=example,DC=com|

Example input:

```
{
  "account_disabled": "true",
  "additional_parameters": {"telephoneNumber":"(617)555-1234"},
  "domain_name": "example.com",
  "first_name": "John",
  "last_name": "Doe",
  "logon_name": "jdoe",
  "password": "mypassword",
  "user_ou": "Users",
  "user_principal_name": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Operation status|

Example output:

```
```

#### Add

This action is used to add the specified Active Directory user.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|account_disabled|string|True|True|Set this to true to disable the user account at creation|['true', 'false']|True|
|additional_parameters|object|None|False|Add additional user parameters in JSON format|None|{"telephoneNumber":"(617)555-1234"}|
|domain_name|string|None|True|The domain name this user will belong to|None|example.com|
|first_name|string|None|True|User's first name|None|John|
|last_name|string|None|True|User's last name|None|Doe|
|logon_name|string|None|True|The logon name for the account|None|jdoe|
|password|password|None|True|The account's starting password|None|mypassword|
|user_ou|string|Users|True|The OU that the user account will be created in|None|Users|
|user_principal_name|string|None|True|The users principal name|None|user@example.com|

Example input:

```
{
  "account_disabled": "true",
  "additional_parameters": "{\"telephoneNumber\":\"(617)555-1234\"}",
  "domain_name": "example.com",
  "first_name": "John",
  "last_name": "Doe",
  "logon_name": "jdoe",
  "password": "mypassword",
  "user_ou": "Users",
  "user_principal_name": "user@example.com"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|search_base|string|None|True|The base of the search request|None|DC=example,DC=com|
|search_filter|string|None|True|The filter of the search request. It must conform to the LDAP filter syntax specified in RFC4515|None|(sAMAccountName=joesmith)|

Example input:

```
{
  "search_base": "DC=example,DC=com",
  "search_filter": "(sAMAccountName=joesmith)"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|distinguished_name|string|None|True|The distinguished name of the user to enable|None|CN=user,OU=domain_users,DC=example,DC=com|

Example input:

```
{
  "distinguished_name": "CN=user,OU=domain_users,DC=example,DC=com"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|distinguished_name|string|None|True|The distinguished name of the user whose membership will be modified|None|CN=user,OU=domain_users,DC=example,DC=com|
|new_ou|string|None|True|The distinguished name of the OU to move the object to|None|OU=disabled_users,DC=example,DC=com|

Example input:

```
{
  "distinguished_name": "CN=user,OU=domain_users,DC=example,DC=com",
  "new_ou": "OU=disabled_users,DC=example,DC=com"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|distinguished_name|string|None|True|The distinguished name of the user whose membership will be modified|None|CN=user,OU=domain_users,DC=example,DC=com|
|new_password|password|None|True|The new password|None|mypassword|

Example input:

```
{
  "distinguished_name": "CN=user,OU=domain_users,DC=example,DC=com",
  "new_password": "mypassword"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|distinguished_name|string|None|True|The distinguished name of the user to disable|None|CN=user,OU=domain_users,DC=example,DC=com|

Example input:

```
{
  "distinguished_name": "CN=user,OU=domain_users,DC=example,DC=com"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|distinguished_name|string|None|True|The distinguished name of the object to delete|None|CN=user,OU=domain_users,DC=example,DC=com|

Example input:

```
{
  "distinguished_name": "CN=user,OU=domain_users,DC=example,DC=com"
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|distinguished_name|string|None|True|The distinguished name of the user who will be forced to reset|None|CN=user,OU=domain_users,DC=example,DC=com|

Example input:

```
{
  "distinguished_name": "CN=user,OU=domain_users,DC=example,DC=com"
}
```

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

_This plugin does not contain any triggers._

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

* 4.0.0 - New action Modify Object | Rename Modify Groups action to 'Add or Remove an Object from Group'
* 3.2.10 - Fix issue where escaped characters were not being handled correctly
* 3.2.9 - Fix issue with error handling and logging for the Modify Groups action | Add example inputs | Update to use ldap3 2.7 and Python 3.8
* 3.2.8 - Fix issue were adding objects to containers might fail
* 3.2.7 - New spec and help.md format for the Extension Library
* 3.2.6 - Update help to document supported Windows Server versions
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
