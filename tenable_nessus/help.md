# Description

The Tenable Nessus plugin allows you to get, start, and analyze scans.

Tenable [Nessus Professional](https://www.tenable.com/products/nessus-vulnerability-scanner/nessus-professional) prevents network attacks by identifying the vulnerabilities and configuration issues that hackers use to penetrate your network.

# Key Features

* Get a scan
* Start a scan
* Get a scan report

# Requirements

* Tenable Nessus access key
* Tenable Nessus secret key
* The address of your Tenable Nessus instance

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|access_key|credential_secret_key|None|True|None|None|
|ssl_verify|boolean|True|True|Validate certificate|None|
|secret_key|credential_secret_key|None|True|None|None|
|hostname|string|None|True|Nessus instance hostname e.g. 192.168.1.10:1234|None|

## Technical Details

### Actions

#### List Scanners

This action is used to return an array of all available scanners.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scanners|[]object|True|None|

Example Output:

```

{
  "scanners": [
      {
          "num_scans": null,
          "aws_availability_zone": null,
          "aws_update_interval": null,
          "needs_restart": null,
          "last_connect": null,
          "loadavg": null,
          "num_tcp_sessions": null,
          "num_hosts": null,
          "num_sessions": null,
          "expiration_time": 3,
          "expiration": 1503067915,
          "loaded_plugin_set": "201708101515",
          "platform": "DARWIN",
          "ui_build": "100",
          "ui_version": "6.11.0",
          "engine_build": "M20100",
          "engine_version": "6.11.0",
          "status": "on",
          "scan_count": 0,
          "linked": 1,
          "type": "local",
          "name": "Local Scanner",
          "uuid": "00000000-0000-0000-0000-00000000000000000000000000000",
          "token": null,
          "owner_name": "system",
          "owner": "nessus_ms_agent",
          "shared": 1,
          "user_permissions": 64,
          "timestamp": 1502462788,
          "last_modification_date": 1502462788,
          "creation_date": 1502462788,
          "owner_id": 1,
          "id": 1
      }
  ]
}

```

#### Launch Scan

This action is used to run a specified scan.

Attempting to launch a scan with the same name as one that is already running will cause errors.

This API endpoint was deprecated in Nessus 7.0.0

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|scan_name|string|None|True|Name of the specified scan|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Return message|

Example Output:

```

{
  "message": "Scan launched successfully"
}

```

#### Get Scans

This action is used to returns a list of scans running on the requested scanner..

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|scanner_name|string|None|False|Name of the requested scanner. Retrieve all scans if none specified|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scans|[]object|True|None|

Example Output:

```

    "scans": [
      {
          "folder_id": 3,
          "type": "local",
          "read": false,
          "last_modification_date": 1502725394,
          "creation_date": 1502725247,
          "status": "completed",
          "uuid": "8be6e77a-0658-a379-c881-f667b8b47eae0a2b457f749b4b6b",
          "shared": false,
          "user_permissions": 128,
          "owner": "name",
          "timezone": null,
          "rrules": null,
          "starttime": null,
          "enabled": false,
          "control": true,
          "name": "scan",
          "id": 19
      },
      {
          "folder_id": 3,
          "type": "local",
          "read": false,
          "last_modification_date": 1502481114,
          "creation_date": 1502480989,
          "status": "completed",
          "uuid": "916affb1-88f0-f79f-affa-f14848827d850352d3ab3f5fb98e",
          "shared": false,
          "user_permissions": 128,
          "owner": "name",
          "timezone": null,
          "rrules": null,
          "starttime": null,
          "enabled": true,
          "control": true,
          "name": "new scan",
          "id": 16
      }
  ]

```

#### Download Report

This action is used to export and download a specified report.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|scan_name|string|None|True|Name of the specified scan|None|
|report_format|string|None|True|File format of the downloaded report|['nessus', 'csv', 'html']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|report|string|True|Text of the returned file|

Example Output:

```

{
  "report": [data]
}

```

#### Create Scan

This action is used to create a new scan.

This API endpoint was deprecated in Nessus 7.0.0

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|template_name|string|None|True|Name of the template to use|None|
|scan_name|string|None|True|Name to label the new scan|None|
|scanner_name|string|None|True|Name of the scanner to use|None|
|description|string|None|False|Additional information to attach to the scan|None|
|targets|[]string|None|True|IP addresses or host names to scan|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|message|string|True|Return message|
|new_scan|object|True|Data describing the newly created scan|

Example Output:

```

{
    "message": "Scan successfully created",
    "new_scan": {
      "container_id": 0,
      "uuid": "template-50579e09-41c3-dd67-720e-f9a4a16bfc9cf7df3650f5c75511",
      "name": "my scan",
      "description": "a scan created just now",
      "policy_id": 53,
      "scanner_id": 1,
      "emails": null,
      "sms": null,
      "enabled": true,
      "use_dashboard": false,
      "dashboard_file": null,
      "scan_time_window": null,
      "custom_targets": "https://www.my-domain.com, https://my-other-domain.com",
      "starttime": null,
      "rrules": null,
      "timezone": null,
      "notification_filters": null,
      "shared": 0,
      "user_permissions": 128,
      "default_permisssions": 0,
      "owner": "name",
      "owner_id": 2,
      "last_modification_date": 1502736552,
      "creation_date": 1502736552,
      "type": "public",
      "id": 54
  }
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.
*Note:* Tenable Nessus deprecated create and launch scan in version 7.0.0

# Version History

* 2.0.1 - New spec and help.md format for the Hub
* 2.0.0 - Use new credential types
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Nessus Professional Product Page](https://www.tenable.com/products/nessus-vulnerability-scanner/nessus-professional)
* Nessus API documentation is only available through your Nessus instance. Assuming default configuration, it can be found at `https://localhost:8834/api`.

