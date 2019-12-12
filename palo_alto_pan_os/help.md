# Description

[PAN-OS](https://www.paloaltonetworks.com/documentation/80/pan-os) is a management console for 
Palo Alto Networks devices. Use this plugin within a workflow to manage configurations, security policies, and more.

This plugin utilizes the [PAN-OS API](https://www.paloaltonetworks.com/documentation/80/pan-os/xml-api).

# Key Features

* Manage Palo Alto Networks devices
* Manage configurations

# Requirements

* PAN-OS credentials

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|True|Username and password|None|
|verify_cert|boolean|None|True|If true, validate the server's TLS certificate when contacting PAN-OS over HTTPS|None|
|server|string|None|True|URL pointing to instance of PAN-OS|None|

## Technical Details

### Actions

#### Set Security Policy Rule

This action is used to create a new security policy rule.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|negate_source|boolean|None|True|Negate source|None|
|description|string|None|True|Description of the rule and what it does|None|
|disabled|boolean|None|True|If true, rule is disabled|None|
|rule_name|string|None|True|Name of the rule|None|
|src_zone|string|None|True|Zone in which the traffic originated e.g. server zone, any|None|
|negate_destination|boolean|None|True|Negate destination|None|
|dst_zone|string|None|True|Zone which the traffic is going to e.g. server zone, any|None|
|log_start|boolean|None|True|Generates a traffic log entry for the start of a session|None|
|disable_server_response_inspection|boolean|None|True|If true, PAN-OS will not inspect this traffic|None|
|service|string|None|True|Service type for which this rule will be applied e.g. HTTP, HTTPS, any|None|
|source|string|None|True|Sources for which this rule will be applied e.g. 10.0.0.1, computername, any|None|
|destination|string|None|True|Destinations for which this rule will be applied e.g. 10.0.0.1, computername, any|None|
|source_user|string|None|True|User that the network traffic originated from e.g. Joe Smith, any|None|
|application|string|None|True|Applications for which this rule will be applied e.g. adobe-cloud, dropbox,  any|None|
|action|string|None|True|Action that will occur if an event meets the rule definitions|None|
|log_end|boolean|None|True|Generates a traffic log entry for the end of a session|None|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|xpath|string|None|True|Xpath location to create the new object|None|
|element|string|None|True|XML representation of the object to be created|None|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|xpath|string|None|True|Xpath targeting the requested portion of the configuration|None|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|xpath|string|None|True|Xpath location of the object to edit|None|
|element|string|None|True|XML representation of the updated object. This replaces the previous object entirely, any unchanged attributes must be restated|None|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|xpath|string|None|True|Xpath targeting the requested portion of the configuration|None|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|count|integer|20|False|Number of logs (nlogs) to retrieve (Max 500), (Default\: 20)|None|
|filter|string|None|False|Search query. Format as a log filter expression|None|
|direction|string|None|False|Order in which to return the logs|['backward', 'forward']|
|max_tries|integer|25|False|Maximum number of times to poll for job completion before timing out (Default\: 25)|None|
|skip|integer|0|False|Log retrieval offset, number of entries to skip (Default\: 0)|None|
|interval|float|0.5|False|Time interval in seconds to wait between queries for commit job completion (Default\: 0.5)|None|
|log-type|string|None|False|Type of log to retrieve|['config', 'hipmatch', 'system', 'threat', 'traffic', 'url', 'wildfire']|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|action|string|commit-all|False|Commit action. (Default: 'commit-all')|None|
|cmd|string|None|True|XML specifying any commit arguments|None|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|xpath|string|None|True|Xpath targeting the object to delete|None|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cmd|string|None|False|XML specifying operation to be completed|None|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|rule_name|string|None|True|Name of the rule|None|
|update_active_or_candidate_configuration|string|None|True|Will apply the update to the active or candidate configuration. If active is chosen any uncommitted candidate configuration will be lost|['active', 'candidate']|
|source|string|None|False|A source for which this rule will be applied e.g. 10.0.0.1, computername, or any|None|
|destination|string|None|False|A destination for which this rule will be applied e.g. 10.0.0.1, computername, or any|None|
|service|string|None|False|Service type for which this rule will be applied e.g. HTTP, HTTPS, or any|None|
|application|string|None|False|Application for which this rule will be applied e.g. adobe-cloud, dropbox, or  any|None|
|source_user|string|None|False|User that the network traffic originated from e.g. Joe Smith, or any|None|
|src_zone|string|None|False|Zone in which the traffic originated e.g. server zone, or any|None|
|dst_zone|string|None|False|Zone which the traffic is going to e.g. server zone, or any|None|
|url_category|string|None|False|The URL category e.g. adult|None|
|hip_profiles|string|None|False|Host information profile|None|
|action|string|None|False|Action that will occur if an event meets the rule definitions|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|config|False|Response from PAN-OS|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|rule_name|string|None|True|Name of the rule|None|
|update_active_or_candidate_configuration|string|None|True|Will apply the update to the active or candidate configuration. If active is chosen any uncommitted candidate configuration will be lost|['active', 'candidate']|
|source|string|None|False|A source for which this rule will be applied e.g. 10.0.0.1, computername, or any|None|
|destination|string|None|False|A Destination for which this rule will be applied e.g. 10.0.0.1, computername, or any|None|
|service|string|None|False|Service type for which this rule will be applied e.g. HTTP, HTTPS, any|None|
|application|string|None|False|Application for which this rule will be applied e.g. adobe-cloud, dropbox, or any|None|
|source_user|string|None|False|User that the network traffic originated from e.g. Joe Smith, or any|None|
|src_zone|string|None|False|Zone in which the traffic originated e.g. server zone, or any|None|
|dst_zone|string|None|False|Zone which the traffic is going to e.g. server zone, or any|None|
|url_category|string|None|False|The URL category e.g. adult|None|
|hip_profiles|string|None|False|Host information profile|None|
|action|string|None|False|The action that will occur if an event meets the rule definitions|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|config|False|Response from PAN-OS|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|source|string|None|True|The web site you will pull the list from e.g. http\://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt|None|
|repeat|string|None|True|The interval at which to retrieve updates from the list|['Five Minute', 'Hourly', 'Daily', 'Weekly']|
|name|string|None|True|An arbitrary name for the list. This name will be used to identify the list in PAN-OS|None|
|list_type|string|None|True|The type of list|['IP List', 'Domain List', 'URL List']|
|time|string|None|True|If repeat is daily or weekly, choose an hour on a 24 hour clock to update (Default\: '')|['', '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']|
|day|string|None|True|If repeat is weekly, choose a day to update|['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']|
|description|string|None|True|A description of the list|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|The status of the requested operation e.g. success, error, etc|
|message|string|False|A message with more detail about the status|
|code|string|False|Response code from PAN-OS|

Example output:

```
{
    "status": "success",
    "code": "20",
    "message": "command succeeded"
}
```

#### Set Address Object

This action is used to create a new address object.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|string|None|True|The IP-Netmask, IP-Range, or FQDN e.g. 192.168.1.0/24, 10.0.0.1-10.0.0.12, google.com|None|
|type|string|None|True|The type of address object to create|['IP-Netmask', 'IP-Range', 'FQDN']|
|object_name|string|None|True|The name of the address object|None|
|object_description|string|None|False|A description for the address object|None|
|tags|string|None|False|Tags for the address object. Use commas to separate multiple tags|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|The status of the requested operation e.g. success, error, etc|
|code|string|False|Response code from PAN-OS|
|message|string|False|A message with more detail about the status|

Example output:

```
{
  "message": "command succeeded",
  "status": "success",
  "code": "20"
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

* 1.5.5 - New spec and help.md format for the Hub
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
