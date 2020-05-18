# Description

[PAN-OS](https://www.paloaltonetworks.com/documentation/80/pan-os) is the software that runs all Palo Alto Networks next-generation firewalls. This plugin utilizes the [PAN-OS API](https://www.paloaltonetworks.com/documentation/80/pan-os/xml-api) to provide programmatic management of the Palo Alto PAN-OS firewall appliance(s).

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

* PAN-OS credentials

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password|None|None|
|server|string|None|True|URL pointing to instance of PAN-OS|None|None|
|verify_cert|boolean|None|True|If true, validate the server's TLS certificate when contacting PAN-OS over HTTPS|None|None|

Example input:

```
```

## Technical Details

### Actions

#### Remove Address Object from Group

This action removes an address object from an address group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address_object|string|None|True|The name of the address object to remove|None|Malicious IP|
|device_name|string|localhost.localdomain|True|Device name|None|localhost.localdomain|
|group_name|string|None|True|Group name|None|ICON Block List|
|virtual_system|string|vsys1|True|Virtual system name|None|vsys1|

Example input:

```
{
  "address_object": "Malicious IP",
  "device_name": "localhost.localdomain",
  "group_name": "ICON Block List",
  "virtual_system": "vsys1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Was operation successful|

Example output:

```
```

#### 

This action is used to .

##### Input

_This action does not contain any inputs._

##### Output

_This action does not contain any outputs._

#### Check If Address in Group

This action checks to see if an IP, CIDR, or domain is in an Address Group.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address|string|None|True|The Address Object name to check. If Enable Search is set to true then we search the addresses (IP, CIDR, doman) within the address object instead of matching the name|None|198.51.100.100|
|device_name|string|localhost.localdomain|True|Device name|None|localhost.localdomain|
|enable_search|boolean|False|True|When enabled, the Address input will accept a IP, CIDR, or domain name to search across the available Address Objects in the system. This is useful when you don’t know the Address Object by its name|None|False|
|group|string|None|True|Group name|None|ICON Block List|
|virtual_system|string|vsys1|True|Virtual system name|None|vsys1|

Example input:

```
{
  "address": "198.51.100.100",
  "device_name": "localhost.localdomain",
  "enable_search": false,
  "group": "ICON Block List",
  "virtual_system": "vsys1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|address_object_names|[]string|False|The names of the address objects that match or contain address|
|found|boolean|True|Was address found in group|

Example output:

```
```

#### Get Policy

This action is used to get a policy.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|device_name|string|localhost.localdomain|True|Device name|None|localhost.localdomain|
|policy_name|string|None|True|Policy name|None|InsightConnect Block List|
|virtual_system|string|vsys1|True|Virtual system name|None|vsys1|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|action|string|False|Action|
|application|[]string|False|Application|
|category|[]string|False|Category|
|destination|[]string|False|Destination|
|from|[]string|False|From|
|hip_profiles|[]string|False|Host Information in Policy Enforcement profile|
|service|[]string|False|Service|
|source|[]string|False|Source|
|source_user|[]string|False|Source user|
|to|[]string|False|To|

Example output:

```
{
  "to": [
    "any"
  ],
  "from": [
    "any"
  ],
  "source": [
    "1.1.1.1",
    "1.1.1.2"
  ],
  "destination": [
    "any"
  ],
  "source_user": [
    "any"
  ],
  "category": [
    "any"
  ],
  "application": [
    "any"
  ],
  "service": [
    "application-default"
  ],
  "hip_profiles": [
    "any"
  ],
  "action": "drop"
}
```

#### Create Address Object

This action is used to create a new address object. It will accept an IP, CIDR, Fully Qualified Domain Name (FQDN), 
or IP range E.g. 10.1.1.1, 192.168.1.0/24, 10.1.1.1-10.1.1.9, or www.example.com.

This action supports a whitelist as a safety check to prevent users from blocking explicitly stated hosts.
If the action encounters a host or network matched in the whitelist, the action will succeed but skip blocking the entry.

The whitelist accepts one or more of any combination of IP addresses, CIDR addresses, and domains e.g. 
["10.1.1.2", "192.168.1.0/24", "www.example.com"]. Note that the whitelist does not support IP ranges, they will not be 
checked against the whitelist of objects.  An additional note is that the whitelist supports matching against CIDRs exactly but will 
not check if a CIDR is within a larger CIDR network. The exception to this rule is if a CIDR is expressed as 1.1.1.1/32. 
In this case, we will strip the /32 from the end and check the IP against the whitelist or the exact CIDR match.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|address_object|string|None|True|The IP address, network CIDR, or FQDN e.g. 192.168.1.1, 192.168.1.0/24, google.com google.com|None|1.1.1.1|
|object_description|string|None|False|A description for the address object|None|Blocked host from Insight Connect|
|object_name|string|None|True|The name of the address object|None|Blocked host|
|tags|string|None|False|Tags for the address object. Use commas to separate multiple tags|None|malware|
|whitelist|[]string|None|False|This list contains a set of network objects that should not be blocked. This can include IPs, CIDR notation, or domains. It can not include an IP range (such as 10.0.0.0-10.0.0.10)|None|['198.51.100.100', '192.0.2.0/24', 'example.com']|

Example input:

```
{
  "address_object": "1.1.1.1",
  "object_description": "Blocked host from Insight Connect",
  "object_name": "Blocked host",
  "tags": "malware",
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
|code|string|False|Response code from PAN-OS|
|message|string|False|A message with more detail about the status|
|status|string|False|The status of the requested operation e.g. success, error, etc|

Example output:

```
{
  "message": "command succeeded",
  "status": "success",
  "code": "20"
}
```

#### Set Security Policy Rule

This action is used to create a new security policy rule.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|None|True|Action that will occur if an event meets the rule definitions|None|None|
|application|string|None|True|Applications for which this rule will be applied e.g. adobe-cloud, dropbox,  any|None|None|
|description|string|None|True|Description of the rule and what it does|None|None|
|destination|string|None|True|Destinations for which this rule will be applied e.g. 10.0.0.1, computername, any|None|None|
|disable_server_response_inspection|boolean|None|True|If true, PAN-OS will not inspect this traffic|None|None|
|disabled|boolean|None|True|If true, rule is disabled|None|None|
|dst_zone|string|None|True|Zone which the traffic is going to e.g. server zone, any|None|None|
|log_end|boolean|None|True|Generates a traffic log entry for the end of a session|None|None|
|log_start|boolean|None|True|Generates a traffic log entry for the start of a session|None|None|
|negate_destination|boolean|None|True|Negate destination|None|None|
|negate_source|boolean|None|True|Negate source|None|None|
|rule_name|string|None|True|Name of the rule|None|None|
|service|string|None|True|Service type for which this rule will be applied e.g. HTTP, HTTPS, any|None|None|
|source|string|None|True|Sources for which this rule will be applied e.g. 10.0.0.1, computername, any|None|None|
|source_user|string|None|True|User that the network traffic originated from e.g. Joe Smith, any|None|None|
|src_zone|string|None|True|Zone in which the traffic originated e.g. server zone, any|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|config|False|Response from PAN-OS|

Example output:

```
{
  "response": {
    "@status": "success",
    "@code": "20",
    "msg": "command succeeded"
  }
}

```

#### Set

This action is used to create a new object.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|element|string|None|True|XML representation of the object to be created|None|None|
|xpath|string|None|True|Xpath location to create the new object|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|object|False|Response from PAN-OS|

Example output:

```
{
  "response": {
    "@status": "success",
    "@code": "20",
    "msg": "command succeeded"
  }
}

```

#### Get

This action is used to get candidate configuration.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|xpath|string|None|True|Xpath targeting the requested portion of the configuration|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|config|False|Response from PAN-OS|

Example output:

```
{
  "response": {
    "@status": "success",
    "@code": "19",
    "result": {
      "-total-count": "2",
      "-count": "2",
      "entry": [
       {
          "-name": "intrazone-default",
          "-__recordInfo": "{\"permission\":\"readonly\",\"xpathId\":\"predefined\",\"position\":\"default-security-rule\"}",
          "action": "allow",
          "log-start": "no",
          "log-end": "no"
        },
        {
          "-name": "interzone-default",
          "-__recordInfo": "{\"permission\":\"readonly\",\"xpathId\":\"predefined\",\"position\":\"default-security-rule\"}",
          "action": "deny",
          "log-start": "no",
          "log-end": "no"
        }
      ]
    }
  }
}

```

#### Edit

This action is used to edit an existing object.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|element|string|None|True|XML representation of the updated object. This replaces the previous object entirely, any unchanged attributes must be restated|None|None|
|xpath|string|None|True|Xpath location of the object to edit|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|object|False|Response from PAN-OS|

Example output:

```
{
  "response": {
    "@status": "success",
    "@code": "20",
    "msg": "command succeeded"
  }
}

```

#### Show

This action is used to get an active configuration.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|xpath|string|None|True|Xpath targeting the requested portion of the configuration|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|config|False|Response from PAN-OS|

Example output:

```
{
  "response": {
    "@status": "success",
    "result": {
      "system": {
        "hostname": "firewall",
        "ip-address": "10.27.0.8",
        "netmask": "255.255.254.0",
        "default-gateway": "10.27.0.1",
        "is-dhcp": "no",
        "ipv6-address": "unknown",
        "ipv6-link-local-address": "fe80::21b:17dd:dedf:c04a/64",
        "mac-address": "00:1b:17:ff:c0:4a",
        "time": "Wed Feb 10 13:03:32 2016",
        "uptime": "1 days, 19:35:51",
        "devicename": "firewall",
        "family": "3000",
        "model": "PA-3020",
        "serial": "001901000114",
        "sw-version": "7.1.",
        "global-protect-client-package-version": "2.0.0",
        "app-version": "557-3138",
        "app-release-date": "2016/02/09  16:56:02",
        "av-version": "2261-2700",
        "av-release-date": "2016/02/09  15:26:53",
        "threat-version": "557-3138",
        "threat-release-date": "2016/02/09  16:56:02",
        "wf-private-version": "0",
        "wf-private-release-date": "unknown",
        "url-db": "paloaltonetworks",
        "wildfire-version": "27518-28208",
        "wildfire-release-date": "2016/01/08  11:08:16",
        "url-filtering-version": "2016.01.08.407",
        "global-protect-datafile-version": "1452328885",
        "global-protect-datafile-release-date": "2016/01/09 08:41:25",
        "logdb-version": "7.0.9",
        "platform-family": "3000",
        "vpn-disable-mode": "off",
        "multi-vsys": "on",
        "operational-mode": "normal"
      }
    }
  }
}

```

#### Retrieve Logs

This action is used to query firewall logs.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|count|integer|20|False|Number of logs to retrieve (Max: 500, Default: 20)|None|None|
|direction|string|None|False|Order in which to return the logs|['backward', 'forward']|None|
|filter|string|None|False|Search query. Format as a log filter expression|None|None|
|interval|float|0.5|False|Time interval in seconds to wait between queries for commit job completion (Default: 0.5)|None|None|
|log_type|string|None|False|Type of log to retrieve|['config', 'hipmatch', 'system', 'threat', 'traffic', 'url', 'wildfire']|None|
|max_tries|integer|25|False|Maximum number of times to poll for job completion before timing out (Default: 25)|None|None|
|skip|integer|0|False|Log retrieval offset, number of entries to skip, (Default: 0)|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|log|False|Response from PAN-OS|

Example output:

```
{
  "response": {
    "@status": "success",
    "result": {
      "job": {
        "tenq": "17:32:53",
        "tdeq": "17:32:53",
        "tlast": "17:32:53",
        "status": "FIN",
        "id": "1466",
        "cached-logs": "0"
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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|log|False|Response from PAN-OS|

#### Commit

This action is used to commit the candidate configuration.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|all|False|Commit action (Default: 'all')|None|None|
|cmd|string|None|True|XML specifying any commit arguments|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|object|False|Response from PAN-OS|

Example output:

```
{
  "response": {
    "@status": "success",
    "@code": "19",
    "result": {
      "msg": { "line": "Commit job enqueued with jobid 152" },
      "job": "152"
    }
  }
}

```

#### Delete

This action is used to delete an object.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|xpath|string|None|True|Xpath targeting the object to delete|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|config|False|Response from PAN-OS|

Example output:

```
{
  "response": {
    "@status": "success",
    "@code": "20",
    "msg": "command succeeded"
  }
}

```

#### Op

This action is used to run operational command.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|cmd|string|None|False|XML specifying operation to be completed|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|object|False|Response from PAN-OS|

Example output:

```
{
  "response": {
    "@status": "success",
    "result": {
    }
  }
}

```

#### Add to Policy

This action is used to add a rule to a PAN-OS security policy.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|None|False|Action that will occur if an event meets the rule definitions|None|None|
|application|string|None|False|Application for which this rule will be applied e.g. adobe-cloud, dropbox, or  any|None|None|
|destination|string|None|False|A destination for which this rule will be applied e.g. 10.0.0.1, computername, or any|None|None|
|dst_zone|string|None|False|Zone which the traffic is going to e.g. server zone, or any|None|None|
|hip_profiles|string|None|False|Host information profile|None|None|
|rule_name|string|None|True|Name of the rule|None|None|
|service|string|None|False|Service type for which this rule will be applied e.g. HTTP, HTTPS, or any|None|None|
|source|string|None|False|A source for which this rule will be applied e.g. 10.0.0.1, computername, or any|None|None|
|source_user|string|None|False|User that the network traffic originated from e.g. Joe Smith, or any|None|None|
|src_zone|string|None|False|Zone in which the traffic originated e.g. server zone, or any|None|None|
|update_active_or_candidate_configuration|string|None|True|Will apply the update to the active or candidate configuration. If active is chosen any uncommitted candidate configuration will be lost|['active', 'candidate']|None|
|url_category|string|None|False|The URL category e.g. adult|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|code|string|False|Response code from PAN-OS|
|message|string|False|A message with more detail about the status|
|status|string|False|Status of the requested operation e.g. success, error, etc|

Example output:

```
{
  "status": "success",
  "code": "20",
  "message": "command succeeded"
}
```

#### Remove from Policy

This action is used to remove a rule from a PAN-OS security policy.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|None|False|The action that will occur if an event meets the rule definitions|None|None|
|application|string|None|False|Application for which this rule will be applied e.g. adobe-cloud, dropbox, or any|None|None|
|destination|string|None|False|A Destination for which this rule will be applied e.g. 10.0.0.1, computername, or any|None|None|
|dst_zone|string|None|False|Zone which the traffic is going to e.g. server zone, or any|None|None|
|hip_profiles|string|None|False|Host information profile|None|None|
|rule_name|string|None|True|Name of the rule|None|None|
|service|string|None|False|Service type for which this rule will be applied e.g. HTTP, HTTPS, any|None|None|
|source|string|None|False|A source for which this rule will be applied e.g. 10.0.0.1, computername, or any|None|None|
|source_user|string|None|False|User that the network traffic originated from e.g. Joe Smith, or any|None|None|
|src_zone|string|None|False|Zone in which the traffic originated e.g. server zone, or any|None|None|
|update_active_or_candidate_configuration|string|None|True|Will apply the update to the active or candidate configuration. If active is chosen any uncommitted candidate configuration will be lost|['active', 'candidate']|None|
|url_category|string|None|False|The URL category e.g. adult|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|code|string|False|Response code from PAN-OS|
|message|string|False|A message with more detail about the status|
|status|string|False|Status of the requested operation e.g. success, error, etc|

Example output:

```
{
  "status": "success",
  "code": "20",
  "message": "command succeeded"
}

```

#### Add External Dynamic List

This action is used to add an external dynamic list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|day|string||True|If repeat is weekly, choose a day to update|['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']|None|
|description|string|None|True|A description of the list|None|None|
|list_type|string|None|True|The type of list|['IP List', 'Domain List', 'URL List']|None|
|name|string|None|True|An arbitrary name for the list. This name will be used to identify the list in PAN-OS|None|None|
|repeat|string|None|True|The interval at which to retrieve updates from the list|['Five Minute', 'Hourly', 'Daily', 'Weekly']|None|
|source|string|None|True|The web site you will pull the list from e.g. https://www.example.com/test.txt|None|None|
|time|string||True|If repeat is daily or weekly, choose an hour on a 24 hour clock to update (Default: '')|['', '00', '01', '02', '03', '04', '05', '06', '07', 8, 9, '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|code|string|False|Response code from PAN-OS|
|message|string|False|A message with more detail about the status|
|status|string|False|The status of the requested operation e.g. success, error, etc|

Example output:

```
{
    "status": "success",
    "code": "20",
    "message": "command succeeded"
}
```

### Triggers

_This plugin does not contain any triggers._

### Troubleshooting

For the URL, include `https://` e.g. `https://10.0.0.1` or `https://myfirewall`.

When using the Add External Dynamic List action, a day and time must be chosen even if they are not used.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

For the URL, include `https://` e.g. `https://10.0.0.1` or `https://myfirewall`.

When using the Add External Dynamic List action, a day and time must be chosen even if they are not used.

# Version History

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

## References

* [Palo Alto PAN-OS](https://www.paloaltonetworks.com/documentation/80/pan-os)
* [Palo Alto PAN-OS API](https://www.paloaltonetworks.com/documentation/80/pan-os/xml-api)
