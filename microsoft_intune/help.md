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
|client_id|string|None|True|Client ID, also called Application ID|None|aaaa55aa-a55a-5a5a-5aa5-aaaaa555aaa|
|client_secret|string|None|True|Client secret key|None|kQDFcZoJYmxJpiS1x7rdyleyNFwhvLgcOZCkYG+5=|
|credentials|credential_username_password|None|True|E-mail address and password|None|{"username": "user@example.com", "password": "mypassword"}|
|tenant_id|string|None|True|Tenant ID can be found in Active Directory|None|aaaa55aa-a55a-5a5a-5aa5-aaaaa555aaa|
|url|string|https://graph.microsoft.com|True|Base URL for the Microsoft endpoint|None|https://graph.microsoft.com|

Example input:

```
{
  "client_id": "aaaa55aa-a55a-5a5a-5aa5-aaaaa555aaa",
  "client_secret": "kQDFcZoJYmxJpiS1x7rdyleyNFwhvLgcOZCkYG+5=",
  "credentials": {
    "username": "user@example.com",
    "password": "mypassword"
  },
  "tenant_id": "aaaa55aa-a55a-5a5a-5aa5-aaaaa555aaa",
  "url": "https://graph.microsoft.com"
}
```
## Technical Details

### Actions

#### Antivirus Scan

This action is used to initiate a Windows Defender Antivirus scan on a machine.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|device|string|None|True|Search devices by device name, user ID, email address, or device ID|None|aaaa55aa-a55a-5a5a-5aa5-aaaaa555aaa|
|update|boolean|False|False|If true the action with update Antivirus Signatures before scan|None|True|

Example input:

```
{
  "device": "aaaa55aa-a55a-5a5a-5aa5-aaaaa555aaa",
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

* 1.0.0 - Initial plugin creation, action Antivirus Scan added

# Links

## References

* [Microsoft Intune](https://docs.microsoft.com/en-us/graph/)
