# Description

[FortiGate Next Generation Firewalls (NGFWs)](https://www.fortinet.com/) enable security-driven networking and consolidate industry-leading security capabilities such as intrusion prevention system (IPS), web filtering, secure sockets layer (SSL) inspection, and automated threat protection.

# Key Features

* Create network address objects
* Add address object to address groups

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
|address_objects|object[]|True|A list of address objects|

Example output:

```
```

#### 

This action is used to .

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|policies|object|False|Policies|

Example output:

```
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
