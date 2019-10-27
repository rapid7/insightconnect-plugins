# Rapid7 InsightIDR

## About

[Rapid7 InsightIDR](https://www.rapid7.com/products/insightidr/) is an intruder analytics solution that gives you the confidence to detect and investigate security incidents faster.

## Actions

### Add Indicators to a Threat

This action is used to add InsightIDR threat indicators to a threat with the given threat key.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain_names|[]string|None|False|Domain names to add. e.g. ["rapid7.com","google.com"]|None|
|hashes|[]string|None|False|Process hashes to add. e.g. ["A94A8FE5CCB19BA61C4C0873D391E987982FBBD3","C3499C2729730A7F807EFB8676A92DCB6F8A3F8F"]|None|
|ips|[]string|None|False|IP addresses to add. e.g. ["10.0.0.1","10.0.0.2"]|None|
|key|string|None|True|The key of a threat for which the indicators are going to be added. e.g. c9404e11-b81a-429d-9400-05c531f229c3|None|
|urls|[]string|None|False|URL's to add. e.g. ["https://example.com","https://test.com"]|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rejected_indicators|[]string|False|The list of indicators that have been rejected during the update|
|threat|threat|False|The information about the threat|

Example output:

```
{
  "rejected_indicators": [
    "https://example.com",
    "https://test.com"
  ],
  "threat": {
    "name": "Contributing Collaborative Threat: Flagged Malicious",
    "published": false,
    "indicator_count": 13
  }
}
```

### List Investigations

This action is used to retrieve a page of investigations matching the given request parameters. The investigations will always be sorted by investigation created time in descending order.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|end_time|date|None|False|An optional ISO formatted timestamp. Only investigations whose createTime is before this date will be returned by the api. If this parameter is omitted investigations with any created time may be returned|None|
|index|integer|0|True|The optional zero based index of the page to retrieve. Must be an integer greater than or equal to zero|None|
|size|integer|20|True|The optional size of the page to retrieve. Must be an integer greater than zero or less then or equal to 1000|None|
|start_time|date|None|False|An optional ISO formatted timestamp. Only investigations whose created time is after this date will be returned by the API. If this parameter is omitted investigations with any created time may be returned|None|
|statuses|string|CLOSED|False|An optional comma separated set of investigation statuses. Only investigation whose status match one of the entries in the list will be returned. If this parameter is omitted investigations with any status may be returned|['OPEN', 'CLOSED', 'EITHER']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|investigations|[]investigation|True|A list of found investigations|
|metadata|investigation_metadata|True|The pagination parameters used to generate this page result|

Example output:

```
{
  "investigations": [
    {
      "id": "22b92896-392e-43f6-b595-a6ae58b130ef",
      "title": "test",
      "status": "OPEN",
      "source": "MANUAL",
      "assignee": {
        "name": "example",
        "email": "test@example.com"
      },
      "alerts": [],
      "created_time": "2019-06-04T15:38:11.358Z"
    },
    {
      "id": "2c6b7745-80c1-487f-a743-8983f78a7f5e",
      "title": "Test",
      "status": "CLOSED",
      "source": "MANUAL",
      "alerts": [],
      "created_time": "2019-05-23T19:27:55.813Z"
    }
  ],
  "metadata": {
    "index": 0,
    "size": 20,
    "total_pages": 1,
    "total_data": 2
  }
}
```

### Set Status of Investigation Action

This action is used to set the status of the investigation with the given ID.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|The ID of the investigation to change the status of|None|
|status|string|EITHER|True|The new status for the investigation |['OPEN', 'CLOSED']|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|investigation|investigation|True|The investigation for which the status was set|

Example output:

```
{
  "investigation": {
    "id": "22b92896-392e-43f6-b595-a6ae58b130ef",
    "title": "test",
    "status": "CLOSED",
    "source": "MANUAL",
    "assignee": {
      "name": "example",
      "email": "test@example.com"
    },
    "alerts": [],
    "created_time": "2019-06-04T15:38:11.358Z"
  }
}
```

## Triggers

_This plugin does not contain any triggers._

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|The API key for InsightAppSec|None|
|url|string|https://us.api.insight.rapid7.com|True|The URL endpoint for InsightAppSec. e.g. https://<REGION_CODE>.api.insight.rapid7.com|None|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

## Workflows

Examples:

* Close investigations

## Versions

* 1.0.0 - Initial plugin
* 1.1.0 - New Action Add Indicators to a Threat

## References

* [Rapid7 InsightIDR](https://www.rapid7.com/products/insightidr/)

## Custom Output Types

### investigation_metadata

|Name|Type|Required|Description|
|----|----|--------|-----------|
|index|integer|False|The 0 based index of the page retrieved|
|size|integer|False|The size of the page requested|
|total_data|integer|False|The total number of results available with the given filter parameters|
|total_pages|integer|False|The total number of pages available with the given filter parameters|

### alerts

|Name|Type|Required|Description|
|----|----|--------|-----------|
|first_event_time|string|False|The time the first event involved in this alert occurred|
|type|string|False|The alert's type|
|type_description|string|False|An optional description of this type of alert|

### assignee

|Name|Type|Required|Description|
|----|----|--------|-----------|
|email|string|False|The email of the assigned user|
|name|string|False|The name of the assigned user|

### investigation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alerts|alerts|False|The alerts involved in this investigation if any|
|assignee|assignee|False|The user assigned to this investigation if any|
|created_time|string|False|The time the investigation was created as an ISO formatted timestamp|
|id|string|False|The ID of the investigation|
|source|string|False|The source of this investigation|
|status|string|False|The status of the investigations|
|title|string|False|The investigation's title|

### threat

|Name|Type|Required|Description|
|----|----|--------|-----------|
|indicator_count|integer|False|The number of indicators in this threat|
|name|string|False|The name of the threat|
|note|string|False|Notes about this threat|
|published|boolean|False|Indicates whether this threat has been published|