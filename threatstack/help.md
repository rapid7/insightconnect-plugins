# Description

Get information about alerts, assets, policies, and more.

[Threat Stack](https://www.threatstack.com) is a cloud security monitoring provider helping companies to achieve compliance and cloud security.

This plugin utilizes the [Threat Stack API](https://apidocs.threatstack.com/).

# Key Features

* Get information about alerts, rules, agents, and events

# Requirements

* Threat Stack API key
* Threat Stack user ID
* Threat Stack organization ID

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|REST API key|None|None|
|org_id|string|None|True|Threat Stack organization ID|None|None|
|timeout|integer|120|False|API timeout|None|None|
|user_id|string|None|True|User ID|None|None|

Example input:

```
{
  "api_key": "23c71eaadfdde87bcfae85cefedb528f0e556c92463b87c3674271d65f00fb3f",
  "org_id": "25cd88bd50b9ff3822aabd88",
  "timeout": 120,
  "user_id": "9bb2ad3aeb246c7d145056e7"
}
```

## Technical Details

### Actions

#### Get Rule

This action is used to get a rule.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|rule_id|string|None|True|Rule ID|None|1bbc84ed9-17db-18cd-1937-1947ebd910a2|
|ruleset_id|string|None|True|Ruleset ID for which the rule ID belongs|None|1947cbe9-1c8e-11e9-91be-18cbed810a82|

Example input:

```
{
  "rule_id": "1bbc84ed9-17db-18cd-1937-1947ebd910a2",
  "ruleset_id": "1947cbe9-1c8e-11e9-91be-18cbed810a82"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rule|rule|True|Rule|

Example output:

```
{
  "rule": {
    "id": "1bbc84ed9-17db-18cd-1937-1947ebd910a2",
    "rulesetId": "1947cbe9-1c8e-11e9-91be-18cbed810a82",
    "name": "User: Sysctl",
    "type": "Host",
    "createdAt": "2019-09-23T15:02:25.924Z",
    "updatedAt": "2020-04-27T21:50:33.549Z",
    "title": "User: Sysctl : {{exe}} run by {{user}} with arguments {{arguments}}",
    "severityOfAlerts": 3,
    "alertDescription": "Monitoring Sysctl",
    "aggregateFields": [
      "user",
      "exe",
      "arguments"
    ],
    "filter": "command = \"sysctl\"",
    "window": 86400,
    "threshold": 1,
    "suppressions": [
      "user = \"root\" and exe = \"/sbin/sysctl\" and arguments = \"/sbin/sysctl\" and agent_id = \"dfe3cc18-12c7-4df3-aa95-4fb4ff00f533\"",
      "user = \"root\" and exe = \"/sbin/sysctl\" and arguments = \"/sbin/sysctl\" and agent_id=\"135ab463-95c8-46d1-b58f-f7922d6a7765\"",
      "cwd starts_with \"/opt/rapid7\" or cwd starts_with \"/home/insightvm\" or user starts_with \"insightvm\"",
      "(user = \"root\" and exe like \"/sbin/sysctl\" and arguments like \"sysctl -n\") and (arguments like \"net.ipv4.tcp_keepalive_intvl\" or arguments like \"vm.dirty_background_ratio\" or arguments like \"vm.dirty_ratio\" or arguments like \"vm.swappiness\" or arguments like \"vm.dirty_expire_centisecs\" or arguments like \"net.ipv4.tcp_keepalive_time\" or arguments like \"net.ipv4.tcp_keepalive_probes\" or arguments like \"net.ipv4.ip_local_port_range\" or arguments like \"net.ipv4.tcp_fin_timeout\" or arguments like \"net.ipv4.tcp_tw_reuse\" or arguments like \"net.ipv4.ip_default_ttl\")"
    ],
    "enabled": true
  }
}
```

#### Get Agents

This action is used to get agent data.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|end|string|None|False|End date in yyyy-mm-dd format e.g. 2018-01-01|None|2018-01-01|
|start|string|None|False|Start date in yyyy-mm-dd format e.g. 2017-01-01|None|2018-01-01|

Example input:

```
{
  "end": "2018-01-01",
  "start": "2018-01-01"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agents|[]agent|True|List of agents|
|count|integer|True|Number of agents|

Example output:

```
{
  "agents": [
    {
      "id": "adbc2b0d-22fd-4e15-82d5-cb55b8e7bdbc",
      "status": "online",
      "createdAt": "2020-07-27T20:41:29.454Z",
      "lastReportedAt": "2020-07-27T20:50:44.505Z",
      "version": "2.1.3c",
      "name": "example",
      "hostname": "example",
      "ipAddresses": {
        "private": [],
        "link_local": [],
        "public": [
          "198.51.100.100"
        ]
      },
      "tags": [
        {
          "source": "ec2",
          "key": "aws:autoscaling:groupName",
          "value": "ac-prod-k8s-cluster-1.15-ac-spot-0"
        },
        {
          "source": "ec2",
          "key": "kubernetes.io/cluster/ac-prod-k8s-cluster",
          "value": "owned"
        }
      ],
      "agentType": "investigate"
    }
  ],
  "count": 1
}
```

#### Get Events

This action is used to get events which contributed to an alert.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_id|string|None|True|Alert ID|None|183d125e-b7b6-47f6-b872-9242df0f21f3|

Example input:

```
{
  "alert_id": "183d125e-b7b6-47f6-b872-9242df0f21f3"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|True|Number of events|
|events|[]event|True|List of events|

Example output:

```
{
  "events": [
    {
      "timestamp": 1595559480000,
      "_id": "92c92b48-064f-4060-b1d2-b240a96c31cd",
      "event_type": "cloudtrail",
      "organization_id": "8d8460c76ca30b6f4e9f429b",
      "user": "i-053374f60a4d79830",
      "agent_id": "68ecb9589e26d51f48d109ff",
      "eventClass": "CloudtrailEvent",
      "miscellaneous": {
        "errorMessage": "User: arn:aws:sts::assumed-role/terraform-eks-k8s-node/i is not authorized to perform: ecr:BatchGetImage on resource: arn:aws:ecr:us-east-1:repository/pygrate",
        "eventId": "2ce0c765-7607-47c6-a8f2-1cc629ea7e75",
        "tsEventType": "cloudtrail",
        "eventType": "AwsApiCall",
        "userIdentity": {
          "arn": "arn:aws:sts::assumed-role/terraform-eks-k8s-node/i",
          "principalId": "AROBCAB8DIQP7TE2APDPT:i-053374f60a4d79830",
          "accessKeyId": "ASIACCRJ43OTPOVNEIFG",
          "accountId": "987047183047",
          "invokedBy": "AWS Internal",
          "type": "AssumedRole",
          "sessionContext": {
            "sessionIssuer": {
              "arn": "arn:aws:iam::946856184103:role/terraform-eks-k8s-node",
              "principalId": "AROBCAB8DIQP7TE2APDPT",
              "accountId": "987047183047",
              "type": "Role",
              "userName": "terraform-eks-k8s-node"
            },
            "webIdFederationData": {},
            "attributes": {
              "mfaAuthenticated": "false",
              "creationDate": "2020-07-24T00:16:39Z"
            },
            "ec2RoleDelivery": "1.0"
          }
        },
        "userAgent": "AWS Internal",
        "mfaUsed": false,
        "recipientAccountId": "987047183047",
        "accountId": "987047183047",
        "profile_id": "1193792bc073bdb479cbe1846",
        "eventVersion": "1.05",
        "feed": "cloudtrail",
        "eventTime": 1595559480000,
        "created_at": 1595559480000,
        "userType": "AssumedRole",
        "eventID": "adfe635d-7a8a-4c0f-9091-0929d14d5018",
        "ip": "AWS Internal",
        "ingestTime": 1595560287588,
        "sourceIPAddress": "AWS Internal",
        "eventSource": "ecr.amazonaws.com",
        "arnRole": "assumed-role/terraform-eks-k8s-node/i",
        "MFAUsed": "false",
        "organizationId": "9bbb85cc42d68e5f4f4ce5fe",
        "requestID": "d649bec7-eaa2-4f4d-8fd1-ea549922510f",
        "eventSourceType": "AwsApiCall",
        "awsRegion": "us-east-1",
        "eventName": "BatchGetImage",
        "error": "AccessDenied",
        "region": "us-east-1",
        "errorCode": "AccessDenied",
        "requestId": "a0881659-9658-4606-9254-056e03a638cf",
        "recipientAccountID": "173457601846",
        "profileId": "1ebde0c9301be18cbdeb5cbe7",
        "accessKey": "ASIACCRJ43OTPOVNEIFG",
        "agentId": "c34cb43e79948f0a4a6b3b2b"
      }
    }
  ],
  "count": 1
}
```

#### Get Alerts

This action is used to get alerts by filter.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|end|string|None|False|End date in yyyy-mm-dd format e.g. 2018-01-01|None|2018-01-01|
|start|string|None|False|Start date in yyyy-mm-dd format e.g. 2017-01-01|None|2018-01-01|

Example input:

```
{
  "end": "2018-01-01",
  "start": "2018-01-01"
}
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
    "id": "cc3c6e27-4262-4b22-89a3-d00f0c6d7e3b",
    "ruleId": "4eabd6aa-b96d-4461-a023-1e403e5e410a",
    "title": "CloudTrail: Access Denied: Event: DescribeScalingP...",
    "aggregates": {
      "ip": "198.51.100.100",
      "user": "user@example.com",
      "accountId": "017484651936",
      "eventName": "DescribeScalingPolicies",
      "eventSource": "autoscaling.amazonaws.com"
    },
    "createdAt": "2020-07-21T19:19:58.625Z",
    "isDismissed": false,
    "rulesetId": "770b3d96-253c-4b2d-b43c-d058e97241e7",
    "severity": 3
  }
}
```

#### Get Alert

This action is used to get alert data by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_id|string|None|True|Alert ID e.g. 597b8c751c7ff17fcf028e54|None|4ed70109-bd4b-4c29-a52f-8c576ba8ce47|

Example input:

```
{
  "alert_id": "4ed70109-bd4b-4c29-a52f-8c576ba8ce47"
}
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
      "hash": "44d88612fea8a8f36de82e1278abb02f",
      "description": "This rule alerts on Login failures by users. Monitoring of failed login attempts can identify brute force/dictionary attacks as well as users trying to access systems without authorization.",
      "title": "User Activity (Login Failures): User {{user}} failed authentication from IP {{src_ip}}",
      "hermes_alert_policy_id": "fd592b75-5a0f-4488-9b7f-1f7628f75701",
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
        "id": "e5b5a82c-7638-4015-8fbb-26cd7b0bdf3f",
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
      "id": "4aa8c3f1-d5a6-4afd-a84e-7789e7abcd41",
      "filter": "group = \"authentication-failed\" or group = \"invalid_login\" OR group = \"authentication_failed\" or group like \"fail\"",
      "aggFields": [
        "user",
        "src_ip"
      ],
      "auto_suppress": false,
      "hermes_rule_id": "3ad1d113-cf3d-48cd-992e-2043673aefac",
      "threshold": 1,
      "_hash_key": "b27736c8444f963efae2fd1692c771bb",
      "type": "all",
      "rule_id": "53743bc0BEEFBEEFBEEFBEEF",
      "enabled": true,
      "policy_id": "91278a37-a2d5-452f-909a-bb1c08959cd9"
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
        "hostname": "example",
        "pid": 30916,
        "location": "/var/log/secure",
        "organization_id": "c7468a346f1e0350fbd0f85a",
        "agent_id": "0c11cec5e91661179a99b08f",
        "groups": [
          "invalid_login",
          "authentication_failed"
        ],
        "_id": "0fd85ed5-c776-4587-ab08-dee6666ce961",
        "_type": "host",
        "event_type": "host"
      }
    ],
    "dismissed": false,
    "key": "1ecf8ef4-3738-425a-b348-f8a34c9ede09-0c11cec5e91661179a99b08f-bcbe79037cbde194784563edf37cb18cb",
    "active": true,
    "rule_id": "53743bc0beefbeefbeefbeef",
    "unread": true,
    "type": "rule",
    "id": "3ac4be2a4bcc032a63a35c15",
    "alert_policy_id": "53743bc0beefbeefbeefbeef",
    "agent_id": "9710350fc348f6d715b3a87c"
  }
}
```

#### Get Agent

This action is used to get agent data.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|agent_id|string|None|True|Agent ID e.g. 597b2c751b7cc18fcf028e52|None|597b2c751b7cc18fcf028e52|

Example input:

```
{
  "agent_id": "597b2c751b7cc18fcf028e52"
}
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
    "agent_id": "06284106-09e6-456a-8988-2b98d484112a-43d709b6284564b47633597e",
    "last_reported_at": "2017-04-27T20:05:09.939Z",
    "online": false,
    "ip_address": "198.51.100.100",
    "id": "d8cac3f5ed3555c35673ac52",
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

* 2.0.0 - Use ThreatStack API v2 | Fix all actions | Type action outputs
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Threat Stack](https://threatstack.com)
* [Threat Stack API](https://apidocs.threatstack.com/)
