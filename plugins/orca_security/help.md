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

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_token|credential_secret_key|None|True|Orca Security API Token|None|44d88612fea8a8f36de82e1278abb02f|None|None|
|region|string|US|True|The region for Orca Security|["US", "EU", "AU"]|US|None|None|

Example input:

```
{
  "api_token": "44d88612fea8a8f36de82e1278abb02f",
  "region": "US"
}
```

## Technical Details

### Actions


#### Add User

This action is used to create an invitation to the organization for the specified user. Administrator privileges are 
required to perform this action

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|all_cloud_accounts|boolean|None|True|Whether the user will have access to all cloud accounts|None|False|None|None|
|cloud_accounts|[]string|None|False|A list of cloud accounts to which the user will have access|None|["test-account"]|None|None|
|invite_user_email|string|None|True|Email address of the user for whom the invitation will be created|None|user@example.com|None|None|
|role|string|None|True|Role name or ID|None|44d88612-fea8-a8f3-6de8-2e1278abb02f|None|None|
|should_send_email|boolean|None|True|Whether the email should be sent|None|True|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|string|True|Status of the action performed|success|
  
Example output:

```
{
  "status": "success"
}
```

#### Delete User

This action is used to delete an invitation to the organization for the specified user. Administrator privileges are 
required to perform this action

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|delete_invite_email|string|None|True|Email address of the user for whom the invitation will be deleted|None|user@example.com|None|None|
  
Example input:

