# Description

[Cisco Firepower Management Center](https://www.cisco.com/c/en/us/products/security/firepower-management-center/index.html) is your administrative nerve center for managing critical Cisco network security solutions.
The Cisco Firepower Management Center InsightConnect plugin allows you to block URLs and hosts. Firewall best practices for blocking and unblocking hosts is to add and remove address objects from a group attached to an existing firewall policy such as a deny-all rule.
In this example, adding an address object to a group attached to a deny-all rule will block the host, and removing the address object from the same group would unblock the host. Automating firewall blocking can be accomplished using the address object management actions in this plugin.

# Key Features

* Create block URL policy
* Address object management to block and unblock hosts, and check if a host is already blocked

# Requirements

* Cisco Firepower Management Center server name
* Cisco Firepower Management Center username and password

# Supported Product Versions

* 6.6.0

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|certificate|bytes|None|True|Base64-encoded certificate to authenticate with the host input API|None|VGhpcyBpcyBhIHNhbXBsZSBiYXNlNjQtZW5jb2RlZCBjZXJ0aWZpY2F0ZSB0byBhdXRoZW50aWNhdGUgd2l0aCB0aGUgaG9zdCBpbnB1dCBBUEku|
|certificate_passphrase|credential_secret_key|None|True|The passphrase to access the certificate|None|passphrase|
|domain|string|Global|False|Cisco FirePower Management Center Domain|None|Global|
|host_input_port|integer|8307|False|The port number for the provided host used in the Host Input API calls|None|8307|
|port|integer|443|False|The port number for provided host|None|443|
|server|string|None|False|Enter the address for the server|None|www.example.com|
|ssl_verify|boolean|True|False|Validate TLS / SSL certificate|None|True|
|username_and_password|credential_username_password|None|True|Cisco username and password|None|{"username":"user1", "password":"mypassword"}|

Example input:

```
{
  "certificate": "VGhpcyBpcyBhIHNhbXBsZSBiYXNlNjQtZW5jb2RlZCBjZXJ0aWZpY2F0ZSB0byBhdXRoZW50aWNhdGUgd2l0aCB0aGUgaG9zdCBpbnB1dCBBUEku",
  "certificate_passphrase": "passphrase",
  "domain": "Global",
  "host_input_port": 8307,
  "port": 443,
  "server": "www.example.com",
  "ssl_verify": true,
  "username_and_password": {
    "username": "user1",
    "password": "mypassword"
  }
}
```

## Technical Details

### Actions

#### Bulk Add Scan Result

This action is used to add scan results from a third-party vulnerability scanner.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|operation|string|None|True|The operation to be performed when adding scan results. ScanFlush to remove existing scan results or ScanUpdate to keep existing scan results|['ScanUpdate', 'ScanFlush']|ScanUpdate|
|scan_results|[]scan_result|None|False|Host scan results to be added|None|[{"host": {"ip_address": "0.0.0.164", "operating_system": {"name": "Ubuntu", "vendor": "Canonical", "version": "16.04"}}, "scan_result_details": {"description": "Example description", "protocol_id": "6", "scanner_id": "ProductZImport", "source_id": "ProductZ", "vulnerability_id": "943387", "vulnerability_title": "Virus Wire 0"}}]|

Example input:

```
{
  "operation": "ScanUpdate",
  "scan_results": [
    {
      "host": {
        "ip_address": "0.0.0.164",
        "operating_system": {
          "name": "Ubuntu",
          "vendor": "Canonical",
          "version": "16.04"
        }
      },
      "scan_result_details": {
        "description": "Example description",
        "protocol_id": "6",
        "scanner_id": "ProductZImport",
        "source_id": "ProductZ",
        "vulnerability_id": "943387",
        "vulnerability_title": "Virus Wire 0"
      }
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|commands_processed|number|True|Number of commands processed|
|errors|number|True|Number of errors|

Example output:

```
{
  "commands_processed": 4,
  "errors": 0
}
```

#### Add Scan Result

This action is used to add a scan result from a third-party vulnerability scanner.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|operation|string|None|True|The operation to be performed when adding scan results. ScanFlush to remove existing scan results or ScanUpdate to keep existing scan results|['ScanUpdate', 'ScanFlush']|ScanUpdate|
|scan_result|scan_result|None|False|The host scan result to be added|None|{"host": {"ip_address": "0.0.0.164", "operating_system": {"name": "Ubuntu", "vendor": "Canonical", "version": "16.04"}}, "scan_result_details": {"description": "Example description", "protocol_id": "6", "scanner_id": "ProductZImport", "source_id": "ProductZ", "vulnerability_id": "943387", "vulnerability_title": "Virus Wire 0"}}|

Example input:

```
{
  "operation": "ScanUpdate",
  "scan_result": {
    "host": {
      "ip_address": "0.0.0.164",
      "operating_system": {
        "name": "Ubuntu",
        "vendor": "Canonical",
        "version": "16.04"
      }
    },
    "scan_result_details": {
      "description": "Example description",
      "protocol_id": "6",
      "scanner_id": "ProductZImport",
      "source_id": "ProductZ",
      "vulnerability_id": "943387",
      "vulnerability_title": "Virus Wire 0"
    }
  }
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|commands_processed|number|True|Number of commands processed|
|errors|number|True|Number of errors|

Example output:

```
{
  "commands_processed": 4,
  "errors": 0
}
```

#### Check if Address in Group

This action checks if the provided Address Object name or host exists in an Address Group. If you don't know the Address Object by name, set Enable Search to true to allow a network indicator search in the Group. This is useful when working directly with IPs and domains.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|Address Object name, or IP, CIDR, or domain name when Enable Search is on|None|MaliciousHost|
|enable_search|boolean|False|False|When enabled, the Address input will accept an IP, CIDR, or domain name to search across the available Address Objects in the system. This is useful when you don't know the Address Object by its name|None|False|
|group|string|None|True|Name of address group to check|None|MaliciousAddressGroup|

Example input:

```
{
  "address": "MaliciousHost",
  "enable_search": false,
  "group": "MaliciousAddressGroup"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address_objects|[]address_object|False|List of found address objects|
|found|boolean|True|Was address found in group|

Example output:

```
{
  "address_objects": [
    {
      "description": " ",
      "dnsResolution": "IPV4_AND_IPV6",
      "id": "00000000-0000-0ed3-0000-021474836483",
      "links": {
        "parent": "https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networkaddresses",
        "self": "https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/fqdns/00000000-0000-0ed3-0000-021474836483"
      },
      "metadata": {
        "domain": {
          "id": "e276abec-e0f2-11e3-8169-6d9ed49b625f",
          "name": "Global",
          "type": "Domain"
        },
        "lastUser": {
          "name": "admin"
        },
        "parentType": "NetworkAddress",
        "timestamp": 1600277332623
      },
      "name": "TestAddressObjectFQDN1",
      "overridable": false,
      "type": "FQDN",
      "value": "example.com"
    }
  ],
  "found": true
}
```

#### Remove Address from Group

This action removes an address object from a group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|The address object name, hostname, an IP address or subnet address expressed in CIDR notation to remove from group|None|MaliciousHost|
|group|string|None|True|Name of the group to remove the address from|None|MaliciousAddressGroup|

Example input:

```
{
  "address": "MaliciousHost",
  "group": "MaliciousAddressGroup"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|network_group|network_group|False|Returns information about the network group|

Example output:

```
{
  "network_group": {
    "links": {
      "self": "https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networkgroups/00000000-0000-0ed3-0000-021474836521"
    },
    "objects": [
      {
        "type": "Host",
        "id": "00000000-0000-0ed3-0000-021474836502",
        "name": "TestAddressObjectHost1"
      },
      {
        "type": "FQDN",
        "id": "00000000-0000-0ed3-0000-021474836483",
        "name": "TestAddressObjectFQDN1"
      },
      {
        "type": "Network",
        "id": "00000000-0000-0ed3-0000-021474836598",
        "name": "TestAddressObjectNetwork"
      }
    ],
    "type": "NetworkGroup",
    "overridable": false,
    "id": "00000000-0000-0ed3-0000-021474836521",
    "name": "TestAddressObjectGroup",
    "metadata": {
      "timestamp": 0,
      "lastUser": {
        "name": "admin"
      },
      "domain": {
        "name": "Global",
        "id": "e276abec-e0f2-11e3-8169-6d9ed49b625f",
        "type": "Domain"
      }
    }
  }
}
```

#### Add Address to Group

This action adds an existing address object to a group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|Name of address object|None|MaliciousHost|
|group|string|None|True|Name of address group to add the address to|None|MaliciousAddressGroup|

Example input:

```
{
  "address": "MaliciousHost",
  "group": "MaliciousAddressGroup"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|network_group|network_group|False|Returns information about the network group|

Example output:

```
{
  "network_group": {
    "links": {
      "self": "https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networkgroups/00000000-0000-0ed3-0000-021474836521"
    },
    "objects": [
      {
        "type": "Host",
        "id": "00000000-0000-0ed3-0000-021474836502",
        "name": "TestAddressObjectHost1"
      },
      {
        "type": "FQDN",
        "id": "00000000-0000-0ed3-0000-021474836483",
        "name": "TestAddressObjectFQDN1"
      },
      {
        "type": "Network",
        "id": "00000000-0000-0ed3-0000-021474836598",
        "name": "TestAddressObjectNetwork"
      }
    ],
    "type": "NetworkGroup",
    "overridable": false,
    "id": "00000000-0000-0ed3-0000-021474836521",
    "name": "TestAddressObjectGroup",
    "metadata": {
      "timestamp": 0,
      "lastUser": {
        "name": "admin"
      },
      "domain": {
        "name": "Global",
        "id": "e276abec-e0f2-11e3-8169-6d9ed49b625f",
        "type": "Domain"
      }
    }
  }
}
```

#### Delete Address Object

This action deletes an address object.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address_object|string|None|True|Name of the address object to delete|None|MaliciousHost|

Example input:

```
{
  "address_object": "MaliciousHost"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address_object|address_object|False|Returns information about the deleted address object|

Example output:

```
{
  "address_object": {
    "dnsResolution": "IPV4_AND_IPV6",
    "id": "00000000-0000-0ed3-0000-012884905524",
    "links": {
      "parent": "https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networkaddresses",
      "self": "https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/fqdns/00000000-0000-0ed3-0000-012884905524"
    },
    "metadata": {
      "domain": {
        "id": "e276abec-e0f2-11e3-8169-6d9ed49b625f",
        "name": "Global",
        "type": "Domain"
      },
      "lastUser": {
        "name": "admin"
      },
      "parentType": "NetworkAddress",
      "timestamp": 0
    },
    "name": "Example Object Created from InsightConnect",
    "overridable": false,
    "type": "FQDN",
    "value": "example.com"
  }
}
```

#### Create Address Object

This action creates a new address object.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|IP address, CIDR IP address, or domain name to assign to the Address Object|None|example.com|
|address_object|string|None|False|Name of the address object, defaults to the value address in the address field if no name is given|None|MaliciousHost|
|skip_private_address|boolean|None|True|If set to true, any addresses that are defined in the RFC1918 space will not be blocked. e.g. 10/8, 172.16/12, 192.168/16|None|True|
|whitelist|[]string|None|False|This list contains a set of hosts that should not be blocked. This can include IP addresses, CIDR IP addresses, and domains|None|["198.51.100.100", "192.0.2.0/24", "example.com"]|

Example input:

```
{
  "address": "example.com",
  "address_object": "MaliciousHost",
  "skip_private_address": true,
  "whitelist": [
    "198.51.100.100",
    "192.0.2.0/24",
    "example.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address_object|address_object|False|Returns information about the newly created address object|

Example output:

```
{
  "address_object": {
    "dnsResolution": "IPV4_AND_IPV6",
    "id": "00000000-0000-0ed3-0000-012884905524",
    "links": {
      "parent": "https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networkaddresses",
      "self": "https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/fqdns/00000000-0000-0ed3-0000-012884905524"
    },
    "metadata": {
      "domain": {
        "id": "e276abec-e0f2-11e3-8169-6d9ed49b625f",
        "name": "Global",
        "type": "Domain"
      },
      "lastUser": {
        "name": "admin"
      },
      "parentType": "NetworkAddress",
      "timestamp": 0
    },
    "name": "Example Object Created from InsightConnect",
    "overridable": false,
    "type": "FQDN",
    "value": "example.com"
  }
}
```

#### Block URL Policy

This action is used to create a new block URL policy.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|access_policy|string|None|True|Name for the access policy to be created|None|Example Access Policy|
|rule_name|string|None|True|Name for the access rule to be created|None|Example Access Rule|
|url_objects|[]url_object|None|True|URL objects to block|None|[{'name': 'example_url', 'url': 'https://example.com'}]|

Example input:

```
{
  "access_policy": "Example Access Policy",
  "rule_name": "Example Access Rule",
  "url_objects": [
    {
      'name': 'example_url',
      'url': 'https://example.com'
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Success|

Example output:

```
{
    "success": True
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.0 - Combine Cisco Firepower and Cisco Firepower Management Center plugins
* 1.2.0 - New actions - Check If Address in Group, Add Address to Group, Remove Address from Group
* 1.1.0 - New actions - Create Address Object, Delete Address Object
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

## References

* [Cisco Firepower Management Center](https://www.cisco.com/c/en/us/products/security/firepower-management-center/index.html)
