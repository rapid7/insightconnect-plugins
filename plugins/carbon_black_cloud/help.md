# Description

The [VMware Carbon Black Cloud](https://www.carbonblack.com/products/vmware-carbon-black-cloud/) is a cloud-native endpoint protection platform (EPP) that combines the intelligent system hardening and behavioral prevention needed to keep emerging threats at bay, using a single lightweight agent and an easy-to-use console. Manage and contain threats on your Carbon Black endpoints using this plugin

# Key Features

* Get device information
* Quarantine a device

# Requirements

* API Credentials
* Base URL

# Supported Product Versions

* 2024-07-01

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


#### Monitor Alerts

This task is used to monitor alerts and observations in your Carbon Black Cloud instance

##### Input
  
*This task does not contain any inputs.*

##### Output

|Name|Type|Required|Description| Example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :--- | :--- | :--- | :--- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|alerts|[]alert|True|List of all alerts and observations|[{"org_key": "ABCD1234", "alert_url": "https://defense.conferdeploy.net/alerts?s[c][query_string]=id:52fa009d-e2d1-4118-8a8d-04f521ae66aa&orgKey=ABCD1234", "id": "12ab345cd6-e2d1-4118-8a8d-04f521ae66aa", "type": "WATCHLIST", "backend_timestamp": "2023-04-14T21:30:40.570Z", "user_update_timestamp": "None", "backend_update_timestamp": "2023-04-14T21:30:40.570Z", "detection_timestamp": "2023-04-14T21:27:14.719Z", "first_event_timestamp": "2023-04-14T21:21:42.193Z", "last_event_timestamp": "2023-04-14T21:21:42.193Z", "severity": 8, "reason": "Process infdefaultinstall.exe was detected by the report Defense Evasion - Signed Binary Proxy Execution - InfDefaultInstall in 6 watchlists", "reason_code": "05696200-88e6-3691-a1e3-8d9a64dbc24e:7828aec8-8502-3a43-ae68-41b5050dab5b", "threat_id": "0569620088E6669121E38D9A64DBC24E", "primary_event_id": "-7RlZFHcSGWKSrF55B_4Ig-0", "policy_applied": "NOT_APPLIED", "run_state": "RAN", "sensor_action": "ALLOW", "workflow": {"change_timestamp": "2023-04-14T21:30:40.570Z", "changed_by_type": "SYSTEM", "changed_by": "ALERT_CREATION", "closure_reason": "NO_REASON", "status": "OPEN"}, "determination": "None", "tags": ["tag1", "tag2"], "alert_notes_present": False, "threat_notes_present": False, "is_updated": False, "device_id": 18118174, "device_name": "pscr-test-01-1677785028.620244-9", "device_uem_id": "", "device_target_value": "LOW", "device_policy": "123abcde-c21b-4d64-9e3e-53595ef9c7af", "device_policy_id": 1234567, "device_os": "WINDOWS", "device_os_version": "Windows 10 x64 SP: 1", "device_username": "user@example.com", "device_location": "UNKNOWN", "device_external_ip": "1.2.3.4", "mdr_alert": False, "report_id": "oJFtoawGS92fVMXlELC1Ow-b4ee93fc-ec58-436a-a940-b4d33a613513", "report_name": "Defense Evasion - Signed Binary Proxy Execution - InfDefaultInstall", "report_description": "\\n\\nThreat:\\nThis behavior may be abused by adversaries to execute malicious files that could bypass application whitelisting and signature validation on systems.\\n\\nFalse Positives:\\nSome environments may legitimate use this, but should be rare.\\n\\nScore:\\n85", "report_tags": ["tag1"], "report_link": "https://attack.mitre.org/wiki/Technique/T1218", "ioc_id": "b4ee93fc-ec58-436a-a940-b4d33a613513-0", "ioc_hit": "((process_name:InfDefaultInstall.exe)) -enriched:true", "watchlists": [{"id": "hfnsh73543jdt", "name": "Carbon Black Advanced Threats"}], "process_guid": "ABCD1234-0114761e-00002ae4-00000000-19db1ded53e8000", "process_pid": 10980, "process_name": "infdefaultinstall.exe", "process_sha256": "1a2345cd88666a458f804e5d0fe925a9f55cf016733458c58c1980addc44cd774", "process_md5": "12c34567894a49f13193513b0138f72a9", "process_effective_reputation": "LOCAL_WHITE", "process_reputation": "NOT_LISTED", "process_cmdline": "InfDefaultInstall.exe C:\\\\Users\\\\username\\\\userdir\\\\Infdefaultinstall.inf", "process_username": "DEMO\\\\DEMOUSER", "process_issuer": "Demo Code Signing CA - G2", "process_publisher": "Demo Test Authority", "childproc_guid": "", "childproc_username": "", "childproc_cmdline": "", "ml_classification_final_verdict": "NOT_ANOMALOUS", "ml_classification_global_prevalence": "LOW", "ml_classification_org_prevalence": "LOW"}, {"backend_timestamp": "2024-04-25T13:13:14.268Z", "device_group_id": 0, "device_id": 1234567, "device_name": "device\\\\name", "device_policy_id": 1234, "device_timestamp": "2024-04-25T13:12:16.965Z", "enriched": True, "enriched_event_type": ["CREATE_PROCESS"], "event_description": "Threat:\\nThis behavior may be abused by adversaries to execute malicious files that could bypass application whitelisting", "event_id": "123abc456hij987", "event_type": "childproc", "ingress_time": 1714050766940, "legacy": True, "observation_description": "Threat:\\nThis behavior may be abused by adversaries to execute malicious files that could bypass application whitelisting", "observation_id": "123abc456hij987", "observation_type": "CONTEXTUAL_ACTIVITY", "org_id": "ABCD123", "parent_guid": "7DESJ9GN-00663165-00000e3c-00000000-1da90da1398f66e", "parent_pid": 1234, "process_guid": "7DESJ9GN-00663165-0000490c-00000000-1da971229580df5", "process_hash": ["460091df9292bf9307cb92d1aef8d0e5", "e59c1ee25d223308115101b022e15bb887a3deba629be743ab03e08439c2b6f6"], "process_name": "c:\\\\program files\\\\directory\\\\example.exe", "process_pid": [18700], "process_username": ["USER\\\\NAME"]}]|

Example output:

```
{
  "alerts": [
    {
      "alert_notes_present": False,
      "alert_url": "https://defense.conferdeploy.net/alerts?s[c][query_string]=id:52fa009d-e2d1-4118-8a8d-04f521ae66aa&orgKey=ABCD1234",
      "backend_timestamp": "2023-04-14T21:30:40.570Z",
      "backend_update_timestamp": "2023-04-14T21:30:40.570Z",
      "childproc_cmdline": "",
      "childproc_guid": "",
      "childproc_username": "",
      "detection_timestamp": "2023-04-14T21:27:14.719Z",
      "determination": "None",
      "device_external_ip": "1.2.3.4",
      "device_id": 18118174,
      "device_location": "UNKNOWN",
      "device_name": "pscr-test-01-1677785028.620244-9",
      "device_os": "WINDOWS",
      "device_os_version": "Windows 10 x64 SP: 1",
      "device_policy": "123abcde-c21b-4d64-9e3e-53595ef9c7af",
      "device_policy_id": 1234567,
      "device_target_value": "LOW",
      "device_uem_id": "",
      "device_username": "user@example.com",
      "first_event_timestamp": "2023-04-14T21:21:42.193Z",
      "id": "12ab345cd6-e2d1-4118-8a8d-04f521ae66aa",
      "ioc_hit": "((process_name:InfDefaultInstall.exe)) -enriched:true",
      "ioc_id": "b4ee93fc-ec58-436a-a940-b4d33a613513-0",
      "is_updated": False,
      "last_event_timestamp": "2023-04-14T21:21:42.193Z",
      "mdr_alert": False,
      "ml_classification_final_verdict": "NOT_ANOMALOUS",
      "ml_classification_global_prevalence": "LOW",
      "ml_classification_org_prevalence": "LOW",
      "org_key": "ABCD1234",
      "policy_applied": "NOT_APPLIED",
      "primary_event_id": "-7RlZFHcSGWKSrF55B_4Ig-0",
      "process_cmdline": "InfDefaultInstall.exe C:\\\\Users\\\\username\\\\userdir\\\\Infdefaultinstall.inf",
      "process_effective_reputation": "LOCAL_WHITE",
      "process_guid": "ABCD1234-0114761e-00002ae4-00000000-19db1ded53e8000",
      "process_issuer": "Demo Code Signing CA - G2",
      "process_md5": "12c34567894a49f13193513b0138f72a9",
      "process_name": "infdefaultinstall.exe",
      "process_pid": 10980,
      "process_publisher": "Demo Test Authority",
      "process_reputation": "NOT_LISTED",
      "process_sha256": "1a2345cd88666a458f804e5d0fe925a9f55cf016733458c58c1980addc44cd774",
      "process_username": "DEMO\\\\DEMOUSER",
      "reason": "Process infdefaultinstall.exe was detected by the report Defense Evasion - Signed Binary Proxy Execution - InfDefaultInstall in 6 watchlists",
      "reason_code": "05696200-88e6-3691-a1e3-8d9a64dbc24e:7828aec8-8502-3a43-ae68-41b5050dab5b",
      "report_description": "\\n\\nThreat:\\nThis behavior may be abused by adversaries to execute malicious files that could bypass application whitelisting and signature validation on systems.\\n\\nFalse Positives:\\nSome environments may legitimate use this, but should be rare.\\n\\nScore:\\n85",
      "report_id": "oJFtoawGS92fVMXlELC1Ow-b4ee93fc-ec58-436a-a940-b4d33a613513",
      "report_link": "https://attack.mitre.org/wiki/Technique/T1218",
      "report_name": "Defense Evasion - Signed Binary Proxy Execution - InfDefaultInstall",
      "report_tags": [
        "tag1"
      ],
      "run_state": "RAN",
      "sensor_action": "ALLOW",
      "severity": 8,
      "tags": [
        "tag1",
        "tag2"
      ],
      "threat_id": "0569620088E6669121E38D9A64DBC24E",
      "threat_notes_present": false,
      "type": "WATCHLIST",
      "user_update_timestamp": "None",
      "watchlists": [
        {
          "id": "hfnsh73543jdt",
          "name": "Carbon Black Advanced Threats"
        }
      ],
      "workflow": {
        "change_timestamp": "2023-04-14T21:30:40.570Z",
        "changed_by": "ALERT_CREATION",
        "changed_by_type": "SYSTEM",
        "closure_reason": "NO_REASON",
        "status": "OPEN"
      }
    },
    {
      "backend_timestamp": "2024-04-25T13:13:14.268Z",
      "device_group_id": 0,
      "device_id": 1234567,
      "device_name": "device\\\\name",
      "device_policy_id": 1234,
      "device_timestamp": "2024-04-25T13:12:16.965Z",
      "enriched": True,
      "enriched_event_type": [
        "CREATE_PROCESS"
      ],
      "event_description": "Threat:\\nThis behavior may be abused by adversaries to execute malicious files that could bypass application whitelisting",
      "event_id": "123abc456hij987",
      "event_type": "childproc",
      "ingress_time": 1714050766940,
      "legacy": true,
      "observation_description": "Threat:\\nThis behavior may be abused by adversaries to execute malicious files that could bypass application whitelisting",
      "observation_id": "123abc456hij987",
      "observation_type": "CONTEXTUAL_ACTIVITY",
      "org_id": "ABCD123",
      "parent_guid": "7DESJ9GN-00663165-00000e3c-00000000-1da90da1398f66e",
      "parent_pid": 1234,
      "process_guid": "7DESJ9GN-00663165-0000490c-00000000-1da971229580df5",
      "process_hash": [
        "460091df9292bf9307cb92d1aef8d0e5",
        "e59c1ee25d223308115101b022e15bb887a3deba629be743ab03e08439c2b6f6"
      ],
      "process_name": "c:\\\\program files\\\\directory\\\\example.exe",
      "process_pid": [
        18700
      ],
      "process_username": [
        "USER\\\\NAME"
      ]
    }
  ]
}
```

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

* 2.2.9 - Fix error handing for when we don't get results served correctly from observations API
* 2.2.8 - Fix error handling for HTTP Not Found status code responses from Carbon Black Cloud | Update SDK to 6.2.0
* 2.2.7 - Restrain the observability window to a configurable amount if data collection falls behind
* 2.2.6 - Update SDK to 6.1.4
* 2.2.5 - To split the PAGE_SIZE limit into ALERT_PAGE_SIZE and OBSERVATION_PAGE_SIZE
* 2.2.4 - Add new connection tests for tasks | Update SDK to 6.1.0
* 2.2.3 - Fix incorrect status code handling | Customise max pages returned in `Monitor Alerts and Observations` task | Bump to SDK 6.0.1
* 2.2.2 - Connection updated to filter whitespace from connection inputs which resulted in unexpected results.
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