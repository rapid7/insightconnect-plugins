# Description

The Threat Stack plugin is used to get information about alerts, assets, and policies.

[Threat Stack](https://www.threatstack.com) is a cloud security monitoring provider helping companies to achieve compliance and cloud security.

This plugin utilizes the [Threatstack API](https://apidocs.threatstack.com/).

Note that the REST API is undocumented the plugin does not have custom types built which allows for the response outputs to be selectable by name in the UI.
In addition, Threat Stack will be deprecating this API in favor of version 2 when it's released.

# Key Features

* Get information about Alerts, Organizations, Policies, and Agents

# Requirements

* A Threat Stack API key
* An Organization ID
* The Threat Stack API version

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|REST API key|None|
|org_id|string||False|Threat Stack Org ID (For use when multiple orgs)|None|
|api_version|integer|1|False|API version|None|
|timeout|integer|120|False|API timeout|None|

## Technical Details

### Actions

#### Get Alert

This action is used to get alert data by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|fields|[]string|None|False|Fields to return|None|
|alert_id|string|None|True|Alert ID e.g. 597b8c751c7ff17fcf028e54|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alert|object|True|Detailed alert data|

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

#### Get Policy

This action is used to get a policy.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|fields|[]string|None|False|Fields to return|None|
|policy_id|string|None|True|Threat Stack policy ID|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|policy|[]object|True|Policy data|

Example output:

```

{
  "policy": {
    "organization_id": "deadbeefdeadbeefdeadbeef",
    "name": "CloudTrail Base Rule Set",
    "file_integrity_rules": [],
    "created_at": "2015-09-25T19:24:03.956Z",
    "alert_policy": [
      {
        "description": "This rule tracks file views (GetObject), file changes (PutObject) into specific S3 buckets ",
        "title": "CloudTrail Activity (S3FIM): {{eventName}} by {{user}}",
        "window_seconds": 86400,
        "created_at": "2017-01-11T13:33:06.593Z",
        "aggregate_fields": [
          "eventName",
          "user"
        ],
        "enabled": true,
        "updated_at": "2017-01-11T13:34:53.315Z",
        "exclusions": [],
        "filter": "(eventName = \"PutObjectAcl\" or eventName = \"GetObjectAcl\" or eventName = \"GetObject\" or eventName = \"PutObject\" or eventName = \"ListObjects\" or eventName = \"HeadObject\") and bucketName = \"xx\"",
        "threshold": 1,
        "type": "cloudtrail",
        "id": "7f7474ae-eef7-11e6-b0e1-d9a81a1397f1",
        "severity": 2
      },
      ...
    ]
    "enabled": true,
    "updated_at": "2015-09-25T19:24:03.956Z",
    "alert_policy_id": "7f6cac6f-eef7-11e6-b0e1-ad6efc548ecd",
    "agent_count": 0,
    "alert_rule_count": 31,
    "id": "7f6cac6f-eef7-11e6-b0e1-ad6efc548ecd",
    "description": "CloudTrail Base Rule Set"
  }
}

```

#### Get Alerts

This action is used to get alerts by filter.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|start|string|None|False|Start date e.g. 2017-01-01|None|
|end|string|None|False|End date e.g. 2018-01-01|None|
|fields|[]string|None|False|Fields to return|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|True|Number of alerts|
|alerts|[]object|True|List of alerts|

Example output:

```

{
  count: 16,
  alerts: [
    {
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
    },
    ...
  ]
}

```

#### Get Organization

This action is used to get an organization.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|organization_id|string|None|True|Threat Stack organization ID e.g. 583cb310a3d05a733a4383ap|None|
|fields|[]string|None|False|Fields to return|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|organization|[]object|True|Organization data|

Example output:

```

{
  "organization": {
    "role": "owner",
    "id": "deadbeefdeadbeefdeadbeef",
    "name": "Example Account"
  }
}

```

#### Get Agents

This action is used to get agent data.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|start|string|None|False|Start date e.g. 2017-01-01|None|
|end|string|None|False|End date e.g. 2018-01-01|None|
|fields|[]string|None|False|Fields to return|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|True|Number of agents|
|alerts|[]object|True|List of agents|

Example output:

```

{
  "count": 47,
  "agents": [
    {
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
    },
    ...
  ]
}

```

#### Get Organizations

This action is used to get organizations.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|fields|[]string|None|False|Fields to return|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|True|Number of organizations|
|organizations|[]object|True|Array of organizations|

Example output:

```

{
  "count": 1,
  "organizations": [
    {
      "role": "owner",
      "id": "deadbeefdeadbeefdeadbeef",
      "name": "Example Account"
    }
  ]
}

```

#### Get Policies

This action is used to get policies.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|fields|[]string|None|False|Fields to return|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|True|Number of policies|
|policies|[]object|True|Array of policies|

Example output:

```

{
  count: 2,
  policies: [
    {
      "policy": {
        "organization_id": "deadbeefdeadbeefdeadbeef",
        "name": "CloudTrail Base Rule Set",
        "file_integrity_rules": [],
        "created_at": "2015-09-25T19:24:03.956Z",
        "alert_policy": [
          {
            "description": "This rule tracks file views (GetObject), file changes (PutObject) into specific S3 buckets ",
            "title": "CloudTrail Activity (S3FIM): {{eventName}} by {{user}}",
            "window_seconds": 86400,
            "created_at": "2017-01-11T13:33:06.593Z",
            "aggregate_fields": [
              "eventName",
              "user"
            ],
            "enabled": true,
            "updated_at": "2017-01-11T13:34:53.315Z",
            "exclusions": [],
            "filter": "(eventName = \"PutObjectAcl\" or eventName = \"GetObjectAcl\" or eventName = \"GetObject\" or eventName = \"PutObject\" or eventName = \"ListObjects\" or eventName = \"HeadObject\") and bucketName = \"xx\"",
            "threshold": 1,
            "type": "cloudtrail",
            "id": "7f7474ae-eef7-11e6-b0e1-d9a81a1397f1",
            "severity": 2
          },
          ...
        ]
        "enabled": true,
        "updated_at": "2015-09-25T19:24:03.956Z",
        "alert_policy_id": "7f6cac6f-eef7-11e6-b0e1-ad6efc548ecd",
        "agent_count": 0,
        "alert_rule_count": 31,
        "id": "7f6cac6f-eef7-11e6-b0e1-ad6efc548ecd",
        "description": "CloudTrail Base Rule Set"
      }
    },
    ...
  ]
}

```

#### Get Agent

This action is used to get agent data.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|fields|[]string|None|False|Fields to return|None|
|agent_id|string|None|True|Agent ID e.g. 597b2c751b7cc18fcf028e52|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|agent|object|True|Detailed agent data|

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

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Threat Stack](https://threatstack.com)
* [Threat Stack API](https://apidocs.threatstack.com/)
