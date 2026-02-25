# Description

[PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-6) is a task-based command-line shell and scripting language from Microsoft that helps system administrators, power-users, and InsightConnect customers rapidly automate tasks that manage operating systems and processes. This plugin runs a PowerShell script on a remote host or locally on an InsightConnect Orchestrator

# Key Features

* Run a PowerShell script to manage (remote) computers from the command line

# Requirements

* For local Orchestrator execution, ensure connectivity to any network resources the script will use
* For remote server execution, a PowerShell-enabled server and administrative credentials
* When adding a password for the script, try to avoid special or escape characters such as single or double quotes
* The use of round-robin DNS lookups is not supported

# Supported Product Versions

* PowerShell 7.5.4

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|auth|string|None|True|Authentication type|["NTLM", "Kerberos", "CredSSP", "None"]|Kerberos|None|None|
|credentials|credential_username_password|None|False|Username and password|None|{"username": "user", "password": "mypassword"}|None|None|
|kerberos|kerberos|None|False|Connection information required for Kerberos|None|{"kdc": "10.0.1.11", "domain": "EXAMPLE.domain"}|None|None|
|port|integer|5986|False|Port number, defaults are 5986 for SSL and 5985 for unencrypted|None|5986|None|None|
|script_secret_key|credential_secret_key|None|False|Credential secret key available in script as PowerShell variable (`$secret_key`)|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|script_username_and_password|credential_username_password|None|False|Username and password available in script as PowerShell variables (`$username`, `$password`)|None|{"username": "user", "password": "mypassword"}|None|None|

Example input:

```
{
  "auth": "None",
  "credentials": {
    "password": "mypassword",
    "username": "user"
  },
  "kerberos": {
    "domain": "EXAMPLE.domain",
    "kdc": "10.0.1.11"
  },
  "port": 5986,
  "script_secret_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "script_username_and_password": {
    "password": "mypassword",
    "username": "user"
  }
}
```

## Technical Details

### Actions


#### Execute Script

This action is used to execute PowerShell script encoded as a base64 file on a remote host

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|False|IP address of the remote host e.g. 192.168.1.1. If address is left blank PowerShell will run locally|None|10.0.1.15|None|None|
|host_name|string|None|False|Case-sensitive name of the remote host, eg. MyComputer for Kerberos connection only|None|windows|None|None|
|script|bytes|None|True|PowerShell script as base64. In this action you can use `$username`, `$password`, `$secret_key` variables if defined in connection|None|R2V0LURhdGU=|None|None|
  
Example input:

