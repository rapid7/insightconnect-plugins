# Description

[AD LDAP](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/3c5916a9-f1a0-429d-b937-f8fe672d777c) (Active Directory Lightweight Directory Access Protocol) is an application protocol for querying and modifying items in Active Directory. This plugin queries [Microsoft's Active Directory service](https://social.technet.microsoft.com/wiki/contents/articles/5392.active-directory-ldap-syntax-filters.aspx) to programmatically manage and query an Active Directory environment

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

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|chase_referrals|boolean|True|True|Allows the plugin to follow referrals from the specified Active Directory server to other Active Directory servers|None|True|None|None|
|host|string|None|True|Server Host, e.g. example.com|None|example.com|None|None|
|port|integer|389|True|Port, e.g. 389|None|389|None|None|
|use_channel_binding|boolean|None|True|Enable this option to require a secure TLS channel before binding, as needed for LDAP connections that enforce channel binding|None|False|None|None|
|use_ssl|boolean|None|True|Use SSL?|None|True|None|None|
|username_password|credential_username_password|None|True|Username and password|None|{"username":"user1", "password":"mypassword"}|None|None|

Example input:

```
{
  "chase_referrals": true,
  "host": "example.com",
  "port": 389,
  "use_channel_binding": false,
  "use_ssl": true,
  "username_password": {
    "password": "mypassword",
    "username": "user1"
  }
}
```

## Technical Details

### Actions


#### Add User

This action is used to add the specified Active Directory user

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|account_disabled|boolean|True|True|Set this to true to disable the user account at creation|None|True|None|None|
|additional_parameters|object|None|False|Add additional user parameters in JSON format|None|{"telephoneNumber":"(617)555-1234"}|None|None|
|domain_name|string|None|True|The domain name this user will belong to|None|example.com|None|None|
|first_name|string|None|True|User's first name|None|John|None|None|
|last_name|string|None|True|User's last name|None|Doe|None|None|
|logon_name|string|None|True|The logon name for the account|None|jdoe|None|None|
|password|password|None|True|The account's starting password|None|mypassword|None|None|
|user_ou|string|Users|True|The OU that the user account will be created in|None|Users|None|None|
|user_principal_name|string|None|True|The users principal name|None|user@example.com|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Operation status|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete

This action is used to delete the LDAP object specified

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|distinguished_name|string|None|True|The distinguished name of the object to delete|None|CN=user,OU=domain_users,DC=example,DC=com|None|None|
  
Example input:

```
{
  "distinguished_name": "CN=user,OU=domain_users,DC=example,DC=com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Operation status|True|
  
Example output:

```
{
  "success": true
}
```

#### Disable User

This action is used to disable an account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|distinguished_name|string|None|True|The distinguished name of the user to disable|None|CN=user,OU=domain_users,DC=example,DC=com|None|None|
  
Example input:

```
{
  "distinguished_name": "CN=user,OU=domain_users,DC=example,DC=com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Operation status|True|
  
Example output:

```
{
  "success": true
}
```

#### Disable Users

This action is used to disable multiple accounts

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|distinguished_names|[]string|None|True|The distinguished names of the users to disable|None|["CN=user,OU=domain_users,DC=example,DC=com"]|None|None|
  
Example input:

```
{
  "distinguished_names": [
    "CN=user,OU=domain_users,DC=example,DC=com"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|completed|[]string|False|List of successfully disabled users|["CN=user,OU=domain_users,DC=example,DC=com"]|
|failed|[]modified_user_error|False|List of unsuccessfully disabled users|[ { "dn": "CN=user,OU=domain_users,DC=test,DC=com", "error": "The DN CN=empty_search,DC=example,DC=com was not found" } ]|
  
Example output:

```
{
  "completed": [
    "CN=user,OU=domain_users,DC=example,DC=com"
  ],
  "failed": [
    {
      "dn": "CN=user,OU=domain_users,DC=test,DC=com",
      "error": "The DN CN=empty_search,DC=example,DC=com was not found"
    }
  ]
}
```

#### Enable User

This action is used to enable an account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|distinguished_name|string|None|True|The distinguished name of the user to enable|None|CN=user,OU=domain_users,DC=example,DC=com|None|None|
  
Example input:

```
{
  "distinguished_name": "CN=user,OU=domain_users,DC=example,DC=com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Operation status|True|
  
Example output:

```
{
  "success": true
}
```

#### Enable Users

This action is used to enable multiple accounts

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|distinguished_names|[]string|None|True|The distinguished names of the users to enable|None|["CN=user,OU=domain_users,DC=example,DC=com"]|None|None|
  
Example input:

```
{
  "distinguished_names": [
    "CN=user,OU=domain_users,DC=example,DC=com"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|completed|[]string|False|List of successfully enabled users|["CN=user,OU=domain_users,DC=example,DC=com"]|
|failed|[]modified_user_error|False|List of unsuccessfully enabled users|[ { "dn": "CN=user,OU=domain_users,DC=test,DC=com", "error": "The DN CN=empty_search,DC=example,DC=com was not found" } ]|
  
Example output:

```
{
  "completed": [
    "CN=user,OU=domain_users,DC=example,DC=com"
  ],
  "failed": [
    {
      "dn": "CN=user,OU=domain_users,DC=test,DC=com",
      "error": "The DN CN=empty_search,DC=example,DC=com was not found"
    }
  ]
}
```

#### Force Password Reset

This action is used to force a user to reset their password on next login

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|distinguished_name|string|None|True|The distinguished name of the user who will be forced to reset|None|CN=user,OU=domain_users,DC=example,DC=com|None|None|
  
Example input:

```
{
  "distinguished_name": "CN=user,OU=domain_users,DC=example,DC=com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Operation status|True|
  
Example output:

```
{
  "success": true
}
```

#### Add or Remove an Object from Group

This action is used to add or remove an object from an Active Directory group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|add_remove|string|None|True|Add or remove the group|["add", "remove"]|add|None|None|
|distinguished_name|string|None|True|The distinguished name of the object whose membership will be modified|None|CN=user,OU=domain_users,DC=mydomain,DC=com|None|None|
|group_dn|string|None|True|The Distinguished Name of the group to add or remove|None|CN=group_name,OU=domain_groups,DC=example,DC=com|None|None|
  
Example input:

```
{
  "add_remove": "add",
  "distinguished_name": "CN=user,OU=domain_users,DC=mydomain,DC=com",
  "group_dn": "CN=group_name,OU=domain_groups,DC=example,DC=com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Operation status|True|
  
Example output:

```
{
  "success": true
}
```

#### Modify Object

This action is used to modify the attributes for an Active Directory object

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|attribute_to_modify|string|None|True|The name of the attribute to modify|None|postalCode|None|None|
|attribute_value|string|None|True|The value of the attribute|None|02114|None|None|
|distinguished_name|string|None|True|The distinguished name of the object to modify|None|CN=user,OU=domain_users,DC=example,DC=com|None|None|
  
Example input:

```
{
  "attribute_to_modify": "postalCode",
  "attribute_value": "02114",
  "distinguished_name": "CN=user,OU=domain_users,DC=example,DC=com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Operation status|True|
  
Example output:

```
{
  "success": true
}
```

#### Move Object

This action is used to move an Active Directory object from one organizational unit to another

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|distinguished_name|string|None|True|The distinguished name of the user whose membership will be modified|None|CN=user,OU=domain_users,DC=example,DC=com|None|None|
|new_ou|string|None|True|The distinguished name of the OU to move the object to|None|OU=disabled_users,DC=example,DC=com|None|None|
  
Example input:

```
{
  "distinguished_name": "CN=user,OU=domain_users,DC=example,DC=com",
  "new_ou": "OU=disabled_users,DC=example,DC=com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Operation status|True|
  
Example output:

```
{
  "success": true
}
```

#### Query

This action is used to run an LDAP query

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|attributes|[]string|None|False|Attributes to search. If empty return all attributes|None|["createTimestamp", "creatorsName"]|None|None|
|search_base|string|None|True|The base of the search request|None|DC=example,DC=com|None|None|
|search_filter|string|None|True|The filter of the search request. It must conform to the LDAP filter syntax specified in RFC4515|None|(sAMAccountName=joesmith)|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|False|Number of results|1|
|results|[]result|False|Results returned|[{"dn":"string","attributes":{"pwdLastSet":"date","objectClass":["string","string","string","string"],"memberOf":["string"],"sAMAccountType":"int","uSNChanged":"int","givenName":"string","userPrincipalName":"string","countryCode":"int","lastLogon":"date","sAMAccountName":"string","name":"string","primaryGroupID":"int","dSCorePropagationData":["date"],"displayName":"string","logonCount":"int","cn":"string","objectSid":"string","codePage":"int","badPwdCount":"int","objectGUID":"string","distinguishedName":"string","whenChanged":"date","badPasswordTime":"date","instanceType":"int","uSNCreated":"int","sn":"string","whenCreated":"date","accountExpires":"date","userAccountControl":"int","lastLogoff":"date","objectCategory":"string"}}]|
  
Example output:

```
{
  "count": 1,
  "results": [
    {
      "attributes": {
        "accountExpires": "date",
        "badPasswordTime": "date",
        "badPwdCount": "int",
        "cn": "string",
        "codePage": "int",
        "countryCode": "int",
        "dSCorePropagationData": [
          "date"
        ],
        "displayName": "string",
        "distinguishedName": "string",
        "givenName": "string",
        "instanceType": "int",
        "lastLogoff": "date",
        "lastLogon": "date",
        "logonCount": "int",
        "memberOf": [
          "string"
        ],
        "name": "string",
        "objectCategory": "string",
        "objectClass": [
          "string",
          "string",
          "string",
          "string"
        ],
        "objectGUID": "string",
        "objectSid": "string",
        "primaryGroupID": "int",
        "pwdLastSet": "date",
        "sAMAccountName": "string",
        "sAMAccountType": "int",
        "sn": "string",
        "uSNChanged": "int",
        "uSNCreated": "int",
        "userAccountControl": "int",
        "userPrincipalName": "string",
        "whenChanged": "date",
        "whenCreated": "date"
      },
      "dn": "string"
    }
  ]
}
```

#### Query Group Membership

This action is used to return users and groups that belonging to the specific group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|expand_nested_groups|boolean|None|False|Expand nested groups in results|None|True|None|None|
|group_name|string|None|True|Name of the group for which membership will be checked|None|Domain Users|None|None|
|include_groups|boolean|None|False|Include groups in results|None|True|None|None|
|search_base|string|None|True|The base of the search request|None|DC=example,DC=com|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|False|Number of results|1|
|results|[]results|False|Results returned|[ { "attributes": { "accountExpires": "9999-12-31 23:59:59.999999+00:00", "adminCount": 0, "badPasswordTime": "1601-01-01 00:00:00+00:00", "badPwdCount": 0, "cn": "Example User", "codePage": 0, "countryCode": 0, "dSCorePropagationData": [ "2021-01-14 18:17:28+00:00", "2021-01-14 17:48:27+00:00", "1601-01-01 00:04:16+00:00" ], "description": [ "Example Account" ], "distinguishedName": "CN=Example User,CN=Users,DC=example,DC=com", "instanceType": 4, "isCriticalSystemObject": true, "lastLogoff": "1601-01-01 00:00:00+00:00", "lastLogon": "1601-01-01 00:00:00+00:00", "logonCount": 0, "memberOf": [ "CN=Domain Users,CN=Users,example,DC=com" ], "name": "Example User", "objectCategory": "CN=Person,CN=Schema,CN=Configuration,DC=example,DC=com", "objectClass": [ "top", "person", "organizationalPerson", "user" ], "objectGUID": "{b45138aa-be39-47d9-ab57-3aee8f381f87}", "objectSid": "S-1-5-33-3456299977-1009817396-2685666617-303", "primaryGroupID": 513, "pwdLastSet": "2021-01-14 17:48:26.197384+00:00", "sAMAccountName": "Example User", "sAMAccountType": 489006322, "showInAdvancedViewOnly": true, "uSNChanged": 16419, "uSNCreated": 12324, "userAccountControl": 514, "whenChanged": "2021-01-14 18:17:28+00:00", "whenCreated": "2021-01-14 17:48:26+00:00" }, "dn": "CN=Example User,CN=Users,DC=example,DC=com" } ]|
  
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

#### Reset Password

This action is used to reset a users password

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|distinguished_name|string|None|True|The distinguished name of the user whose membership will be modified|None|CN=user,OU=domain_users,DC=example,DC=com|None|None|
|new_password|password|None|True|The new password|None|mypassword|None|None|
  
Example input:

```
{
  "distinguished_name": "CN=user,OU=domain_users,DC=example,DC=com",
  "new_password": "mypassword"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Operation status|True|
  
Example output:

```
{
  "success": true
}
```

#### Unlock User

This action is used to unlock an account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|distinguished_name|string|None|True|The distinguished name of the user to unlock|None|CN=user,OU=domain_users,DC=example,DC=com|None|None|
  
Example input:

```
{
  "distinguished_name": "CN=user,OU=domain_users,DC=example,DC=com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Operation status|True|
  
Example output:

```
{
  "success": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**attributes**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Account Expires|string|None|False|Account expires|None|
|Admin Count|integer|None|False|Admin count|None|
|Bad Password Time|string|None|False|Bad password time|None|
|Bad PWD Count|integer|None|False|Bad PWD count|None|
|CN|string|None|False|CN|None|
|Code Page|integer|None|False|Code page|None|
|Country Code|integer|None|False|Country code|None|
|DS Core Propagation Data|[]string|None|False|DS core propagation data|None|
|Description|[]string|None|False|Description|None|
|Distinguished Name|string|None|False|Distinguished name|None|
|Instance Type|integer|None|False|Instance type|None|
|Is Critical System Object|boolean|None|False|Is critical system object|None|
|Last Log Off|string|None|False|Last log off|None|
|Last Log On|string|None|False|Last log on|None|
|Last Log On Timestamp|string|None|False|Last log on timestamp|None|
|Log On Count|integer|None|False|Log on count|None|
|Member Of|[]string|None|False|Member of|None|
|Name|string|None|False|Name|None|
|Object Category|string|None|False|Object category|None|
|Object Class|[]string|None|False|Object class|None|
|Object GUID|string|None|False|Object GUID|None|
|Object SID|string|None|False|Object SID|None|
|Primary Group ID|integer|None|False|Primary group ID|None|
|PWD Last Set|string|None|False|PWD last set|None|
|SAM Account Name|string|None|False|SAM account name|None|
|SAM Account Type|integer|None|False|SAM account type|None|
|USN changed|integer|None|False|USN changed|None|
|USN created|integer|None|False|USN created|None|
|User Account Control|integer|None|False|User account control|None|
|When Changed|string|None|False|When changed|None|
|When Created|string|None|False|When created|None|
  
**results**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attributes|attributes|None|False|Attributes|None|
|DN|string|None|False|DN|None|
  
**result**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attributes|object|None|None|None|None|
|DN|string|None|None|None|None|
  
**modified_user_error**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|DN|string|None|False|DN|None|
|Error|string|None|False|Error|None|


## Troubleshooting

* Objects that contain an equals sign `=` or an asterisk `*` require the signs to be escaped.
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

* 10.0.0 - Support for channel binding | Updated SDK to the latest version (6.3.3)
* 9.0.4 - Updated SDK to the latest version (6.2.5)
* 9.0.3 - Initial updates for fedramp compliance | Updated SDK to the latest version
* 9.0.2 - Updated the SDK to the latest version to address memory usage issues
* 9.0.1 - Fix problem where some ASCII characters were not escaped properly
* 9.0.0 - Action: `Disable User` & `Enable User` - Rename title of actions from `Disable` & `Enable` to `Disable Users` & `Enable Users` on the front-end.
* 8.0.0 - Update actions Enable Users and Enable Users to add outputs Completed and Failed and remove output All Operations Succeeded
* 7.0.0 - Update actions Enable Users and Enable Users to replace output Success with All Operations Succeeded True/False
* 6.0.0 - Add actions Enable Users and Disable users allowing for the bulk enablement/disablement of users
* 5.3.5 - Fix issue where JSON Marshaling error was raised when receiving unexpected API response in the Force Password Reset action
* 5.3.4 - Fix issue with space character in DN in modify object action | Enhanced LDAP logging | Fix issue with variable error when connection fails
* 5.3.3 - Fix issue with escaping brackets in Query action
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

* [Learn Azure Active Directory](https://learn.microsoft.com/en-us/azure/active-directory/)
* [AD LDAP](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/3c5916a9-f1a0-429d-b937-f8fe672d777c)
* [Microsoft's Active Directory service](https://social.technet.microsoft.com/wiki/contents/articles/5392.active-directory-ldap-syntax-filters.aspx)

## References

* [Python LDAP3](https://ldap3.readthedocs.io)
* [RFC4515](https://tools.ietf.org/search/rfc4515)