# Description

The `freeipa` InsightConnect plugin retrieve user details, status and delete user from [FreeIPA](https://www.freeipa.org/) which is an integrated Identity and Authentication solution for Linux/UNIX networked environments.
This plugin runs commands on a FreeIPA server using this [freeipa](https://github.com/nordnet/python-freeipa-json) python library.
The FreeIPA API is viewable on the FreeIPA server web interface.

# Key Features

* Search user and retrieve user details
* Delete user

# Requirements

* Username and Password to logon to [freeipa](https://www.freeipa.org/) server.

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|Username to logon to FreeIPA server|None|
|password|password|None|True|Password|None|
|server|string|None|True|The name of the FreeIPA server e.g. ipa.demo1.freeipa.org|None|

## Technical Details

### Actions

#### User Status

This action returns information on a user's status.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|The UID of the user to return status of|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|Boolean showing the status of the request|
|full_message|user_status_output|False|All data returned by the request|

Example output:

```

{
  "success": true,
  "full_message": {
    "dn": "uid=helpdesk,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org",
    "krblastsuccessfulauth": [
      "N/A"
    ],
    "krblastfailedauth": [
      "N/A"
    ],
    "krbloginfailedcount": [
      "0"
    ],
    "server": "ipa.demo1.freeipa.org",
    "now": "2018-04-03T15:14:03Z"
  }
}

```

#### Find User

This action is used to search for a user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|search_parameters|string|None|False|A string to look for in relevant user fields. If blank will return all users with a return limit of 40000|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|full_message|[]find_user_output|False|All stored information match the search criteria|
|users|[]string|False|A list of users that match the search criteria|

Example output:

```

{
  "users": [
    "helpdesk"
  ],
  "full_output": [
    {
      "displayname": [
        "Test Helpdesk"
      ],
      "objectclass": [
        "top",
        "person",
        "organizationalperson",
        "inetorgperson",
        "inetuser",
        "posixaccount",
        "krbprincipalaux",
        "krbticketpolicyaux",
        "ipaobject",
        "ipasshuser",
        "ipaSshGroupOfPubKeys",
        "mepOriginEntry",
        "ipantuserattrs"
      ],
      "initials": [
        "TH"
      ],
      "gecos": [
        "Test Helpdesk"
      ],
      "cn": [
        "Test Helpdesk"
      ],
      "ipauniqueid": [
        "2dc4c184-5417-11e7-955e-064e44e5853f"
      ],
      "krblastpwdchange": [
        "20170618111338Z"
      ],
      "krbextradata": [
        {
          "__base64__": "AAJiYEZZa2FkbWluZEBERU1PMS5GUkVFSVBBLk9SRwA="
        }
      ],
      "mepmanagedentry": [
        "cn=helpdesk,cn=groups,cn=accounts,dc=demo1,dc=freeipa,dc=org"
      ],
      "ipantsecurityidentifier": [
        "S-1-5-21-3514317308-1802916877-2057042358-1005"
      ],
      "krbticketflags": [
        "128"
      ],
      "krbloginfailedcount": [
        "0"
      ],
      "krbcanonicalname": [
        "helpdesk@DEMO1.FREEIPA.ORG"
      ],
      "uid": [
        "helpdesk"
      ],
      "sn": [
        "Helpdesk"
      ],
      "uidnumber": [
        "1198600005"
      ],
      "homedirectory": [
        "/home/helpdesk"
      ],
      "givenname": [
        "Test"
      ],
      "gidnumber": [
        "1198600005"
      ],
      "mail": [
        "helpdesk@demo1.freeipa.org"
      ],
      "krbprincipalname": [
        "helpdesk@DEMO1.FREEIPA.ORG"
      ],
      "loginshell": [
        "/bin/sh"
      ],
      "nsaccountlock": false,
      "preserved": false,
      "memberof_group": [
        "ipausers"
      ],
      "memberof_role": [
        "helpdesk"
      ],
      "dn": "uid=helpdesk,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org"
    }
  ]
}

```

#### Show User

This action is used to return all available information on a specified user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|The login name of the user to search for|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|Boolean showing the status of the request|
|full_message|show_user_out|False|All data returned by the request|

Example output:

```

{
  "success": true,
  "full_message": {
    "displayname": [
      "Test Helpdesk"
    ],
    "objectclass": [
      "top",
      "person",
      "organizationalperson",
      "inetorgperson",
      "inetuser",
      "posixaccount",
      "krbprincipalaux",
      "krbticketpolicyaux",
      "ipaobject",
      "ipasshuser",
      "ipaSshGroupOfPubKeys",
      "mepOriginEntry",
      "ipantuserattrs"
    ],
    "initials": [
      "TH"
    ],
    "gecos": [
      "Test Helpdesk"
    ],
    "cn": [
      "Test Helpdesk"
    ],
    "ipauniqueid": [
      "2dc4c184-5417-11e7-955e-064e44e5853f"
    ],
    "krblastpwdchange": [
      "20170618111338Z"
    ],
    "krbextradata": [
      {
        "__base64__": "AAJiYEZZa2FkbWluZEBERU1PMS5GUkVFSVBBLk9SRwA="
      }
    ],
    "mepmanagedentry": [
      "cn=helpdesk,cn=groups,cn=accounts,dc=demo1,dc=freeipa,dc=org"
    ],
    "ipantsecurityidentifier": [
      "S-1-5-21-3514317308-1802916877-2057042358-1005"
    ],
    "krbticketflags": [
      "128"
    ],
    "krbloginfailedcount": [
      "0"
    ],
    "krbcanonicalname": [
      "helpdesk@DEMO1.FREEIPA.ORG"
    ],
    "uid": [
      "helpdesk"
    ],
    "homedirectory": [
      "/home/helpdesk"
    ],
    "gidnumber": [
      "1198600005"
    ],
    "mail": [
      "helpdesk@demo1.freeipa.org"
    ],
    "krbprincipalname": [
      "helpdesk@DEMO1.FREEIPA.ORG"
    ],
    "sn": [
      "Helpdesk"
    ],
    "uidnumber": [
      "1198600005"
    ],
    "givenname": [
      "Test"
    ],
    "loginshell": [
      "/bin/sh"
    ],
    "nsaccountlock": false,
    "has_password": true,
    "has_keytab": true,
    "preserved": false,
    "memberof_role": [
      "helpdesk"
    ],
    "memberof_group": [
      "ipausers"
    ],
    "dn": "uid=helpdesk,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org"
  }
}

```

#### Delete User

This action is used to delete a user.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|The UID of the user to delete|None|
|preserve|boolean|None|True|If true the user will be preserved rather than deleted|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|Status of the delete User request. Will be false if |
|summary|string|False|A summary of the deleted user|

Example output:

```

{
  "summary": "Deleted user 'tuser'"
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

For the delete user action, setting `Preserve` to `True` will preserve the user rather than deleting them.
Note that deletion is permanent and cannot be undone.

# Version History

* 2.0.0 - Support web server mode | Update to new credential types
* 1.0.0 - Initial plugin

# Links

## References

* [FreeIPA Demo](https://ipa.demo1.freeipa.org)
* [ipahttp library](https://github.com/nordnet/python-freeipa-json)

