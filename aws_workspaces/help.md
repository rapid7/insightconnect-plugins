# AWS WorkSpaces

## About

[AWS WorkSpaces](https://aws.amazon.com/workspaces/) is a fully managed desktop computing service in the cloud that allows its customers to provide cloud-based desktops to their end-users.

## Actions

### Create Workspace

This action is used to create a workspace.

#### Input

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

#### Output

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

## Triggers

_This plugin does not contain any triggers._

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|aws_access_key_id|credential_secret_key|None|True|The ID of the AWS access key to use for authentication|None|
|aws_secret_access_key|credential_secret_key|None|True|The AWS secret access Key used for signing requests with the given AWS access key ID|None|
|region|string|None|True|The AWS region to use for requests. An example would be us-east-1|['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ca-central-1', 'ap-south-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'sa-east-1']|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

## Workflows

Examples:

* Create a workspace 

## Versions

* 1.0.0 - Initial plugin

## References

* [AWS WorkSpaces](https://aws.amazon.com/workspaces/)

## Custom Output Types

### workspace_properties

|Name|Type|Required|Description|
|----|----|--------|-----------|
|compute_type_name|string|False|Compute type name|
|root_volume_size|integer|False|Root volume size in gigabytes|
|running_mode|string|False|Running mode|
|running_mode_auto_stop_time_out|integer|False|Running mode auto stop time out in minutes. It should be a multiple of 60|
|user_volume_size|integer|False|User volume size in gigabytes|

### tag

|Name|Type|Required|Description|
|----|----|--------|-----------|
|key|string|False|The key in a key-value pair of a tag|
|value|string|False|The value in a key-value pair of a tag|

### workspace_id_state

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|True|ID of a created workspace|
|state|string|True|Current status of a created workspace|


