# Description

[SonicWall Capture Client](https://www.sonicwall.com/products/firewalls/security-services/capture-client/) is a unified client platform that delivers multiple endpoint protection capabilities, including next-generation malware protection and application vulnerability intelligence.

# Key Features

* Get agent details

# Requirements

* E-mail address and password for SonicWall Capture Client

# Documentation
## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Email address and password|None|{"username": "admin", "password": "mypassword"}|

Example input:

```
{
  "credentials": {
    "username": "user@example.com", 
    "password": "mypassword"
  }
}
```
## Technical Details

### Actions

#### Get Agent Details

This action is used to get details for an agent.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent|string|None|True|Agent to retrieve device information from. Accepts IP address, MAC address, hostname, or device ID|None|198.51.100.100|

Example input:

```
{
  "agent": "198.51.100.100"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agent_information|agent_information|True|Information about an agent|

Example output:

```

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### activeDirectory

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Computer Member of|[]object|False|Computer member of|
|Last User Member of|[]object|False|Last user member of|

#### agentPolicySettings

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|ID|
|Add to Keychain|boolean|False|Add to keychain|
|Add to Windows Store|boolean|False|Add to windows store|
|Certificates|[]object|False|Certificates|
|Firefox Store MAC|string|False|Firefox store MAC|
|Firefox Store Windows|string|False|Firefox store windows|
|Keep After Uninstall Client|boolean|False|Keep after uninstall client|

#### agent_information

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Active Directory|activeDirectory|False|Active directory|
|Active Threats|integer|False|Active threats|
|Agent Version|string|False|Agent version|
|Alerts|[]object|False|Alerts|
|Applications|[]applications|False|Applications|
|Client State|string|False|Client state|
|Client State TS|integer|False|Clientstate TS|
|Client Version|string|False|Client version|
|Created At|string|False|Created at|
|Current Firewall SN|string|False|Current firewall SN|
|Current User|string|False|Current user|
|Device ID|string|False|Device ID|
|Device Settings TS|integer|False|Device settings TS|
|Device Type|string|False|Device type|
|Domain|string|False|Domain|
|Encrypted Applications|boolean|False|Encrypted applications|
|Enforced Policy|[]enforcedPolicy|False|Enforced policy|
|External IP|string|False|Externali IP|
|Firewall Protection Mode|string|False|Firewall protection mode|
|GEO Location|geoLocation|False|GEO Location|
|Groups|[]object|False|Groups|
|HW Model|string|False|HW model|
|Infected|boolean|False|Infected|
|Install Token|string|False|Install token|
|IP|string|False|IP|
|Is Active|boolean|False|Is active|
|Is Mobile|boolean|False|Is mobile|
|Is Pending Uninstall|boolean|False|Is pending uninstall|
|Last Policy ID|string|False|Last policy ID|
|Last Policy Update TS|integer|False|Last policy update TS|
|Licenses|[]licenses|False|Licenses|
|Local IP|string|False|Local IP|
|Location|location|False|Location|
|Location TS|integer|False|Location TS|
|MAC Address|string|False|MAC address|
|Mitigation Mode|string|False|Mitigation mode|
|Mitigation Mode Suspicious|string|False|Mitigation mode suspicious|
|Name|string|False|Name|
|Network|network|False|Network|
|Network Status|string|False|Network status|
|Online Status|string|False|Online status|
|OS|string|False|OS|
|OS Version|string|False|OS version|
|Process TS|integer|False|Process TS|
|Processes|[]processes|False|Processes|
|Processor Type|string|False|Processor type|
|Release GUIDS|[]object|False|Release GUIDS|
|S1 Agent ID|string|False|S1 agent ID|
|S1 Group ID|string|False|S1 group ID|
|S1 Passphrase|string|False|S1 passphrase|
|S1 Passphrase TS|integer|False|S1 passphrase TS|
|Scan Aborted At|string|False|Scan aborted at|
|Scan Finished At|string|False|Scan finished at|
|Scan Started At|string|False|Scan started at|
|Scan Status|string|False|Scan status|
|Scan Status TS|integer|False|Scan status TS|
|Server Type|string|False|Server type|
|Telemetry TS|integer|False|Telemetry TS|
|Tenant|tenant|False|Tenant|
|Timezone Name|string|False|Timezone name|
|Timezone Offset|string|False|Timezone offset|
|Uninstall PWD|string|False|Uninstall PWD|
|Updated At|string|False|Updated at|
|User ctions Needed|[]object|False|User actions needed|
|Users|[]users|False|Users|

#### applications

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Installed Date|string|False|Installed date|
|Name|string|False|Name|
|Publisher|string|False|Publisher|
|Size|integer|False|Size|
|Version|string|False|Version|

#### enforcedPolicy

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|ID|
|Policy|policy|False|Policy|
|Policy TS|integer|False|Policy TS|
|Type|string|False|Type|

#### geoLocation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Coordinates|[]float|False|Coordinates|
|Type|string|False|Type|

#### interfaces

|Name|Type|Required|Description|
|----|----|--------|-----------|
|DNS Servers|[]string|False|DNS Servers|
|IPv4 Addresses|[]string|False|IPv4 addresses|
|IPv6 Addresses|[]string|False|IPv6 addresses|
|MAC Address|string|False|MAC address|
|Name|string|False|Name|

#### licenses

|Name|Type|Required|Description|
|----|----|--------|-----------|
|V|integer|False|V|
|ID|string|False|ID|
|Created At|string|False|Created at|
|Expiration|integer|False|Expiration|
|Level|string|False|Level|
|License ID|string|False|License ID|
|NB Available|integer|False|NB available|
|NB Total|integer|False|NB total|
|Start Date|integer|False|Start date|
|Tenant|string|False|Tenant|
|Trial|boolean|False|Trial|
|Type|string|False|Type|
|Updated At|string|False|Updated at|
|Vendor|string|False|Vendor|

#### location

|Name|Type|Required|Description|
|----|----|--------|-----------|
|City|string|False|City|
|Country|string|False|Country|
|Countrycode|string|False|Countrycode|

#### network

|Name|Type|Required|Description|
|----|----|--------|-----------|
|V|integer|False|v|
|ID|string|False|ID|
|Device|string|False|Device|
|Interfaces|[]interfaces|False|Interfaces|
|Routes|[]routes|False|Routes|

#### policy

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Agent Policy Settings|agentPolicySettings|False|Agent policy settings|
|Enforced|boolean|False|Enforced|
|Name|string|False|Name|
|Policy ID|string|False|Policy ID|
|Policy TS|integer|False|Policy TS|
|Release GUID|string|False|Release GUID|
|Tenant|string|False|Tenant|
|Type|string|False|Type|
|Type Description|string|False|Type description|
|Uninstall|boolean|False|Uninstall|

#### processes

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Description|string|False|Description|
|Executable Path|string|False|Executable path|
|Memory Usage|integer|False|Memory usage|
|PID|integer|False|PID|
|Process Name|string|False|Process name|
|Start Time|integer|False|Start time|
|Version|string|False|Version|

#### routes

|Name|Type|Required|Description|
|----|----|--------|-----------|
|DST|string|False|DST|
|Gateway|string|False|Gateway|
|Interface|string|False|Interface|

#### tenant

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|ID|
|S1 Settings|string|False|S1 settings|
|Tenant ID|string|False|Tenant ID|
|Tenant Name|string|False|Tenant name|

#### tenant_0

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|ID|
|Tenant ID|string|False|Tenant ID|
|Tenant Name|string|False|Tenant Name|

#### users

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Full Name|string|False|Full name|
|Policies|[]object|False|Policies|
|Tenant|tenant_0|False|Tenant|
|User Groups|[]object|False|User groups|
|User ID|string|False|User ID|
|Username|string|False|Username|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [SonicWall Capture Client](https://www.sonicwall.com/products/firewalls/security-services/capture-client/)
