# Description

[PAN-OS](https://www.paloaltonetworks.com/documentation/80/pan-os) is the software that runs all Palo Alto Networks next-generation firewalls. This plugin utilizes the [PAN-OS API](https://www.paloaltonetworks.com/documentation/80/pan-os/xml-api) to provide programmatic management of the Palo Alto Firewall appliance(s). It supports managing firewalls individually or centralized via [Panorama](https://www.paloaltonetworks.com/network-security/panorama)

# Key Features

* Create a new security policy rule to allow or block traffic based on IP addresses, services, applications, users, and zones
* Add rules to and remove rules from existing policies to update the active or candidate firewall configuration
* Commit the candidate configuration to update the active firewall configuration
* Set, Edit, and Delete Objects in order to construct, schedule, and search for policy rules
* Add an external dynamic list of IP addresses, URLs, and domains to an enforcement policy
* Run an operational command to manage your firewall(s)
* Query firewall log events to search for matches or patterns
* Get candidate configuration and show active configuration to view configuration settings

# Requirements

* Access to Palo Alto Next Generation firewall or Palo Alto Panorama device

# Supported Product Versions

* 11.X

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_username_password|None|True|Username and password|None|{"username":"username", "password":"password"}|None|None|
|server|string|None|True|URL pointing to instance of Panorama or an individual Palo Alto Firewall|None|http://www.example.com|None|None|
|verify_cert|boolean|None|True|If true, validate the server's TLS certificate when contacting the firewall over HTTPS|None|True|None|None|

Example input:

```
{
  "credentials": {
    "password": "password",
    "username": "username"
  },
  "server": "http://www.example.com",
  "verify_cert": true
}
```

## Technical Details

### Actions


#### Add Address Object to Group

This action is used to adds address objects to an address group. This action uses a direct connection to the firewall

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address_object|[]string|None|True|The names of the address objects to add|None|["198.51.100.100", "198.51.100.101", "example.com"]|None|None|
|device_name|string|localhost.localdomain|True|Device name|None|localhost.localdomain|None|None|
|group|string|None|True|Group name|None|InsightConnect Block List|None|None|
|virtual_system|string|vsys1|True|Virtual system name|None|vsys1|None|None|
  
Example input:

```
{
  "address_object": [
    "198.51.100.100",
    "198.51.100.101",
    "example.com"
  ],
  "device_name": "localhost.localdomain",
  "group": "InsightConnect Block List",
  "virtual_system": "vsys1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|address_objects|[]string|True|Address objects currently in group|["test.com", "domain.com", "198.51.100.102", "198.51.100.100", "198.51.100.101", "example.com"]|
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "address_objects": [
    "test.com",
    "domain.com",
    "198.51.100.102",
    "198.51.100.100",
    "198.51.100.101",
    "example.com"
  ],
  "success": true
}
```

#### Add External Dynamic List

This action is used to add an external dynamic list. This action uses a direct connection to the firewall

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|day|string||True|If repeat is weekly, choose a day to update|["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]|Monday|None|None|
|description|string|None|True|A description of the list|None|List of IP's|None|None|
|list_type|string|None|True|The type of list|["IP List", "Domain List", "URL List"]|IP List|None|None|
|name|string|None|True|An arbitrary name for the list. This name will be used to identify the list in the firewall|None|IP List|None|None|
|repeat|string|None|True|The interval at which to retrieve updates from the list|["Five Minute", "Hourly", "Daily", "Weekly"]|Five Minute|None|None|
|source|string|None|True|The web site you will pull the list from e.g. https://www.example.com/test.txt|None|https://www.example.com/test.txt|None|None|
|time|string||True|If repeat is daily or weekly, choose an hour on a 24 hour clock to update (Default: '')|["", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]|00|None|None|
  
Example input:

```
{
  "day": "",
  "description": "List of IP's",
  "list_type": "IP List",
  "name": "IP List",
  "repeat": "Five Minute",
  "source": "https://www.example.com/test.txt",
  "time": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|code|string|False|Response code from the firewall|20|
|message|string|False|A message with more detail about the status|command succeeded|
|status|string|False|The status of the requested operation e.g. success, error, etc|success|
  
Example output:

```
{
  "code": 20,
  "message": "command succeeded",
  "status": "success"
}
```

#### Add to Policy

This action is used to add a rule to a firewall security policy. This action uses a direct connection to the firewall

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|None|False|Action that will occur if an event meets the rule definitions|None|drop|None|None|
|application|string|None|False|Application for which this rule will be applied e.g. adobe-cloud, dropbox, or  any|None|any|None|None|
|destination|string|None|False|A destination for which this rule will be applied e.g. 10.0.0.1, computername, or any|None|any|None|None|
|dst_zone|string|None|False|Zone which the traffic is going to e.g. server zone, or any|None|any|None|None|
|hip_profiles|string|None|False|Host information profile|None|any|None|None|
|rule_name|string|None|True|Name of the rule|None|InsightConnect Block Rule|None|None|
|service|string|None|False|Service type for which this rule will be applied e.g. HTTP, HTTPS, or any|None|any|None|None|
|source|string|None|False|A source for which this rule will be applied e.g. 10.0.0.1, computername, or any|None|any|None|None|
|source_user|string|None|False|User that the network traffic originated from e.g. Joe Smith, or any|None|Joe Smith|None|None|
|src_zone|string|None|False|Zone in which the traffic originated e.g. server zone, or any|None|any|None|None|
|update_active_or_candidate_configuration|string|None|True|Will apply the update to the active or candidate configuration. If active is chosen any uncommitted candidate configuration will be lost|["active", "candidate"]|active|None|None|
|url_category|string|None|False|The URL category e.g. adult|None|adult|None|None|
  
Example input:

```
{
  "action": "drop",
  "application": "any",
  "destination": "any",
  "dst_zone": "any",
  "hip_profiles": "any",
  "rule_name": "InsightConnect Block Rule",
  "service": "any",
  "source": "any",
  "source_user": "Joe Smith",
  "src_zone": "any",
  "update_active_or_candidate_configuration": "active",
  "url_category": "adult"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|code|string|False|Response code from firewall|20|
|message|string|False|A message with more detail about the status|command succeeded|
|status|string|False|Status of the requested operation e.g. success, error, etc|success|
  
Example output:

```
{
  "code": 20,
  "message": "command succeeded",
  "status": "success"
}
```

#### Check if Address in Group

This action is used to checks to see if an IP address, CIDR IP address, or domain is in an Address Group. Supports 
IPv6. This action uses a direct connection to the firewall

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|The Address Object name to check. If Enable Search is set to true then we search the addresses (IP, CIDR, domain) within the address object instead of matching the name|None|198.51.100.100|None|None|
|device_name|string|localhost.localdomain|True|Device name|None|localhost.localdomain|None|None|
|enable_search|boolean|False|True|When enabled, the Address input will accept a IP, CIDR, or domain name to search across the available Address Objects in the system. This is useful when you don't know the Address Object by its name|None|False|None|None|
|group|string|None|True|Group name|None|InsightConnect Block List|None|None|
|virtual_system|string|vsys1|True|Virtual system name|None|vsys1|None|None|
  
Example input:

```
{
  "address": "198.51.100.100",
  "device_name": "localhost.localdomain",
  "enable_search": false,
  "group": "InsightConnect Block List",
  "virtual_system": "vsys1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|address_objects|[]string|False|The names of the address objects that match or contain address|["198.51.100.100"]|
|found|boolean|True|Was address found in group|True|
  
Example output:

```
{
  "address_objects": [
    "198.51.100.100"
  ],
  "found": true
}
```

#### Commit

This action is used to commits the candidate configuration. This action uses a direct connection to the firewall

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|all|False|Commit action (Default: 'all')|None|all|None|None|
|cmd|string|None|True|XML specifying any commit arguments|None|<commit></commit>|None|None|
  
Example input:

```
{
  "action": "all",
  "cmd": "<commit></commit>"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|Response from the firewall|{'@status': 'success', '@code': '19', 'result': {'msg': {'line': 'Commit job enqueued with jobid 152'}, 'job': '152'}}|
  
Example output:

```
{
  "response": {
    "@code": "19",
    "@status": "success",
    "result": {
      "job": "152",
      "msg": {
        "line": "Commit job enqueued with jobid 152"
      }
    }
  }
}
```

#### Delete

This action is used to delete an object. This action uses Panorama

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|xpath|string|None|True|Xpath targeting the object to delete|None|/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address-group/entry[@name='test_group']|None|None|
  
Example input:

```
{
  "xpath": "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address-group/entry[@name='test_group']"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|config|False|Response from the firewall|{'@status': 'success', '@code': '20', 'msg': 'command succeeded'}|
  
Example output:

```
{
  "response": {
    "@code": "20",
    "@status": "success",
    "msg": "command succeeded"
  }
}
```

#### Edit

This action is used to edit an existing object. This action uses Panorama

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|element|string|None|True|XML representation of the updated object. This replaces the previous object entirely, any unchanged attributes must be restated|None|<application><member>8x8</member></application>|None|None|
|xpath|string|None|True|Xpath location of the object to edit|None|/config/devices/entry/vsys/entry/rulebase/security/rules/entry[@name='test rule']/application|None|None|
  
Example input:

```
{
  "element": "<application><member>8x8</member></application>",
  "xpath": "/config/devices/entry/vsys/entry/rulebase/security/rules/entry[@name='test rule']/application"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|Response from the firewall|{'@status': 'success', '@code': '20', 'msg': 'command succeeded'}|
  
Example output:

```
{
  "response": {
    "@code": "20",
    "@status": "success",
    "msg": "command succeeded"
  }
}
```

#### Get

This action is used to get candidate configuration. This action uses Panorama

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|xpath|string|None|True|Xpath targeting the requested portion of the configuration|None|/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address-group/entry[@name='test_group']|None|None|
  
Example input:

```
{
  "xpath": "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']/address-group/entry[@name='test_group']"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|config|False|Response from the firewall|{'@status': 'success', '@code': '19', 'result': {'@total-count': '1', '@count': '1', 'entry': {'@name': 'test_group', '@admin': 'admin', '@dirtyid': '4', '@time': '2020/08/25 09:35:48', 'static': {'@admin': 'admin', '@dirtyid': '4', '@time': '2020/08/25 09:35:48', 'member': {'@admin': 'admin', '@dirtyid': '4', '@time': '2020/08/25 09:35:48', '#text': '1.1.1.1'}}, 'description': {'@admin': 'admin', '@dirtyid': '4', '@time': '2020/08/25 09:35:48', '#text': 'test'}}}}|
  
Example output:

```
{
  "response": {
    "@code": "19",
    "@status": "success",
    "result": {
      "@count": "1",
      "@total-count": "1",
      "entry": {
        "@admin": "admin",
        "@dirtyid": "4",
        "@name": "test_group",
        "@time": "2020/08/25 09:35:48",
        "description": {
          "#text": "test",
          "@admin": "admin",
          "@dirtyid": "4",
          "@time": "2020/08/25 09:35:48"
        },
        "static": {
          "@admin": "admin",
          "@dirtyid": "4",
          "@time": "2020/08/25 09:35:48",
          "member": {
            "#text": "1.1.1.1",
            "@admin": "admin",
            "@dirtyid": "4",
            "@time": "2020/08/25 09:35:48"
          }
        }
      }
    }
  }
}
```

#### Get Addresses from Group

This action is used to get addresses from an address group. This action uses a direct connection to the firewall

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|device_name|string|localhost.localdomain|True|Device name|None|localhost.localdomain|None|None|
|group|string|None|True|Group name|None|InsightConnect Block List|None|None|
|virtual_system|string|vsys1|True|Virtual system name|None|vsys1|None|None|
  
Example input:

```
{
  "device_name": "localhost.localdomain",
  "group": "InsightConnect Block List",
  "virtual_system": "vsys1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|all_addresses|[]string|True|Addresses currently in group|["1.1.1.1", "1.1.1.1/24", "1.2.3.4", "2.2.2.2", "2.2.4.5", "5.182.39.91", "8.8.8.8", "8.8.8.9", "8.8.8.10", "8.8.8.11", "20.20.20.20", "2001:0db8:85a3:0000:0000:8a2e:0370:7334", "domain.com", "test.com", "example1.com", "example2.com"]|
|fqdn_addresses|[]string|True|FQDN addresses currently in group|["domain.com", "test.com", "example1.com", "example2.com"]|
|ipv4_addresses|[]string|True|IPv4 addresses currently in group|["1.1.1.1", "1.1.1.1/24", "1.2.3.4", "2.2.2.2", "2.2.4.5", "5.182.39.91", "8.8.8.8", "8.8.8.9", "8.8.8.10", "8.8.8.11", "20.20.20.20"]|
|ipv6_addresses|[]string|True|IPv6 addresses currently in group|["2001:0db8:85a3:0000:0000:8a2e:0370:7334"]|
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "all_addresses": [
    "1.1.1.1",
    "1.1.1.1/24",
    "1.2.3.4",
    "2.2.2.2",
    "2.2.4.5",
    "5.182.39.91",
    "8.8.8.8",
    "8.8.8.9",
    "8.8.8.10",
    "8.8.8.11",
    "20.20.20.20",
    "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
    "domain.com",
    "test.com",
    "example1.com",
    "example2.com"
  ],
  "fqdn_addresses": [
    "domain.com",
    "test.com",
    "example1.com",
    "example2.com"
  ],
  "ipv4_addresses": [
    "1.1.1.1",
    "1.1.1.1/24",
    "1.2.3.4",
    "2.2.2.2",
    "2.2.4.5",
    "5.182.39.91",
    "8.8.8.8",
    "8.8.8.9",
    "8.8.8.10",
    "8.8.8.11",
    "20.20.20.20"
  ],
  "ipv6_addresses": [
    "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
  ],
  "success": true
}
```

#### Get Policy

This action is used to get a policy by name. This action uses a direct connection to the firewall

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|device_name|string|localhost.localdomain|True|Device name|None|localhost.localdomain|None|None|
|policy_name|string|None|True|Policy name|None|InsightConnect Block Policy|None|None|
|virtual_system|string|vsys1|True|Virtual system name|None|vsys1|None|None|
  
Example input:

```
{
  "device_name": "localhost.localdomain",
  "policy_name": "InsightConnect Block Policy",
  "virtual_system": "vsys1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|action|string|False|Action|["drop"]|
|application|[]string|False|Application|["any"]|
|category|[]string|False|Category|["any"]|
|destination|[]string|False|Destination|["any"]|
|from|[]string|False|From|["any"]|
|hip_profiles|[]string|False|Host Information in Policy Enforcement profile|["any"]|
|service|[]string|False|Service|["application-default"]|
|source|[]string|False|Source|["1.1.1.1", "1.1.1.2"]|
|source_user|[]string|False|Source user|["any"]|
|to|[]string|False|To|["any"]|
  
Example output:

```
{
  "action": [
    "drop"
  ],
  "application": [
    "any"
  ],
  "category": [
    "any"
  ],
  "destination": [
    "any"
  ],
  "from": [
    "any"
  ],
  "hip_profiles": [
    "any"
  ],
  "service": [
    "application-default"
  ],
  "source": [
    "1.1.1.1",
    "1.1.1.2"
  ],
  "source_user": [
    "any"
  ],
  "to": [
    "any"
  ]
}
```

#### Op

This action is used to runs operational command. This action uses a direct connection to the firewall

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cmd|string|None|False|XML specifying operation to be completed|None|<show><commit-locks/></show>|None|None|
  
Example input:

```
{
  "cmd": "<show><commit-locks/></show>"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|Response from the firewall|{'@status': 'success', 'result': {'system': {'hostname': 'firewall', 'ip-address': '10.27.0.8', 'netmask': '255.255.254.0', 'default-gateway': '10.27.0.1', 'is-dhcp': 'no', 'ipv6-address': 'unknown', 'ipv6-link-local-address': 'fe80::21b:17dd:dedf:c04a/64', 'mac-address': '00:1b:17:ff:c0:4a', 'time': 'Wed Feb 10 13:03:32 2016', 'uptime': '1 days, 19:35:51', 'devicename': 'firewall', 'family': '3000', 'model': 'PA-3020', 'serial': '001901000114', 'sw-version': '7.1.', 'global-protect-client-package-version': '2.0.0', 'app-version': '557-3138', 'app-release-date': '2016/02/09  16:56:02', 'av-version': '2261-2700', 'av-release-date': '2016/02/09  15:26:53', 'threat-version': '557-3138', 'threat-release-date': '2016/02/09  16:56:02', 'wf-private-version': '0', 'wf-private-release-date': 'unknown', 'url-db': 'paloaltonetworks', 'wildfire-version': '27518-28208', 'wildfire-release-date': '2016/01/08  11:08:16', 'url-filtering-version': '2016.01.08.407', 'global-protect-datafile-version': '1452328885', 'global-protect-datafile-release-date': '2016/01/09 08:41:25', 'logdb-version': '7.0.9', 'platform-family': '3000', 'vpn-disable-mode': 'off', 'multi-vsys': 'on', 'operational-mode': 'normal'}}}|
  
Example output:

```
{
  "response": {
    "@status": "success",
    "result": {
      "system": {
        "app-release-date": "2016/02/09  16:56:02",
        "app-version": "557-3138",
        "av-release-date": "2016/02/09  15:26:53",
        "av-version": "2261-2700",
        "default-gateway": "10.27.0.1",
        "devicename": "firewall",
        "family": "3000",
        "global-protect-client-package-version": "2.0.0",
        "global-protect-datafile-release-date": "2016/01/09 08:41:25",
        "global-protect-datafile-version": "1452328885",
        "hostname": "firewall",
        "ip-address": "10.27.0.8",
        "ipv6-address": "unknown",
        "ipv6-link-local-address": "fe80::21b:17dd:dedf:c04a/64",
        "is-dhcp": "no",
        "logdb-version": "7.0.9",
        "mac-address": "00:1b:17:ff:c0:4a",
        "model": "PA-3020",
        "multi-vsys": "on",
        "netmask": "255.255.254.0",
        "operational-mode": "normal",
        "platform-family": "3000",
        "serial": "001901000114",
        "sw-version": "7.1.",
        "threat-release-date": "2016/02/09  16:56:02",
        "threat-version": "557-3138",
        "time": "Wed Feb 10 13:03:32 2016",
        "uptime": "1 days, 19:35:51",
        "url-db": "paloaltonetworks",
        "url-filtering-version": "2016.01.08.407",
        "vpn-disable-mode": "off",
        "wf-private-release-date": "unknown",
        "wf-private-version": "0",
        "wildfire-release-date": "2016/01/08  11:08:16",
        "wildfire-version": "27518-28208"
      }
    }
  }
}
```

#### Remove Address Object from Group

This action is used to removes an address object from an address group. Supports IPv6. This action uses a direct 
connection to the firewall

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address_object|string|None|True|The name of the address object to remove|None|Malicious Host|None|None|
|device_name|string|localhost.localdomain|True|Device name|None|localhost.localdomain|None|None|
|group|string|None|True|Group name|None|InsightConnect Block List|None|None|
|virtual_system|string|vsys1|True|Virtual system name|None|vsys1|None|None|
  
Example input:

```
{
  "address_object": "Malicious Host",
  "device_name": "localhost.localdomain",
  "group": "InsightConnect Block List",
  "virtual_system": "vsys1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Was operation successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Remove from Policy

This action is used to remove a rule from a firewall security policy. This action uses a direct connection to the 
firewall

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|None|False|The action that will occur if an event meets the rule definitions|None|drop|None|None|
|application|string|None|False|Application for which this rule will be applied e.g. adobe-cloud, dropbox, or any|None|any|None|None|
|destination|string|None|False|A Destination for which this rule will be applied e.g. 10.0.0.1, computername, or any|None|any|None|None|
|dst_zone|string|None|False|Zone which the traffic is going to e.g. server zone, or any|None|any|None|None|
|hip_profiles|string|None|False|Host information profile|None|any|None|None|
|rule_name|string|None|True|Name of the rule|None|InsightConnect Block Rule|None|None|
|service|string|None|False|Service type for which this rule will be applied e.g. HTTP, HTTPS, any|None|any|None|None|
|source|string|None|False|A source for which this rule will be applied e.g. 10.0.0.1, computername, or any|None|any|None|None|
|source_user|string|None|False|User that the network traffic originated from e.g. Joe Smith, or any|None|any|None|None|
|src_zone|string|None|False|Zone in which the traffic originated e.g. server zone, or any|None|any|None|None|
|update_active_or_candidate_configuration|string|None|True|Will apply the update to the active or candidate configuration. If active is chosen any uncommitted candidate configuration will be lost|["active", "candidate"]|active|None|None|
|url_category|string|None|False|The URL category e.g. adult|None|adult|None|None|
  
Example input:

```
{
  "action": "drop",
  "application": "any",
  "destination": "any",
  "dst_zone": "any",
  "hip_profiles": "any",
  "rule_name": "InsightConnect Block Rule",
  "service": "any",
  "source": "any",
  "source_user": "any",
  "src_zone": "any",
  "update_active_or_candidate_configuration": "active",
  "url_category": "adult"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|code|string|False|Response code from the firewall|20|
|message|string|False|A message with more detail about the status|command succeeded|
|status|string|False|Status of the requested operation e.g. success, error, etc|success|
  
Example output:

```
{
  "code": 20,
  "message": "command succeeded",
  "status": "success"
}
```

#### Retrieve Logs

This action is used to queries firewall logs. This action uses a direct connection to the firewall

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|count|integer|20|False|Number of logs to retrieve (Max: 500, Default: 20)|None|20|None|None|
|direction|string|None|False|Order in which to return the logs|["backward", "forward"]|backward|None|None|
|filter|string|None|False|Search query. Format as a log filter expression|None|receive_time geq '2021/12/22 08:00:00'|None|None|
|interval|float|0.5|False|Time interval in seconds to wait between queries for commit job completion (Default: 0.5)|None|0.5|None|None|
|log_type|string|None|False|Type of log to retrieve|["config", "hipmatch", "system", "threat", "traffic", "url", "wildfire"]|config|None|None|
|max_tries|integer|25|False|Maximum number of times to poll for job completion before timing out (Default: 25)|None|25|None|None|
|skip|integer|0|False|Log retrieval offset, number of entries to skip, (Default: 0)|None|0|None|None|
  
Example input:

```
{
  "count": 20,
  "direction": "backward",
  "filter": "receive_time geq '2021/12/22 08:00:00'",
  "interval": 0.5,
  "log_type": "config",
  "max_tries": 25,
  "skip": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|log|False|Response from the firewall|{'@status': 'success', 'result': {'job': {'tenq': '17:32:53', 'tdeq': '17:32:53', 'tlast': '17:32:53', 'status': 'FIN', 'id': '1466', 'cached-logs': '0'}, 'log': {'logs': {'-count': '0', '-progress': '100'}}, 'meta': {'devices': {'entry': {'-name': 'localhost.localdomain', 'hostname': 'localhost.localdomain', 'vsys': {'entry': {'-name': 'vsys1', 'display-name': 'vsys1'}}}}}}}|
  
Example output:

```
{
  "response": {
    "@status": "success",
    "result": {
      "job": {
        "cached-logs": "0",
        "id": "1466",
        "status": "FIN",
        "tdeq": "17:32:53",
        "tenq": "17:32:53",
        "tlast": "17:32:53"
      },
      "log": {
        "logs": {
          "-count": "0",
          "-progress": "100"
        }
      },
      "meta": {
        "devices": {
          "entry": {
            "-name": "localhost.localdomain",
            "hostname": "localhost.localdomain",
            "vsys": {
              "entry": {
                "-name": "vsys1",
                "display-name": "vsys1"
              }
            }
          }
        }
      }
    }
  }
}
```

#### Set

This action is used to create a new object. This action uses Panorama

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|element|string|None|True|XML representation of the object to be created|None|<application><member>8x8</member></application>|None|None|
|xpath|string|None|True|Xpath location to create the new object|None|/config/devices/entry/vsys/entry/rulebase/security/rules/entry[@name='test rule']|None|None|
  
Example input:

```
{
  "element": "<application><member>8x8</member></application>",
  "xpath": "/config/devices/entry/vsys/entry/rulebase/security/rules/entry[@name='test rule']"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|object|False|Response from the firewall|{'@status': 'success', '@code': '20', 'msg': 'command succeeded'}|
  
Example output:

```
{
  "response": {
    "@code": "20",
    "@status": "success",
    "msg": "command succeeded"
  }
}
```

#### Create Address Object

This action is used to create a new address object. Supports IPv6. This action uses a direct connection to the firewall

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|The IP address, network CIDR, or FQDN e.g. 192.168.1.1, 192.168.1.0/24, google.com|None|1.1.1.1|None|None|
|address_object|string|None|True|The name of the address object|None|Blocked host|None|None|
|description|string|None|False|A description for the address object|None|Blocked host from Insight Connect|None|None|
|skip_rfc1918|boolean|False|True|Skip private IP addresses as defined in RFC 1918|None|True|None|None|
|tags|string|None|False|Tags for the address object. Use commas to separate multiple tags|None|malware|None|None|
|whitelist|[]string|None|False|This list contains a set of network objects that should not be blocked. This can include IPs, CIDR notation, or domains. It can not include an IP range (such as 10.0.0.0-10.0.0.10)|None|["198.51.100.100", "192.0.2.0/24", "example.com"]|None|None|
  
Example input:

```
{
  "address": "1.1.1.1",
  "address_object": "Blocked host",
  "description": "Blocked host from Insight Connect",
  "skip_rfc1918": false,
  "tags": "malware",
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
|code|string|False|Response code from the firewall|20|
|message|string|False|A message with more detail about the status|command succeeded|
|status|string|False|The status of the requested operation e.g. success, error, etc|success|
  
Example output:

```
{
  "code": 20,
  "message": "command succeeded",
  "status": "success"
}
```

#### Set Security Policy Rule

This action is used to creates a new Security Policy Rule. This action uses a direct connection to the firewall

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|None|True|Action that will occur if an event meets the rule definitions|None|drop|None|None|
|application|string|None|True|Applications for which this rule will be applied e.g. adobe-cloud, dropbox,  any|None|any|None|None|
|description|string|None|True|Description of the rule and what it does|None|Block Rule|None|None|
|destination|string|None|True|Destinations for which this rule will be applied e.g. 10.0.0.1, computername, any|None|any|None|None|
|disable_server_response_inspection|boolean|None|True|If true, the firewall will not inspect this traffic|None|False|None|None|
|disabled|boolean|None|True|If true, rule is disabled|None|False|None|None|
|dst_zone|string|None|True|Zone which the traffic is going to e.g. server zone, any|None|any|None|None|
|log_end|boolean|None|True|Generates a traffic log entry for the end of a session|None|False|None|None|
|log_start|boolean|None|True|Generates a traffic log entry for the start of a session|None|False|None|None|
|negate_destination|boolean|None|True|Negate destination|None|False|None|None|
|negate_source|boolean|None|True|Negate source|None|False|None|None|
|rule_name|string|None|True|Name of the rule|None|InsightConnect Block Rule|None|None|
|service|string|None|True|Service type for which this rule will be applied e.g. HTTP, HTTPS, any|None|any|None|None|
|source|string|None|True|Sources for which this rule will be applied e.g. 10.0.0.1, computername, any|None|any|None|None|
|source_user|string|None|True|User that the network traffic originated from e.g. Joe Smith, any|None|any|None|None|
|src_zone|string|None|True|Zone in which the traffic originated e.g. server zone, any|None|any|None|None|
  
Example input:

```
{
  "action": "drop",
  "application": "any",
  "description": "Block Rule",
  "destination": "any",
  "disable_server_response_inspection": false,
  "disabled": false,
  "dst_zone": "any",
  "log_end": false,
  "log_start": false,
  "negate_destination": false,
  "negate_source": false,
  "rule_name": "InsightConnect Block Rule",
  "service": "any",
  "source": "any",
  "source_user": "any",
  "src_zone": "any"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|config|False|Response from the firewall|{'@status': 'success', '@code': '20', 'msg': 'command succeeded'}|
  
Example output:

```
{
  "response": {
    "@code": "20",
    "@status": "success",
    "msg": "command succeeded"
  }
}
```

#### Show

This action is used to gets active configuration. This action uses Panorama

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|xpath|string|None|True|Xpath targeting the requested portion of the configuration|None|/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']|None|None|
  
Example input:

```
{
  "xpath": "/config/devices/entry[@name='localhost.localdomain']/vsys/entry[@name='vsys1']"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|config|False|Response from the firewall|{'@status': 'success', 'result': {'system': {'hostname': 'firewall', 'ip-address': '10.27.0.0', 'netmask': '255.255.254.0', 'default-gateway': '10.27.0.1', 'is-dhcp': 'no', 'ipv6-address': 'unknown', 'ipv6-link-local-address': 'fe80::21b:17dd:dedf:c04a/64', 'mac-address': '00:1b:17:ff:c0:4a', 'time': 'Wed Feb 10 13:03:32 2016', 'uptime': '1 days, 19:35:51', 'devicename': 'firewall', 'family': '3000', 'model': 'PA-3020', 'serial': '001901000114', 'sw-version': '7.1.', 'global-protect-client-package-version': '2.0.0', 'app-version': '557-3138', 'app-release-date': '2016/02/09 16:56:02', 'av-version': '2261-2700', 'av-release-date': '2016/02/09 15:26:53', 'threat-version': '557-3138', 'threat-release-date': '2016/02/09 16:56:02', 'wf-private-version': '0', 'wf-private-release-date': 'unknown', 'url-db': 'paloaltonetworks', 'wildfire-version': '27518-28208', 'wildfire-release-date': '2016/01/08 11:08:16', 'url-filtering-version': '2016.01.08.407', 'global-protect-datafile-version': '1452328885', 'global-protect-datafile-release-date': '2016/01/09 08:41:25', 'logdb-version': '7.0.9', 'platform-family': '3000', 'vpn-disable-mode': 'off', 'multi-vsys': 'on', 'operational-mode': 'normal'}}}|
  
Example output:

```
{
  "response": {
    "@status": "success",
    "result": {
      "system": {
        "app-release-date": "2016/02/09 16:56:02",
        "app-version": "557-3138",
        "av-release-date": "2016/02/09 15:26:53",
        "av-version": "2261-2700",
        "default-gateway": "10.27.0.1",
        "devicename": "firewall",
        "family": "3000",
        "global-protect-client-package-version": "2.0.0",
        "global-protect-datafile-release-date": "2016/01/09 08:41:25",
        "global-protect-datafile-version": "1452328885",
        "hostname": "firewall",
        "ip-address": "10.27.0.0",
        "ipv6-address": "unknown",
        "ipv6-link-local-address": "fe80::21b:17dd:dedf:c04a/64",
        "is-dhcp": "no",
        "logdb-version": "7.0.9",
        "mac-address": "00:1b:17:ff:c0:4a",
        "model": "PA-3020",
        "multi-vsys": "on",
        "netmask": "255.255.254.0",
        "operational-mode": "normal",
        "platform-family": "3000",
        "serial": "001901000114",
        "sw-version": "7.1.",
        "threat-release-date": "2016/02/09 16:56:02",
        "threat-version": "557-3138",
        "time": "Wed Feb 10 13:03:32 2016",
        "uptime": "1 days, 19:35:51",
        "url-db": "paloaltonetworks",
        "url-filtering-version": "2016.01.08.407",
        "vpn-disable-mode": "off",
        "wf-private-release-date": "unknown",
        "wf-private-version": "0",
        "wildfire-release-date": "2016/01/08 11:08:16",
        "wildfire-version": "27518-28208"
      }
    }
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**config**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|data|object|None|None|None|None|
  
**log**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|data|object|None|None|None|None|


## Troubleshooting

* For the URL, include `https://` e.g. `https://10.0.0.1` or `https://myfirewall.`

 When using the `Add External Dynamic List` action, a day and time must be chosen, even if they are not used.

 Action Connection Type:

 | Action name                      | Connection type       |
 | -----------                      | --------------------- |
 | Add Address Object to Group      | Direct firewall       |
 | Add External Dynamic List        | Direct firewall       |
 | Add to Policy                    | Direct firewall       |
 | Check if Address in Group        | Direct firewall       |
 | Commit                           | Direct firewall       |
 | Create Address Object            | Direct firewall       |
 | Delete                           | Panorama              |
 | Edit                             | Panorama              |
 | Get                              | Panorama              |
 | Get Addresses from Group         | Direct firewall       |
 | Get Policy                       | Direct firewall       |
 | Op                               | Direct firewall       |
 | Remove Address Object from Group | Direct firewall       |
 | Remove from Policy               | Direct firewall       |
 | Retrieve Logs                    | Direct firewall       |
 | Set                              | Panorama              |
 | Set Security Policy Rule         | Direct firewall       |
 | Show                             | Panorama              |


# Version History

* 6.1.11 - Update for compatibility with Palo Alto version 11.X | Updated SDK to latest version (6.4.2)
* 6.1.10 - Addressed Snyk Vulnerability | Updated SDK to latest version (6.3.10)
* 6.1.9 - Addressed Snyk Vulnerability | Updated SDK to latest version (6.3.4)
* 6.1.8 - Updated SDK to the latest version (6.2.6)
* 6.1.7 - Fix issue in 'add_address_object_to_group' action | SDK bump to 6.2.0 | Bumping requirements.txt
* 6.1.6 - Update SDK | Fix critical Snyk vulnerability
* 6.1.5 - Bumping requirements of `gunicorn` and `validators` | update the SDK to 5.4.9 | Added examples to all actions | Updated unit tests to include schema checks
* 6.1.4 - Add information to every action on whether it uses Panorama or a direct firewall connection
* 6.1.3 - Fix `check_if_private` method in Set Address Object action | Improve `determine_address_type` method in Set Address Object action | Fix issue where Add External Dynamic List action fails when `repeat` input has been set to retrieve updates from list weekly | Add example for `filter` input for Retrieve Logs action
* 6.1.2 - Add `docs_url` in plugin spec | Update `source_url` in plugin spec
* 6.1.1 - Remove duplicate Troubleshooting section in documentation
* 6.1.0 - Improve error handling for xpath elements and paths in `pa_os_request.py` | New action Get Addresses from Group | Support adding a list of address objects in Add Address Object to Group action
* 6.0.4 - Update error handling in Add Address Object to Group, Check if Address in Group, Get Policy and Remove Address Object from Group actions
* 6.0.3 - Add Input and Output examples
* 6.0.2 - Fix issue where Set Network Object did not support IPv6
* 6.0.1 - Improve error handling in `pa_os_request.py`
* 6.0.0 - Update to Create Address Object to add Skip RFC 1918 input
* 5.1.1 - Fix issue where IPv6 address were not supported
* 5.1.0 - New action Add Address Object to Group
* 5.0.0 - Change plugin title to "Palo Alto Firewall" from "Palo Alto PAN-OS" and update remaining references
* 4.0.0 - Update to Create Address Object to make input consistent with other actions
* 3.0.0 - New action Remove Address Object from Group | Update to Check if Address in Group to match input of Remove Address Object from Group
* 2.2.0 - New action Check if Address in Group
* 2.1.0 - New action Get Policy
* 2.0.0 - Update to rename Set Address Object to Create Address Object | Update Create Address Object to accept a whitelist of address objects and auto detect the type of incoming object
* 1.5.7 - Default value of Commit action updated
* 1.5.6 - Fix issue where edit action was causing an error with certain input
* 1.5.5 - New spec and help.md format for the Extension Library
* 1.5.4 - Fix issue where new plugin version was causing SSL to fail
* 1.5.3 - Fix issue where undefined objects in security configurations caused actions to crash | Add debug logging to assist with future troubleshooting | Update to use the `komand/python-3-37-slim-plugin:3` Docker image to reduce plugin size
* 1.5.2 - Fix typo in plugin spec
* 1.5.1 - Fix issue where the Add to Policy action would sometimes fail with candidate configurations
* 1.5.0 - New action Set Address Object
* 1.4.1 - Update connection tests
* 1.4.0 - Update Add to Policy action to allow for updates to active configuration or candidate objects | Update Remove from Policy action to allow for updates to active configuration or candidate objects
* 1.3.1 - Update descriptions
* 1.3.0 - New action Add External Dynamic List
* 1.2.0 - New action Remove from Policy
* 1.1.0 - New action Add to Policy
* 1.0.0 - Add action to set a new security policy | Update to v2 Python plugin architecture | Support web server mode | Add error handling
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Palo Alto PAN-OS](https://www.paloaltonetworks.com/documentation/80/pan-os)

## References

* [Palo Alto PAN-OS API](https://www.paloaltonetworks.com/documentation/80/pan-os/xml-api)