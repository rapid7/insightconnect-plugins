# Description

[Microsoft Intune](https://www.microsoft.com/en-us/microsoft-365/enterprise-mobility-security/microsoft-intune) is a Microsoft cloud-based management solution that provides for mobile device and operating system management.

# Key Features

* Initiate a Windows Defender Antivirus scan on a machine.

# Requirements

* Azure credentials
* Client ID, Client Secret and Tenant ID

# Documentation

## Setup

1. Create an Azure Active Directory application.
2. Assign the following API Permissions to the application:
    * Within Microsoft Graph select Delegated Permissions and pick below permissions under DeviceManagementManagedDevices:
        * DeviceManagementManagedDevices.PrivilegedOperations.All
        * DeviceManagementManagedDevices.Read.All
        * DeviceManagementManagedDevices.ReadWrite.All
    * Please note, these API Permissions require administrator consent.
3. Create a new secret and copy and paste the secret value into the connection.
4. Copy and paste the 'Application (client) ID' and 'Directory (tenant) ID' (from the Overview tab) into the connection.

For detailed instructions refer to [Microsoft Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal).

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|client_id|string|None|True|Client ID, also called Application ID|None|a74dfb10-i33o-44e1-ba87-5fn2bb4e6b4d|
|client_secret|string|None|True|Client secret key|None|kQDFcZoJYmxJpiS1x7rdyleyNFwhvLgcOZCkYG+5=|
|credentials|credential_username_password|None|True|E-mail address and password|None|{"username": "user@example.com", "password": "mypassword"}|
|tenant_id|string|None|True|Tenant ID can be found in Active Directory|None|3a522933-ae5e-2b63-96ab-3c004b4f7f10|
|url|string|https://graph.microsoft.com|True|Base URL for the Microsoft endpoint|None|https://graph.microsoft.com|

Example input:

```
{
  "client_id": "a74dfb10-i33o-44e1-ba87-5fn2bb4e6b4d",
  "client_secret": "kQDFcZoJYmxJpiS1x7rdyleyNFwhvLgcOZCkYG+5=",
  "credentials": {
    "username": "user@example.com",
    "password": "mypassword"
  },
  "tenant_id": "3a522933-ae5e-2b63-96ab-3c004b4f7f10",
  "url": "https://graph.microsoft.com"
}
```

## Technical Details

### Actions

#### Wipe

This action is used to wipe device by device name, device ID, user ID, or email address. It supports a whitelist to skip critical devices that should never be whitelisted.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|device|string|None|True|Device name, user ID, email address, or device ID|None|547a48e3-0942-4888-acf1-a92b7fb19ef9|
|whitelist|[]string|None|False|This list contains a set of of device names, user IDs, email addresses, or device IDs that a user can pass in that will not be wiped|None|["user@example.com", "705c034c-034c-705c-4c03-5c704c035c70"]|

Example input:

```
{
  "device": "547a48e3-0942-4888-acf1-a92b7fb19ef9",
  "whitelist": [
    "user@example.com",
    "705c034c-034c-705c-4c03-5c704c035c70"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Return true if device was successfully wiped|

Example output:

```
{
  "success": false
}
```

#### Search Devices

This action is used to search devices by device name, user ID, email address or device ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|device|string|None|True|Search devices by either of - device name, user ID, email address, device ID|None|547a48e3-0942-4888-acf1-a92b7fb19ef9|

Example input:

```
{
  "device": "547a48e3-0942-4888-acf1-a92b7fb19ef9"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|devices|[]device|False|Devices details|

Example output:

```
{
  "devices": [
    {
      "complianceGracePeriodExpirationDateTime": "9999-12-31T23:59:59Z",
      "deviceEnrollmentType": "windowsAzureADJoin",
      "id": "547a48e3-0942-4888-acf1-a92b7fb19ef9",
      "manufacturer": "innotek GmbH",
      "lastSyncDateTime": "2020-06-13T20:00:23Z",
      "remoteAssistanceSessionUrl": null,
      "meid": "",
      "phoneNumber": "",
      "userId": "ac785ffe-530a-45a1-bbf4-e275457e464b",
      "easActivationDateTime": "0001-01-01T00:00:00Z",
      "enrolledDateTime": "2020-06-12T13:52:38Z",
      "exchangeAccessState": "none",
      "isSupervised": false,
      "operatingSystem": "Windows",
      "serialNumber": "0",
      "totalStorageSpaceInBytes": 135996112896,
      "deviceCategoryDisplayName": "Unknown",
      "deviceName": "DESKTOP-8SGGSQ9",
      "emailAddress": "user@example.com",
      "imei": "",
      "activationLockBypassCode": null,
      "managedDeviceName": "user1_Windows_6/12/2020_1:52 PM",
      "managementAgent": "mdm",
      "deviceActionResults": [],
      "deviceHealthAttestationState": null,
      "freeStorageSpaceInBytes": 115349651456,
      "jailBroken": "Unknown",
      "androidSecurityPatchLevel": "",
      "azureADRegistered": false,
      "complianceState": "compliant",
      "configurationManagerClientEnabledFeatures": null,
      "wiFiMacAddress": "",
      "model": "VirtualBox",
      "osVersion": "10.0.18363.836",
      "partnerReportedThreatState": "unknown",
      "userPrincipalName": "user@example.com",
      "isEncrypted": false,
      "remoteAssistanceSessionErrorDetails": null,
      "azureADDeviceId": "4302106f-1d7b-49d6-9f7f-f43fecba007b",
      "easActivated": false,
      "exchangeAccessStateReason": "none",
      "exchangeLastSuccessfulSyncDateTime": "0001-01-01T00:00:00Z",
      "userDisplayName": "User1",
      "deviceRegistrationState": "registered",
      "easDeviceId": "",
      "managedDeviceOwnerType": "company",
      "subscriberCarrier": ""
    }
  ]
}
```

#### Manage Device

This action is used to perform management tasks on a device such as rebooting and syncing.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|device|string|None|True|Device name, user ID, email address, or device ID|None|aaaa55aa-a55a-5a5a-5aa5-aaaaa555aaa|
|type|string|None|True|Type of action|['Reboot', 'Sync']|None|
|whitelist|[]string|None|False|This list contains a set of of device names, user IDs, email addresses, or device IDs that action will not be performed on|None|["user@example.com", "705c034c-034c-705c-4c03-5c704c035c70"]|

Example input:

```
{
  "device": "aaaa55aa-a55a-5a5a-5aa5-aaaaa555aaa",
  "whitelist": [
    "user@example.com",
    "705c034c-034c-705c-4c03-5c704c035c70"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Return true if action was successfully performed on device|

Example output:

```
{
  "success": true
}
```

#### Antivirus Scan

This action is used to initiate a Windows Defender Antivirus scan on a machine.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|device|string|None|True|Search devices by device name, user ID, email address, or device ID|None|547a48e3-0942-4888-acf1-a92b7fb19ef9|
|update|boolean|False|False|If true the action updates Antivirus Signatures before scan|None|True|

Example input:

```
{
  "device": "547a48e3-0942-4888-acf1-a92b7fb19ef9",
  "update": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Return true if scan was initiated successfully|

Example output:

```
{
  "success": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.2.0 - Add new action Manage Device
* 1.1.0 - Add new actions Search Devices and Wipe
* 1.0.0 - Initial plugin creation, action Antivirus Scan added

# Links

## References

* [Microsoft Intune](https://docs.microsoft.com/en-us/graph/)
