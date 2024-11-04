# Description

This plugin utilizes [AWS WorkSpaces](https://aws.amazon.com/workspaces/) to create workspaces. Amazon WorkSpaces is a fully managed
 desktop computing service in the cloud that allows its customers to provide cloud-based desktops to their end-users. Can be utilized for bring your own device policies and product testing.

# Key Features

* Create workspace

# Requirements

* AWS account
* AWS access key ID for authentication
* AWS secret key for signing requests with the given AWS access key ID
* AWS region to use for requests

# Supported Product Versions

* 2024-11-4

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|aws_access_key_id|credential_secret_key|None|True|The ID of the AWS access key to use for authentication|None|AKIAEXAMPLEACCESSKEY|None|None|
|aws_secret_access_key|credential_secret_key|None|True|The AWS secret access key used for signing requests with the given AWS access key ID|None|wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY|None|None|
|region|string|None|True|The AWS region to use for requests. An example would be us-east-1|None|us-west-2|None|None|

Example input:

```
{
  "aws_access_key_id": "AKIAEXAMPLEACCESSKEY",
  "aws_secret_access_key": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
  "region": "us-west-2"
}
```

## Technical Details

### Actions


#### Create Workspace

This action is used to create a workspace

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|bundle_id|string|None|True|The identifier of the bundle for the workspace|None|wsb-0zsvgp8fc|None|None|
|directory_id|string|None|True|The identifier of the AWS Directory Service directory for the workspace|None|d-926722edaf|None|None|
|root_volume_encryption_enabled|boolean|None|False|Flag indicating whether the data stored on the root volume is encrypted|None|True|None|None|
|tags|[]string|None|False|Tags|None|[{"Key": "Environment", "Value": "Production"}]|None|None|
|user_volume_encryption_enabled|boolean|None|False|Flag indicating whether the data stored on the user volume is encrypted|None|True|None|None|
|username|string|None|True|The username of the user for the workspace|None|Mateo|None|None|
|volume_encryption_key|string|None|False|The KMS key used to encrypt data stored on your workspace|None|arn:aws:kms:us-west-2:123456789012:key/abcd1234-5678-90ef-gh12-ijkl3456mnop|None|None|
|workspace_properties|workspace_properties|None|False|Workspace properties|None|{ "running_mode": "AUTO_STOP", "running_mode_auto_stop_time_out": 60, "root_volume_size": 80, "user_volume_size": 50, "compute_type_name": "VALUE" }|None|None|
  
Example input:

```
{
  "bundle_id": "wsb-0zsvgp8fc",
  "directory_id": "d-926722edaf",
  "root_volume_encryption_enabled": true,
  "tags": [
    {
      "Key": "Environment",
      "Value": "Production"
    }
  ],
  "user_volume_encryption_enabled": true,
  "username": "Mateo",
  "volume_encryption_key": "arn:aws:kms:us-west-2:123456789012:key/abcd1234-5678-90ef-gh12-ijkl3456mnop",
  "workspace_properties": {
    "compute_type_name": "VALUE",
    "root_volume_size": 80,
    "running_mode": "AUTO_STOP",
    "running_mode_auto_stop_time_out": 60,
    "user_volume_size": 50
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|workspace_id_state|workspace_id_state|True|ID and state of a created workspace|None|
  
Example output:

```
{
  "workspace_id_state": {
    "id": "ws-9s7685j2s",
    "state": "PENDING"
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**workspace_properties**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Compute Type Name|string|None|False|Compute type name|None|
|Root Volume Size|integer|80|False|Root volume size in gigabytes|None|
|Running Mode|string|None|False|Running mode|None|
|Running Mode Auto Stop Time Out|integer|60|False|Running mode auto stop time out in minutes. It should be a multiple of 60|None|
|User Volume Size|integer|10|False|User volume size in gigabytes|None|
  
**tag**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Key|string|None|False|The key in a key-value pair of a tag|None|
|Value|string|None|False|The value in a key-value pair of a tag|None|
  
**workspace_id_state**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|True|ID of a created workspace|None|
|State|string|None|True|Current status of a created workspace|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 2.0.0 - Bumping requirements.txt | SDK bump to 6.1.4
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

* [AWS WorkSpaces](https://aws.amazon.com/workspaces/)

## References

* [AWS WorkSpaces API Docs](https://docs.aws.amazon.com/workspaces/latest/api/welcome.html)