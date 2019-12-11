# Description

[AWS Security Hub](https://aws.amazon.com/security-hub/) is a comprehensive view of your high-priority security alerts and compliance status across AWS accounts.
The AWS Security Hub InsightConnect plugin allows you to list and describe security hub-aggregated findings and retrieve SQS messages.

This plugin utilizes the [AWS Security Hub API](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Operations.html) and [Boto3](https://github.com/boto/boto3) Python library.

# Key Features

* Lists and describes Security Hub-aggregated findings
* Get SQS messages

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
|AttributeNames|[]string|['All']|False|A list of attributes that need to be returned along with each message ['All','Policy','VisibilityTimeout','MaximumMessageSize','MessageRetentionPeriod','ApproximateNumberOfMessages','ApproximateNumberOfMessagesNotVisible','CreatedTimestamp','LastModifiedTimestamp','QueueArn','ApproximateNumberOfMessagesDelayed','DelaySeconds','ReceiveMessageWaitTimeSeconds','RedrivePolicy','FifoQueue','ContentBasedDeduplication','KmsMasterKeyId','KmsDataKeyReusePeriodSeconds']|None|
|MaxNumberOfMessages|integer|1|False|The maximum number of messages to return. Amazon SQS never returns more messages than this value. Valid values 1 to 10. Default 1|None|
|MessageAttributeNames|[]string|['All']|False|The name of the message attribute|None|
|ReceiveRequestAttemptId|string||False|This parameter applies only to FIFO (first-in-first-out) queues|None|
|VisibilityTimeout|integer|0|False|The duration (in seconds) that the received messages are hidden from subsequent retrieve requests after being retrieved by a ReceiveMessage request|None|
|WaitTimeSeconds|integer|0|False|The duration (in seconds) for which the call waits for a message to arrive in the queue before returning. If a message is available, the call returns sooner than WaitTimeSeconds|None|
|interval|integer|5|True|How many seconds to wait until next poll|None|
|queue_url|string|None|True|URL for the SQS queue|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Message|Message|False|Message|
|ResponseMetadata|ResponseMetadata|False|Response metadata|
|securityhubevent|securityHubPayload|False|Security Hub Event|

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

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.0 - Plugin spec update
* 1.0.1 - New spec and help.md format for the Hub | Variable names updated as acronyms
* 1.0.0 - Initial plugin

# Links

## References

* [AWS Security Hub](https://aws.amazon.com/security-hub/)
* [AWS Security Hub API](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Operations.html)
* [Boto3](https://github.com/boto/boto3)

