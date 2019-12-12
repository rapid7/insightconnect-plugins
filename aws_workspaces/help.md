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

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|aws_access_key_id|credential_secret_key|None|True|The ID of the AWS access key to use for authentication|None|
|aws_secret_access_key|credential_secret_key|None|True|The AWS secret access Key used for signing requests with the given AWS access key ID|None|
|region|string|None|True|The AWS region to use for requests. An example would be us-east-1|['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ca-central-1', 'ap-south-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'sa-east-1']|

## Technical Details

### Actions

#### Create Workspace

This action is used to create a workspace.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|bundle_id|string|None|True|The identifier of the bundle for the workspace|None|
|directory_id|string|None|True|The identifier of the AWS Directory Service directory for the workspace|None|
|root_volume_encryption_enabled|boolean|None|False|Flag indicating whether the data stored on the root volume is encrypted|None|
|tags|[] tag|None|False|Tags|None|
|username|string|None|True|The username of the user for the workspace|None|
|user_volume_encryption_enabled|boolean|None|False|Flag indicating whether the data stored on the user volume is encrypted|None|
|volume_encryption_key|string|None|False|The KMS key used to encrypt data stored on your workspace|None|
|workspace_properties|workspace_properties|None|False|Workspace properties|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|workspace_id_state|workspace_id_state|True|ID and state of a created workspace|

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

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Initial plugin

# Links

## References

* [AWS WorkSpaces](https://aws.amazon.com/workspaces/)

