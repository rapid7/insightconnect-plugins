# Description

[Secure Shell](https://en.wikipedia.org/wiki/Secure_Shell) (SSH) is a cryptographic network protocol for operating network services securely over an unsecured network.
This plugin uses the [paramiko](http://www.paramiko.org/) to connect to a remote host via the library. The SSH plugin allows you to run commands on a remote host.

# Key Features

* Run remote commands with SSH

# Requirements

* Credentials for the target remote host
* Address and port for the target remote host

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|host|string|None|True|Remote host to connect to. Can be over-ridden in actions|None|198.51.100.100|
|key|credential_asymmetric_key|None|False|A base64 encoded SSH private key to use to authenticate to remote server. A newline is required after the beginning and before the end marker|None|{"privateKey": "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFcFFJQkFBS0NBUUVBakdub1V0ZlBIcXZYM1BJVTZOOUZLbXdRM1psK05vYVdiNHlNTGh1ZGtkRUJKM0F1CitJOFFkbHFES0JtNjU2VWVPQ2gzci9pOWUwVUxLeGtYREZmS21jM3AyV3YrMGxWT1lHdnhaRktVd0tIMHJpQUwKQTRpbXlZdUwvZndlT1NHU25RbGdZS3I5OUhjaVRCSWRMMTVTWjMyVGpZYitQRFpCbCs2elFzdzJIWU5KY3FNagppY2lDN0NBajZnQjlTTzh4MXZNc1JrVStycUt1YzJyOFVrK3FoRUN3OHpSNEs2NndGdVlNMTdzR1VNWFVxL3BICldkaUV2TzNxL21kSzQ3TnJ4NWkyYmFDN281UlhzcEtIWXk2WGVyNFZibmlwbDREZ0FLa2FOT0wwMmErWnYzOFEKbCt4eTl3ZG1XcVVJYk1pcVNiai9rNnh4RGlQUWtUUisvMDMyZVFJREFRQUJBb0lCQUVrUHpwQlV0UFFickozTgo1UzFyQjcxVUw4NXUwT3FrUzJETnZCODl4VmFiYjBOTEwxV3NjMzl5QjI3MVBIak9SUlFwa21XaFEwOENGUmFlCjNveFFuaDQ3cytPck94UE15WlNJZGptaWNyNXRSempYZVlPa05rMEc3SmdDK09MM1lpZU9PblR5WkdReEhVcUIKM21mSVo0NXNIRHYzTXhDM2xwZnMzNS94VEhNOEUvZ1cvZ1RmdlUzUWJvUWFMMXEvdGFSUVlFSHZnaXV0d2RaMApzRUZ0SjhlQXdPQkFCWGlWM1FQeG5BUWdJcHdZcGJpY2wzQUsxNWdzNUVOSzRSbmdpMmJJN2hkbU13RFdhNnQvCmcwQ1AwVGl0eUZxMDVKVW1uYXo0d2VrWHhENUVCbTc3NkVZTlNveFRDYVN6VE1Zd1pDSVRycVhsNlk0L29nZVQKdVZTbTlaRUNnWUVBN0c4Q3l5REtEVEJZb0l5RWtuSlZLU3d1ZWxPQTJlZHhtVnlLTDhoTG9QaXExUW9TSC9OMQozMG5OL0dWY3ZEN1FFRDRwL3UwWGFNdVBtMkhWaHVYd3h1L3Q5ajExRFZsS1A3UXNIOXU0cEpLeml3Nk5tVjVOCi85K21jamRXQUg1QnFhSnRtcEYwdW9ac1drNDFKVmUwZkE3YTNGQ3JYcDFVL0dEOUJLU0FEMDBDZ1lFQW1BaW8KQ2hFaDcrcEQ3dnV0Rjg1dStGcWJkalkrS215RmVUUGQyNzE3UDZpNVY2QzZsVnBjbk03dm9abEd5MGZqb2FsZAplOW50bTBWVThGWmtVSWloS1B6VzkvTFNBVjhCZ08rdlNRck4vSU1FbURxb2w5NTlJeHhJLzZ5emtZNUp3WVJQCm1sd29OelUwZWtjSHpnMGV1N0RBMXV6UmZ2NEYxTlVXK1F5bFJkMENnWUVBenIwN09oZFAxanlDSXREOFUzbjYKRVdoNnM2ZzBzVlY1dGRwL1VzelhwTWdMeVFGblc5enRJdlJNVS9qbUlBemtybTlORllhSHc3REx2OWpLZDR5MAovNTlvK3JvK2tnK1RweVNLdU1qT0tjbkZpVUNPZko5RG9Rd1ZaU1lSNDVpREhpdlRueWExWlN5SnJtVllmM0N6CmR3OGVQU3VremJUUlRXWVptR2VuT3JrQ2dZRUFob082TWRZQXdlWHpIMEo4WHNEZVBFem1tY3ZhYXV6RGwzNUYKZ0lPQXhjMUIxMzgxTnFuUm9VZ1NpMWN6Wk82QlArcTY5TGJYM1BhVjlXTnF0RHArNU9YNFNUOEZnZ01PTUlkZwovbTVaM0Y0THRhakl2RDQxVjloUjJpMXlYNG1XUm1zTGgxYWNtbVF2dnpTVGVrTHZlejhqRDhaT2dWNjl5QmFWCmtkc1hhOTBDZ1lFQWsrNmdocFhOa3UxMlVBTmY5TUg4bG9OKzM1L2lQZWVvcWYwTVk1Rk1WUll4MTBaQTkxTGgKaWVBY3pWaGlxenhDdEhXaExBNFN4RTk2MmVnK2ppL2F3a1M0a1hMQ011WklFU0UrakZjN3B0VW1KamxzT1dqdgo4L2RxVUg1eWpSS3MycXhrQldHNEhtVDNOeDZBOHNZSXJVWXh5cVZMQnBHOHlLbmdibmFZUFY0PQotLS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQ=="}|
|password|credential_secret_key|None|False|Password authentication or password to decrypt provided private key. Either this or SSH private key is required|None|{"secretKey": "mypassword"}|
|port|integer|22|True|Remote port to use|None|22|
|use_key|boolean|None|True|True to connect via key, false to connect via password|None|True|
|username|string|None|True|User to run command as|None|user1|

Example input:

```
{
  "host": "198.51.100.100",
  "key": {"privateKey": "LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFcFFJQkFBS0NBUUVBakdub1V0ZlBIcXZYM1BJVTZOOUZLbXdRM1psK05vYVdiNHlNTGh1ZGtkRUJKM0F1CitJOFFkbHFES0JtNjU2VWVPQ2gzci9pOWUwVUxLeGtYREZmS21jM3AyV3YrMGxWT1lHdnhaRktVd0tIMHJpQUwKQTRpbXlZdUwvZndlT1NHU25RbGdZS3I5OUhjaVRCSWRMMTVTWjMyVGpZYitQRFpCbCs2elFzdzJIWU5KY3FNagppY2lDN0NBajZnQjlTTzh4MXZNc1JrVStycUt1YzJyOFVrK3FoRUN3OHpSNEs2NndGdVlNMTdzR1VNWFVxL3BICldkaUV2TzNxL21kSzQ3TnJ4NWkyYmFDN281UlhzcEtIWXk2WGVyNFZibmlwbDREZ0FLa2FOT0wwMmErWnYzOFEKbCt4eTl3ZG1XcVVJYk1pcVNiai9rNnh4RGlQUWtUUisvMDMyZVFJREFRQUJBb0lCQUVrUHpwQlV0UFFickozTgo1UzFyQjcxVUw4NXUwT3FrUzJETnZCODl4VmFiYjBOTEwxV3NjMzl5QjI3MVBIak9SUlFwa21XaFEwOENGUmFlCjNveFFuaDQ3cytPck94UE15WlNJZGptaWNyNXRSempYZVlPa05rMEc3SmdDK09MM1lpZU9PblR5WkdReEhVcUIKM21mSVo0NXNIRHYzTXhDM2xwZnMzNS94VEhNOEUvZ1cvZ1RmdlUzUWJvUWFMMXEvdGFSUVlFSHZnaXV0d2RaMApzRUZ0SjhlQXdPQkFCWGlWM1FQeG5BUWdJcHdZcGJpY2wzQUsxNWdzNUVOSzRSbmdpMmJJN2hkbU13RFdhNnQvCmcwQ1AwVGl0eUZxMDVKVW1uYXo0d2VrWHhENUVCbTc3NkVZTlNveFRDYVN6VE1Zd1pDSVRycVhsNlk0L29nZVQKdVZTbTlaRUNnWUVBN0c4Q3l5REtEVEJZb0l5RWtuSlZLU3d1ZWxPQTJlZHhtVnlLTDhoTG9QaXExUW9TSC9OMQozMG5OL0dWY3ZEN1FFRDRwL3UwWGFNdVBtMkhWaHVYd3h1L3Q5ajExRFZsS1A3UXNIOXU0cEpLeml3Nk5tVjVOCi85K21jamRXQUg1QnFhSnRtcEYwdW9ac1drNDFKVmUwZkE3YTNGQ3JYcDFVL0dEOUJLU0FEMDBDZ1lFQW1BaW8KQ2hFaDcrcEQ3dnV0Rjg1dStGcWJkalkrS215RmVUUGQyNzE3UDZpNVY2QzZsVnBjbk03dm9abEd5MGZqb2FsZAplOW50bTBWVThGWmtVSWloS1B6VzkvTFNBVjhCZ08rdlNRck4vSU1FbURxb2w5NTlJeHhJLzZ5emtZNUp3WVJQCm1sd29OelUwZWtjSHpnMGV1N0RBMXV6UmZ2NEYxTlVXK1F5bFJkMENnWUVBenIwN09oZFAxanlDSXREOFUzbjYKRVdoNnM2ZzBzVlY1dGRwL1VzelhwTWdMeVFGblc5enRJdlJNVS9qbUlBemtybTlORllhSHc3REx2OWpLZDR5MAovNTlvK3JvK2tnK1RweVNLdU1qT0tjbkZpVUNPZko5RG9Rd1ZaU1lSNDVpREhpdlRueWExWlN5SnJtVllmM0N6CmR3OGVQU3VremJUUlRXWVptR2VuT3JrQ2dZRUFob082TWRZQXdlWHpIMEo4WHNEZVBFem1tY3ZhYXV6RGwzNUYKZ0lPQXhjMUIxMzgxTnFuUm9VZ1NpMWN6Wk82QlArcTY5TGJYM1BhVjlXTnF0RHArNU9YNFNUOEZnZ01PTUlkZwovbTVaM0Y0THRhakl2RDQxVjloUjJpMXlYNG1XUm1zTGgxYWNtbVF2dnpTVGVrTHZlejhqRDhaT2dWNjl5QmFWCmtkc1hhOTBDZ1lFQWsrNmdocFhOa3UxMlVBTmY5TUg4bG9OKzM1L2lQZWVvcWYwTVk1Rk1WUll4MTBaQTkxTGgKaWVBY3pWaGlxenhDdEhXaExBNFN4RTk2MmVnK2ppL2F3a1M0a1hMQ011WklFU0UrakZjN3B0VW1KamxzT1dqdgo4L2RxVUg1eWpSS3MycXhrQldHNEhtVDNOeDZBOHNZSXJVWXh5cVZMQnBHOHlLbmdibmFZUFY0PQotLS0tLUVORCBSU0EgUFJJVkFURSBLRVktLS0tLQ=="},
  "password": {"secretKey": "mypassword"},
  "port": 22,
  "use_key": true,
  "username": "user1"
}
```

The `key` field takes a base64 encoded RSA private key which must contain a newline character after the BEGIN marker and before the END marker:
E.g.

```
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7g4h53s=
...
-----END RSA PRIVATE KEY-----
```

You can easily encode a private key file and copy a key to your clipboard on MacOS with the following command: `base64 < .ssh/id_rsa | pbcopy`.
This can then be pasted into the Connection's `key` input field.

## Technical Details

### Actions

#### Run Remote Command

This action is used to run remote command.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|command|string|None|True|Command to execute on remote host|None|pwd|
|host|string|None|False|Host to run remote commands. If not provided, the connection host will be used|None|198.51.100.100|

Example input:

```
{
  "command": "pwd",
  "host": "198.51.100.100"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|results|True|Results|

Example output:

```
{
  "results": {
    "all_output": "/home/vagrant\n",
    "stderr": "",
    "stdout": "/home/vagrant\n"
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 3.0.1 - Fixed issue obtaining username in connection
* 3.0.0 - Update connection username from credential_secret_key to string
* 2.0.0 - Update Run action output to return 3 output fields i.e. `stderr`, `stdout`, and `all_output`
* 1.0.3 - New spec and help.md format for the Extension Library
* 1.0.2 - Fixed issue where Run was excluded
* 1.0.1 - Fix issue where run action was excluded from plugin on build
* 1.0.0 - Support web server mode | Update to new credential types | Rename "Run remote command" action to "Run Remote Command"
* 0.1.3 - SSL bug fix in SDK
* 0.1.2 - Strip extra newlines in key
* 0.1.1 - Connection SSH key input is now type bytes
* 0.1.0 - Initial plugin

# Links

## References

* [Secure Shell](https://en.wikipedia.org/wiki/Secure_Shell)
* [OpenSSH](https://www.openssh.com/)
* [paramiko](http://www.paramiko.org/)

## Custom Output Types

### results

|Name|Type|Required|Description|
|----|----|--------|-----------|
|stderr|string|True|Stderr|
|stdout|string|True|Stdout|
|all_output|string|True|All output|
