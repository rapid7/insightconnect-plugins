# Description

[AWS Security Hub](https://aws.amazon.com/security-hub/) is a comprehensive view of your high-priority security alerts and compliance status across AWS accounts.

This plugin utilizes the [AWS Security Hub API](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Operations.html) and [Boto3](https://github.com/boto/boto3) Python library.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|aws_access_key_id|credential_secret_key|None|True|The ID of the AWS Access Key to use for authentication with AWS|None|
|aws_secret_access_key|credential_secret_key|None|True|The AWS Secret Access Key used for signing requests with the given AWS Access Key ID|None|
|region|string|None|False|AWS Region. This is not required|['us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ca-central-1', 'ap-south-1', 'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'sa-east-1']|

## Technical Details

### Actions

#### Get Findings

This action is used to lists and describes Security Hub-aggregated findings that are specified by filter attributes.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filters|object|None|False|An object of filters|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Findings|[]Findings|False|Findings|
|NextToken|string|False|Next token|

Example output:

```
{
  "Findings": [
    {
      "SchemaVersion": "2018-10-08",
      "Id": "arn:aws:securityhub:us-east-2:000000000000:subscription/cis-aws-foundations-benchmark/v/1.2.0/1.2/finding/0000000-0000-0000-0000-0000000000000",
      "ProductArn": "arn:aws:securityhub:us-east-2::product/aws/securityhub",
      "GeneratorId": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.2",
      "AwsAccountId": "000000000000",
      "Types": [
        "Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark"
      ],
      "FirstObservedAt": "2019-05-14T05:20:43.691Z",
      "LastObservedAt": "2019-05-30T17:32:00.372Z",
      "CreatedAt": "2019-05-14T05:20:43.691Z",
      "UpdatedAt": "2019-05-30T17:32:00.372Z",
      "Severity": {
        "Product": 2,
        "Normalized": 20
      },
      "Title": "1.2 Ensure multi-factor authentication (MFA) is enabled for all IAM users that have a console password",
      "Description": "Multi-Factor Authentication (MFA) adds an extra layer of protection on top of a user name and password. It is recommended that MFA be enabled for all accounts that have a console password.",
      "Remediation": {
        "Recommendation": {
          "Text": "For directions on how to fix this issue, please consult the AWS Security Hub CIS documentation.",
          "Url": "https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html#securityhub-standards-checks-1.2"
        }
      },
      "ProductFields": {
        "StandardsGuideArn": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0",
        "StandardsGuideSubscriptionArn": "arn:aws:securityhub:us-east-2:000000000000:subscription/cis-aws-foundations-benchmark/v/1.2.0",
        "RuleId": "1.2",
        "RecommendationUrl": "https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html#securityhub-standards-checks-1.2",
        "RelatedAWSResources:0/name": "securityhub-mfa-enabled-for-iam-console-access-000000",
        "RelatedAWSResources:0/type": "AWS::Config::ConfigRule",
        "RecordState": "ACTIVE",
        "aws/securityhub/FindingId": "arn:aws:securityhub:us-east-2::product/aws/securityhub/arn:aws:securityhub:us-east-2:000000000000:subscription/cis-aws-foundations-benchmark/v/1.2.0/1.2/finding/0000000-0000-0000-0000-000000000",
        "aws/securityhub/SeverityLabel": "LOW",
        "aws/securityhub/ProductName": "Security Hub",
        "aws/securityhub/CompanyName": "AWS"
      },
      "Resources": [
        {
          "Type": "AwsAccount",
          "Id": "AWS::::Account:0000000000",
          "Partition": "aws",
          "Region": "us-east-2"
        }
      ],
      "Compliance": {
        "Status": "FAILED"
      },
      "WorkflowState": "NEW",
      "RecordState": "ACTIVE"
    }
  ]
}
```

### Triggers

#### Get SQS Message

This trigger is used to poll from a SQS Queue.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|AttributeNames|[]string|['All']|False|A list of s that need to be returned along with each message|None|
|MaxNumberOfMessages|integer|1|False|The maximum number of messages to return. Amazon SQS never returns more messages than this value. Valid values 1 to 10. Default 1|None|
|MessageAttributeNames|[]string|['All']|False|The name of the message attribute|None|
|ReceiveRequestAttemptId|string||False|This parameter applies only to FIFO (first-in-first-out) queues|None|
|VisibilityTimeout|integer|0|False|The duration (in seconds) that the received messages are hidden from subsequent retrieve requests after being retrieved by a ReceiveMessage request|None|
|WaitTimeSeconds|integer|0|False|he duration (in seconds) for which the call waits for a message to arrive in the queue before returning. If a message is available, the call returns sooner than WaitTimeSeconds|None|
|interval|integer|5|True|How many seconds to wait till next poll|None|
|queue_url|string|None|True|URL for the SQS queue|None|

Additional Configuration Information:
  To enable long-poll support for the SQS Feed increase `WaitTimeSeconds`.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Message|Message|False|Message|
|ResponseMetadata|ResponseMetadata|False|Response metadata|

Example output:

```
{
  "Message": {
    "MessageId": "3bd3134a-379f-4bbc-953b-ea631537bd75",
    "ReceiptHandle": "AQEBRCB5IzduYADYYhtUnV8sJ08nqTGSi1P6KiFoIhXRDIWZC6rjZGM/f5+Mvh0AnO2xJsc5559dQupnHZLJTPcnjFygYN5vbgOVx9G2cfcO4iFE9c53/31jPd8+KpsJRL9DVjRb4cRX6d84G+kstBXmZuDc684zS2I93jsjWFkvId26ReHzbQ6+iRMM7m0h2W5er+KymAkLhhdPCrWYbMreoI35HALUYbSFZV8vd+srwKNPJ59l+DMme3nHAzFGKvQoyJqSWp6uk2ywIvbHISzYWqKk7cBsnnROsIhiF9umsWgBM+T/lm5HHeRIfsa6T4vzEyI4FepeZmrk2Tz8g7z4k+GHJr1wF8AxOxQR+VUfa2ycM3wvpUgKsaAtekDRhO3LJQVuyp/Ll6m9vzf+QAIcKg==",
    "MD5OfBody": "bbdc5fdb8be7251f5c910905db994bab",
    "Body": "Information about current NY Times fiction bestseller for week of 12/11/2016.",
    "Attributes": {
      "SenderId": "AIDAZTUUAVRPYOR5E7A5W",
      "ApproximateFirstReceiveTimestamp": "1559246912467",
      "ApproximateReceiveCount": "1",
      "SentTimestamp": "1559246899951"
    },
    "MD5OfMessageAttributes": "d25a6aea97eb8f585bfa92d314504a92",
    "MessageAttributes": {
      "Author": {
        "StringValue": "John Grisham",
        "DataType": "String"
      },
      "Title": {
        "StringValue": "The Whistler",
        "DataType": "String"
      },
      "WeeksOn": {
        "StringValue": "6",
        "DataType": "Number"
      }
    }
  },
  "ResponseMetadata": {
    "RequestId": "c52dccd3-9d9c-5f34-9e74-99b9a71cc3e9",
    "HTTPStatusCode": 200,
    "HTTPHeaders": {
      "x-amzn-requestid": "c52dccd3-9d9c-5f34-9e74-99b9a71cc3e9",
      "date": "Thu, 30 May 2019 20:08:32 GMT",
      "content-type": "text/xml",
      "content-length": "1737"
    },
    "RetryAttempts": 0
  }
}
```

### Custom Output Types

#### Compliance

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Status|string|False|Status|

#### Malware

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Name|string|False|Name|
|Path|string|False|Path|
|State|string|False|State|
|Type|string|False|Type|

#### Network

|Name|Type|Required|Description|
|----|----|--------|-----------|
|DestinationDomain|string|False|Destination domain|
|DestinationIpV4|string|False|Destination IPv4|
|DestinationIpV6|string|False|Destination IPv6|
|DestinationPort|integer|False|Destination port|
|Direction|string|False|Direction|
|Protocol|string|False|Protocol|
|SourceDomain|string|False|Source domain|
|SourceIpV4|string|False|Source IPv4|
|SourceIpV6|string|False|Source IPv6|
|SourceMac|string|False|Source MAC|
|SourcePort|integer|False|Source port|

#### Note

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Text|string|False|Text|
|UpdatedAt|string|False|Updated At|
|UpdatedBy|string|False|Updated by|

#### Process

|Name|Type|Required|Description|
|----|----|--------|-----------|
|LaunchedAt|string|False|Launched at|
|Name|string|False|Name|
|ParentPid|integer|False|Parent PID|
|Path|string|False|Path|
|Pid|integer|False|PID|
|TerminatedAt|string|False|Terminated at|

#### ProductFields

|Name|Type|Required|Description|
|----|----|--------|-----------|
|string|string|False|String|

#### RelatedFindings

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Id|string|False|ID|
|ProductArn|string|False|Product ARN|

#### Recommendation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Text|string|False|Text|
|Url|string|False|URL|

#### Remediation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Recommendation|Recommendation|False|Recommendation|

#### AwsEc2Instance

|Name|Type|Required|Description|
|----|----|--------|-----------|
|IamInstanceProfileArn|string|False|IAM instance profile ARN|
|ImageId|string|False|Image ID|
|IpV4Addresses|[]string|False|IPv4 addresses|
|IpV6Addresses|[]string|False|IPv6 addresses|
|KeyName|string|False|Keyname|
|LaunchedAt|string|False|Launched at|
|SubnetId|string|False|Subnet ID|
|Type|string|False|Type|
|VpcId|string|False|VPC ID|

#### AwsIamAccessKey

|Name|Type|Required|Description|
|----|----|--------|-----------|
|CreatedAt|string|False|Created at|
|Status|string|False|Status|
|UserName|string|False|Username|

#### AwsS3Bucket

|Name|Type|Required|Description|
|----|----|--------|-----------|
|OwnerId|string|False|Owner ID|
|OwnerName|string|False|Owner name|

#### Container

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ImageId|string|False|Image ID|
|ImageName|string|False|Image name|
|LaunchedAt|string|False|Launched at|
|Name|string|False|Name|

#### Details

|Name|Type|Required|Description|
|----|----|--------|-----------|
|AwsEc2Instance|AwsEc2Instance|False|AWS EC2 instance|
|AwsIamAccessKey|AwsIamAccessKey|False|AWS IAM access key|
|AwsS3Bucket|AwsS3Bucket|False|AWS S3 bucket|
|Container|Container|False|Container|
|Other|ProductFields|False|Other|

#### Resources

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Details|Details|False|Details|
|Id|string|False|ID|
|Partition|string|False|Partition|
|Region|string|False|Region|
|Tags|ProductFields|False|Tags|
|Type|string|False|Type|

#### Severity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Normalized|integer|False|Normalized|
|Product|integer|False|Product|

#### ThreatIntelIndicators

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Category|string|False|Category|
|LastObservedAt|string|False|Last observed at|
|Source|string|False|Source|
|SourceUrl|string|False|Source URL|
|Type|string|False|Type|
|Value|string|False|Value|

#### Findings

|Name|Type|Required|Description|
|----|----|--------|-----------|
|AwsAccountId|string|False|AWS account ID|
|Compliance|Compliance|False|Compliance|
|Confidence|integer|False|Confidence|
|CreatedAt|string|False|Created at|
|Criticality|integer|False|Criticality|
|Description|string|False|Description|
|FirstObservedAt|string|False|First observed at|
|GeneratorId|string|False|Generator ID|
|Id|string|False|ID|
|LastObservedAt|string|False|Last observed at|
|Malware|[]Malware|False|Malware|
|Network|Network|False|Network|
|Note|Note|False|Note|
|Process|Process|False|Process|
|ProductArn|string|False|Product ARN|
|ProductFields|ProductFields|False|Product fields|
|RecordState|string|False|Record state|
|RelatedFindings|[]RelatedFindings|False|Related findings|
|Remediation|Remediation|False|Remediation|
|Resources|[]Resources|False|Resources|
|SchemaVersion|string|False|Schema version|
|Severity|Severity|False|Severity|
|SourceUrl|string|False|Source URL|
|ThreatIntelIndicators|[]ThreatIntelIndicators|False|Threat intel indicators|
|Title|string|False|Title|
|Types|[]string|False|Types|
|UpdatedAt|string|False|Updated at|
|UserDefinedFields|ProductFields|False|User-defined fields|
|VerificationState|string|False|Verification state|
|WorkflowState|string|False|Workflow state|

#### Attributes

|Name|Type|Required|Description|
|----|----|--------|-----------|
|SentTimestamp|string|False|Sent timestamp|

#### Author

|Name|Type|Required|Description|
|----|----|--------|-----------|
|DataType|string|False|Data type|
|StringValue|string|False|String value|

#### MessageAttributes

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Author|Author|False|Author|
|Title|Author|False|Title|
|WeeksOn|Author|False|Weeks on|

#### Message

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Attributes|Attributes|False|Attributes|
|Body|string|False|Body|
|MD5OfBody|string|False|MD5 of body|
|MD5OfMessageAttributes|string|False|MD5 of message attributes|
|MessageAttributes|MessageAttributes|False|Message attributes|
|MessageId|string|False|Message ID|
|ReceiptHandle|string|False|Receipt handle|

#### HTTPHeaders

|Name|Type|Required|Description|
|----|----|--------|-----------|
|content-length|string|False|Content length|
|content-type|string|False|Content type|
|date|string|False|Date|
|x-amzn-requestid|string|False|X-amzn-requestid|

#### ResponseMetadata

|Name|Type|Required|Description|
|----|----|--------|-----------|
|HTTPHeaders|HTTPHeaders|False|HTTP headers|
|HTTPStatusCode|integer|False|HTTP status code|
|RequestId|string|False|Request ID|
|RetryAttempts|integer|False|Retry attempts|

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [AWS Security Hub](https://aws.amazon.com/security-hub/)
* [AWS Security Hub API](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Operations.html)
* [Boto3](https://github.com/boto/boto3)

