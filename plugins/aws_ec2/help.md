# Description

[Amazon EC2](https://aws.amazon.com/documentation/ec2) is a Amazon Elastic Compute Cloud (Amazon EC2) provides resizable computing capacity in the Amazon Web Services (AWS) cloud.
This plugin allows security practictioners to perform host containment and implement security group policies in addition
to general management of EC2 instances.

# Key Features

* Manage EC2 instances for asset containment
* Manage security groups for network containment

# Requirements

* An AWS account with admin permissions for EC2
* An AWS Access Key ID and Secret Access Key

# Supported Product Versions

* botocore 1.26.5

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|aws_access_key_id|credential_secret_key|None|True|The ID of the AWS Access Key to use for authentication with AWS|None|KKILPPPPPRAA4OBNTHE2|
|aws_secret_access_key|credential_secret_key|None|True|The AWS Secret Access Key used for signing requests with the given AWS Access Key ID. Note: Domain is not required|None|pp20bF88GZ2PGY+QUAAc2BSNA/6TUprPpYMCSc0tD|
|region|string|None|True|The AWS Region to use for requests. An example would be us-east-1|None|us-east-1|

Example input:

```
{
  "aws_access_key_id": "KKILPPPPPRAA4OBNTHE2",
  "aws_secret_access_key": "pp20bF88GZ2PGY+QUAAc2BSNA/6TUprPpYMCSc0tD",
  "region": "us-east-1"
}
```

## Technical Details

### Actions

#### Authorize Security Group Egress

[EC2-VPC only] Adds one or more egress rules to a security group for use with a VPC. See [http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupEgress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupEgress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|cidr_ip|string|None|False|Not supported|None|10.20.0.0/27|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response|None|True|
|from_port|integer|None|False|Not supported|None|8800|
|group_id|string|None|True|The ID of the security group|None|sg-a02005k2|
|ip_permissions|[]ip_permission|None|False|One or more sets of IP permissions|None|["{ "from_port": 8080, "ip_protocol": "tcp", "ip_ranges" : [{ "cidr_ip": "10.20.0.0/27", "description": "Blah" }], "to_port": 8090}"]|
|ip_protocol|string|None|False|Not supported|None|UDP|
|source_security_group_name|string|None|False|Not supported|None|launch-wizard-1|
|source_security_group_owner_id|string|None|False|Not supported|None|otheraccountgroup|
|to_port|integer|None|False|Not supported|None|8900|
|role_arn|string|None|False|AWS IAM role ARN to assume|None|arn:aws:iam::123456781111:role/ExampleRole|
|external_id|string|None|False|External ID given during role creation|None|exampleexternalid|

Example input:

```
{
  "cidr_ip":"10.20.0.0/27",
  "dry_run":true,
  "from_port":8800,
  "group_id":"sg-a02005k2",
  "ip_permissions":[
    {
      "from_port":8080,
      "ip_protocol":"tcp",
      "ip_ranges":[
        {
          "cidr_ip":"10.20.0.0/27",
          "description":"Blah"
        }
      ],
      "to_port":8090
    }
  ],
  "ip_protocol":"UDP",
  "source_security_group_name":"launch-wizard-1",
  "source_security_group_owner_id":"otheraccountgroup",
  "to_port":8900
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

#### Authorize Security Group Ingress

Adds one or more ingress rules to a security group. See [http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|cidr_ip|string|None|False|The CIDR IPv4 address range|None|10.2.0.0/27|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response|None|False|
|from_port|integer|None|False|The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number|None|8800|
|group_id|string|None|False|The ID of the security group|None|sg-123456|
|group_name|string|None|False|[EC2-Classic, default VPC] The name of the security group|None|default|
|ip_permissions|[]ip_permission|None|False|One or more sets of IP permissions|None|["{ "from_port": 8080, "ip_protocol": "tcp", "ip_ranges" : [{ "cidr_ip": "10.20.0.0/27", "description": "Blah" }], "to_port": 8090}"]|
|ip_protocol|string|None|False|The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers)|None|UDP|
|source_security_group_name|string|None|False|[EC2-Classic, default VPC] The name of the source security group|None|group_name|
|source_security_group_owner_id|string|None|False|[EC2-Classic] The AWS account ID for the source security group, if the source security group is in a different account|None|otheraccount|
|to_port|integer|None|False|The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code number|None|8900|
|role_arn|string|None|False|AWS IAM role ARN to assume|None|arn:aws:iam::123456781111:role/ExampleRole|
|external_id|string|None|False|External ID given during role creation|None|exampleexternalid|

Example input:

```
{
  "cidr_ip": "10.2.0.0/27",
  "dry_run": false,
  "from_port": 8800,
  "group_id": "sg-123456",
  "group_name": "default",
  "ip_permissions":[
    {
      "from_port":8080,
      "ip_protocol":"tcp",
      "ip_ranges":[
        {
          "cidr_ip":"10.20.0.0/27",
          "description":"Blah"
        }
      ],
      "to_port":8090
    }
  ],
  "ip_protocol": "UDP",
  "source_security_group_name": "group_name",
  "source_security_group_owner_id": "otheraccount",
  "to_port": 8900
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

#### Describe Instances

Describes one or more of your instances. See [http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClassicLinkInstances.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClassicLinkInstances.html)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response|None|False|
|filters|[]filter|None|False|One or more filters|None|{'name': 'instance-type', 'values': ['t2.micro', 't3.micro']}|
|instance_ids|[]string|None|False|One or more instance IDs|None|["i-0dd117dc6df90be2e"]|
|role_arn|string|None|False|AWS IAM role ARN to assume|None|arn:aws:iam::123456781111:role/ExampleRole|
|external_id|string|None|False|External ID given during role creation|None|exampleexternalid|

Example input:

```
{
  "dry_run":false,
  "filters":{
    "name":"instance-type",
    "values":[
      "t2.micro",
      "t3.micro"
    ]
  },
  "instance_ids":[
    "i-0dd117dc6df90be2e"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|reservations|[]reservation|False|Zero or more reservations|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

#### Describe Security Groups

Describes one or more of your security groups. See [http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response|None|False|
|filters|[]filter|None|False|One or more filters|None|["{"name": "ip-permission.from-port", "values": [80]}"]|
|group_ids|[]string|None|False|One or more security group IDs|None|["sg-123456"]|
|group_names|[]string|None|False|[EC2-Classic and default VPC only] One or more security group names|None|["groupname"]|
|role_arn|string|None|False|AWS IAM role ARN to assume|None|arn:aws:iam::123456781111:role/ExampleRole|
|external_id|string|None|False|External ID given during role creation|None|exampleexternalid|

Example input:

```
{
  "dry_run":false,
  "filters":[
    {
      "name":"ip-permission.from-port",
      "values":[
        80
      ]
    }
  ],
  "group_ids":[
    "sg-123456"
  ],
  "group_names":[
    "groupname"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|security_groups|[]security_group|False|Information about one or more security groups|

#### Revoke Security Group Egress

[EC2-VPC only] Removes one or more egress rules from a security group for EC2-VPC. See [http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|cidr_ip|string|None|False|Not supported|None|10.10.0.0/27|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response|None|True|
|from_port|integer|None|False|Not supported|None|8000|
|group_id|string|None|True|The ID of the security group|None|sg-123456|
|ip_permissions|[]ip_permission|None|False|One or more sets of IP permissions|None|["{ "from_port": 8080, "ip_protocol": "tcp", "ip_ranges" : [{ "cidr_ip": "10.20.0.0/27", "description": "Blah" }], "to_port": 8090}"]|
|ip_protocol|string|None|False|Not supported|None|UDP|
|source_security_group_name|string|None|False|Not supported|None|sourcegroup|
|source_security_group_owner_id|string|None|False|Not supported|None|ownergroup|
|to_port|integer|None|False|Not supported|None|9000|
|role_arn|string|None|False|AWS IAM role ARN to assume|None|arn:aws:iam::123456781111:role/ExampleRole|
|external_id|string|None|False|External ID given during role creation|None|exampleexternalid|

Example input:

```
{
  "cidr_ip":"10.10.0.0/27",
  "dry_run":true,
  "from_port":8000,
  "group_id":"sg-123456",
  "ip_permissions":[
    {
      "from_port":8080,
      "ip_protocol":"tcp",
      "ip_ranges":[
        {
          "cidr_ip":"10.20.0.0/27",
          "description":"Blah"
        }
      ],
      "to_port":8090
    }
  ],
  "ip_protocol":"UDP",
  "source_security_group_name":"sourcegroup",
  "source_security_group_owner_id":"ownergroup",
  "to_port":9000
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

#### Revoke Security Group Ingress

Removes one or more ingress rules from a security group. See [http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupIngress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupIngress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|cidr_ip|string|None|False|The CIDR IP address range|None|10.2.0.0/27|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response|None|True|
|from_port|integer|None|False|The start of port range for the TCP and UDP protocols, or an ICMP type number|None|8000|
|group_id|string|None|False|The ID of the security group|None|sg-123456|
|group_name|string|None|False|[EC2-Classic, default VPC] The name of the security group|None|groupname|
|ip_permissions|[]ip_permission|None|False|One or more sets of IP permissions|None|["{ "from_port": 8080, "ip_protocol": "tcp", "ip_ranges" : [{ "cidr_ip": "10.20.0.0/27", "description": "Blah" }], "to_port": 8090}"]|
|ip_protocol|string|None|False|The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers)|None|UDP|
|source_security_group_name|string|None|False|[EC2-Classic, default VPC] The name of the source security group|None|name|
|source_security_group_owner_id|string|None|False|[EC2-Classic] The AWS account ID of the source security group, if the source security group is in a different account|None|ownername|
|to_port|integer|None|False|The end of port range for the TCP and UDP protocols, or an ICMP code number|None|9000|
|role_arn|string|None|False|AWS IAM role ARN to assume|None|arn:aws:iam::123456781111:role/ExampleRole|
|external_id|string|None|False|External ID given during role creation|None|exampleexternalid|

Example input:

```
{
  "cidr_ip":"10.10.0.0/27",
  "dry_run":true,
  "from_port":8000,
  "group_id":"sg-123456",
  "ip_permissions":[
    {
      "from_port":8080,
      "ip_protocol":"tcp",
      "ip_ranges":[
        {
          "cidr_ip":"10.20.0.0/27",
          "description":"Blah"
        }
      ],
      "to_port":8090
    }
  ],
  "ip_protocol":"UDP",
  "source_security_group_name":"sourcegroup",
  "source_security_group_owner_id":"ownergroup",
  "to_port":9000
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

#### Update Security Group Rule Descriptions Egress

[EC2-VPC only] Updates the description of an egress (outbound) security group rule. See [http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsEgress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsEgress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response|None|True|
|group_id|string|None|False|The ID of the security group|None|sg-123456|
|group_name|string|None|False|[Default VPC] The name of the security group|None|groupname|
|ip_permissions|[]ip_permission|None|True|The IP permissions for the security group rule|None|["{ "from_port": 8080, "ip_protocol": "tcp", "ip_ranges" : [{ "cidr_ip": "10.20.0.0/27", "description": "Blah" }], "to_port": 8090}"]|
|role_arn|string|None|False|AWS IAM role ARN to assume|None|arn:aws:iam::123456781111:role/ExampleRole|
|external_id|string|None|False|External ID given during role creation|None|exampleexternalid|

Example input:

```
{
  "dry_run":true,
  "group_id":"sg-123456",
  "group_name":"groupname",
  "ip_permissions":[
    {
      "from_port":8080,
      "ip_protocol":"tcp",
      "ip_ranges":[
        {
          "cidr_ip":"10.20.0.0/27",
          "description":"Blah"
        }
      ],
      "to_port":8090
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|return|boolean|False|Returns true if the request succeeds; otherwise, returns an error|

#### Update Security Group Rule Descriptions Ingress

Updates the description of an ingress (inbound) security group rule. See [http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsIngress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsIngress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response|None|True|
|group_id|string|None|False|The ID of the security group|None|sg-123456|
|group_name|string|None|False|[EC2-Classic, default VPC] The name of the security group|None|groupname|
|ip_permissions|[]ip_permission|None|True|The IP permissions for the security group rule|None|["{ "from_port": 8080, "ip_protocol": "tcp", "ip_ranges" : [{ "cidr_ip": "10.20.0.0/27", "description": "Blah" }], "to_port": 8090}"]|
|role_arn|string|None|False|AWS IAM role ARN to assume|None|arn:aws:iam::123456781111:role/ExampleRole|
|external_id|string|None|False|External ID given during role creation|None|exampleexternalid|

Example input:

```
{
  "dry_run":true,
  "group_id":"sg-123456",
  "group_name":"groupname",
  "ip_ranges":[
    {
      "cidr_ip":"10.20.0.0/27",
      "description":"Blah"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|return|boolean|False|Returns true if the request succeeds; otherwise, returns an error|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.2.1 - Updated Connection and Actions to use related AWS Client in SDK
* 1.2.0 - Updated Connect and Action inputs to include Role ARN and External ID to provide support for AWS Assume Role functionality at both an Action and a Connection level
* 1.1.0 - Update plugin runtime to InsightConnect 
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.2 - SSL bug fix in SDK
* 0.1.1 - Fix connection test not passing output validation
* 0.1.0 - Initial plugin

# Links

## References

* [Documentation Overview](https://aws.amazon.com/documentation/ec2)
* [API Reference](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html)

