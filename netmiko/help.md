# Description

[Netmiko](https://github.com/ktbyers/netmiko) is a network device configuration tool that sends commands over
SSHv2. Netmiko is a fork of Paramiko. The Netmiko plugin is used to send commands to a network device over SSH.
Multiple commands can be sent over in a single SSH session.

# Key Features

* Automate network configuration
* Multiple SSH commands can be provided in one action

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password to run commands as|None|{"username": "user@example.com", "password": "mypassword"}|
|device_type|string|None|True|The type of device to connect|['a10', 'accedian', 'alcatel_aos', 'alcatel_sros', 'arista_eos', 'aruba_os', 'avaya_ers', 'avaya_vsp', 'brocade_fastiron', 'brocade_netiron', 'brocade_nos', 'brocade_vdx', 'brocade_vyos', 'checkpoint_gaia', 'calix_b6', 'ciena_saos', 'cisco_asa', 'cisco_ios', 'cisco_nxos', 'cisco_s300', 'cisco_tp', 'cisco_wlc', 'cisco_xe', 'cisco_xr', 'coriant', 'dell_force10', 'dell_powerconnect', 'eltex', 'enterasys', 'extreme', 'extreme_wing', 'f5_ltm', 'fortinet', 'generic_termserver', 'hp_comware', 'hp_procurve', 'huawei', 'juniper', 'juniper_junos', 'linux', 'mellanox', 'mrv_optiswitch', 'netapp_cdot', 'ovs_linux', 'paloalto_panos', 'pluribus', 'quanta_mesh', 'ruckus_fastiron', 'ubiquiti_edge', 'ubiquiti_edgeswitch', 'vyatta_vyos', 'vyos']|linux|
|host|string|None|True|Remote Host|None|example.com|
|key|credential_asymmetric_key|None|False|A base64 encoded SSH private key to use to authenticate to network device|None|LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFcFFJQkFBS0NBUUVBakdub1V0ZlBIcXZYM1BJVTZOOUZLbXdRM1psK05vYVdiNHlNTGh1ZGtkRUJKM0F1CitJOFFkbHFES0JtNjU2VWVPQ2gzci9pOWUwVUxLeGtYREZmS21jM3AyV3YrMGxWT1lHdnhaRktVd0tIMHJpQUwKQTRpbXlZdUwvZndlT1NHU25RbGdZS3I5OUhjaVRCSWRMMTVTWjMyVGpZYitQRFpCbCs2elFzdzJIWU5KY3FNagppY2lDN0NBajZnQjlTTzh4MXZNc1JrVStycUt1YzJyOFVrK3FoRUN3OHpSNEs2NndGdVlNMTdzR1VNWFVxL3BICldkaUV2TzNxL21kSzQ3TnJ4NWkyYmFDN281UlhzcEtIWXk2WGVyNFZibmlwbDREZ0FLa2FOT0wwMmErWnYzOFEKbCt4eTl3ZG1XcVVJYk1pcVNiai9rNnh4RGlQUWtUUisvMDMyZVFJREFRQUJBb0lCQUVrUHpwQlV0UFFickozTgo1UzFyQjcxVUw4NXUwT3FrUzJETnZCODl4VmFiYjBOTEwxV3NjMzl5QjI3MVBIak9SUlFwa21XaFEwOENGUmFlCjNveFFuaDQ3cytPck94UE15WlNJZGptaWNyNXRSempYZVlPa05rMEc3SmdDK09MM1lpZU9PblR5WkdReEhVcUIKM21mSVo0NXNIRHYzTXhDM2xwZnMzNS94VEhNOEUvZ1cvZ1RmdlUzUWJvUWFMMXEvdGFSUVlFSHZnaXV0d2RaMApzRUZ0SjhlQXdPQkFCWGlWM1FQeG5BUWdJcHdZcGJpY2wzQUsxNWdzNUVOSzRSbmdpMmJJN2hkbU13RFdhNnQvCmcwQ1AwVGl0eUZxMDVKVW1uYXo0d2VrWHhENUVCbTc3NkVZTlNveFRDYVN6VE1Zd1pDSVRycVhsNlk0L29nZVQKdVZTbTlaRUNnWUVBN0c4Q3l5REtEVEJZb0l5RWtuSlZLU3d1ZWxPQTJlZHhtVnlLTDhoTG9QaXExUW9TSC9OMQozMG5OL0dWY3ZEN1FFRDRwL3UwWGFNdVBtMkhWaHVYd3h1L3Q5ajExRFZsS1A3UXNIOXU0cEpLeml3Nk5tVjVOCi85K21jamRXQUg1QnFhSnRtcEYwdW9ac1drNDFKVmUwZkE3YTNGQ3JYcDFVL0dEOUJLU0FEMDBDZ1lFQW1BaW8KQ2hFaDcrcEQ3dnV0Rjg1dStGcWJkalkrS215RmVUUGQyNzE3UDZpNVY2QzZsVnBjbk03dm9abEd5MGZqb2FsZAplOW50bTBWVThGWmtVSWloS1B6VzkvTFNBVjhCZ08rdlNRck4vSU1FbURxb2w5NTlJeHhJLzZ5emtZNUp3WVJQCm1sd29OelUwZWtjSHpnMGV1N0RBMXV6UmZ2NEYxTlVXK1F5bFJkMENnWUVBenIwN09oZFAxanlDSXREOFUzbjYKRVdoNnM2ZzBzVlY1dGRwL1VzelhwTWdMeVFGblc5enRJdlJNVS9qbUlBemtybTlORllhSHc3REx2OWpLZDR5MAovNTlvK3JvK2tnK1RweVNLdU1qT0tjbkZpVUNPZko5RG9Rd1ZaU1lSNDVpREhpdlRueWExWlN5SnJtVllmM0N6CmR3OGVQU3VremJUUlRXWVptR2VuT3JrQ2dZRUFob082TWRZQXdlWHpIMEo4WHNEZVBFem1tY3ZhYXV6RGwzNUYKZ0lPQXhjMUIxMzgxTnFuUm9VZ1NpMWN6Wk82QlArcTY5TGJYM1BhVjlXTnF0RHArNU9YNFNUOEZnZ01PTUlkZwovbTVaM0Y0THRhakl2RDQxVjloUjJpMXlYNG1XUm1zTGgxYWNtbVF2dnpTVGVrTHZlejhqRDhaT2dWNjl5QmFWCmtkc1hhOTBDZ1lFQWsrNmdocFhOa3UxMlVBTmY5TUg4bG9OKzM1L2lQZWVvcWYwTVk1Rk1WUll4MTBaQTkxTGgKaWVBY3pWaGlxenhDdEhXaExBNFN4RTk2MmVnK2ppL2F3a1M0a1hMQ011WklFU0UrakZjN3B0VW1KamxzT1dqdgo4L2RxVUg1eWpSS3MycXhrQldHNEhtVDNOeDZBOHNZSXJVWXh5cVZMQnBHOHlLbmdibmFZUFY0PQotLS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQ==|
|port|integer|22|True|Remote port|None|22|
|secret|credential_secret_key|None|False|API secret key|None|b42ec8b4-deb2-c75e-ebd0-132d63f8e8d4|
|verbose|boolean|False|True|Additional messages to standard output|None|True|

Example input:

```
{
  "credentials": {
    "username": "user@example.com",
    "password": "mypassword"
  },
  "device_type": "linux",
  "host": "example.com",
  "key": "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFcFFJQkFBS0NBUUVBakdub1V0ZlBIcXZYM1BJVTZOOUZLbXdRM1psK05vYVdiNHlNTGh1ZGtkRUJKM0F1CitJOFFkbHFES0JtNjU2VWVPQ2gzci9pOWUwVUxLeGtYREZmS21jM3AyV3YrMGxWT1lHdnhaRktVd0tIMHJpQUwKQTRpbXlZdUwvZndlT1NHU25RbGdZS3I5OUhjaVRCSWRMMTVTWjMyVGpZYitQRFpCbCs2elFzdzJIWU5KY3FNagppY2lDN0NBajZnQjlTTzh4MXZNc1JrVStycUt1YzJyOFVrK3FoRUN3OHpSNEs2NndGdVlNMTdzR1VNWFVxL3BICldkaUV2TzNxL21kSzQ3TnJ4NWkyYmFDN281UlhzcEtIWXk2WGVyNFZibmlwbDREZ0FLa2FOT0wwMmErWnYzOFEKbCt4eTl3ZG1XcVVJYk1pcVNiai9rNnh4RGlQUWtUUisvMDMyZVFJREFRQUJBb0lCQUVrUHpwQlV0UFFickozTgo1UzFyQjcxVUw4NXUwT3FrUzJETnZCODl4VmFiYjBOTEwxV3NjMzl5QjI3MVBIak9SUlFwa21XaFEwOENGUmFlCjNveFFuaDQ3cytPck94UE15WlNJZGptaWNyNXRSempYZVlPa05rMEc3SmdDK09MM1lpZU9PblR5WkdReEhVcUIKM21mSVo0NXNIRHYzTXhDM2xwZnMzNS94VEhNOEUvZ1cvZ1RmdlUzUWJvUWFMMXEvdGFSUVlFSHZnaXV0d2RaMApzRUZ0SjhlQXdPQkFCWGlWM1FQeG5BUWdJcHdZcGJpY2wzQUsxNWdzNUVOSzRSbmdpMmJJN2hkbU13RFdhNnQvCmcwQ1AwVGl0eUZxMDVKVW1uYXo0d2VrWHhENUVCbTc3NkVZTlNveFRDYVN6VE1Zd1pDSVRycVhsNlk0L29nZVQKdVZTbTlaRUNnWUVBN0c4Q3l5REtEVEJZb0l5RWtuSlZLU3d1ZWxPQTJlZHhtVnlLTDhoTG9QaXExUW9TSC9OMQozMG5OL0dWY3ZEN1FFRDRwL3UwWGFNdVBtMkhWaHVYd3h1L3Q5ajExRFZsS1A3UXNIOXU0cEpLeml3Nk5tVjVOCi85K21jamRXQUg1QnFhSnRtcEYwdW9ac1drNDFKVmUwZkE3YTNGQ3JYcDFVL0dEOUJLU0FEMDBDZ1lFQW1BaW8KQ2hFaDcrcEQ3dnV0Rjg1dStGcWJkalkrS215RmVUUGQyNzE3UDZpNVY2QzZsVnBjbk03dm9abEd5MGZqb2FsZAplOW50bTBWVThGWmtVSWloS1B6VzkvTFNBVjhCZ08rdlNRck4vSU1FbURxb2w5NTlJeHhJLzZ5emtZNUp3WVJQCm1sd29OelUwZWtjSHpnMGV1N0RBMXV6UmZ2NEYxTlVXK1F5bFJkMENnWUVBenIwN09oZFAxanlDSXREOFUzbjYKRVdoNnM2ZzBzVlY1dGRwL1VzelhwTWdMeVFGblc5enRJdlJNVS9qbUlBemtybTlORllhSHc3REx2OWpLZDR5MAovNTlvK3JvK2tnK1RweVNLdU1qT0tjbkZpVUNPZko5RG9Rd1ZaU1lSNDVpREhpdlRueWExWlN5SnJtVllmM0N6CmR3OGVQU3VremJUUlRXWVptR2VuT3JrQ2dZRUFob082TWRZQXdlWHpIMEo4WHNEZVBFem1tY3ZhYXV6RGwzNUYKZ0lPQXhjMUIxMzgxTnFuUm9VZ1NpMWN6Wk82QlArcTY5TGJYM1BhVjlXTnF0RHArNU9YNFNUOEZnZ01PTUlkZwovbTVaM0Y0THRhakl2RDQxVjloUjJpMXlYNG1XUm1zTGgxYWNtbVF2dnpTVGVrTHZlejhqRDhaT2dWNjl5QmFWCmtkc1hhOTBDZ1lFQWsrNmdocFhOa3UxMlVBTmY5TUg4bG9OKzM1L2lQZWVvcWYwTVk1Rk1WUll4MTBaQTkxTGgKaWVBY3pWaGlxenhDdEhXaExBNFN4RTk2MmVnK2ppL2F3a1M0a1hMQ011WklFU0UrakZjN3B0VW1KamxzT1dqdgo4L2RxVUg1eWpSS3MycXhrQldHNEhtVDNOeDZBOHNZSXJVWXh5cVZMQnBHOHlLbmdibmFZUFY0PQotLS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQ==",
  "port": 22,
  "secret": "b42ec8b4-deb2-c75e-ebd0-132d63f8e8d4",
  "verbose": true
}
```

## Technical Details

### Actions

#### Execute Configuration Commands

This action is used to change the device's configuration (global configuration mode).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|command|[]string|None|True|Commands to change the configuration on network device|None|["ls -la"]|
|host|string|None|False|Optional hosts to run remote commands. If not provided, the connection host will be used|None|example.com|

Example input:

```
{
  "command": [
    "ls -la"
  ],
  "host": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|string|True|Output device CLI|

Example Output:

```

{
  "results": "sudo -s\nroot@buster:/home/vagrant# ls -la\ntotal 125088\ndrwxr-xr-x  9 vagrant vagrant      4096 Mar 31 19:24 .\ndrwxr-xr-x  3 root    root         4096 May 10  2020 ..\n-rw-------  1 vagrant vagrant     74883 Mar 31 19:24 .bash_history\n-rw-r--r--  1 vagrant vagrant       220 May 10  2020 .bash_logout\n-rw-r--r--  1 vagrant vagrant      3685 Sep 20  2020 .bashrc\ndrwxr-xr-x  6 vagrant vagrant      4096 Sep 20  2020 .cache\ndrwxr-xr-x  4 vagrant vagrant      4096 Sep 16  2020 .gem\n-rw-r--r--  1 vagrant vagrant        24 Sep 20  2020 .gitconfig\ndrwx------  3 vagrant vagrant      4096 Sep 16  2020 .gnupg\ndrwxr-xr-x 10 root    root         4096 May  6  2019 go\n-rw-r--r--  1 root    root    127938445 Sep 16  2020 go1.12.5.linux-amd64.tar.gz\ndrwxr-xr-x  4 vagrant vagrant      4096 Sep 20  2020 go_work\ndrwx------  4 vagrant vagrant      4096 Nov 25 00:51 .local\n-rw-r--r--  1 vagrant vagrant       807 May 10  2020 .profile\ndrwx------  2 vagrant vagrant      4096 Nov  2 16:16 .ssh\n-rw-------  1 vagrant vagrant     19449 Mar 23 20:33 .viminfo\nroot@buster:/home/vagrant# "
}

```

#### Execute Show Commands

This action is used to check the devices configurations (privilege exec mode).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|command|string|None|True|Show command to execute on network device|None|ls -la|
|host|string|None|False|Optional host to run remote commands. If not provided, the connection host will be used|None|example.com|

Example input:

```
{
  "command": "ls -la",
  "host": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|string|True|Output results|

Example output:

```

{
  "results": "total 125088\ndrwxr-xr-x  9 vagrant vagrant      4096 Mar 31 19:24 .\ndrwxr-xr-x  3 root    root         4096 May 10  2020 ..\n-rw-------  1 vagrant vagrant     74883 Mar 31 19:24 .bash_history\n-rw-r--r--  1 vagrant vagrant       220 May 10  2020 .bash_logout\n-rw-r--r--  1 vagrant vagrant      3685 Sep 20  2020 .bashrc\ndrwxr-xr-x  6 vagrant vagrant      4096 Sep 20  2020 .cache\ndrwxr-xr-x  4 vagrant vagrant      4096 Sep 16  2020 .gem\n-rw-r--r--  1 vagrant vagrant        24 Sep 20  2020 .gitconfig\ndrwx------  3 vagrant vagrant      4096 Sep 16  2020 .gnupg\ndrwxr-xr-x 10 root    root         4096 May  6  2019 go\n-rw-r--r--  1 root    root    127938445 Sep 16  2020 go1.12.5.linux-amd64.tar.gz\ndrwxr-xr-x  4 vagrant vagrant      4096 Sep 20  2020 go_work\ndrwx------  4 vagrant vagrant      4096 Nov 25 00:51 .local\n-rw-r--r--  1 vagrant vagrant       807 May 10  2020 .profile\ndrwx------  2 vagrant vagrant      4096 Nov  2 16:16 .ssh\n-rw-------  1 vagrant vagrant     19449 Mar 23 20:33 .viminfo"
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.0 - Update `netmiko` and `paramiko` version in requirements | Update to use the `insightconnect-python-3-38-slim-plugin:4` Docker image | Use input and output constants | Code refactor | Add example input and output | Change output title in Execute Configuration Commands and Execute Show Commands actions | Fix bug where error occurs when SSH Key is empty
* 1.0.2 - Fix bug where the SSH private key was not being retrieved correctly from the user in the connection
* 1.0.1 - Updated python libraries | New spec and help.md format for the Extension Library
* 1.0.0 - Support web server mode | Update to new credential types | Rename "Execute show commands" action to "Execute Show Commands" | Rename "Execute configuration change commands" action to "Execute Configuration Commands"
* 0.1.0 - Initial plugin

# Links

## References

* [Paramiko](http://www.paramiko.org/)
