# Description

[Cisco Firepower Management Center](https://www.cisco.com/c/en/us/products/security/firepower-management-center/index.html) centralizes management of Cisco security solutions. The InsightConnect plugin can block URLs/hosts by adding address objects to a group tied to an existing deny-all rule; removing the object from that group unblocks. This plugin automates blocking via address object management actions

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

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|certificate|bytes|None|True|Base64-encoded certificate in PKCS12 format to authenticate with the host input API|None|VGhpcyBpcyBhIHNhbXBsZSBiYXNlNjQtZW5jb2RlZCBjZXJ0aWZpY2F0ZSB0byBhdXRoZW50aWNhdGUgd2l0aCB0aGUgaG9zdCBpbnB1dCBBUEku|None|None|
|certificate_passphrase|credential_secret_key|None|True|The passphrase to access the certificate|None|passphrase|None|None|
|domain|string|Global|False|Cisco FirePower Management Center Domain|None|Global|None|None|
|host_input_port|integer|8307|False|The port number for the provided host used in the Host Input API calls|None|8307|None|None|
|port|integer|443|False|The port number for provided host|None|443|None|None|
|server|string|None|False|Enter the address for the server|None|www.example.com|None|None|
|ssl_verify|boolean|True|False|Validate TLS / SSL certificate|None|True|None|None|
|username_and_password|credential_username_password|None|True|Cisco username and password|None|{"username":"user1", "password":"mypassword"}|None|None|

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
    "password": "mypassword",
    "username": "user1"
  }
}
```

## Technical Details

### Actions


#### Add Address to Group

This action is used to adds an existing address object to a group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|Name of address object|None|MaliciousHost|None|None|
|group|string|None|True|Name of address group to add the address to|None|MaliciousAddressGroup|None|None|
  
Example input:

```
{
  "address": "MaliciousHost",
  "group": "MaliciousAddressGroup"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|network_group|network_group|False|Returns information about the network group|{"links":{"self":"https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networkgroups/00000000-0000-0ed3-0000-021474836521"},"objects":[{"type":"Host","id":"00000000-0000-0ed3-0000-021474836502","name":"TestAddressObjectHost1"},{"type":"FQDN","id":"00000000-0000-0ed3-0000-021474836483","name":"TestAddressObjectFQDN1"},{"type":"Network","id":"00000000-0000-0ed3-0000-021474836598","name":"TestAddressObjectNetwork"}],"type":"NetworkGroup","overridable":false,"id":"00000000-0000-0ed3-0000-021474836521","name":"TestAddressObjectGroup","metadata":{"timestamp":0,"lastUser":{"name":"admin"},"domain":{"name":"Global","id":"e276abec-e0f2-11e3-8169-6d9ed49b625f","type":"Domain"}}}|
  
Example output:

```
{
  "network_group": {
    "id": "00000000-0000-0ed3-0000-021474836521",
    "links": {
      "self": "https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networkgroups/00000000-0000-0ed3-0000-021474836521"
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
      "timestamp": 0
    },
    "name": "TestAddressObjectGroup",
    "objects": [
      {
        "id": "00000000-0000-0ed3-0000-021474836502",
        "name": "TestAddressObjectHost1",
        "type": "Host"
      },
      {
        "id": "00000000-0000-0ed3-0000-021474836483",
        "name": "TestAddressObjectFQDN1",
        "type": "FQDN"
      },
      {
        "id": "00000000-0000-0ed3-0000-021474836598",
        "name": "TestAddressObjectNetwork",
        "type": "Network"
      }
    ],
    "overridable": false,
    "type": "NetworkGroup"
  }
}
```

#### Add Scan Result

This action is used to add a scan result from a third-party vulnerability scanner

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|operation|string|None|True|The operation to be performed when adding scan results. ScanFlush to remove existing scan results or ScanUpdate to keep existing scan results|["ScanUpdate", "ScanFlush"]|ScanUpdate|None|None|
|scan_result|scan_result|None|False|The host scan result to be added|None|{"host": {"ip_address": "0.0.0.164", "operating_system": {"name": "Ubuntu", "vendor": "Canonical", "version": "16.04"}}, "scan_result_details": {"description": "Example description", "protocol_id": "6", "scanner_id": "ProductZImport", "source_id": "ProductZ", "vulnerability_id": "943387", "vulnerability_title": "Virus Wire 0"}}|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|commands_processed|number|True|Number of commands processed|4|
|errors|number|True|Number of errors|0|
  
Example output:

```
{
  "commands_processed": 4,
  "errors": 0
}
```

#### Block URL Policy

This action is used to create a new block URL policy

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|access_policy|string|None|True|Name for the access policy to be created|None|Example Access Policy|None|None|
|rule_name|string|None|True|Name for the access rule to be created|None|Example Access Rule|None|None|
|url_objects|[]url_object|None|True|URL objects to block|None|[{'name': 'example_url', 'url': 'https://example.com'}]|None|None|
  
Example input:

```
{
  "access_policy": "Example Access Policy",
  "rule_name": "Example Access Rule",
  "url_objects": "[{'name': 'example_url', 'url': 'https://example.com'}]"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Success|True|
  
Example output:

```
{
  "success": true
}
```

#### Bulk Add Scan Result

This action is used to add scan results from a third-party vulnerability scanner

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|operation|string|None|True|The operation to be performed when adding scan results. ScanFlush to remove existing scan results or ScanUpdate to keep existing scan results|["ScanUpdate", "ScanFlush"]|ScanUpdate|None|None|
|scan_results|[]scan_result|None|False|Host scan results to be added|None|[{"host": {"ip_address": "0.0.0.164", "operating_system": {"name": "Ubuntu", "vendor": "Canonical", "version": "16.04"}}, "scan_result_details": {"description": "Example description", "protocol_id": "6", "scanner_id": "ProductZImport", "source_id": "ProductZ", "vulnerability_id": "943387", "vulnerability_title": "Virus Wire 0"}}]|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|commands_processed|number|True|Number of commands processed|4|
|errors|number|True|Number of errors|0|
  
Example output:

```
{
  "commands_processed": 4,
  "errors": 0
}
```

#### Check if Address in Group

This action is used to checks if provided Address Object name or host exists in the Address Group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|Address Object name, or IP, CIDR, or domain name when Enable Search is on|None|MaliciousHost|None|None|
|enable_search|boolean|False|False|When enabled, the Address input will accept an IP, CIDR, or domain name to search across the available Address Objects in the system. This is useful when you don't know the Address Object by its name|None|False|None|None|
|group|string|None|True|Name of address group to check|None|MaliciousAddressGroup|None|None|
  
Example input:

```
{
  "address": "MaliciousHost",
  "enable_search": false,
  "group": "MaliciousAddressGroup"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|address_objects|[]address_object|False|List of found address objects|{"description":" ","dnsResolution":"IPV4_AND_IPV6","id":"00000000-0000-0ed3-0000-021474836483","links":{"parent":"https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networkaddresses","self":"https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/fqdns/00000000-0000-0ed3-0000-021474836483"},"metadata":{"domain":{"id":"e276abec-e0f2-11e3-8169-6d9ed49b625f","name":"Global","type":"Domain"},"lastUser":{"name":"admin"},"parentType":"NetworkAddress","timestamp":1600277332623},"name":"TestAddressObjectFQDN1","overridable":false,"type":"FQDN","value":"example.com"}|
|found|boolean|True|Was address found in group|True|
|literal_objects|[]literal_object|False|List of found literals|[{"type":"FQDN","value":"example.com"}]|
  
Example output:

```
{
  "address_objects": {
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
  },
  "found": true,
  "literal_objects": [
    {
      "type": "FQDN",
      "value": "example.com"
    }
  ]
}
```

#### Create Address Object

This action is used to creates a new address object

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|IP address, CIDR IP address, or domain name to assign to the Address Object|None|example.com|None|None|
|address_object|string|None|False|Name of the address object, defaults to the value address in the address field if no name is given|None|MaliciousHost|None|None|
|skip_private_address|boolean|None|True|If set to true, any addresses that are defined in the RFC1918 space will not be blocked. e.g. 10/8, 172.16/12, 192.168/16|None|True|None|None|
|whitelist|[]string|None|False|This list contains a set of hosts that should not be blocked. This can include IP addresses, CIDR IP addresses, and domains|None|["198.51.100.100", "192.0.2.0/24", "example.com"]|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|address_object|address_object|False|Returns information about the newly created address object|{"dnsResolution":"IPV4_AND_IPV6","id":"00000000-0000-0ed3-0000-012884905524","links":{"parent":"https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networkaddresses","self":"https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/fqdns/00000000-0000-0ed3-0000-012884905524"},"metadata":{"domain":{"id":"e276abec-e0f2-11e3-8169-6d9ed49b625f","name":"Global","type":"Domain"},"lastUser":{"name":"admin"},"parentType":"NetworkAddress","timestamp":0},"name":"Example Object Created from InsightConnect","overridable":false,"type":"FQDN","value":"example.com"}|
  
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

#### Delete Address Object

This action is used to deletes an address object

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address_object|string|None|True|Name of the address object to delete|None|MaliciousHost|None|None|
  
Example input:

```
{
  "address_object": "MaliciousHost"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|address_object|address_object|False|Returns information about the deleted address object|{"dnsResolution":"IPV4_AND_IPV6","id":"00000000-0000-0ed3-0000-012884905524","links":{"parent":"https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networkaddresses","self":"https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/fqdns/00000000-0000-0ed3-0000-012884905524"},"metadata":{"domain":{"id":"e276abec-e0f2-11e3-8169-6d9ed49b625f","name":"Global","type":"Domain"},"lastUser":{"name":"admin"},"parentType":"NetworkAddress","timestamp":0},"name":"Example Object Created from InsightConnect","overridable":false,"type":"FQDN","value":"example.com"}|
  
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

#### Remove Address from Group

This action is used to removes an address from a group

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|The address object name, hostname, an IP address or subnet address expressed in CIDR notation to remove from group|None|MaliciousHost|None|None|
|group|string|None|True|Name of the group to remove the address from|None|MaliciousAddressGroup|None|None|
  
Example input:

```
{
  "address": "MaliciousHost",
  "group": "MaliciousAddressGroup"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|network_group|network_group|False|Returns information about the network group|{"links":{"self":"https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networkgroups/00000000-0000-0ed3-0000-021474836521"},"objects":[{"type":"Host","id":"00000000-0000-0ed3-0000-021474836502","name":"TestAddressObjectHost1"},{"type":"FQDN","id":"00000000-0000-0ed3-0000-021474836483","name":"TestAddressObjectFQDN1"},{"type":"Network","id":"00000000-0000-0ed3-0000-021474836598","name":"TestAddressObjectNetwork"}],"type":"NetworkGroup","overridable":false,"id":"00000000-0000-0ed3-0000-021474836521","name":"TestAddressObjectGroup","metadata":{"timestamp":0,"lastUser":{"name":"admin"},"domain":{"name":"Global","id":"e276abec-e0f2-11e3-8169-6d9ed49b625f","type":"Domain"}}}|
  
Example output:

```
{
  "network_group": {
    "id": "00000000-0000-0ed3-0000-021474836521",
    "links": {
      "self": "https://192.50.100.100/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networkgroups/00000000-0000-0ed3-0000-021474836521"
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
      "timestamp": 0
    },
    "name": "TestAddressObjectGroup",
    "objects": [
      {
        "id": "00000000-0000-0ed3-0000-021474836502",
        "name": "TestAddressObjectHost1",
        "type": "Host"
      },
      {
        "id": "00000000-0000-0ed3-0000-021474836483",
        "name": "TestAddressObjectFQDN1",
        "type": "FQDN"
      },
      {
        "id": "00000000-0000-0ed3-0000-021474836598",
        "name": "TestAddressObjectNetwork",
        "type": "Network"
      }
    ],
    "overridable": false,
    "type": "NetworkGroup"
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**os**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Name|None|
|Vendor|string|None|False|Vendor|None|
|Version|string|None|False|Version|None|
  
**host**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IP Address|string|None|True|IP address|None|
|Host Operating System|os|None|False|Host operating system|None|
  
**result_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Bugtraq IDs|[]string|None|False|The identification numbers associated with the vulnerability in the Bugtraq database (http://www.securityfocus.com/bid)|None|
|CVE IDs|[]string|None|False|The identification number associated with the vulnerability in MITRE's Common Vulnerabilities and Exposures (CVE) database (http://www.cve.mitre.org/)|None|
|Description|string|None|False|Description|None|
|Port|string|None|False|Port|None|
|Protocol ID|string|None|False|Protocol ID|None|
|Scanner ID|string|None|True|Scanner ID for the scanner that obtained the scan results|None|
|Source ID|string|None|True|Application or source ID|None|
|Vulnerability ID|string|None|True|Vulnerability ID|None|
|Vulnerability Title|string|None|True|Title of the vulnerability|None|
  
**scan_result**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Host|host|None|False|Add an untracked host to the network map|None|
|Scan Result Details|result_details|None|False|Scan result for the host|None|
  
**url_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|True|Name of URL object|None|
|URL|string|None|True|URL to block (max 400 chars)|None|
  
**links**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Parent|string|None|False|Full resource URL path to reference the parent (if any) for this resource|None|
|Self|string|None|False|Full resource URL path to reference this particular resource|None|
  
**metadata_user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|The unique UUID of the user|None|
|Links|links|None|False|This defines the self referencing links for the given resource|None|
|Name|string|None|False|Name of the user|None|
|Type|string|None|False|The user type|None|
  
**domain**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Unique UUID of this domain|None|
|Links|links|None|False|This defines the self referencing links for the given resource|None|
|Name|string|None|False|Name of the domain|None|
|Type|string|None|False|Domain type definition|None|
  
**read_only**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Reason|string|None|False|Reason the resource is read only - SYSTEM (if it is system defined), RBAC (if user RBAC permissions make it read only) or DOMAIN (if resource is read only in current domain)|None|
|State|boolean|None|False|True if this resource is read only and false otherwise|None|
  
**metadata**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Domain|domain|None|False|The details about the domain|None|
|IP Type|string|None|False|IP type|None|
|Last User|metadata_user|None|False|This object defines details about the user|None|
|Parent Type|string|None|False|Parent type|None|
|Read Only|read_only|None|False|Defines the read only conditions if the referenced resource is read only|None|
|Timestamp|integer|None|False|The last updated timestamp|None|
  
**reference**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Unique identifier representing resource|None|
|Links|links|None|False|This defines the self referencing links for the given resource|None|
|Name|string|None|False|User chosen resource name|None|
|Type|string|None|False|Response object associated with resource|None|
  
**override**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Parent|reference|None|False|Contains parent reference information|None|
|Target|reference|None|False|Contains target reference information|None|
  
**literal_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Type|string|None|False|The unique type of literal|None|
|Metadata|string|None|False|Actual value of the network|None|
  
**address_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|User provided resource description|None|
|DNS Resolution|string|None|False|DNS resolution|None|
|ID|string|None|False|Unique identifier representing response object|None|
|Links|links|None|False|This defines the self referencing links for the given resource|None|
|Metadata|metadata|None|False|Defines read only details about the object - whether it is system defined, last user who modified the object etc|None|
|Name|string|None|False|User assigned resource name|None|
|Overridable|boolean|None|False|Boolean indicating whether object values can be overridden|None|
|Override Target ID|string|None|False|Unique identifier of domain or device when override assigned to child domain. Used as path parameter to GET override details for a specific object on a specific target (device or domain)|None|
|Overrides|override|None|False|Defines the override details for this object|None|
|Type|string|None|False|The unique type of this object|None|
|Value|string|None|False|Actual value of the network|None|
|Version|string|None|False|Version number of the response object|None|
  
**network_address**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|User provided resource description|None|
|ID|string|None|False|Unique identifier of response object|None|
|Links|links|None|False|This defines the self referencing links for the given resource|None|
|Metadata|metadata|None|False|Defines read only details about the object - whether it is system defined, last user who modified the object etc|None|
|Name|string|None|False|User chosen resource name|None|
|Overridable|boolean|None|False|Boolean indicating whether object values can be overridden|None|
|Override Target ID|string|None|False|Unique identifier of domain or device when override assigned to child domain. Used as path parameter to GET override details for a specific object on a specific target|None|
|Type|string|None|False|Subtype of NetworkAddress (Host, Network, Range, NetworkGroup)|None|
|Value|string|None|False|None|None|
|Version|string|None|False|Version number of the response object|None|
  
**network_address_literal**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Type|string|None|False|Type|None|
|Value|string|None|False|Value|None|
  
**network_group**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|User provided resource description|None|
|ID|string|None|False|Unique identifier of response object|None|
|Links|links|None|False|This defines the self referencing links for the given resource|None|
|Literals|[]network_address_literal|None|False|List of network values in group|None|
|Metadata|metadata|None|False|Defines read only details about the object - whether it is system defined, last user who modified the object etc|None|
|Name|string|None|False|User chosen resource name|None|
|Objects|[]network_address|None|False|The list of member network objects|None|
|Overridable|boolean|None|False|Boolean indicating whether object values can be overridden|None|
|Type|string|None|False|Unique identifier of domain or device when override assigned to child domain. Used as path parameter to GET override details for a specific object on a specific target (device or domain)|None|
|Overrides|override|None|False|Defines the override details for this object|None|
|Type|string|None|False|Type associated with the resource|None|
|Version|string|None|False|Version number of the response object|None|


## Troubleshooting

* The certificate authentication is used solely in two actions, namely: `Add Scan Result` and `Bulk Add Scan Result`. Please remember, that the data entered into the certificate input field in the connection is required to be a base-64 encoded PKCS12 certificate file, exported from the Firepower Management Center server. The passphrase is a password created during the PKCS12 certificate file export.`SSL Verify` field is used by all other actions (i.e. excluding `Add Scan Result` and `Bulk Add Scan Result`), for SSL certificate verification. If the certificate is self-signed then SSL Verify should be set to `False` for those actions.

# Version History

* 2.1.5 - SDK Bump to 6.4.3 | Bumped 'cryptography' package to latest version
* 2.1.4 - Bumped 'cryptography' package to latest version | SDK Bump to 6.2.4
* 2.1.3 - Bumped 'cryptography' | SDK Bump to 6.1.2
* 2.1.2 - `Block URL Policy` - Refactor the action to use local API calls | Remove vulnerable dependencies
* 2.1.1 - Updated to latest SDK version | Fixed issue related to pagination
* 2.1.0 - `Check if Address in Group`: Extended search for manually added literals | Added new output field `literal_objects`
* 2.0.1 - Fix issue in Add Address to Group action where Network Groups that had no objects would result in action failure
* 2.0.0 - Combine Cisco Firepower and Cisco Firepower Management Center plugins
* 1.2.0 - New actions - Check If Address in Group, Add Address to Group, Remove Address from Group
* 1.1.0 - New actions - Create Address Object, Delete Address Object
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

* [Cisco Firepower Management Center](https://www.cisco.com/c/en/us/products/security/firepower-management-center/index.html)

## References

* [Cisco Firepower Management Center](https://www.cisco.com/c/en/us/products/security/firepower-management-center/index.html)