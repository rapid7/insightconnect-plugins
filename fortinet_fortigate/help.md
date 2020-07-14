# Description

[FortiGate Next Generation Firewalls (NGFWs)](https://www.fortinet.com/) enable security-driven networking and consolidate industry-leading security capabilities such as intrusion prevention system (IPS), web filtering, secure sockets layer (SSL) inspection, and automated threat protection.

# Key Features

* Create network address objects
* Add address object to address groups

The intended way to use this plugin is to have an existing policy in place with a predefined address group in it. 
As threats are detected, their address can be added to your existing policy through the address group. This allows
for flexible policy management of large groups of dynamic addresses. 

# Requirements

* An admin API key
* The IP of the orchestrator must be set as a trusted host in Settings > Administrator (Edit button) > Trusted Hosts 

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|API key|None|2Fty5834tFpBdidePJnt9075MMdkUb|
|hostname|string|None|True|Hostname or IP of your FortiGate server e.g. myfortigate.internal, 192.168.10.1, 192.168.10.1:8000|None|example.com|
|ssl_verify|boolean|None|True|SSL verify|None|False|

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

#### Remove Address Object from Group

This action removes an address object from an address group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address_object|string|None|True|Address object|None|MaliciousHost|
|group|string|None|True|Group name|None|InsightConnect Block List|

Example input:

```
{
  "address_object": "MaliciousHost",
  "group": "InsightConnect Block List"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result_object|object|True|An object containing the results of the action|
|success|boolean|True|Was the operation successful|

Example output:

```
{
  "success": true,
  "result_object": {
    "http_method": "PUT",
    "revision": "ae0c665d9d5ad469c280efc424e00e29",
    "revision_changed": true,
    "old_revision": "94d82356a2bc4cb05963807103392ca3",
    "mkey": "Test Group",
    "status": "success",
    "http_status": 200,
    "vdom": "root",
    "path": "firewall",
    "name": "addrgrp",
    "serial": "FGVM02TM20001791",
    "version": "v6.2.3",
    "build": 1066
  }
}
```

#### Check if Address in Group

This action is used to check if an IP address is in an address group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|The Address Object name to check. If Enable Search is set to true then we search the addresses (IP, CIDR, domain) within the address object instead of matching the name|None|198.51.100.100|
|enable_search|boolean|False|True|When enabled, the Address input will accept a IP, CIDR, or domain name to search across the available Address Objects in the system. This is useful when you don't know the Address Object by its name|None|False|
|group|string|None|True|Name of Address Group to check for address|None|InsightConnect Block Policy|

Example input:

```
{
  "address": "198.51.100.100",
  "enable_search": false,
  "group": "InsightConnect Block Policy"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address_objects|[]string|True|The names of the address objects that match or contain the address|
|found|boolean|True|Was address found in group|

Example output:

```
{
  "found": true,
  "address_objects": ["198.51.100.100/32"]
}
```

#### Get Policies

This action is used to get policies.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name_filter|string|None|False|Optional name to filter on|None|InsightConnect Block Policy|

Example input:

```
{
  "name_filter": "InsightConnect Block Policy"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|policies|[]policies|False|Policies|

Example output:

```
{
  "policies": [
    {
      "policyid": 1,
      "q_origin_key": 1,
      "name": "Test Policy",
      "uuid": "6193559a-6862-51ea-44ce-e27594b8536a",
      "srcintf": [
        {
          "name": "port1",
          "q_origin_key": "port1"
        }
      ],
      "dstintf": [
        {
          "name": "port1",
          "q_origin_key": "port1"
        }
      ],
      "srcaddr": [
        {
          "name": "Test Group",
          "q_origin_key": "Test Group"
        }
      ],
      "dstaddr": [
        {
          "name": "Test Group",
          "q_origin_key": "Test Group"
        }
      ],
      "internet-service": "disable",
      "internet-service-id": [],
      "internet-service-group": [],
      "internet-service-custom": [],
      "internet-service-custom-group": [],
      "internet-service-src": "disable",
      "internet-service-src-id": [],
      "internet-service-src-group": [],
      "internet-service-src-custom": [],
      "internet-service-src-custom-group": [],
      "reputation-minimum": 0,
      "reputation-direction": "destination",
      "rtp-nat": "disable",
      "rtp-addr": [],
      "action": "accept",
      "send-deny-packet": "disable",
      "firewall-session-dirty": "check-all",
      "status": "enable",
      "schedule": "always",
      "schedule-timeout": "disable",
      "service": [
        {
          "name": "ALL",
          "q_origin_key": "ALL"
        }
      ],
      "tos": "0x00",
      "tos-mask": "0x00",
      "tos-negate": "disable",
      "anti-replay": "enable",
      "tcp-session-without-syn": "disable",
      "geoip-anycast": "disable",
      "utm-status": "disable",
      "inspection-mode": "flow",
      "http-policy-redirect": "disable",
      "ssh-policy-redirect": "disable",
      "profile-type": "single",
      "profile-protocol-options": "default",
      "ssl-ssh-profile": "no-inspection",
      "logtraffic": "utm",
      "logtraffic-start": "disable",
      "capture-packet": "disable",
      "auto-asic-offload": "enable",
      "wanopt": "disable",
      "wanopt-detection": "active",
      "wanopt-passive-opt": "default",
      "webcache": "disable",
      "webcache-https": "disable",
      "application": [],
      "app-category": [],
      "url-category": [],
      "app-group": [],
      "nat": "enable",
      "permit-any-host": "disable",
      "permit-stun-host": "disable",
      "fixedport": "disable",
      "ippool": "disable",
      "poolname": [],
      "session-ttl": "0",
      "vlan-cos-fwd": 255,
      "vlan-cos-rev": 255,
      "inbound": "disable",
      "outbound": "enable",
      "natinbound": "disable",
      "natoutbound": "disable",
      "wccp": "disable",
      "ntlm": "disable",
      "ntlm-guest": "disable",
      "ntlm-enabled-browsers": [],
      "fsso": "enable",
      "wsso": "enable",
      "rsso": "disable",
      "groups": [],
      "users": [],
      "fsso-groups": [],
      "auth-path": "disable",
      "disclaimer": "disable",
      "email-collect": "disable",
      "natip": "0.0.0.0 0.0.0.0",
      "match-vip": "disable",
      "match-vip-only": "disable",
      "diffserv-forward": "disable",
      "diffserv-reverse": "disable",
      "diffservcode-forward": "000000",
      "diffservcode-rev": "000000",
      "tcp-mss-sender": 0,
      "tcp-mss-receiver": 0,
      "block-notification": "disable",
      "custom-log-fields": [],
      "srcaddr-negate": "disable",
      "dstaddr-negate": "disable",
      "service-negate": "disable",
      "internet-service-negate": "disable",
      "internet-service-src-negate": "disable",
      "timeout-send-rst": "disable",
      "captive-portal-exempt": "disable",
      "ssl-mirror": "disable",
      "ssl-mirror-intf": [],
      "dsri": "disable",
      "radius-mac-auth-bypass": "disable",
      "delay-tcp-npu-session": "disable"
    }
  ]
}
```

#### Add Address Object to Group

This action is used to add an address object to an address group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address_object|string|None|True|Address object|None|MaliciousHost|
|group|string|None|True|Group name|None|InsightConnect Block List|

Example input:

```
{
  "address_object": "MaliciousHost",
  "group": "InsightConnect Block List"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result_object|object|True|An object containing the results of the action|
|success|boolean|True|Was the operation successful|

Example output:

```
{
  "success": true,
  "result_object": {
    "http_method": "PUT",
    "revision": "ae0c665d9d5ad469c280efc424e00e29",
    "revision_changed": true,
    "old_revision": "94d82356a2bc4cb05963807103392ca3",
    "mkey": "Test Group",
    "status": "success",
    "http_status": 200,
    "vdom": "root",
    "path": "firewall",
    "name": "addrgrp",
    "serial": "FGVM02TM20001791",
    "version": "v6.2.3",
    "build": 1066
  }
}
```

#### Create Address Object

This action is used to create an address object.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|The address to assign to the Address Object. This can be an IP address, CIDR IP address e.g. 198.51.100.0/24, or a domain name|None|198.51.100.100|
|address_object|string|None|False|Optional name to give this address object. If not provided, the name will be the value of address input field|None|MaliciousHost|
|skip_rfc1918|boolean|True|True|Skip private IP addresses as defined in RFC 1918|None|True|
|whitelist|[]string|None|False|This list contains a set of network object that should not be blocked. This can be an IP address, CIDR IP address e.g. 198.51.100.0/24, or a domain name|None|["198.51.100.100", "example.com", "192.0.2.0/24"]|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_object|object|True|Information about the operation that was performed|
|success|boolean|True|Boolean value indicating the success of the operation|

Example output:

```
{
  "success": true,
  "response_object": {
    "http_method": "POST",
    "revision": "e089319342f23d5e31b70f5edfb5164c",
    "revision_changed": true,
    "old_revision": "d04190fe309ea6ce1fbf4be1e5cd3233",
    "mkey": "192.168.2.1",
    "status": "success",
    "http_status": 200,
    "vdom": "root",
    "path": "firewall",
    "name": "address",
    "serial": "FGVM02TM20001791",
    "version": "v6.2.3",
    "build": 1066
  }
}
```

#### Delete Address Object

This action is used to delete an address object.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address_object|string|None|True|Name of Address Object to delete|None|MaliciousHost|

Example input:

```
{
  "address_object": "MaliciousHost"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_object|object|True|Information about the operation that was performed|
|success|boolean|True|Boolean value indicating the success of the operation|

Example output:

```
{
  "success": true,
  "response_object": {
    "http_method": "DELETE",
    "revision": "31a57b41b37574780e38a4be9a5cf117",
    "revision_changed": true,
    "old_revision": "e089319342f23d5e31b70f5edfb5164c",
    "mkey": "192.168.3.1/32",
    "status": "success",
    "http_status": 200,
    "vdom": "root",
    "path": "firewall",
    "name": "address",
    "serial": "FGVM02TM20001791",
    "version": "v6.2.3",
    "build": 1066
  }
}
```

#### Get Address Objects

This action is used to get address objects.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|fqdn_filter|string|None|False|Optional FQDN to filter on|None|example.com|
|name_filter|string|None|False|Optional name to filter on|None|MaliciousHost|
|subnet_filter|string|None|False|Optional subnet to filter on|None|198.51.100.100/32|

Example input:

```
{
  "fqdn_filter": "example.com",
  "name_filter": "MaliciousHost",
  "subnet_filter": "198.51.100.100/32"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address_objects|[]address_object|True|A list of address objects|

Example output:

```
{
  "address_objects": [
    {
      "name": "FABRIC_DEVICE",
      "q_origin_key": "FABRIC_DEVICE",
      "uuid": "7773d538-25a0-51ea-fcb2-a2340d71f5d9",
      "subnet": "0.0.0.0 0.0.0.0",
      "type": "ipmask",
      "sub-type": "sdn",
      "clearpass-spt": "unknown",
      "start-mac": "00:00:00:00:00:00",
      "end-mac": "00:00:00:00:00:00",
      "cache-ttl": 0,
      "fsso-group": [],
      "comment": "IPv4 addresses of Fabric Devices.",
      "visibility": "enable",
      "color": 0,
      "sdn-addr-type": "private",
      "list": [],
      "tagging": [],
      "allow-routing": "disable"
    }
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### address_objects

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Allow-Routing|string|False|Allow-routing|
|Cache-TTL|integer|False|Cache-TTL|
|Clear Pass-Spt|string|False|Clear Pass-spt|
|Color|integer|False|Color|
|Comment|string|False|Comment|
|End-MAC|string|False|End-MAC|
|FSSO-Group|[]object|False|FSSO-group|
|List|[]object|False|List|
|Name|string|False|Name|
|Q Origin Key|string|False|Q origin key|
|Sdn-Addr-Type|string|False|Sdn-addr-type|
|Start-MAC|string|False|Start-MAC|
|Sub-Type|string|False|Sub-type|
|Subnet|string|False|Subnet|
|Tagging|[]object|False|Tagging|
|Type|string|False|Type|
|UUID|string|False|UUID|
|Visibility|string|False|Visibility|

#### dstaddr

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Name|string|False|Name|
|Q Origin Key|string|False|Q origin key|

#### policies

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Action|string|False|Action|
|Anti-Replay|string|False|Anti-replay|
|App-Category|[]object|False|App-category|
|App-Group|[]object|False|App-group|
|Application|[]object|False|Application|
|Auth-Path|string|False|Auth-path|
|Auto-ASIC-Offload|string|False|Auto-ASIC-offload|
|Block-Notification|string|False|Block-notification|
|Captive-Portal-Exempt|string|False|Captive-portal-exempt|
|Capture-Packet|string|False|Capture-packet|
|Delay-TCP-Npu-Session|string|False|Delay-TCP-npu-session|
|Diffserv-Forward|string|False|Diffserv-forward|
|Diffserv-Reverse|string|False|Diffserv-reverse|
|Diffservcode-Forward|string|False|Diffservcode-forward|
|Diffservcode-Rev|string|False|Diffservcode-rev|
|Disclaimer|string|False|Disclaimer|
|DSRI|string|False|DSRI|
|Dstaddr|[]dstaddr|False|Dstaddr|
|Dstaddr-Negate|string|False|Dstaddr-negate|
|Dstintf|[]dstaddr|False|Dstintf|
|Email-Collect|string|False|Email-collect|
|Firewall-Session-Dirty|string|False|Firewall-session-dirty|
|Fixed Port|string|False|Fixed port|
|FSSO|string|False|FSSO|
|FSSO-Groups|[]object|False|FSSO-groups|
|Geoip-Anycast|string|False|Geoip-anycast|
|Groups|[]object|False|Groups|
|HTTP-Policy-Redirect|string|False|HTTP-policy-redirect|
|Inbound|string|False|Inbound|
|Inspection-Mode|string|False|Inspection-mode|
|Internet-Service|string|False|Internet-service|
|Internet-Service-Custom|[]object|False|Internet-service-custom|
|Internet-Service-Group|[]object|False|Internet-service-group|
|Internet-Service-Negate|string|False|Internet-service-negate|
|Internet-Service-Src|string|False|Internet-service-src|
|Internet-Service-Src-Group|[]object|False|Internet-service-src-group|
|Internet-Service-Src-Negate|string|False|Internet-service-src-negate|
|IP Pool|string|False|IP pool|
|Log Traffic|string|False|Log Traffic|
|Logtraffic-Start|string|False|Logtraffic-start|
|Match-VIP|string|False|Match-VIP|
|Match-VIP-Only|string|False|Match-VIP-only|
|Name|string|False|Name|
|NAT|string|False|NAT|
|NAT Inbound|string|False|NAT inbound|
|NAT IP|string|False|NAT IP|
|NAT Outbound|string|False|NAT outbound|
|NTLM|string|False|NTLM|
|NTLM-Enabled-Browsers|[]object|False|NTLM-enabled-browsers|
|NTLM-Guest|string|False|NTLM-guest|
|Outbound|string|False|Outbound|
|Permit-Any-Host|string|False|Permit-any-host|
|Permit-Stun-Host|string|False|Permit-stun-host|
|Policy ID|integer|False|Policy ID|
|Profile-Protocol-Options|string|False|Profile-protocol-options|
|Profile-Type|string|False|Profile-type|
|Q Origin Key|integer|False|Q origin key|
|Radius-MAC-Auth-Bypass|string|False|Radius-MAC-auth-bypass|
|Reputation-Direction|string|False|Reputation-direction|
|Reputation-Minimum|integer|False|Reputation-minimum|
|RSSO|string|False|RSSO|
|Rtp-Addr|[]object|False|Rtp-addr|
|RTP-NAT|string|False|RTP-NAT|
|Schedule|string|False|Schedule|
|Schedule-Timeout|string|False|Schedule-timeout|
|Send-Deny-Packet|string|False|Send-deny-packet|
|Service|[]dstaddr|False|Service|
|Service-Negate|string|False|Service-negate|
|Session-TTL|string|False|Session-TTL|
|Srcaddr|[]dstaddr|False|Srcaddr|
|Srcaddr-Negate|string|False|Srcaddr-negate|
|Srcintf|[]dstaddr|False|Srcintf|
|SSH-Policy-Redirect|string|False|SSH-policy-redirect|
|SSL-Mirror|string|False|SSL-mirror|
|Ssl-Ssh-Profile|string|False|Ssl-ssh-profile|
|Status|string|False|Status|
|Tcp-Mss-Receiver|integer|False|Tcp-mss-receiver|
|TCP-Mss-Sender|integer|False|TCP-mss-sender|
|TCP-Session-Without-SYN|string|False|TCP-session-without-SYN|
|Timeout-Send-RST|string|False|Timeout-send-RST|
|TOS|string|False|TOS|
|TOS-Mask|string|False|TOS-mask|
|TOS-Negate|string|False|TOS-negate|
|URL-Category|[]object|False|URL-category|
|Users|[]object|False|Users|
|UTM-Status|string|False|UTM-status|
|UUID|string|False|UUID|
|Vlan-Cos-Fwd|integer|False|Vlan-cos-fwd|
|Vlan-Cos-Rev|integer|False|Vlan-cos-rev|
|WAN Option|string|False|WAN option|
|WAN opt-Detection|string|False|WAN opt-detection|
|WAN opt-Passive-Opt|string|False|WAN opt-passive-opt|
|WCCP|string|False|WCCP|
|Webcache|string|False|Webcache|
|Web cache-https|string|False|Web cache-https|
|WSSO|string|False|WSSO|

## Troubleshooting

To accomplish this, log into the FortiGate firewall. Go to the System tab -> Administrator subtab and then select and edit the API admin.
Add the orchestrator's IP address to the trusted hosts in CIDR form e.g. `198.51.100.100/32`

# Version History

* 5.0.0 - Improve input handling to allow IPs, CIDRs, and subnet masks in actions | Fix output of Get Address Objects action to return usable data | Update Get Address Objects action to allow for additional search parameters
* 4.0.4 - Improve error messaging around HTTP 401 status codes to indicate that the InsightConnect orchestrator IP address not being in the trusted host list may be the cause
* 4.0.3 - Improve assistance message when the API returns an Internal Server Errror
* 4.0.2 - Support host URL in connection | Improve Create Address Object action to allow for IPs and CIDRs as input
* 4.0.1 - Bug fix where some names were being incorrectly parsed in the Check if Address in Group action causing the action to fail
* 4.0.0 - Update Create Address Object action to accept a RFC1918 whitelist | Add enable_search functionality to Check if Address in Group action
* 3.0.0 - Revise action input/output naming schemes | Add example inputs | New action Remove Address Object from Group
* 2.0.0 - Simplify the Create Address Object action to auto-detect the input type | Add whitelist safety check to Create Address Object action
* 1.1.0 - New Action Check if IP is in Address Group
* 1.0.0 - Initial plugin

# Links

## References

* [Fortinet FortiGate](https://www.fortinet.com/)
