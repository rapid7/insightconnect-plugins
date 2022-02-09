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

# Supported Product Versions

* Azure Active Directory 2.0.89.0

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|chase_referrals|boolean|True|True|Allows the plugin to follow referrals from the specified Active Directory server to other Active Directory servers|None|True|
|host|string|None|True|Server Host, e.g. example.com|None|example.com|
|port|integer|389|True|Port, e.g. 389|None|389|
|use_ssl|boolean|None|True|Use SSL?|None|True|
|username_password|credential_username_password|None|True|Username and password|None|{"username":"user1", "password":"mypassword"}|

Example input:

```
{
  "chase_referrals": true,
  "host": "example.com",
  "port": 389,
  "use_ssl": true,
  "username_password": {
    "username": "user1", 
    "password": "mypassword"
  }
}
```

## Technical Details

### Actions

#### Unlock User

This action is used to unlock an account.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|distinguished_name|string|None|True|The distinguished name of the user to unlock|None|CN=user,OU=domain_users,DC=example,DC=com|

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

#### Query Group Membership

This action is used to query group membership.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|expand_nested_groups|boolean|None|False|Expand nested groups in results|None|True|
|group_name|string|None|True|Name of the group for which membership will be checked|None|Domain Users|
|include_groups|boolean|None|False|Include groups in results|None|True|
|search_base|string|None|True|The base of the search request|None|DC=example,DC=com|

Example input:

```
{
  "expand_nested_groups": true,
  "group_name": "Domain Users",
  "include_groups": true,
  "search_base": "DC=example,DC=com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|False|Number of results|
|results|[]results|False|Results returned|

Example output:

```
{
  "count": 1,
  "results": [
    {
      "attributes": {
        "accountExpires": "9999-12-31 23:59:59.999999+00:00",
        "adminCount": 0,
        "badPasswordTime": "1601-01-01 00:00:00+00:00",
        "badPwdCount": 0,
        "cn": "Example User",
        "codePage": 0,
        "countryCode": 0,
        "dSCorePropagationData": [
          "2021-01-14 18:17:28+00:00",
          "2021-01-14 17:48:27+00:00",
          "1601-01-01 00:04:16+00:00"
        ],
        "description": [
          "Example Account"
        ],
        "distinguishedName": "CN=Example User,CN=Users,DC=example,DC=com",
        "instanceType": 4,
        "isCriticalSystemObject": true,
        "lastLogoff": "1601-01-01 00:00:00+00:00",
        "lastLogon": "1601-01-01 00:00:00+00:00",
        "logonCount": 0,
        "memberOf": [
          "CN=Domain Users,CN=Users,example,DC=com"
        ],
        "name": "Example User",
        "objectCategory": "CN=Person,CN=Schema,CN=Configuration,DC=example,DC=com",
        "objectClass": [
          "top",
          "person",
          "organizationalPerson",
          "user"
        ],
        "objectGUID": "{b45138aa-be39-47d9-ab57-3aee8f381f87}",
        "objectSid": "S-1-5-33-3456299977-1009817396-2685666617-303",
        "primaryGroupID": 513,
        "pwdLastSet": "2021-01-14 17:48:26.197384+00:00",
        "sAMAccountName": "Example User",
        "sAMAccountType": 489006322,
        "showInAdvancedViewOnly": true,
        "uSNChanged": 16419,
        "uSNCreated": 12324,
        "userAccountControl": 514,
        "whenChanged": "2021-01-14 18:17:28+00:00",
        "whenCreated": "2021-01-14 17:48:26+00:00"
      },
      "dn": "CN=Example User,CN=Users,DC=example,DC=com"
    }
  ]
}

