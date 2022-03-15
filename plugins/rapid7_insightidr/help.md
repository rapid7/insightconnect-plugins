# Description

Do more with Investigations in [InsightIDR](https://www.rapid7.com/products/insightidr/) with the InsightConnect plugin. Add indicators to a threat or view the status of an investigation to drive accuracy and faster time to resolutions for your detections.

# Key Features

* Set status of investigation
* Add indicators
* List investigations

# Requirements

* Requires an API Key from the Insight platform

# Supported Product Versions

* Latest release successfully tested on 2021-09-15.

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|InsightIDR API key|None|4472f2g7-991z-4w70-li11-7552w8qm0266|
|url|string|https://example.com|True|The URL endpoint for InsightIDR. e.g. https://<REGION_CODE>.api.insight.rapid7.com|None|https://example.com|

Example input:

```
{
  "api_key": "4472f2g7-991z-4w70-li11-7552w8qm0266",
  "url": "https://us.api.insight.rapid7.com"
}
```

## Technical Details

### Actions

#### Create Threat

This action is used to create a private InsightIDR threat and add indicators to this threat.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|indicators|[]string|None|True|Add indicators to new threat in InsightIDR. Accept IP addresses, process hashes (SHA1, MD5, SHA256), domain names, URLs|None|["example.com", "10.0.0.1"]|
|note_text|string|Threat created via InsightConnect|False|Note text of created threat|None|Threat created via InsightConnect|
|threat_name|string|None|True|Name of created threat|None|Threat created via InsightConnect|

Example input:

```
{
  "indicators": [
    "example.com",
    "10.0.0.1"
  ],
  "note_text": "Threat created via InsightConnect",
  "threat_name": "Threat created via InsightConnect"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rejected_indicators|[]string|True|Rejected indicators in new threat|
|threat|threat|True|The information about the new threat|

Example output:

```
{
    "rejected_indicators": [],
    "threat": {
      "name": "Threat created via InsightConnect",
      "note": "Threat created via InsightConnect",
      "published": false,
      "indicator_count": 2
  }
}
```

#### Advanced Query on Log Set

This action is used to realtime query an InsightIDR log set. This will query entire log sets for results and can accept
a relative or absolute time-range from which to query.

This action should be used when querying a collection of related services.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|log_set|string|None|True|Log Set to search|['Advanced Malware Alert', 'Active Directory Admin Activity', 'Asset Authentication', 'Cloud Service Admin Activity', 'Cloud Service Activity', 'DNS Query', 'Endpoint Activity', 'EndPoint Agent', 'Exploit Mitigation Alert', 'File Access Activity', 'File Modification Activity', 'Firewall Activity', 'Network Flow', 'Host To IP Observations', 'IDS Alert', 'Ingress Authentication', 'Raw Log', 'SSO Authentication', 'Unparsed Data', 'Third Party Alert', 'Virus Alert', 'Web Proxy Activity']|Firewall Activity|
|query|string|None|True|LQL Query|None|where(user=adagentadmin, loose)|
|relative_time|string|Last 5 Minutes|True|A relative time in the past to look for alerts|['Last 5 Minutes', 'Last 10 Minutes', 'Last 20 Minutes', 'Last 30 Minutes', 'Last 45 Minutes', 'Last 1 Hour', 'Last 2 Hours', 'Last 3 Hours', 'Last 6 Hours', 'Last 12 Hours', 'Use Time From Value']|Last 5 Minutes|
|time_from|string|None|False|Beginning date and time for the query. This will be ignored unless Relative Time input is set to 'Use Time From Value'. The format is flexible and will work with simple dates (e.g. 01-01-2020) to full ISO time (e.g. 01-01-2020T00:00:00)|None|01-01-2020T00:00:00|
|time_to|string|None|False|Date and time for the end of the query. If left blank, the current time will be used. The format is flexible and will work with simple dates (e.g. 01-01-2020) to full ISO time (e.g. 01-01-2020T00:00:00)|None|12-31-2020T00:00:00|
|timeout|int|60|True|Time in seconds to wait for the query to return. If exceeded the plugin will throw an error|None|60|

Example input:

```
{
  "log": "Firewall Activity",
  "query": "where(user=adagentadmin, loose)",
  "relative_time": "Last 5 Minutes",
  "time_from": "01-01-2020T00:00:00",
  "time_to": "12-31-2020T00:00:00",
  "timeout": 60
}
```

To use Relative Time, leave `Time From` and `Time To` blank. For example:

```
{
  "relative_time": "Last 5 Minutes",
  "time_from": "",
  "time_to": "",
  ...
}
```

The above settings will run your search from 5 minutes ago until now.

If you want to use absolute time for a query. You can set up the input like this:

```
{
  "relative_time": "Use Time From Value",
  "time_from": "1/1/2021",
  "time_to": "1/31/2021",
  ...
}
```

This will run your search for the entire month of January every time.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|True|Number of log entries found|
|results|[]events|True|Query Results|

Example output:

```
{
  "results": [
    {
      "labels": [],
      "timestamp": 1601598638768,
      "sequence_number": 123456789123456789,
      "log_id": "64z0f0p9-1a99-4501-xe36-a6d03687f313",
      "message": {
        "timestamp": "2020-10-02T00:29:14.649Z",
        "destination_asset": "iagent-win7",
        "source_asset_address": "192.168.100.50",
        "destination_asset_address": "example-host",
        "destination_local_account": "user",
        "logon_type": "NETWORK",
        "result": "SUCCESS",
        "new_authentication": "false",
        "service": "ntlmssp ",
        "source_json": {
          "sourceName": "Microsoft-Windows-Security-Auditing",
          "insertionStrings": [
            "S-1-0-0",
            "-",
            "-",
            "0x0",
            "X-X-X-XXXXXXXXXXX",
            "user@example.com",
            "example-host",
            "0x204f163c",
            "3",
            "NtLmSsp ",
            "NTLM",
            "",
            "{00000000-0000-0000-0000-000000000000}",
            "-",
            "NTLM V2",
            "128",
            "0x0",
            "-",
            "192.168.50.1",
            "59090"
          ],
          "eventCode": 4624,
          "computerName": "example-host",
          "sid": "",
          "isDomainController": false,
          "eventData": null,
          "timeWritten": "2020-10-02T00:29:13.670722000Z"
        }
      },
      "links": [
        {
          "rel": "Context",
          "href": "https://us.api.insight.rapid7.com/log_search/query/context/xxxx"
        }
      ],
      "sequence_number_str": "123456789123456789"
    }
  ]
}
```

#### Advanced Query on Log

This action is used to realtime query an InsightIDR log. This will query individual logs for results using a relative or absolute time-range from which to query.

This action should be used if querying an individual service or device.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|log|string|None|True|Log to search|None|Firewall Activity|
|query|string|None|True|LQL Query|None|where(user=adagentadmin, loose)|
|relative_time|string|Last 5 Minutes|True|A relative time in the past to look for alerts|['Last 5 Minutes', 'Last 10 Minutes', 'Last 20 Minutes', 'Last 30 Minutes', 'Last 45 Minutes', 'Last 1 Hour', 'Last 2 Hours', 'Last 3 Hours', 'Last 6 Hours', 'Last 12 Hours', 'Use Time From Value']|Last 5 Minutes|
|time_from|string|None|False|Beginning date and time for the query. This will be ignored unless Relative Time input is set to 'Use Time From Value'. The format is flexible and will work with simple dates (e.g. 01-01-2020) to full ISO time (e.g. 01-01-2020T00:00:00)|None|01-01-2020T00:00:00|
|time_to|string|None|False|Date and time for the end of the query. If left blank, the current time will be used. The format is flexible and will work with simple dates (e.g. 01-01-2020) to full ISO time (e.g. 01-01-2020T00:00:00)|None|12-31-2020T00:00:00|
|timeout|int|60|True|Time in seconds to wait for the query to return. If exceeded the plugin will throw an error|None|60|

Example input:

```
{
  "log": "Firewall Activity",
  "query": "where(user=adagentadmin, loose)",
  "relative_time": "Last 5 Minutes",
  "time_from": "01-01-2020T00:00:00",
  "time_to": "12-31-2020T00:00:00",
  "timeout": 60
}
```

To use Relative Time, leave `Time From` and `Time To` blank. For example:

```
{
  "relative_time": "Last 5 Minutes",
  "time_from": "",
  "time_to": "",
  ...
}
```

The above settings will run your search from 5 minutes ago until now.

If you want to use absolute time for a query. You can set up the input like this:

```
{
  "relative_time": "Use Time From Value",
  "time_from": "1/1/2021",
  "time_to": "1/31/2021",
  ...
}
```

This will run your search for the entire month of January every time.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|True|Number of log entries found|
|results|[]events|True|Query Results|

Example output:

```
{
  "results": [
    {
      "labels": [],
      "timestamp": 1601598638768,
      "sequence_number": 123456789123456789,
      "log_id": "64z0f0p9-1a99-4501-xe36-a6d03687f313",
      "message": {
        "timestamp": "2020-10-02T00:29:14.649Z",
        "destination_asset": "iagent-win7",
        "source_asset_address": "192.168.100.50",
        "destination_asset_address": "example-host",
        "destination_local_account": "user",
        "logon_type": "NETWORK",
        "result": "SUCCESS",
        "new_authentication": "false",
        "service": "ntlmssp ",
        "source_json": {
          "sourceName": "Microsoft-Windows-Security-Auditing",
          "insertionStrings": [
            "S-1-0-0",
            "-",
            "-",
            "0x0",
            "X-X-X-XXXXXXXXXXX",
            "user@example.com",
            "example-host",
            "0x204f163c",
            "3",
            "NtLmSsp ",
            "NTLM",
            "",
            "{00000000-0000-0000-0000-000000000000}",
            "-",
            "NTLM V2",
            "128",
            "0x0",
            "-",
            "192.168.50.1",
            "59090"
          ],
          "eventCode": 4624,
          "computerName": "example-host",
          "sid": "",
          "isDomainController": false,
          "eventData": null,
          "timeWritten": "2020-10-02T00:29:13.670722000Z"
        }
      },
      "links": [
        {
          "rel": "Context",
          "href": "https://us.api.insight.rapid7.com/log_search/query/context/xxxx"
        }
      ],
      "sequence_number_str": "123456789123456789"
    }
  ]
}
```

#### Get All Logs

This action is used to request a list of all Logs for an account. This action should be used when querying multiple related services.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|logs|logsets_info|True|All logs|

Example output:

```
{
  "log": {
    "log": {
      "id": "0b9a242d-d2fb-4e42-8656-eb5ff64d652f",
      "name": "Windows Defender",
      "tokens": [
        "bc38a911-65f1-4755-cca3-a330a6336b3a"
      ],
      "structures": [
        "1238a911-65f1-4755-cca3-a330a6336b3a"
      ],
      "user_data": {
        "platform_managed": "true"
      },
      "source_type": "token",
      "token_seed": null,
      "retention_period": "default",
      "links": [
        {
          "rel": "Related",
          "href": "https://example.com"
        }
      ],
      "rrn": "rrn:logsearch:us:bc38a911-65f1-4755-cca3-a330a6336b3a:log:bc38a911-65f1-4755-cca3-a330a6336b3a",
      "logsets_info": [
        {
          "id": "bc38a911-65f1-4755-cca3-a330a6336b3a",
          "name": "Unparsed Data",
          "rrn": "rrn:logsearch:us:bc38a911-65f1-4755-cca3-a330a6336b3a:logset:bc38a911-65f1-4755-cca3-a330a6336b3a",
          "links": [
            {
              "rel": "Self",
              "href": "https://example.com/3e966a63-bf3a-4a3c-8903-979c7e90ce85"
            }
          ]
        }
      ]
    }
  }
}
```

#### Get a Log

This action is used to get a specific log from an account.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Query ID|None|174e4f99-2ac7-4481-9301-4d24c34baf06|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|log|logsets_info|True|Requested log|

Example output:

```
{
  "log": {
    "log": {
      "id": "0b9a242d-d2fb-4e42-8656-eb5ff64d652f",
      "name": "Windows Defender",
      "tokens": [
        "bc38a911-65f1-4755-cca3-a330a6336b3a"
      ],
      "structures": [
        "1238a911-65f1-4755-cca3-a330a6336b3a"
      ],
      "user_data": {
        "platform_managed": "true"
      },
      "source_type": "token",
      "token_seed": null,
      "retention_period": "default",
      "links": [
        {
          "rel": "Related",
          "href": "https://example.com"
        }
      ],
      "rrn": "rrn:logsearch:us:bc38a911-65f1-4755-cca3-a330a6336b3a:log:bc38a911-65f1-4755-cca3-a330a6336b3a",
      "logsets_info": [
        {
          "id": "bc38a911-65f1-4755-cca3-a330a6336b3a",
          "name": "Unparsed Data",
          "rrn": "rrn:logsearch:us:bc38a911-65f1-4755-cca3-a330a6336b3a:logset:bc38a911-65f1-4755-cca3-a330a6336b3a",
          "links": [
            {
              "rel": "Self",
              "href": "https://example.com/3e966a63-bf3a-4a3c-8903-979c7e90ce85"
            }
          ]
        }
      ]
    }
  }
}
```

#### Close Investigations in Bulk

This action is used to close all investigations that fall within a date range.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_type|string|None|False|The category of alerts that should be closed|None|Account Created|
|datetime_from|date|None|False|An ISO formatted timestamp, default last week|None|2018-07-01 00:00:00 00:00|
|datetime_to|date|None|False|An ISO formatted timestamp of the ending date range, current time if left blank|None|2018-07-01 00:00:00 00:00|
|max_investigations_to_close|integer|None|False|An optional maximum number of alerts to close with this request. If this parameter is not specified then there is no maximum. If this limit is exceeded, then an error is returned|None|10|
|source|string|MANUAL|False|The name of an investigation source|['ALERT', 'MANUAL', 'HUNT']|MANUAL|

Example input:

```
{
  "alert_type": "Account Created",
  "datetime_from": "2018-07-01 00:00:00 00:00",
  "datetime_to": "2018-07-01 00:00:00 00:00",
  "max_investigations_to_close": 10,
  "source": "MANUAL"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ids|[]string|True|The IDs of the investigations that were closed by the request|
|num_closed|integer|True|The number of investigations closed by the request|

Example output:

```
{
  "ids": [
    "6c7db8d1-abc5-b9da-dd71-1a3ffffe8a16"
  ],
  "num_closed": 1
}
```

#### Get Query Results

This action is used to get query results for a LEQL query by query ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Query ID|None|174e4f99-2ac7-4481-9301-4d24c34baf06|

Example input:

```
{
  "id": "174e4f99-2ac7-4481-9301-4d24c34baf06"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|events|[]events|True|Events from logs|

Example output:

```
{
  "events": [
    {
      "labels": [],
      "log_id": "1b1a111d-d1fb-1a12-1651-eb1ff61a651a",
      "message": {
        "computerName": "iagent1-win10",
        "eventCode": 1111,
        "eventData": {
          "data": [],
          "engineVersion": "1.1.17300.4",
          "platformVersion": "4.18.2007.8",
          "productName": "%827",
          "signatureVersion": "1.321.836.0",
          "unused": null
        },
        "isDomainController": false,
        "sid": "S-1-5-18",
        "sourceName": "Microsoft-Windows-Windows Defender",
        "timeWritten": "2020-08-07T21:44:12.335999900Z"
      },
      "sequence_number": 1211198512587571200,
      "sequence_number_str": "1211198512587571200",
      "timestamp": 1596836653511
    }
  ]
}

```

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
|urls|[]string|None|False|URLs to add. e.g. ["https://example.com","https://test.com"]|None|["https://example.com", "https://test.com"]|

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
|index|integer|0|True|The optional zero-based index of the page to retrieve. Must be an integer greater than or equal to 0|None|1|
|size|integer|1000|True|The optional size of the page to retrieve. Must be an integer greater than 0 or less than or equal to 1000. Default value is 1000|None|1000|
|start_time|date|None|False|An optional ISO-formatted timestamp. Only investigations whose createTime is after this date will be returned by the API. If this parameter is omitted investigations with any create_time may be returned|None|2020-06-01T12:11:13+05:30|
|statuses|string|CLOSED|True|An optional-comma separated set of investigation statuses. Only the investigation whose status matches one of the entries in the list will be returned. If this parameter is omitted investigations with any status may be returned|['OPEN', 'CLOSED', 'EITHER']|CLOSED|

Example input:

```
{
  "end_time": "2020-06-01T12:11:13+05:30",
  "index": 1,
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

* 4.0.0 - Change object `labels` to `[]string` in Advanced Query on Log and Advanced Query on Log Set actions
* 3.1.4 - Add `docs_url` to plugin spec with a link to [InsightIDR plugin setup guide](https://docs.rapid7.com/insightconnect/rapid7-insightidr)
* 3.1.3 - Fix issue where Get a Log and Get All Logs would either fail in workflow or in connection test
* 3.1.2 - Send plugin name and version in the User-Agent string to vendor
* 3.1.1 - Convert given date from timezone to UTC in List Investigations action
* 3.1.0 - Add new action Create Threat
* 3.0.0 - Added Relative Time options to Advanced Query actions | Fix issue where a query with no results would crash the plugin
* 2.1.0 - New action Close Investigations in Bulk
* 2.0.1 - Fix issue where long-running queries could crash the plugin
* 2.0.0 - Refactor and split Advanced Query into two new actions Advanced Query on Log and Advanced Query on Log Set
* 1.5.0 - New actions Get a Log and Get All Logs
* 1.4.0 - New action Advanced Query
* 1.3.1 - Fix ID input description in Get Query Results action
* 1.3.0 - New action Get Query Results
* 1.2.1 - Change default value in the `size` input parameter to 1000 in List Investigations action
* 1.2.0 - New Action Assign User to Investigation
* 1.1.1 - New spec and help.md format for the Extension Library
* 1.1.0 - New Action Add Indicators to a Threat
* 1.0.0 - Initial plugin

# Links

## References

* [Rapid7 InsightIDR](https://www.rapid7.com/products/insightidr/)
