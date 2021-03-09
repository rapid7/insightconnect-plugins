# Description

[Elasticsearch](https://www.elastic.co) is a distributed real-time search and analytics engine. This plugin allows for indexing and updating documents, as well as searching indexes and polling for new documents given a query. The Elasticsearch plugin will allow you to update and search documents. It will also allow you to check your cluster's health.
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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Basic Auth username and password|None|{"username":"user1", "password":"mypassword"}|
|url|string|None|True|Host URL E.g. http://10.0.2.2:9200|None|http://10.0.2.2:9200|
|use_authentication|boolean|True|True|If the Elasticsearch host does not use authentication set this value to false|None|True|

Example input:

```
{
  "credentials": {
    "username": "user1",
    "password": "mypassword"
  },
  "url": "http://10.0.2.2:9200",
  "use_authentication": true
}
```

## Technical Details

### Actions

#### Cluster Health

This action is used to check cluster health.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|cluster_health|health|False|Cluster Health|

Example output:

```
{
  "cluster_health": {
    "active_primary_shards": 11,
    "discovered_master": true,
    "initializing_shards": 0,
    "active_shards": 11,
    "active_shards_percent_as_number": 52.38095238095239,
    "number_of_nodes": 1,
    "status": "yellow",
    "delayed_unassigned_shards": 0,
    "number_of_in_flight_fetch": 0,
    "number_of_pending_tasks": 0,
    "relocating_shards": 0,
    "task_max_waiting_in_queue_millis": 0,
    "cluster_name": "388488718562:dm-test-es",
    "number_of_data_nodes": 1,
    "timed_out": false,
    "unassigned_shards": 10
  }
}
```

#### Update Document

This action is used to update a document.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|_id|string|None|True|Optional ID of Indexed Document|None|001|
|_index|string|None|True|Index to Insert Document Into|None|index001|
|_source|string|None|False|Control If and How Source is Returned|None|meta.*|
|_type|string|None|False|Type of Document to Index|None|_doc|
|_version|integer|None|False|Optional Version Specification|None|1|
|parent|string|None|False|Optional Parent|None|001|
|refresh|string|false|False|Control when Changes Become Visible|['true', 'wait_for', 'false']|false|
|retry_on_conflict|integer|None|False|Optional Number of Times to Retry on Update Conflict|None|5|
|routing|string|None|False|Optional Shard Placement|None|user1|
|script|object|None|True|JSON Script to Modify a Document|None|{"lang": "painless"}|
|timeout|string|1m|False|Custom Timeout Window|None|1m|
|wait_for_active_shards|integer|None|False|Number of Shard Copies required Before Update|None|2|

Example input:

```
{
  "_id": "001",
  "_index": "index001",
  "_source": "meta.*",
  "_type": "_doc",
  "_version": 1,
  "parent": "001",
  "refresh": "false",
  "retry_on_conflict": 5,
  "routing": "user1",
  "script": {
    "lang": "painless"
  },
  "timeout": "1m",
  "wait_for_active_shards": 2
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|update_response|op_response|False|Updated response|

Example output:

```
{
  "_id": "1",
  "_index": "account",
  "_primary_term": 1,
  "_seq_no": 0,
  "_shards": {
    "successful": 1,
    "total": 2,
    "failed": 0
  },
  "_type": "doc",
  "_version": 1,
  "result": "created"
}
```

#### Search Documents

This action is used to search for documents.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|_index|string|None|True|Document Index|None|shakespeare|
|_type|string|None|False|Document Type|None|doc|
|query|object|None|False|JSON Query DSL|None|{"query": {"match": {"line_number": {"query": "1.1.1"}}}}|
|routing|string|None|False|Optional Shards to Search|None|user1|

Example input:

```
{
  "_index": "shakespeare",
  "_type": "doc",
  "query": {
    "query": {
      "match": {
        "line_number": {
          "query": "1.1.1"
        }
      }
    }
  },
  "routing": "user1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|_shards|_shards|False|Information About Replication Process|
|hits|hits|False|Information About Hits|
|timed_out|boolean|False|Timed Out Flag|
|took|integer|False|Duration in Milliseconds|

Example output:

```
{
  "took": 4,
  "timed_out": false,
  "_shards": {
    "total": 5,
    "successful": 5,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 4.3903255,
    "hits": [
      {
        "_index": "shakespeare",
        "_type": "doc",
        "_id": "3",
        "_version": 1,
        "_score": 4.3903255,
        "_source": {
          "type": "line",
          "line_id": 4,
          "play_name": "Henry IV",
          "speech_number": 1,
          "line_number": "1.1.1",
          "speaker": "KING HENRY IV",
          "text_entry": "So shaken as we are, so wan with care,"
        }
      }
    ]
  }
}
```

#### Index Document

This action is used to create or replace a document by index.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|_id|string|None|False|Optional ID of Indexed Document|None|001|
|_index|string|None|True|Index to Insert Document Into|None|index001|
|_type|string|None|False|Type of Document to Index|None|_doc|
|_version|integer|None|False|Optional Version Specification|None|1|
|document|object|None|False|JSON Document to Index|None|{"firstname": "Jon", "lastname": "Doe", "gender": "M", "city": "Dante"}|
|parent|string|None|False|Optional Parent|None|001|
|routing|string|None|False|Optional Shard Placement|None|user1|
|timeout|string|1m|False|Custom Timeout Window|None|1m|
|version_type|string|internal|False|Optional Version Type|['internal', 'external', 'external_gt', 'external_gte']|internal|

Example input:

```
{
  "_id": "001",
  "_index": "index001",
  "_type": "_doc",
  "_version": 1,
  "document": {
    "firstname": "Jon",
    "lastname": "Doe",
    "gender": "M",
    "city": "Dante"
  },
  "parent": "001",
  "routing": "user1",
  "timeout": "1m",
  "version_type": "internal"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|index_response|op_response|False|Result of Index Operation|

Example output:

```
{
  "_seq_no": 0,
  "_shards": {
    "failed": 0,
    "successful": 1,
    "total": 2
  },
  "_type": "doc",
  "_version": 1,
  "result": "created",
  "_id": "1",
  "_index": "account",
  "_primary_term": 1
}
```

### Triggers

#### Poll Documents

This trigger is used to poll for new documents given a query.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|_index|string|None|True|Document Index|None|bank|
|_type|string|None|False|Document Type|None|doc|
|frequency|integer|60|False|Poll frequency in seconds|None|60|
|query|object|None|False|JSON Query DSL|None|{"query": {"match": {"line_number": {"query": "1.1.1"}}}}|
|routing|string|None|False|Optional Shards to Search|None|account|

Example input:

```
{
  "_index": "bank",
  "_type": "doc",
  "frequency": 60,
  "query": {
    "query": {
      "match": {
        "line_number": {
          "query": "1.1.1"
        }
      }
    }
  },
  "routing": "account"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|hits|[]hit|False|New Hits|

Example output:

```
{
  "hits": [
    {
      "_type": "doc",
      "_version": 1,
      "_id": "3",
      "_index": "shakespeare",
      "_score": 4.3903255,
      "_source": {
        "line_id": 4,
        "line_number": "1.1.1",
        "play_name": "Henry IV",
        "speaker": "KING HENRY IV",
        "speech_number": 1,
        "text_entry": "So shaken as we are, so wan with care,",
        "type": "line"
      }
    }
  ]
}
```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.0.5 - Updated example inputs and outputs for all the actions
* 2.0.4 - Correct spelling in help.md
* 2.0.3 - Updated Search Documents action output schema
* 2.0.2 - New spec and help.md format for the Extension Library
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
