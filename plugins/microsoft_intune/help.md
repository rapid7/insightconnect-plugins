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
|----|----|-------|--------|-----------|----|-------|
|clientId|string|None|True|Client ID, also called Application ID|None|a74dfb10-i33o-44e1-ba87-5fn2bb4e6b4d|
|clientSecret|credential_secret_key|None|True|Client secret key|None|kQDFcZoJYmxJpiS1x7rdyleyNFwhvLgcOZCkYG+5=|
|credentials|credential_username_password|None|True|E-mail address and password|None|{"username": "user@example.com", "password": "mypassword"}|
|tenantId|string|None|True|Tenant ID can be found in Active Directory|None|3a522933-ae5e-2b63-96ab-3c004b4f7f10|
|url|string|https://graph.microsoft.com|True|Base URL for the Microsoft endpoint|None|https://graph.microsoft.com|

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
  "tenantId": "3a522933-ae5e-2b63-96ab-3c004b4f7f10",
  "url": "https://graph.microsoft.com"
}
```

## Technical Details

### Actions

#### Delete Device from Intune

This action is used to delete the managed device from Intune.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|deviceId|string|None|True|ID of the managed device|None|9e8fd111-6c41-1111-85b9-11395662e111|

Example input:

```
{
  "deviceId": "9e8fd111-6c41-1111-85b9-11395662e111"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|------|
|success|boolean|True|Whether the scan was successful|True|

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
|----|----|-------|--------|-----------|----|-------|
|deviceId|string|None|True|ID of the device|None|9e8fd111-6c41-1111-85b9-11395662e111|

Example input:

```
{
  "deviceId": "9e8fd111-6c41-1111-85b9-11395662e111"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Whether the scan was successful|True|

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
|----|----|-------|--------|-----------|----|-------|
|deviceId|string|None|True|ID of the Autopilot device|None|9e8fd111-6c41-1111-85b9-11395662e111|

Example input:

```
{
  "deviceId": "9e8fd111-6c41-1111-85b9-11395662e111"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
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

#### Full Scan

This action is used to perform a full scan of the device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|deviceId|string|None|True|ID of the device|None|9e8fd111-6c41-1111-85b9-11395662e111|

Example input:

```
{
  "deviceId": "9e8fd111-6c41-1111-85b9-11395662e111"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|False|Whether the scan was successful|True|

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
|----|----|-------|--------|-----------|----|-------|
|deviceId|string|None|True|ID of the device|None|9e8fd111-6c41-1111-85b9-11395662e111|

Example input:

```
{
  "deviceId": "9e8fd111-6c41-1111-85b9-11395662e111"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|False|Whether the scan was successful|True|

Example output:

```
{
  "success": true
}
```

#### Get Device

This action is used to get information about the device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|deviceId|string|None|True|ID of the device|None|9e8fd111-6c41-1111-85b9-11395662e111|

Example input:

```
{
  "deviceId": "9e8fd111-6c41-1111-85b9-11395662e111"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
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
|----|----|-------|--------|-----------|----|-------|
|app|string|None|False|Application ID or name, if empty returns all applications|None|af6040ed-efe0-494c-89ed-89880989674c|

Example input:

```
{
  "app": "af6040ed-efe0-494c-89ed-89880989674c"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|managedApps|[]value|False|Application details|[]|

Example output:

```
{
  "managed_apps": [
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

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Return true if device was successfully wiped|True|

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

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
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

#### Manage Device

This action is used to perform management tasks on a device such as rebooting and syncing.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
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
|----|----|--------|-----------|-------|
|success|boolean|True|Return true if action was successfully performed on device|True|

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

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Return true if scan was initiated successfully|True|

Example output:

```
{
  "success": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### autopilotDevice

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Addressable User Name|string|False|Addressable user name|
|Azure Active Directory Device ID|string|False|The unique identifier for the Azure Active Directory device|
|Display Name|string|False|Display name of the device|
|Enrollment State|string|False|State of the enrollment|
|Group Tag|string|False|Group tag of the autopilot device|
|ID|string|False|Unique identifier for the autopilot device|
|Last Contacted Date Time|string|False|The date when the device was last contacted|
|Managed Device ID|string|False|The identifier of the managed device|
|Manufacturer|string|False|OEM manufacturer of the device|
|Model|string|False|Model of the autopilot device|
|Product Key|string|False|Product key of the device|
|Purchase Order Identifier|string|False|The identifier of the purchase order|
|Resource Name|string|False|Name of the resource|
|Serial Number|string|False|Serial number of the device|
|SKU Number|string|False|Stock Keeping Unit number of the device|
|System Family|string|False|Family of the device system|
|User Principal Name|string|False|Principal name of the user|

#### configurationManagerClientEnabledFeatures

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Odata Type|string|False|Odata type|
|Compliance Policy|boolean|False|Compliance policy|
|Device Configuration|boolean|False|Device configuration|
|Inventory|boolean|False|Inventory|
|Modern Apps|boolean|False|Modern apps|
|Resource Access|boolean|False|Resource access|
|Windows Update For Business|boolean|False|Windows update for business|

#### device

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Odata Type|string|False|Odata type|
|Activation Lock Bypass Code|string|False|Activation lock bypass code|
|Android Security Patch Level|string|False|Android security patch level|
|Azure AD Device ID|string|False|Azure AD device ID|
|Azure AD Registered|boolean|False|Azure AD registered|
|Compliance Grace Period Expiration Date Time|date|False|Compliance grace period expiration date time|
|Compliance State|string|False|Compliance state|
|Configuration Manager Client Enabled Features|configurationManagerClientEnabledFeatures|False|Configuration manager client enabled features|
|Device Action Results|[]deviceActionResults|False|Device action results|
|Device Category Display Name|string|False|Device category display name|
|Device Enrollment Type|string|False|Device enrollment type|
|Device Health Attestation State|deviceHealthAttestationState|False|Device health attestation state|
|Device Name|string|False|Device name|
|Device Registration State|string|False|Device registration state|
|EAS Activated|boolean|False|EAS activated|
|EAS Activation Date Time|date|False|EAS activation date time|
|EAS Device ID|string|False|EAS device ID|
|Email Address|string|False|Email address|
|Enrolled Date Time|date|False|Enrolled date time|
|Exchange Access State|string|False|Exchange access state|
|Exchange Access State Reason|string|False|Exchange access state reason|
|Exchange Last Successful Sync Date Time|date|False|Exchange last successful sync date time|
|Free Storage Space In Bytes|integer|False|Free storage space in bytes|
|ID|string|False|ID|
|IMEI|string|False|IMEI|
|Is Encrypted|boolean|False|Is encrypted|
|Is Supervised|boolean|False|Is supervised|
|Jail Broken|string|False|Jail broken|
|Last Sync Date Time|date|False|Last sync date time|
|Managed Device Name|string|False|Managed device name|
|Managed Device Owner Type|string|False|Managed device owner type|
|Management Agent|string|False|Management agent|
|Manufacturer|string|False|Manufacturer|
|MEID|string|False|MEID|
|Model|string|False|Model|
|Operating System|string|False|Operating system|
|OS Version|string|False|OS version|
|Partner Reported Threat State|string|False|Partner reported threat state|
|Phone Number|string|False|Phone number|
|Remote Assistance Session Error Details|string|False|Remote assistance session error details|
|Remote Assistance Session URL|string|False|Remote assistance session URL|
|Serial Number|string|False|Serial number|
|Subscriber Carrier|string|False|Subscriber carrier|
|Total Storage Space In Bytes|integer|False|Total storage space in bytes|
|User Display Name|string|False|User display name|
|User ID|string|False|User ID|
|User Principal Name|string|False|User principal name|
|Wifi MAC Address|string|False|Wifi MAC address|

#### deviceActionResults

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Odata Type|string|False|Odata type|
|Action Name|string|False|Action name|
|Action State|string|False|Action state|
|Last Updated Date Time|date|False|Last updated date time|
|Start Date Time|date|False|Start date time|

#### deviceHealthAttestationState

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Odata Type|string|False|Odata type|
|Attestation Identity Key|string|False|Attestation identity key|
|BitLocker Status|string|False|BitLocker status|
|Boot App Security Version|string|False|Boot app security version|
|Boot Debugging|string|False|Boot debugging|
|Boot Manager Security Version|string|False|Boot manager security version|
|Boot Manager Version|string|False|Boot manager version|
|Boot Revision List Info|string|False|Boot revision list info|
|Code Integrity|string|False|Code integrity|
|Code Integrity Check Version|string|False|Code integrity check version|
|Code Integrity Policy|string|False|Code integrity policy|
|Content Namespace URL|string|False|Content namespace URL|
|Content Version|string|False|Content version|
|Data Excution Policy|string|False|Data excution policy|
|Device Health Attestation Status|string|False|Device health attestation status|
|Early Launch Anti Malware Driver Protection|string|False|Early launch anti malware driver protection|
|Health Attestation Supported Status|string|False|Health attestation supported status|
|Health Status Mismatch Info|string|False|Health status mismatch info|
|Issued Date Time|date|False|Issued date time|
|Last Update Date Time|date|False|Last update date time|
|Operating System Kernel Debugging|string|False|Operating system kernel debugging|
|Operating System Rev List Info|string|False|Operating system rev list info|
|PCR0|string|False|PCR0|
|PCR Hash Algorithm|string|False|PCR hash algorithm|
|Reset Count|integer|False|Reset count|
|Restart Count|integer|False|Restart count|
|Safe Mode|string|False|Safe mode|
|Secure Boot|string|False|Secure boot|
|Secure Boot Configuration Policy Finger Print|string|False|Secure boot configuration policy finger print|
|Test Signing|string|False|Test signing|
|TPM Version|string|False|TPM version|
|Virtual Secure Mode|string|False|Virtual secure mode|
|Windows PE|string|False|Windows PE|

#### value

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Odata Context|string|False|Odata context|
|Odata Type|string|False|Odata type|
|App Availability|string|False|App availability|
|App Store URL|string|False|App store URL|
|Created Datetime|string|False|Created datetime|
|Description|string|False|Description|
|Developer|string|False|Developer|
|Display Name|string|False|Display Name|
|ID|string|False|ID|
|Information URL|string|False|Information URL|
|Is Featured|boolean|False|Is featured|
|Large Icon|object|False|Large icon|
|Last Modified Datetime|string|False|Last modified datetime|
|Minimum Supported Operating System|object|False|Minimum supported operating system|
|Notes|string|False|Notes|
|Owner|string|False|Owner|
|Package ID|string|False|Package ID|
|Privacy Information URL|string|False|Privacy information URL|
|Publisher|string|False|Publisher|
|Publishing State|string|False|Publishing state|
|Version|string|False|Version|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.0 - Add new actions Get Device, Get Autopilot Device, Full Scan, Quick Scan, Delete Device from Intune, Delete Device from Autopilot | Change `client_secret` input type in connection | Code refactor
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
