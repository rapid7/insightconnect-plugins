# Description

[Microsoft Intune](https://www.microsoft.com/en-us/microsoft-365/enterprise-mobility-security/microsoft-intune) is a Microsoft cloud-based management solution that provides for mobile device and operating system management.

# Key Features

* Initiate a Windows Defender Antivirus scan on a machine.
* Get information about the device
* Get information about the Autopilot device
* Get information about managed applications
* Search for devices by ID, name or email
* Run a quick or full scan of the device
* Delete the device from Autopilot and Intune
* Reboot, sync or wipe the device

# Requirements

* Azure credentials
* Client ID, Client Secret and Tenant ID

# Supported Product Versions

* Microsoft Graph REST API v1.0 2023-08-29

# Documentation

## Setup

1. Create an Azure Active Directory application.
2. Assign the following API Permissions to the application:
    * Within Microsoft Graph select Delegated Permissions and pick below permissions under DeviceManagementManagedDevices:
        * DeviceManagementManagedDevices.PrivilegedOperations.All
        * DeviceManagementManagedDevices.Read.All
        * DeviceManagementManagedDevices.ReadWrite.All
        * DeviceManagementServiceConfig.Read.All
    * Please note, these API Permissions require administrator consent.
3. Create a new secret and copy and paste the secret value into the connection.
4. Copy and paste the 'Application (client) ID' and 'Directory (tenant) ID' (from the Overview tab) into the connection.

For detailed instructions refer to [Microsoft Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal).

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|clientId|string|None|True|Client ID, also called Application ID|None|a74dfb10-i33o-44e1-ba87-5fn2bb4e6b4d|
|clientSecret|credential_secret_key|None|True|Client secret key|None|kQDFcZoJYmxJpiS1x7rdyleyNFwhvLgcOZCkYG+5=|
|credentials|credential_username_password|None|True|E-mail address and password|None|{"username": "user@example.com", "password": "mypassword"}|
|tenantId|string|None|True|Tenant ID can be found in Active Directory|None|3a522933-ae5e-2b63-96ab-3c004b4f7f10|

Example input:

```
{
  "clientId": "a74dfb10-i33o-44e1-ba87-5fn2bb4e6b4d",
  "clientSecret": {
    "secretKey": "kQDFcZoJYmxJpiS1x7rdyleyNFwhvLgcOZCkYG+5="
  },
  "credentials": {
    "username": "user@example.com",
    "password": "mypassword"
  },
  "tenantId": "3a522933-ae5e-2b63-96ab-3c004b4f7f10"
}
```

## Technical Details

### Actions

#### Antivirus Scan

This action is used to initiate a Windows Defender Antivirus scan on a machine.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|device|string|None|True|Search devices by device name, user ID, email address, or device ID|None|547a48e3-0942-4888-acf1-a92b7fb19ef9|
|update|boolean|False|False|If true the action updates Antivirus Signatures before scan|None|True|

Example input:

```
{
  "device": "547a48e3-0942-4888-acf1-a92b7fb19ef9",
  "update": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Return true if scan was initiated successfully|True|

Example output:

```
{
  "success": true
}
```

#### Delete Device from Autopilot

This action is used to delete the device from Autopilot.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|deviceId|string|None|True|ID of the device|None|9e8fd111-6c41-1111-85b9-11395662e111|

Example input:

```
{
  "deviceId": "9e8fd111-6c41-1111-85b9-11395662e111"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the scan was successful|True|

Example output:

```
{
  "success": true
}
```

#### Delete Device from Intune

This action is used to delete the managed device from Intune.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|deviceId|string|None|True|ID of the managed device|None|9e8fd111-6c41-1111-85b9-11395662e111|

Example input:

```
{
  "deviceId": "9e8fd111-6c41-1111-85b9-11395662e111"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the scan was successful|True|

Example output:

```
{
  "success": true
}
```

#### Full Scan

This action is used to perform a full scan of the device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|deviceId|string|None|True|ID of the device|None|9e8fd111-6c41-1111-85b9-11395662e111|

Example input:

```
{
  "deviceId": "9e8fd111-6c41-1111-85b9-11395662e111"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Whether the scan was successful|True|

Example output:

```
{
  "success": true
}
```

#### Get Autopilot Device
  
This action is used to get information about the Autopilot device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|deviceId|string|None|True|ID of the Autopilot device|None|9e8fd111-6c41-1111-85b9-11395662e111|

Example input:

```
{
  "deviceId": "9e8fd111-6c41-1111-85b9-11395662e111"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|device|autopilotDevice|False|Information about the autopilot device|{}|

Example output:

```
{
  "device": {
    "id": "9e8fd111-6c41-1111-85b9-11395662e111",
    "group_tag": "example-tag",
    "purchase_order_identifier": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
    "serial_number": "A1B2C3D4",
    "product_key": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
    "manufacturer": "Example Manufacturer",
    "model": "Example Model",
    "last_contacted_date_time": "2021-06-24T00:37:04.5885438Z",
    "enrollment_state": "notContacted",
    "addressable_user_name": "user@example.com",
    "user_principal_name": "Example Name",
    "resource_name": "Example Resource Name",
    "sku_number": "ABCD1234",
    "system_family": "EXAMPLE_FAMILY",
    "azure_active_directory_device_id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
    "managed_device_id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
    "display_name": "Example Name"
  }
}
```

#### Get Device

This action is used to get information about the device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|deviceId|string|None|True|ID of the device|None|9e8fd111-6c41-1111-85b9-11395662e111|

Example input:

```
{
  "deviceId": "9e8fd111-6c41-1111-85b9-11395662e111"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|device|device|False|Information about the device|{}|

Example output:

```
{
  "device": {
    "id": "9e8fd111-6c41-1111-85b9-11395662e111",
    "userId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
    "deviceName": "INTUNE-W10-C",
    "managedDeviceOwnerType": "personal",
    "enrolledDateTime": "2021-06-24T00:37:04.5885438Z",
    "lastSyncDateTime": "2023-08-23T09:05:10.1997623Z",
    "operatingSystem": "Windows",
    "complianceState": "compliant",
    "jailBroken": "Unknown",
    "managementAgent": "mdm",
    "osVersion": "10.0.19044.3084",
    "easActivated": true,
    "easDeviceId": "FD80418A34D1234567E08E82604E1111",
    "easActivationDateTime": "2021-06-24T08:37:10.2303995Z",
    "azureADRegistered": true,
    "deviceEnrollmentType": "userEnrollment",
    "emailDddress": "user@example.com",
    "azureADDeviceId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
    "deviceRegistrationState": "registered",
    "isSupervised": false,
    "exchangeLastSuccessfulSyncDateTime": "0001-01-01T00:00:00Z",
    "exchangeAccessState": "none",
    "exchangeAccessStateReason": "none",
    "isEncrypted": false,
    "userPrincipalName": "user@example.com",
    "model": "VMware Virtual Platform",
    "manufacturer": "VMware, Inc.",
    "complianceGracePeriodExpirationDateTime": "9999-12-31T23:59:59.9999999Z",
    "serialNumber": "VMware-42146feae7654321-123456304825cc11",
    "userDisplayName": "Example User",
    "totalStorageSpaceInBytes": 33773584384,
    "freeStorageSpaceInBytes": 1660944384,
    "partnerReportedThreatState": "unknown",
    "managementCertificateExpirationDate": "2024-02-13T19:33:06Z",
    "ethernetMacAddress": "005056949D3E",
    "physicalMemoryInBytes": 0,
    "deviceActionResults": [
      {
        "actionName": "windowsDefenderUpdateSignatures",
        "actionState": "done",
        "startDateTime": "2022-04-26T13:19:45.3008934Z",
        "lastUpdatedDateTime": "2022-04-26T13:25:27Z"
      },
      {
        "@odata.type": "#microsoft.graph.windowsDefenderScanActionResult",
        "actionName": "windowsDefenderScan",
        "actionState": "done",
        "startDateTime": "2023-08-23T08:20:27.9731659Z",
        "lastUpdatedDateTime": "2023-08-23T09:04:07Z",
        "scanType": "Full Scan"
      },
      {
        "@odata.type": "#microsoft.graph.windowsDefenderScanActionResult",
        "actionName": "windowsDefenderScan",
        "actionState": "done",
        "startDateTime": "2023-08-23T08:21:02.3882789Z",
        "lastUpdatedDateTime": "2023-08-23T09:04:07Z",
        "scanType": "Quick scan"
      }
    ]
  }
}
```

#### Get Managed Apps

This action returns InTune manageable apps.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|app|string|None|False|Application ID or name, if empty returns all applications|None|af6040ed-efe0-494c-89ed-89880989674c|

Example input:

```
{
  "app": "af6040ed-efe0-494c-89ed-89880989674c"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|managedApps|[]value|False|Application details|[]|

Example output:

```
{
  "managedApps": [
    {
      "publisher": "Adobe Inc.",
      "appAvailability": "lineOfBusiness",
      "appStoreUrl": "https://play.google.com/store/apps/details?id=com....",
      "createdDateTime": "2020-11-20T14:51:29.9832609Z",
      "description": "Adobe Acrobat Reader is the most reliable, free gl...",
      "displayName": "Adobe Acrobat Reader",
      "id": "af6040ed-efe0-494c-89ed-89880989674c",
      "isFeatured": false,
      "publishingState": "published",
      "@odata.type": "#microsoft.graph.managedAndroidStoreApp",
      "minimumSupportedOperatingSystem": {
        "v4_1": false,
        "v4_2": false,
        "v4_3": false,
        "v4_4": true,
        "v5_0": false,
        "v5_1": false,
        "v4_0": false,
        "v4_0_3": false
      },
      "lastModifiedDateTime": "2020-11-20T14:51:29.9832609Z",
      "version": "\"da13c2e2-b4b4-419c-a223-af043e69c799\"",
      "packageId": "com.adobe.reader"
    }
  ]
}
```

#### Manage Device

This action is used to perform management tasks on a device such as rebooting and syncing.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|device|string|None|True|Device name, user ID, email address, or device ID|None|aaaa55aa-a55a-5a5a-5aa5-aaaaa555aaa|
|type|string|None|True|Type of action|['Reboot', 'Sync']|Sync|
|whitelist|[]string|None|False|This list contains a set of of device names, user IDs, email addresses, or device IDs that action will not be performed on|None|["user@example.com", "705c034c-034c-705c-4c03-5c704c035c70"]|

Example input:

```
{
  "device": "aaaa55aa-a55a-5a5a-5aa5-aaaaa555aaa",
  "type": "Sync",
  "whitelist": [
    "user@example.com",
    "705c034c-034c-705c-4c03-5c704c035c70"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Return true if action was successfully performed on device|True|

Example output:

```
{
  "success": true
}
```

#### Quick Scan

This action is used to perform a quick scan of the device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|deviceId|string|None|True|ID of the device|None|9e8fd111-6c41-1111-85b9-11395662e111|

Example input:

```
{
  "deviceId": "9e8fd111-6c41-1111-85b9-11395662e111"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Whether the scan was successful|True|

Example output:

```
{
  "success": true
}
```

#### Search Devices
  
This action is used to search devices by device name, user ID, email address or device ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|device|string|None|True|Search devices by either of - device name, user ID, email address, device ID|None|547a48e3-0942-4888-acf1-a92b7fb19ef9|

Example input:

```
{
  "device": "547a48e3-0942-4888-acf1-a92b7fb19ef9"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|devices|[]device|False|Devices details|[]|

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
      "managedDeviceName": "user1_Windows_6/12/2020_1:52 PM",
      "managementAgent": "mdm",
      "freeStorageSpaceInBytes": 115349651456,
      "jailBroken": "Unknown",
      "azureADRegistered": false,
      "complianceState": "compliant",
      "model": "VirtualBox",
      "osVersion": "10.0.18363.836",
      "partnerReportedThreatState": "unknown",
      "userPrincipalName": "user@example.com",
      "isEncrypted": false,
      "azureADDeviceId": "4302106f-1d7b-49d6-9f7f-f43fecba007b",
      "easActivated": false,
      "exchangeAccessStateReason": "none",
      "exchangeLastSuccessfulSyncDateTime": "0001-01-01T00:00:00Z",
      "userDisplayName": "User1",
      "deviceRegistrationState": "registered",
      "managedDeviceOwnerType": "company"
    }
  ]
}
```

#### Wipe

This action is used to wipe device by device name, device ID, user ID, or email address. It supports a whitelist to skip critical devices that should never be whitelisted.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Return true if device was successfully wiped|True|

Example output:

```
{
  "success": true
}
```

### Triggers

*This plugin does not contain any triggers.*

### Tasks

*This plugin does not contain any tasks.*

### Custom Output Types

**value**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Odata Context|string|None|False|Odata context|https://example.com|
|Odata Type|string|None|False|Odata type|#microsoft.graph.managedApp|
|App Availability|string|None|False|App availability|global|
|App Store URL|string|None|False|App store URL|https://example.com|
|Created Datetime|string|None|False|Created datetime|2020-11-20 14:51:29+00:00|
|Description|string|None|False|Description|Example description|
|Developer|string|None|False|Developer|Example developer|
|Display Name|string|None|False|Display Name|Adobe Acrobat Reader|
|ID|string|None|False|ID|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Information URL|string|None|False|Information URL|https://example.com|
|Is Featured|boolean|None|False|Is featured|False|
|Large Icon|object|None|False|Large icon|{}|
|Last Modified Datetime|string|None|False|Last modified datetime|2020-11-20 14:51:29+00:00|
|Minimum Supported Operating System|object|None|False|Minimum supported operating system|{"v4_0": false}|
|Notes|string|None|False|Notes|Example notes|
|Owner|string|None|False|Owner|Example owner|
|Package ID|string|None|False|Package ID|com.adobe.reader|
|Privacy Information URL|string|None|False|Privacy information URL|https://example.com|
|Publisher|string|None|False|Publisher|Adobe Inc.|
|Publishing State|string|None|False|Publishing state|published|
|Version|string|None|False|Version|1.0|

**configurationManagerClientEnabledFeatures**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Odata Type|string|None|False|Odata type|microsoft.graph.configurationManagerClientEnabledFeatures|
|Compliance Policy|boolean|None|False|Compliance policy|True|
|Device Configuration|boolean|None|False|Device configuration|True|
|Inventory|boolean|None|False|Inventory|True|
|Modern Apps|boolean|None|False|Modern apps|True|
|Resource Access|boolean|None|False|Resource access|True|
|Windows Update For Business|boolean|None|False|Windows update for business|True|

**deviceActionResults**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Odata Type|string|None|False|Odata type|#microsoft.graph.windowsDefenderScanActionResult|
|Action Name|string|None|False|Action name|windowsDefenderScan|
|Action State|string|None|False|Action state|done|
|Last Updated Date Time|date|None|False|Last updated date time|2023-08-30 10:21:31+00:00|
|Start Date Time|date|None|False|Start date time|2023-08-30 10:13:51.339250+00:00|

**deviceHealthAttestationState**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Odata Type|string|None|False|Odata type|microsoft.graph.deviceHealthAttestationState|
|Attestation Identity Key|string|None|False|Attestation identity key|Example key|
|BitLocker Status|string|None|False|BitLocker status|Bit Locker Status value|
|Boot App Security Version|string|None|False|Boot app security version|Boot App Security Version value|
|Boot Debugging|string|None|False|Boot debugging|Boot Debugging value|
|Boot Manager Security Version|string|None|False|Boot manager security version|Boot Manager Security Version value|
|Boot Manager Version|string|None|False|Boot manager version|Boot Manager Version value|
|Boot Revision List Info|string|None|False|Boot revision list info|Boot Revision List Info value|
|Code Integrity|string|None|False|Code integrity|Code Integrity value|
|Code Integrity Check Version|string|None|False|Code integrity check version|Code Integrity Check Version value|
|Code Integrity Policy|string|None|False|Code integrity policy|Code Integrity Policy value|
|Content Namespace URL|string|None|False|Content namespace URL|https://example.com|
|Content Version|string|None|False|Content version|Content Version value|
|Data Excution Policy|string|None|False|Data excution policy|Data Excution Policy value|
|Device Health Attestation Status|string|None|False|Device health attestation status|Device Health Attestation Status value|
|Early Launch Anti Malware Driver Protection|string|None|False|Early launch anti malware driver protection|Early Launch Anti Malware Driver Protection value|
|Health Attestation Supported Status|string|None|False|Health attestation supported status|Health Attestation Supported Status value|
|Health Status Mismatch Info|string|None|False|Health status mismatch info|Health Status Mismatch Info value|
|Issued Date Time|date|None|False|Issued date time|2023-08-30 10:13:51.339250+00:00|
|Last Update Date Time|date|None|False|Last update date time|2023-08-30 10:13:51.339250+00:00|
|Operating System Kernel Debugging|string|None|False|Operating system kernel debugging|Operating System Kernel Debugging value|
|Operating System Rev List Info|string|None|False|Operating system rev list info|Operating System Rev List Info value|
|PCR0|string|None|False|PCR0|Pcr0 value|
|PCR Hash Algorithm|string|None|False|PCR hash algorithm|Pcr Hash Algorithm value|
|Reset Count|integer|None|False|Reset count|1024|
|Restart Count|integer|None|False|Restart count|1024|
|Safe Mode|string|None|False|Safe mode|Safe Mode value|
|Secure Boot|string|None|False|Secure boot|Secure Boot value|
|Secure Boot Configuration Policy Finger Print|string|None|False|Secure boot configuration policy finger print|Secure Boot Configuration Policy Finger Print value|
|Test Signing|string|None|False|Test signing|Test Signing value|
|TPM Version|string|None|False|TPM version|TPM Version value|
|Virtual Secure Mode|string|None|False|Virtual secure mode|Virtual Secure Mode value|
|Windows PE|string|None|False|Windows PE|Windows PE value|

**device**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Odata Type|string|None|False|Odata type|#microsoft.graph.managedDevice|
|Activation Lock Bypass Code|string|None|False|Activation lock bypass code|123456789|
|Android Security Patch Level|string|None|False|Android security patch level|2023-08-30|
|Azure AD Device ID|string|None|False|Azure AD device ID|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Azure AD Registered|boolean|None|False|Azure AD registered|True|
|Compliance Grace Period Expiration Date Time|date|None|False|Compliance grace period expiration date time|9999-12-31 23:59:59.999999+00:00|
|Compliance State|string|None|False|Compliance state|compliant|
|Configuration Manager Client Enabled Features|configurationManagerClientEnabledFeatures|None|False|Configuration manager client enabled features|{}|
|Device Action Results|[]deviceActionResults|None|False|Device action results|[]|
|Device Category Display Name|string|None|False|Device category display name|Example category|
|Device Enrollment Type|string|None|False|Device enrollment type|userEnrollment|
|Device Health Attestation State|deviceHealthAttestationState|None|False|Device health attestation state|{}|
|Device Name|string|None|False|Device name|INTUNE-W10|
|Device Registration State|string|None|False|Device registration state|registered|
|EAS Activated|boolean|None|False|EAS activated|True|
|EAS Activation Date Time|date|None|False|EAS activation date time|2021-06-24 08:37:10.230399+00:00|
|EAS Device ID|string|None|False|EAS device ID|FD12345678904B5820E08E8123456789|
|Email Address|string|None|False|Email address|user@example.com|
|Enrolled Date Time|date|None|False|Enrolled date time|2021-06-24 00:37:04.588543+00:00|
|Exchange Access State|string|None|False|Exchange access state|unknown|
|Exchange Access State Reason|string|None|False|Exchange access state reason|unknown|
|Exchange Last Successful Sync Date Time|date|None|False|Exchange last successful sync date time|2021-06-24 00:37:04.588543+00:00|
|Free Storage Space In Bytes|integer|None|False|Free storage space in bytes|1646264320|
|ID|string|None|False|ID|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|IMEI|string|None|False|IMEI|123456789876543|
|Is Encrypted|boolean|None|False|Is encrypted|True|
|Is Supervised|boolean|None|False|Is supervised|True|
|Jail Broken|string|None|False|Jail broken|Unknown|
|Last Sync Date Time|date|None|False|Last sync date time|2023-08-30 10:22:33.628668+00:00|
|Managed Device Name|string|None|False|Managed device name|Example device|
|Managed Device Owner Type|string|None|False|Managed device owner type|personal|
|Management Agent|string|None|False|Management agent|mdm|
|Manufacturer|string|None|False|Manufacturer|VMware, Inc.|
|MEID|string|None|False|MEID|ABC123456789CBA|
|Model|string|None|False|Model|VMware Virtual Platform|
|Operating System|string|None|False|Operating system|Windows|
|OS Version|string|None|False|OS version|10.0.19044.3086|
|Partner Reported Threat State|string|None|False|Partner reported threat state|activated|
|Phone Number|string|None|False|Phone number|123456789|
|Remote Assistance Session Error Details|string|None|False|Remote assistance session error details|Example details|
|Remote Assistance Session URL|string|None|False|Remote assistance session URL|https://example.com|
|Serial Number|string|None|False|Serial number|VMware-123456789-987654321|
|Subscriber Carrier|string|None|False|Subscriber carrier|Example subscriber carrier|
|Total Storage Space In Bytes|integer|None|False|Total storage space in bytes|33773584384|
|User Display Name|string|None|False|User display name|Example User|
|User ID|string|None|False|User ID|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|User Principal Name|string|None|False|User principal name|user@example.com|
|Wifi MAC Address|string|None|False|Wifi MAC address|12-34-56-78-AB-CD|

**autopilotDevice**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Addressable User Name|string|None|False|Addressable user name|user@example.com|
|Azure Active Directory Device ID|string|None|False|The unique identifier for the Azure Active Directory device|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Display Name|string|None|False|Display name of the device|Example Name|
|Enrollment State|string|None|False|State of the enrollment|notContacted|
|Group Tag|string|None|False|Group tag of the autopilot device|example-tag|
|ID|string|None|False|Unique identifier for the autopilot device|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Last Contacted Date Time|string|None|False|The date when the device was last contacted|2021-06-24 00:37:04.588543+00:00|
|Managed Device ID|string|None|False|The identifier of the managed device|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Manufacturer|string|None|False|OEM manufacturer of the device|Example Manufacturer|
|Model|string|None|False|Model of the autopilot device|Example Model|
|Product Key|string|None|False|Product key of the device|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Purchase Order Identifier|string|None|False|The identifier of the purchase order|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Resource Name|string|None|False|Name of the resource|Example Name|
|Serial Number|string|None|False|Serial number of the device|1A2B3C4D|
|SKU Number|string|None|False|Stock Keeping Unit number of the device|ABCD1234|
|System Family|string|None|False|Family of the device system|example_family|
|User Principal Name|string|None|False|Principal name of the user|Example Name|

## Troubleshooting

*There is no troubleshooting for this plugin.*

# Version History

* 2.0.0 - Add new actions Get Device, Get Autopilot Device, Full Scan, Quick Scan, Delete Device from Intune, Delete Device from Autopilot | Change `client_secret` input type in connection | Remove `url` input from connection | Code refactor
* 1.3.0 - Add new action Get Managed Apps
* 1.2.2 - Add `docs_url` to plugin spec with link to [plugin setup guide](https://docs.rapid7.com/insightconnect/microsoft-intune/)
* 1.2.1 - Improve e-mail search in Search Devices action by performing an extended all device search for  `emailAddress` and `userPrincipalName` when email is not found
* 1.2.0 - Add new action Manage Device
* 1.1.0 - Add new actions Search Devices and Wipe
* 1.0.0 - Initial plugin creation, action Antivirus Scan added

# Links

* [Microsoft Intune](https://docs.microsoft.com/en-us/graph/)

## References

* [Microsoft Intune](https://docs.microsoft.com/en-us/graph/)
