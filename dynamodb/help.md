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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|access_key|credential_secret_key|None|True|Access key ID|None|
|secret_key|credential_secret_key|None|True|Secret access key|None|
|region|string|None|False|Region|None|

## Technical Details

### Actions

#### Insert

This action will insert the provided data into the specified table.

Optionally, you can specify a ConditionExpression which can prevent Dynamo from accepting writes if the conditions
are met. For example, if you had a primary key of "myid", you could set this to "attribute_not_exist(myid)" to reject
the insert if a key with the same value as this object already existed. Otherwise, the default behvior of Dynamo is to
overwrite the existing record.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|condition_expression|string|None|False|An optional expression that can be used to reject inserts based on evaluating existing data|None|
|table|string|None|True|The table name to store into|None|
|data|object|None|True|The object data to store|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|None|

#### Update

This action will upset the provided data under the specified key (or key pair) for a given table.
Optionally, you can specify a ConditionExpression which can prevent Dynamo from accepting writes if the conditions
are met.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|condition_expression|string|None|False|An optional expression that can be used to reject updates based on evaluating existing data|None|
|table|string|None|True|The table name to store into|None|
|data|object|None|True|The object data to update, as key/value pairs|None|
|key|object|None|True|The primary key and optionally the sort key of the object to update. Provided as a pair of key/values|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|None|

#### Scan

This action will scan the provided table using the metrics you give it to look up any matching data.
Optionally, you can provide the name of an index which can be used in lieu of performing a full scan
It will return the list of objects found, and a count of the records.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|table|string|None|True|The table name to search|None|
|params|object|None|True|The params to query with, as key/value pairs|None|
|index|string|None|False|The index to use. If empty, defaults to a full Scan of the table|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|int|False|None|
|records|array|False|None|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Any situation in which you provide a ConditionExpression and it causes the job to fail, will fail the workflow by default.

# Version History

* 1.0.3 - New spec and help.md format for the Hub
* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - Set `params` input in Scan action to not required
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.2 - Clean up unsatisfactory debugging message
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Dynamo Developer Resources](https://aws.amazon.com/dynamodb/developer-resources/)
* [Dynamo Condition Expression Guide](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html#ConditionExpressionReference)

