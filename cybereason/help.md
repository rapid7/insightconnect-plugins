# Description

The Cybereason platform provides military-grade cyber security with real-time awareness and detection.

# Key Features

Identify key features of plugin.

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|False|Username and password|None|{"username": "user@example.com", "password": "mypassword"}|
|hostname|string|None|True|Enter the hostname|None|None|
|port|integer|8443|True|Enter the port|None|None|

Example input:

```
{
  "credentials": "{\"username\": \"user@example.com\", \"password\": \"mypassword\"}"
}
```

## Technical Details

### Actions

#### Isolate Machine

This action is used to isolate a machine associated with the root cause of a Malop, or to remediate a process not involved in a malop.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|actions_by_machine|object|None|False|Actions by machine|None|None|
|initiator_user_name|string|None|False|Initiator user name|None|None|
|malop_id|string|None|False|Malop ID to isolate a machine or empty to remediate process not involved in a malop|None|None|
|pylum_ids|[]string|None|False|The unique sensor ID the Cybereason platform uses for the machines to isolate|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|object|False|Malop response|

Example output:

```

```

#### Search for Files

This action is used to find files on any machine in your environment with a Cybereason sensor installed..

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file_filter|string|None|True|A fileFilters object where you filter by machine name, folder, file creation or modification time or file size with operator Equals, NotEquals, ContainsIgnoreCase, NotContainsIgnoreCase and others|None|fileName Equals: ["sample.py"]|
|server_filter|string|None|False|A Sensor filters object where you filter sensors by different criteria such as operating system|None|machineName: ["rapid7-windows"]|

Example input:

```
{
  "file_filter": "fileName Equals: [\"sample.py\"]",
  "server_filter": "machineName: [\"rapid7-windows\"]"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|True||

Example output:

```
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Cybereason Plugin](LINK TO PRODUCT/VENDOR WEBSITE)
