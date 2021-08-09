# Description

[Dynamo DB](https://aws.amazon.com/dynamodb/) is a key/value store powered by Amazon available for members
of AWS. It provides an easy-to-use and scalable system that exposes some basic indexing and querying capabilities,
making it a versatile and convenient way to store data. Users can manage their data using the DynamoDB plugin for
Rapid7 InsightConnect.

# Key Features

* Scan data
* Store data
* Update data

# Requirements

* Access key
* Secret key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|access_key|credential_secret_key|None|True|Access key ID|None|602B2EA0A04B66BEB2C0|
|region|string|None|False|Region|None|us-east-2|
|secret_key|credential_secret_key|None|True|Secret access key|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "access_key": "602B2EA0A04B66BEB2C0",
  "region": "us-east-2",
  "secret_key": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

## Technical Details

### Actions

#### Insert

This action will insert the provided data into the specified table.

Optionally, you can specify a ConditionExpression which can prevent Dynamo from accepting writes if the conditions
are met. For example, if you had a primary key of "myid", you could set this to "attribute_not_exist(myid)" to reject
the insert if a key with the same value as this object already existed. Otherwise, the default behavior of Dynamo is to
overwrite the existing record.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|condition_expression|string|None|False|An optional expression that can be used to reject inserts based on evaluating existing data|None|keytable<>user|
|data|object|None|True|The object data to store|None|{"keytable": "login", "e-mail": "user@example.com", "user": "Username"}|
|table|string|None|True|The table name to store into|None|Table-name|

Example input:

```
{
  "condition_expression": "keytable<>user",
  "data": {
    "keytable": "login",
    "e-mail": "user@example.com",
    "user": "Username"
  },
  "table": "Table-name"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Success|

Example output:

```
{
  "success": true
}
```

#### Update

This action will upset the provided data under the specified key (or key pair) for a given table.
Optionally, you can specify a ConditionExpression which can prevent Dynamo from accepting writes if the conditions
are met.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|condition_expression|string|None|False|An optional expression that can be used to reject updates based on evaluating existing data|None|keytable<>user|
|data|object|None|True|The object data to update, as key/value pairs|None|{"e-mail": "user2@example.com", "user": "Username2"}|
|key|object|None|True|The primary key and optionally the sort key of the object to update. Provided as a pair of key/values|None|{"keytable": "login"}|
|table|string|None|True|The table name to store into|None|Table-name|

Example input:

```
{
  "condition_expression": "keytable<>user",
  "data": {
    "e-mail": "user2@example.com",
    "user": "Username2"
    },
  "key": {
  "keytable": "login"
  },
  "table": "Table-name"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Success|

Example output:

```
{
  "success": true
}
```

#### Scan

This action will scan the provided table using the metrics you give it to look up any matching data.
Optionally, you can provide the name of an index which can be used in lieu of performing a full scan
It will return the list of objects found, and a count of the records.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|index|string|None|False|The index to use. If empty, defaults to a full Scan of the table|None|index-name|
|params|object|None|False|The params to query with, as key/value pairs|None|{"email": "user@example.com"}|
|table|string|None|True|The table name to search|None|Table-name|

Example input:

```
{
  "index": "index-name",
  "params": {
    "email": "user@example.com"
    },
  "table": "Table-name"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Count|integer|True|Items count|
|Items|[]object|True|Database items|
|ResponseMetadata|ResponseMetadata|False|Response metadata|
|ScannedCount|integer|False|Scanned count|

Example output:

```
{
  "response": {
    "Items": [
      {
        "e-mail": "user@example.com",
        "user": "Username",
        "keytable": "login"
      }
    ],
    "Count": 1,
    "ScannedCount": 2,
    "ResponseMetadata": {
      "RequestId": "b42ec8b47deb2dc75edebd01132d63f8e8d4cd08e5d26d8bd366",
      "HTTPStatusCode": 200,
      "HTTPHeaders": {
        "server": "Server",
        "date": "Sun, 25 Jul 2021 20:46:19 GMT",
        "content-type": "application/x-amz-json-1.0",
        "content-length": "130",
        "connection": "keep-alive",
        "x-amzn-requestid": "b42ec8b47deb2dc75edebd01132d63f8e8d4cd08e5d26d8bd366",
        "x-amz-crc32": "1592874513"
      },
      "RetryAttempts": 0
    }
  }
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Any situation in which you provide a ConditionExpression and it causes the job to fail, will fail the workflow by default.

# Version History

* 2.0.0 - Create custom output type for Scan action | Add example inputs and outputs
* 1.0.3 - Correct spelling in help.md
* 1.0.2 - New spec and help.md format for the Extension Library | Add missing title values for actions in plugin.spec.yaml
* 1.0.1 - Set `params` input in Scan action to not required
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.2 - Clean up unsatisfactory debugging message
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Dynamo Developer Resources](https://aws.amazon.com/dynamodb/developer-resources/)
* [Dynamo Condition Expression Guide](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html#ConditionExpressionReference)