```

#### Modify Object

This action is used to modify the attributes of an Active Directory object.

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
  "attribute_value": "02114",
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
  "add_remove": "add",
  "distinguished_name": "CN=user,OU=domain_users,DC=mydomain,DC=com",
  "group_dn": "CN=group_name,OU=domain_groups,DC=example,DC=com"
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

#### Add User

This action is used to add the specified Active Directory user.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|account_disabled|boolean|True|True|Set this to true to disable the user account at creation|None|True|
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
  "account_disabled": true,
  "additional_parameters": {
    "telephoneNumber": "(617)555-1234"
  },
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
|attributes|[]string|None|False|Attributes to search. If empty return all attributes|None|["createTimestamp", "creatorsName"]|
|search_base|string|None|True|The base of the search request|None|DC=example,DC=com|
|search_filter|string|None|True|The filter of the search request. It must conform to the LDAP filter syntax specified in RFC4515|None|(sAMAccountName=joesmith)|

Example input:

```
{
  "attributes": [
    "createTimestamp",
    "creatorsName"
  ],
  "search_base": "DC=example,DC=com",
  "search_filter": "(sAMAccountName=joesmith)"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|False|Number of results|
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

Example output:

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

Example output:

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

#### attributes

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Account Expires|string|False|Account expires|
|Admin Count|integer|False|Admin count|
|Bad Password Time|string|False|Bad password time|
|Bad PWD Count|integer|False|Bad PWD count|
|CN|string|False|CN|
|Code Page|integer|False|Code page|
|Country Code|integer|False|Country code|
|DS Core Propagation Data|[]string|False|DS core propagation data|
|Description|[]string|False|Description|
|Distinguished Name|string|False|Distinguished name|
|Instance Type|integer|False|Instance type|
|Is Critical System Object|boolean|False|Is critical system object|
|Last Log Off|string|False|Last log off|
|Last Log On|string|False|Last log on|
|Last Log On Timestamp|string|False|Last log on timestamp|
|Log On Count|integer|False|Log on count|
|Member Of|[]string|False|Member of|
|Name|string|False|Name|
|Object Category|string|False|Object category|
|Object Class|[]string|False|Object class|
|Object GUID|string|False|Object GUID|
|Object SID|string|False|Object SID|
|Primary Group ID|integer|False|Primary group ID|
|PWD Last Set|string|False|PWD last set|
|SAM Account Name|string|False|SAM account name|
|SAM Account Type|integer|False|SAM account type|
|USN changed|integer|False|USN changed|
|USN created|integer|False|USN created|
|User Account Control|integer|False|User account control|
|When Changed|string|False|When changed|
|When Created|string|False|When created|

#### result

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Attributes|object|False|None|
|Dn|string|False|None|

#### results

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Attributes|attributes|False|Attributes|
|DN|string|False|DN|

## Troubleshooting

Objects that contain an equals sign `=` or an asterisk `*` require the signs to be escaped.
For example `CN=Robert = bob Smith,OU=domain_users,DC=rapid7,DC=com` must be escaped as`CN=Robert \= bob Smith,OU=domain_users,DC=mattsdomain,DC=local` in the input.
A second example would be `CN=C**l guy,OU=domain_users,DC=rapid7,DC=com`. This must be escaped as `CN=C\*\*l guy,OU=domain_users,DC=rapid7,DC=com`.

This plugin does not support objects and unpaired `\(\)` as part of their names.
Paired `\(\)` are supported.
For example `CN=Robert (Bob) Smith,OU=domain_users,DC=rapid7,DC=com` is supported
but `CN=Robert Bob) Smith,OU=domain_users,DC=rapid7,DC=com` is not.

All inputs to the query action must be correctly escaped.

If you cannot connect, ensure that network access is available, and view the logs to identify any auth errors.

For the Add User action it is recommended that SSL be enabled. Without SSL the action is only partially functional.
It will create the user, but it will not be able to assign a password or enable the account.

SSL must be enabled for the Reset Password action to function.

To look up a Distinguished Name (DN) in Microsoft AD use the query action. Use the search filter (sAMAccountName=objectname ) where
objectname is the logon name of the user you are looking for. The DN can then be fed into another action by Repeating a collection for
the query results, and then using the variable step $item.dn

# Version History

* 5.3.2 - Improve LDAP connection handling
* 5.3.1 - Improved error messaging in case the specified group was not found in the Query Group Membership action
* 5.3.0 - Add Unlock User action
* 5.2.2 - Add automatic pagination in Query Group Membership and Query actions
* 5.2.1 - Add default prefix `ldap://` and `ldaps://` to provided host
* 5.2.0 - New action Query Group Membership
* 5.1.0 - Update error handling in Add User, Force Password Reset, Reset Password actions | Update connection.py to raise PluginException rather than ConnectionTestException
* 5.0.0 - Add Chase Referrals input to the connection to support multi-domain environments | Rename Add action to Add User to be more explicit | Refactor reusable code from actions into util.py
* 4.1.0 - Add new input Attributes in action Query | Add new output Count in action Query
* 4.0.3 - Fix issue with connection documentation incorrectly stating a protocol prefix is required
* 4.0.2 - Fix issue where some host names were being incorrectly parsed
* 4.0.1 - Fix issue were logging of connection info did not display hostname correctly
* 4.0.0 - New action Modify Object | Rename Modify Groups action to 'Add or Remove an Object from Group' | Fix issue where non-ASCII characters were not being escaped
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

[Python LDAP3](https://ldap3.readthedocs.io)
[RFC4515](https://tools.ietf.org/search/rfc4515)
