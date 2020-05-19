# Description

[Check Point’s Next Generation Firewalls (NGFW’s)](https://www.checkpoint.com/products/next-generation-firewall/) are trusted by customers for their highest security effectiveness and their ability to keep organizations protected from sophisticated fifth generation cyber-attacks.

# Key Features

* Add and remove hosts
* Add and remove access rules
* Show rulebase
* Discard all sessions

# Requirements

* Username and password with administrative privileges
* Check Point API is enabled and running. This requires that the NGFW machine has 6GB of RAM available, and the API has been enabled
* For more information on enabling the API visit here: https://community.checkpoint.com/t5/API-CLI-Discussion-and-Samples/Enabling-web-api/td-p/32641
* Make sure the IP of the orchestrator running this plugin is set as an allowed host in Checkpoint

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|port|integer|443|True|Check Point server port|None|443|
|server|string|None|True|Check Point server IP address|None|198.168.2.1|
|ssl_verify|boolean|True|True|Use SSL verification|None|True|
|username_password|credential_username_password|None|True|Username and password|None|None|

Example input:

```
{
  "port": 443,
  "server": "198.168.2.1",
  "ssl_verify": true
}
```

## Technical Details

### Actions

#### Check if Address in Group

This action checks to see if an IP, CIDR, or domain is in an Address Group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|Address to check in the group|None|198.51.100.100|
|discard_other_sessions|boolean|True|True|Discard all other user sessions. This can fix errors when objects are locked by other sessions|None|True|
|enable_search|boolean|False|False|Search contents of address objects for IP addresses, CIDR IP addresses, or domains|None|False|
|group|string|None|False|Group to check. UID is not supported|None|InsightConnect Block List|

Example input:

```
{
  "address": "198.51.100.100",
  "discard_other_sessions": true,
  "enable_search": false,
  "group": "InsightConnect Block List"
}
```

##### Output

_This action does not contain any outputs._

#### Install Policy

This action is used to install a policy to selected targets.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|access_control_policy|boolean|True|True|Set to be true in order to install the Access Control policy. By default, the value is true if Access Control policy is enabled on the input policy package, otherwise false|None|True|
|desktop_security_policy|boolean|False|True|Set to be true in order to install the Desktop Security policy. By default, the value is true if desktop security policy is enabled on the input policy package, otherwise false|None|False|
|discard_other_sessions|boolean|False|True|Discard all other user sessions. This can fix errors when objects are locked by other sessions|None|False|
|install_on_all_cluster_members_or_fail|boolean|False|True|Relevant for the gateway clusters. If true, the policy is installed on all the cluster members. If the installation on a cluster member fails, don't install on that cluster|None|False|
|policy_package|string|standard|True|Policy package to install|None|standard|
|qos_policy|boolean|False|True|Set to be true in order to install the QoS policy. By default, the value is true if Quality-of-Service policy is enabled on the input policy package, otherwise false|None|False|
|targets|[]string|["target name"]|True|On what targets to execute this command. Targets may be identified by their name, or object unique identifier|None|["checkpoint_fw_1", "checkpoint_fw_2"]|
|threat_prevention_policy|boolean|True|True|Set to be true in order to install the Threat Prevention policy. By default, the value is true if Threat Prevention policy is enabled on the input policy package, otherwise false|None|True|

Example input:

```
{
  "access_control_policy": true,
  "desktop_security_policy": false,
  "discard_other_sessions": false,
  "install_on_all_cluster_members_or_fail": false,
  "policy_package": "standard",
  "qos_policy": false,
  "targets": [
    "checkpoint_fw_1",
    "checkpoint_fw_2"
  ],
  "threat_prevention_policy": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Success|

Example output:

```
{
  "success": true
}
```

#### Set Threat Protection

This action is used to set a threat protection action.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|None|True|Action|['Inactive', 'Detect', 'Prevent', 'Drop', 'Accept']|Prevent|
|discard_other_sessions|boolean|True|True|Discard all other user sessions. This can fix errors when objects are locked by other sessions|None|True|
|name|string|None|True|Name of the protection to act on|None|Blaster Attacks|
|profile|string|Optimized|True|Profile e.g. Optimized, Basic, Strict|None|Optimized|

Example input:

```
{
  "action": "Prevent",
  "discard_other_sessions": true,
  "name": "Blaster Attacks",
  "profile": "Optimized"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
{
  "success": true
}
```

#### Add Host to Network Group

This action is used to add a host to a network group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|discard_other_sessions|boolean|True|True|Discard all other user sessions. This can fix errors when objects are locked by other sessions|None|None|
|group_name|string|None|True|Name of the group to add this object to|None|None|
|host_name|string|None|True|The host to add to the network group, usually the IP address|None|None|

Example input:

```
{
  "color": "black",
  "discard_other_sessions": true,
  "host_ip": "192.168.2.1",
  "name": "192.168.2.1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Success|

Example output:

```
{
  "success": true
}
```

#### Discard All Sessions

This action is a troubleshooting action that will discard all active sessions. This can sometimes alleviate the 
issue where objects remain locked after editing. 

##### Input

_This action does not contain any inputs._

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Success|

Example output:

```
{
  "success": true
}
```

#### Remove Host

This action is used to remove a host from network objects.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|discard_other_sessions|boolean|True|True|Discard all other user sessions. This can fix errors when objects are locked by other sessions|None|True|
|name|string|None|True|Name|None|192.168.2.1|

Example input:

```
{
  "discard_other_sessions": true,
  "name": "192.168.2.1"
}
```

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

This action is used to add a host as a network object.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|color|string|black|False|Color|['black', 'aquamarine', 'blue', 'brown', 'burlywood', 'coral', 'crete', 'cyan', 'dark blue', 'dark gold', 'dark gray', 'dark green', 'dark orange', 'dark sea green', 'firebrick', 'forest green', 'gold', 'gray', 'khaki', 'lemon chiffon', 'light green', 'magenta', 'navy blue', 'olive', 'orange', 'orchid', 'pink', 'purple', 'red', 'sea green', 'sienna', 'sky blue', 'slate blue', 'turquoise', 'violet red', 'yellow']|black|
|discard_other_sessions|boolean|True|True|Discard all other user sessions. This can fix errors when objects are locked by other sessions|None|True|
|host_ip|string|None|True|Host IP address|None|192.168.2.1|
|name|string|None|True|Name|None|192.168.2.1|

Example input:

```
{
  "color": "black",
  "discard_other_sessions": true,
  "host_ip": "192.168.2.1",
  "name": "192.168.2.1"
}
```

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

This action is used to remove an access rule.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|access_rule_name|string|None|True|Access rule name|None|InsightConnect Access Rule|
|discard_other_sessions|boolean|True|True|Discard all other user sessions. This can fix errors when objects are locked by other sessions|None|True|
|layer|string|Network|True|Layer|None|Network|

Example input:

```
{
  "access_rule_name": "InsightConnect Access Rule",
  "discard_other_sessions": true,
  "layer": "Network"
}
```

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

This action is used to show the access rulebase.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|layer_name|string|Network|True|Layer name|None|Network|
|limit|integer|500|False|Limit|None|500|

Example input:

```
{
  "layer_name": "Network",
  "limit": 500
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|Drop|True|Action to take|['Accept', 'Drop', 'Ask', 'Inform', 'Reject', 'User Auth', 'Client Auth', 'Apply Layer']|Drop|
|destination|string|None|False|Destination network object name|None|192.168.2.1|
|discard_other_sessions|boolean|True|True|Discard all other user sessions. This can fix errors when objects are locked by other sessions|None|True|
|layer|string|Network|True|Layer to add this rule to|None|Network|
|list_of_services|[]string|None|False|List of services to block|None|["AOL", "SMTP"]|
|name|string|None|True|Rule name|None|Malicious IP Addresses|
|position|string|top|True|Position in the list of rules. e.g. top, bottom, 15|None|1|
|source|string|None|False|Source network object name|None|192.168.2.1|

Example input:

```
{
  "action": "Drop",
  "destination": "192.168.2.1",
  "discard_other_sessions": true,
  "layer": "Network",
  "list_of_services": [
    "AOL",
    "SMTP"
  ],
  "name": "Malicious IP Addresses",
  "position": 1,
  "source": "192.168.2.1"
}
```

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

Connections to the Check Point security management is based upon client to server sessions. Multiple administrators may connect 
at one time and from R80.20 M1, one administrator can open more than one session at a time. Policy and objects are locked when 
an administrator makes changes to those objects. The lock is released when a publish or discard occurs.

If the plugin tries to make a change while an administrator has a pending change, 
the plugin will sometimes fail. To prevent this, you can set the Discard Other Changes boolean value 
to True in each action. That will effectively remove all other pending changes when the 
plugin tries to publish its changes. A best practice is to have separate administrator accounts so that you can 
better track changes done via the plugin or manually via SmartConsole.

### Common Errors

#### 403 Forbidden

If you are presented with a `403 Forbidden` error when running the connection test, the API hasn't been enabled and will need to be enabled for the connection test to succeed.
 
For more information on enabling the API visit: 

[https://community.checkpoint.com/t5/API-CLI-Discussion-and-Samples/Enabling-web-api/td-p/32641]( https://community.checkpoint.com/t5/API-CLI-Discussion-and-Samples/Enabling-web-api/td-p/32641)

#### err_login_failed

If the plugin gives this error during the connection test: 

```
{
  "code" : "err_login_failed",
  "message" : "Authentication to server failed."
}
```

Verify the password on the account you are using. Make sure the user that you are logging in with has administrative
privileges.

# Version History

* 1.3.0 - Update to add install options to Install Policy
* 1.2.0 - New action Install Policy | Fix issue where logout could fail | Update to help to improve troubleshooting | Update to `Add Host` action to with color option 
* 1.1.0 - New action Add Host to Network Group
* 1.0.0 - Initial plugin

# Links

## References

* [Check Point NGFW](https://www.checkpoint.com/products/next-generation-firewall/)
* [Check Point Management API](https://sc1.checkpoint.com/documents/latest/APIs/)