```
{
  "delete_invite_email": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|string|True|Status of the action performed|success|
  
Example output:

```
{
  "status": "success"
}
```

#### Download Malicious File

This action is used to download the malicious file for the given alert ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_id|string|None|True|ID of the alert for which the file will be downloaded|None|orca-111|None|None|
  
Example input:

```
{
  "alert_id": "orca-111"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|content|bytes|False|Content of the file|UEsDBBQAAQAIAEOc4VDdLFoEwgAAADQBAAANAAAAZWljYXJjb20yLnppcHh/TfxnimPnPKhgQN2dbxgmser+vfLMNzzE1xAxvrcMW29TW94War8gHCOQ3uAHD+InNly2Rm9lZcSEwSRaDbMgc4Er6/yC7KWSO7g4Kkb7dcHoYWfSDZt6Wjkvoc1hUy6jm2AZKg4FExQN/wS7n03sWy7VhU0CYVmsp1pmkVGqb4czd3OaAC07HmC/K9E3LO9yi9OejcZ+MJpA6zCLnUvZMr2KYjdl0s+9ENEspL/oTLErcDboDQ2DBJkKQpUsK0fRUEsBAgAAFAABAAgAQ5zhUN0sWgTCAAAANAEAAA0AAAAAAAAAAAAAAAAAAAAAAGVpY2FyY29tMi56aXBQSwUGAAAAAAEAAQA7AAAA7QAAAAAA|
|success|boolean|True|Whether the action was successful|True|
  
Example output:

```
{
  "content": "UEsDBBQAAQAIAEOc4VDdLFoEwgAAADQBAAANAAAAZWljYXJjb20yLnppcHh/TfxnimPnPKhgQN2dbxgmser+vfLMNzzE1xAxvrcMW29TW94War8gHCOQ3uAHD+InNly2Rm9lZcSEwSRaDbMgc4Er6/yC7KWSO7g4Kkb7dcHoYWfSDZt6Wjkvoc1hUy6jm2AZKg4FExQN/wS7n03sWy7VhU0CYVmsp1pmkVGqb4czd3OaAC07HmC/K9E3LO9yi9OejcZ+MJpA6zCLnUvZMr2KYjdl0s+9ENEspL/oTLErcDboDQ2DBJkKQpUsK0fRUEsBAgAAFAABAAgAQ5zhUN0sWgTCAAAANAEAAA0AAAAAAAAAAAAAAAAAAAAAAGVpY2FyY29tMi56aXBQSwUGAAAAAAEAAQA7AAAA7QAAAAAA",
  "success": true
}
```

#### Get Alert by ID

This action is used to get alert information for given alert ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_id|string|None|True|ID of the alert for which information will be obtained|None|orca-111|None|None|
  
Example input:

```
{
  "alert_id": "orca-111"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alert|alert|True|Information about the alert with the given ID|None|
  
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

#### Get Alerts

This action is used to get alerts that match the specified filter criteria. If no filters are given, all alerts will be
 returned

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filters|object|None|False|The object containing the fields against which the alerts will be filtered|None|{"state.severity": "hazardous"}|None|None|
|limit|integer|20|False|Maximum number of alerts returned (max value: 1000)|None|20|None|None|
  
Example input:

```
{
  "filters": {
    "state.severity": "hazardous"
  },
  "limit": 20
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alerts|[]alert|False|Results containing information about alerts|None|
  
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

#### Get Asset by ID

This action is used to get asset information by providing asset unique ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_unique_id|string|None|True|Unique ID of the asset for which information will be obtained|None|example-asset|None|None|
  
Example input:

```
{
  "asset_unique_id": "example-asset"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|asset|asset|True|Information about the asset with the given unique ID|None|
  
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

#### Get Assets

This action is used to get assets that match the specified filter criteria. If no inputs are given, all assets will be 
returned

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_labels|string|None|False|The label of the asset|None|internet_facing|None|None|
|asset_state|string|None|False|The state of the asset|None|running|None|None|
|asset_type|string|None|False|The type of the asset|None|container|None|None|
|asset_unique_id|string|None|False|Unique ID of the asset for which information will be obtained|None|example-asset-123|None|None|
|cloud_provider_id|string|None|False|ID of the cloud provider for which the assets will be returned|None|123456789|None|None|
|compute_regions|string|None|False|The region for which the assets will be returned|None|us-east-1|None|None|
|compute_vpcs|string|None|False|The virtual private cloud|None|vpc-1234567890|None|None|
|internet_facing|string|None|False|Whether asset is accessible from the internet|None|True|None|None|
|state_score|string|None|False|The score of the asset|None|4|None|None|
|state_severity|string|None|False|The severity of the asset|None|informational|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assets|[]asset|False|Results containing information about assets|None|
|total_items|integer|True|Total number of assets|1|
|total_supported_items|integer|False|Total number of supported assets|1000|
|total_ungrouped_items|integer|False|Total number of ungrouped assets|10|
  
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

#### Get Users

This action is used to get organization users information. Administrator privileges are required to perform this action

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|users|[]get_users_response|True|A response containing information about users|None|
  
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

#### Update Alert Severity

This action is used to update the severity for the given alert ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_id|string|None|True|ID of the alert for which the severity will be updated|None|orca-111|None|None|
|severity|string|None|True|The severity of the alert to which it will be changed|None|hazardous|None|None|
  
Example input:

```
{
  "alert_id": "orca-111",
  "severity": "hazardous"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|update_alert_severity_response|False|A response with information about the update|None|
  
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

This action is used to update the status for the given alert ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_id|string|None|True|ID of the alert for which the status will be updated|None|orca-111|None|None|
|status|string|None|True|The status of the alert to which it will be changed|["in_progress", "open", "close", "dismiss"]|close|None|None|
  
Example input:

```
{
  "alert_id": "orca-111",
  "status": "close"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|update_alert_status_response|False|A response with information about the update|None|
  
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

#### Verify Alert

This action is used to initiate verification for a given alert ID to check if it is resolved

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_id|string|None|True|ID of the alert that will be verified|None|orca-111|None|None|
  
Example input:

```
{
  "alert_id": "orca-111"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|string|False|Current verification status|scanning|
|success|boolean|True|Whether the action was successful|True|
  
Example output:

```
{
  "status": "scanning",
  "success": true
}
```
### Triggers


#### New Alert

This trigger is used to indicate that a new alert has occurred

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filters|[]object|None|False|The list of objects containing fields against which new alerts will be filtered|None|[{"field": "state.severity", "includes": ["hazardous"]}]|None|None|
|interval|integer|60|True|Interval between next poll in seconds, default value set to 60 seconds|None|60|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alert|alert|False|Information about a new alert|None|
  
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
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**alert_data**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Details|string|None|False|Details|None|
|Headline|string|None|False|Headline|None|
|Mitre Category|string|None|False|Mitre category|None|
|More Details|[]string|None|False|More details|None|
|Recommendation|string|None|False|Recommendation|None|
|Remediation Actions|[]string|None|False|Remediation actions|None|
|Remediation CLI|[]string|None|False|Remediation CLI|None|
|Remediation Console|[]string|None|False|Remediation console|None|
|Time Series Field|string|None|False|Time series field|None|
|Title|string|None|False|Title|None|
  
**configuration**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Comments Count|integer|None|False|Comments count|None|
|Jira Issue|string|None|False|Jira issue|None|
|Jira Issue Link|string|None|False|Jira issue link|None|
|Last Verified Event|string|None|False|Last verified event|None|
|Snooze Until|string|None|False|Snooze until|None|
|User Score|integer|None|False|User score|None|
|User Status|string|None|False|User status|None|
  
**priv**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alert ID|string|None|False|Alert ID|None|
|Full Scan Time|string|None|False|Full scan time|None|
|Key|string|None|False|Key|None|
|Original Score|integer|None|False|Original score|None|
|Score|integer|None|False|Score|None|
  
**state**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alert ID|string|None|False|Alert ID|None|
|Closed Reason|string|None|False|Closed reason|None|
|Created At|string|None|False|Created at|None|
|High Since|string|None|False|High since|None|
|In Verification|boolean|None|False|In verification|None|
|Last Seen|string|None|False|Last seen|None|
|Last Updated|string|None|False|Last updated|None|
|Low Since|string|None|False|Low since|None|
|Score|integer|None|False|Score|None|
|Severity|string|None|False|Severity|None|
|Status|string|None|False|Status|None|
|Status Time|string|None|False|Status time|None|
|Verification Status|string|None|False|Verification status|None|
  
**alert**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alert Labels|[]string|None|False|Alert labels|None|
|Asset Auto Updates|string|None|False|Asset auto updates|None|
|Asset Availability Zones|[]string|None|False|Asset availability zones|None|
|Asset Distribution Major Version|string|None|False|Asset distribution major version|None|
|Asset Distribution Name|string|None|False|Asset distribution name|None|
|Asset Distribution Version|string|None|False|Asset distribution version|None|
|Asset Extra Data|object|None|False|Asset extra data|None|
|Asset First Private DNSs|[]string|None|False|Asset first private DNSs|None|
|Asset First Private IPs|[]string|None|False|Asset first private IPs|None|
|Asset First Public DNSs|[]string|None|False|Asset first public DNSs|None|
|Asset First Public IPs|[]string|None|False|Asset first public IPs|None|
|Asset Image ID|string|None|False|Asset image ID|None|
|Asset Info|object|None|False|Asset info|None|
|Asset Ingress Ports|[]string|None|False|Asset ingress ports|None|
|Asset Num Private DNSs|integer|None|False|Asset num private DNSs|None|
|Asset Num Private IPs|integer|None|False|Asset num private IPs|None|
|Asset Num Public DNSs|integer|None|False|Asset num public DNSs|None|
|Asset Num Public IPs|integer|None|False|Asset Num public IPs|None|
|Asset Regions|[]string|None|False|Asset regions|None|
|Asset Regions Names|[]string|None|False|Asset regions names|None|
|Asset Role Names|[]string|None|False|Asset role names|None|
|Asset State|string|None|False|Asset state|None|
|Asset Stopped|boolean|None|False|Asset stopped|None|
|Asset Tags Info List|[]string|None|False|Asset tags info list|None|
|Asset VPCs|[]string|None|False|Asset VPCs|None|
|Category|string|None|False|Category|None|
|Configuration|configuration|None|False|Configuration|None|
|Container Image Name|string|None|False|Container image name|None|
|Container K8s Pod Namespace|string|None|False|Container K8s pod namespace|None|
|Container Service Name|string|None|False|Container service name|None|
|CVE List|[]string|None|False|CVE list|None|
|Data|alert_data|None|False|Data|None|
|Description|string|None|False|Description|None|
|Details|string|None|False|Details|None|
|Finding Schema|object|None|False|Finding schema|None|
|Git Repo Sensitive Data Rules|[]string|None|False|Git repo sensitive data rules|None|
|Git Repo Sensitive Data Tags|[]string|None|False|Git repo sensitive data tags|None|
|Is Compliance|boolean|None|False|Is compliance|None|
|Is Rule|boolean|None|False|Is rule|None|
|Num Children Unique IDs|integer|None|False|Num children unique IDs|None|
|Priv|priv|None|False|Priv|None|
|Recommendation|string|None|False|Recommendation|None|
|Rule ID|string|None|False|Rule ID|None|
|Rule Query|string|None|False|Rule query|None|
|Severity Contributing Factors|[]string|None|False|Severity contributing factors|None|
|Severity Reducing Factors|[]string|None|False|Severity reducing factors|None|
|State|state|None|False|State|None|
|Subject Type|string|None|False|Subject type|None|
|Tags Info List|[]string|None|False|Tags info list|None|
|Type|string|None|False|Type|None|
|Type Key|string|None|False|Type key|None|
|Type String|string|None|False|Type string|None|
|User Defined|boolean|None|False|User defined|None|
  
**asset**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Account Name|string|None|False|Account name|None|
|Asset Category|string|None|False|Asset category|None|
|Asset Name|string|None|False|Asset name|None|
|Asset State|string|None|False|Asset state|None|
|Asset Subcategory|string|None|False|Asset subcategory|None|
|Asset Type String|string|None|False|Asset type string|None|
|Asset Unique ID|string|None|False|Asset unique ID|None|
|Asset Vendor ID|string|None|False|Asset vendor ID|None|
|Cloud Account ID|string|None|False|Cloud account ID|None|
|Cloud Provider|string|None|False|Cloud provider|None|
|Cloud Provider ID|string|None|False|Cloud provider ID|None|
|Cloud Vendor ID|string|None|False|Cloud vendor ID|None|
|Cluster Name|string|None|False|Cluster name|None|
|Configuration|object|None|False|Configuration|None|
|Group Name|string|None|False|Group name|None|
|Group Unique ID|string|None|False|Group unique ID|None|
|Group Value|string|None|False|Group value|None|
|Model|object|None|False|Model|None|
|Organization ID|string|None|False|Organization ID|None|
|Organization Name|string|None|False|Organization name|None|
|State|object|None|False|State|None|
|Type|string|None|False|Type|None|
  
**update_alert_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|Description|None|
|From|string|None|False|From|None|
|To|string|None|False|To|None|
  
**update_alert_status_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alert ID|string|None|False|Alert ID|None|
|Asset Unique ID|string|None|False|Asset Unique ID|None|
|Create Time|string|None|False|Create time|None|
|Details|update_alert_details|None|False|Details|None|
|Subtype|string|None|False|Subtype|None|
|Type|string|None|False|Type|None|
|Unique ID|string|None|False|Unique ID|None|
|User Email|string|None|False|User email|None|
|User Name|string|None|False|User name|None|
  
**update_severity_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|Description|None|
|Severity|string|None|False|Severity|None|
  
**update_alert_severity_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alert ID|string|None|False|Alert ID|None|
|Asset Unique ID|string|None|False|Asset unique ID|None|
|Create Time|string|None|False|Create time|None|
|Details|update_severity_details|None|False|Details|None|
|Type|string|None|False|Type|None|
|Unique ID|string|None|False|Unique ID|None|
|User Email|string|None|False|User email|None|
|User Name|string|None|False|User name|None|
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Email|string|None|False|Email|None|
|First Name|string|None|False|First name|None|
|User ID|string|None|False|User ID|None|
|Last Name|string|None|False|Last name|None|
|Type|string|None|False|User's account type|None|
  
**role**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|User Role ID|string|None|False|ID of the user role|None|
|Name|string|None|False|User role name|None|
  
**cloud_accounts**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Cloud Account ID|string|None|False|ID of cloud account|None|
|Name|string|None|False|The cloud account display name|None|
  
**get_users_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|All Cloud Accounts|boolean|None|False|All cloud accounts|None|
|Cloud Accounts|[]cloud_accounts|None|False|List of cloud accounts|None|
|User Access Role ID|string|None|False|ID of user access role|None|
|User Role Details|role|None|False|Details of the role assigned to the user|None|
|Shift left projects|[]string|None|False|List of user shift left projects|None|
|User Details|user|None|False|User object containing the details|None|
|User Filters|[]string|None|False|List of user filter IDs|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 2.0.1 - Bumping requirements.txt | SDK bump to 6.2.0
* 2.0.0 - Get Users: Updated the API endpoint to return an array of users
* 1.0.0 - Initial plugin | Add Get Assets, Get Asset by ID, Get Alerts, Get Alert by ID, Update Alert Severity, Update Alert Status, Verify Alert, Download Malicious File, Get Users, Add User and Delete User actions | Add New Alert trigger

# Links

* [Orca Security](https://orca.security/)

## References

* [Orca Security](https://orca.security/)