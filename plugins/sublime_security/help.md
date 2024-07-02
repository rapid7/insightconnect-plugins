# Description

A plugin to interact with Sublime Security API

# Key Features

* Enrich alerts with message metadata or screenshots

# Requirements

* Sublime Security API key

# Supported Product Versions

* Sublime Security API v0

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|The API key used for authentication with the Sublime Security API.|None|None|None|None|

Example input:

```
{
  "api_key": {
    "secretKey": ""
  }
}
```

## Technical Details

### Actions


#### Analyze Message by ID

This action is used to analyze a message by its ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|message_id|string|None|True|The ID of the message to be analyzed.|None|12345|None|None|
  
Example input:

```
{
  "message_id": 12345
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|analysis|object|False|The analysis result of the message.|{'threats': ['Phishing'], 'score': 85, 'details': 'The message contains suspicious links and sender address.'}|
  
Example output:

```
{
  "analysis": {
    "details": "The message contains suspicious links and sender address.",
    "score": 85,
    "threats": [
      "Phishing"
    ]
  }
}
```

#### Analyze Raw Message

This action is used to analyze a raw email message.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|queries|[]queries|None|False|Queries to analyze|None|[{"name": "string", "severity": "string", "source": "string"}]|None|None|
|raw_message|bytes|None|True|The full base64 encoded raw eml message|None|UmFwaWQ3Cj09PT09PQo=|None|None|
|rules|[]rules|None|False|Rules to analyze|None|[{"active": true, "feed_id": "string", "name": "string", "severity": "string", "source": "string"}]|None|None|
|run_active_detection_rules|boolean|None|False|Whether to analyze the message with all active detection rules in your organization|None|True|None|None|
|run_all_detection_rules|boolean|None|False|Whether to analyze with all detection rules from all Feeds, including uninstalled + inactive Feed rules, as well as any active detection rules you’ve created that are not part of a Feed|None|True|None|None|
|run_all_insights|boolean|None|False|Whether to analyze with all insights|None|True|None|None|
  
Example input:

```
{
  "queries": [
    {
      "name": "string",
      "severity": "string",
      "source": "string"
    }
  ],
  "raw_message": "UmFwaWQ3Cj09PT09PQo=",
  "rules": [
    {
      "active": true,
      "feed_id": "string",
      "name": "string",
      "severity": "string",
      "source": "string"
    }
  ],
  "run_active_detection_rules": true,
  "run_all_detection_rules": true,
  "run_all_insights": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|query_results|[]query_results|False|Query result details|[{"error": "string", "execution_time": 0, "external_errors": ["string"], "query": {"name": "string", "severity": "string", "source": "string"}, "success": true}]|
|rule_results|[]rule_results|False|Analyze result details|[{"error": "string", "execution_time": 0, "external_errors": ["string"], "matched": true, "rule": {"id": "string", "name": "string", "severity": "string", "source": "string"}, "success": true}]|
  
Example output:

```
{
  "query_results": [
    {
      "error": "string",
      "execution_time": 0,
      "external_errors": [
        "string"
      ],
      "query": {
        "name": "string",
        "severity": "string",
        "source": "string"
      },
      "success": true
    }
  ],
  "rule_results": [
    {
      "error": "string",
      "execution_time": 0,
      "external_errors": [
        "string"
      ],
      "matched": true,
      "rule": {
        "id": "string",
        "name": "string",
        "severity": "string",
        "source": "string"
      },
      "success": true
    }
  ]
}
```

#### Create Message

This action is used to create a new message.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|message|object|None|True|The message object to be created.|None|{'subject': 'Test Message', 'body': 'This is a test message.', 'sender': 'test@example.com', 'recipients': ['recipient@example.com']}|None|None|
  
Example input:

```
{
  "message": {
    "body": "This is a test message.",
    "recipients": [
      "recipient@example.com"
    ],
    "sender": "test@example.com",
    "subject": "Test Message"
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message_id|string|False|The ID of the created message.|12345|
  
Example output:

```
{
  "message_id": 12345
}
```

#### Retrieve Message

This action is used to retrieve a message by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|message_id|string|None|True|The ID of the message to be retrieved.|None|12345|None|None|
  
Example input:

```
{
  "message_id": 12345
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|object|False|The retrieved message object.|{'subject': 'Test Message', 'body': 'This is a test message.', 'sender': 'test@example.com', 'recipients': ['recipient@example.com']}|
  
Example output:

```
{
  "message": {
    "body": "This is a test message.",
    "recipients": [
      "recipient@example.com"
    ],
    "sender": "test@example.com",
    "subject": "Test Message"
  }
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**query_results**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|error|string|None|False|None|None|
|execution_time|integer|None|False|None|None|
|external_errors|[]string|None|False|None|None|
|query|query|None|False|None|None|
|success|boolean|None|False|None|None|
  
**query**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|False|None|None|
|severity|string|None|False|None|None|
|source|string|None|False|None|None|
  
**rule_results**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|error|string|None|False|None|None|
|execution_time|integer|None|False|None|None|
|external_errors|[]string|None|False|None|None|
|matched|boolean|None|False|None|None|
|rule|rule|None|False|None|None|
|success|boolean|None|False|None|None|
  
**rule**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|False|None|None|
|name|string|None|False|None|None|
|severity|string|None|False|None|None|
|sources|string|None|False|None|None|
  
**queries**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|False|None|None|
|severity|string|None|False|None|None|
|source|string|None|False|None|None|
  
**rules**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|active|boolean|None|False|None|None|
|feed_id|string|None|False|None|None|
|name|string|None|False|None|None|
|severity|string|None|False|None|None|
|source|string|None|False|None|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 0.1.0 - Initial Plugin

# Links

* [Sublime Security API](https://docs.sublimesecurity.com/reference/introduction)

## References

* [Sublime Security](https://www.sublimesecurity.com/)