# Description

The [Open Vulnerability Assessment System](http://openvas.org/about.html) is an automated
scanning tool that can check network reachable services for common and publicly published
security vulnerabilities. This OpenVAS plugin allows Komand users to perform common tasks such as
starting, stopping, deleting and scheduling scans from an OpenVAS server. To use this plugin, one
should have a reachable OpenVAS server somewhere on the same network as the Komand server, and
the OpenVAS management port should be accessible by the Komand server. If the `ssl_verify` option
is set in the plugin connection, the Komand server will check to ensure that the TLS/SSL
certificate presented by the service running on the management port is valid, using the operating
systems certificate store accessible to the python programming language.

The OpenVAS system uses 36 character long IDs to refer to many different objects managed in the
OpenVAS system, such as scans, targets, schedules, and port lists. Calls to the create_*
Komand Actions return a corresponding ID on success that can then be used in subsequent calls.
Alternatively, all of the various IDs can also be found in the OpenVAS Greenbone Security
Assistant UI.

This plugin also defines a custom "datetime" type, which is used when creating schedules for
scans to launch. Please note that the input given to the create_schedule function assumes that
the date given to the create_schedule function is given in the UTC timezone.

# Key Features

* Run vulnerability scans on networked services
* Schedule scans
* Get scan reports

# Requirements

* OpenVAS server
* Username and password

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|None|None|
|ssl_verify|boolean|False|False|Verify SSL Certificate|None|
|password|string|None|True|None|None|
|timeout|integer|10|False|Timeout to connect to server|None|
|server|string|127.0.0.1\:9390|True|OpenVAS Management Protocol Server URL (<host>\:<port>)|None|

## Technical Details

### Actions

#### Get Finished Scans

This action is used to get a list of all finished scans.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|list_scans|[]scan|False|JSON array containing the list of all finished scans|
|message|string|False|None|
|success|boolean|False|None|

#### Create Target

This action is used to create a new target in the OpenVAS server.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|port_list_id|string|None|False|ID of the Port List to use for scanning, if you want to scan a custom list of ports.|None|
|host_list|[]string|None|True|Target IP List, in the form of a JSON array for each host or list of hosts. CIDR notation can be used. For example, the following would be a valid list\: ['192.168.0.101', '192.168.1.101,192.168.1.103,192.168.1.105','192.168.1.2/24','192.168.3.105-112']|None|
|name|string|None|True|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|
|target_id|string|False|None|
|success|boolean|False|None|

#### Get Running Scans

This action is used to get a list of all currently running scans.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|list_scans|[]scan|False|JSON array containing the list of all running scans|
|message|string|False|None|
|success|boolean|False|None|

#### Delete Scan

This action is used to delete a specified scan ID in the OpenVAS server.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|scan_id|string|None|True|Scan ID E.g. 9a849831-23a0-48ba-8e8f-a3deeaa45f7e|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|
|success|boolean|False|None|

#### Get Report HTML

This action is used to get the HTML version of the report for a particular scan.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|scan_id|string|None|True|Scan ID E.g. 9a849831-23a0-48ba-8e8f-a3deeaa45f7e|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report|string|False|HTML output of report|
|message|string|False|None|
|success|boolean|False|None|

#### Launch Scan

This action is used to launch a new audit in OpenVAS.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|profile|string|None|True|Scan profile in the OpenVAS server E.g. Full and fast|None|
|target|string|None|True|If only one IP address is to be scanned, the IP can be passed directly through this parameter. Otherwise, a target ID can be passed from the Create Target functionality|None|
|schedule|string|None|False|schedule id to use for the scan|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan_id|string|False|None|
|target_id|string|False|None|
|message|string|False|None|
|success|boolean|False|None|

#### Create Schedule

This action is used to create a schedule to run a scan on.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|duration|integer|None|False|How long the Manager will run the scheduled task for, in hours|None|
|first_time|datetime|None|True|The first time the schedule will run, in UTC timezone|None|
|name|string|None|True|None|None|
|period|integer|None|False|How often the Manager will repeat the scheduled task, in days|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|schedule_id|string|False|None|
|message|string|False|None|
|success|boolean|False|None|

#### Get Scan Configurations

This action is used to get a list of all scan configurations in the OpenVAS server.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|
|list_scan_configs|[]scan|False|JSON array containing the list of all scan configurations|
|success|boolean|False|None|

#### Stop Scan

This action is used to stop a scan by the specified scan ID in the OpenVAS server.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|scan_id|string|None|True|Scan ID E.g. 9a849831-23a0-48ba-8e8f-a3deeaa45f7e|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|
|success|boolean|False|None|

#### Get Report XML

This action is used to get the XML version of the report for a particular scan.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|scan_id|string|None|True|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report|string|False|XML output of report|
|message|string|False|None|
|success|boolean|False|None|

#### Create Port List

This action is used to create a new list of ports to scan in the OpenVAS server.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|port_list_TCP|[]string|None|False|Target Port List for TCP ports, in the form of a JSON array for each port or list of ports. For example, the following would be a valid list\: ['22', '80','443-445']|None|
|name|string|None|True|None|None|
|port_list_UDP|[]string|None|False|Target Port List for UDP ports, in the form of a JSON array for each port or list of ports. For example, the following would be a valid list\: ['53', '6881-6890']|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|port_list_id|string|False|None|
|message|string|False|None|
|success|boolean|False|None|

#### Delete Target

This action is used to delete specified target ID in the OpenVAS server.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|target_id|string|None|True|None|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|False|None|
|success|boolean|False|None|

#### Get All Scans

This action is used to get a list of all scans in the OpenVAS server.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|list_scans|[]scan|False|JSON array containing the list of all running scans|
|message|string|False|None|
|success|boolean|False|None|

#### Scan Status

This action is used to get the status of scan by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|scan_id|string|None|True|Scan ID E.g. 9a849831-23a0-48ba-8e8f-a3deeaa45f7e|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|None|
|message|string|False|None|
|success|boolean|False|None|

### Triggers

#### Check Scan Done

This trigger is used to poll a scan by ID for completion.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|scan_id|string|None|True|Scan ID E.g. 9a849831-23a0-48ba-8e8f-a3deeaa45f7e|None|
|poll|float|3|False|Length of time to wait between polling (in minutes)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan_finished|boolean|False|None|

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Example](https://example.com)
* [Example API](http://docs.example.com)
