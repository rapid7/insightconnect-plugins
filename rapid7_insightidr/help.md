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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|InsightIDR API key|None|4472f2g7-991z-4w70-li11-7552w8qm0266|
|url|string|https://us.api.insight.rapid7.com|True|The URL endpoint for InsightIDR. e.g. https://<REGION_CODE>.api.insight.rapid7.com|None|https://us.api.insight.rapid7.com|

Example input:

```
{
  "api_key": "4472f2g7-991z-4w70-li11-7552w8qm0266",
  "url": "https://us.api.insight.rapid7.com"
}
```

## Technical Details

### Actions

#### Set Status of Investigation

This action is used to set the status of the investigation by the Investigation ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|The ID of the investigation to change the status of|None|174e4f99-2ac7-4481-9301-4d24c34baf06|
|status|string|CLOSED|True|The new status for the investigation|['OPEN', 'CLOSED']|CLOSED|

Example input:

```
{
  "id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
  "status": "CLOSED"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|investigation|investigation|True|The investigation for which the status was set|

Example output:

```
{
  "investigation": {
    "id": "13d353b2-8939-468d-97df-d707d0e262b6",
    "title": "Test Investigation",
    "status": "OPEN",
    "source": "MANUAL",
    "assignee": {
      "name": "Example User",
      "email": "user@example.com"
    },
    "alerts": [],
    "created_time": "2020-08-12T13:40:18.718Z"
  }
}
```

#### Assign User to Investigation

This action is used to assign a user to the specified investigation.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Investigation ID|None|174e4f99-2ac7-4481-9301-4d24c34baf06|
|user_email_address|string|None|True|The email address of the user to assign to this investigation, used to log into the insight platform|None|user@example.com|

Example input:

```
{
  "id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
  "user_email_address": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|investigation|investigation|True|The investigation that was modified|
|success|boolean|True|Was the user assigned successfully|

Example output:

```
{
  "success": true,
  "investigation": {
    "id": "13d353b2-8939-468d-97df-d707d0e262b6",
    "title": "Test Investigation",
    "status": "OPEN",
    "source": "MANUAL",
    "assignee": {
      "name": "Example User",
      "email": "user@example.com"
    },
    "alerts": [],
    "created_time": "2020-08-12T13:40:18.718Z"
  }
}
```

#### Add Indicators to a Threat

This action is used to add InsightIDR threat indicators to a threat with the given threat key.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|domain_names|[]string|None|False|Domain names to add. e.g. ["rapid7.com","google.com"]|None|["rapid7.com", "google.com"]|
|hashes|[]string|None|False|Process hashes to add. e.g. ["A94A8FE5CCB19BA61C4C0873D391E987982FBBD3","C3499C2729730A7F807EFB8676A92DCB6F8A3F8F"]|None|["A94A8FE5CCB19BA61C4C0873D391E987982FBBD3", "C3499C2729730A7F807EFB8676A92DCB6F8A3F8F"]|
|ips|[]string|None|False|IP addresses to add. e.g. ["10.0.0.1","10.0.0.2"]|None|["10.0.0.1", "10.0.0.2"]|
|key|string|None|True|The key of a threat for which the indicators are going to be added. e.g. c9404e11-b81a-429d-9400-05c531f229c3|None|c9404e11-b81a-429d-9400-05c531f229c3|
|urls|[]string|None|False|URL's to add. e.g. ["https://example.com","https://test.com"]|None|["https://example.com", "https://test.com"]|

Example input:

```
{
  "domain_names": [
    "rapid7.com",
    "google.com"
  ],
  "hashes": [
    "A94A8FE5CCB19BA61C4C0873D391E987982FBBD3",
    "C3499C2729730A7F807EFB8676A92DCB6F8A3F8F"
  ],
  "ips": [
    "10.0.0.1",
    "10.0.0.2"
  ],
  "key": "c9404e11-b81a-429d-9400-05c531f229c3",
  "urls": [
    "https://example.com",
    "https://test.com"
  ]
}
```

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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|end_time|date|None|False|An optional-ISO formatted timestamp. Only investigations whose createTime is before this date will be returned by the API. If this parameter is omitted investigations with any create_time may be returned|None|2020-06-01T12:11:13+05:30|
|index|integer|0|True|The optional zero-based index of the page to retrieve. Must be an integer greater than or equal to 0|None|0|
|size|integer|1000|True|The optional size of the page to retrieve. Must be an integer greater than 0 or less than or equal to 1000. Default value is 1000|None|1000|
|start_time|date|None|False|An optional ISO-formatted timestamp. Only investigations whose createTime is after this date will be returned by the API. If this parameter is omitted investigations with any create_time may be returned|None|2020-06-01T12:11:13+05:30|
|statuses|string|CLOSED|True|An optional-comma separated set of investigation statuses. Only the investigation whose status matches one of the entries in the list will be returned. If this parameter is omitted investigations with any status may be returned|['OPEN', 'CLOSED', 'EITHER']|CLOSED|

Example input:

```
{
  "end_time": "2020-06-01T12:11:13+05:30",
  "index": 0,
  "size": 1000,
  "start_time": "2020-06-01T12:11:13+05:30",
  "statuses": "CLOSED"
}
```

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
        "email": "user@example.com"
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

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.2.1 - Change default value in the `size` input parameter to 1000 in List Investigations action
* 1.2.0 - New Action Assign User to Investigation
* 1.1.1 - New spec and help.md format for the Extension Library
* 1.1.0 - New Action Add Indicators to a Threat
* 1.0.0 - Initial plugin

# Links

## References

* [Rapid7 InsightIDR](https://www.rapid7.com/products/insightidr/)
