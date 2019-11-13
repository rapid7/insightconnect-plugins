# Description

This plugin runs a PowerShell script on a remote host or locally on the Komand host.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|False|Username and password|None|
|kerberos|kerberos|None|False|Connection information required for Kerberos|None|
|port|integer|5986|False|Port number, defaults are 5986 for SSL and 5985 for unencrypted|None|
|auth|string|None|True|Authentication type|['NTLM', 'Kerberos', 'None', 'CredSSP']|

## Technical Details

### Actions

#### PowerShell String

This action is used to execute a PowerShell script in the form of a string on a remote host or locally on the Komand host.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|script|string|None|True|PowerShell script as a string|None|
|host_name|string|None|False|Case-sensitive name of the remote host, eg. MyComputer for Kerberos connection only|None|
|address|string|None|True|IP address of the remote host e.g. 192.168.1.1|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|stderr|string|False|PowerShell standard error|
|stdout|string|False|PowerShell standard output|

Example output:

```

{
  "stdout": "Mr $test  $test2\r\nMr bob  said hello\r\nbob \n  said hello\r\n5\r\ntesting chars in lit string \\ / \\r /r // \\\\ ! @ ## $ %\r\ntesting chars in interpreted string // \\\\ /r/n ! @ ## $\r\n\r\nPath            \r\n----            \r\nC:\\Users\\mhofert\r\nC:\\Users        \r\nC:\\             \r\n\r\n\r\n",
  "stderr": "#< CLIXML\r\n<Objs Version=\"1.1.0.1\" xmlns=\"http://schemas.microsoft.com/powershell/2004/04\"><Obj S=\"progress\" RefId=\"0\"><TN RefId=\"0\"><T>System.Management.Automation.PSCustomObject</T><T>System.Object</T></TN><MS><I64 N=\"SourceId\">1</I64><PR N=\"Record\"><AV>Preparing modules for first use.</AV><AI>0</AI><Nil /><PI>-1</PI><PC>-1</PC><T>Completed</T><SR>-1</SR><SD> </SD></PR></MS></Obj><Obj S=\"progress\" RefId=\"1\"><TNRef RefId=\"0\" /><MS><I64 N=\"SourceId\">1</I64><PR N=\"Record\"><AV>Preparing modules for first use.</AV><AI>0</AI><Nil /><PI>-1</PI><PC>-1</PC><T>Completed</T><SR>-1</SR><SD> </SD></PR></MS></Obj></Objs>"
}

```

#### Execute Script

This action is used to execute a PowerShell script on a remote host or locally on the Komand host.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|script|bytes|None|True|PowerShell script as base64|None|
|host_name|string|None|False|Case-sensitive name of the remote host, eg. MyComputer for Kerberos connection only|None|
|address|string|None|True|IP address of the remote host e.g. 192.168.1.1|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|stderr|string|False|PowerShell standard error|
|stdout|string|False|PowerShell standard output|

Example output:

```

{
  "stdout": "Mr $test  $test2\r\nMr bob  said hello\r\nbob \n  said hello\r\n5\r\ntesting chars in lit string \\ / \\r /r // \\\\ ! @ ## $ %\r\ntesting chars in interpreted string // \\\\ /r/n ! @ ## $\r\n\r\nPath            \r\n----            \r\nC:\\Users\\mhofert\r\nC:\\Users        \r\nC:\\             \r\n\r\n\r\n",
  "stderr": "#< CLIXML\r\n<Objs Version=\"1.1.0.1\" xmlns=\"http://schemas.microsoft.com/powershell/2004/04\"><Obj S=\"progress\" RefId=\"0\"><TN RefId=\"0\"><T>System.Management.Automation.PSCustomObject</T><T>System.Object</T></TN><MS><I64 N=\"SourceId\">1</I64><PR N=\"Record\"><AV>Preparing modules for first use.</AV><AI>0</AI><Nil /><PI>-1</PI><PC>-1</PC><T>Completed</T><SR>-1</SR><SD> </SD></PR></MS></Obj><Obj S=\"progress\" RefId=\"1\"><TNRef RefId=\"0\" /><MS><I64 N=\"SourceId\">1</I64><PR N=\"Record\"><AV>Preparing modules for first use.</AV><AI>0</AI><Nil /><PI>-1</PI><PC>-1</PC><T>Completed</T><SR>-1</SR><SD> </SD></PR></MS></Obj></Objs>"
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

If Auth Type is set to "None" the PowerShell script will execute locally on the Komand host.
This can also by accomplished by leaving the address field blank.

The username supplied must have local admin privileges on the remote host Windows computer.
When using a domain account with NTLM the username must be in the following format MYDOMAIN\username
When using the Kerberos connection option the username must be a domain account that has permission to join computers to the domain.

This plugin can connect over HTTP, the default port for this is 5985. It should be noted that this type of connection is
not secure as all information passed is in plain text. In addition, Windows will not allow HTTP connections by default.
The following commands must be run on the Windows computer that you want to connect to.

For more information see [Compromising Yourself with WinRM's AllowUnencrypted = True](https://blogs.msdn.microsoft.com/powershell/2015/10/27/compromising-yourself-with-winrms-allowunencrypted-true/)

```

winrm set winrm/config/client/auth '@{Basic="true"}'
winrm set winrm/config/service/auth '@{Basic="true"}'
winrm set winrm/config/service '@{AllowUnencrypted="true"}'

```

When using the Kerberos connection option, the username should not include an @example.com or other domain identifier. These will be added by the plugin as needed.

This plugin will join the Komand docker instance to the Windows domain as a computer if the Kerberos option is used.

For the Execute Script action PowerShell code should be submitted as base64. This can be done by
copying a `.txt` file with the PowerShell code into the plugin.

This plugin does not validate the PowerShell code.

Any errors generated on the remote computer by the PowerShell code
are forwarded to the log file.

Run this PowerShell command on a Windows host first to set up a unsigned certificate for authentication:
This will not be needed if the host alredy has a SSL certificate set up for Winrm

```

Invoke-Expression ((New-Object System.Net.Webclient).DownloadString('https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1'))

```

# Version History

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

## References

* [pywinrm library](https://pypi.python.org/pypi/pywinrm)
* [samba-common](https://packages.debian.org/sid/samba-common)
* [krb5-user](https://packages.debian.org/search?keywords=krb5-user)
* [realmd](https://packages.debian.org/jessie/admin/realmd)

