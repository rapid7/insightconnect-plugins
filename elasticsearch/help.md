# Description

[Elasticsearch](https://www.elastic.co) is a distrbuted real-time search and analytics engine. This plugin allows for indexing and updating documents, as well as searching indexes and polling for new documents given a query. The Elasticsearch plugin will allow you to update and search documents. It will also allow you to check your cluster's health. 
This plugin utilizes the [Elasticsearch API](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html). 

# Key Features

* Search documents
* Update documents
* Check your cluster's health

# Requirements

* An Elasticsearch server
* Elasticsearch credentials

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|Host URL E.g. http\://10.0.2.2\:9200|None|
|credentials|credential_username_password|None|True|Basic Auth username and password|None|
|use_authentication|boolean|None|True|If the Elasticsearch host does not use authentication set this value to false|None|

## Technical Details

### Actions

#### Cluster Health

This action is used to check cluster health.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cluster_health|health|False|None|

#### Update Document

This action is used to update a document.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|_type|string|None|True|Type of Document to Index|None|
|retry_on_conflict|integer|None|False|Optional Number of Times to Retry on Update Conflict|None|
|parent|string|None|False|Optional Parent|None|
|_index|string|None|True|Index to Insert Document Into|None|
|_source|string|None|False|Control If and How Source is Returned|None|
|_version|integer|None|False|Optional Version Specification|None|
|refresh|string|false|False|Control when Changes Become Visible|['true', 'wait_for', 'false']|
|script|object|None|True|JSON Script to Modify a Document|None|
|wait_for_active_shards|integer|None|False|Number of Shard Copies required Before Update|None|
|routing|string|None|False|Optional Shard Placement|None|
|timeout|string|1m|False|Custom Timeout Window|None|
|_id|string|None|True|Optional ID of Indexed Document|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|update_response|op_response|False|None|

#### Search Documents

This action is used to search for documents.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|object|None|False|JSON Query DSL|None|
|_type|string|None|True|Document Type|None|
|routing|string|None|False|Optional Shards to Search|None|
|_index|string|None|True|Document Index|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|hits|hits|False|Information About Hits|
|took|integer|False|Duration in Milliseconds|
|timed_out|boolean|False|Timed Out Flag|
|_shards|_shards|False|Information About Replication Process|

#### Index Document

This action is used to create or replace a document by index.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|_type|string|None|True|Type of Document to Index|None|
|_id|string|None|False|Optional ID of Indexed Document|None|
|parent|string|None|False|Optional Parent|None|
|version_type|string|internal|False|Optional Version Type|['internal', 'external', 'external_gt', 'external_gte']|
|_index|string|None|True|Index to Insert Document Into|None|
|_version|integer|None|False|Optional Version Specification|None|
|routing|string|None|False|Optional Shard Placement|None|
|timeout|string|1m|False|Custom Timeout Window|None|
|document|object|None|False|JSON Document to Index|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|index_response|op_response|False|None|

### Triggers

#### Poll Documents

This trigger is used to poll for new documents given a query.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|query|object|None|False|JSON Query DSL|None|
|_type|string|None|True|Document Type|None|
|frequency|integer|60|False|Poll frequency in seconds|None|
|routing|string|None|False|Optional Shards to Search|None|
|_index|string|None|True|Document Index|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|hits|[]hit|False|New Hits|

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.2 - New spec and help.md format for the Hub
* 2.0.1 - Fix typo in plugin spec
* 2.0.0 - Fix issue where Poll Documents trigger will sometimes not return results | Update connection to allow optional authentication
* 1.0.1 - Fix issue where Poll Documents trigger test would always fail
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.2 - SSL bug fix in SDK
* 0.1.1 - Bugfix for NoneType assignment
* 0.1.0 - Initial plugin

# Links

## References

* [ElasticSearch](https://www.elastic.co/)
* [ElasticSearch API](https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html)

