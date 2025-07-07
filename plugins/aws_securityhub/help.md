# Description

[AWS Security Hub](https://aws.amazon.com/security-hub/) is a comprehensive view of your high-priority security alerts and compliance status across AWS accounts.

The AWS Security Hub InsightConnect plugin allows you to list and describe security hub-aggregated findings and retrieve SQS messages.

This plugin utilizes the [AWS Security Hub API](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Operations.html) and [Boto3](https://github.com/boto/boto3) Python library

# Key Features

* Lists and describes Security Hub-aggregated findings
* Get SQS messages

# Requirements

* AWS account
* AWS access key ID for authentication
* AWS secret key for signing requests with the given AWS access key ID
* AWS region to use for requests

# Supported Product Versions

* 2024-10-31

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|aws_access_key_id|credential_secret_key|None|True|The ID of the AWS Access Key to use for authentication with AWS|None|PSIETEWUYWWB776HFG|None|None|
|aws_secret_access_key|credential_secret_key|None|True|The AWS Secret Access Key used for signing requests with the given AWS Access Key ID|None|WwwivfnwvwjsNN229933ksERE8|None|None|
|region|string|None|False|AWS Region. This is not required|["us-east-2", "us-east-1", "us-west-1", "us-west-2", "ca-central-1", "ap-south-1", "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-northeast-1", "eu-central-1", "eu-west-1", "eu-west-2", "sa-east-1"]|us-east-2|None|None|

Example input:

```
{
  "aws_access_key_id": "PSIETEWUYWWB776HFG",
  "aws_secret_access_key": "WwwivfnwvwjsNN229933ksERE8",
  "region": "us-east-2"
}
```

## Technical Details

### Actions


#### Get Findings

This action is used to lists and describes Security Hub-aggregated findings that are specified by filter attributes

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filters|object|None|False|An object of filters|None|{}|None|None|
  
Example input:

```
{
  "filters": {}
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|Findings|[]Findings|False|Security Hub-aggregated findings|[{"SchemaVersion": "2018-10-08", "Id": "arn:aws:securityhub:us-east-2:000000000000:subscription/cis-aws-foundations-benchmark/v/1.2.0/1.2/finding/0000000-0000-0000-0000-0000000000000", "ProductArn": "arn:aws:securityhub:us-east-2::product/aws/securityhub", "GeneratorId": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.2", "AwsAccountId": "000000000000", "Types": ["Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark"], "FirstObservedAt": "2019-05-14T05:20:43.691Z", "LastObservedAt": "2019-05-30T17:32:00.372Z", "CreatedAt": "2019-05-14T05:20:43.691Z", "UpdatedAt": "2019-05-30T17:32:00.372Z", "Severity": {"Product": 2, "Normalized": 20}, "Title": "1.2 Ensure multi-factor authentication (MFA) is enabled for all IAM users that have a console password", "Description": "Multi-Factor Authentication (MFA) adds an extra layer of protection on top of a user name and password. It is recommended that MFA be enabled for all accounts that have a console password.", "Remediation": {"Recommendation": {"Text": "For directions on how to fix this issue, please consult the AWS Security Hub CIS documentation.", "Url": "https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html#securityhub-standards-checks-1.2"}}, "ProductFields": {"StandardsGuideArn": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0", "StandardsGuideSubscriptionArn": "arn:aws:securityhub:us-east-2:000000000000:subscription/cis-aws-foundations-benchmark/v/1.2.0", "RuleId": "1.2", "RecommendationUrl": "https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html#securityhub-standards-checks-1.2", "RelatedAWSResources:0/name": "securityhub-mfa-enabled-for-iam-console-access-000000", "RelatedAWSResources:0/type": "AWS::Config::ConfigRule", "RecordState": "ACTIVE", "aws/securityhub/FindingId": "arn:aws:securityhub:us-east-2::product/aws/securityhub/arn:aws:securityhub:us-east-2:000000000000:subscription/cis-aws-foundations-benchmark/v/1.2.0/1.2/finding/0000000-0000-0000-0000-000000000", "aws/securityhub/SeverityLabel": "LOW", "aws/securityhub/ProductName": "Security Hub", "aws/securityhub/CompanyName": "AWS"}, "Resources": [{"Type": "AwsAccount", "Id": "AWS::::Account:0000000000", "Partition": "aws", "Region": "us-east-2"}], "Compliance": {"Status": "FAILED"}, "WorkflowState": "NEW", "RecordState": "ACTIVE"}]|
  
Example output:

```
{
  "Findings": [
    {
      "AwsAccountId": "000000000000",
      "Compliance": {
        "Status": "FAILED"
      },
      "CreatedAt": "2019-05-14T05:20:43.691Z",
      "Description": "Multi-Factor Authentication (MFA) adds an extra layer of protection on top of a user name and password. It is recommended that MFA be enabled for all accounts that have a console password.",
      "FirstObservedAt": "2019-05-14T05:20:43.691Z",
      "GeneratorId": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.2",
      "Id": "arn:aws:securityhub:us-east-2:000000000000:subscription/cis-aws-foundations-benchmark/v/1.2.0/1.2/finding/0000000-0000-0000-0000-0000000000000",
      "LastObservedAt": "2019-05-30T17:32:00.372Z",
      "ProductArn": "arn:aws:securityhub:us-east-2::product/aws/securityhub",
      "ProductFields": {
        "RecommendationUrl": "https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html#securityhub-standards-checks-1.2",
        "RecordState": "ACTIVE",
        "RelatedAWSResources:0/name": "securityhub-mfa-enabled-for-iam-console-access-000000",
        "RelatedAWSResources:0/type": "AWS::Config::ConfigRule",
        "RuleId": "1.2",
        "StandardsGuideArn": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0",
        "StandardsGuideSubscriptionArn": "arn:aws:securityhub:us-east-2:000000000000:subscription/cis-aws-foundations-benchmark/v/1.2.0",
        "aws/securityhub/CompanyName": "AWS",
        "aws/securityhub/FindingId": "arn:aws:securityhub:us-east-2::product/aws/securityhub/arn:aws:securityhub:us-east-2:000000000000:subscription/cis-aws-foundations-benchmark/v/1.2.0/1.2/finding/0000000-0000-0000-0000-000000000",
        "aws/securityhub/ProductName": "Security Hub",
        "aws/securityhub/SeverityLabel": "LOW"
      },
      "RecordState": "ACTIVE",
      "Remediation": {
        "Recommendation": {
          "Text": "For directions on how to fix this issue, please consult the AWS Security Hub CIS documentation.",
          "Url": "https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html#securityhub-standards-checks-1.2"
        }
      },
      "Resources": [
        {
          "Id": "AWS::::Account:0000000000",
          "Partition": "aws",
          "Region": "us-east-2",
          "Type": "AwsAccount"
        }
      ],
      "SchemaVersion": "2018-10-08",
      "Severity": {
        "Normalized": 20,
        "Product": 2
      },
      "Title": "1.2 Ensure multi-factor authentication (MFA) is enabled for all IAM users that have a console password",
      "Types": [
        "Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark"
      ],
      "UpdatedAt": "2019-05-30T17:32:00.372Z",
      "WorkflowState": "NEW"
    }
  ]
}
```
### Triggers


#### Get SQS Message

This trigger is used to poll from an SQS Queue

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|AttributeNames|[]string|["All"]|False|A list of attributes that need to be returned along with each message ['All', 'Policy', 'VisibilityTimeout', 'MaximumMessageSize', 'MessageRetentionPeriod', 'ApproximateNumberOfMessages', 'ApproximateNumberOfMessagesNotVisible', 'CreatedTimestamp', 'LastModifiedTimestamp', 'QueueArn', 'ApproximateNumberOfMessagesDelayed', 'DelaySeconds', 'ReceiveMessageWaitTimeSeconds', 'RedrivePolicy', 'FifoQueue', 'ContentBasedDeduplication', 'KmsMasterKeyId', 'KmsDataKeyReusePeriodSeconds']|None|All|None|None|
|MaxNumberOfMessages|integer|1|False|The maximum number of messages to return. Amazon SQS never returns more messages than this value. Valid values 1 to 10. Default 1|None|1|None|None|
|MessageAttributeNames|[]string|["All"]|False|The name of the message attribute|None|All|None|None|
|ReceiveRequestAttemptId|string||False|This parameter applies only to FIFO (first-in-first-out) queues|None|b57d1e3f-0a3f-4b67-9bb9-3a6d5f9b4f8c|None|None|
|VisibilityTimeout|integer|0|False|The duration (in seconds) that the received messages are hidden from subsequent retrieve requests after being retrieved by a ReceiveMessage request|None|0|None|None|
|WaitTimeSeconds|integer|0|False|The duration (in seconds) for which the call waits for a message to arrive in the queue before returning. If a message is available, the call returns sooner than WaitTimeSeconds|None|0|None|None|
|interval|integer|5|True|How many seconds to wait until next poll|None|5|None|None|
|queue_url|string|None|True|URL for the SQS queue|None|https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue|None|None|
  
Example input:

```
{
  "AttributeNames": [
    "All"
  ],
  "MaxNumberOfMessages": 1,
  "MessageAttributeNames": [
    "All"
  ],
  "ReceiveRequestAttemptId": "",
  "VisibilityTimeout": 0,
  "WaitTimeSeconds": 0,
  "interval": 5,
  "queue_url": "https://sqs.us-east-1.amazonaws.com/177715257436/MyQueue"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|Message|Message|False|Security Hub message|{'MessageId': '3bd3134a-379f-4bbc-953b-ea631537bd75', 'ReceiptHandle': 'AQEBRCB5IzduYADYYhtUnV8sJ08nqTGSi1P6KiFoIhXRDIWZC6rjZGM/f5+Mvh0AnO2xJsc5559dQupnHZLJTPcnjFygYN5vbgOVx9G2cfcO4iFE9c53/31jPd8+KpsJRL9DVjRb4cRX6d84G+kstBXmZuDc684zS2I93jsjWFkvId26ReHzbQ6+iRMM7m0h2W5er+KymAkLhhdPCrWYbMreoI35HALUYbSFZV8vd+srwKNPJ59l+DMme3nHAzFGKvQoyJqSWp6uk2ywIvbHISzYWqKk7cBsnnROsIhiF9umsWgBM+T/lm5HHeRIfsa6T4vzEyI4FepeZmrk2Tz8g7z4k+GHJr1wF8AxOxQR+VUfa2ycM3wvpUgKsaAtekDRhO3LJQVuyp/Ll6m9vzf+QAIcKg==', 'MD5OfBody': 'bbdc5fdb8be7251f5c910905db994bab', 'Body': 'Information about current NY Times fiction bestseller for week of 12/11/2016.', 'Attributes': {'SenderId': 'AIDAZTUUAVRPYOR5E7A5W', 'ApproximateFirstReceiveTimestamp': '1559246912467', 'ApproximateReceiveCount': '1', 'SentTimestamp': '1559246899951'}, 'MD5OfMessageAttributes': 'd25a6aea97eb8f585bfa92d314504a92', 'MessageAttributes': {'Author': {'StringValue': 'John Grisham', 'DataType': 'String'}, 'Title': {'StringValue': 'The Whistler', 'DataType': 'String'}, 'WeeksOn': {'StringValue': '6', 'DataType': 'Number'}}}|
|ResponseMetadata|ResponseMetadata|False|Security Hub response metadata|{'RequestId': 'c52dccd3-9d9c-5f34-9e74-99b9a71cc3e9', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': 'c52dccd3-9d9c-5f34-9e74-99b9a71cc3e9', 'date': 'Thu, 30 May 2019 20:08:32 GMT', 'content-type': 'text/xml', 'content-length': '1737'}, 'RetryAttempts': 0}|
|securityhubevent|securityHubPayload|False|Security Hub event payload|{'securityhubevent': {'version': '0', 'id': 'abcd1234-5678-90ef-abcd-1234567890ef', 'detail-type': 'Security Hub Findings - Imported', 'source': 'aws.securityhub', 'account': '123456789012', 'time': '2025-07-04T12:34:56Z', 'region': 'us-east-1', 'resources': ['arn:aws:securityhub:us-east-1::product/aws/securityhub'], 'detail': {'findings': [{'SchemaVersion': '2018-10-08', 'Id': 'arn:aws:securityhub:us-east-1:123456789012:finding/abc12345', 'ProductArn': 'arn:aws:securityhub:us-east-1::product/aws/securityhub', 'AwsAccountId': '123456789012', 'Types': ['Software and Configuration Checks/AWS Security Best Practices'], 'FirstObservedAt': '2025-07-04T12:00:00Z', 'LastObservedAt': '2025-07-04T12:34:00Z', 'CreatedAt': '2025-07-04T12:34:56Z', 'UpdatedAt': '2025-07-04T12:35:00Z', 'Severity': {'Product': 8, 'Normalized': 80, 'Label': 'HIGH'}, 'Title': 'IAM user has active access keys not rotated for 90 days', 'Description': "The IAM user 'jane.doe' has access keys that have not been rotated in 90 days.", 'Remediation': {'Recommendation': {'Text': 'Rotate the access keys for the IAM user regularly.', 'Url': 'https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html'}}, 'ProductFields': {'aws/securityhub/FindingId': 'abc12345', 'aws/securityhub/CompanyName': 'AWS', 'aws/securityhub/ProductName': 'Security Hub', 'aws/securityhub/SeverityLabel': 'HIGH'}, 'Resources': [{'Type': 'AwsIamUser', 'Id': 'arn:aws:iam::123456789012:user/jane.doe', 'Partition': 'aws', 'Region': 'us-east-1'}], 'Compliance': {'Status': 'FAILED'}, 'WorkflowState': 'NEW', 'RecordState': 'ACTIVE'}]}}}|
  
Example output:

```
{
  "Message": {
    "Attributes": {
      "ApproximateFirstReceiveTimestamp": "1559246912467",
      "ApproximateReceiveCount": "1",
      "SenderId": "AIDAZTUUAVRPYOR5E7A5W",
      "SentTimestamp": "1559246899951"
    },
    "Body": "Information about current NY Times fiction bestseller for week of 12/11/2016.",
    "MD5OfBody": "bbdc5fdb8be7251f5c910905db994bab",
    "MD5OfMessageAttributes": "d25a6aea97eb8f585bfa92d314504a92",
    "MessageAttributes": {
      "Author": {
        "DataType": "String",
        "StringValue": "John Grisham"
      },
      "Title": {
        "DataType": "String",
        "StringValue": "The Whistler"
      },
      "WeeksOn": {
        "DataType": "Number",
        "StringValue": "6"
      }
    },
    "MessageId": "3bd3134a-379f-4bbc-953b-ea631537bd75",
    "ReceiptHandle": "AQEBRCB5IzduYADYYhtUnV8sJ08nqTGSi1P6KiFoIhXRDIWZC6rjZGM/f5+Mvh0AnO2xJsc5559dQupnHZLJTPcnjFygYN5vbgOVx9G2cfcO4iFE9c53/31jPd8+KpsJRL9DVjRb4cRX6d84G+kstBXmZuDc684zS2I93jsjWFkvId26ReHzbQ6+iRMM7m0h2W5er+KymAkLhhdPCrWYbMreoI35HALUYbSFZV8vd+srwKNPJ59l+DMme3nHAzFGKvQoyJqSWp6uk2ywIvbHISzYWqKk7cBsnnROsIhiF9umsWgBM+T/lm5HHeRIfsa6T4vzEyI4FepeZmrk2Tz8g7z4k+GHJr1wF8AxOxQR+VUfa2ycM3wvpUgKsaAtekDRhO3LJQVuyp/Ll6m9vzf+QAIcKg=="
  },
  "ResponseMetadata": {
    "HTTPHeaders": {
      "content-length": "1737",
      "content-type": "text/xml",
      "date": "Thu, 30 May 2019 20:08:32 GMT",
      "x-amzn-requestid": "c52dccd3-9d9c-5f34-9e74-99b9a71cc3e9"
    },
    "HTTPStatusCode": 200,
    "RequestId": "c52dccd3-9d9c-5f34-9e74-99b9a71cc3e9",
    "RetryAttempts": 0
  },
  "securityhubevent": {
    "securityhubevent": {
      "account": "123456789012",
      "detail": {
        "findings": [
          {
            "AwsAccountId": "123456789012",
            "Compliance": {
              "Status": "FAILED"
            },
            "CreatedAt": "2025-07-04T12:34:56Z",
            "Description": "The IAM user 'jane.doe' has access keys that have not been rotated in 90 days.",
            "FirstObservedAt": "2025-07-04T12:00:00Z",
            "Id": "arn:aws:securityhub:us-east-1:123456789012:finding/abc12345",
            "LastObservedAt": "2025-07-04T12:34:00Z",
            "ProductArn": "arn:aws:securityhub:us-east-1::product/aws/securityhub",
            "ProductFields": {
              "aws/securityhub/CompanyName": "AWS",
              "aws/securityhub/FindingId": "abc12345",
              "aws/securityhub/ProductName": "Security Hub",
              "aws/securityhub/SeverityLabel": "HIGH"
            },
            "RecordState": "ACTIVE",
            "Remediation": {
              "Recommendation": {
                "Text": "Rotate the access keys for the IAM user regularly.",
                "Url": "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html"
              }
            },
            "Resources": [
              {
                "Id": "arn:aws:iam::123456789012:user/jane.doe",
                "Partition": "aws",
                "Region": "us-east-1",
                "Type": "AwsIamUser"
              }
            ],
            "SchemaVersion": "2018-10-08",
            "Severity": {
              "Label": "HIGH",
              "Normalized": 80,
              "Product": 8
            },
            "Title": "IAM user has active access keys not rotated for 90 days",
            "Types": [
              "Software and Configuration Checks/AWS Security Best Practices"
            ],
            "UpdatedAt": "2025-07-04T12:35:00Z",
            "WorkflowState": "NEW"
          }
        ]
      },
      "detail-type": "Security Hub Findings - Imported",
      "id": "abcd1234-5678-90ef-abcd-1234567890ef",
      "region": "us-east-1",
      "resources": [
        "arn:aws:securityhub:us-east-1::product/aws/securityhub"
      ],
      "source": "aws.securityhub",
      "time": "2025-07-04T12:34:56Z",
      "version": "0"
    }
  }
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**Compliance**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Status|string|None|False|Status|None|
  
**Malware**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Name|None|
|Path|string|None|False|Path|None|
|State|string|None|False|State|None|
|Type|string|None|False|Type|None|
  
**Network**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Destination Domain|string|None|False|Destination domain|None|
|Destination IPv4|string|None|False|Destination IPv4|None|
|Destination IPv6|string|None|False|Destination IPv6|None|
|Destination Port|integer|None|False|Destination port|None|
|Direction|string|None|False|Direction|None|
|Protocol|string|None|False|Protocol|None|
|Source Domain|string|None|False|Source domain|None|
|Source IPv4|string|None|False|Source IPv4|None|
|Source IPv6|string|None|False|Source IPv6|None|
|Source MAC|string|None|False|Source MAC|None|
|Source Port|integer|None|False|Source port|None|
  
**Note**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Text|string|None|False|Text|None|
|Updated At|string|None|False|Updated At|None|
|Updated By|string|None|False|Updated by|None|
  
**Process**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Launched At|string|None|False|Launched at|None|
|Name|string|None|False|Name|None|
|Parent PID|integer|None|False|Parent PID|None|
|Path|string|None|False|Path|None|
|PID|integer|None|False|PID|None|
|Terminated At|string|None|False|Terminated at|None|
  
**ProductFields**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|String|string|None|False|String|None|
  
**RelatedFindings**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|ID|None|
|Product ARN|string|None|False|Product ARN|None|
  
**Recommendation**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Text|string|None|False|Text|None|
|URL|string|None|False|URL|None|
  
**Remediation**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Recommendation|Recommendation|None|False|Recommendation|None|
  
**AwsEc2Instance**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|IAM Instance Profile ARN|string|None|False|IAM instance profile ARN|None|
|Image ID|string|None|False|Image ID|None|
|IPv4 Addresses|[]string|None|False|IPv4 addresses|None|
|IPv6 Addresses|[]string|None|False|IPv6 addresses|None|
|Keyname|string|None|False|Keyname|None|
|Launched At|string|None|False|Launched at|None|
|Subnet ID|string|None|False|Subnet ID|None|
|Type|string|None|False|Type|None|
|VPC ID|string|None|False|VPC ID|None|
  
**AwsIamAccessKey**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created At|string|None|False|Created at|None|
|Status|string|None|False|Status|None|
|Username|string|None|False|Username|None|
  
**AwsS3Bucket**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Owner ID|string|None|False|Owner ID|None|
|Owner Name|string|None|False|Owner name|None|
  
**Container**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Image ID|string|None|False|Image ID|None|
|Image Name|string|None|False|Image name|None|
|Launched At|string|None|False|Launched at|None|
|Name|string|None|False|Name|None|
  
**Details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|AWS EC2 Instance|AwsEc2Instance|None|False|AWS EC2 instance|None|
|AWS IAM Access Key|AwsIamAccessKey|None|False|AWS IAM access key|None|
|AWS S3 Bucket|AwsS3Bucket|None|False|AWS S3 bucket|None|
|Container|Container|None|False|Container|None|
|Other|ProductFields|None|False|Other|None|
  
**Resources**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Details|Details|None|False|Details|None|
|ID|string|None|False|ID|None|
|Partition|string|None|False|Partition|None|
|Region|string|None|False|Region|None|
|Tags|ProductFields|None|False|Tags|None|
|Type|string|None|False|Type|None|
  
**Severity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Normalized|integer|None|False|Normalized|None|
|Product|integer|None|False|Product|None|
  
**ThreatIntelIndicators**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Category|string|None|False|Category|None|
|Last Observed At|string|None|False|Last observed at|None|
|Source|string|None|False|Source|None|
|Source URL|string|None|False|Source URL|None|
|Type|string|None|False|Type|None|
|Value|string|None|False|Value|None|
  
**Findings**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|AWS account ID|string|None|False|AWS account ID|None|
|Compliance|Compliance|None|False|Compliance|None|
|Confidence|integer|None|False|Confidence|None|
|Created At|string|None|False|Created at|None|
|Criticality|integer|None|False|Criticality|None|
|Description|string|None|False|Description|None|
|First Observed At|string|None|False|First observed at|None|
|Generator ID|string|None|False|Generator ID|None|
|ID|string|None|False|ID|None|
|Last Observed At|string|None|False|Last observed at|None|
|Malware|[]Malware|None|False|Malware|None|
|Network|Network|None|False|Network|None|
|Note|Note|None|False|Note|None|
|Process|Process|None|False|Process|None|
|Product ARN|string|None|False|Product ARN|None|
|Product Fields|ProductFields|None|False|Product fields|None|
|Record State|string|None|False|Record state|None|
|Related Findings|[]RelatedFindings|None|False|Related findings|None|
|Remediation|Remediation|None|False|Remediation|None|
|Resources|[]Resources|None|False|Resources|None|
|Schema Version|string|None|False|Schema version|None|
|Severity|Severity|None|False|Severity|None|
|Source URL|string|None|False|Source URL|None|
|Threat Intel Indicators|[]ThreatIntelIndicators|None|False|Threat intel indicators|None|
|Title|string|None|False|Title|None|
|Types|[]string|None|False|Types|None|
|Updated At|string|None|False|Updated at|None|
|User-defined Fields|ProductFields|None|False|User-defined fields|None|
|Verification State|string|None|False|Verification state|None|
|Workflow State|string|None|False|Workflow state|None|
  
**Attributes**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Sent Timestamp|string|None|False|Sent timestamp|None|
  
**Author**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Data Type|string|None|False|Data type|None|
|String Value|string|None|False|String value|None|
  
**MessageAttributes**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Author|Author|None|False|Author|None|
|Title|Author|None|False|Title|None|
|Weeks On|Author|None|False|Weeks on|None|
  
**Message**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attributes|Attributes|None|False|Attributes|None|
|Body|string|None|False|Body|None|
|MD5 of Body|string|None|False|MD5 of body|None|
|MD5 of Message attributes|string|None|False|MD5 of message attributes|None|
|Message Attributes|MessageAttributes|None|False|Message attributes|None|
|Message ID|string|None|False|Message ID|None|
|Receipt Handle|string|None|False|Receipt handle|None|
  
**HTTPHeaders**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Content Length|string|None|False|Content length|None|
|Content Type|string|None|False|Content type|None|
|Date|string|None|False|Date|None|
|Amazon Request ID|string|None|False|X-amzn-requestid|None|
  
**ResponseMetadata**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HTTP Headers|HTTPHeaders|None|False|HTTP headers|None|
|HTTP Status Code|integer|None|False|HTTP status code|None|
|Request ID|string|None|False|Request ID|None|
|Retry Attempts|integer|None|False|Retry attempts|None|
  
**SHCompliance**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Status|string|None|False|Status|None|
  
**SHProductFields**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Recommendationurl|string|None|False|Recommendationurl|None|
|Recordstate|string|None|False|Recordstate|None|
|Relatedawsresources:0/Name|string|None|False|Relatedawsresources:0/name|None|
|Relatedawsresources:0/Type|string|None|False|Relatedawsresources:0/type|None|
|Ruleid|string|None|False|Ruleid|None|
|Standardsguidearn|string|None|False|Standardsguidearn|None|
|Standardsguidesubscriptionarn|string|None|False|Standardsguidesubscriptionarn|None|
|Aws/Securityhub/Companyname|string|None|False|Aws/securityhub/companyname|None|
|Aws/Securityhub/Findingid|string|None|False|Aws/securityhub/findingid|None|
|Aws/Securityhub/Productname|string|None|False|Aws/securityhub/productname|None|
|Aws/Securityhub/Severitylabel|string|None|False|Aws/securityhub/severitylabel|None|
  
**SHRecommendation**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Text|string|None|False|Text|None|
|URL|string|None|False|URL|None|
  
**SHRemediation**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Recommendation|SHRecommendation|None|False|Recommendation|None|
  
**SHResources**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Id|string|None|False|Id|None|
|Partition|string|None|False|Partition|None|
|Region|string|None|False|Region|None|
|Type|string|None|False|Type|None|
  
**SHSeverity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Normalized|integer|None|False|Normalized|None|
|Product|integer|None|False|Product|None|
  
**findings**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Awsaccountid|string|None|False|Awsaccountid|None|
|Compliance|SHCompliance|None|False|Compliance|None|
|Createdat|string|None|False|Createdat|None|
|Description|string|None|False|Description|None|
|Firstobservedat|string|None|False|Firstobservedat|None|
|Generatorid|string|None|False|Generatorid|None|
|Id|string|None|False|Id|None|
|Lastobservedat|string|None|False|Lastobservedat|None|
|Productarn|string|None|False|Productarn|None|
|Productfields|SHProductFields|None|False|Productfields|None|
|Recordstate|string|None|False|Recordstate|None|
|Remediation|SHRemediation|None|False|Remediation|None|
|Resources|[]SHResources|None|False|Resources|None|
|Schemaversion|string|None|False|Schemaversion|None|
|Severity|SHSeverity|None|False|Severity|None|
|Title|string|None|False|Title|None|
|Types|[]string|None|False|Types|None|
|Updatedat|string|None|False|Updatedat|None|
|Workflowstate|string|None|False|Workflowstate|None|
|Approximatearrivaltimestamp|float|None|False|Approximatearrivaltimestamp|None|
|Updatedat|string|None|False|Updatedat|None|
  
**detail**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Actiondescription|string|None|False|Actiondescription|None|
|Actionname|string|None|False|Actionname|None|
|Findings|[]findings|None|False|Findings|None|
  
**securityHubPayload**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Account|string|None|False|Account|None|
|Detail|detail|None|False|Detail|None|
|Detail-Type|string|None|False|Detail-type|None|
|Id|string|None|False|Id|None|
|Region|string|None|False|Region|None|
|Resources|[]string|None|False|Resources|None|
|Source|string|None|False|Source|None|
|Time|string|None|False|Time|None|
|Version|string|None|False|Version|None|


## Troubleshooting

* If you encounter any issues configuring the plugin, check out the [plugin guide](https://insightconnect.help.rapid7.com/docs/aws-security-hub) for more details on how to configure this plugin.

# Version History

* 2.0.5 - Resolved Snyk vulnerabilities | SDK bump to latest version (6.3.7)
* 2.0.4 - Bumping requirements.txt | SDK bump to 6.1.4
* 2.0.3 - Update `docs_url` in plugin spec with a new link to [plugin setup guide](https://docs.rapid7.com/insightconnect/aws-security-hub/)
* 2.0.2 - Add `docs_url` to plugin spec with link to [plugin setup guide](https://insightconnect.help.rapid7.com/docs/aws-security-hub)
* 2.0.1 - Removed unused variables
* 2.0.0 - New spec and help.md format for the Extension Library | Variable names updated as acronyms
* 1.0.0 - Initial plugin

# Links

* [AWS Security Hub](https://aws.amazon.com/security-hub/)

## References

* [ AWS Security Hub](https://aws.amazon.com/security-hub/)
* [AWS Security Hub API](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Operations.html)
* [Boto3](https://github.com/boto/boto3)
* [InsightConnect Plugin Guide](https://docs.rapid7.com/insightconnect/aws-security-hub/)