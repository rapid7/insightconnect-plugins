# Description

The [VMware Carbon Black Cloud](https://www.carbonblack.com/products/vmware-carbon-black-cloud/) is a cloud-native endpoint protection platform (EPP) that combines the intelligent system hardening and behavioral prevention needed to keep emerging threats at bay, using a single lightweight agent and an easy-to-use console. Manage and contain threats on your Carbon Black endpoints using this plugin

# Key Features

* Get device information
* Quarantine a device

# Requirements

* API Credentials
* Base URL

# Supported Product Versions

* 2026-03-02

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_id|string|None|True|API ID|None|ADFF2QLIIZ|APP ID|Enter the API ID from your Carbon Black Account.|
|api_secret_key|credential_secret_key|None|True|API secret key|None|Z1PXFRDZI321LXQVAB9IJKKZ|API Secret Key|Enter your Carbon Black Cloud API Secret Key.|
|org_key|string|None|True|Organization Key|None|1ABZY2FJ|Org Key|Enter the Carbon Black Cloud Org Key. To obtain the Org Key, log in to your Carbon Black Cloud account and go to Settings > API Access > API Keys.|
|url|string|defense.conferdeploy.net|True|The Carbon Black Cloud URL you use. You can find this by looking at the web address of your Carbon Black Cloud console|["defense-eap01.conferdeploy.net", "dashboard.confer.net", "defense.conferdeploy.net", "defense-prod05.conferdeploy.net", "defense-eu.conferdeploy.net", "defense-prodnrt.conferdeploy.net", "defense-prodsyd.conferdeploy.net", "ew2.carbonblackcloud.vmware.com", "gprd1usgw1.carbonblack-us-gov.vmware.com"]|defense.conferdeploy.net|URL|To determine which URL to select, login to your Carbon Black Cloud account and refer to the URL displayed in the address bar.|

Example input:

```
{
  "api_id": "ADFF2QLIIZ",
  "api_secret_key": "Z1PXFRDZI321LXQVAB9IJKKZ",
  "org_key": "1ABZY2FJ",
  "url": "defense.conferdeploy.net"
}
```

## Technical Details

### Actions


#### Get Agent Details

This action is used to get agent details

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|True|Agent to retrieve device information from. Accepts IP address, hostname, or device ID. Search results are case-sensitive|None|198.51.100.100|None|None|
  
Example input:

```
{
  "agent": "198.51.100.100"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|agent|agent|False|Details about the agent|{"adGroupId":0,"policyOverride":false,"currentSensorPolicyName":null,"deviceMetaDataItemList":null,"lastDevicePolicyRequestedTime":null,"lastDevicePolicyChangedTime":null,"lastPolicyUpdatedTime":null,"loginUserName":null,"messages":null,"lastReportedTime":1591962280381,"uninstallCode":null,"organizationId":1105,"deviceId":3466056,"createTime":null,"deviceGuid":null,"email":"user@example.com","deviceSessionId":null,"deviceType":"WINDOWS","assignedToId":null,"assignedToName":null,"lastName":"User","firstName":"Test","middleName":null,"deviceOwnerId":12345,"activationCode":"1A2B3C","targetPriorityType":"HIGH","organizationName":"example.com","sensorVersion":"3.5.0.1680","activationCodeExpiryTime":1234567891011,"sensorKitType":null,"osVersion":"Server 2012 x64","registeredTime":1234567891011,"lastContact":1234567891011,"windowsPlatform":null,"vdiBaseDevice":null,"avStatus":["AV_ACTIVE","ONDEMAND_SCAN_DISABLED"],"deregisteredTime":null,"sensorStates":["ACTIVE","LIVE_RESPONSE_NOT_RUNNING","LIVE_RESPONSE_NOT_KILLED","LIVE_RESPONSE_ENABLED","SECURITY_CENTER_OPTLN_DISABLED"],"rootedBySensor":false,"rootedBySensorTime":null,"quarantined":false,"lastInternalIpAddress":"198.51.100.100","macAddress":"000000000000","lastExternalIpAddress":"198.51.100.100","lastLocation":"OFFSITE","sensorOutOfDate":false,"avUpdateServers":null,"passiveMode":false,"lastResetTime":0,"lastShutdownTime":0,"scanStatus":null,"scanLastActionTime":0,"scanLastCompleteTime":0,"linuxKernelVersion":null,"avEngine":"4.13.0.207-ave.8.3.60.40:avpack.8.5.0.60:vdf.8.18.2.56:apc.2.10.0.149","avProductVersion":"4.13.0.207","avAveVersion":"8.3.60.40","avPackVersion":"8.5.0.60","avVdfVersion":"8.18.2.56","avLastScanTime":0,"virtualMachine":false,"virtualizationProvider":"UNKNOWN","sensorPendingUpdate":false,"rootedByAnalytics":false,"rootedByAnalyticsTime":null,"avMaster":false,"firstVirusActivityTime":0,"lastVirusActivityTime":0,"testId":-1,"uninstalledTime":null,"encodedActivationCode":null,"originEventHash":null,"name":"example-host","status":"REGISTERED","policyId":12345,"policyName":"test"}|
  
Example output:

```
{
  "agent": {
    "activationCode": "1A2B3C",
    "activationCodeExpiryTime": 1234567891011,
    "adGroupId": 0,
    "assignedToId": null,
    "assignedToName": null,
    "avAveVersion": "8.3.60.40",
    "avEngine": "4.13.0.207-ave.8.3.60.40:avpack.8.5.0.60:vdf.8.18.2.56:apc.2.10.0.149",
    "avLastScanTime": 0,
    "avMaster": false,
    "avPackVersion": "8.5.0.60",
    "avProductVersion": "4.13.0.207",
    "avStatus": [
      "AV_ACTIVE",
      "ONDEMAND_SCAN_DISABLED"
    ],
    "avUpdateServers": null,
    "avVdfVersion": "8.18.2.56",
    "createTime": null,
    "currentSensorPolicyName": null,
    "deregisteredTime": null,
    "deviceGuid": null,
    "deviceId": 3466056,
    "deviceMetaDataItemList": null,
    "deviceOwnerId": 12345,
    "deviceSessionId": null,
    "deviceType": "WINDOWS",
    "email": "user@example.com",
    "encodedActivationCode": null,
    "firstName": "Test",
    "firstVirusActivityTime": 0,
    "lastContact": 1234567891011,
    "lastDevicePolicyChangedTime": null,
    "lastDevicePolicyRequestedTime": null,
    "lastExternalIpAddress": "198.51.100.100",
    "lastInternalIpAddress": "198.51.100.100",
    "lastLocation": "OFFSITE",
    "lastName": "User",
    "lastPolicyUpdatedTime": null,
    "lastReportedTime": 1591962280381,
    "lastResetTime": 0,
    "lastShutdownTime": 0,
    "lastVirusActivityTime": 0,
    "linuxKernelVersion": null,
    "loginUserName": null,
    "macAddress": "000000000000",
    "messages": null,
    "middleName": null,
    "name": "example-host",
    "organizationId": 1105,
    "organizationName": "example.com",
    "originEventHash": null,
    "osVersion": "Server 2012 x64",
    "passiveMode": false,
    "policyId": 12345,
    "policyName": "test",
    "policyOverride": false,
    "quarantined": false,
    "registeredTime": 1234567891011,
    "rootedByAnalytics": false,
    "rootedByAnalyticsTime": null,
    "rootedBySensor": false,
    "rootedBySensorTime": null,
    "scanLastActionTime": 0,
    "scanLastCompleteTime": 0,
    "scanStatus": null,
    "sensorKitType": null,
    "sensorOutOfDate": false,
    "sensorPendingUpdate": false,
    "sensorStates": [
      "ACTIVE",
      "LIVE_RESPONSE_NOT_RUNNING",
      "LIVE_RESPONSE_NOT_KILLED",
      "LIVE_RESPONSE_ENABLED",
      "SECURITY_CENTER_OPTLN_DISABLED"
    ],
    "sensorVersion": "3.5.0.1680",
    "status": "REGISTERED",
    "targetPriorityType": "HIGH",
    "testId": -1,
    "uninstallCode": null,
    "uninstalledTime": null,
    "vdiBaseDevice": null,
    "virtualMachine": false,
    "virtualizationProvider": "UNKNOWN",
    "windowsPlatform": null
  }
}
```

#### Quarantine

This action is used to quarantine an agent

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|True|Agent to retrieve device information from. Accepts IP address, hostname, or device ID. Search results are case-sensitive|None|198.51.100.100|None|None|
|quarantine_state|boolean|True|True|Set to true to quarantine the agent, set to false to unquarantine an agent|None|True|None|None|
|whitelist|[]string|None|False|An array of IPs, hostnames, or device ID that a user can pass in that will not be quarantined|None|["198.51.100.100", "win-test"]|None|None|
  
Example input:

```
{
  "agent": "198.51.100.100",
  "quarantine_state": true,
  "whitelist": [
    "198.51.100.100",
    "win-test"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|quarantined|boolean|True|Indicates whether or not the agent has been quarantined|True|
  
Example output:

```
{
  "quarantined": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**agent**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Activation Code|string|None|False|Activation code|None|
|Activation Code Expiry Time|integer|None|False|Activation code expiry time|None|
|AD Group ID|integer|None|False|AD group ID|None|
|Assigned to ID|string|None|False|Assigned to ID|None|
|Assigned to Name|string|None|False|Assigned to name|None|
|AV AVE Version|string|None|False|AV AVE version|None|
|AV Engine|string|None|False|AV engine|None|
|AV Last Scan Time|integer|None|False|AV last scan time|None|
|AV Master|boolean|None|False|AV master|None|
|AV Pack Version|string|None|False|AV pack version|None|
|AV Product Version|string|None|False|AV product version|None|
|AV Status|[]string|None|False|AV status|None|
|AV Update Servers|string|None|False|AV update servers|None|
|AV VDF Version|string|None|False|AV VDF version|None|
|Create Time|string|None|False|Create time|None|
|Current Sensor Policy Name|string|None|False|Current sensor policy name|None|
|Deregistered Time|string|None|False|Deregistered time|None|
|Device GUID|string|None|False|Device GUID|None|
|Device ID|integer|None|False|Device ID|None|
|Device Meta Data Item List|string|None|False|Device meta data item list|None|
|Device Owner ID|integer|None|False|Device owner ID|None|
|Device Session ID|string|None|False|Device session ID|None|
|Device Type|string|None|False|Device type|None|
|Email|string|None|False|Email|None|
|Encoded Activation Code|string|None|False|Encoded activation code|None|
|First Name|string|None|False|First name|None|
|First Virus Activity Time|integer|None|False|First virus activity time|None|
|Last Contact|integer|None|False|Last contact|None|
|Last Device Policy Changed Time|string|None|False|Last device policy changed time|None|
|Last Device Policy Requested time|string|None|False|Last device policy requested time|None|
|Last External IP Address|string|None|False|Last external IP address|None|
|Last Internal IP Address|string|None|False|Last internal IP address|None|
|Last Location|string|None|False|Last location|None|
|Last Name|string|None|False|Last name|None|
|Last Policy Updated Time|string|None|False|Last policy updated time|None|
|Last Reported Time|integer|None|False|Last reported time|None|
|Last Reset Time|integer|None|False|Last reset time|None|
|Last Shutdown Time|integer|None|False|Last shutdown time|None|
|Last Virus Activity Time|integer|None|False|Last virus activity time|None|
|Linux Kernel Version|string|None|False|Linux kernel version|None|
|Login User Name|string|None|False|Login user name|None|
|MAC Address|string|None|False|MAC address|None|
|Messages|string|None|False|Messages|None|
|Middle Name|string|None|False|Middle name|None|
|Name|string|None|False|Name|None|
|Organization ID|integer|None|False|Organization ID|None|
|Organization Name|string|None|False|Organization name|None|
|Origin Event Hash|string|None|False|Origin event hash|None|
|OS Version|string|None|False|OS version|None|
|Passive Mode|boolean|None|False|Passive mode|None|
|Policy ID|integer|None|False|Policy ID|None|
|Policy Name|string|None|False|Policy name|None|
|Policy Override|boolean|None|False|Policy override|None|
|Quarantined|boolean|None|False|Quarantined|None|
|Registered Time|integer|None|False|Registered time|None|
|Rooted by Analytics|boolean|None|False|Rooted by analytics|None|
|Rooted by Analytics Time|string|None|False|Rooted by analytics time|None|
|Rooted by Sensor|boolean|None|False|Rooted by sensor|None|
|Rooted by Sensor Time|string|None|False|Rooted by sensor time|None|
|Scan Last Action Time|integer|None|False|Scan last action time|None|
|Scan Last Complete Time|integer|None|False|Scan last complete time|None|
|Scan Status|string|None|False|Scan status|None|
|Sensor Kit Type|string|None|False|Sensor kit type|None|
|Sensor Out of Date|boolean|None|False|Sensor out of date|None|
|Sensor Pending Update|boolean|None|False|Sensor pending update|None|
|Sensor States|[]string|None|False|Sensor states|None|
|Sensor Version|string|None|False|Sensor version|None|
|Status|string|None|False|Status|None|
|Target Priority Type|string|None|False|Target priority type|None|
|Test ID|integer|None|False|Test ID|None|
|Uninstall Code|string|None|False|Uninstall code|None|
|Uninstalled Time|string|None|False|Uninstalled time|None|
|VDI Base Device|string|None|False|VDI base device|None|
|Virtual Machine|boolean|None|False|Virtual machine|None|
|Virtualization Provider|string|None|False|Virtualization provider|None|
|Windows Platform|string|None|False|Windows platform|None|
  
**alert**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alert Type Code|string|None|False|Type of alert|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 2.2.13 - Updated SDK to the latest version (6.4.3) | Removed migrated event source code
* 2.2.12 - Updated SDK to the latest version (6.3.10)
* 2.2.11 - 'Monitor Alerts': Fix bug related to search window reset for deduplicated alerts
* 2.2.10 - Add support for high volume event support at cutoff time and date | Update SDK to 6.3.6
* 2.2.9 - Fix error handing for when we don't get results served correctly from observations API
* 2.2.8 - Fix error handling for HTTP Not Found status code responses from Carbon Black Cloud | Update SDK to 6.2.0
* 2.2.7 - Restrain the observability window to a configurable amount if data collection falls behind
* 2.2.6 - Update SDK to 6.1.4
* 2.2.5 - To split the PAGE_SIZE limit into ALERT_PAGE_SIZE and OBSERVATION_PAGE_SIZE
* 2.2.4 - Add new connection tests for tasks | Update SDK to 6.1.0
* 2.2.3 - Fix incorrect status code handling | Customise max pages returned in `Monitor Alerts and Observations` task | Bump to SDK 6.0.1
* 2.2.2 - `Connection updated to filter whitespace from connection inputs which resulted in unexpected results.
* 2.2.1 - `Monitor Alerts and Observations` surface status code from Carbon Black in task error.
* 2.2.0 - Implement new task `Monitor Alerts and Observations` and bump to SDK 5.4.8
* 2.0.1 - Allows user entered hostnames to be case insensitive for `get_agent_details` and `quarantine` actions | Fix bug where error is raised if endpoint was not found in `get_agent` method | To add escaping of special characters in hostnames when performing hostname searches to Carbon Black
* 2.0.0 - Updated the SDK version | Cloud enabled
* 1.0.2 - Updated branding
* 1.0.1 - Fix issue where retry on error call could crash plugin
* 1.0.0 - Initial plugin

# Links

* [Carbon Black Cloud](https://www.carbonblack.com/products/vmware-carbon-black-cloud)

## References

* [Carbon Black Cloud](https://www.carbonblack.com/products/vmware-carbon-black-cloud)
* [Carbon Black Authentication](https://developer.carbonblack.com/reference/carbon-black-cloud/authentication/)
* [Carbon Black API URLs](https://developer.carbonblack.com/reference/carbon-black-cloud/authentication/#constructing-your-request)