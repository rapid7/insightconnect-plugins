# Description

[OSSEC](https://ossec.github.io/) is a free, open-source host-based intrusion detection system with file integrity 
monitoring and log analysis capabilities. This plugin parses the standard multi-line OSSEC alerts 
found in `/var/ossec/logs/alerts/alerts.log` into usable JSON.

# Key Features

* Parse OSSEC alerts
* Convert alerts to JSON

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Alert Parse

This action is used to parse standard OSSEC alerts. If the OSSEC log does contain the `User:` or `Src IP:` lines we set the values of missing fields to `Unknown`.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|alert|string|None|True|OSSEC Alert alert|None|

Example input:

```

** Alert 1471014810.6994: - syslog,sshd,invalid_login,
2016 Aug 12 15:13:30 (bastion) any->/var/log/secure
Rule: 5718 (level 5) -> 'Attempt to login using a denied user.'
Src IP: 116.31.116.16
User: root
Aug 12 15:13:29 bastion sshd[17047]: User root from 116.31.116.16 not allowed because none of user's groups are listed in AllowGroups

```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alert|alert_alert|False|None|

Example output:

```

{
  "alert": {
    "timestamp": "2016 Aug 12 15:13:30",
    "user": "root",
    "alert_id": 1471014810.6994,
    "logs": [
      "Aug 12 15:13:29 bastion sshd[17047]: User root from 116.31.116.16 not allowed because none of user's groups are listed in AllowGroups"
    ],
    "level": 5,
    "rule_id": 5718,
    "agent": "bastion",
    "category": "syslog,sshd,invalid_login,",
    "rule_name": "Attempt to login using a denied user.",
    "source_ip": "116.31.116.16"
  }
}

```

#### Rootcheck Parse

This action is used to parse OSSEC Rootcheck alerts.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|alert|string|None|True|OSSEC Rootcheck alert|None|

Example input:

```

** Alert 1471016950.7633: - rootcheck,
2016 Aug 12 15:49:10 (komand.dev.komand.local) any->rootcheck
Rule: 510 (level 7) -> 'Host-based anomaly detection event (rootcheck).'
File '/var/lib/docker/containers/d1cc36313c308122fb4170a6e6637176ed13763c98f7ef1473470ddc800c054b/hostconfig.json' is owned by root and has written permissions to anyone.

```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alert|rootcheck_alert|False|None|

Example output:

```

{
  "alert": {
    "rule_id": 510,
    "log": "File '/var/lib/docker/containers/d1cc36313c308122fb4170a6e6637176ed13763c98f7ef1473470ddc800c054b/hostconfig.json' is owned by root and has written permissions to anyone.",
    "agent": "komand.dev.komand.local",
    "logs": [
      "File '/var/lib/docker/containers/d1cc36313c308122fb4170a6e6637176ed13763c98f7ef1473470ddc800c054b/hostconfig.json' is owned by root and has written permissions to anyone."
    ],
    "rule_name": "Host-based anomaly detection event (rootcheck).",
    "level": 7,
    "file": "/var/lib/docker/containers/d1cc36313c308122fb4170a6e6637176ed13763c98f7ef1473470ddc800c054b/hostconfig.json",
    "alert_id": 1471016950.7633,
    "category": "rootcheck,",
    "timestamp": "2016 Aug 12 15:49:10"
  }
}

```

#### Syscheck Parse

This action is used to parse OSSEC Syscheck alerts. If the OSSEC log does contain the MD5, SHA, or Permissions lines we set the values for missing fields to `Unknown`.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|alert|string|None|True|OSSEC Syscheck alert|None|

Example input:

```

** Alert 1475146364.5660: - syscheck,
2016 Sep 29 10:52:44 (komand.dev.komand.local2) any->syscheck
Rule: 550 (level 7) -> 'Integrity checksum changed.'
Integrity checksum changed for: '/bin/openssl'
Size changed from '508664' to '508656'
Old md5sum was: '2ec933a677c9cf1d3ca46c6830c6890f'
New md5sum is : 'b4d006f0b53ccf7be855346cc5cdd2b9'
Old sha1sum was: 'f5c2ff9963fb2a6e8eb2a02259e8c05960dfe9f8'
New sha1sum is : 'a3b348a86b54b0185a5d3c0df8c785f5b72dfc04'

```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alert|syscheck_alert|False|None|

Example output:

```

{
  "alert": {
    "md5_new": "b4d006f0b53ccf7be855346cc5cdd2b9",
    "sha_old": "f5c2ff9963fb2a6e8eb2a02259e8c05960dfe9f8",
    "size_old": 508664,
    "md5_old": "2ec933a677c9cf1d3ca46c6830c6890f",
    "category": "syscheck,",
    "sha_new": "a3b348a86b54b0185a5d3c0df8c785f5b72dfc04",
    "agent": "komand.dev.komand.local2",
    "rule_id": 550,
    "rule_name": "Integrity checksum changed.",
    "alert_id": 1475146364.566,
    "timestamp": "2016 Sep 29 10:52:44",
    "size_new": 508656,
    "level": 7,
    "file": "/bin/openssl"
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

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [OSSEC](https://ossec.github.io/)
