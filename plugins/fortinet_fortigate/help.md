# Description

[FortiGate Next Generation Firewalls (NGFWs)](https://www.fortinet.com/) enable security-driven networking and consolidate industry-leading security capabilities such as intrusion prevention system (IPS), web filtering, secure sockets layer (SSL) inspection, and automated threat protection

# Key Features

* Create network address objects
* Add address object to address groups

* The intended way to use this plugin is to have an existing policy in place with a predefined address group in it.
As threats are detected, their address can be added to your existing policy through the address group. This allows for flexible policy management of large groups of dynamic addresses

# Requirements

* An admin API key
* The IP of the orchestrator must be set as a trusted host in Settings > Administrator (Edit button) > Trusted Hosts

# Supported Product Versions

* 7.2.4

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|API key|None|2Fty5834tFpBdidePJnt9075MMdkUb|None|None|
|hostname|string|None|True|Hostname or IP of your FortiGate server e.g. myfortigate.internal, 192.168.10.1, 192.168.10.1:8000|None|example.com|None|None|
|ssl_verify|boolean|False|True|SSL verify|None|False|None|None|

Example input:

```
{
  "api_key": "2Fty5834tFpBdidePJnt9075MMdkUb",
  "hostname": "example.com",
  "ssl_verify": false
}
```

## Technical Details

### Actions


#### Add Address Object to Group

This action is used to add an address object to an address group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address_object|string|None|True|Address object|None|MaliciousHost|None|None|
|group|string|None|True|Group name|None|InsightConnect Block List|None|None|
|ipv6_group|string|None|True|The name of the IPv6 address group|None|InsightConnect IPv6 Block List|None|None|
  
Example input:

```
{
  "address_object": "MaliciousHost",
  "group": "InsightConnect Block List",
  "ipv6_group": "InsightConnect IPv6 Block List"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result_object|object|True|An object containing the results of the action|{'http_method': 'PUT', 'revision': 'ae0c665d9d5ad469c280efc424e00e29', 'revision_changed': True, 'old_revision': '94d82356a2bc4cb05963807103392ca3', 'mkey': 'Test Group', 'status': 'success', 'http_status': 200, 'vdom': 'root', 'path': 'firewall', 'name': 'addrgrp', 'serial': 'FGVM02TM20001791', 'version': 'v6.2.3', 'build': 1066}|
|success|boolean|True|Was the operation successful|True|
  
Example output:

```
{
  "result_object": {
    "build": 1066,
    "http_method": "PUT",
    "http_status": 200,
    "mkey": "Test Group",
    "name": "addrgrp",
    "old_revision": "94d82356a2bc4cb05963807103392ca3",
    "path": "firewall",
    "revision": "ae0c665d9d5ad469c280efc424e00e29",
    "revision_changed": true,
    "serial": "FGVM02TM20001791",
    "status": "success",
    "vdom": "root",
    "version": "v6.2.3"
  },
  "success": true
}
```

#### Check if Address in Group

This action is used to check if an IP address is in an address group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|The Address Object name to check. If Enable Search is set to true then we search the addresses (IP, CIDR, domain) within the address object instead of matching the name|None|198.51.100.100|None|None|
|enable_search|boolean|False|True|When enabled, the Address input will accept a IP, CIDR, or domain name to search across the available Address Objects in the system. This is useful when you don't know the Address Object by its name|None|False|None|None|
|group|string|None|True|Name of Address Group to check for address|None|InsightConnect Block Policy|None|None|
|ipv6_group|string|None|True|The name of the IPv6 address group|None|InsightConnect IPv6 Block List|None|None|
  
Example input:

```
{
  "address": "198.51.100.100",
  "enable_search": false,
  "group": "InsightConnect Block Policy",
  "ipv6_group": "InsightConnect IPv6 Block List"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|address_objects|[]string|True|The names of the address objects that match or contain the address|["198.51.100.100/32"]|
|found|boolean|True|Was address found in group|True|
  
Example output:

```
{
  "address_objects": [
    "198.51.100.100/32"
  ],
  "found": true
}
```

#### Create Address Object

This action is used to create an address object

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|The address to assign to the Address Object. This can be an IP address, CIDR IP address e.g. 198.51.100.0/24, or a domain name|None|198.51.100.100|None|None|
|address_object|string|None|False|Optional name to give this address object. If not provided, the name will be the value of address input field|None|MaliciousHost|None|None|
|skip_rfc1918|boolean|True|True|Skip private IP addresses as defined in RFC 1918|None|True|None|None|
|whitelist|[]string|None|False|This list contains a set of network object that should not be blocked. This can be an IP address, CIDR IP address e.g. 198.51.100.0/24, or a domain name|None|["198.51.100.100", "example.com", "192.0.2.0/24"]|None|None|
  
Example input:

```
{
  "address": "198.51.100.100",
  "address_object": "MaliciousHost",
  "skip_rfc1918": true,
  "whitelist": [
    "198.51.100.100",
    "example.com",
    "192.0.2.0/24"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response_object|object|True|Information about the operation that was performed|{'http_method': 'POST', 'revision': 'e089319342f23d5e31b70f5edfb5164c', 'revision_changed': True, 'old_revision': 'd04190fe309ea6ce1fbf4be1e5cd3233', 'mkey': '192.168.2.1', 'status': 'success', 'http_status': 200, 'vdom': 'root', 'path': 'firewall', 'name': 'address', 'serial': 'FGVM02TM20001791', 'version': 'v6.2.3', 'build': 1066}|
|success|boolean|True|Boolean value indicating the success of the operation|True|
  
Example output:

```
{
  "response_object": {
    "build": 1066,
    "http_method": "POST",
    "http_status": 200,
    "mkey": "192.168.2.1",
    "name": "address",
    "old_revision": "d04190fe309ea6ce1fbf4be1e5cd3233",
    "path": "firewall",
    "revision": "e089319342f23d5e31b70f5edfb5164c",
    "revision_changed": true,
    "serial": "FGVM02TM20001791",
    "status": "success",
    "vdom": "root",
    "version": "v6.2.3"
  },
  "success": true
}
```

#### Delete Address Object

This action is used to delete an address object

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address_object|string|None|True|Name of Address Object to delete|None|MaliciousHost|None|None|
  
Example input:

```
{
  "address_object": "MaliciousHost"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response_object|object|True|Information about the operation that was performed|{'http_method': 'DELETE', 'revision': '31a57b41b37574780e38a4be9a5cf117', 'revision_changed': True, 'old_revision': 'e089319342f23d5e31b70f5edfb5164c', 'mkey': '192.168.3.1/32', 'status': 'success', 'http_status': 200, 'vdom': 'root', 'path': 'firewall', 'name': 'address', 'serial': 'FGVM02TM20001791', 'version': 'v6.2.3', 'build': 1066}|
|success|boolean|True|Boolean value indicating the success of the operation|True|
  
Example output:

```
{
  "response_object": {
    "build": 1066,
    "http_method": "DELETE",
    "http_status": 200,
    "mkey": "192.168.3.1/32",
    "name": "address",
    "old_revision": "e089319342f23d5e31b70f5edfb5164c",
    "path": "firewall",
    "revision": "31a57b41b37574780e38a4be9a5cf117",
    "revision_changed": true,
    "serial": "FGVM02TM20001791",
    "status": "success",
    "vdom": "root",
    "version": "v6.2.3"
  },
  "success": true
}
```

#### Get Address Objects

This action is used to get address objects

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|fqdn_filter|string|None|False|Optional FQDN to filter on|None|example.com|None|None|
|ipv6_subnet_filter|string|None|False|Optional IPv6 subnet to filter on|None|2001:db8:8:4::2/128|None|None|
|name_filter|string|None|False|Optional name to filter on|None|MaliciousHost|None|None|
|subnet_filter|string|None|False|Optional subnet to filter on|None|198.51.100.100/32|None|None|
  
Example input:

```
{
  "fqdn_filter": "example.com",
  "ipv6_subnet_filter": "2001:db8:8:4::2/128",
  "name_filter": "MaliciousHost",
  "subnet_filter": "198.51.100.100/32"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|address_objects|[]address_object|True|A list of address objects|[ { "name": "FABRIC_DEVICE", "q_origin_key": "FABRIC_DEVICE", "uuid": "7773d538-25a0-51ea-fcb2-a2340d71f5d9", "subnet": "0.0.0.0 0.0.0.0", "type": "ipmask", "sub-type": "sdn", "clearpass-spt": "unknown", "start-mac": "00:00:00:00:00:00", "end-mac": "00:00:00:00:00:00", "cache-ttl": 0, "fsso-group": [], "comment": "IPv4 addresses of Fabric Devices.", "visibility": "enable", "color": 0, "sdn-addr-type": "private", "list": [], "tagging": [], "allow-routing": "disable" } ]|
|ipv6_address_objects|[]ipv6_address_object|True|A list of IPv6 address objects|[ { "name": "FABRIC_DEVICE", "q_origin_key": "FABRIC_DEVICE", "uuid": "7773d538-25a0-51ea-fcb2-a2340d71f5d9", "subnet": "0.0.0.0 0.0.0.0", "type": "ipmask", "sub-type": "sdn", "clearpass-spt": "unknown", "start-mac": "00:00:00:00:00:00", "end-mac": "00:00:00:00:00:00", "cache-ttl": 0, "fsso-group": [], "comment": "IPv4 addresses of Fabric Devices.", "visibility": "enable", "color": 0, "sdn-addr-type": "private", "list": [], "tagging": [], "allow-routing": "disable" } ]|
  
Example output:

```
{
  "address_objects": [
    {
      "allow-routing": "disable",
      "cache-ttl": 0,
      "clearpass-spt": "unknown",
      "color": 0,
      "comment": "IPv4 addresses of Fabric Devices.",
      "end-mac": "00:00:00:00:00:00",
      "fsso-group": [],
      "list": [],
      "name": "FABRIC_DEVICE",
      "q_origin_key": "FABRIC_DEVICE",
      "sdn-addr-type": "private",
      "start-mac": "00:00:00:00:00:00",
      "sub-type": "sdn",
      "subnet": "0.0.0.0 0.0.0.0",
      "tagging": [],
      "type": "ipmask",
      "uuid": "7773d538-25a0-51ea-fcb2-a2340d71f5d9",
      "visibility": "enable"
    }
  ],
  "ipv6_address_objects": [
    {
      "allow-routing": "disable",
      "cache-ttl": 0,
      "clearpass-spt": "unknown",
      "color": 0,
      "comment": "IPv4 addresses of Fabric Devices.",
      "end-mac": "00:00:00:00:00:00",
      "fsso-group": [],
      "list": [],
      "name": "FABRIC_DEVICE",
      "q_origin_key": "FABRIC_DEVICE",
      "sdn-addr-type": "private",
      "start-mac": "00:00:00:00:00:00",
      "sub-type": "sdn",
      "subnet": "0.0.0.0 0.0.0.0",
      "tagging": [],
      "type": "ipmask",
      "uuid": "7773d538-25a0-51ea-fcb2-a2340d71f5d9",
      "visibility": "enable"
    }
  ]
}
```

#### Get Policies

This action is used to get policies

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name_filter|string|None|False|Optional name to filter on|None|InsightConnect Block Policy|None|None|
  
Example input:

```
{
  "name_filter": "InsightConnect Block Policy"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|policies|[]policies|False|Policies|[{"policyid": 1, "q_origin_key": 1, "name": "Test Policy", "uuid": "6193559a-6862-51ea-44ce-e27594b8536a", "srcintf": [{"name": "port1", "q_origin_key": "port1"}], "dstintf": [{"name": "port1", "q_origin_key": "port1"}], "srcaddr": [{"name": "Test Group", "q_origin_key": "Test Group"}], "dstaddr": [{"name": "Test Group", "q_origin_key": "Test Group"}], "internet-service": "disable", "internet-service-id": [], "internet-service-group": [], "internet-service-custom": [], "internet-service-custom-group": [], "internet-service-src": "disable", "internet-service-src-id": [], "internet-service-src-group": [], "internet-service-src-custom": [], "internet-service-src-custom-group": [], "reputation-minimum": 0, "reputation-direction": "destination", "rtp-nat": "disable", "rtp-addr": [], "action": "accept", "send-deny-packet": "disable", "firewall-session-dirty": "check-all", "status": "enable", "schedule": "always", "schedule-timeout": "disable", "service": [{"name": "ALL", "q_origin_key": "ALL"}], "tos": "0x00", "tos-mask": "0x00", "tos-negate": "disable", "anti-replay": "enable", "tcp-session-without-syn": "disable", "geoip-anycast": "disable", "utm-status": "disable", "inspection-mode": "flow", "http-policy-redirect": "disable", "ssh-policy-redirect": "disable", "profile-type": "single", "profile-protocol-options": "default", "ssl-ssh-profile": "no-inspection", "logtraffic": "utm", "logtraffic-start": "disable", "capture-packet": "disable", "auto-asic-offload": "enable", "wanopt": "disable", "wanopt-detection": "active", "wanopt-passive-opt": "default", "webcache": "disable", "webcache-https": "disable", "application": [], "app-category": [], "url-category": [], "app-group": [], "nat": "enable", "permit-any-host": "disable", "permit-stun-host": "disable", "fixedport": "disable", "ippool": "disable", "poolname": [], "session-ttl": "0", "vlan-cos-fwd": 255, "vlan-cos-rev": 255, "inbound": "disable", "outbound": "enable", "natinbound": "disable", "natoutbound": "disable", "wccp": "disable", "ntlm": "disable", "ntlm-guest": "disable", "ntlm-enabled-browsers": [], "fsso": "enable", "wsso": "enable", "rsso": "disable", "groups": [], "users": [], "fsso-groups": [], "auth-path": "disable", "disclaimer": "disable", "email-collect": "disable", "natip": "0.0.0.0 0.0.0.0", "match-vip": "disable", "match-vip-only": "disable", "diffserv-forward": "disable", "diffserv-reverse": "disable", "diffservcode-forward": "000000", "diffservcode-rev": "000000", "tcp-mss-sender": 0, "tcp-mss-receiver": 0, "block-notification": "disable", "custom-log-fields": [], "srcaddr-negate": "disable", "dstaddr-negate": "disable", "service-negate": "disable", "internet-service-negate": "disable", "internet-service-src-negate": "disable", "timeout-send-rst": "disable", "captive-portal-exempt": "disable", "ssl-mirror": "disable", "ssl-mirror-intf": [], "dsri": "disable", "radius-mac-auth-bypass": "disable", "delay-tcp-npu-session": "disable"}]|
  
Example output:

```
{
  "policies": [
    {
      "action": "accept",
      "anti-replay": "enable",
      "app-category": [],
      "app-group": [],
      "application": [],
      "auth-path": "disable",
      "auto-asic-offload": "enable",
      "block-notification": "disable",
      "captive-portal-exempt": "disable",
      "capture-packet": "disable",
      "custom-log-fields": [],
      "delay-tcp-npu-session": "disable",
      "diffserv-forward": "disable",
      "diffserv-reverse": "disable",
      "diffservcode-forward": "000000",
      "diffservcode-rev": "000000",
      "disclaimer": "disable",
      "dsri": "disable",
      "dstaddr": [
        {
          "name": "Test Group",
          "q_origin_key": "Test Group"
        }
      ],
      "dstaddr-negate": "disable",
      "dstintf": [
        {
          "name": "port1",
          "q_origin_key": "port1"
        }
      ],
      "email-collect": "disable",
      "firewall-session-dirty": "check-all",
      "fixedport": "disable",
      "fsso": "enable",
      "fsso-groups": [],
      "geoip-anycast": "disable",
      "groups": [],
      "http-policy-redirect": "disable",
      "inbound": "disable",
      "inspection-mode": "flow",
      "internet-service": "disable",
      "internet-service-custom": [],
      "internet-service-custom-group": [],
      "internet-service-group": [],
      "internet-service-id": [],
      "internet-service-negate": "disable",
      "internet-service-src": "disable",
      "internet-service-src-custom": [],
      "internet-service-src-custom-group": [],
      "internet-service-src-group": [],
      "internet-service-src-id": [],
      "internet-service-src-negate": "disable",
      "ippool": "disable",
      "logtraffic": "utm",
      "logtraffic-start": "disable",
      "match-vip": "disable",
      "match-vip-only": "disable",
      "name": "Test Policy",
      "nat": "enable",
      "natinbound": "disable",
      "natip": "0.0.0.0 0.0.0.0",
      "natoutbound": "disable",
      "ntlm": "disable",
      "ntlm-enabled-browsers": [],
      "ntlm-guest": "disable",
      "outbound": "enable",
      "permit-any-host": "disable",
      "permit-stun-host": "disable",
      "policyid": 1,
      "poolname": [],
      "profile-protocol-options": "default",
      "profile-type": "single",
      "q_origin_key": 1,
      "radius-mac-auth-bypass": "disable",
      "reputation-direction": "destination",
      "reputation-minimum": 0,
      "rsso": "disable",
      "rtp-addr": [],
      "rtp-nat": "disable",
      "schedule": "always",
      "schedule-timeout": "disable",
      "send-deny-packet": "disable",
      "service": [
        {
          "name": "ALL",
          "q_origin_key": "ALL"
        }
      ],
      "service-negate": "disable",
      "session-ttl": "0",
      "srcaddr": [
        {
          "name": "Test Group",
          "q_origin_key": "Test Group"
        }
      ],
      "srcaddr-negate": "disable",
      "srcintf": [
        {
          "name": "port1",
          "q_origin_key": "port1"
        }
      ],
      "ssh-policy-redirect": "disable",
      "ssl-mirror": "disable",
      "ssl-mirror-intf": [],
      "ssl-ssh-profile": "no-inspection",
      "status": "enable",
      "tcp-mss-receiver": 0,
      "tcp-mss-sender": 0,
      "tcp-session-without-syn": "disable",
      "timeout-send-rst": "disable",
      "tos": "0x00",
      "tos-mask": "0x00",
      "tos-negate": "disable",
      "url-category": [],
      "users": [],
      "utm-status": "disable",
      "uuid": "6193559a-6862-51ea-44ce-e27594b8536a",
      "vlan-cos-fwd": 255,
      "vlan-cos-rev": 255,
      "wanopt": "disable",
      "wanopt-detection": "active",
      "wanopt-passive-opt": "default",
      "wccp": "disable",
      "webcache": "disable",
      "webcache-https": "disable",
      "wsso": "enable"
    }
  ]
}
```

#### Remove Address Object from Group

This action is used to removes an address object from an address group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address_object|string|None|True|Address object|None|MaliciousHost|None|None|
|group|string|None|True|Group name|None|InsightConnect Block List|None|None|
|ipv6_group|string|None|True|The name of the IPv6 address group|None|InsightConnect IPv6 Block List|None|None|
  
Example input:

```
{
  "address_object": "MaliciousHost",
  "group": "InsightConnect Block List",
  "ipv6_group": "InsightConnect IPv6 Block List"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result_object|object|True|An object containing the results of the action|{'http_method': 'PUT', 'revision': 'ae0c665d9d5ad469c280efc424e00e29', 'revision_changed': True, 'old_revision': '94d82356a2bc4cb05963807103392ca3', 'mkey': 'Test Group', 'status': 'success', 'http_status': 200, 'vdom': 'root', 'path': 'firewall', 'name': 'addrgrp', 'serial': 'FGVM02TM20001791', 'version': 'v6.2.3', 'build': 1066}|
|success|boolean|True|Was the operation successful|True|
  
Example output:

```
{
  "result_object": {
    "build": 1066,
    "http_method": "PUT",
    "http_status": 200,
    "mkey": "Test Group",
    "name": "addrgrp",
    "old_revision": "94d82356a2bc4cb05963807103392ca3",
    "path": "firewall",
    "revision": "ae0c665d9d5ad469c280efc424e00e29",
    "revision_changed": true,
    "serial": "FGVM02TM20001791",
    "status": "success",
    "vdom": "root",
    "version": "v6.2.3"
  },
  "success": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**dstaddr**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Name|None|
|Q Origin Key|string|None|False|Q origin key|None|
  
**policies**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action|string|None|False|Action|None|
|Anti-Replay|string|None|False|Anti-replay|None|
|App-Category|[]object|None|False|App-category|None|
|App-Group|[]object|None|False|App-group|None|
|Application|[]object|None|False|Application|None|
|Auth-Path|string|None|False|Auth-path|None|
|Auto-ASIC-Offload|string|None|False|Auto-ASIC-offload|None|
|Block-Notification|string|None|False|Block-notification|None|
|Captive-Portal-Exempt|string|None|False|Captive-portal-exempt|None|
|Capture-Packet|string|None|False|Capture-packet|None|
|Delay-TCP-Npu-Session|string|None|False|Delay-TCP-npu-session|None|
|Diffserv-Forward|string|None|False|Diffserv-forward|None|
|Diffserv-Reverse|string|None|False|Diffserv-reverse|None|
|Diffservcode-Forward|string|None|False|Diffservcode-forward|None|
|Diffservcode-Rev|string|None|False|Diffservcode-rev|None|
|Disclaimer|string|None|False|Disclaimer|None|
|DSRI|string|None|False|DSRI|None|
|Dstaddr|[]dstaddr|None|False|Dstaddr|None|
|Dstaddr-Negate|string|None|False|Dstaddr-negate|None|
|Dstintf|[]dstaddr|None|False|Dstintf|None|
|Email-Collect|string|None|False|Email-collect|None|
|Firewall-Session-Dirty|string|None|False|Firewall-session-dirty|None|
|Fixed Port|string|None|False|Fixed port|None|
|FSSO|string|None|False|FSSO|None|
|FSSO-Groups|[]object|None|False|FSSO-groups|None|
|Geoip-Anycast|string|None|False|Geoip-anycast|None|
|Groups|[]object|None|False|Groups|None|
|HTTP-Policy-Redirect|string|None|False|HTTP-policy-redirect|None|
|Inbound|string|None|False|Inbound|None|
|Inspection-Mode|string|None|False|Inspection-mode|None|
|Internet-Service|string|None|False|Internet-service|None|
|Internet-Service-Custom|[]object|None|False|Internet-service-custom|None|
|Internet-Service-Group|[]object|None|False|Internet-service-group|None|
|Internet-Service-Negate|string|None|False|Internet-service-negate|None|
|Internet-Service-Src|string|None|False|Internet-service-src|None|
|Internet-Service-Src-Group|[]object|None|False|Internet-service-src-group|None|
|Internet-Service-Src-Negate|string|None|False|Internet-service-src-negate|None|
|IP Pool|string|None|False|IP pool|None|
|Log Traffic|string|None|False|Log Traffic|None|
|Logtraffic-Start|string|None|False|Logtraffic-start|None|
|Match-VIP|string|None|False|Match-VIP|None|
|Match-VIP-Only|string|None|False|Match-VIP-only|None|
|Name|string|None|False|Name|None|
|NAT|string|None|False|NAT|None|
|NAT Inbound|string|None|False|NAT inbound|None|
|NAT IP|string|None|False|NAT IP|None|
|NAT Outbound|string|None|False|NAT outbound|None|
|NTLM|string|None|False|NTLM|None|
|NTLM-Enabled-Browsers|[]object|None|False|NTLM-enabled-browsers|None|
|NTLM-Guest|string|None|False|NTLM-guest|None|
|Outbound|string|None|False|Outbound|None|
|Permit-Any-Host|string|None|False|Permit-any-host|None|
|Permit-STUN-Host|string|None|False|Permit-STUN-host|None|
|Policy ID|integer|None|False|Policy ID|None|
|Profile-Protocol-Options|string|None|False|Profile-protocol-options|None|
|Profile-Type|string|None|False|Profile-type|None|
|Q Origin Key|integer|None|False|Q origin key|None|
|Radius-MAC-Auth-Bypass|string|None|False|Radius-MAC-auth-bypass|None|
|Reputation-Direction|string|None|False|Reputation-direction|None|
|Reputation-Minimum|integer|None|False|Reputation-minimum|None|
|RSSO|string|None|False|RSSO|None|
|Rtp-Addr|[]object|None|False|Rtp-addr|None|
|RTP-NAT|string|None|False|RTP-NAT|None|
|Schedule|string|None|False|Schedule|None|
|Schedule-Timeout|string|None|False|Schedule-timeout|None|
|Send-Deny-Packet|string|None|False|Send-deny-packet|None|
|Service|[]dstaddr|None|False|Service|None|
|Service-Negate|string|None|False|Service-negate|None|
|Session-TTL|string|None|False|Session-TTL|None|
|Srcaddr|[]dstaddr|None|False|Srcaddr|None|
|Srcaddr-Negate|string|None|False|Srcaddr-negate|None|
|Srcintf|[]dstaddr|None|False|Srcintf|None|
|SSH-Policy-Redirect|string|None|False|SSH-policy-redirect|None|
|SSL-Mirror|string|None|False|SSL-mirror|None|
|Ssl-Ssh-Profile|string|None|False|Ssl-ssh-profile|None|
|Status|string|None|False|Status|None|
|Tcp-Mss-Receiver|integer|None|False|Tcp-mss-receiver|None|
|TCP-Mss-Sender|integer|None|False|TCP-mss-sender|None|
|TCP-Session-Without-SYN|string|None|False|TCP-session-without-SYN|None|
|Timeout-Send-RST|string|None|False|Timeout-send-RST|None|
|TOS|string|None|False|TOS|None|
|TOS-Mask|string|None|False|TOS-mask|None|
|TOS-Negate|string|None|False|TOS-negate|None|
|URL-Category|[]object|None|False|URL-category|None|
|Users|[]object|None|False|Users|None|
|UTM-Status|string|None|False|UTM-status|None|
|UUID|string|None|False|UUID|None|
|Vlan-Cos-Fwd|integer|None|False|Vlan-cos-fwd|None|
|Vlan-Cos-Rev|integer|None|False|Vlan-cos-rev|None|
|WAN Option|string|None|False|WAN option|None|
|WAN opt-Detection|string|None|False|WAN opt-detection|None|
|WAN opt-Passive-Opt|string|None|False|WAN opt-passive-opt|None|
|WCCP|string|None|False|WCCP|None|
|Webcache|string|None|False|Webcache|None|
|Web cache-https|string|None|False|Web cache-https|None|
|WSSO|string|None|False|WSSO|None|
  
**address_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Allow-Routing|string|None|False|Allow-routing|None|
|Cache-TTL|integer|None|False|Cache-TTL|None|
|Clear Pass-Spt|string|None|False|Clear Pass-spt|None|
|Color|integer|None|False|Color|None|
|Comment|string|None|False|Comment|None|
|End-MAC|string|None|False|End-MAC|None|
|FQDN|string|None|False|FQDN|None|
|FSSO-Group|[]object|None|False|FSSO-group|None|
|List|[]object|None|False|List|None|
|Name|string|None|False|Name|None|
|Q Origin Key|string|None|False|Q origin key|None|
|Sdn-Addr-Type|string|None|False|Sdn-addr-type|None|
|Start-MAC|string|None|False|Start-MAC|None|
|Sub-Type|string|None|False|Sub-type|None|
|Subnet|string|None|False|Subnet|None|
|Tagging|[]object|None|False|Tagging|None|
|Type|string|None|False|Type|None|
|UUID|string|None|False|UUID|None|
|Visibility|string|None|False|Visibility|None|
  
**tags**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Name|None|
  
**tagging**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Category|string|None|False|Category|None|
|Name|string|None|False|Name|None|
|Tags|[]tags|None|False|Tags|None|
  
**list**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IP Address|string|None|False|IP address|None|
|Net-ID|string|None|False|Network ID|None|
|Obj-ID|string|None|False|Object ID|None|
  
**segments**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Name|None|
|Type|string|None|False|Type|None|
|Value|string|None|False|Value|None|
  
**ipv6_address_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Cache-TTL|integer|None|False|Cache-TTL|None|
|Color|integer|None|False|Color|None|
|Comment|string|None|False|Comment|None|
|End-IP|string|None|False|End IP|None|
|Host|string|None|False|Host|None|
|Host-type|string|None|False|Host type|None|
|IPv6 Address|string|None|False|IPv6 address|None|
|List|[]list|None|False|List|None|
|Name|string|None|False|Name|None|
|Obj-ID|string|None|False|Object ID for NSX|None|
|Q Origin Key|string|None|False|Q origin key|None|
|SDN|string|None|False|SDN|None|
|Start-IP|string|None|False|Start IP|None|
|Subnet-segment|[]segments|None|False|Subnet segment|None|
|Tagging|[]tagging|None|False|Tagging|None|
|Template|string|None|False|Template|None|
|Type|string|None|False|Type|None|
|UUID|string|None|False|UUID|None|
|Visibility|string|None|False|Visibility|None|


## Troubleshooting

* To accomplish this, log into the FortiGate firewall. Go to the System tab -> Administrator subtab and then select and edit the API admin.
Add the orchestrator's IP address to the trusted hosts in CIDR form e.g. `198.51.100.100/32`

# Version History

* 6.0.4 - Moved authorization from params to headers to enhance security | Bumped SDK to latest version (6.3.10)
* 6.0.3 - Fixed issue within connection test | Bumped SDK to latest version (6.3.8)
* 6.0.2 - Bumping requirements.txt | SDK bump to 6.2.0 | Fixing 'cidr' function in unit test
* 6.0.1 - Resolve connection test failure with Fortigate version 6.4.1 and above | Fix bug in action 'Check if Address in Group', where the action would fail if the IPV6 Group did not exist
* 6.0.0 - Fix the issue where creating address objects for domains does not work in the Create Address Object action | Fix the issue where address objects for IPv4 were created using the wrong endpoint in the Create Address Object action | Correct the payloads for creating address objects for domains and IPv6 in the Create Address Object action | Add support for checking if IPv6 is whitelisted in the Create Address Object action | Fix IPv6 support in all actions | Code refactor | Add default value for SSL verify parameter in connection configuration
* 5.1.1 - Add `docs_url` in plugin spec | Update `source_url` in plugin spec
* 5.1.0 - Support for IPV6 in all actions
* 5.0.0 - Improve input handling to allow IPs, CIDRs, and subnet masks in actions | Fix output of Get Address Objects action to return usable data | Update Get Address Objects action to allow for additional search parameters
* 4.0.4 - Improve error messaging around HTTP 401 status codes to indicate that the InsightConnect orchestrator IP address not being in the trusted host list may be the cause
* 4.0.3 - Improve assistance message when the API returns an Internal Server Error
* 4.0.2 - Support host URL in connection | Improve Create Address Object action to allow for IPs and CIDRs as input
* 4.0.1 - Bug fix where some names were being incorrectly parsed in the Check if Address in Group action causing the action to fail
* 4.0.0 - Update Create Address Object action to accept a RFC1918 whitelist | Add enable_search functionality to Check if Address in Group action
* 3.0.0 - Revise action input/output naming schemes | Add example inputs | New action Remove Address Object from Group
* 2.0.0 - Simplify the Create Address Object action to auto-detect the input type | Add whitelist safety check to Create Address Object action
* 1.1.0 - New Action Check if IP is in Address Group
* 1.0.0 - Initial plugin

# Links

* [Fortinet FortiGate](https://www.fortinet.com/)

## References

* [Fortinet FortiGate API](https://docs.fortinet.com/document/fortigate/7.6.0/administration-guide/940602/using-apis)