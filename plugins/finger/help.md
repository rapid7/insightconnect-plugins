# Description

Query the Finger Service

# Key Features

* Query the Finger Service for user information

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2026-02-13

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Finger

This action is used to ask finger about a username

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|host|string|None|True|Finger server host|None|example.com|None|None|
|user|string|None|True|User|None|John Smith|None|None|
  
Example input:

```
{
  "host": "example.com",
  "user": "John Smith"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|False|Whether user exists on the system|True|
|fullname|string|False|User's full name|John Smith|
|home|string|False|Path to user's home directory|/home/jsmith|
|homephone|string|False|User home phone|555-555-5555|
|login|string|False|User's login name|user@example.com|
|loginfrom|string|False|User's last login source address|0.0.0.0|
|loginstatus|string|False|When the user logged in|2024-01-01 12:00:00|
|mail|string|False|Mail forward address if it exists|johnsmith@email.com|
|mailstatus|string|False|Status on unread mail|Mail last read|
|plan|string|False|The contents of the plan file if it exists|Plan A|
|project|string|False|The contents of the project file if it exists|Project X|
|pubkey|string|False|The contents of user's public key if it exists|ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC...|
|room|string|False|User room|Room 101|
|shell|string|False|The user's default shell|/bin/bash|
|status|string|False|Success or any error messages|Success|
|workphone|string|False|User work phone|555-555-5555|
  
Example output:

```
{
  "found": true,
  "fullname": "John Smith",
  "home": "/home/jsmith",
  "homephone": "555-555-5555",
  "login": "user@example.com",
  "loginfrom": "0.0.0.0",
  "loginstatus": "2024-01-01 12:00:00",
  "mail": "johnsmith@email.com",
  "mailstatus": "Mail last read",
  "plan": "Plan A",
  "project": "Project X",
  "pubkey": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC...",
  "room": "Room 101",
  "shell": "/bin/bash",
  "status": "Success",
  "workphone": "555-555-5555"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.0.3 - Updated SDK version to 6.4.3
* 1.0.2 - Change docker image from `komand/python-2-plugin` to `komand/python-3-37-plugin:3` to use python 3 | Use input and output constants | Changed variables names to more readable | Changed descriptions | Added "f" strings | Removed method test from action
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Support web server mode
* 0.1.1 - SSL bug fix in SDK -0.1.0 - Initial plugin

# Links

* [Finger](https://www.ibm.com/docs/en/aix/7.2.0?topic=f-finger-command)

## References

* [Finger](https://www.ibm.com/docs/en/aix/7.2.0?topic=f-finger-command)