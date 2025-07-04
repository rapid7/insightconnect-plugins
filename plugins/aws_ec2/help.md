# Description

[Amazon EC2](https://aws.amazon.com/documentation/ec2) is a Amazon Elastic Compute Cloud (Amazon EC2) provides resizable computing capacity in the Amazon Web Services (AWS) cloud.
This plugin allows security practitioners to perform host containment and implement security group policies in addition to general management of EC2 instances

# Key Features

* Manage EC2 instances for asset containment
* Manage security groups for network containment

# Requirements

* An AWS account with admin permissions for EC2
* An AWS Access Key ID and Secret Access Key

# Supported Product Versions

* botocore 1.27.96

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|aws_access_key_id|credential_secret_key|None|True|The ID of the AWS Access Key to use for authentication with AWS|None|KKILPPPPPRAA4OBNTHE2|None|None|
|aws_secret_access_key|credential_secret_key|None|True|The AWS Secret Access Key used for signing requests with the given AWS Access Key ID. Note: Domain is not required|None|pp20bF88GZ2PGY+QUAAc2BSNA/6TUprPpYMCSc0tD|None|None|
|external_id|string|None|False|External ID given during role creation|None|exampleexternalid|None|None|
|region|string|None|True|The AWS Region to use for requests. An example would be us-east-1|None|us-east-1|None|None|
|role_arn|string|None|False|AWS IAM role ARN to assume|None|arn:aws:iam::123456781111:role/ExampleRole|None|None|

Example input:

```
{
  "aws_access_key_id": "KKILPPPPPRAA4OBNTHE2",
  "aws_secret_access_key": "pp20bF88GZ2PGY+QUAAc2BSNA/6TUprPpYMCSc0tD",
  "external_id": "exampleexternalid",
  "region": "us-east-1",
  "role_arn": "arn:aws:iam::123456781111:role/ExampleRole"
}
```

## Technical Details

### Actions


#### Authorize Security Group Egress

This action is used to add one or more egress rules to a security group for use with a VPC [EC2-VPC only]. See 
[http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupEgress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupEgress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assume_role_params|assume_role_params|None|False|Parameters that allows to assume IAM role|None|{'role_arn': 'arn:aws:iam::123456781111:role/ExampleRole', 'external_id': 'ExampleExternalID', 'region': 'us-west-2'}|None|None|
|cidr_ip|string|None|False|Not supported|None|10.20.0.0/27|None|None|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response|None|True|None|None|
|from_port|integer|None|False|Not supported|None|8800|None|None|
|group_id|string|None|True|The ID of the security group|None|sg-a02005k2|None|None|
|ip_permissions|[]ip_permission|None|False|One or more sets of IP permissions|None|[{"from_port": 8080, "ip_protocol": "tcp", "ip_ranges": [{"cidr_ip": "10.20.0.0/27", "description": "Blah"}], "to_port": 8090}]|None|None|
|ip_protocol|string|None|False|Not supported|None|UDP|None|None|
|source_security_group_name|string|None|False|Not supported|None|launch-wizard-1|None|None|
|source_security_group_owner_id|string|None|False|Not supported|None|otheraccountgroup|None|None|
|to_port|integer|None|False|Not supported|None|8900|None|None|
  
Example input:

```
{
  "assume_role_params": {
    "external_id": "ExampleExternalID",
    "region": "us-west-2",
    "role_arn": "arn:aws:iam::123456781111:role/ExampleRole"
  },
  "cidr_ip": "10.20.0.0/27",
  "dry_run": true,
  "from_port": 8800,
  "group_id": "sg-a02005k2",
  "ip_permissions": [
    {
      "from_port": 8080,
      "ip_protocol": "tcp",
      "ip_ranges": [
        {
          "cidr_ip": "10.20.0.0/27",
          "description": "Blah"
        }
      ],
      "to_port": 8090
    }
  ],
  "ip_protocol": "UDP",
  "source_security_group_name": "launch-wizard-1",
  "source_security_group_owner_id": "otheraccountgroup",
  "to_port": 8900
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response_metadata|response_metadata|True|Metadata about the response from AWS|{'HTTP Status Code': 200, 'Request ID': '564416517006'}|
  
Example output:

```
{
  "response_metadata": {
    "HTTP Status Code": 200,
    "Request ID": "564416517006"
  }
}
```

#### Authorize Security Group Ingress

This action is used to add one or more ingress rules to a security group. See 
[http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assume_role_params|assume_role_params|None|False|Parameters that allows to assume IAM role|None|{'role_arn': 'arn:aws:iam::123456781111:role/ExampleRole', 'external_id': 'ExampleExternalID', 'region': 'us-west-2'}|None|None|
|cidr_ip|string|None|False|The CIDR IPv4 address range|None|10.2.0.0/27|None|None|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response|None|False|None|None|
|from_port|integer|None|False|The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number|None|8800|None|None|
|group_id|string|None|False|The ID of the security group|None|sg-123456|None|None|
|group_name|string|None|False|[EC2-Classic, default VPC] The name of the security group|None|default|None|None|
|ip_permissions|[]ip_permission|None|False|One or more sets of IP permissions|None|[{"from_port": 8080, "ip_protocol": "tcp", "ip_ranges": [{"cidr_ip": "10.20.0.0/27", "description": "Blah"}], "to_port": 8090}]|None|None|
|ip_protocol|string|None|False|The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers)|None|UDP|None|None|
|source_security_group_name|string|None|False|[EC2-Classic, default VPC] The name of the source security group|None|group_name|None|None|
|source_security_group_owner_id|string|None|False|[EC2-Classic] The AWS account ID for the source security group, if the source security group is in a different account|None|otheraccount|None|None|
|to_port|integer|None|False|The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code number|None|8900|None|None|
  
Example input:

```
{
  "assume_role_params": {
    "external_id": "ExampleExternalID",
    "region": "us-west-2",
    "role_arn": "arn:aws:iam::123456781111:role/ExampleRole"
  },
  "cidr_ip": "10.2.0.0/27",
  "dry_run": false,
  "from_port": 8800,
  "group_id": "sg-123456",
  "group_name": "default",
  "ip_permissions": [
    {
      "from_port": 8080,
      "ip_protocol": "tcp",
      "ip_ranges": [
        {
          "cidr_ip": "10.20.0.0/27",
          "description": "Blah"
        }
      ],
      "to_port": 8090
    }
  ],
  "ip_protocol": "UDP",
  "source_security_group_name": "group_name",
  "source_security_group_owner_id": "otheraccount",
  "to_port": 8900
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response_metadata|response_metadata|True|Metadata about the response from AWS|{'HTTP Status Code': 200, 'Request ID': '564416517006'}|
  
Example output:

```
{
  "response_metadata": {
    "HTTP Status Code": 200,
    "Request ID": "564416517006"
  }
}
```

#### Describe Instances

This action is used to describe one or more of your instances. See 
[http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClassicLinkInstances.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClassicLinkInstances.html)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assume_role_params|assume_role_params|None|False|Parameters that allows to assume IAM role|None|{'role_arn': 'arn:aws:iam::123456781111:role/ExampleRole', 'external_id': 'ExampleExternalID', 'region': 'us-west-2'}|None|None|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response|None|False|None|None|
|filters|[]filter|None|False|One or more filters|None|{'name': 'instance-type', 'values': ['t2.micro', 't3.micro']}|None|None|
|instance_ids|[]string|None|False|One or more instance IDs|None|["i-0dd117dc6df90be2e"]|None|None|
  
Example input:

```
{
  "assume_role_params": {
    "external_id": "ExampleExternalID",
    "region": "us-west-2",
    "role_arn": "arn:aws:iam::123456781111:role/ExampleRole"
  },
  "dry_run": false,
  "filters": {
    "name": "instance-type",
    "values": [
      "t2.micro",
      "t3.micro"
    ]
  },
  "instance_ids": [
    "i-0dd117dc6df90be2e"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|reservations|[]reservation|False|Zero or more reservations|[{"groups": [], "instances": [{"ami_launch_index": 0, "architecture": "x86_64", "block_device_mappings": [{"device_name": "/dev/xvda", "ebs": {"attach_time": "2025-01-21T17:47:47+00:00", "delete_on_termination": True, "status": "attached", "volume_id": "vol-04f0094363642d765"}}], "client_token": "fleet-473d853d-b60e-448d-0e98-89aa13f8447d-0", "Ebs Optimized": False, "Ena Support": True, "Hypervisor": "xen", "IAM Instance Profile": {"arn": "arn:aws:iam::444478183327:instance-profile/eks-2ac9d683-48ff-fedb-54be-02db947f90b0", "id": "AIPAWO7HW26P27VYYTD4I"}, "image_id": "ami-094fb6db0f574f0d6", "instance_id": "i-04e80852e9b93033f", "instance_type": "m5.4xlarge", "instance_lifecycle": "spot", "key_name": "integrationalliacestage1", "launch_time": "2025-07-01T10:46:15+00:00", "monitoring": {"state": "disabled"}, "network_interfaces": [{"attachment": {"attach_time": "2025-07-01T10:46:15+00:00", "attachment_id": "eni-attach-05cc60f70ab8a6ff4", "delete_on_termination": True, "device_index": 0, "network_card_index": 0, "status": "attached"}, "description": "aws-K8S-i-0ad23684d897727a0", "groups": [{"group_id": "sg-0e7c1c06433e52cea", "group_name": "alliance-stage-1-worker-sg"}, {"group_id": "sg-0d11f2b3f19a1f2f9", "group_name": "alliance-stage-1-worker-for-pd"}], "ipv6_addresses": [], "mac_address": "0e:e4:77:59:4d:d9", "network_interface_id": "eni-0dc5b31f15e9d42e5", "owner_id": "444478183327", "private_dns_name": "ip-10-0-166-192.ec2.internal", "private_ip_address": "10.0.166.192", "private_ip_addresses": [{"primary": True, "private_dns_name": "ip-10-0-166-192.ec2.internal", "private_ip_address": "10.0.166.192"}], "source_dest_check": True, "subnet_id": "subnet-0435e9bc29b1cde05", "vpc_id": "vpc-0be18e98afa1e5b00"}], "placement": {"availability_zone": "us-east-1b", "group_name": "", "tenancy": "default"}, "private_dns_name": "ip-10-0-190-192.ec2.internal", "private_ip_address": "10.0.190.192", "product_codes": [], "public_dns_name": "", "root_device_name": "/dev/xvda", "root_device_type": "ebs", "security_groups": [{"group_id": "sg-0e7c1c06433e52cea", "group_name": "alliance-stage-1-worker-sg"}, {"group_id": "sg-0d11f2b3f19a1f2f9", "group_name": "alliance-stage-1-worker-for-pd"}], "source_dest_check": True, "spot_instance_request_id": "sir-n77764rg", "state": {"code": 16, "name": "running"}, "subnet_id": "subnet-02b2d189058e4cf23", "tags": [{"key": "aws:ec2launchtemplate:version", "value": "1"}, {"key": "Environment", "value": "Staging"}], "usage_operation": "RunInstances", "usage_operation_update_time": "2025-07-01T19:00:38+00:00", "virtualization_type": "hvm", "vpc_id": "vpc-0be18e98afa1e5b00"}], "owner_id": "444478183327", "requester_id": "564416517006", "reservation_id": "r-082d830d6529d632d"}]|
|response_metadata|response_metadata|True|Metadata about the response from AWS|{'http_status_code': 200, 'request_id': 'a8ace239-fbc0-4253-81c8-0865e93ca081'}|
  
Example output:

```
{
  "reservations": [
    {
      "groups": [],
      "instances": [
        {
          "Ebs Optimized": false,
          "Ena Support": true,
          "Hypervisor": "xen",
          "IAM Instance Profile": {
            "arn": "arn:aws:iam::444478183327:instance-profile/eks-2ac9d683-48ff-fedb-54be-02db947f90b0",
            "id": "AIPAWO7HW26P27VYYTD4I"
          },
          "ami_launch_index": 0,
          "architecture": "x86_64",
          "block_device_mappings": [
            {
              "device_name": "/dev/xvda",
              "ebs": {
                "attach_time": "2025-01-21T17:47:47+00:00",
                "delete_on_termination": true,
                "status": "attached",
                "volume_id": "vol-04f0094363642d765"
              }
            }
          ],
          "client_token": "fleet-473d853d-b60e-448d-0e98-89aa13f8447d-0",
          "image_id": "ami-094fb6db0f574f0d6",
          "instance_id": "i-04e80852e9b93033f",
          "instance_lifecycle": "spot",
          "instance_type": "m5.4xlarge",
          "key_name": "integrationalliacestage1",
          "launch_time": "2025-07-01T10:46:15+00:00",
          "monitoring": {
            "state": "disabled"
          },
          "network_interfaces": [
            {
              "attachment": {
                "attach_time": "2025-07-01T10:46:15+00:00",
                "attachment_id": "eni-attach-05cc60f70ab8a6ff4",
                "delete_on_termination": true,
                "device_index": 0,
                "network_card_index": 0,
                "status": "attached"
              },
              "description": "aws-K8S-i-0ad23684d897727a0",
              "groups": [
                {
                  "group_id": "sg-0e7c1c06433e52cea",
                  "group_name": "alliance-stage-1-worker-sg"
                },
                {
                  "group_id": "sg-0d11f2b3f19a1f2f9",
                  "group_name": "alliance-stage-1-worker-for-pd"
                }
              ],
              "ipv6_addresses": [],
              "mac_address": "0e:e4:77:59:4d:d9",
              "network_interface_id": "eni-0dc5b31f15e9d42e5",
              "owner_id": "444478183327",
              "private_dns_name": "ip-10-0-166-192.ec2.internal",
              "private_ip_address": "10.0.166.192",
              "private_ip_addresses": [
                {
                  "primary": true,
                  "private_dns_name": "ip-10-0-166-192.ec2.internal",
                  "private_ip_address": "10.0.166.192"
                }
              ],
              "source_dest_check": true,
              "subnet_id": "subnet-0435e9bc29b1cde05",
              "vpc_id": "vpc-0be18e98afa1e5b00"
            }
          ],
          "placement": {
            "availability_zone": "us-east-1b",
            "group_name": "",
            "tenancy": "default"
          },
          "private_dns_name": "ip-10-0-190-192.ec2.internal",
          "private_ip_address": "10.0.190.192",
          "product_codes": [],
          "public_dns_name": "",
          "root_device_name": "/dev/xvda",
          "root_device_type": "ebs",
          "security_groups": [
            {
              "group_id": "sg-0e7c1c06433e52cea",
              "group_name": "alliance-stage-1-worker-sg"
            },
            {
              "group_id": "sg-0d11f2b3f19a1f2f9",
              "group_name": "alliance-stage-1-worker-for-pd"
            }
          ],
          "source_dest_check": true,
          "spot_instance_request_id": "sir-n77764rg",
          "state": {
            "code": 16,
            "name": "running"
          },
          "subnet_id": "subnet-02b2d189058e4cf23",
          "tags": [
            {
              "key": "aws:ec2launchtemplate:version",
              "value": "1"
            },
            {
              "key": "Environment",
              "value": "Staging"
            }
          ],
          "usage_operation": "RunInstances",
          "usage_operation_update_time": "2025-07-01T19:00:38+00:00",
          "virtualization_type": "hvm",
          "vpc_id": "vpc-0be18e98afa1e5b00"
        }
      ],
      "owner_id": "444478183327",
      "requester_id": "564416517006",
      "reservation_id": "r-082d830d6529d632d"
    }
  ],
  "response_metadata": {
    "http_status_code": 200,
    "request_id": "a8ace239-fbc0-4253-81c8-0865e93ca081"
  }
}
```

#### Describe Security Groups

This action is used to describe one or more of your security groups. See 
[http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assume_role_params|assume_role_params|None|False|Parameters that allows to assume IAM role|None|{'role_arn': 'arn:aws:iam::123456781111:role/ExampleRole', 'external_id': 'ExampleExternalID', 'region': 'us-west-2'}|None|None|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response|None|False|None|None|
|filters|[]filter|None|False|One or more filters|None|[{"name": "ip-permission.from-port", "values": [80]}]|None|None|
|group_ids|[]string|None|False|One or more security group IDs|None|["sg-123456"]|None|None|
|group_names|[]string|None|False|[EC2-Classic and default VPC only] One or more security group names|None|["groupname"]|None|None|
  
Example input:

```
{
  "assume_role_params": {
    "external_id": "ExampleExternalID",
    "region": "us-west-2",
    "role_arn": "arn:aws:iam::123456781111:role/ExampleRole"
  },
  "dry_run": false,
  "filters": [
    {
      "name": "ip-permission.from-port",
      "values": [
        80
      ]
    }
  ],
  "group_ids": [
    "sg-123456"
  ],
  "group_names": [
    "groupname"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response_metadata|response_metadata|True|Metadata about the response from AWS|{'http_status_code': 200, 'request_id': 'ad7c7803-e83a-4207-9fd3-42c47a038926'}|
|security_groups|[]security_group|False|Information about one or more security groups|[{"description": "Microsoft Windows Server 2019 created 2025-02-07T06:34:33.847Z", "group_id": "sg-0b0c45cacf690376a", "group_name": "Microsoft Windows Server 2019 with HyperV-2025", "ip_permissions": [{"from_port": 80, "ip_protocol": "tcp", "ip_ranges": [{"cidr_ip": "0.0.0.0/0"}], "ipv6_ranges": [], "prefix_list_ids": [], "to_port": 80, "user_id_group_pairs": []}], "user_id_group_pairs": [], "ip_permissions_egress": [{"ip_protocol": "-1", "ip_ranges": [{"cidr_ip": "0.0.0.0/0"}], "ipv6_ranges": [], "prefix_list_ids": [], "user_id_group_pairs": []}], "owner_id": "28926151422", "vpc_id": "vpc-33821512"}]|
  
Example output:

```
{
  "response_metadata": {
    "http_status_code": 200,
    "request_id": "ad7c7803-e83a-4207-9fd3-42c47a038926"
  },
  "security_groups": [
    {
      "description": "Microsoft Windows Server 2019 created 2025-02-07T06:34:33.847Z",
      "group_id": "sg-0b0c45cacf690376a",
      "group_name": "Microsoft Windows Server 2019 with HyperV-2025",
      "ip_permissions": [
        {
          "from_port": 80,
          "ip_protocol": "tcp",
          "ip_ranges": [
            {
              "cidr_ip": "0.0.0.0/0"
            }
          ],
          "ipv6_ranges": [],
          "prefix_list_ids": [],
          "to_port": 80,
          "user_id_group_pairs": []
        }
      ],
      "ip_permissions_egress": [
        {
          "ip_protocol": "-1",
          "ip_ranges": [
            {
              "cidr_ip": "0.0.0.0/0"
            }
          ],
          "ipv6_ranges": [],
          "prefix_list_ids": [],
          "user_id_group_pairs": []
        }
      ],
      "owner_id": "28926151422",
      "user_id_group_pairs": [],
      "vpc_id": "vpc-33821512"
    }
  ]
}
```

#### Revoke Security Group Egress

This action is used to remove one or more egress rules from a security group for EC2-VPC ([EC2-VPC only]). See 
[http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assume_role_params|assume_role_params|None|False|Parameters that allows to assume IAM role|None|{'role_arn': 'arn:aws:iam::123456781111:role/ExampleRole', 'external_id': 'ExampleExternalID', 'region': 'us-west-2'}|None|None|
|cidr_ip|string|None|False|Not supported|None|10.10.0.0/27|None|None|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response|None|True|None|None|
|from_port|integer|None|False|Not supported|None|8000|None|None|
|group_id|string|None|True|The ID of the security group|None|sg-123456|None|None|
|ip_permissions|[]ip_permission|None|False|One or more sets of IP permissions|None|[{"from_port": 8080, "ip_protocol": "tcp", "ip_ranges": [{"cidr_ip": "10.20.0.0/27", "description": "Blah"}], "to_port": 8090}]|None|None|
|ip_protocol|string|None|False|Not supported|None|UDP|None|None|
|source_security_group_name|string|None|False|Not supported|None|sourcegroup|None|None|
|source_security_group_owner_id|string|None|False|Not supported|None|ownergroup|None|None|
|to_port|integer|None|False|Not supported|None|9000|None|None|
  
Example input:

```
{
  "assume_role_params": {
    "external_id": "ExampleExternalID",
    "region": "us-west-2",
    "role_arn": "arn:aws:iam::123456781111:role/ExampleRole"
  },
  "cidr_ip": "10.10.0.0/27",
  "dry_run": true,
  "from_port": 8000,
  "group_id": "sg-123456",
  "ip_permissions": [
    {
      "from_port": 8080,
      "ip_protocol": "tcp",
      "ip_ranges": [
        {
          "cidr_ip": "10.20.0.0/27",
          "description": "Blah"
        }
      ],
      "to_port": 8090
    }
  ],
  "ip_protocol": "UDP",
  "source_security_group_name": "sourcegroup",
  "source_security_group_owner_id": "ownergroup",
  "to_port": 9000
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response_metadata|response_metadata|True|Metadata about the response from AWS|{'http_status_code': 200, 'request_id': 'a824e239-fbc110-4553-71c8-0865e433ca08'}|
  
Example output:

```
{
  "response_metadata": {
    "http_status_code": 200,
    "request_id": "a824e239-fbc110-4553-71c8-0865e433ca08"
  }
}
```

#### Revoke Security Group Ingress

This action is used to remove one or more ingress rules from a security group. See 
[http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupIngress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupIngress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assume_role_params|assume_role_params|None|False|Parameters that allows to assume IAM role|None|{'role_arn': 'arn:aws:iam::123456781111:role/ExampleRole', 'external_id': 'ExampleExternalID', 'region': 'us-west-2'}|None|None|
|cidr_ip|string|None|False|The CIDR IP address range|None|10.2.0.0/27|None|None|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response|None|True|None|None|
|from_port|integer|None|False|The start of port range for the TCP and UDP protocols, or an ICMP type number|None|8000|None|None|
|group_id|string|None|False|The ID of the security group|None|sg-123456|None|None|
|group_name|string|None|False|[EC2-Classic, default VPC] The name of the security group|None|groupname|None|None|
|ip_permissions|[]ip_permission|None|False|One or more sets of IP permissions|None|[{"from_port": 8080, "ip_protocol": "tcp", "ip_ranges": [{"cidr_ip": "10.20.0.0/27", "description": "Blah"}], "to_port": 8090}]|None|None|
|ip_protocol|string|None|False|The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers)|None|UDP|None|None|
|source_security_group_name|string|None|False|[EC2-Classic, default VPC] The name of the source security group|None|sourcegroup|None|None|
|source_security_group_owner_id|string|None|False|[EC2-Classic] The AWS account ID of the source security group, if the source security group is in a different account|None|ownergroup|None|None|
|to_port|integer|None|False|The end of port range for the TCP and UDP protocols, or an ICMP code number|None|9000|None|None|
  
Example input:

```
{
  "assume_role_params": {
    "external_id": "ExampleExternalID",
    "region": "us-west-2",
    "role_arn": "arn:aws:iam::123456781111:role/ExampleRole"
  },
  "cidr_ip": "10.2.0.0/27",
  "dry_run": true,
  "from_port": 8000,
  "group_id": "sg-123456",
  "group_name": "groupname",
  "ip_permissions": [
    {
      "from_port": 8080,
      "ip_protocol": "tcp",
      "ip_ranges": [
        {
          "cidr_ip": "10.20.0.0/27",
          "description": "Blah"
        }
      ],
      "to_port": 8090
    }
  ],
  "ip_protocol": "UDP",
  "source_security_group_name": "sourcegroup",
  "source_security_group_owner_id": "ownergroup",
  "to_port": 9000
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response_metadata|response_metadata|True|Metadata about the response from AWS|{'http_status_code': 200, 'request_id': 'b39sh34r-fbc110-7385-09c8-08hsn3v8g'}|
  
Example output:

```
{
  "response_metadata": {
    "http_status_code": 200,
    "request_id": "b39sh34r-fbc110-7385-09c8-08hsn3v8g"
  }
}
```

#### Update Security Group Rule Descriptions Egress

This action is used to update the description of an egress (outbound) security group rule [EC2-VPC only]. See 
[http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsEgress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsEgress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assume_role_params|assume_role_params|None|False|Parameters that allows to assume IAM role|None|{'role_arn': 'arn:aws:iam::123456781111:role/ExampleRole', 'external_id': 'ExampleExternalID', 'region': 'us-west-2'}|None|None|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response|None|True|None|None|
|group_id|string|None|False|The ID of the security group|None|sg-123456|None|None|
|group_name|string|None|False|[Default VPC] The name of the security group|None|groupname|None|None|
|ip_permissions|[]ip_permission|None|True|The IP permissions for the security group rule|None|[{"from_port": 8080, "ip_protocol": "tcp", "ip_ranges": [{"cidr_ip": "10.20.0.0/27", "description": "Blah"}], "to_port": 8090}]|None|None|
  
Example input:

```
{
  "assume_role_params": {
    "external_id": "ExampleExternalID",
    "region": "us-west-2",
    "role_arn": "arn:aws:iam::123456781111:role/ExampleRole"
  },
  "dry_run": true,
  "group_id": "sg-123456",
  "group_name": "groupname",
  "ip_permissions": [
    {
      "from_port": 8080,
      "ip_protocol": "tcp",
      "ip_ranges": [
        {
          "cidr_ip": "10.20.0.0/27",
          "description": "Blah"
        }
      ],
      "to_port": 8090
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response_metadata|response_metadata|True|Metadata about the response from AWS|{'http_status_code': 200, 'request_id': 'lklwmsv92v-si202-1192-003e-22uabamw'}|
|return|boolean|False|Returns true if the request succeeds; otherwise, returns an error|True|
  
Example output:

```
{
  "response_metadata": {
    "http_status_code": 200,
    "request_id": "lklwmsv92v-si202-1192-003e-22uabamw"
  },
  "return": true
}
```

#### Update Security Group Rule Descriptions Ingress

This action is used to update the description of an ingress (inbound) security group rule. See 
[http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsIngress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsIngress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|assume_role_params|assume_role_params|None|False|Parameters that allows to assume IAM role|None|{'role_arn': 'arn:aws:iam::123456781111:role/ExampleRole', 'external_id': 'ExampleExternalID', 'region': 'us-west-2'}|None|None|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response|None|True|None|None|
|group_id|string|None|False|The ID of the security group|None|sg-123456|None|None|
|group_name|string|None|False|[EC2-Classic, default VPC] The name of the security group|None|groupname|None|None|
|ip_permissions|[]ip_permission|None|True|The IP permissions for the security group rule|None|[{"from_port": 8080, "ip_protocol": "tcp", "ip_ranges": [{"cidr_ip": "10.20.0.0/27", "description": "Blah"}], "to_port": 8090}]|None|None|
  
Example input:

```
{
  "assume_role_params": {
    "external_id": "ExampleExternalID",
    "region": "us-west-2",
    "role_arn": "arn:aws:iam::123456781111:role/ExampleRole"
  },
  "dry_run": true,
  "group_id": "sg-123456",
  "group_name": "groupname",
  "ip_permissions": [
    {
      "from_port": 8080,
      "ip_protocol": "tcp",
      "ip_ranges": [
        {
          "cidr_ip": "10.20.0.0/27",
          "description": "Blah"
        }
      ],
      "to_port": 8090
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response_metadata|response_metadata|True|Metadata about the response from AWS|{'http_status_code': 200, 'request_id': 'dusbw8bgs-339s-1201-2245-33ajka'}|
|return|boolean|False|Returns true if the request succeeds; otherwise, returns an error|True|
  
Example output:

```
{
  "response_metadata": {
    "http_status_code": 200,
    "request_id": "dusbw8bgs-339s-1201-2245-33ajka"
  },
  "return": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**instance_network_interface_association**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IP Owner ID|string|None|False|The ID of the owner of the Elastic IP address|None|
|Public DNS Name|string|None|False|The public DNS name|None|
|Public IP|string|None|False|The public IP address or Elastic IP address bound to the network interface|None|
  
**instance_private_ip_address**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Association|instance_network_interface_association|None|False|The association information for an Elastic IP address for the network interface|None|
|Primary|boolean|None|False|Indicates whether this IPv4 address is the primary private IP address of the network interface|None|
|Private DNS Name|string|None|False|The private IPv4 DNS name|None|
|Private IP Address|string|None|False|The private IPv4 address of the network interface|None|
  
**instance_ipv6_address**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IPv6 Address|string|None|False|The IPv6 address|None|
  
**group_identifier**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Group ID|string|None|False|The ID of the security group|None|
|Group Name|string|None|False|The name of the security group|None|
  
**instance_network_interface_attachment**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attach Time|string|None|False|The time stamp when the attachment initiated|None|
|Attachment ID|string|None|False|The ID of the network interface attachment|None|
|Delete On Termination|boolean|None|False|Indicates whether the network interface is deleted when the instance is terminated|None|
|Device Index|integer|None|False|The index of the device on the instance for the network interface attachment|None|
|Status|string|None|False|The attachment state|None|
  
**ebs_instance_block_device**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attach Time|string|None|False|The time stamp when the attachment initiated|None|
|Delete On Termination|boolean|None|False|Indicates whether the volume is deleted on instance termination|None|
|Status|string|None|False|The attachment state|None|
|Volume ID|string|None|False|The ID of the EBS volume|None|
  
**user_id_group_pair**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|A description for the security group rule that references this user ID group pair|None|
|Group ID|string|None|False|The ID of the security group|None|
|Group Name|string|None|False|The name of the security group|None|
|Peering Status|string|None|False|The status of a VPC peering connection, if applicable|None|
|User ID|string|None|False|The ID of an AWS account|None|
|VPC ID|string|None|False|The ID of the VPC for the referenced security group, if applicable|None|
|VPC Peering Connection ID|string|None|False|The ID of the VPC peering connection, if applicable|None|
  
**prefix_list_id**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|A description for the security group rule that references this prefix list ID|None|
|Prefix List ID|string|None|False|The ID of the prefix|None|
  
**ipv6_range**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CIDR IPv6|string|None|False|The IPv6 CIDR range|None|
|Description|string|None|False|A description for the security group rule that references this IPv6 address range|None|
  
**ip_range**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CIDR IP|string|None|False|The IPv4 CIDR range|None|
|Description|string|None|False|A description for the security group rule that references this IPv4 address range|None|
  
**tag**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Key|string|None|False|The key of the tag|None|
|Value|string|None|False|The value of the tag|None|
  
**state_reason**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Code|string|None|False|The reason code for the state change|None|
|Message|string|None|False|The message for the state change|None|
  
**instance_network_interface**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Association|instance_network_interface_association|None|False|The association information for an Elastic IPv4 associated with the network interface|None|
|Attachment|instance_network_interface_attachment|None|False|The network interface attachment|None|
|Description|string|None|False|The description|None|
|Groups|[]group_identifier|None|False|One or more security groups|None|
|IPv6 Addresses|[]instance_ipv6_address|None|False|One or more IPv6 addresses associated with the network interface|None|
|MAC Address|string|None|False|The MAC address|None|
|Network Interface ID|string|None|False|The ID of the network interface|None|
|Owner ID|string|None|False|The ID of the AWS account that created the network interface|None|
|Private DNS Name|string|None|False|The private DNS name|None|
|Private IP Address|string|None|False|The IPv4 address of the network interface within the subnet|None|
|Private IP Addresses|[]instance_private_ip_address|None|False|One or more private IPv4 addresses associated with the network interface|None|
|Source Dest Check|boolean|None|False|Indicates whether to validate network traffic to or from this network interface|None|
|Status|string|None|False|The status of the network interface|None|
|Subnet ID|string|None|False|The ID of the subnet|None|
|VPC ID|string|None|False|The ID of the VPC|None|
  
**elastic_gpu_association**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Elastic GPU Association ID|string|None|False|The ID of the association|None|
|Elastic GPU Association State|string|None|False|The state of the association between the instance and the Elastic GPU|None|
|Elastic GPU Association Time|string|None|False|The time the Elastic GPU was associated with the instance|None|
|Elastic GPU ID|string|None|False|The ID of the Elastic GPU|None|
  
**iam_instance_profile**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ARN|string|None|False|The Amazon Resource Name (ARN) of the instance profile|None|
|ID|string|None|False|The ID of the instance profile|None|
  
**instance_block_device_mapping**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Device Name|string|None|False|The device name (for example, /dev/sdh or xvdh)|None|
|Ebs|ebs_instance_block_device|None|False|Parameters used to automatically set up EBS volumes when the instance is launched|None|
  
**instance_state**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Code|integer|None|False|The low byte represents the state|None|
|Name|string|None|False|The current state of the instance|None|
  
**product_code**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Product Code ID|string|None|False|The product code|None|
|Product Code Type|string|None|False|The type of product code|None|
  
**placement**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Affinity|string|None|False|The affinity setting for the instance on the Dedicated Host|None|
|Availability Zone|string|None|False|The Availability Zone of the instance|None|
|Group Name|string|None|False|The name of the placement group the instance is in (for cluster compute instances)|None|
|Host ID|string|None|False|The ID of the Dedicated Host on which the instance resides|None|
|Spread Domain|string|None|False|Reserved for future use|None|
|Tenancy|string|None|False|The tenancy of the instance (if the instance is running in a VPC)|None|
  
**monitoring**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|State|string|None|False|Indicates whether detailed monitoring is enabled|None|
  
**ip_permission**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|From Port|integer|None|False|The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number|None|
|IP Protocol|string|None|False|The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers)|None|
|IP Ranges|[]ip_range|None|False|One or more IPv4 ranges|None|
|IPv6 Ranges|[]ipv6_range|None|False|[EC2-VPC only] One or more IPv6 ranges|None|
|Prefix List IDs|[]prefix_list_id|None|False|(Valid for AuthorizeSecurityGroupEgress, RevokeSecurityGroupEgress and DescribeSecurityGroups only) One or more prefix list IDs for an AWS service|None|
|To Port|integer|None|False|The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code|None|
|User ID Group Pairs|[]user_id_group_pair|None|False|One or more security group and AWS account ID pairs|None|
  
**instance**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|AMI Launch Index|integer|None|False|The AMI launch index, which can be used to find this instance in the launch group|None|
|Architecture|string|None|False|The architecture of the image|None|
|Block Device Mappings|[]instance_block_device_mapping|None|False|Any block device mapping entries for the instance|None|
|Client Token|string|None|False|The idempotency token you provided when you launched the instance, if applicable|None|
|Ebs Optimized|boolean|None|False|Indicates whether the instance is optimized for Amazon EBS I/O|None|
|Elastic GPU Associations|[]elastic_gpu_association|None|False|The Elastic GPU associated with the instance|None|
|Ena Support|boolean|None|False|Specifies whether enhanced networking with ENA is enabled|None|
|Hypervisor|string|None|False|The hypervisor type of the instance|None|
|IAM Instance Profile|iam_instance_profile|None|False|The IAM instance profile associated with the instance, if applicable|None|
|Image ID|string|None|False|The ID of the AMI used to launch the instance|None|
|Instance ID|string|None|False|The ID of the instance|None|
|Instance Lifecycle|string|None|False|Indicates whether this is a Spot Instance or a Scheduled Instance|None|
|Instance Type|string|None|False|The instance type|None|
|Kernel ID|string|None|False|The kernel associated with this instance, if applicable|None|
|Key Name|string|None|False|The name of the key pair, if this instance was launched with an associated key pair|None|
|Launch Time|string|None|False|The time the instance was launched|None|
|Monitoring|monitoring|None|False|The monitoring for the instance|None|
|Network Interfaces|[]instance_network_interface|None|False|[EC2-VPC] One or more network interfaces for the instance|None|
|Placement|placement|None|False|The location where the instance launched, if applicable|None|
|Platform|string|None|False|The value is Windows for Windows instances; otherwise blank|None|
|Private DNS Name|string|None|False|(IPv4 only) The private DNS hostname name assigned to the instance|None|
|Private IP Address|string|None|False|The private IPv4 address assigned to the instance|None|
|Product Codes|[]product_code|None|False|The product codes attached to this instance, if applicable|None|
|Public DNS Name|string|None|False|(IPv4 only) The public DNS name assigned to the instance|None|
|Public IP Address|string|None|False|The public IPv4 address assigned to the instance, if applicable|None|
|Ramdisk ID|string|None|False|The RAM disk associated with this instance, if applicable|None|
|Root Device Name|string|None|False|The device name of the root device volume (for example, /dev/sda1)|None|
|Root Device Type|string|None|False|The root device type used by the AMI|None|
|Security Groups|[]group_identifier|None|False|One or more security groups for the instance|None|
|Source Dest Check|boolean|None|False|Specifies whether to enable an instance launched in a VPC to perform NAT|None|
|Spot Instance Request ID|string|None|False|If the request is a Spot Instance request, the ID of the request|None|
|Sriov Net Support|string|None|False|Specifies whether enhanced networking with the Intel 82599 Virtual Function interface is enabled|None|
|State|instance_state|None|False|The current state of the instance|None|
|State Reason|state_reason|None|False|The reason for the most recent state transition|None|
|State Transition Reason|string|None|False|The reason for the most recent state transition|None|
|Subnet ID|string|None|False|[EC2-VPC] The ID of the subnet in which the instance is running|None|
|Tags|[]tag|None|False|Any tags assigned to the instance|None|
|Virtualization Type|string|None|False|The virtualization type of the instance|None|
|VPC ID|string|None|False|[EC2-VPC] The ID of the VPC in which the instance is running|None|
  
**response_metadata**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HTTP Status Code|integer|None|True|HTTP status code for the request|None|
|Request ID|string|None|True|Unique identifier for the request|None|
  
**security_group**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|A description of the security group|None|
|Group ID|string|None|False|The ID of the security group|None|
|Group Name|string|None|False|The name of the security group|None|
|IP Permissions|[]ip_permission|None|False|One or more inbound rules associated with the security group|None|
|IP Permissions Egress|[]ip_permission|None|False|[EC2-VPC] One or more outbound rules associated with the security group|None|
|Owner ID|string|None|False|The AWS account ID of the owner of the security group|None|
|Tags|[]tag|None|False|Any tags assigned to the security group|None|
|VPC ID|string|None|False|[EC2-VPC] The ID of the VPC for the security group|None|
  
**filter**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|The name of the filter|None|
|Values|[]string|None|False|One or more filter values|None|
  
**reservation**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Groups|[]group_identifier|None|False|[EC2-Classic only] One or more security groups|None|
|Instances|[]instance|None|False|One or more instances|None|
|Owner ID|string|None|False|The ID of the AWS account that owns the reservation|None|
|Requester ID|string|None|False|The ID of the requester that launched the instances on your behalf (for example, AWS Management Console or Auto Scaling)|None|
|Reservation ID|string|None|False|The ID of the reservation|None|
  
**assume_role_params**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|External ID|string|None|False|External ID given during role creation|None|
|Region|string|None|False|Which section of the AWS cloud is being inspected|None|
|Role ARN|string|None|False|AWS IAM role ARN to assume|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.3.1 - SDK Bump to 6.3.7 | Resolved Snyk Vulnerabilities
* 1.3.0 - Add region input field to all Actions
* 1.2.1 - Updated Connection and Actions to use related AWS Client in SDK
* 1.2.0 - Updated Connect and Action inputs to include Role ARN and External ID to provide support for AWS Assume Role functionality at both an Action and a Connection level
* 1.1.0 - Update plugin runtime to InsightConnect
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.2 - SSL bug fix in SDK
* 0.1.1 - Fix connection test not passing output validation
* 0.1.0 - Initial plugin

# Links

* [AWS EC2](https://aws.amazon.com/ec2/)

## References

* [Documentation Overview](https://aws.amazon.com/documentation/ec2)
* [API Reference](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html)