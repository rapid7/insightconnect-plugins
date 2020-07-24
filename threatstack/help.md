# Description

The Threat Stack plugin is used to get information about alerts, assets, and policies.

[Threat Stack](https://www.threatstack.com) is a cloud security monitoring provider helping companies to achieve compliance and cloud security.

This plugin utilizes the [Threatstack API](https://apidocs.threatstack.com/).

Note that the REST API is undocumented the plugin does not have custom types built which allows for the response outputs to be selectable by name in the UI.
In addition, Threat Stack will be deprecating this API in favor of version 2 when it's released.

# Key Features

* Get information about alerts, organizations, policies, and agents

# Requirements

* A Threat Stack API key
* An organization ID
* The Threat Stack API version

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|REST API key|None|None|
|org_id|string|None|True|Threat Stack Organization ID|None|None|
|timeout|integer|120|False|API timeout|None|None|
|user_id|string|None|True|User ID|None|None|

Example input:

```
```

## Technical Details

### Actions

#### Get Rule

This action is used to get rule.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|rule_id|string|None|True|Rule ID|None|None|
|ruleset_id|string|None|True|Ruleset ID for which the rule ID belongs|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rule|object|True|Rule|

Example output:

```
```

#### Get Agents

This action is used to get agent data.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|end|string|None|False|End date e.g. 2018-01-01|None|None|
|start|string|None|False|Start date e.g. 2017-01-01|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agents|[]agent|True|List of agents|
|count|integer|True|Number of agents|

Example output:

```

```

#### Get Events

This action is used to get events which contributed to an alert.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_id|string|None|True|Alert ID|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|True|Number of events|
|events|[]event|True|List of events|

Example output:

```
{
  "count": 11,
  "events": [
    {
      "eventSource": "ecr.amazonaws.com",
      "eventType": "AwsApiCall",
      "created_at": 1595559480000,
      "errorCode": "AccessDenied",
      "mfaUsed": false,
      "profile_id": "5d52ac59c08db5d269aa3108",
      "userType": "AssumedRole",
      "agent_id": "5d52ac59c08db5d269aa3108",
      "_id": "0e36a925-a612-4b4a-9714-35eaaf9b9964",
      "errorMessage": "User: arn:aws:sts::113901497002:assumed-role/terra...",
      "eventClass": "CloudtrailEvent",
      "eventID": "0e36a925-a612-4b4a-9714-35eaaf9b9964",
      "MFAUsed": "false",
      "eventName": "BatchGetImage",
      "feed": "cloudtrail",
      "ip": "AWS Internal",
      "recipientAccountId": "113901497002",
      "eventId": "0e36a925-a612-4b4a-9714-35eaaf9b9964",
      "error": "AccessDenied",
      "recipientAccountID": "113901497002",
      "requestID": "832d1700-3e62-4021-83f0-ca1fc05d663a",
      "tsEventType": "cloudtrail",
      "accountId": "113901497002",
      "eventVersion": "1.05",
      "organizationId": "5babc3a62d1d16f529050c86",
      "userIdentity": {
        "principalId": "AROAIRC6TNAC6P32APTLG:i-053374f60a4d79830",
        "sessionContext": {
          "attributes": {
            "creationDate": "2020-07-24T00:16:39Z",
            "mfaAuthenticated": "false"
          },
          "ec2RoleDelivery": "1.0",
          "sessionIssuer": {
            "type": "Role",
            "userName": "terraform-eks-k8s-node",
            "accountId": "113901497002",
            "arn": "arn:aws:iam::113901497002:role/terraform-eks-k8s-n...",
            "principalId": "AROAIRC6TNAC6P32APTLG"
          },
          "webIdFederationData": {}
        },
        "type": "AssumedRole",
        "accessKeyId": "ASIAJJRY65OGGO2NCTEQ",
        "accountId": "113901497002",
        "arn": "arn:aws:sts::113901497002:assumed-role/terraform-e...",
        "invokedBy": "AWS Internal"
      },
      "eventSourceType": "AwsApiCall",
      "eventTime": 1595559480000,
      "profileId": "5d52ac59c08db5d269aa3108",
      "timestamp": 1595559480000,
      "user": "i-053374f60a4d79830",
      "arnRole": "assumed-role/terraform-eks-k8s-node/i-053374f60a4d...",
      "agentId": "5d52ac59c08db5d269aa3108",
      "awsRegion": "us-east-1",
      "event_type": "cloudtrail",
      "ingestTime": 1595560287588,
      "organization_id": "5babc3a62d1d16f529050c86",
      "region": "us-east-1",
      "requestId": "832d1700-3e62-4021-83f0-ca1fc05d663a",
      "accessKey": "ASIAJJRY65OGGO2NCTEQ",
      "userAgent": "AWS Internal",
      "sourceIPAddress": "AWS Internal"
    },
    {
      "requestID": "a4f7c208-541e-4206-beb8-34b02cedb663",
      "created_at": 1595559174000,
      "errorCode": "AccessDenied",
      "eventType": "AwsApiCall",
      "eventVersion": "1.05",
      "event_type": "cloudtrail",
      "ingestTime": 1595559811447,
      "mfaUsed": false,
      "accountId": "113901497002",
      "eventID": "2f121599-941b-433e-a0c9-a3179ecca3be",
      "eventSourceType": "AwsApiCall",
      "ip": "AWS Internal",
      "organizationId": "5babc3a62d1d16f529050c86",
      "recipientAccountId": "113901497002",
      "region": "us-east-1",
      "userAgent": "AWS Internal",
      "errorMessage": "User: arn:aws:sts::113901497002:assumed-role/terra...",
      "accessKey": "ASIAJJRY65OGGO2NCTEQ",
      "recipientAccountID": "113901497002",
      "userType": "AssumedRole",
      "MFAUsed": "false",
      "eventSource": "ecr.amazonaws.com",
      "organization_id": "5babc3a62d1d16f529050c86",
      "timestamp": 1595559174000,
      "arnRole": "assumed-role/terraform-eks-k8s-node/i-053374f60a4d...",
      "error": "AccessDenied",
      "eventId": "2f121599-941b-433e-a0c9-a3179ecca3be",
      "eventName": "BatchGetImage",
      "profileId": "5d52ac59c08db5d269aa3108",
      "sourceIPAddress": "AWS Internal",
      "user": "i-053374f60a4d79830",
      "agent_id": "5d52ac59c08db5d269aa3108",
      "profile_id": "5d52ac59c08db5d269aa3108",
      "userIdentity": {
        "arn": "arn:aws:sts::113901497002:assumed-role/terraform-e...",
        "invokedBy": "AWS Internal",
        "principalId": "AROAIRC6TNAC6P32APTLG:i-053374f60a4d79830",
        "sessionContext": {
          "attributes": {
            "creationDate": "2020-07-24T00:16:39Z",
            "mfaAuthenticated": "false"
          },
          "ec2RoleDelivery": "1.0",
          "sessionIssuer": {
            "type": "Role",
            "userName": "terraform-eks-k8s-node",
            "accountId": "113901497002",
            "arn": "arn:aws:iam::113901497002:role/terraform-eks-k8s-n...",
            "principalId": "AROAIRC6TNAC6P32APTLG"
          },
          "webIdFederationData": {}
        },
        "type": "AssumedRole",
        "accessKeyId": "ASIAJJRY65OGGO2NCTEQ",
        "accountId": "113901497002"
      },
      "eventTime": 1595559174000,
      "agentId": "5d52ac59c08db5d269aa3108",
      "awsRegion": "us-east-1",
      "eventClass": "CloudtrailEvent",
      "feed": "cloudtrail",
      "requestId": "a4f7c208-541e-4206-beb8-34b02cedb663",
      "tsEventType": "cloudtrail",
      "_id": "2f121599-941b-433e-a0c9-a3179ecca3be"
    }
  ]
}
```

#### Get Alerts

This action is used to get alerts by filter.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|end|string|None|False|End date e.g. 2018-01-01|None|None|
|start|string|None|False|Start date e.g. 2017-01-01|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alerts|[]alert|True|List of alerts|
|count|integer|True|Number of alerts|

Example output:

```
{
  "alert": {
    "dataSource": "cloudtrail",
    "id": "2abca110-cb87-11ea-b55e-4f5cfb08a8d1",
    "ruleId": "ed8418b3-69f6-11ea-8dc5-19fea1b7cb31",
    "title": "CloudTrail: Access Denied: Event: DescribeScalingP...",
    "aggregates": {
      "ip": "38.98.140.20",
      "user": "user@example.com",
      "accountId": "113901497002",
      "eventName": "DescribeScalingPolicies",
      "eventSource": "autoscaling.amazonaws.com"
    },
    "createdAt": "2020-07-21T19:19:58.625Z",
    "isDismissed": false,
    "rulesetId": "aac04548-69f6-11ea-b4d2-ad32b4432dec",
    "severity": 3
  }
}
```

#### Get Alert

This action is used to get alert data by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_id|string|None|True|Alert ID e.g. 597b8c751c7ff17fcf028e54|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alert|alert|True|Detailed alert data|

Example output:

```

{
  "alert": {
    "count": 34,
    "severity": 3,
    "title": "User Activity (Login Failures): User undefined failed authentication from IP undefined",
    "rule": {
      "exclusion_filter": null,
      "hash": "b27736c8444f963efae2fd1692c771bb",
      "description": "This rule alerts on Login failures by users. Monitoring of failed login attempts can identify brute force/dictionary attacks as well as users trying to access systems without authorization.",
      "title": "User Activity (Login Failures): User {{user}} failed authentication from IP {{src_ip}}",
      "hermes_alert_policy_id": "7f7ba0ac-eef7-11e6-b0e1-cf66e6984857",
      "severity": 3,
      "original_rule": {
        "description": "This rule alerts on Login failures by users. Monitoring of failed login attempts can identify brute force/dictionary attacks as well as users trying to access systems without authorization.",
        "severity": 3,
        "tags": [],
        "anomalous_only": false,
        "enabled": true,
        "created_at": "2016-01-27T22:19:51.516Z",
        "aggregate_fields": [
          "user",
          "src_ip"
        ],
        "window_seconds": 3600,
        "updated_at": "2017-04-06T15:24:33.586Z",
        "id": "7f842c39-eef7-11e6-b0e1-8d4568316479",
        "filter": "group = \"authentication-failed\" or group = \"invalid_login\" OR group = \"authentication_failed\" or group like \"fail\"",
        "auto_suppress": false,
        "threshold": 1,
        "title": "User Activity (Login Failures): User {{user}} failed authentication from IP {{src_ip}}",
        "type": "all",
        "exclusions": [],
        "name": "Users : Login Failures"
      },
      "window_seconds": 3600,
      "TranslationKeyMap": {
        "files": [],
        "domain": [],
        "src_port": [],
        "event_type": [],
        "ip": [],
        "agent": [],
        "port": [],
        "exit": [],
        "user": [],
        "host_signatures": [],
        "threat_type": [],
        "threat_source": [],
        "dst_port": []
      },
      "alert_policy_id": "53743bc0BEEFBEEFBEEFBEEF",
      "id": "7f842c39-eef7-11e6-b0e1-8d4568316479",
      "filter": "group = \"authentication-failed\" or group = \"invalid_login\" OR group = \"authentication_failed\" or group like \"fail\"",
      "aggFields": [
        "user",
        "src_ip"
      ],
      "auto_suppress": false,
      "hermes_rule_id": "7f842c39-eef7-11e6-b0e1-8d4568316479",
      "threshold": 1,
      "_hash_key": "b27736c8444f963efae2fd1692c771bb",
      "type": "all",
      "rule_id": "53743bc0BEEFBEEFBEEFBEEF",
      "enabled": true,
      "policy_id": "7f7ba0ac-eef7-11e6-b0e1-cf66e6984857"
    },
    "created_at": 1500245139383,
    "last_updated_at": "2017-07-16T23:43:47.340Z",
    "expires_at": 1500248739383,
    "latest_events": [
      {
        "comment": "Attempt to login using a non-existent user",
        "sigid": 5710,
        "group": [
          "invalid_login",
          "authentication_failed"
        ],
        "log": "Jul 16 23:43:33 ip-10-1-255-11 sshd[30916]: input_userauth_request: invalid user ubnt [preauth]",
        "level": 5,
        "_insert_time": 1500248609195,
        "timestamp": 1500248620555,
        "hostname": "ip-10-1-255-11",
        "pid": 30916,
        "location": "/var/log/secure",
        "organization_id": "589cb810a7d05f7f3a438cb2",
        "agent_id": "58e52b4c4cc77462cf786a9d",
        "groups": [
          "invalid_login",
          "authentication_failed"
        ],
        "_id": "9888ce3c-6a80-11e7-9dab-0acd2b127a3c",
        "_type": "host",
        "event_type": "host"
      },
      {
        "comment": "Attempt to login using a non-existent user",
        "sigid": 5710,
        "group": [
          "invalid_login",
          "authentication_failed"
        ],
        "log": "Jul 16 23:43:35 ip-10-1-255-11 sshd[30938]: input_userauth_request: invalid user user [preauth]",
        "level": 5,
        "_insert_time": 1500248609195,
        "timestamp": 1500248620555,
        "hostname": "ip-10-1-255-11",
        "pid": 30938,
        "location": "/var/log/secure",
        "organization_id": "589cb810a7d05f7f3a438cb2",
        "agent_id": "58e52b4c4cc77462cf786a9d",
        "groups": [
          "invalid_login",
          "authentication_failed"
        ],
        "_id": "9888ce3d-6a80-11e7-9dab-0acd2b127a3c",
        "_type": "host",
        "event_type": "host"
      },
      {
        "comment": "Attempt to login using a non-existent user",
        "sigid": 5710,
        "group": [
          "invalid_login",
          "authentication_failed"
        ],
        "log": "Jul 16 23:43:23 ip-10-1-255-11 sshd[30891]: input_userauth_request: invalid user telnet [preauth]",
        "level": 5,
        "_insert_time": 1500248579195,
        "timestamp": 1500248608549,
        "hostname": "ip-10-1-255-11",
        "pid": 30891,
        "location": "/var/log/secure",
        "organization_id": "589cb810a7d05f7f3a438cb2",
        "agent_id": "58e52b4c4cc77462cf786a9d",
        "groups": [
          "invalid_login",
          "authentication_failed"
        ],
        "_id": "9160d616-6a80-11e7-b48f-1296fd8e9d1a",
        "_type": "host",
        "event_type": "host"
      },
      {
        "comment": "Attempt to login using a non-existent user",
        "sigid": 5710,
        "group": [
          "invalid_login",
          "authentication_failed"
        ],
        "log": "Jul 16 23:43:24 ip-10-1-255-11 sshd[30911]: input_userauth_request: invalid user test [preauth]",
        "level": 5,
        "_insert_time": 1500248579195,
        "timestamp": 1500248608549,
        "hostname": "ip-10-1-255-11",
        "pid": 30911,
        "location": "/var/log/secure",
        "organization_id": "589cb810a7d05f7f3a438cb2",
        "agent_id": "58e52b4c4cc77462cf786a9d",
        "groups": [
          "invalid_login",
          "authentication_failed"
        ],
        "_id": "9160d617-6a80-11e7-b48f-1296fd8e9d1a",
        "_type": "host",
        "event_type": "host"
      },
      {
        "comment": "Attempt to login using a non-existent user",
        "sigid": 5710,
        "group": [
          "invalid_login",
          "authentication_failed"
        ],
        "log": "Jul 16 23:43:42 ip-10-1-255-11 sshd[30941]: input_userauth_request: invalid user user1 [preauth]",
        "level": 5,
        "_insert_time": 1500248609195,
        "timestamp": 1500248623562,
        "hostname": "ip-10-1-255-11",
        "pid": 30941,
        "location": "/var/log/secure",
        "organization_id": "589cb810a7d05f7f3a438cb2",
        "agent_id": "58e52b4c4cc77462cf786a9d",
        "groups": [
          "invalid_login",
          "authentication_failed"
        ],
        "_id": "9a53a3b1-6a80-11e7-baf2-0acabd9a2786",
        "_type": "host",
        "event_type": "host"
      }
    ],
    "dismissed": false,
    "key": "7f842c39-eef7-11e6-b0e1-8d4568316479-58e52b4c4cc77462cf786a9d-b27736c8444f963efae2fd1692c771bb",
    "active": true,
    "rule_id": "53743bc0beefbeefbeefbeef",
    "unread": true,
    "type": "rule",
    "id": "596bec96f11ead2a97ee0bc0",
    "alert_policy_id": "53743bc0beefbeefbeefbeef",
    "agent_id": "58e52b4c4cc77462cf786a9d"
  }
}

```

#### Get Agent

This action is used to get agent data.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent_id|string|None|True|Agent ID e.g. 597b2c751b7cc18fcf028e52|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agent|agent|True|Detailed agent data|

Example output:

```

{
  "agent": {
    "status": "active",
    "hostname": "default-centos-67",
    "name": "default-centos-67",
    "created_at": "2017-04-27T20:01:22.353Z",
    "activated_at": "2017-04-27T20:01:22.130Z",
    "enabled": false,
    "updated_at": "2017-05-11T20:15:12.268Z",
    "paused": false,
    "version": "1.6.2",
    "agent_id": "589cb810a7d05f7f3a438cb2-4885b890-2b84-11e7-b27b-9f608f21aff091bf46da8a73e77e",
    "last_reported_at": "2017-04-27T20:05:09.939Z",
    "online": false,
    "ip_address": "144.121.5.10",
    "id": "59024beed911cadeadee1b09",
    "description": ""
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

* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Threat Stack](https://threatstack.com)
* [Threat Stack API](https://apidocs.threatstack.com/)