```
{
  "address": "10.0.1.15",
  "host_name": "windows",
  "script": "R2V0LURhdGU="
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|stderr|string|False|PowerShell standard error|Fatal error.|
|stdout|string|False|PowerShell standard output|Tuesday, January 11, 2022 5:05:42 AM|
  
Example output:

```
{
  "stderr": "Fatal error.",
  "stdout": "Tuesday, January 11, 2022 5:05:42 AM"
}
```

#### PowerShell String

This action is used to execute PowerShell script in the form of a string

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|False|IP address of the remote host e.g. 192.168.1.1. If address is left blank PowerShell will run locally|None|10.0.1.17|None|None|
|host_name|string|None|False|Case-sensitive name of the remote host, eg. MyComputer for Kerberos connection only|None|windows|None|None|
|script|string|None|True|PowerShell script as a string. In this action you can use `$username`, `$password`, `$secret_key` variables if defined in connection|None|Get-Date|None|None|
  
Example input:

```
{
  "address": "10.0.1.17",
  "host_name": "windows",
  "script": "Get-Date"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|stderr|string|False|PowerShell standard error|Fatal error.|
|stdout|string|False|PowerShell standard output|Tuesday, January 11, 2022 5:05:42 AM|
  
Example output:

```
{
  "stderr": "Fatal error.",
  "stdout": "Tuesday, January 11, 2022 5:05:42 AM"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**kerberos**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Domain Name|string|None|False|The fully qualified domain name of the remote host e.g. example.com. If Auth Type is set to None then leave this blank|None|
|KDC|string|None|False|IP address of the Active Directory server. If Auth Type is set to None then leave this blank|None|


## Troubleshooting

* The use of round-robin DNS lookups is not supported
* If Auth Type is set to "None" the PowerShell script will execute locally on the Komand host. This can also be accomplished by leaving the address field blank.
* The username supplied must have local admin privileges on the remote host Windows computer.
* When using a domain account with NTLM the username must be in the following format MYDOMAIN\username
* When using the Kerberos connection option the username must be a domain account that has permission to join computers to the domain.
* This plugin can connect over HTTP, the default port for this is 5985.
It should be noted that this type of connection is not secure as all information passed is in plain text. In addition, Windows will not allow HTTP connections by default.
 
The following commands must be run on the Windows computer that you want to connect to.

For more information see [Compromising Yourself with WinRM's AllowUnencrypted = True](https://blogs.msdn.microsoft.com/PowerShell/2015/10/27/compromising-yourself-with-winrms-allowunencrypted-true/)
 
```
winrm set winrm/config/client/auth '@{Basic="true"}'
winrm set winrm/config/service/auth '@{Basic="true"}'
winrm set winrm/config/service '@{AllowUnencrypted="true"}'
```

* When using the Kerberos connection option, the username should not include an @example.com or other domain identifier. These will be added by the plugin as needed.
This plugin will join the Komand docker instance to the Windows domain as a computer if the Kerberos option is used.
For the Execute Script action PowerShell code should be submitted as base64. This can be done by copying a `.txt` file with the PowerShell code into the plugin.

_This plugin does not validate the PowerShell code._
 Any errors generated on the remote computer by the PowerShell code are forwarded to the log file.

Run this PowerShell command on a Windows host first to set up a unsigned certificate for authentication:
This will not be needed if the host already has a SSL certificate set up for Winrm

```
Invoke-Expression ((New-Object System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1'))
```
* SSL is not configured for port `5985`

# Version History

* 3.0.13 - Updated dependencies
* 3.0.12 - Updated dependencies | Updated SDK to the latest version (6.4.3)
* 3.0.11 - Updated dependencies | Updated SDK to the latest version (6.4.1)
* 3.0.10 - Resolved Snyk Vulnerabilities | SDK bump to latest version (6.3.7)
* 3.0.9 - Resolved Snyk Vulnerability | SDK bump to latest version (6.3.6)
* 3.0.8 - Updated clean message | Updated SDK to the latest version (6.2.5) | bumping `cryptography` package
* 3.0.7 - Updated dependencies | Updated SDK to the latest version
* 3.0.6 - Bump SDK to 6.2.0
* 3.0.5 - Bump requirements.txt | Bump SDK to 6.1.4 | Update help.md to enforce that the use of round-robin DNS lookups is not supported
* 3.0.4 - Upgrade user from `nobody` to `root` | bump SDK to 6.0.1 and switch back to `Bullseye` based SDK image
* 3.0.3 - Fix decoding error in `Execute Script` action | Update SDK | Update packages for alpine image
* 3.0.2 - Updated the SDK version to include output masking | Updated all the dependencies to the newest versions
* 3.0.1 - Bug fix - Fix issue where single quotes in password causes parsing error
* 3.0.0 - Move custom script credentials to Connection | Update runtime to insightconnect_plugin_runtime
* 2.2.0 - Add custom credentials in Execute Script and PowerShell String actions | Update plugin to allow unencrypted connections when connection is targeting port 5985
* 2.1.4 - Update `docs_url` in plugin spec with a new link to [plugin setup guide](https://docs.rapid7.com/insightconnect/mass-delete-with-powershell/)
* 2.1.3 - Correct spelling in help.md
* 2.1.2 - Add `docs_url` to plugin spec with link to [plugin setup guide](https://insightconnect.help.rapid7.com/docs/mass-delete-with-powershell)
* 2.1.1 - New spec and help.md format for the Extension Library
* 2.1.0 - Add functionality to allow CredSSP connections
* 2.0.1 - Fix issue with unicode characters
* 2.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 1.1.0 - Add functionality to allow PowerShell to execute locally
* 1.0.2 - Bug fix for NTLM version `stdout` output property name in String action
* 1.0.1 - Bug fix for `stdout` output property name in String action
* 1.0.0 - Updated PyWinrm, bugfixes, add PowerShell String action
* 0.2.1 - Bug fix and improved error handling
* 0.2.0 - Allow connections on a Windows domain with Kerberos
* 0.1.0 - Initial plugin

# Links

* [InsightConnect Powershell Plugin Guide](https://docs.rapid7.com/insightconnect/mass-delete-with-PowerShell/)

## References

* [pywinrm library](https://pypi.python.org/pypi/pywinrm)
* [samba-common](https://packages.debian.org/sid/samba-common)
* [krb5-user](https://packages.debian.org/search?keywords=krb5-user)
* [realmd](https://packages.debian.org/jessie/admin/realmd)