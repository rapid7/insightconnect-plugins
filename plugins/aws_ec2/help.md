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

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|region|string|None|True|The AWS Region to use for requests. An example would be us-east-1|None|
|aws_access_key_id|credential_secret_key|None|True|The ID of the AWS Access Key to use for authentication with AWS|None|
|aws_secret_access_key|credential_secret_key|None|True|The AWS Secret Access Key used for signing requests with the given AWS Access Key ID. Note\: Domain is not required|None|

## Technical Details

### Actions

#### Authorize Security Group Egress

[EC2-VPC only] Adds one or more egress rules to a security group for use with a VPC. See [http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupEgress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupEgress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response.|None|
|group_id|string|None|True|The ID of the security group.|None|
|ip_permissions|[]ip_permission|None|False|One or more sets of IP permissions.|None|
|cidr_ip|string|None|False|Not supported.|None|
|from_port|integer|None|False|Not supported.|None|
|ip_protocol|string|None|False|Not supported.|None|
|to_port|integer|None|False|Not supported.|None|
|source_security_group_name|string|None|False|Not supported.|None|
|source_security_group_owner_id|string|None|False|Not supported.|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

#### Authorize Security Group Ingress

Adds one or more ingress rules to a security group. See [http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cidr_ip|string|None|False|The CIDR IPv4 address range.|None|
|from_port|integer|None|False|The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number.|None|
|group_id|string|None|False|The ID of the security group.|None|
|group_name|string|None|False|[EC2-Classic, default VPC] The name of the security group.|None|
|ip_permissions|[]ip_permission|None|False|One or more sets of IP permissions.|None|
|ip_protocol|string|None|False|The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers).|None|
|source_security_group_name|string|None|False|[EC2-Classic, default VPC] The name of the source security group.|None|
|source_security_group_owner_id|string|None|False|[EC2-Classic] The AWS account ID for the source security group, if the source security group is in a different account.|None|
|to_port|integer|None|False|The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code number.|None|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response.|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

#### Describe Instances

Describes one or more of your instances. See [http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClassicLinkInstances.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeClassicLinkInstances.html)

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filters|[]filter|None|False|One or more filters.|None|
|instance_ids|[]string|None|False|One or more instance IDs.|None|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response.|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|reservations|[]reservation|False|Zero or more reservations.|

#### Describe Security Groups

Describes one or more of your security groups. See [http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html)

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filters|[]filter|None|False|One or more filters.|None|
|group_ids|[]string|None|False|One or more security group IDs.|None|
|group_names|[]string|None|False|[EC2-Classic and default VPC only] One or more security group names.|None|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response.|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|security_groups|[]security_group|False|Information about one or more security groups.|

#### Revoke Security Group Egress

[EC2-VPC only] Removes one or more egress rules from a security group for EC2-VPC. See [http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response.|None|
|group_id|string|None|True|The ID of the security group.|None|
|ip_permissions|[]ip_permission|None|False|One or more sets of IP permissions.|None|
|cidr_ip|string|None|False|Not supported.|None|
|from_port|integer|None|False|Not supported.|None|
|ip_protocol|string|None|False|Not supported.|None|
|to_port|integer|None|False|Not supported.|None|
|source_security_group_name|string|None|False|Not supported.|None|
|source_security_group_owner_id|string|None|False|Not supported.|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

#### Revoke Security Group Ingress

Removes one or more ingress rules from a security group. See [http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupIngress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupIngress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cidr_ip|string|None|False|The CIDR IP address range.|None|
|from_port|integer|None|False|The start of port range for the TCP and UDP protocols, or an ICMP type number.|None|
|group_id|string|None|False|The ID of the security group.|None|
|group_name|string|None|False|[EC2-Classic, default VPC] The name of the security group.|None|
|ip_permissions|[]ip_permission|None|False|One or more sets of IP permissions.|None|
|ip_protocol|string|None|False|The IP protocol name (tcp, udp, icmp) or number (see Protocol Numbers).|None|
|source_security_group_name|string|None|False|[EC2-Classic, default VPC] The name of the source security group.|None|
|source_security_group_owner_id|string|None|False|[EC2-Classic] The AWS account ID of the source security group, if the source security group is in a different account.|None|
|to_port|integer|None|False|The end of port range for the TCP and UDP protocols, or an ICMP code number.|None|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response.|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|

#### Update Security Group Rule Descriptions Egress

[EC2-VPC only] Updates the description of an egress (outbound) security group rule. See [http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsEgress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsEgress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response.|None|
|group_id|string|None|False|The ID of the security group.|None|
|group_name|string|None|False|[Default VPC] The name of the security group.|None|
|ip_permissions|[]ip_permission|None|True|The IP permissions for the security group rule.|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|return|boolean|False|Returns true if the request succeeds; otherwise, returns an error.|

#### Update Security Group Rule Descriptions Ingress

Updates the description of an ingress (inbound) security group rule. See [http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsIngress.html](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UpdateSecurityGroupRuleDescriptionsIngress.html)

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|dry_run|boolean|None|False|Checks whether you have the required permissions for the action, without actually making the request, and provides an error response.|None|
|group_id|string|None|False|The ID of the security group.|None|
|group_name|string|None|False|[EC2-Classic, default VPC] The name of the security group.|None|
|ip_permissions|[]ip_permission|None|True|The IP permissions for the security group rule.|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response_metadata|response_metadata|True|Metadata about the response from AWS|
|return|boolean|False|Returns true if the request succeeds; otherwise, returns an error.|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.2 - SSL bug fix in SDK
* 0.1.1 - Fix connection test not passing output validation
* 0.1.0 - Initial plugin

# Links

## References

* [Documentation Overview](https://aws.amazon.com/documentation/ec2)
* [API Reference](http://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html)

