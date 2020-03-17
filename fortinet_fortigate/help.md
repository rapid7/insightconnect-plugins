# Description

[FortiGate Next Generation Firewalls (NGFWs)](https://www.fortinet.com/) enable security-driven networking and consolidate industry-leading security capabilities such as intrusion prevention system (IPS), web filtering, secure sockets layer (SSL) inspection, and automated threat protection.

# Key Features

* Create network address objects
* Add address object to address groups

The intended way to use this plugin is to have an existing policy in place with a predefined address group in it. 
As threats are detected, their address can be added to your existing policy through the address group. This allows
for flexible policy management of large groups of dynamic addresses. 

# Requirements

* A admin API key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|API key|None|
|hostname|string|None|True|Hostname or IP of your FortiGate server e.g. myfortigate.internal, 192.168.10.1, 192.168.10.1:8000|None|
|ssl_verify|boolean|None|True|SSL verify|None|

## Technical Details

### Actions

#### Add Address Object to Group

This action is used to add an address object to an address group.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address_object_name|string|None|True|Address object name|None|
|group_name|string|None|True|Group name|None|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cidr|integer|32|True|CIDR|None|
|ip|string|None|True|IP|None|
|name|string|None|False|Optional name to give this address object. If not provided, the name will be the IP address|None|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cidr|integer|32|True|CIDR|None|
|ip|string|None|True|IP|None|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|name_filter|string|None|False|Optional name to filer on|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address_objects|[]object|True|A list of address objects|

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

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Fortinet FortiGate](https://www.fortinet.com/)
