# Description

[Check Point’s Next Generation Firewalls (NGFW’s)](https://www.checkpoint.com/products/next-generation-firewall/) are trusted by customers for their highest security effectiveness and their ability to keep organizations protected from sophisticated fifth generation cyber-attacks.

# Key Features

Actions and triggers that utilize Check Point NGFW api.

# Requirements

* Username and Password with administrative privileges
* Check Point API is up and running. This requires that the NGFW machine has 6 gb of ram available, and the API has been enabled
* For more information on enabling the API go here: https://community.checkpoint.com/t5/API-CLI-Discussion-and-Samples/Enabling-web-api/td-p/32641

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|port|int|443|True|Server port|None|
|server|string|None|True|Server IP|None|
|ssl_verify|boolean|True|True|Use SSL verification|None|
|username_password|credential_username_password|None|True|Username and password|None|

## Technical Details

### Actions

#### Discard All Sessions

This action is used to troubleshooting action to discard all other user sessions.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Success|

Example output:

```
```

#### Remove Host

This action is used to remove Host from network objects.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|discard_other_sessions|boolean|True|True|Discard all other user sessions. This can fix errors when objects are locked by other sessions|None|
|name|string|None|True|Name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Remove operation status|
|success|boolean|True|Success|

Example output:

```
{
  "message": "OK",
  "success": true
}
```

#### Add Host

This action is used to add Host as a network object.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|discard_other_sessions|boolean|True|True|Discard all other user sessions. This can fix errors when objects are locked by other sessions|None|
|host_ip|string|None|True|Host IP|None|
|name|string|None|True|Name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|host_object|host_object|True|Information about the host that was added|

Example output:

```
{
  "host_object": {
    "uid": "70c9580f-0708-4878-8fdd-98bd4f6d3b44",
    "name": "192.1.2.1",
    "type": "host",
    "domain": {
      "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
      "name": "SMC User",
      "domain-type": "domain"
    },
    "ipv4-address": "192.1.2.1",
    "interfaces": [],
    "nat-settings": {
      "auto-rule": false
    },
    "groups": [],
    "comments": "",
    "color": "black",
    "icon": "Objects/host",
    "tags": [],
    "meta-info": {
      "lock": "unlocked",
      "validation-state": "ok",
      "last-modify-time": {
        "posix": 1583272492299,
        "iso-8601": "2020-03-03T16:54-0500"
      },
      "last-modifier": "api_admin",
      "creation-time": {
        "posix": 1583272492299,
        "iso-8601": "2020-03-03T16:54-0500"
      },
      "creator": "api_admin"
    },
    "read-only": true
  }
}
```

#### Remove Access Rule

This action is used to remove access rule.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|access_rule_name|string|None|True|Access rule name|None|
|discard_other_sessions|boolean|True|True|Discard all other user sessions. This can fix errors when objects are locked by other sessions|None|
|layer|string|Network|True|Layer|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Remove operation status|
|success|boolean|True|Success|

Example output:

```
{
  "message": "OK",
  "success": true
}
```

#### Show Access Rulebase

This action is used to show access rulebase.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|layer_name|string|Network|True|Layer name|None|
|limit|int|500|False|Limit|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|access_rules|rulebase_type|False|Access rules|

Example output:

```
{
  "access_rules": {
    "uid": "50c71672-c7da-40cb-92ae-5c10d61f6739",
    "name": "Network",
    "rulebase": [
      {
        "uid": "6ea80837-2b05-4436-a6d9-75025070a8e5",
        "name": "Cleanup rule",
        "type": "access-rule",
        "domain": {
          "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
          "name": "SMC User",
          "domain-type": "domain"
        },
        "rule-number": 1,
        "track": {
          "type": "29e53e3d-23bf-48fe-b6b1-d59bd88036f9",
          "per-session": false,
          "per-connection": false,
          "accounting": false,
          "alert": "none"
        },
        "source": [
          "97aeb369-9aea-11d5-bd16-0090272ccb30"
        ],
        "source-negate": false,
        "destination": [
          "97aeb369-9aea-11d5-bd16-0090272ccb30"
        ],
        "destination-negate": false,
        "service": [
          "97aeb369-9aea-11d5-bd16-0090272ccb30"
        ],
        "service-negate": false,
        "vpn": [
          "97aeb369-9aea-11d5-bd16-0090272ccb30"
        ],
        "action": "6c488338-8eec-4103-ad21-cd461ac2c473",
        "action-settings": {},
        "content": [
          "97aeb369-9aea-11d5-bd16-0090272ccb30"
        ],
        "content-negate": false,
        "content-direction": "any",
        "time": [
          "97aeb369-9aea-11d5-bd16-0090272ccb30"
        ],
        "custom-fields": {},
        "meta-info": {
          "lock": "unlocked",
          "validation-state": "ok",
          "last-modify-time": {
            "posix": 1539118183442,
            "iso-8601": "2018-10-09T16:49-0400"
          },
          "last-modifier": "System",
          "creation-time": {
            "posix": 1539118183442,
            "iso-8601": "2018-10-09T16:49-0400"
          },
          "creator": "System"
        },
        "enabled": true,
        "install-on": [
          "6c488338-8eec-4103-ad21-cd461ac2c476"
        ]
      }
    ],
    "objects-dictionary": [
      {
        "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
        "name": "Any",
        "type": "CpmiAnyObject",
        "domain": {
          "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
          "name": "Check Point Data",
          "domain-type": "data domain"
        },
        "color": "black",
        "meta-info": {
          "validation-state": "ok",
          "last-modify-time": {
            "posix": 1539092746487,
            "iso-8601": "2018-10-09T09:45-0400"
          },
          "last-modifier": "System",
          "creation-time": {
            "posix": 1539092746487,
            "iso-8601": "2018-10-09T09:45-0400"
          },
          "creator": "System"
        },
        "tags": [],
        "icon": "General/globalsAny"
      },
      {
        "uid": "6c488338-8eec-4103-ad21-cd461ac2c473",
        "name": "Drop",
        "type": "RulebaseAction",
        "domain": {
          "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
          "name": "Check Point Data",
          "domain-type": "data domain"
        },
        "color": "none",
        "meta-info": {
          "validation-state": "ok",
          "last-modify-time": {
            "posix": 1539092770251,
            "iso-8601": "2018-10-09T09:46-0400"
          },
          "last-modifier": "System",
          "creation-time": {
            "posix": 1539092770251,
            "iso-8601": "2018-10-09T09:46-0400"
          },
          "creator": "System"
        },
        "tags": [],
        "icon": "Actions/actionsDrop",
        "comments": "Drop",
        "display-name": "Drop"
      },
      {
        "uid": "29e53e3d-23bf-48fe-b6b1-d59bd88036f9",
        "name": "None",
        "type": "Track",
        "domain": {
          "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
          "name": "Check Point Data",
          "domain-type": "data domain"
        },
        "color": "none",
        "meta-info": {
          "validation-state": "ok",
          "last-modify-time": {
            "posix": 1539092769942,
            "iso-8601": "2018-10-09T09:46-0400"
          },
          "last-modifier": "System",
          "creation-time": {
            "posix": 1539092769942,
            "iso-8601": "2018-10-09T09:46-0400"
          },
          "creator": "System"
        },
        "tags": [],
        "icon": "General/globalsNone",
        "comments": "No tracking."
      },
      {
        "uid": "6c488338-8eec-4103-ad21-cd461ac2c476",
        "name": "Policy Targets",
        "type": "Global",
        "domain": {
          "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
          "name": "Check Point Data",
          "domain-type": "data domain"
        },
        "color": "none",
        "meta-info": {
          "validation-state": "ok",
          "last-modify-time": {
            "posix": 1539092769822,
            "iso-8601": "2018-10-09T09:46-0400"
          },
          "last-modifier": "System",
          "creation-time": {
            "posix": 1539092769822,
            "iso-8601": "2018-10-09T09:46-0400"
          },
          "creator": "System"
        },
        "tags": [],
        "icon": "General/globalsAny",
        "comments": "The policy target gateways"
      }
    ],
    "from": 1,
    "to": 1,
    "total": 1
  }
}
```

#### Add Access Rule

This action is used to create a rule to block traffic.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|action|string|Drop|True|Action to take|['Accept', 'Drop', 'Ask', 'Inform', 'Reject', 'User Auth', 'Client Auth', 'Apply Layer']|
|destination|string|None|False|Destination network object name|None|
|discard_other_sessions|boolean|True|True|Discard all other user sessions. This can fix errors when objects are locked by other sessions|None|
|layer|string|Network|True|Layer to add this rule to|None|
|list_of_services|[]string|None|True|List of services to block. e.g. ["AOL", "SMTP"]|None|
|name|string|None|True|Rule name|None|
|position|string|top|True|Postion in the list of rules. e.g. top, bottom, 15|None|
|source|string|None|False|Source network object name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|access_rule|access_rule|True|The rule that was created|

Example output:

```
{
  "uid": "c8e7657e-dd78-4189-9999-78546892db06",
  "name": "Rule 1",
  "type": "access-rule",
  "domain": {
    "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
    "name": "SMC User",
    "domain-type": "domain"
  },
  "track": {
    "type": {
      "uid": "29e53e3d-23bf-48fe-b6b1-d59bd88036f9",
      "name": "None",
      "type": "Track",
      "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain"
      }
    },
    "per-session": false,
    "per-connection": false,
    "accounting": false,
    "alert": "none"
  },
  "layer": "50c71672-c7da-40cb-92ae-5c10d61f6739",
  "source": [
    {
      "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
      "name": "Any",
      "type": "CpmiAnyObject",
      "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain"
      }
    }
  ],
  "source-negate": false,
  "destination": [
    {
      "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
      "name": "Any",
      "type": "CpmiAnyObject",
      "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain"
      }
    }
  ],
  "destination-negate": false,
  "service": [
    {
      "uid": "97aeb44f-9aea-11d5-bd16-0090272ccb30",
      "name": "AOL",
      "type": "service-tcp",
      "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain"
      },
      "port": "5190"
    }
  ],
  "service-negate": false,
  "vpn": [
    {
      "uid": "66b5d03a-a64e-481f-97d9-4a61f8602840",
      "name": "MyIntranet",
      "type": "vpn-community-meshed",
      "domain": {
        "uid": "41e821a0-3720-11e3-aa6e-0800200c9fde",
        "name": "SMC User",
        "domain-type": "domain"
      }
    }
  ],
  "action": {
    "uid": "6c488338-8eec-4103-ad21-cd461ac2c473",
    "name": "Drop",
    "type": "RulebaseAction",
    "domain": {
      "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
      "name": "Check Point Data",
      "domain-type": "data domain"
    }
  },
  "action-settings": {},
  "content": [
    {
      "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
      "name": "Any",
      "type": "CpmiAnyObject",
      "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain"
      }
    }
  ],
  "content-negate": false,
  "content-direction": "any",
  "time": [
    {
      "uid": "97aeb369-9aea-11d5-bd16-0090272ccb30",
      "name": "Any",
      "type": "CpmiAnyObject",
      "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain"
      }
    }
  ],
  "custom-fields": {
    "field-1": "",
    "field-2": "",
    "field-3": ""
  },
  "meta-info": {
    "lock": "locked by current session",
    "validation-state": "ok",
    "last-modify-time": {
      "posix": 1582906756962,
      "iso-8601": "2020-02-28T11:19-0500"
    },
    "last-modifier": "admin",
    "creation-time": {
      "posix": 1582906756962,
      "iso-8601": "2020-02-28T11:19-0500"
    },
    "creator": "admin"
  },
  "comments": "",
  "enabled": true,
  "install-on": [
    {
      "uid": "6c488338-8eec-4103-ad21-cd461ac2c476",
      "name": "Policy Targets",
      "type": "Global",
      "domain": {
        "uid": "a0bbbc99-adef-4ef8-bb6d-defdefdefdef",
        "name": "Check Point Data",
        "domain-type": "data domain"
      }
    }
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### access_rule

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Action|action_type|False|Action|
|Action-Settings|object|False|Action-settings|
|Comments|string|False|Comments|
|Content|[]action_type|False|Content|
|Content-Direction|string|False|Content-direction|
|Content-Negate|boolean|False|Content-negate|
|Custom-Fields|object|False|Custom-fields|
|Destination|[]action_type|False|Destination|
|Destination-Negate|boolean|False|Destination-negate|
|Domain|domain|False|Domain|
|Enabled|boolean|False|Enabled|
|Install-On|[]action_type|False|Install-on|
|Layer|string|False|Layer|
|Meta-Info|meta_info_type|False|Meta-info|
|Name|string|False|Name|
|Service|[]objects_dictionary_type|False|Service|
|Service-Negate|boolean|False|Service-negate|
|Source|[]action_type|False|Source|
|Source-Negate|boolean|False|Source-negate|
|Time|[]action_type|False|Time|
|Track|track|False|Track|
|Type|string|False|Type|
|UID|string|False|UID|
|VPN|[]action_type|False|VPN|

#### action_type

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Domain|domain|False|Domain|
|Name|string|False|Name|
|Type|string|False|Type|
|UID|string|False|UID|

#### creation_time_type

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ISO-8601|string|False|ISO-8601|
|POSIX|integer|False|POSIX|

#### domain

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Domain-Type|string|False|Domain-type|
|Name|string|False|Name|
|UID|string|False|UID|

#### host_object

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Color|string|False|Color|
|Comments|string|False|Comments|
|Domain|domain|False|Domain|
|Groups|[]object|False|Groups|
|Icon|string|False|Icon|
|Interfaces|[]object|False|Interfaces|
|IPv4-Address|string|False|IPv4-address|
|Meta-Info|meta_info_type|False|Meta-info|
|Name|string|False|Name|
|NAT-Settings|object|False|NAT-settings|
|Read-Only|boolean|False|Read-only|
|Tags|[]object|False|Tags|
|Type|string|False|Type|
|UID|string|False|UID|

#### meta-info_0

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Creation-Time|creation_time_type|False|Creation-time|
|Creator|string|False|Creator|
|Last-Modifier|string|False|Last-modifier|
|Last-Modify-Time|creation_time_type|False|Last-modify-time|
|Lock|string|False|Lock|
|Validation-State|string|False|Validation-state|

#### meta_info_type

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Creation-Time|creation_time_type|False|Creation-time|
|Creator|string|False|Creator|
|Last-Modifier|string|False|Last-modifier|
|Last-Modify-Time|creation_time_type|False|Last-modify-time|
|Lock|string|False|Lock|
|Validation-State|string|False|Validation-state|

#### objects_dictionary_type

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Color|string|False|Color|
|Comments|string|False|Comments|
|Custom Fields|object|False|Custom fields|
|Display-Name|string|False|Display-name|
|Domain|domain|False|Domain|
|Icon|string|False|Icon|
|Meta-Info|meta_info_type|False|Meta-info|
|Name|string|False|Name|
|Port|string|False|Port|
|Tags|[]object|False|Tags|
|Type|string|False|Type|
|UID|string|False|UID|

#### rulebase_type

|Name|Type|Required|Description|
|----|----|--------|-----------|
|From|integer|False|From|
|Name|string|False|Name|
|Objects-Dictionary|[]objects_dictionary_type|False|Objects-dictionary|
|Rulebase|[]objects_dictionary_type|False|Rulebase|
|To|integer|False|To|
|Total|integer|False|Total|
|UID|string|False|UID|

#### track

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Accounting|boolean|False|Accounting|
|Alert|string|False|Alert|
|Per-Connection|boolean|False|Per-connection|
|Per-Session|boolean|False|Per-session|
|Type|action_type|False|Type|

## Troubleshooting

An issue with Check Point servers is that only one user may make changes to the server at a time. If two users make 
edits to the configuration at the same time, one user's edits will fail. The API handles this through Session IDs 
(SIDs). If the plugin tries to make a change while an administrator has a pending change, the plugin will sometimes 
fail. 

To prevent this, you can turn on discard other changes, which will effectively remove all other pending changes when the 
plugin tries to publish it's changes. However, this can cause issues with the web portal and Smart Console. If the 
Smart Console starts displaying errors, the administrator will have to close the Smart Console and reopen it.

To effectively use this plugin, it will need it's own administrative account. This will help prevent session conflicts.  

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Checkpoint NGFW](https://www.checkpoint.com/products/next-generation-firewall/)
* [Check Point Management API](https://sc1.checkpoint.com/documents/latest/APIs/)
