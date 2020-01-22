# Description

[Firepower](https://www.cisco.com/c/en_uk/products/security/firewalls/index.html) is a Next-Generation Firewall (NGFW) with NGIPS, incorporating access and application control, threat prevention and firewall capabilities.
The Cisco Firepower InsightConnect plugin allows you to add scan results from a third-party vulnerability scanner.

This plugin utilizes the [Host Input API](https://www.cisco.com/c/en/us/td/docs/security/firepower/60/api/host-input/HostInputAPIGuide.html).

# Key Features

* Add scan results from a third-party vulnerability scanner

# Requirements

* Cisco Firepower server name and port number
* Base64-encoded certificate to authenticate with the host input API
* The passphrase to access the certificate

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|certificate_passphrase|credential_secret_key|None|False|The passphrase to access the certificate|None|
|port|integer|8307|False|Enter the port to connect to the Host Input API (Default:8307)|None|
|certificate|bytes|None|False|Base64 encoded certificate to authenticate with the host input API|None|
|server|string|None|False|Enter the address for the server|None|

## Technical Details

### Actions

#### Bulk Add Scan Result

This action is used to add scan results from a third-party vulnerability scanner.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|operation|string|None|True|The operation to be performed when adding scan results. ScanFlush to remove existing scan results or ScanUpdate to keep existing scan results|['ScanUpdate', 'ScanFlush']|
|scan_results|[]scan_result|None|False|Scan results to add|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|commands_processed|number|False|None|
|errors|number|False|None|

Example output:

```

{
  "errors": 0,
  "commands_processed": 10512
}

```

#### Add Scan Result

This action is used to add a scan result from a third-party vulnerability scanner.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|scan_result|scan_result|None|False|Scan result for the host|None|
|operation|string|None|True|The operation to be performed when adding scan results. ScanFlush to remove existing scan results or ScanUpdate to keep existing scan results|['ScanUpdate', 'ScanFlush']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|commands_processed|number|False|None|
|errors|number|False|None|

Example output:

```

{
  "commands_processed": 4,
  "errors": 0
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - Update descriptions
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.0 - Initial plugin

# Links

## References

* [Firepower](https://www.cisco.com/c/en_uk/products/security/firewalls/index.html)
* [Host Input API](https://www.cisco.com/c/en/us/td/docs/security/firepower/60/api/host-input/HostInputAPIGuide.html)

