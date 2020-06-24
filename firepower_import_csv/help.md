# Description

The [Cisco Firepower](https://www.cisco.com/c/en/us/products/security/firepower-management-center/index.html) plugin adds scan results from a CSV file. 

The plugin will create a Firepower formatted comma separated values (CSV) of commands from an input CSV file. 
It will then SCP that file onto the server and use SSH to run nmimport.pl

# Key Features

Import comma separated values (CSV) file of vulnerabilities to Firepower 

# Requirements

* Firepower server IP
* SSH credentials to the the Firepower server

# Documentation

## Setup

Before running this plugin, nmimport needs to be added to the sudoers file on the Firepower server. 

To do this SSH into the Firepower server and run  

`sudo visudo`

At the bottom of the sudoers file add these lines: 

```
# Needed for CVS import from InsightConnect
admin fmc-6-3-0 = (root) NOPASSWD: /usr/local/sf/bin/nmimport.pl /Volume/home/admin/firepower_import.csv
```

This allows the plugin to run `sudo nmimport.pl` without providing a password.  

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|server|string|None|False|Enter the address for the server|None|198.51.100.100|
|username_password|credential_username_password|None|False|Username and password used to SSH into the Firepower server|None|{"username": "username", "password": "password"}|

Example input:

```
{
  "server": "198.51.100.100",
  "username_password": "{\"username\": \"username\", \"password\": \"password\"}"
}
```


## Technical Details

### Actions

#### Import CSV

This action is used to import a base64 encoded CSV of vulnerabilities.

NOTE: This action is limited to around 100-200 vulnerabilities. If too many records are processed at one time Firepower
will unexpectedly hang with no warnings or timeouts. This is based on a 4 core server with 32gb of ram.  

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|csv|bytes|None|True|CSV of vulnerabilities|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|

Example input:

```
{
  "csv": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|string|False|Results from the import utility on the Firepower server|
|success|boolean|True|Was import successful|

Example output:

```
{
  "result": "Done processing 108 commands.",
  "success": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

The import CSV action is limited to around 100-200 vulnerabilities. If too many records are processed at one time Firepower
unexpectedly hangs with no warnings or timeouts. This is based on a 4 core server with 32gb of ram. 

If this plugin hangs for a long time, try to batch the input CSV into smaller CSVs. 

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Cisco Firepower](https://www.cisco.com/c/en/us/products/security/firepower-management-center/index.html)
