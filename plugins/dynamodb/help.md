# Description

[Dynamo DB](https://aws.amazon.com/dynamodb/) is a key/value store powered by Amazon available for members of AWS. It provides an easy-to-use and scalable system that exposes some basic indexing and querying capabilities, making it a versatile and convenient way to store data. Users can manage their data using the DynamoDB plugin for Rapid7 InsightConnect

# Key Features

* Scan data
* Store data
* Update data

# Requirements

* Access key
* Secret key

# Supported Product Versions

* Amazon DynamoDB 2024-02-27

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|access_key|credential_secret_key|None|True|Access key ID|None|602B2EA0A04B66BEB2C0|None|None|
|region|string|us-east-1|False|Region|None|us-east-1|None|None|
|secret_key|credential_secret_key|None|True|Secret access key|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|

Example input:

```
{
  "access_key": "602B2EA0A04B66BEB2C0",
  "region": "us-east-1",
  "secret_key": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

## Technical Details

### Actions


#### Get Item

This action is used to return a set of attributes for the item with the given primary key

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|consistent_read|boolean|None|False|Determines the read consistency model; If set to true, then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads|None|True|None|None|
|expression_attribute_names|object|None|False|One or more substitution tokens for attribute names in an expression|None|{"#P":"Percentile"}|None|None|
|key|object|None|True|A map of attribute names to AttributeValue objects, representing the primary key of the item to retrieve|None|{"CustomerID": {"S":"12345"}}|None|None|
|projection_expression|string|None|False|A string that identifies one or more attributes to retrieve from the specified table or index|None|Description|None|None|
|return_consumed_capacity|string|TOTAL|False|Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response|["NONE", "INDEXES", "TOTAL"]|TOTAL|None|None|
|table_name|string|None|True|The table name to search|None|Table-name|None|None|
  
Example input:

```
{
  "consistent_read": true,
  "expression_attribute_names": {
    "#P": "Percentile"
  },
  "key": {
    "CustomerID": {
      "S": "12345"
    }
  },
  "projection_expression": "Description",
  "return_consumed_capacity": "TOTAL",
  "table_name": "Table-name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|item|object|True|Output item|{"ClientID": {"S": "2"}}|
  
Example output:

```
{
  "item": {
    "ClientID": {
      "S": "2"
    }
  }
}
```

#### Insert
  
This action is used to add the provided data into the specified table.

Optionally, you can specify a 
ConditionExpression which can prevent Dynamo from accepting writes if the conditions are met. For example, if you had a 
primary key of 'myid', you could set this to 'attribute_not_exist(myid)' to reject the insert if a key with the same 
value as this object already existed. Otherwise, the default behavior of Dynamo is to overwrite the existing record

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|condition_expression|string|None|False|An optional expression that can be used to reject inserts based on evaluating existing data|None|keytable<>user|None|None|
|expression_attribute_names|object|None|False|One or more substitution tokens for attribute names in an expression|None|{"#P":"Percentile"}|None|None|
|expression_attribute_values|object|None|False|One or more values that can be substituted in an expression|None|{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} }|None|None|
|item|object|None|True|The object data to store|None|{"keytable": "login", "e-mail": "user@example.com", "user": "Username"}|None|None|
|return_consumed_capacity|string|TOTAL|False|Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response|["NONE", "INDEXES", "TOTAL"]|TOTAL|None|None|
|return_item_collection_metrics|boolean|None|False|Determines whether item collection metrics are returned|None|False|None|None|
|return_values|boolean|None|False|Use ReturnValues if you want to get the item attributes as they appeared before they were updated with the PutItem request|None|False|None|None|
|table_name|string|None|True|The table name to store into|None|Table-name|None|None|
  
Example input:

```
{
  "condition_expression": "keytable<>user",
  "expression_attribute_names": {
    "#P": "Percentile"
  },
  "expression_attribute_values": {
    ":avail": {
      "S": "Available"
    },
    ":back": {
      "S": "Backordered"
    },
    ":disc": {
      "S": "Discontinued"
    }
  },
  "item": {
    "e-mail": "user@example.com",
    "keytable": "login",
    "user": "Username"
  },
  "return_consumed_capacity": "TOTAL",
  "return_item_collection_metrics": false,
  "return_values": false,
  "table_name": "Table-name"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Success|True|
  
Example output:

```
{
  "success": true
}
```

#### Scan

This action is used to scan the provided table using the metrics you give it to look up any matching data

Optionally, 
you can provide the name of an index which can be used in lieu of performing a full scan.
It will return the list of 
objects found, and a count of the records

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|consistent_read|boolean|None|False|Value that determines the read consistency model during the scan|None|False|None|None|
|exclusive_start_key|object|None|False|The primary key of the first item that this operation will evaluate. Follows AttributeValue formatting, please refer to https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.scan|None|{"email": {"S": "user@example.com"}}|None|None|
|expression_attribute_names|object|None|False|One or more substitution tokens for attribute names in an expression|None|{"#P":"Percentile"}|None|None|
|expression_attribute_values|object|None|False|One or more values that can be substituted in an expression|None|{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} }|None|None|
|filter_expression|string|None|False|A string that contains conditions that DynamoDB applies after the Scan operation|None|test = :test|None|None|
|index_name|string|None|False|The index to use. If empty, defaults to a full Scan of the table|None|index-name|None|None|
|limit|integer|100|False|The maximum number of items to evaluate (not necessarily the number of matching items)|None|100|None|None|
|projection_expression|string|None|False|A string that identifies one or more attributes to retrieve from the specified table or index|None|Description|None|None|
|return_consumed_capacity|string|TOTAL|False|Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response|["NONE", "INDEXES", "TOTAL"]|TOTAL|None|None|
|segment|integer|None|False|For a parallel Scan request, Segment identifies an individual segment to be scanned by an application worker|None|100|None|None|
|select|string|ALL_ATTRIBUTES|False|The attributes to be returned in the result|["ALL_ATTRIBUTES", "ALL_PROJECTED_ATTRIBUTES", "COUNT", "SPECIFIC_ATTRIBUTES"]|ALL_ATTRIBUTES|None|None|
|table_name|string|None|True|The table name to search|None|Table-name|None|None|
|total_segments|integer|None|False|For a parallel Scan request, TotalSegments represents the total number of segments into which the Scan operation will be divided|None|100|None|None|
  
Example input:

```
{
  "consistent_read": false,
  "exclusive_start_key": {
    "email": {
      "S": "user@example.com"
    }
  },
  "expression_attribute_names": {
    "#P": "Percentile"
  },
  "expression_attribute_values": {
    ":avail": {
      "S": "Available"
    },
    ":back": {
      "S": "Backordered"
    },
    ":disc": {
      "S": "Discontinued"
    }
  },
  "filter_expression": "test = :test",
  "index_name": "index-name",
  "limit": 100,
  "projection_expression": "Description",
  "return_consumed_capacity": "TOTAL",
  "segment": 100,
  "select": "ALL_ATTRIBUTES",
  "table_name": "Table-name",
  "total_segments": 100
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|Count|integer|True|Items count|1|
|Items|[]object|True|Database items|[{"e-mail":"user@example.com","user":"Username","keytable":"login"}]|
|ResponseMetadata|ResponseMetadata|False|Response metadata|{"RequestId":"b42ec8b47deb2dc75edebd01132d63f8e8d4cd08e5d26d8bd366","HTTPStatusCode":200,"HTTPHeaders":{"server":"Server","date":"Sun, 25 Jul 2021 20:46:19 GMT","content-type":"application/x-amz-json-1.0","content-length":"130","connection":"keep-alive","x-amzn-requestid":"b42ec8b47deb2dc75edebd01132d63f8e8d4cd08e5d26d8bd366","x-amz-crc32":"1592874513"},"RetryAttempts":0}|
|ScannedCount|integer|False|Scanned count|2|
  
Example output:

```
{
  "Count": 1,
  "Items": [
    {
      "e-mail": "user@example.com",
      "keytable": "login",
      "user": "Username"
    }
  ],
  "ResponseMetadata": {
    "HTTPHeaders": {
      "connection": "keep-alive",
      "content-length": "130",
      "content-type": "application/x-amz-json-1.0",
      "date": "Sun, 25 Jul 2021 20:46:19 GMT",
      "server": "Server",
      "x-amz-crc32": "1592874513",
      "x-amzn-requestid": "b42ec8b47deb2dc75edebd01132d63f8e8d4cd08e5d26d8bd366"
    },
    "HTTPStatusCode": 200,
    "RequestId": "b42ec8b47deb2dc75edebd01132d63f8e8d4cd08e5d26d8bd366",
    "RetryAttempts": 0
  },
  "ScannedCount": 2
}
```

#### Update

This action is used to update an object in DynamoDB

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|condition_expression|string|None|False|An optional expression that can be used to reject updates based on evaluating existing data|None|keytable<>user|None|None|
|expression_attribute_names|object|None|False|One or more substitution tokens for attribute names in an expression|None|{"#P":"Percentile"}|None|None|
|expression_attribute_values|object|None|False|One or more values that can be substituted in an expression|None|{ ":avail":{"S":"Available"}, ":back":{"S":"Backordered"}, ":disc":{"S":"Discontinued"} }|None|None|
|key|object|None|True|The primary key and optionally the sort key of the object to update. Provided as a pair of key/values|None|{"keytable": "login"}|None|None|
|return_consumed_capacity|string|TOTAL|False|Determines the level of detail about either provisioned or on-demand throughput consumption that is returned in the response|["NONE", "INDEXES", "TOTAL"]|TOTAL|None|None|
|return_item_collection_metrics|boolean|None|False|Determines whether item collection metrics are returned|None|False|None|None|
|return_values|string|NONE|False|Use ReturnValues if you want to get the item attributes as they appear before or after they are updated|["NONE", "ALL_OLD", "UPDATE_OLD", "ALL_NEW", "UPDATED_NEW"]|ALL_OLD|None|None|
|table_name|string|None|True|The table name to store into|None|Table-name|None|None|
|update_expression|string|None|False|An expression that defines one or more attributes to be updated, the action to be performed on them, and new values for them|None|SET #Y = :y, #AT = :t|None|None|
  
Example input:

```
{
  "condition_expression": "keytable<>user",
  "expression_attribute_names": {
    "#P": "Percentile"
  },
  "expression_attribute_values": {
    ":avail": {
      "S": "Available"
    },
    ":back": {
      "S": "Backordered"
    },
    ":disc": {
      "S": "Discontinued"
    }
  },
  "key": {
    "keytable": "login"
  },
  "return_consumed_capacity": "TOTAL",
  "return_item_collection_metrics": false,
  "return_values": "NONE",
  "table_name": "Table-name",
  "update_expression": "SET #Y = :y, #AT = :t"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Success|True|
  
Example output:

```
{
  "success": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**HTTPHeaders**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Connection|string|None|False|Connection|None|
|Content-Length|string|None|False|Content-length|None|
|Content-Type|string|None|False|Content-type|None|
|Date|string|None|False|Date|None|
|Server|string|None|False|Server|None|
|X-Amz-Crc32|string|None|False|X-amz-crc32|None|
|X-Amzn-RequestID|string|None|False|X-amzn-requestID|None|
  
**ResponseMetadata**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HTTP Headers|HTTPHeaders|None|False|HTTP headers|None|
|HTTP Status Code|integer|None|False|HTTP status code|None|
|Request ID|string|None|False|Request ID|None|
|Retry Attempts|integer|None|False|Retry attempts|None|


## Troubleshooting

* Any situation in which you provide a ConditionExpression and it causes the job to fail, will fail the workflow by default.

# Version History

* 3.1.2 - Resolved Snyk Vulnerabilities | SDK Bump to 6.3.7
* 3.1.1 - Updated to the latest SDK to address memory usage issues | Updated plugin packages
* 3.1.0 - Add Get Item action
* 3.0.2 - Fix number should be a string for boto3 input bug
* 3.0.1 - Validate exclusive_start_key parameter for Scan action
* 3.0.0 - Create separate class for communication with AWS | Refactor all actions | Fix incompatible types in output in Scan action | Update Python SDK version
* 2.0.0 - Create custom output type for Scan action | Add example inputs and outputs
* 1.0.3 - Correct spelling in help.md
* 1.0.2 - New spec and help.md format for the Extension Library | Add missing title values for actions in plugin.spec.yaml
* 1.0.1 - Set `params` input in Scan action to not required
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.2 - Clean up unsatisfactory debugging message
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

* [Dynamo Developer Resources](https://aws.amazon.com/dynamodb/developer-resources/)

## References

* [Dynamo Developer Resources](https://aws.amazon.com/dynamodb/developer-resources/)
* [Dynamo Condition Expression Guide](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.SpecifyingConditions.html#ConditionExpressionReferenIce)