# Description

Do more with Investigations in [InsightIDR](https://www.rapid7.com/products/insightidr/) with the InsightConnect plugin. Add indicators to a threat or view the status of an investigation to drive accuracy and faster time to resolutions for your detections.

# Key Features

* Set status of investigation
* Add indicators
* List investigations

# Requirements

* Requires an API Key from the Insight platform

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|The API key for InsightAppSec|None|
|url|string|https://us.api.insight.rapid7.com|True|The URL endpoint for InsightAppSec. e.g. https://<REGION_CODE>.api.insight.rapid7.com|None|

## Technical Details

### Actions

#### Add Indicators to a Threat

This action is used to add InsightIDR threat indicators to a threat with the given threat key.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain_names|[]string|None|False|Domain names to add. e.g. ["rapid7.com","google.com"]|None|
|hashes|[]string|None|False|Process hashes to add. e.g. ["A94A8FE5CCB19BA61C4C0873D391E987982FBBD3","C3499C2729730A7F807EFB8676A92DCB6F8A3F8F"]|None|
|ips|[]string|None|False|IP addresses to add. e.g. ["10.0.0.1","10.0.0.2"]|None|
|key|string|None|True|The key of a threat for which the indicators are going to be added. e.g. c9404e11-b81a-429d-9400-05c531f229c3|None|
|urls|[]string|None|False|URL's to add. e.g. ["https://example.com","https://test.com"]|None|

##### Output

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

#### List Investigations

This action is used to retrieve a page of investigations matching the given request parameters. The investigations will always be sorted by investigation created time in descending order.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|end_time|date|None|False|An optional ISO formatted timestamp. Only investigations whose createTime is before this date will be returned by the api. If this parameter is omitted investigations with any created time may be returned|None|
|index|integer|0|True|The optional zero based index of the page to retrieve. Must be an integer greater than or equal to zero|None|
|size|integer|20|True|The optional size of the page to retrieve. Must be an integer greater than zero or less then or equal to 1000|None|
|start_time|date|None|False|An optional ISO formatted timestamp. Only investigations whose created time is after this date will be returned by the API. If this parameter is omitted investigations with any created time may be returned|None|
|statuses|string|CLOSED|False|An optional comma separated set of investigation statuses. Only investigation whose status match one of the entries in the list will be returned. If this parameter is omitted investigations with any status may be returned|['OPEN', 'CLOSED', 'EITHER']|

##### Output

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

#### Set Status of Investigation Action

This action is used to set the status of the investigation with the given ID.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|id|string|None|True|The ID of the investigation to change the status of|None|
|status|string|EITHER|True|The new status for the investigation |['OPEN', 'CLOSED']|

##### Output

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

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.1.1 - New spec and help.md format for the Hub
* 1.1.0 - New Action Add Indicators to a Threat
* 1.0.0 - Initial plugin

# Links

## References

* [Rapid7 InsightIDR](https://www.rapid7.com/products/insightidr/)

