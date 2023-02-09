# Description

Orca's agentless, cloud-native security and compliance platform detects, monitors, and prioritizes the most critical cloud security risks for AWS, Azure, and Google Cloud estates

# Key Features

* Get assets
* Get alerts
* Update alert status and severity
* Initiate alert verification
* Get, add and delete users 

# Requirements

* Orca Security API Token generated using [this instruction](https://docs.orcasecurity.io/docs/create-a-token-for-api-usage)
* Administrator privileges to use Get Users, Add User and Delete User actions

# Supported Product Versions

* Orca Security API 2022-08-15

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_token|credential_secret_key|None|True|Orca Security API Token|None|9de5069c5afe602b2ea0a04b66beb2c0|
|region|string|US|True|The region for Orca Security|['US', 'EU', 'AU']|US|

Example input:

```
{
  "api_token": "44d88612fea8a8f36de82e1278abb02f",
  "region": "US"
}
```

## Technical Details

### Actions

#### Delete User

This action is used to delete an invitation to the organization for the specified user. Administrator privileges are required to perform this action.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|delete_invite_email|string|None|True|Email address of the user for whom the invitation will be deleted|None|user@example.com|

Example input:

```
{
  "delete_invite_email": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|True|Status of the action performed|

Example output:

```
{
  "status": "success"
}
```

#### Add User

This action is used to create an invitation to the organization for the specified user. Administrator privileges are required to perform this action.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|all_cloud_accounts|boolean|None|True|Whether the user will have access to all cloud accounts|None|False|
|cloud_accounts|[]string|None|False|A list of cloud accounts to which the user will have access|None|["test-account"]|
|invite_user_email|string|None|True|Email address of the user for whom the invitation will be created|None|user@example.com|
|role|string|None|True|Role name or ID|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|
|should_send_email|boolean|None|True|Whether the email should be sent|None|True|

Example input:

```
{
  "all_cloud_accounts": false,
  "cloud_accounts": [
    "test-account"
  ],
  "invite_user_email": "user@example.com",
  "role": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
  "should_send_email": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|True|Status of the action performed|

Example output:

```
{
  "status": "success"
}
```

#### Get Assets

This action is used to get assets that match the specified filter criteria. If no inputs are given, all assets will be returned.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|asset_labels|string|None|False|The label of the asset|None|internet_facing|
|asset_state|string|None|False|The state of the asset|None|running|
|asset_type|string|None|False|The type of the asset|None|container|
|asset_unique_id|string|None|False|Unique ID of the asset for which information will be obtained|None|example-asset-123|
|cloud_provider_id|string|None|False|ID of the cloud provider for which the assets will be returned|None|123456789|
|compute_regions|string|None|False|The region for which the assets will be returned|None|us-east-1|
|compute_vpcs|string|None|False|The virtual private cloud|None|vpc-1234567890|
|internet_facing|string|None|False|Whether asset is accessible from the internet|None|True|
|state_score|string|None|False|The score of the asset|None|4|
|state_severity|string|None|False|The severity of the asset|None|informational|

Example input:

```
{
  "asset_labels": "internet_facing",
  "asset_state": "running",
  "asset_type": "container",
  "asset_unique_id": "example-asset-123",
  "cloud_provider_id": 123456789,
  "compute_regions": "us-east-1",
  "compute_vpcs": "vpc-1234567890",
  "internet_facing": true,
  "state_score": 4,
  "state_severity": "informational"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|assets|[]asset|False|Results containing information about assets|
|total_items|integer|True|Total number of assets|
|total_supported_items|integer|False|Total number of supported assets|
|total_ungrouped_items|integer|False|Total number of ungrouped assets|

Example output:

```
{
  "total_items": 1,
  "total_ungrouped_items": 10,
  "total_supported_items": 1000,
  "assets": [
    {
      "group_val": "group",
      "asset_type_string": "VM",
      "configuration": {},
      "group_type_string": "VM",
      "group_type": "asg",
      "cluster_type": "asg",
      "type": "vm",
      "group_unique_id": "group-12345",
      "tags_value_list": [
        "ECSAutoScalingGroup"
      ],
      "vm_asset_unique_ids": [
        "vm_12345"
      ],
      "cloud_account_id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "compute": {
        "distribution_name": "Amazon",
        "num_cpus": 10,
        "memory": 7891,
        "num_vcpus_api": 2,
        "regions": [
          "us-east-1"
        ],
        "disks": [
          {
            "size": "7.87 GB",
            "used": "1.35 GB"
          }
        ],
        "private_dnss": [
          "ip-198-51-100-100.ec2.internal"
        ],
        "hardware_info_from_disk": 7,
        "roles": [
          {
            "name": "ssh",
            "is_public": false,
            "type": "ssh"
          }
        ],
        "memory_api": 8192,
        "regions_names": [
          "N. Virginia"
        ],
        "data_frameworks": [
          "cis_os_dist_indep"
        ],
        "cpu_type": "Intel(R) Xeon(R) Platinum 8252C CPU",
        "os_bit_mode_api": 64,
        "public_dnss": [
          "ec2-198-51-100-100.compute-1.amazonaws.com"
        ],
        "subnets": [
          "subnet-059fa51de12f0855c",
          "subnet-02ad498d5134c5499"
        ],
        "vpcs": [
          "vpc-1234567890"
        ],
        "os_bit_mode": 64,
        "mac_addresses": [
          "10:DD:32:45:00:11"
        ],
        "public_ips": [
          "198.51.100.100"
        ],
        "auto_updates": "off",
        "availability_zones": [
          "us-east-1a",
          "us-east-1b"
        ],
        "iam_role": "arn:aws:iam::12345:instance-profile/TestInstanceProfile-123",
        "num_vcpus": 2,
        "distribution_major_version": "1",
        "uptime": "2022-07-24T09:55:41+00:00",
        "security_groups": [
          "TestHostSecurityGroup-123"
        ],
        "last_update_time": "2022-05-26",
        "kernel_version": "4.14.281-144.502.amzn1.x86_64 (mockbuild@koji-pdx-corp-builder-64001) (gcc version 7.2.1 20170915 (Red Hat 7.2.1-2) (GCC)) #1 SMP Thu May 26 10:34:22 UTC 2022",
        "distribution_version": "2018.03 (2022.06.13)",
        "private_ips": [
          "198.51.100.100"
        ],
        "cpu_frequency": 3800,
        "cpu_frequency_api": 4500,
        "total_disks_bytes": 42265006080
      },
      "internet_facing_new": false,
      "asset_name": "test-asset",
      "tags_key_list": [
        "aws:autoscaling:groupName"
      ],
      "account_name": "test-account",
      "context": "data",
      "asset_type": "asg",
      "children_unique_ids": [
        "vm_12345"
      ],
      "model": {
        "data": {
          "AwsEc2Instance": {
            "AutoScalingGroup": {
              "model": {
                "name": "TestAutoScalingGroup-123",
                "asset_unique_id": "AwsAsg_542760197740_44d88612-fea8-a8f3-6de8-2e1278abb02f",
                "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
                "type": "AwsAsg"
              }
            }
          },
          "Vm": {
            "ImageName": "amzn-ami-2018.03.20220627-amazon-ecs-optimized",
            "ImageOwnerId": "591542846629",
            "ImageIsPublic": "True",
            "ImageId": "ami-061c737b1691cb15f",
            "ImageDescription": "Amazon Linux AMI amzn-ami-2018.03.20220627 x86_64 ECS HVM GP2",
            "InstanceType": "m5zn.large",
            "Name": "i-041e727ac105d8bd5"
          },
          "Inventory": {
            "NewSubCategory": "Virtual Instances",
            "DetectedCrownJewelReason": "Access: Host compromise",
            "Category": "VM",
            "UiUniqueField": "i-041e727ac105d8bd5",
            "IsInternetFacing": false,
            "NewCategory": "Compute Services",
            "Name": "i-041e727ac105d8bd5",
            "DetectedCrownJewelScore": 10,
            "SubCategory": "VM",
            "ModelTags": "{\"Category\": \"Compute\"}"
          }
        },
        "name": "i-041e727ac105d8bd5",
        "asset_unique_id": "example-asset-123",
        "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
        "type": "AwsEc2Instance"
      },
      "state": {
        "severity": "informational",
        "score": 4,
        "safe_since": "2022-07-31T14:03:04+00:00",
        "last_seen": "2022-08-13T01:22:08+00:00",
        "created_at": "2022-07-31T14:03:04+00:00",
        "status_time": "2022-07-31T14:03:04+00:00",
        "status": "exists"
      },
      "cluster_unique_id": "12345",
      "cluster_name": "test-cluster",
      "create_time": "2022-07-24T09:55:31+00:00",
      "tags_list": [
        {
          "value": "ECSAutoScalingGroup",
          "key": "aws:cloudformation:logical-id"
        }
      ],
      "group_name": "TestAutoScalingGroup-123",
      "level": 0,
      "tags_info_list": [
        "aws:cloudformation:logical-id|ECSAutoScalingGroup"
      ],
      "cloud_provider": "aws",
      "internet_facing": true,
      "organization_name": "Test",
      "asset_subcategory": "VM",
      "cloud_vendor_id": "1234567890",
      "asset_category": "VM",
      "asset_state": "running",
      "asset_labels": [
        "brute-force_attempts",
        "internet_facing"
      ],
      "organization_id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "vm": {
        "image_name": "amzn-ami-2018.03.20220627-amazon-ecs-optimized",
        "image_description": "Amazon Linux AMI amzn-ami-2018.03.20220627 x86_64 ECS HVM GP2",
        "image_is_public": true,
        "image_id": "ami-061c737b1691cb15f",
        "instance_type": "m5zn.large",
        "image_owner_id": "591542846629"
      },
      "cloud_provider_id": "123456789",
      "asset_unique_id": "example-asset-123",
      "num_children_unique_ids": 1
    }
  ]
}
```

#### Download Malicious File

This action is used to download the malicious file for the given alert ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_id|string|None|True|ID of the alert for which the file will be downloaded|None|orca-111|

Example input:

```
{
  "alert_id": "orca-111"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|content|bytes|False|Content of the file|
|success|boolean|True|Whether the action was successful|

Example output:

```
{
  "success": true,
  "content": "UEsDBBQAAQAIAEOc4VDdLFoEwgAAADQBAAANAAAAZWljYXJjb20yLnppcHh/TfxnimPnPKhgQN2dbxgmser+vfLMNzzE1xAxvrcMW29TW94War8gHCOQ3uAHD+InNly2Rm9lZcSEwSRaDbMgc4Er6/yC7KWSO7g4Kkb7dcHoYWfSDZt6Wjkvoc1hUy6jm2AZKg4FExQN/wS7n03sWy7VhU0CYVmsp1pmkVGqb4czd3OaAC07HmC/K9E3LO9yi9OejcZ+MJpA6zCLnUvZMr2KYjdl0s+9ENEspL/oTLErcDboDQ2DBJkKQpUsK0fRUEsBAgAAFAABAAgAQ5zhUN0sWgTCAAAANAEAAA0AAAAAAAAAAAAAAAAAAAAAAGVpY2FyY29tMi56aXBQSwUGAAAAAAEAAQA7AAAA7QAAAAAA"
}
```

#### Get Users

This action is used to get organization users information. Administrator privileges are required to perform this action.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|users|[]get_users_response|True|A response containing information about users|

Example output:

```
{
  "users": [
    {
      "id": "1111111-1111-1111-1111-11111111111",
      "all_cloud_accounts": true,
      "cloud_accounts": [],
      "role": {
        "id": "1111111-1111-1111-1111-11111111111",
        "name": "Test"
      },
      "user": {
        "id": "1111111-1111-1111-1111-11111111111",
        "email": "user@example.com",
        "first_name": "User",
        "last_name": "Test",
        "type": "normal"
      },
      "user_filters": [],
      "shiftleft_projects": []
    }
  ]
}
```

#### Verify Alert

This action is used to initiate verification for a given alert ID to check if it is resolved.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_id|string|None|True|ID of the alert that will be verified|None|orca-111|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|Current verification status|
|success|boolean|True|Whether the action was successful|

Example output:

```
{
  "status": "scanning",
  "success": true
}
```

#### Get Asset by ID

This action is used to get asset information by providing asset unique ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|asset_unique_id|string|None|True|Unique ID of the asset for which information will be obtained|None|example-asset|

Example input:

```
{
  "asset_unique_id": "example-asset"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|asset|asset|True|Information about the asset with the given unique ID|

Example output:

```
{
  "asset": {
    "group_val": "group",
    "asset_type_string": "VM",
    "configuration": {},
    "group_type_string": "VM",
    "group_type": "asg",
    "cluster_type": "asg",
    "type": "vm",
    "group_unique_id": "group-12345",
    "tags_value_list": [
      "ECSAutoScalingGroup"
    ],
    "vm_asset_unique_ids": [
      "vm_12345"
    ],
    "cloud_account_id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "compute": {
      "distribution_name": "Amazon",
      "num_cpus": 10,
      "memory": 7891,
      "num_vcpus_api": 2,
      "regions": [
        "us-east-1"
      ],
      "disks": [
        {
          "size": "7.87 GB",
          "used": "1.35 GB"
        }
      ],
      "private_dnss": [
        "ip-198-51-100-100.ec2.internal"
      ],
      "hardware_info_from_disk": 7,
      "roles": [
        {
          "name": "ssh",
          "is_public": false,
          "type": "ssh"
        }
      ],
      "memory_api": 8192,
      "regions_names": [
        "N. Virginia"
      ],
      "data_frameworks": [
        "cis_os_dist_indep"
      ],
      "cpu_type": "Intel(R) Xeon(R) Platinum 8252C CPU",
      "os_bit_mode_api": 64,
      "public_dnss": [
        "ec2-198-51-100-100.compute-1.amazonaws.com"
      ],
      "subnets": [
        "subnet-059fa51de12f0855c",
        "subnet-02ad498d5134c5499"
      ],
      "vpcs": [
        "vpc-013b79fa8fe9a81b6"
      ],
      "os_bit_mode": 64,
      "mac_addresses": [
        "10:DD:32:45:00:11"
      ],
      "public_ips": [
        "198.51.100.100"
      ],
      "auto_updates": "off",
      "availability_zones": [
        "us-east-1a",
        "us-east-1b"
      ],
      "iam_role": "arn:aws:iam::123:instance-profile/TestInstanceProfile-123",
      "num_vcpus": 2,
      "distribution_major_version": "1",
      "uptime": "2022-07-24T09:55:41+00:00",
      "security_groups": [
        "TestHostSecurityGroup-123"
      ],
      "last_update_time": "2022-05-26",
      "kernel_version": "4.14.281-144.502.amzn1.x86_64 (mockbuild@koji-pdx-corp-builder-64001) (gcc version 7.2.1 20170915 (Red Hat 7.2.1-2) (GCC)) #1 SMP Thu May 26 10:34:22 UTC 2022",
      "distribution_version": "2018.03 (2022.06.13)",
      "private_ips": [
        "198.51.100.100"
      ],
      "cpu_frequency": 3800,
      "cpu_frequency_api": 4500,
      "total_disks_bytes": 42265006080
    },
    "internet_facing_new": false,
    "asset_name": "example-asset",
    "tags_key_list": [
      "aws:autoscaling:groupName"
    ],
    "account_name": "test-account",
    "context": "data",
    "asset_type": "asg",
    "children_unique_ids": [
      "vm_12345"
    ],
    "model": {
      "data": {
        "AwsEc2Instance": {
          "AutoScalingGroup": {
            "model": {
              "name": "TestAutoScalingGroup-123",
              "asset_unique_id": "AwsAsg_542760197740_44d88612-fea8-a8f3-6de8-2e1278abb02f",
              "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
              "type": "AwsAsg"
            }
          }
        },
        "Vm": {
          "ImageName": "amzn-ami-2018.03.20220627-amazon-ecs-optimized",
          "ImageOwnerId": "591542846629",
          "ImageIsPublic": "True",
          "ImageId": "ami-061c737b1691cb15f",
          "ImageDescription": "Amazon Linux AMI amzn-ami-2018.03.20220627 x86_64 ECS HVM GP2",
          "InstanceType": "m5zn.large",
          "Name": "i-041e727ac105d8bd5"
        },
        "Inventory": {
          "NewSubCategory": "Virtual Instances",
          "DetectedCrownJewelReason": "Access: Host compromise",
          "Category": "VM",
          "UiUniqueField": "i-041e727ac105d8bd5",
          "IsInternetFacing": false,
          "NewCategory": "Compute Services",
          "Name": "i-041e727ac105d8bd5",
          "DetectedCrownJewelScore": 10,
          "SubCategory": "VM",
          "ModelTags": "{\"Category\": \"Compute\"}"
        }
      },
      "name": "i-041e727ac105d8bd5",
      "asset_unique_id": "example-asset",
      "id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
      "type": "AwsEc2Instance"
    },
    "state": {
      "severity": "informational",
      "score": 4,
      "safe_since": "2022-07-31T14:03:04+00:00",
      "last_seen": "2022-08-13T01:22:08+00:00",
      "created_at": "2022-07-31T14:03:04+00:00",
      "status_time": "2022-07-31T14:03:04+00:00",
      "status": "exists"
    },
    "cluster_unique_id": "12345",
    "cluster_name": "test-cluster",
    "create_time": "2022-07-24T09:55:31+00:00",
    "tags_list": [
      {
        "value": "ECSAutoScalingGroup",
        "key": "aws:cloudformation:logical-id"
      }
    ],
    "group_name": "TestAutoScalingGroup-123",
    "level": 0,
    "tags_info_list": [
      "aws:cloudformation:logical-id|ECSAutoScalingGroup"
    ],
    "cloud_provider": "aws",
    "internet_facing": false,
    "organization_name": "Test",
    "asset_subcategory": "VM",
    "cloud_vendor_id": "1234567890",
    "asset_category": "VM",
    "asset_state": "running",
    "organization_id": "44d88612-fea8-a8f3-6de8-2e1278abb02f",
    "vm": {
      "image_name": "amzn-ami-2018.03.20220627-amazon-ecs-optimized",
      "image_description": "Amazon Linux AMI amzn-ami-2018.03.20220627 x86_64 ECS HVM GP2",
      "image_is_public": true,
      "image_id": "ami-061c737b1691cb15f",
      "instance_type": "m5zn.large",
      "image_owner_id": "591542846629"
    },
    "cloud_provider_id": "9876543210",
    "asset_unique_id": "example-asset",
    "num_children_unique_ids": 1
  }
}
```

#### Update Alert Severity

This action is used to update the severity for the given alert ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_id|string|None|True|ID of the alert for which the severity will be updated|None|orca-111|
|severity|string|None|True|The severity of the alert to which it will be changed|None|hazardous|

Example input:

```
{
  "alert_id": "orca-111",
  "severity": "hazardous"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|update_alert_severity_response|False|A response with information about the update|

Example output:

```
{
  "response": {
    "user_email": "user@example.com",
    "user_name": "Example User",
    "alert_id": "orca-111",
    "asset_unique_id": "asset-1",
    "create_time": "2022-08-10T15:25:50+00:00",
    "type": "score_override",
    "details": {
      "description": "Alert risk level changed",
      "severity": "hazardous"
    }
  }
}
```

#### Update Alert Status

This action is used to update the status for the given alert ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_id|string|None|True|ID of the alert for which the status will be updated|None|orca-111|
|status|string|None|True|The status of the alert to which it will be changed|['in_progress', 'open', 'close', 'dismiss']|close|

Example input:

```
{
  "alert_id": "orca-111",
  "status": "close"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|update_alert_status_response|False|A response with information about the update|

Example output:

```
{
  "response": {
    "unique_id": "None",
    "user_email": "user@example.com",
    "user_name": "Example User",
    "alert_id": "orca-111",
    "asset_unique_id": "asset-1",
    "create_time": "2022-08-10T15:25:50+00:00",
    "type": "set_status",
    "sub_type": "closed",
    "details": {
      "description": "Alert status changed",
      "from": "open",
      "to": "closed"
    }
  }
}
```

#### Get Alerts

This action is used to get alerts that match the specified filter criteria. If no filters are given, all alerts will be returned.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filters|object|None|False|The object containing the fields against which the alerts will be filtered|None|{"state.severity": "hazardous"}|
|limit|integer|20|False|Maximum number of alerts returned (max value: 1000)|None|20|

Example input:

```
{
  "filters": {
    "state.severity": "hazardous"
  },
  "limit": 20
}
```

```
{
  "filters": {
    "state.status": "open",
    "alert_labels": "mitre: discovery"
  },
  "limit": 20
}
```

```
{
  "filters": {
    "data.title": "Classic Load Balancer (ELB) with public access",
    "type": "aws_elb_with_public_access"
  },
  "limit": 20
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alerts|[]alert|False|Results containing information about alerts|

Example output:

```
{
  "alerts": [
    {
      "data": {
        "recommendation": "It is recommended to associate {AwsEc2Elb} Classic Load Balancer with security groups that allow inbound traffic only from authorized IP addresses, for more details follow the link https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html.",
        "details": "Classic Load Balancer (ELB) provides basic load balancing across multiple Amazon EC2 instances and operates at both the request level and connection level. The load balancer {AwsEc2Elb} was discovered to be associated with a security group {AwsEc2Elb.SecurityGroups} that allows public ingress access without IP filtering (0.0.0.0/0). Load balancer configured with public access opens the application hosted behind the load balancer to attacks from malicious entities on the Internet.",
        "title": "Classic Load Balancer (ELB) with public access",
        "remediation_console": [
          ">1. Sign in to the AWS Management Console and open the **[EC2 console](https://console.aws.amazon.com/ec2)**.",
          ">2. In the navigation pane, under **Load Balancing**, choose **Load Balancers**.",
          ">3. Select the desired load balancer.",
          ">4. Under **Actions** choose **Edit security groups**.",
          ">5. Uncheck the boxes of the inbound permissive security groups.",
          ">6. Check the boxes of a more explicit inbound security groups.",
          ">7. Choose **Save**."
        ]
      },
      "alert_labels": [
        "mitre: discovery"
      ],
      "configuration": {
        "user_status": "open",
        "user_score": 3
      },
      "is_compliance": false,
      "description": "Classic Load Balancer (ELB) with public access",
      "recommendation": "It is recommended to associate 44d88612fea8a8f36de82e1278abb02f Classic Load Balancer with security groups that allow inbound traffic only from authorized IP addresses, for more details follow the link https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html.",
      "type": "aws_elb_with_public_access",
      "type_string": "Classic Load Balancer (ELB) with public access",
      "details": "Classic Load Balancer (ELB) provides basic load balancing across multiple Amazon EC2 instances and operates at both the request level and connection level. The load balancer a51a26a188ddb415d87d7f96b3c4a128 was discovered to be associated with a security group k8s-elb-a51a26a188ddb415d87d7f96b3c4a128 that allows public ingress access without IP filtering (0.0.0.0/0). Load balancer configured with public access opens the application hosted behind the load balancer to attacks from malicious entities on the Internet.",
      "state": {
        "severity": "hazardous",
        "last_updated": "2022-08-10T16:28:51+00:00",
        "last_seen": "2022-08-07T21:06:47+00:00",
        "in_verification": true,
        "created_at": "2022-03-19T16:55:08+00:00",
        "verification_status": "scan_initiated",
        "score": 3,
        "orca_score": 3,
        "alert_id": "orca-001",
        "high_since": "2022-08-10T16:28:51+00:00",
        "status_time": "2022-08-10T16:17:43+00:00",
        "status": "open"
      },
      "rule_query": "AwsEc2Elb with (Scheme = 'internet-facing') and SecurityGroups with SgIpPermissions with (IpRanges containing '0.0.0.0/0' or IpRanges containing '::/0') and not egress",
      "subject_type": "AwsEc2Elb",
      "tags_info_list": [
        "kubernetes.io/service-name|istio-system/istio-ingressgateway",
        "kubernetes.io/cluster/Omikron|owned"
      ],
      "is_rule": true,
      "type_key": "44d88612fea8a8f36de82e1278abb02f",
      "rule_id": "r27471a255e",
      "asset_state": "enabled",
      "asset_tags_info_list": [
        "kubernetes.io/service-name|istio-system/istio-ingressgateway",
        "kubernetes.io/cluster/Omikron|owned"
      ],
      "category": "Network misconfigurations"
    }
  ]
}
```

#### Get Alert by ID

This action is used to get alert information for given alert ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_id|string|None|True|ID of the alert for which information will be obtained|None|orca-111|

Example input:

```
{
  "alert_id": "orca-111"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alert|alert|True|Information about the alert with the given ID|

Example output:

```
{
  "alert": {
    "data": {
      "recommendation": "It is recommended to associate {AwsEc2Elb} Classic Load Balancer with security groups that allow inbound traffic only from authorized IP addresses, for more details follow the link https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html.",
      "details": "Classic Load Balancer (ELB) provides basic load balancing across multiple Amazon EC2 instances and operates at both the request level and connection level. The load balancer {AwsEc2Elb} was discovered to be associated with a security group {AwsEc2Elb.SecurityGroups} that allows public ingress access without IP filtering (0.0.0.0/0). Load balancer configured with public access opens the application hosted behind the load balancer to attacks from malicious entities on the Internet.",
      "title": "Classic Load Balancer (ELB) with public access",
      "remediation_console": [
        ">1. Sign in to the AWS Management Console and open the **[EC2 console](https://console.aws.amazon.com/ec2)**.",
        ">2. In the navigation pane, under **Load Balancing**, choose **Load Balancers**.",
        ">3. Select the desired load balancer.",
        ">4. Under **Actions** choose **Edit security groups**.",
        ">5. Uncheck the boxes of the inbound permissive security groups.",
        ">6. Check the boxes of a more explicit inbound security groups.",
        ">7. Choose **Save**."
      ]
    },
    "alert_labels": [
      "mitre: discovery"
    ],
    "configuration": {
      "user_status": "open",
      "user_score": 3
    },
    "is_compliance": false,
    "description": "Classic Load Balancer (ELB) with public access",
    "recommendation": "It is recommended to associate 44d88612fea8a8f36de82e1278abb02f Classic Load Balancer with security groups that allow inbound traffic only from authorized IP addresses, for more details follow the link https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html.",
    "type": "aws_elb_with_public_access",
    "type_string": "Classic Load Balancer (ELB) with public access",
    "details": "Classic Load Balancer (ELB) provides basic load balancing across multiple Amazon EC2 instances and operates at both the request level and connection level. The load balancer a51a26a188ddb415d87d7f96b3c4a128 was discovered to be associated with a security group k8s-elb-a51a26a188ddb415d87d7f96b3c4a128 that allows public ingress access without IP filtering (0.0.0.0/0). Load balancer configured with public access opens the application hosted behind the load balancer to attacks from malicious entities on the Internet.",
    "state": {
      "severity": "hazardous",
      "last_updated": "2022-08-10T16:28:51+00:00",
      "last_seen": "2022-08-07T21:06:47+00:00",
      "in_verification": true,
      "created_at": "2022-03-19T16:55:08+00:00",
      "verification_status": "scan_initiated",
      "score": 3,
      "orca_score": 3,
      "alert_id": "orca-111",
      "high_since": "2022-08-10T16:28:51+00:00",
      "status_time": "2022-08-10T16:17:43+00:00",
      "status": "open"
    },
    "rule_query": "AwsEc2Elb with (Scheme = 'internet-facing') and SecurityGroups with SgIpPermissions with (IpRanges containing '0.0.0.0/0' or IpRanges containing '::/0') and not egress",
    "subject_type": "AwsEc2Elb",
    "tags_info_list": [
      "kubernetes.io/service-name|istio-system/istio-ingressgateway",
      "kubernetes.io/cluster/Omikron|owned"
    ],
    "is_rule": true,
    "type_key": "44d88612fea8a8f36de82e1278abb02f",
    "rule_id": "r27471a255e",
    "asset_state": "enabled",
    "asset_tags_info_list": [
      "kubernetes.io/service-name|istio-system/istio-ingressgateway",
      "kubernetes.io/cluster/Omikron|owned"
    ],
    "category": "Network misconfigurations"
  }
}
```

### Triggers

#### New Alert

This trigger is used to indicate that a new alert has occurred.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|filters|[]object|None|False|The list of objects containing fields against which new alerts will be filtered|None|[{"field": "state.severity", "includes": ["hazardous"]}]|
|interval|integer|60|True|Interval between next poll in seconds, default value set to 60 seconds|None|60|

Example input:

```
{
  "filters": [
    {
      "field": "state.severity",
      "includes": [
        "hazardous"
      ]
    }
  ],
  "interval": 60
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alert|alert|False|Information about a new alert|

Example output:

```
{
  "alert": {
    "data": {
      "recommendation": "It is recommended to associate {AwsEc2Elb} Classic Load Balancer with security groups that allow inbound traffic only from authorized IP addresses, for more details follow the link https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html.",
      "details": "Classic Load Balancer (ELB) provides basic load balancing across multiple Amazon EC2 instances and operates at both the request level and connection level. The load balancer {AwsEc2Elb} was discovered to be associated with a security group {AwsEc2Elb.SecurityGroups} that allows public ingress access without IP filtering (0.0.0.0/0). Load balancer configured with public access opens the application hosted behind the load balancer to attacks from malicious entities on the Internet.",
      "title": "Classic Load Balancer (ELB) with public access",
      "remediation_console": [
        ">1. Sign in to the AWS Management Console and open the **[EC2 console](https://console.aws.amazon.com/ec2)**.",
        ">2. In the navigation pane, under **Load Balancing**, choose **Load Balancers**.",
        ">3. Select the desired load balancer.",
        ">4. Under **Actions** choose **Edit security groups**.",
        ">5. Uncheck the boxes of the inbound permissive security groups.",
        ">6. Check the boxes of a more explicit inbound security groups.",
        ">7. Choose **Save**."
      ]
    },
    "alert_labels": [
      "mitre: discovery"
    ],
    "configuration": {
      "user_status": "open",
      "user_score": 3
    },
    "is_compliance": false,
    "description": "Classic Load Balancer (ELB) with public access",
    "recommendation": "It is recommended to associate 44d88612fea8a8f36de82e1278abb02f Classic Load Balancer with security groups that allow inbound traffic only from authorized IP addresses, for more details follow the link https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-groups.html.",
    "type": "aws_elb_with_public_access",
    "type_string": "Classic Load Balancer (ELB) with public access",
    "details": "Classic Load Balancer (ELB) provides basic load balancing across multiple Amazon EC2 instances and operates at both the request level and connection level. The load balancer a51a26a188ddb415d87d7f96b3c4a128 was discovered to be associated with a security group k8s-elb-a51a26a188ddb415d87d7f96b3c4a128 that allows public ingress access without IP filtering (0.0.0.0/0). Load balancer configured with public access opens the application hosted behind the load balancer to attacks from malicious entities on the Internet.",
    "state": {
      "severity": "hazardous",
      "last_updated": "2022-08-10T16:28:51+00:00",
      "last_seen": "2022-08-07T21:06:47+00:00",
      "in_verification": true,
      "created_at": "2022-03-19T16:55:08+00:00",
      "verification_status": "scan_initiated",
      "score": 3,
      "orca_score": 3,
      "alert_id": "orca-111",
      "high_since": "2022-08-10T16:28:51+00:00",
      "status_time": "2022-08-10T16:17:43+00:00",
      "status": "open"
    },
    "rule_query": "AwsEc2Elb with (Scheme = 'internet-facing') and SecurityGroups with SgIpPermissions with (IpRanges containing '0.0.0.0/0' or IpRanges containing '::/0') and not egress",
    "subject_type": "AwsEc2Elb",
    "tags_info_list": [
      "kubernetes.io/service-name|istio-system/istio-ingressgateway",
      "kubernetes.io/cluster/Omikron|owned"
    ],
    "is_rule": true,
    "type_key": "44d88612fea8a8f36de82e1278abb02f",
    "rule_id": "r27471a255e",
    "asset_state": "enabled",
    "asset_tags_info_list": [
      "kubernetes.io/service-name|istio-system/istio-ingressgateway",
      "kubernetes.io/cluster/Omikron|owned"
    ],
    "category": "Network misconfigurations"
  }
}
```

### Custom Output Types

#### alert

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Alert Labels|[]string|False|Alert labels|
|Asset Auto Updates|string|False|Asset auto updates|
|Asset Availability Zones|[]string|False|Asset availability zones|
|Asset Distribution Major Version|string|False|Asset distribution major version|
|Asset Distribution Name|string|False|Asset distribution name|
|Asset Distribution Version|string|False|Asset distribution version|
|Asset Extra Data|object|False|Asset extra data|
|Asset First Private DNSs|[]string|False|Asset first private DNSs|
|Asset First Private IPs|[]string|False|Asset first private IPs|
|Asset First Public DNSs|[]string|False|Asset first public DNSs|
|Asset First Public IPs|[]string|False|Asset first public IPs|
|Asset Image ID|string|False|Asset image ID|
|Asset Info|object|False|Asset info|
|Asset Ingress Ports|[]string|False|Asset ingress ports|
|Asset Num Private DNSs|integer|False|Asset num private DNSs|
|Asset Num Private IPs|integer|False|Asset num private IPs|
|Asset Num Public DNSs|integer|False|Asset num public DNSs|
|Asset Num Public IPs|integer|False|Asset Num public IPs|
|Asset Regions|[]string|False|Asset regions|
|Asset Regions Names|[]string|False|Asset regions names|
|Asset Role Names|[]string|False|Asset role names|
|Asset State|string|False|Asset state|
|Asset Stopped|boolean|False|Asset stopped|
|Asset Tags Info List|[]string|False|Asset tags info list|
|Asset VPCs|[]string|False|Asset VPCs|
|Category|string|False|Category|
|Configuration|configuration|False|Configuration|
|Container Image Name|string|False|Container image name|
|Container K8s Pod Namespace|string|False|Container K8s pod namespace|
|Container Service Name|string|False|Container service name|
|CVE List|[]string|False|CVE list|
|Data|alert_data|False|Data|
|Description|string|False|Description|
|Details|string|False|Details|
|Finding Schema|object|False|Finding schema|
|Git Repo Sensitive Data Rules|[]string|False|Git repo sensitive data rules|
|Git Repo Sensitive Data Tags|[]string|False|Git repo sensitive data tags|
|Is Compliance|boolean|False|Is compliance|
|Is Rule|boolean|False|Is rule|
|Num Children Unique IDs|integer|False|Num children unique IDs|
|Priv|priv|False|Priv|
|Recommendation|string|False|Recommendation|
|Rule ID|string|False|Rule ID|
|Rule Query|string|False|Rule query|
|Severity Contributing Factors|[]string|False|Severity contributing factors|
|Severity Reducing Factors|[]string|False|Severity reducing factors|
|State|state|False|State|
|Subject Type|string|False|Subject type|
|Tags Info List|[]string|False|Tags info list|
|Type|string|False|Type|
|Type Key|string|False|Type key|
|Type String|string|False|Type string|
|User Defined|boolean|False|User defined|

#### alert_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Details|string|False|Details|
|Headline|string|False|Headline|
|Mitre Category|string|False|Mitre category|
|More Details|[]string|False|More details|
|Recommendation|string|False|Recommendation|
|Remediation Actions|[]string|False|Remediation actions|
|Remediation CLI|[]string|False|Remediation CLI|
|Remediation Console|[]string|False|Remediation console|
|Time Series Field|string|False|Time series field|
|Title|string|False|Title|

#### asset

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Account Name|string|False|Account name|
|Asset Category|string|False|Asset category|
|Asset Name|string|False|Asset name|
|Asset State|string|False|Asset state|
|Asset Subcategory|string|False|Asset subcategory|
|Asset Type String|string|False|Asset type string|
|Asset Unique ID|string|False|Asset unique ID|
|Asset Vendor ID|string|False|Asset vendor ID|
|Cloud Account ID|string|False|Cloud account ID|
|Cloud Provider|string|False|Cloud provider|
|Cloud Provider ID|string|False|Cloud provider ID|
|Cloud Vendor ID|string|False|Cloud vendor ID|
|Cluster Name|string|False|Cluster name|
|Configuration|object|False|Configuration|
|Group Name|string|False|Group name|
|Group Unique ID|string|False|Group unique ID|
|Group Value|string|False|Group value|
|Model|object|False|Model|
|Organization ID|string|False|Organization ID|
|Organization Name|string|False|Organization name|
|State|object|False|State|
|Type|string|False|Type|

#### configuration

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Comments Count|integer|False|Comments count|
|Jira Issue|string|False|Jira issue|
|Jira Issue Link|string|False|Jira issue link|
|Last Verified Event|string|False|Last verified event|
|Snooze Until|string|False|Snooze until|
|User Score|integer|False|User score|
|User Status|string|False|User status|

#### get_users_response

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Organization Name|string|False|Organization name|
|Pending Invites|[]invitation|False|Pending invites|
|Users|[]user|False|Users|

#### invitation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|All Cloud Account|boolean|False|All cloud account|
|Cloud Accounts|[]string|False|Cloud accounts|
|Email|string|False|Email|
|ID|string|False|ID|
|Invite Email Sent At|string|False|Invite email sent at|
|Role|string|False|Role|

#### priv

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Alert ID|string|False|Alert ID|
|Full Scan Time|string|False|Full scan time|
|Key|string|False|Key|
|Original Score|integer|False|Original score|
|Score|integer|False|Score|

#### state

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Alert ID|string|False|Alert ID|
|Closed Reason|string|False|Closed reason|
|Created At|string|False|Created at|
|High Since|string|False|High since|
|In Verification|boolean|False|In verification|
|Last Seen|string|False|Last seen|
|Last Updated|string|False|Last updated|
|Low Since|string|False|Low since|
|Score|integer|False|Score|
|Severity|string|False|Severity|
|Status|string|False|Status|
|Status Time|string|False|Status time|
|Verification Status|string|False|Verification status|

#### update_alert_details

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Description|string|False|Description|
|From|string|False|From|
|To|string|False|To|

#### update_alert_severity_response

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Alert ID|string|False|Alert ID|
|Asset Unique ID|string|False|Asset unique ID|
|Create Time|string|False|Create time|
|Details|update_severity_details|False|Details|
|Type|string|False|Type|
|Unique ID|string|False|Unique ID|
|User Email|string|False|User email|
|User Name|string|False|User name|

#### update_alert_status_response

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Alert ID|string|False|Alert ID|
|Asset Unique ID|string|False|Asset Unique ID|
|Create Time|string|False|Create time|
|Details|update_alert_details|False|Details|
|Subtype|string|False|Subtype|
|Type|string|False|Type|
|Unique ID|string|False|Unique ID|
|User Email|string|False|User email|
|User Name|string|False|User name|

#### update_severity_details

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Description|string|False|Description|
|Severity|string|False|Severity|

#### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Email|string|False|Email|
|First Name|string|False|First name|
|Last Name|string|False|Last name|
|User ID|string|False|User ID|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.0 - Get Users: Updated the API endpoint to return an array of users
* 1.0.0 - Initial plugin | Add Get Assets, Get Asset by ID, Get Alerts, Get Alert by ID, Update Alert Severity, Update Alert Status, Verify Alert, Download Malicious File, Get Users, Add User and Delete User actions | Add New Alert trigger

# Links

## References

* [Orca Security](https://orca.security/)

