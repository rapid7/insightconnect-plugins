# Description

[Finger](https://linux.die.net/man/1/finger) is a utility that queries a `finger` daemon for information. This plugin uses GNU Finger to get information about a system's user.
For example, from the command line:

```

$ finger user@example.com
[server.com]
Trying ...
-----------------------------------------------------------------------------
Username: bross            Real name: Bob Ross
Home: /home/bross/         Shell: /bin/bash
Room: 506                  Work phone: 222-333-4444
Home phone:

This user has no mail or mail spool.

```

# Key Features

* Retrieve information about a user

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Finger

This action is used to retrieve information about a user account.

##### Input

It accepts a user to query and a `finger` host (IP or domain) to perform the query.

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|True|Finger server host|None|
|user|string|None|True|User|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|Whether user exists on the system|
|fullname|string|False|User's full name|
|home|string|False|Path to user's home directory|
|homephone|string|False|User home phone|
|login|string|False|User's login name|
|loginfrom|string|False|User's last login source address|
|loginstatus|string|False|When the user logged in|
|mail|string|False|Mail forward address if it exists|
|mailstatus|string|False|Status on unread mail|
|plan|string|False|The contents of the plan file if it exists|
|project|string|False|The contents of the project file if it exists|
|pubkey|string|False|The contents of user's public key if it exists|
|room|string|False|User room|
|shell|string|False|The user's default shell|
|status|string|False|Success or any error messages|
|workphone|string|False|User work phone|

The plugin can return the following properties:

* Home - Path to user's home directory
* Found - Whether user exists on the system
* Full Name - User's full name
* Login - User's login name
* Login From - User's last login source address
* Login Status - When the user logged in
* Mail - Mail forward address if it exists
* Mail Status - Status on unread mail
* Plan - The contents of the plan file if it exists
* Project - The contents of the project file if it exists
* Pub Key - The contents of user's public key if it exists
* Shell - The user's default shell
* Status - Success or any error messages

Some properties will not be returned if `finger` has no information about them.

On success, the raw output will look like the following:

```

{
  "status": "Success",
  "shell": "/sbin/sh",
  "mailstatus": "No unread mail",
  "plan": "No plan",
  "loginstatus": "Never logged in",
  "found": true,
  "home": "/",
  "fullname": "Super-User",
  "loginfrom": "Never logged in",
  "login": "root"
}

```

On failure, the raw output may look like the following:

```

{
  "status": "finger: connect: Connection timed out",
  "found": false
}

```

##### Notes

If a user does not exist on the system but the `finger` daemon gives a response that doesn't contain stderr then `found` will be set to `true`.
This is a best guess for determining whether the user actually exists because some `finger` daemons will not return any or very little information
about a user that exists. We can improve this in the future.

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Some `finger` daemons return answers in a different format which will cause this plugin to be unable to interpret the data correctly.

# Version History

* 1.0.2 - Change docker image from `komand/python-2-plugin` to `komand/python-3-37-plugin:3` to use python 3 | Use input and output constants | Changed variables names to more readable | Changed descriptions | Added "f" strings | Removed method test from action
* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Finger](https://linux.die.net/man/1/finger)

