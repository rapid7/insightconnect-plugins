
# Rapid7 Metasploit

## About

[Metasploit Framework](https://www.metasploit.com/) is the world's most used penetration testing framework.
This plugin utilizes the Metasploit [RPC API](https://metasploit.help.rapid7.com/docs/rpc-api).

## Actions

### Search for Exploit

This action is used to search for an exploit within Metasploit over an RPC session.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|search_term|string|None|True|Search term, e.g. 'vsftp'|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|exploits|[]string|False|A list of exploits found searching Metasploit|

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

### Execute Exploit

This action is used to run a selected Metasploit exploit.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|options|object|None|False|Metasploit module options|None|
|module|string|None|False|A Metasploit module|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|session_information|[]session_info|False|Session information provided when a module is executed|
|console_output|[]string|False|Information from the console when a module is executed|

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

## Triggers

### New Modules

This trigger is used to check for new Metasploit modules.

#### Input

This action does not contain any inputs.

#### Output

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
    "author": ["Kristian Erik Hermansen", "Sagi Shahar <blah@example.com>",
    "Kostas Lintovois <kostas.lintovois@mwrinfosecurity.com>"],
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

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|msf|False|Username|None|
|ssl|boolean|True|False|Use SSL|None|
|port|integer|55553|False|Port|None|
|password|password|None|True|Password|None|
|uri|string|/api/|False|The msfrpcd URI|None|
|server|string|None|False|Remote Server IP|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Versions

* 0.1.0 - Initial plugin
* 1.0.0 - Trigger added: New Modules
* 1.0.1 - Update Ruby script release
* 1.0.2 - Bugfix: Plugin could occasionally crash due to unhandled unicode characters while searching for exploits
* 1.0.3 - Support web server mode
* 1.0.4 - Update to use new JSON API
* 2.0.0 - Update to new credential types

## Workflows

Examples:

* Search for existing Metasploit exploits based on service or version
* Remotely execute a Metasploit module and return information on the findings

## References

* [Metasploit](https://www.metasploit.com/)
* [RPC API](https://metasploit.help.rapid7.com/docs/rpc-api)
