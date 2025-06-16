# Description

This plugin allows you to add indicators to a threat and see the status of investigations

# Key Features

* System Information and Event Management
* Endpoint Detection and Response
* Network Traffic Analysis
* User and Entity Behaviour Analytics
* Cloud and Integrations
* Embedded Threat Intelligence
* Deception Technology
* Incident Response and Investigations

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* Latest release successfully tested on 2025-06-11.

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|InsightIDR API key|None|4472f2g7-991z-4w70-li11-7552w8qm0266|None|None|
|region|string|United States 1|True|The region for InsightIDR|["United States 1", "United States 2", "United States 3", "Europe", "Canada", "Australia", "Japan"]|United States 1|None|None|

Example input:

```
{
  "api_key": "4472f2g7-991z-4w70-li11-7552w8qm0266",
  "region": "United States 1"
}
```

## Technical Details

### Actions


#### Add Indicators to a Threat

This action is used to add InsightIDR threat indicators to a threat with the given threat key

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain_names|[]string|None|False|Domain names to add|None|["rapid7.com", "google.com"]|None|None|
|hashes|[]string|None|False|Process hashes to add|None|["A94A8FE5CCB19BA61C4C0873D391E987982FBBD3", "C3499C2729730A7F807EFB8676A92DCB6F8A3F8F"]|None|None|
|ips|[]string|None|False|IP addresses to add|None|["10.0.0.1", "10.0.0.2"]|None|None|
|key|string|None|True|The key of a threat for which the indicators are going to be added|None|c9404e11-b81a-429d-9400-05c531f229c3|None|None|
|urls|[]string|None|False|URLs to add|None|["https://example.com", "https://test.com"]|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|rejected_indicators|[]string|False|The list of indicators that have been rejected during the update|["https://example.com", "https://test.com"]|
|threat|threat|False|The information about the threat|{'name': 'Contributing Collaborative Threat: Flagged Malicious', 'published': False, 'note': 'Notes', 'indicator_count': 13}|
  
Example output:

```
{
  "rejected_indicators": [
    "https://example.com",
    "https://test.com"
  ],
  "threat": {
    "indicator_count": 13,
    "name": "Contributing Collaborative Threat: Flagged Malicious",
    "note": "Notes",
    "published": false
  }
}
```

#### Advanced Query on Log

This action is used to realtime query an InsightIDR log. This will query individual logs for results. Note only 500 
results will be returned from a single call, if all results are required for this query please use smaller timeranges. 
If both a log name and a log ID are provided, the log ID will be used. However, either the log name OR log ID is 
required for the action to execute

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|log|string|None|False|Log name to search|None|Firewall Activity|None|None|
|log_id|string|None|False|Log id to search|None|123456-abcd-1234-abcd-123456abc|None|None|
|query|string|None|True|LEQL Query|None|where(user=adagentadmin, loose)|None|None|
|relative_time|string|Last 5 Minutes|True|A relative time in the past to look for alerts|["Last 5 Minutes", "Last 10 Minutes", "Last 20 Minutes", "Last 30 Minutes", "Last 45 Minutes", "Last 1 Hour", "Last 2 Hours", "Last 3 Hours", "Last 6 Hours", "Last 12 Hours", "Use Time From Value"]|Last 5 Minutes|None|None|
|time_from|string|None|False|Beginning date and time for the query. This will be ignored unless Relative Time input is set to 'Use Time From Value'. The format is flexible and will work with simple dates (e.g. 01-01-2020) to full ISO time (e.g. 01-01-2020T00:00:00)|None|01-01-2020T00:00:00|None|None|
|time_to|string|None|False|Date and time for the end of the query. If left blank, the current time will be used. The format is flexible and will work with simple dates (e.g. 01-01-2020) to full ISO time (e.g. 01-01-2020T00:00:00)|None|12-31-2020T00:00:00|None|None|
|timeout|int|60|True|Time in seconds to wait for the query to return. If exceeded the plugin will throw an error|None|60|None|None|
  
Example input:

```
{
  "log": "Firewall Activity",
  "log_id": "123456-abcd-1234-abcd-123456abc",
  "query": "where(user=adagentadmin, loose)",
  "relative_time": "Last 5 Minutes",
  "time_from": "01-01-2020T00:00:00",
  "time_to": "12-31-2020T00:00:00",
  "timeout": 60
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of log entries found|10|
|results_events|[]events|False|Query Results|[{"labels": [],"timestamp": 1601598638768,"sequence_number": 123456789123456789,"log_id": "64z0f0p9-1a99-4501-xe36-a6d03687f313","message": {"timestamp": "2020-10-02T00:29:14.649Z","destination_asset": "iagent-win7","source_asset_address": "192.168.100.50","destination_asset_address": "example-host","destination_local_account": "user","logon_type": "NETWORK","result": "SUCCESS","new_authentication": "false","service": "ntlmssp ","source_json": {"sourceName": "Microsoft-Windows-Security-Auditing","insertionStrings": ["S-1-0-0","-","-","0x0","X-X-X-XXXXXXXXXXX","user@example.com","example-host","0x204f163c","3","NtLmSsp ","NTLM","","{00000000-0000-0000-0000-000000000000}","-","NTLM V2","128","0x0","-","192.168.50.1","59090"],"eventCode": 4624,"computerName": "example-host","sid": "","isDomainController": false,"eventData": null,"timeWritten": "2020-10-02T00:29:13.670722000Z"}},"links": [{"rel": "Context","href": "https://us.api.insight.rapid7.com/log_search/query/context/xxxx"}],"sequence_number_str": "123456789123456789"}]|
|results_statistical|results_statistics|False|Query Results|{"leql":{"during":{"from":1699579214000,"to":1699622414000},"statement":"groupby(r7_context.asset.name)"},"logs":["123456-abcd-1234-abcd-123456abc"],"search_stats":{"bytes_all":9961260,"bytes_checked":9961260,"duration_ms":19,"events_all":1640,"events_checked":1640,"events_matched":1639,"index_factor":0.0},"statistics":{"all_exact_result":true,"cardinality":0,"from":1699579214000,"granularity":4320000,"groups":[{"linux":{"count":1163.0}},{"windowsx64":{"count":476.0}}],"groups_timeseries":[{"linux":{"groups_timeseries":[],"series":[{"count":45.0},{"count":21.0},{"count":16.0},{"count":270.0},{"count":27.0},{"count":43.0},{"count":27.0},{"count":39.0},{"count":29.0},{"count":646.0}],"totals":{"count":1163.0}}},{"windowsx64":{"groups_timeseries":[],"series":[{"count":54.0},{"count":40.0},{"count":60.0},{"count":37.0},{"count":42.0},{"count":62.0},{"count":41.0},{"count":47.0},{"count":49.0},{"count":44.0}],"totals":{"count":476.0}}}],"others":{"series":[]},"stats":{},"status":200,"timeseries":{},"to":1699622414000,"type":"count"}}|
  
Example output:

```
{
  "count": 10,
  "results_events": [
    {
      "labels": [],
      "links": [
        {
          "href": "https://us.api.insight.rapid7.com/log_search/query/context/xxxx",
          "rel": "Context"
        }
      ],
      "log_id": "64z0f0p9-1a99-4501-xe36-a6d03687f313",
      "message": {
        "destination_asset": "iagent-win7",
        "destination_asset_address": "example-host",
        "destination_local_account": "user",
        "logon_type": "NETWORK",
        "new_authentication": "false",
        "result": "SUCCESS",
        "service": "ntlmssp ",
        "source_asset_address": "192.168.100.50",
        "source_json": {
          "computerName": "example-host",
          "eventCode": 4624,
          "eventData": null,
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
          "isDomainController": false,
          "sid": "",
          "sourceName": "Microsoft-Windows-Security-Auditing",
          "timeWritten": "2020-10-02T00:29:13.670722000Z"
        },
        "timestamp": "2020-10-02T00:29:14.649Z"
      },
      "sequence_number": 123456789123456789,
      "sequence_number_str": "123456789123456789",
      "timestamp": 1601598638768
    }
  ],
  "results_statistical": {
    "leql": {
      "during": {
        "from": 1699579214000,
        "to": 1699622414000
      },
      "statement": "groupby(r7_context.asset.name)"
    },
    "logs": [
      "123456-abcd-1234-abcd-123456abc"
    ],
    "search_stats": {
      "bytes_all": 9961260,
      "bytes_checked": 9961260,
      "duration_ms": 19,
      "events_all": 1640,
      "events_checked": 1640,
      "events_matched": 1639,
      "index_factor": 0.0
    },
    "statistics": {
      "all_exact_result": true,
      "cardinality": 0,
      "from": 1699579214000,
      "granularity": 4320000,
      "groups": [
        {
          "linux": {
            "count": 1163.0
          }
        },
        {
          "windowsx64": {
            "count": 476.0
          }
        }
      ],
      "groups_timeseries": [
        {
          "linux": {
            "groups_timeseries": [],
            "series": [
              {
                "count": 45.0
              },
              {
                "count": 21.0
              },
              {
                "count": 16.0
              },
              {
                "count": 270.0
              },
              {
                "count": 27.0
              },
              {
                "count": 43.0
              },
              {
                "count": 27.0
              },
              {
                "count": 39.0
              },
              {
                "count": 29.0
              },
              {
                "count": 646.0
              }
            ],
            "totals": {
              "count": 1163.0
            }
          }
        },
        {
          "windowsx64": {
            "groups_timeseries": [],
            "series": [
              {
                "count": 54.0
              },
              {
                "count": 40.0
              },
              {
                "count": 60.0
              },
              {
                "count": 37.0
              },
              {
                "count": 42.0
              },
              {
                "count": 62.0
              },
              {
                "count": 41.0
              },
              {
                "count": 47.0
              },
              {
                "count": 49.0
              },
              {
                "count": 44.0
              }
            ],
            "totals": {
              "count": 476.0
            }
          }
        }
      ],
      "others": {
        "series": []
      },
      "stats": {},
      "status": 200,
      "timeseries": {},
      "to": 1699622414000,
      "type": "count"
    }
  }
}
```

#### Advanced Query on Log Set

This action is used to realtime query an InsightIDR log set. This will query entire log sets for results. Note only 500
 results will be returned from a single call, if all results are required for this query please use smaller timeranges

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|log_set|string|None|True|Log Set to search|["Advanced Malware Alert", "Active Directory Admin Activity", "Asset Authentication", "Cloud Service Admin Activity", "Cloud Service Activity", "DNS Query", "Endpoint Activity", "Endpoint Agent", "Exploit Mitigation Alert", "File Access Activity", "File Modification Activity", "Firewall Activity", "Network Flow", "Host To IP Observations", "IDS Alert", "Ingress Authentication", "Raw Log", "SSO Authentication", "Unparsed Data", "Third Party Alert", "Virus Alert", "Web Proxy Activity"]|Firewall Activity|None|None|
|query|string|None|True|LEQL Query|None|where(user=adagentadmin, loose)|None|None|
|relative_time|string|Last 5 Minutes|True|A relative time in the past to look for alerts|["Last 5 Minutes", "Last 10 Minutes", "Last 20 Minutes", "Last 30 Minutes", "Last 45 Minutes", "Last 1 Hour", "Last 2 Hours", "Last 3 Hours", "Last 6 Hours", "Last 12 Hours", "Use Time From Value"]|Last 5 Minutes|None|None|
|time_from|string|None|False|Beginning date and time for the query. This will be ignored unless Relative Time input is set to 'Use Time From Value'. The format is flexible and will work with simple dates (e.g. 01-01-2020) to full ISO time (e.g. 01-01-2020T00:00:00)|None|01-01-2020T00:00:00|None|None|
|time_to|string|None|False|Date and time for the end of the query. If left blank, the current time will be used. The format is flexible and will work with simple dates (e.g. 01-01-2020) to full ISO time (e.g. 01-01-2020T00:00:00)|None|12-31-2020T00:00:00|None|None|
|timeout|int|60|True|Time in seconds to wait for the query to return. If exceeded the plugin will throw an error|None|60|None|None|
  
Example input:

```
{
  "log_set": "Firewall Activity",
  "query": "where(user=adagentadmin, loose)",
  "relative_time": "Last 5 Minutes",
  "time_from": "01-01-2020T00:00:00",
  "time_to": "12-31-2020T00:00:00",
  "timeout": 60
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of log entries found|10|
|results_events|[]events|False|Query Results|[{"labels": [],"timestamp": 1601598638768,"sequence_number": 123456789123456789,"log_id": "64z0f0p9-1a99-4501-xe36-a6d03687f313","message": {"timestamp": "2020-10-02T00:29:14.649Z","destination_asset": "iagent-win7","source_asset_address": "192.168.100.50","destination_asset_address": "example-host","destination_local_account": "user","logon_type": "NETWORK","result": "SUCCESS","new_authentication": "false","service": "ntlmssp ","source_json": {"sourceName": "Microsoft-Windows-Security-Auditing","insertionStrings": ["S-1-0-0","-","-","0x0","X-X-X-XXXXXXXXXXX","user@example.com","example-host","0x204f163c","3","NtLmSsp ","NTLM","","{00000000-0000-0000-0000-000000000000}","-","NTLM V2","128","0x0","-","192.168.50.1","59090"],"eventCode": 4624,"computerName": "example-host","sid": "","isDomainController": false,"eventData": null,"timeWritten": "2020-10-02T00:29:13.670722000Z"}},"links": [{"rel": "Context","href": "https://us.api.insight.rapid7.com/log_search/query/context/xxxx"}],"sequence_number_str": "123456789123456789"}]|
|results_statistical|results_statistics|False|Query Results|{"leql":{"during":{"from":1699579214000,"to":1699622414000},"statement":"groupby(r7_context.asset.name)"},"logs":["123456-abcd-1234-abcd-123456abc"],"search_stats":{"bytes_all":9961260,"bytes_checked":9961260,"duration_ms":19,"events_all":1640,"events_checked":1640,"events_matched":1639,"index_factor":0.0},"statistics":{"all_exact_result":true,"cardinality":0,"from":1699579214000,"granularity":4320000,"groups":[{"linux":{"count":1163.0}},{"windowsx64":{"count":476.0}}],"groups_timeseries":[{"linux":{"groups_timeseries":[],"series":[{"count":45.0},{"count":21.0},{"count":16.0},{"count":270.0},{"count":27.0},{"count":43.0},{"count":27.0},{"count":39.0},{"count":29.0},{"count":646.0}],"totals":{"count":1163.0}}},{"windowsx64":{"groups_timeseries":[],"series":[{"count":54.0},{"count":40.0},{"count":60.0},{"count":37.0},{"count":42.0},{"count":62.0},{"count":41.0},{"count":47.0},{"count":49.0},{"count":44.0}],"totals":{"count":476.0}}}],"others":{"series":[]},"stats":{},"status":200,"timeseries":{},"to":1699622414000,"type":"count"}}|
  
Example output:

```
{
  "count": 10,
  "results_events": [
    {
      "labels": [],
      "links": [
        {
          "href": "https://us.api.insight.rapid7.com/log_search/query/context/xxxx",
          "rel": "Context"
        }
      ],
      "log_id": "64z0f0p9-1a99-4501-xe36-a6d03687f313",
      "message": {
        "destination_asset": "iagent-win7",
        "destination_asset_address": "example-host",
        "destination_local_account": "user",
        "logon_type": "NETWORK",
        "new_authentication": "false",
        "result": "SUCCESS",
        "service": "ntlmssp ",
        "source_asset_address": "192.168.100.50",
        "source_json": {
          "computerName": "example-host",
          "eventCode": 4624,
          "eventData": null,
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
          "isDomainController": false,
          "sid": "",
          "sourceName": "Microsoft-Windows-Security-Auditing",
          "timeWritten": "2020-10-02T00:29:13.670722000Z"
        },
        "timestamp": "2020-10-02T00:29:14.649Z"
      },
      "sequence_number": 123456789123456789,
      "sequence_number_str": "123456789123456789",
      "timestamp": 1601598638768
    }
  ],
  "results_statistical": {
    "leql": {
      "during": {
        "from": 1699579214000,
        "to": 1699622414000
      },
      "statement": "groupby(r7_context.asset.name)"
    },
    "logs": [
      "123456-abcd-1234-abcd-123456abc"
    ],
    "search_stats": {
      "bytes_all": 9961260,
      "bytes_checked": 9961260,
      "duration_ms": 19,
      "events_all": 1640,
      "events_checked": 1640,
      "events_matched": 1639,
      "index_factor": 0.0
    },
    "statistics": {
      "all_exact_result": true,
      "cardinality": 0,
      "from": 1699579214000,
      "granularity": 4320000,
      "groups": [
        {
          "linux": {
            "count": 1163.0
          }
        },
        {
          "windowsx64": {
            "count": 476.0
          }
        }
      ],
      "groups_timeseries": [
        {
          "linux": {
            "groups_timeseries": [],
            "series": [
              {
                "count": 45.0
              },
              {
                "count": 21.0
              },
              {
                "count": 16.0
              },
              {
                "count": 270.0
              },
              {
                "count": 27.0
              },
              {
                "count": 43.0
              },
              {
                "count": 27.0
              },
              {
                "count": 39.0
              },
              {
                "count": 29.0
              },
              {
                "count": 646.0
              }
            ],
            "totals": {
              "count": 1163.0
            }
          }
        },
        {
          "windowsx64": {
            "groups_timeseries": [],
            "series": [
              {
                "count": 54.0
              },
              {
                "count": 40.0
              },
              {
                "count": 60.0
              },
              {
                "count": 37.0
              },
              {
                "count": 42.0
              },
              {
                "count": 62.0
              },
              {
                "count": 41.0
              },
              {
                "count": 47.0
              },
              {
                "count": 49.0
              },
              {
                "count": 44.0
              }
            ],
            "totals": {
              "count": 476.0
            }
          }
        }
      ],
      "others": {
        "series": []
      },
      "stats": {},
      "status": 200,
      "timeseries": {},
      "to": 1699622414000,
      "type": "count"
    }
  }
}
```

#### Assign User to Investigation

This action is used to assign a user to the specified investigation

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|Investigation ID or RRN|None|174e4f99-2ac7-4481-9301-4d24c34baf06|None|None|
|user_email_address|string|None|True|The email address of the user to assign to this investigation, used to log into the insight platform|None|user@example.com|None|None|
  
Example input:

```
{
  "id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
  "user_email_address": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|investigation|investigation|True|The investigation that was modified|{'assignee': {'email': 'user@example.com', 'name': 'Ellen Example'}, 'created_time': '2018-06-06T16:56:42Z', 'disposition': 'BENIGN', 'first_alert_time': '2018-06-06T16:56:42Z', 'last_accessed': '2018-06-06T16:56:42Z', 'latest_alert_time': '2018-06-06T16:56:42Z', 'organization_id': '174e4f99-2ac7-4481-9301-4d24c34baf06', 'priority': 'CRITICAL', 'rrn': 'rrn:example', 'source': 'ALERT', 'status': 'OPEN', 'title': 'Example Title'}|
|success|boolean|True|Was the user assigned successfully|True|
  
Example output:

```
{
  "investigation": {
    "assignee": {
      "email": "user@example.com",
      "name": "Ellen Example"
    },
    "created_time": "2018-06-06T16:56:42Z",
    "disposition": "BENIGN",
    "first_alert_time": "2018-06-06T16:56:42Z",
    "last_accessed": "2018-06-06T16:56:42Z",
    "latest_alert_time": "2018-06-06T16:56:42Z",
    "organization_id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
    "priority": "CRITICAL",
    "rrn": "rrn:example",
    "source": "ALERT",
    "status": "OPEN",
    "title": "Example Title"
  },
  "success": true
}
```

#### Close Investigations in Bulk
  
This action is used to close all investigations that fall within a date range

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_type|string|None|False|The category of alerts that should be closed|None|Account Created|None|None|
|datetime_from|date|None|False|An ISO formatted timestamp, default last week|None|2018-07-01 00:00:00 00:00|None|None|
|datetime_to|date|None|False|An ISO formatted timestamp of the ending date range, current time if left blank|None|2018-07-01 00:00:00 00:00|None|None|
|max_investigations_to_close|integer|None|False|An optional maximum number of alerts to close with this request. If this parameter is not specified then there is no maximum. If this limit is exceeded, then an error is returned|None|10|None|None|
|source|string|MANUAL|False|The name of an investigation source|["ALERT", "MANUAL", "HUNT"]|MANUAL|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ids|[]string|True|The IDs of the investigations that were closed by the request|["6c7db8d1-abc5-b9da-dd71-1a3ffffe8a16"]|
|num_closed|integer|True|The number of investigations closed by the request|10|
  
Example output:

```
{
  "ids": [
    "6c7db8d1-abc5-b9da-dd71-1a3ffffe8a16"
  ],
  "num_closed": 10
}
```

#### Create Comment

This action is used to create a comment for a particular target. The target determines where the comment will appear 
within InsightIDR. Only certain types of RRNs are permitted as targets, such as investigation RRNs

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|attachments|[]string|None|False|An array of attachment RRNs to associate with the comment|None|["rrn:collaboration:us:01234567-89ab-cdef-0000-123123123123:attachment:ABCDEF543210"]|None|None|
|body|string|None|False|The body of the comment|None|Example comment|None|None|
|target|string|None|True|The target of the comment, which determines where it will appear within InsightIDR|None|rrn:investigation:us:01234567-89ab-cdef-0000-123123123123:investigation:ABCDEF543210|None|None|
  
Example input:

```
{
  "attachments": [
    "rrn:collaboration:us:01234567-89ab-cdef-0000-123123123123:attachment:ABCDEF543210"
  ],
  "body": "Example comment",
  "target": "rrn:investigation:us:01234567-89ab-cdef-0000-123123123123:investigation:ABCDEF543210"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|comment|comment|False|Newly created comment|{'created_time': '2022-09-22T08:38:13.962Z', 'rrn': 'rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:comment:1234567890', 'target': 'rrn:investigation:us:01234567-89ab-cdef-0000-123123123123:investigation:ABCDEF543210', 'creator': {'type': 'USER', 'name': 'Example User'}, 'body': 'test', 'visibility': 'PUBLIC', 'attachments': [{'rrn': 'rrn:collaboration:us:01234567-89ab-cdef-0000-123123123123:attachment:ABCDEF543210', 'creator': {'type': 'USER', 'name': 'Example User'}, 'created_time': '2022-09-20T13:54:28.246Z', 'file_name': 'test.txt', 'mime_type': 'text/plain', 'size': 4, 'scan_status': 'CLEAN'}]}|
|success|boolean|True|Whether the action was successful or not|True|
  
Example output:

```
{
  "comment": {
    "attachments": [
      {
        "created_time": "2022-09-20T13:54:28.246Z",
        "creator": {
          "name": "Example User",
          "type": "USER"
        },
        "file_name": "test.txt",
        "mime_type": "text/plain",
        "rrn": "rrn:collaboration:us:01234567-89ab-cdef-0000-123123123123:attachment:ABCDEF543210",
        "scan_status": "CLEAN",
        "size": 4
      }
    ],
    "body": "test",
    "created_time": "2022-09-22T08:38:13.962Z",
    "creator": {
      "name": "Example User",
      "type": "USER"
    },
    "rrn": "rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:comment:1234567890",
    "target": "rrn:investigation:us:01234567-89ab-cdef-0000-123123123123:investigation:ABCDEF543210",
    "visibility": "PUBLIC"
  },
  "success": true
}
```

#### Create Investigation

This action is used to allows to create investigation manually

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|disposition|string|None|False|Investigation's disposition|["", "UNDECIDED", "BENIGN", "MALICIOUS", "NOT_APPLICABLE"]|BENIGN|None|None|
|email|string|None|False|A user's email address for investigation to be assigned|None|user@example.com|None|None|
|priority|string|None|False|Investigation's priority|["", "LOW", "MEDIUM", "HIGH", "CRITICAL"]|LOW|None|None|
|status|string|None|False|Investigation's status|["", "OPEN", "CLOSED"]|OPEN|None|None|
|title|string|None|True|Investigation's title|None|Example Title|None|None|
  
Example input:

```
{
  "disposition": "BENIGN",
  "email": "user@example.com",
  "priority": "LOW",
  "status": "OPEN",
  "title": "Example Title"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|investigation|investigation|True|The body of the specified investigation|{'assignee': {'email': 'user@example.com', 'name': 'Ellen Example'}, 'created_time': '2018-06-06T16:56:42Z', 'disposition': 'BENIGN', 'first_alert_time': '2018-06-06T16:56:42Z', 'last_accessed': '2018-06-06T16:56:42Z', 'latest_alert_time': '2018-06-06T16:56:42Z', 'organization_id': '174e4f99-2ac7-4481-9301-4d24c34baf06', 'priority': 'CRITICAL', 'rrn': 'rrn:example', 'source': 'ALERT', 'status': 'OPEN', 'title': 'Example Title'}|
  
Example output:

```
{
  "investigation": {
    "assignee": {
      "email": "user@example.com",
      "name": "Ellen Example"
    },
    "created_time": "2018-06-06T16:56:42Z",
    "disposition": "BENIGN",
    "first_alert_time": "2018-06-06T16:56:42Z",
    "last_accessed": "2018-06-06T16:56:42Z",
    "latest_alert_time": "2018-06-06T16:56:42Z",
    "organization_id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
    "priority": "CRITICAL",
    "rrn": "rrn:example",
    "source": "ALERT",
    "status": "OPEN",
    "title": "Example Title"
  }
}
```

#### Create Threat

This action is used to create a private InsightIDR threat and add indicators to this threat

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|indicators|[]string|None|True|Add indicators to new threat in InsightIDR. Accept IP addresses, process hashes (SHA1, MD5, SHA256), domain names, URLs|None|["example.com", "10.0.0.1"]|None|None|
|note_text|string|Threat created via InsightConnect|False|Note text of created threat|None|Threat created via InsightConnect|None|None|
|threat_name|string|None|True|Name of created threat|None|Threat created via InsightConnect|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|rejected_indicators|[]string|True|Rejected indicators in new threat|["example.com", "10.0.0.1"]|
|threat|threat|True|The information about the new threat|{'name': 'Threat created via InsightConnect', 'note': 'Threat created via InsightConnect', 'published': False, 'indicator_count': 2}|
  
Example output:

```
{
  "rejected_indicators": [
    "example.com",
    "10.0.0.1"
  ],
  "threat": {
    "indicator_count": 2,
    "name": "Threat created via InsightConnect",
    "note": "Threat created via InsightConnect",
    "published": false
  }
}
```

#### Delete Attachment

This action is used to delete an attachment with the given RRN

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|attachment_rrn|string|None|True|The RRN of the attachment|None|rrn:collaboration:us:01234567-89ab-cdef-0000-123123123123:attachment:ABCDEF543210|None|None|
  
Example input:

```
{
  "attachment_rrn": "rrn:collaboration:us:01234567-89ab-cdef-0000-123123123123:attachment:ABCDEF543210"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the action was successful or not|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete Comment

This action is used to delete a comment by using an RRN. The RRN determines which comment will be deleted

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|comment_rrn|string|None|True|The RRN of the comment|None|rrn:collaboration:us:01234567-89ab-cdef-0000-123123123123:comment:ABCDEF543210|None|None|
  
Example input:

```
{
  "comment_rrn": "rrn:collaboration:us:01234567-89ab-cdef-0000-123123123123:comment:ABCDEF543210"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the action was successful or not|True|
  
Example output:

```
{
  "success": true
}
```

#### Download Attachment

This action is used to download an attachment by RRN. The RRN determines which attachment is downloaded

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|attachment_rrn|string|None|True|The RRN of the attachment|None|rrn:collaboration:us:01234567-89ab-cdef-0000-123123123123:attachment:ABCDEF543210|None|None|
  
Example input:

```
{
  "attachment_rrn": "rrn:collaboration:us:01234567-89ab-cdef-0000-123123123123:attachment:ABCDEF543210"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|attachment_content|bytes|False|The base64 encoded content of the attachment|dGVzdA==|
|success|boolean|True|Whether the action was successful or not|True|
  
Example output:

```
{
  "attachment_content": "dGVzdA==",
  "success": true
}
```

#### Get a Log

This action is used to get a specific log from an account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|Query ID|None|174e4f99-2ac7-4481-9301-4d24c34baf06|None|None|
  
Example input:

```
{
  "id": "174e4f99-2ac7-4481-9301-4d24c34baf06"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|log|logsets_info|True|Requested log|{"id": "0b9a242d-d2fb-4e42-8656-eb5ff64d652f","name": "Windows Defender","tokens": ["bc38a911-65f1-4755-cca3-a330a6336b3a"],"structures": ["1238a911-65f1-4755-cca3-a330a6336b3a"],"user_data": {"platform_managed": "true"},"source_type": "token","token_seed": null,"retention_period": "default","links": [{"rel": "Related","href": "https://example.com"}],"rrn": "rrn:logsearch:us:bc38a911-65f1-4755-cca3-a330a6336b3a:log:bc38a911-65f1-4755-cca3-a330a6336b3a","logsets_info": [{"id": "bc38a911-65f1-4755-cca3-a330a6336b3a","name": "Unparsed Data","rrn": "rrn:logsearch:us:bc38a911-65f1-4755-cca3-a330a6336b3a:logset:bc38a911-65f1-4755-cca3-a330a6336b3a","links": [{"rel": "Self","href": "https://example.com/3e966a63-bf3a-4a3c-8903-979c7e90ce85"}]}]}|
  
Example output:

```
{
  "log": {
    "id": "0b9a242d-d2fb-4e42-8656-eb5ff64d652f",
    "links": [
      {
        "href": "https://example.com",
        "rel": "Related"
      }
    ],
    "logsets_info": [
      {
        "id": "bc38a911-65f1-4755-cca3-a330a6336b3a",
        "links": [
          {
            "href": "https://example.com/3e966a63-bf3a-4a3c-8903-979c7e90ce85",
            "rel": "Self"
          }
        ],
        "name": "Unparsed Data",
        "rrn": "rrn:logsearch:us:bc38a911-65f1-4755-cca3-a330a6336b3a:logset:bc38a911-65f1-4755-cca3-a330a6336b3a"
      }
    ],
    "name": "Windows Defender",
    "retention_period": "default",
    "rrn": "rrn:logsearch:us:bc38a911-65f1-4755-cca3-a330a6336b3a:log:bc38a911-65f1-4755-cca3-a330a6336b3a",
    "source_type": "token",
    "structures": [
      "1238a911-65f1-4755-cca3-a330a6336b3a"
    ],
    "token_seed": null,
    "tokens": [
      "bc38a911-65f1-4755-cca3-a330a6336b3a"
    ],
    "user_data": {
      "platform_managed": "true"
    }
  }
}
```

#### Get a Saved Query

This action is used to retrieve a saved InsightIDR LEQL query by its ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query_id|string|None|True|UUID of saved query|None|00000000-0000-10d0-0000-000000000000|None|None|
  
Example input:

```
{
  "query_id": "00000000-0000-10d0-0000-000000000000"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|saved_query|query|True|Saved LEQL query|{'id': '00000000-0000-9eec-0000-000000000000', 'leql': {'during': {'from': None, 'time_range': 'yesterday', 'to': None}, 'statement': 'where(931dde6c60>=800)'}, 'logs': ['31a4d56e-460e-460f-9542-c2bc8edd7c6b'], 'name': 'Large Values Yesterday'}|
  
Example output:

```
{
  "saved_query": {
    "id": "00000000-0000-9eec-0000-000000000000",
    "leql": {
      "during": {
        "from": null,
        "time_range": "yesterday",
        "to": null
      },
      "statement": "where(931dde6c60>=800)"
    },
    "logs": [
      "31a4d56e-460e-460f-9542-c2bc8edd7c6b"
    ],
    "name": "Large Values Yesterday"
  }
}
```

#### Get Account Information

This action is used to get information from an account by RRN. The RRN determines which account information is 
retrieved from

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|account_rrn|string|None|True|The RRN of the Account|None|rrn:uba:us:123456-12334-1234-abcd-123456abc:account:123456abc|None|None|
  
Example input:

```
{
  "account_rrn": "rrn:uba:us:123456-12334-1234-abcd-123456abc:account:123456abc"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|account|account_object|False|Account details|{'rrn': 'rrn:uba:us:6bcf6c5b-552d-49a4-a3f5-259e0514585f:account:83002c85d7c6', 'name': 'jdoe@acme.com', 'domain': 'tor.acme.com', 'disabled': True, 'user': {'rrn': 'rrn:uba:us:6bcf6c5b-552d-49a4-a3f5-259e0514585f:user:83002c85d7c6', 'name': 'John Doe'}, 'authentication_service': 'ACTIVE_DIRECTORY'}|
  
Example output:

```
{
  "account": {
    "authentication_service": "ACTIVE_DIRECTORY",
    "disabled": true,
    "domain": "tor.acme.com",
    "name": "jdoe@acme.com",
    "rrn": "rrn:uba:us:6bcf6c5b-552d-49a4-a3f5-259e0514585f:account:83002c85d7c6",
    "user": {
      "name": "John Doe",
      "rrn": "rrn:uba:us:6bcf6c5b-552d-49a4-a3f5-259e0514585f:user:83002c85d7c6"
    }
  }
}
```

#### Retrieve Actors for a Single Alert

This action is used to allows the user to retrieve actors for a single alert from an alert RRN

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_rrn|string|None|True|The RRN of the alert|None|rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:actor:1:12345678-abcd-cdef-1234-12345abg|None|None|
|index|integer|0|False|Zero-based index of the page to retrieve, where value must be greater than or equal to 0|None|1|None|None|
|size|integer|100|False|Amount of data for a page to retrieve, where its value must be greater than 0 or less than or equal to 100|None|100|None|None|
  
Example input:

```
{
  "alert_rrn": "rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:actor:1:12345678-abcd-cdef-1234-12345abg",
  "index": 0,
  "size": 100
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|actors|[]actor_object|False|The alerts actors|[{"display_name": "test display name", "id": "12345678-abcd-cdef-1234-12345abc", "rrn": "rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:actor:1:12345678-abcd-cdef-1234-12345abg", "type": "ACCOUNT", "user_id": "12345678-abcd-cdef-1234-12345abf"}]|
|metadata|investigation_metadata|True|The pagination parameters used to generate this page result|{'index': 0, 'size': 1, 'total_data': 1, 'total_pages': 1}|
  
Example output:

```
{
  "actors": [
    {
      "display_name": "test display name",
      "id": "12345678-abcd-cdef-1234-12345abc",
      "rrn": "rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:actor:1:12345678-abcd-cdef-1234-12345abg",
      "type": "ACCOUNT",
      "user_id": "12345678-abcd-cdef-1234-12345abf"
    }
  ],
  "metadata": {
    "index": 0,
    "size": 1,
    "total_data": 1,
    "total_pages": 1
  }
}
```

#### Retrieve Evidence for a Single Alert

This action is used to allows the user to retrieve evidence for a single alert from an alert RRN

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_rrn|string|None|True|The RRN of the alert|None|rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:actor:1:12345678-abcd-cdef-1234-12345abg|None|None|
|index|integer|0|False|Zero-based index of the page to retrieve, where value must be greater than or equal to 0|None|1|None|None|
|size|integer|100|False|Amount of data for a page to retrieve, where its value must be greater than 0 or less than or equal to 100|None|100|None|None|
  
Example input:

```
{
  "alert_rrn": "rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:actor:1:12345678-abcd-cdef-1234-12345abg",
  "index": 0,
  "size": 100
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|evidences|[]evidence_object|False|The alert evidence|[{"created_at": "2023-12-04T13:59:06.768731Z", "data": {"timestamp": "2023-12-04T13:44:56.000Z", "user": "test_user", "account": "test_user", "result": "SUCCESS", "source_ip": "1.1.1.1", "service": "o365", "geoip_city": "Boston", "geoip_country_code": "US", "geoip_country_name": "United States", "geoip_organization": "TowardEX Technologies International", "geoip_region": "MA", "source_json": {"CreationTime": "2023-12-04T13:44:56", "Id": "12345678-abcd-cdef-1234-12345abc0", "Operation": "UserLoggedIn", "OrganizationId": "12345678-abcd-cdef-1234-12345abc", "RecordType": 15, "ResultStatus": "Success", "UserKey": "12345678-abcd-cdef-1234-12345abc", "UserType": 0, "Version": 1, "Workload": "AzureActiveDirectory", "ClientIP": "1.1.1.1", "ObjectId": "00000002-0000-0000-c000-000000000000", "UserId": "test_user", "AzureActiveDirectoryEventType": 1, "ExtendedProperties": [{"Name": "ResultStatusDetail", "Value": "Success"}, {"Name": "UserAuthenticationMethod", "Value": "1"}, {"Name": "RequestType", "Value": "OAuth2:Token"}], "ModifiedProperties": [], "Actor": [{"ID": "12345678-abcd-cdef-1234-12345abc", "Type": 0}, {"ID": "test_user", "Type": 5}], "ActorContextId": "12345678-abcd-cdef-1234-12345abc", "ActorIpAddress": "1.1.1.1", "InterSystemsId": "1bd394a5-be1b-4af3-a608-8ec6c73d5c02", "IntraSystemId": "12345678-abcd-cdef-1234-12345abc0", "SupportTicketId": "", "Target": [{"ID": "00000002-0000-0000-c000-000000000000", "Type": 0}], "TargetContextId": "12345678-abcd-cdef-1234-12345abc", "ApplicationId": "cb1056e2-e479-49de-ae31-7812af012ed8", "DeviceProperties": [{"Name": "OS", "Value": "Windows10"}, {"Name": "BrowserType", "Value": "Other"}, {"Name": "SessionId", "Value": "512345678-abcd-cdef-1234-12345abc"}], "ErrorNumber": "0"}, "custom_data": {"SourceRelative Url": "TargetContextId", "source_account": "RecordType"}, "r7_context": {"user": {"type": "user", "rrn": "rrn:uba:us:512345678-abcd-cdef-1234-12345abc:user:ABCDEFGH", "name": "test_user"}, "account": {"type": "account", "rrn": "rrn:uba:us:512345678-abcd-cdef-1234-12345abc:account:ABCDEFGH", "name": "test_user"}}}, "event_type": "ingress_auth", "evented_at": "2023-12-04T13:59:06.349Z", "external_source": "IDR ABA", "rrn": "rrn:alerts:us1:512345678-abcd-cdef-1234-12345abc:evidence:1:512345678-abcd-cdef-1234-12345abc", "updated_at": "2023-12-04T13:59:06.768731Z", "version": 1}]|
|metadata|investigation_metadata|True|The pagination parameters used to generate this page result|{'index': 0, 'size': 1, 'total_data': 1, 'total_pages': 1}|
  
Example output:

```
{
  "evidences": [
    {
      "created_at": "2023-12-04T13:59:06.768731Z",
      "data": {
        "account": "test_user",
        "custom_data": {
          "SourceRelative Url": "TargetContextId",
          "source_account": "RecordType"
        },
        "geoip_city": "Boston",
        "geoip_country_code": "US",
        "geoip_country_name": "United States",
        "geoip_organization": "TowardEX Technologies International",
        "geoip_region": "MA",
        "r7_context": {
          "account": {
            "name": "test_user",
            "rrn": "rrn:uba:us:512345678-abcd-cdef-1234-12345abc:account:ABCDEFGH",
            "type": "account"
          },
          "user": {
            "name": "test_user",
            "rrn": "rrn:uba:us:512345678-abcd-cdef-1234-12345abc:user:ABCDEFGH",
            "type": "user"
          }
        },
        "result": "SUCCESS",
        "service": "o365",
        "source_ip": "1.1.1.1",
        "source_json": {
          "Actor": [
            {
              "ID": "12345678-abcd-cdef-1234-12345abc",
              "Type": 0
            },
            {
              "ID": "test_user",
              "Type": 5
            }
          ],
          "ActorContextId": "12345678-abcd-cdef-1234-12345abc",
          "ActorIpAddress": "1.1.1.1",
          "ApplicationId": "cb1056e2-e479-49de-ae31-7812af012ed8",
          "AzureActiveDirectoryEventType": 1,
          "ClientIP": "1.1.1.1",
          "CreationTime": "2023-12-04T13:44:56",
          "DeviceProperties": [
            {
              "Name": "OS",
              "Value": "Windows10"
            },
            {
              "Name": "BrowserType",
              "Value": "Other"
            },
            {
              "Name": "SessionId",
              "Value": "512345678-abcd-cdef-1234-12345abc"
            }
          ],
          "ErrorNumber": "0",
          "ExtendedProperties": [
            {
              "Name": "ResultStatusDetail",
              "Value": "Success"
            },
            {
              "Name": "UserAuthenticationMethod",
              "Value": "1"
            },
            {
              "Name": "RequestType",
              "Value": "OAuth2:Token"
            }
          ],
          "Id": "12345678-abcd-cdef-1234-12345abc0",
          "InterSystemsId": "1bd394a5-be1b-4af3-a608-8ec6c73d5c02",
          "IntraSystemId": "12345678-abcd-cdef-1234-12345abc0",
          "ModifiedProperties": [],
          "ObjectId": "00000002-0000-0000-c000-000000000000",
          "Operation": "UserLoggedIn",
          "OrganizationId": "12345678-abcd-cdef-1234-12345abc",
          "RecordType": 15,
          "ResultStatus": "Success",
          "SupportTicketId": "",
          "Target": [
            {
              "ID": "00000002-0000-0000-c000-000000000000",
              "Type": 0
            }
          ],
          "TargetContextId": "12345678-abcd-cdef-1234-12345abc",
          "UserId": "test_user",
          "UserKey": "12345678-abcd-cdef-1234-12345abc",
          "UserType": 0,
          "Version": 1,
          "Workload": "AzureActiveDirectory"
        },
        "timestamp": "2023-12-04T13:44:56.000Z",
        "user": "test_user"
      },
      "event_type": "ingress_auth",
      "evented_at": "2023-12-04T13:59:06.349Z",
      "external_source": "IDR ABA",
      "rrn": "rrn:alerts:us1:512345678-abcd-cdef-1234-12345abc:evidence:1:512345678-abcd-cdef-1234-12345abc",
      "updated_at": "2023-12-04T13:59:06.768731Z",
      "version": 1
    }
  ],
  "metadata": {
    "index": 0,
    "size": 1,
    "total_data": 1,
    "total_pages": 1
  }
}
```

#### Get Alert Information

This action is used to get information from an alert by RRN. The RRN determines which alert the information is 
retrieved from

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_rrn|string|None|True|The RRN of the alert|None|rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:alert:1:12345678-abcd-cdef-1234-12345abg|None|None|
  
Example input:

```
{
  "alert_rrn": "rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:alert:1:12345678-abcd-cdef-1234-12345abg"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alert|alert_object|False|Alert details|{'alerted_at': '2023-12-04T13:59:06.349Z', 'created_at': '2023-12-04T13:59:06.757109Z', 'disposition': 'UNDECIDED', 'external_id': '12345678-abcd-cdef-1234-12345abc', 'external_source': 'IDR ABA', 'fields': [], 'ingested_at': '2023-12-04T13:59:06.751813Z', 'investigation_rrn': 'rrn:investigation:us:12345678-abcd-cdef-1234-12345abc:investigation:ABCDEFGHI', 'organization': {'customer_id': '12345678-abcd-cdef-1234-12345abc', 'customer_name': 'Dev Test', 'flags': [], 'id': '12345678-abcd-cdef-1234-12345abc', 'name': 'Dev Test', 'product_token': 'abcdefgh12345abc', 'region': 'us1'}, 'permissions': {'canEdit': False}, 'priority': 'LOW', 'responsibility': 'MDR', 'rrn': 'rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:alert:1:12345678-abcd-cdef-1234-12345abc', 'rule': {'mitre_tcodes': ['Credential Access', 'T1110'], 'rrn': 'rrn:cba:::detection-rule:ABCDEFGHIJK', 'version_rrn': 'rrn:cba:::detection-rule:version:ABCDEFGHIJK'}, 'rule_keys_of_interest': [{'key': 'result', 'values': ['SUCCESS']}, {'key': 'account', 'values': ['test_account']}, {'key': 'geoip_country_code', 'values': ['US']}, {'key': 'source_ip', 'values': ['1.1.1.1']}], 'rule_matching_keys': [{'key': 'entryType', 'values': ['ingress_auth']}, {'key': 'orgId', 'values': ['12345678-abcd-cdef-1234-12345abc']}], 'status': 'OPEN', 'tags': [], 'title': 'MVD Verification', 'type': 'MVD Verification', 'updated_at': '2023-12-05T11:51:39.29059Z', 'version': 8}|
|success|boolean|True|Whether the action was successful or not|True|
  
Example output:

```
{
  "alert": {
    "alerted_at": "2023-12-04T13:59:06.349Z",
    "created_at": "2023-12-04T13:59:06.757109Z",
    "disposition": "UNDECIDED",
    "external_id": "12345678-abcd-cdef-1234-12345abc",
    "external_source": "IDR ABA",
    "fields": [],
    "ingested_at": "2023-12-04T13:59:06.751813Z",
    "investigation_rrn": "rrn:investigation:us:12345678-abcd-cdef-1234-12345abc:investigation:ABCDEFGHI",
    "organization": {
      "customer_id": "12345678-abcd-cdef-1234-12345abc",
      "customer_name": "Dev Test",
      "flags": [],
      "id": "12345678-abcd-cdef-1234-12345abc",
      "name": "Dev Test",
      "product_token": "abcdefgh12345abc",
      "region": "us1"
    },
    "permissions": {
      "canEdit": false
    },
    "priority": "LOW",
    "responsibility": "MDR",
    "rrn": "rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:alert:1:12345678-abcd-cdef-1234-12345abc",
    "rule": {
      "mitre_tcodes": [
        "Credential Access",
        "T1110"
      ],
      "rrn": "rrn:cba:::detection-rule:ABCDEFGHIJK",
      "version_rrn": "rrn:cba:::detection-rule:version:ABCDEFGHIJK"
    },
    "rule_keys_of_interest": [
      {
        "key": "result",
        "values": [
          "SUCCESS"
        ]
      },
      {
        "key": "account",
        "values": [
          "test_account"
        ]
      },
      {
        "key": "geoip_country_code",
        "values": [
          "US"
        ]
      },
      {
        "key": "source_ip",
        "values": [
          "1.1.1.1"
        ]
      }
    ],
    "rule_matching_keys": [
      {
        "key": "entryType",
        "values": [
          "ingress_auth"
        ]
      },
      {
        "key": "orgId",
        "values": [
          "12345678-abcd-cdef-1234-12345abc"
        ]
      }
    ],
    "status": "OPEN",
    "tags": [],
    "title": "MVD Verification",
    "type": "MVD Verification",
    "updated_at": "2023-12-05T11:51:39.29059Z",
    "version": 8
  },
  "success": true
}
```

#### Get All Logs

This action is used to request used to list all logs for an account

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|logs|logsets_info|True|All logs|[{"log": {"id": "0b9a242d-d2fb-4e42-8656-eb5ff64d652f","name": "Windows Defender","tokens": ["bc38a911-65f1-4755-cca3-a330a6336b3a"],"structures": ["1238a911-65f1-4755-cca3-a330a6336b3a"],"user_data": {"platform_managed": "true"},"source_type": "token","token_seed": null,"retention_period": "default","links": [{"rel": "Related","href": "https://example.com"}],"rrn": "rrn:logsearch:us:bc38a911-65f1-4755-cca3-a330a6336b3a:log:bc38a911-65f1-4755-cca3-a330a6336b3a","logsets_info": [{"id": "bc38a911-65f1-4755-cca3-a330a6336b3a","name": "Unparsed Data","rrn": "rrn:logsearch:us:bc38a911-65f1-4755-cca3-a330a6336b3a:logset:bc38a911-65f1-4755-cca3-a330a6336b3a","links": [{"rel": "Self","href": "https://example.com/3e966a63-bf3a-4a3c-8903-979c7e90ce85"}]}]}}]|
  
Example output:

```
{
  "logs": [
    {
      "log": {
        "id": "0b9a242d-d2fb-4e42-8656-eb5ff64d652f",
        "links": [
          {
            "href": "https://example.com",
            "rel": "Related"
          }
        ],
        "logsets_info": [
          {
            "id": "bc38a911-65f1-4755-cca3-a330a6336b3a",
            "links": [
              {
                "href": "https://example.com/3e966a63-bf3a-4a3c-8903-979c7e90ce85",
                "rel": "Self"
              }
            ],
            "name": "Unparsed Data",
            "rrn": "rrn:logsearch:us:bc38a911-65f1-4755-cca3-a330a6336b3a:logset:bc38a911-65f1-4755-cca3-a330a6336b3a"
          }
        ],
        "name": "Windows Defender",
        "retention_period": "default",
        "rrn": "rrn:logsearch:us:bc38a911-65f1-4755-cca3-a330a6336b3a:log:bc38a911-65f1-4755-cca3-a330a6336b3a",
        "source_type": "token",
        "structures": [
          "1238a911-65f1-4755-cca3-a330a6336b3a"
        ],
        "token_seed": null,
        "tokens": [
          "bc38a911-65f1-4755-cca3-a330a6336b3a"
        ],
        "user_data": {
          "platform_managed": "true"
        }
      }
    }
  ]
}
```

#### Get All Saved Queries

This action is used to retrieve all saved InsightIDR LEQL queries

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|saved_queries|[]query|True|Saved LEQL queries|[{"id": "00000000-0000-9eec-0000-000000000000", "leql": {"during": {"from": null, "time_range": "yesterday", "to": null}, "statement": "where(931dde6c60>=800)"}, "logs": ["31a4d56e-460e-460f-9542-c2bc8edd7c6b"], "name": "Large Values Yesterday"}]|
  
Example output:

```
{
  "saved_queries": [
    {
      "id": "00000000-0000-9eec-0000-000000000000",
      "leql": {
        "during": {
          "from": null,
          "time_range": "yesterday",
          "to": null
        },
        "statement": "where(931dde6c60>=800)"
      },
      "logs": [
        "31a4d56e-460e-460f-9542-c2bc8edd7c6b"
      ],
      "name": "Large Values Yesterday"
    }
  ]
}
```

#### Get Asset Information

This action is used to get information from an asset by RRN. The RRN determines which asset the information is 
retrieved from

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|asset_rrn|string|None|True|The RRN of the asset|None|rrn:uba:us:6bcf6c5b-552d-49a4-a3f5-259e0514585f:asset:83002c85d7c6|None|None|
  
Example input:

```
{
  "asset_rrn": "rrn:uba:us:6bcf6c5b-552d-49a4-a3f5-259e0514585f:asset:83002c85d7c6"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|asset|asset|False|Asset details|{'name': 'morbo.tor.acme.com', 'rrn': 'rrn:uba:us:6bcf6c5b-552d-49a4-a3f5-259e0514585f:asset:83002c85d7c6'}|
|success|boolean|True|Whether the action was successful or not|True|
  
Example output:

```
{
  "asset": {
    "name": "morbo.tor.acme.com",
    "rrn": "rrn:uba:us:6bcf6c5b-552d-49a4-a3f5-259e0514585f:asset:83002c85d7c6"
  },
  "success": true
}
```

#### Get Attachment Information

This action is used to get information from an attachment by RRN. The RRN determines which attachment information is 
retrieved from

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|attachment_rrn|string|None|True|The RRN of the attachment|None|rrn:collaboration:us:01234567-89ab-cdef-0000-123123123123:attachment:ABCDEF543210|None|None|
  
Example input:

```
{
  "attachment_rrn": "rrn:collaboration:us:01234567-89ab-cdef-0000-123123123123:attachment:ABCDEF543210"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|attachment|attachment|False|Attachment details|{'rrn': 'rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890', 'creator': {'type': 'USER', 'name': 'Example User'}, 'created_time': '2022-08-19T13:00:58.645Z', 'file_name': 'test.txt', 'mime_type': 'text/plain', 'size': 4, 'scan_status': 'CLEAN'}|
|success|boolean|True|Whether the action was successful or not|True|
  
Example output:

```
{
  "attachment": {
    "created_time": "2022-08-19T13:00:58.645Z",
    "creator": {
      "name": "Example User",
      "type": "USER"
    },
    "file_name": "test.txt",
    "mime_type": "text/plain",
    "rrn": "rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890",
    "scan_status": "CLEAN",
    "size": 4
  },
  "success": true
}
```

#### Get Investigation

This action is used to allows to get existing investigation by ID or RRN

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|The identifier of investigation (ID or RRN)|None|rrn:investigation:example:11111111-1111-1111-1111-111111111111:investigation:11111111|None|None|
  
Example input:

```
{
  "id": "rrn:investigation:example:11111111-1111-1111-1111-111111111111:investigation:11111111"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|investigation|investigation|True|The body of the specified investigation|{'assignee': {'email': 'user@example.com', 'name': 'Ellen Example'}, 'created_time': '2018-06-06T16:56:42Z', 'disposition': 'BENIGN', 'first_alert_time': '2018-06-06T16:56:42Z', 'last_accessed': '2018-06-06T16:56:42Z', 'latest_alert_time': '2018-06-06T16:56:42Z', 'organization_id': '174e4f99-2ac7-4481-9301-4d24c34baf06', 'priority': 'CRITICAL', 'rrn': 'rrn:example', 'source': 'ALERT', 'status': 'OPEN', 'title': 'Example Title'}|
  
Example output:

```
{
  "investigation": {
    "assignee": {
      "email": "user@example.com",
      "name": "Ellen Example"
    },
    "created_time": "2018-06-06T16:56:42Z",
    "disposition": "BENIGN",
    "first_alert_time": "2018-06-06T16:56:42Z",
    "last_accessed": "2018-06-06T16:56:42Z",
    "latest_alert_time": "2018-06-06T16:56:42Z",
    "organization_id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
    "priority": "CRITICAL",
    "rrn": "rrn:example",
    "source": "ALERT",
    "status": "OPEN",
    "title": "Example Title"
  }
}
```

#### Get User Information

This action is used to get information from an user by RRN. The RRN determines which user the information is retrieved 
from

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|user_rrn|string|None|True|The RRN of the user|None|rrn:uba:us:6bcf6c5b-552d-49a4-a3f5-259e0514585f:user:83002c85d7c6|None|None|
  
Example input:

```
{
  "user_rrn": "rrn:uba:us:6bcf6c5b-552d-49a4-a3f5-259e0514585f:user:83002c85d7c6"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the action was successful or not|True|
|user|user|False|User details|{'domain': 'tor.acme.com', 'first_name': 'John', 'last_name': 'Doe', 'name': 'John Doe', 'rrn': 'rrn:uba:us:6bcf6c5b-552d-49a4-a3f5-259e0514585f:user:83002c85d7c6'}|
  
Example output:

```
{
  "success": true,
  "user": {
    "domain": "tor.acme.com",
    "first_name": "John",
    "last_name": "Doe",
    "name": "John Doe",
    "rrn": "rrn:uba:us:6bcf6c5b-552d-49a4-a3f5-259e0514585f:user:83002c85d7c6"
  }
}
```

#### List Alerts for Investigation

This action is used to retrieve a page of alerts associated with the specified investigation

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|The identifier of investigation (ID or RRN)|None|rrn:investigation:example:11111111-1111-1111-1111-111111111111:investigation:11111111|None|None|
|index|integer|0|True|The optional zero-based index of the page to retrieve. Must be an integer greater than or equal to 0|None|1|None|None|
|size|integer|100|True|The optional size of the page to retrieve. Must be an integer greater than 0 or less than or equal to 100. Default value is 100|None|100|None|None|
  
Example input:

```
{
  "id": "rrn:investigation:example:11111111-1111-1111-1111-111111111111:investigation:11111111",
  "index": 0,
  "size": 100
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alerts|[]alert|True|A list of alerts associated with the investigation|[{"alert_type": "Example Type", "alert_type_description": "Example Description", "created_time": "01-01-2020T00:00:00", "detection_rule_rrn": "rrn:example", "first_event_time": "01-01-2020T00:00:00", "id": "11111111-1111-1111-1111-111111111111", "latest_event_time": "01-01-2020T00:00:00", "title": "Example Title"}]|
|metadata|investigation_metadata|True|The pagination parameters used to generate this page result|{'index': 0, 'size': 1, 'total_data': 1, 'total_pages': 1}|
  
Example output:

```
{
  "alerts": [
    {
      "alert_type": "Example Type",
      "alert_type_description": "Example Description",
      "created_time": "01-01-2020T00:00:00",
      "detection_rule_rrn": "rrn:example",
      "first_event_time": "01-01-2020T00:00:00",
      "id": "11111111-1111-1111-1111-111111111111",
      "latest_event_time": "01-01-2020T00:00:00",
      "title": "Example Title"
    }
  ],
  "metadata": {
    "index": 0,
    "size": 1,
    "total_data": 1,
    "total_pages": 1
  }
}
```

#### List Attachments

This action is used to retrieves attachments matching the given request parameters

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|index|integer|0|False|The optional 0 based index of the page to retrieve. Must be an integer greater than or equal to 0. Default value set to 0|None|3|None|None|
|size|integer|20|False|Size of the page to retrieve. Must be an integer greater than 0 or less than or equal to 100. Default value set to 20|None|100|None|None|
|target|string|None|True|The RRN of the target, for which attachments will be returned|None|rrn:investigation:us:01234567-89ab-cdef-0000-123123123123:investigation:ABCDEF543210|None|None|
  
Example input:

```
{
  "index": 0,
  "size": 20,
  "target": "rrn:investigation:us:01234567-89ab-cdef-0000-123123123123:investigation:ABCDEF543210"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|attachments|[]attachment|False|List of attachments|[{"rrn": "rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890", "creator": {"type": "USER", "name": "Example User"}, "created_time": "2022-08-19T13:00:58.645Z", "file_name": "test.txt", "mime_type": "text/plain", "size": 4, "scan_status": "CLEAN"}]|
|success|boolean|True|Whether the action was successful or not|True|
  
Example output:

```
{
  "attachments": [
    {
      "created_time": "2022-08-19T13:00:58.645Z",
      "creator": {
        "name": "Example User",
        "type": "USER"
      },
      "file_name": "test.txt",
      "mime_type": "text/plain",
      "rrn": "rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890",
      "scan_status": "CLEAN",
      "size": 4
    }
  ],
  "success": true
}
```

#### List Comments

This action is used to list all comments on an investigation by passing an investigation's RRN as the target value

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|index|integer|0|False|The optional 0 based index of the page to retrieve. Must be an integer greater than or equal to 0. Default value set to 0|None|3|None|None|
|size|integer|20|False|Size of the page to retrieve. Must be an integer greater than 0 or less than or equal to 100. Default value set to 20|None|100|None|None|
|target|string|None|True|The target of the comment, which determines where it will appear within InsightIDR|None|rrn:investigation:us:01234567-89ab-cdef-0000-123123123123:investigation:ABCDEF543210|None|None|
  
Example input:

```
{
  "index": 0,
  "size": 20,
  "target": "rrn:investigation:us:01234567-89ab-cdef-0000-123123123123:investigation:ABCDEF543210"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|comments|[]comment|False|List of comments|[{"created_time": "2022-08-18T12:53:26.676Z", "rrn": "rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:comment:1234567890", "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:1234567890", "creator": {"type": "USER", "name": "Example User"}, "body": "test", "visibility": "PUBLIC", "attachments": [{"rrn": "rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890", "creator": {"type": "USER", "name": "Example User"}, "created_time": "2022-08-19T13:00:58.645Z", "file_name": "test.txt", "mime_type": "text/plain", "size": 4, "scan_status": "CLEAN"}]}]|
|success|boolean|True|Whether the action was successful or not|True|
  
Example output:

```
{
  "comments": [
    {
      "attachments": [
        {
          "created_time": "2022-08-19T13:00:58.645Z",
          "creator": {
            "name": "Example User",
            "type": "USER"
          },
          "file_name": "test.txt",
          "mime_type": "text/plain",
          "rrn": "rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890",
          "scan_status": "CLEAN",
          "size": 4
        }
      ],
      "body": "test",
      "created_time": "2022-08-18T12:53:26.676Z",
      "creator": {
        "name": "Example User",
        "type": "USER"
      },
      "rrn": "rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:comment:1234567890",
      "target": "rrn:investigation:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:investigation:1234567890",
      "visibility": "PUBLIC"
    }
  ],
  "success": true
}
```

#### List Investigations

This action is used to retrieve a page of investigations matching the given request parameters. If there is no 
'start_time' and 'end_time' provided, 'start_time' will  default to 28 days prior, and 'end_time' will default to the 
current time

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|email|string|None|False|A user's email address, where only investigations assigned to that user will be included|None|user@example.com|None|None|
|end_time|date|None|False|An optional-ISO formatted timestamp, where only investigations whose createTime is before this date will be returned. If there is no value provided, this will default to the current time|None|2020-06-01T12:11:13+05:30|None|None|
|index|integer|0|True|Zero-based index of the page to retrieve, where value must be greater than or equal to 0|None|1|None|None|
|priorities|[]string|None|False|A comma-separated list of investigation priorities to include in the result, where possible values are LOW, MEDIUM, HIGH, CRITICAL|None|["LOW", "MEDIUM", "HIGH", "CRITICAL"]|None|None|
|size|integer|100|True|Amount of data for a page to retrieve, where its value must be greater than 0 and less than or equal to 100|None|100|None|None|
|sort|string|None|False|A field for investigations to be sorted|["", "Created time Ascending", "Created time Descending", "Priority Ascending", "Priority Descending", "RRN Ascending", "RRN Descending", "Alerts most recent created time Ascending", "Alerts most recent created time Descending", "Alerts most recent detection created time Ascending", "Alerts most recent detection created time Descending", "Responsibility Ascending", "Responsibility Descending"]|Created time Ascending|None|None|
|sources|[]string|None|False|A comma-separated list of investigation sources to include in the result, where possible values are USER, ALERT, HUNT, AUTOMATION|None|["USER","ALERT"]|None|None|
|start_time|date|None|False|An optional ISO-formatted timestamp, where only investigations whose createTime is after this date will be returned. If there is no value provided this will default to 28 days prior|None|2020-06-01T12:11:13+05:30|None|None|
|statuses|[]string|None|False|Comma-separated list of investigation statuses to include in the result. Possible values are OPEN, CLOSED, INVESTIGATING, WAITING|None|["CLOSED"]|None|None|
  
Example input:

```
{
  "email": "user@example.com",
  "end_time": "2020-06-01T12:11:13+05:30",
  "index": 0,
  "priorities": [
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL"
  ],
  "size": 100,
  "sort": "Created time Ascending",
  "sources": [
    "USER",
    "ALERT"
  ],
  "start_time": "2020-06-01T12:11:13+05:30",
  "statuses": [
    "CLOSED"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|investigations|[]investigation|True|A list of found investigations|[{"assignee": {"email": "user@example.com", "name": "Ellen Example"}, "created_time": "2018-06-06T16:56:42Z", "disposition": "BENIGN", "first_alert_time": "2018-06-06T16:56:42Z", "last_accessed": "2018-06-06T16:56:42Z", "latest_alert_time": "2018-06-06T16:56:42Z", "organization_id": "174e4f99-2ac7-4481-9301-4d24c34baf06", "priority": "CRITICAL", "rrn": "rrn:example", "source": "ALERT", "status": "OPEN", "title": "Example Title"}]|
|metadata|investigation_metadata|True|The pagination parameters used to generate this page result|{'index': 0, 'size': 1, 'total_data': 1, 'total_pages': 1}|
  
Example output:

```
{
  "investigations": [
    {
      "assignee": {
        "email": "user@example.com",
        "name": "Ellen Example"
      },
      "created_time": "2018-06-06T16:56:42Z",
      "disposition": "BENIGN",
      "first_alert_time": "2018-06-06T16:56:42Z",
      "last_accessed": "2018-06-06T16:56:42Z",
      "latest_alert_time": "2018-06-06T16:56:42Z",
      "organization_id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
      "priority": "CRITICAL",
      "rrn": "rrn:example",
      "source": "ALERT",
      "status": "OPEN",
      "title": "Example Title"
    }
  ],
  "metadata": {
    "index": 0,
    "size": 1,
    "total_data": 1,
    "total_pages": 1
  }
}
```

#### Get Query Results

This action is used to get query results for a LEQL query by log ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|Log ID|None|174e4f99-2ac7-4481-9301-4d24c34baf06|None|None|
|most_recent_first|boolean|None|False|Order most recent first|None|True|None|None|
  
Example input:

```
{
  "id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
  "most_recent_first": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|events|[]events|True|Events from logs|[{"labels": [],"timestamp": 1601598638768,"sequence_number": 123456789123456789,"log_id": "64z0f0p9-1a99-4501-xe36-a6d03687f313","message": {"timestamp": "2020-10-02T00:29:14.649Z","destination_asset": "iagent-win7","source_asset_address": "192.168.100.50","destination_asset_address": "example-host","destination_local_account": "user","logon_type": "NETWORK","result": "SUCCESS","new_authentication": "false","service": "ntlmssp ","source_json": {"sourceName": "Microsoft-Windows-Security-Auditing","insertionStrings": ["S-1-0-0","-","-","0x0","X-X-X-XXXXXXXXXXX","user@example.com","example-host","0x204f163c","3","NtLmSsp ","NTLM","","{00000000-0000-0000-0000-000000000000}","-","NTLM V2","128","0x0","-","192.168.50.1","59090"],"eventCode": 4624,"computerName": "example-host","sid": "","isDomainController": false,"eventData": null,"timeWritten": "2020-10-02T00:29:13.670722000Z"}},"links": [{"rel": "Context","href": "https://us.api.insight.rapid7.com/log_search/query/context/xxxx"}],"sequence_number_str": "123456789123456789"}]|
  
Example output:

```
{
  "events": [
    {
      "labels": [],
      "links": [
        {
          "href": "https://us.api.insight.rapid7.com/log_search/query/context/xxxx",
          "rel": "Context"
        }
      ],
      "log_id": "64z0f0p9-1a99-4501-xe36-a6d03687f313",
      "message": {
        "destination_asset": "iagent-win7",
        "destination_asset_address": "example-host",
        "destination_local_account": "user",
        "logon_type": "NETWORK",
        "new_authentication": "false",
        "result": "SUCCESS",
        "service": "ntlmssp ",
        "source_asset_address": "192.168.100.50",
        "source_json": {
          "computerName": "example-host",
          "eventCode": 4624,
          "eventData": null,
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
          "isDomainController": false,
          "sid": "",
          "sourceName": "Microsoft-Windows-Security-Auditing",
          "timeWritten": "2020-10-02T00:29:13.670722000Z"
        },
        "timestamp": "2020-10-02T00:29:14.649Z"
      },
      "sequence_number": 123456789123456789,
      "sequence_number_str": "123456789123456789",
      "timestamp": 1601598638768
    }
  ]
}
```

#### Replace Indicators

This action is used to replace InsightIDR threat indicators in a threat with the given threat key

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain_names|[]string|None|False|Domain names to add|None|["rapid7.com", "google.com"]|None|None|
|hashes|[]string|None|False|Process hashes to add|None|["A94A8FE5CCB19BA61C4C0873D391E987982FBBD3", "C3499C2729730A7F807EFB8676A92DCB6F8A3F8F"]|None|None|
|ips|[]string|None|False|IP addresses to add|None|["10.0.0.1", "10.0.0.2"]|None|None|
|key|string|None|True|The key of a threat for which the indicators are going to be added|None|c9404e11-b81a-429d-9400-05c531f229c3|None|None|
|urls|[]string|None|False|URLs to add|None|["https://example.com", "https://test.com"]|None|None|
  
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

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|rejected_indicators|[]string|False|The list of indicators that have been rejected during the update|["example.com", "10.0.0.1"]|
|threat|threat|False|The information about the threat|{'name': 'bad-virus', 'note': 'test', 'published': False, 'indicator_count': 2}|
  
Example output:

```
{
  "rejected_indicators": [
    "example.com",
    "10.0.0.1"
  ],
  "threat": {
    "indicator_count": 2,
    "name": "bad-virus",
    "note": "test",
    "published": false
  }
}
```

#### Search Accounts

This action is used to allows the user to retrieve idr accounts that match the given criteria

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|index|integer|0|False|Zero-based index of the page to retrieve, where value must be greater than or equal to 0|None|1|None|None|
|search|[]search_accounts_object|None|False|The criteria for which entities to return|None|[{"field": "Example Field", "operator": "EQUALS", "value": "Test Value"}]|None|None|
|size|integer|100|False|Amount of data for a page to retrieve, where its value must be greater than 0 or less than or equal to 100|None|100|None|None|
|sort|[]sort_accounts_object|None|False|The criteria and sorting information for searching|None|[{"field": "Example Field", "order": "ASC"}]|None|None|
  
Example input:

```
{
  "index": 0,
  "search": [
    {
      "field": "Example Field",
      "operator": "EQUALS",
      "value": "Test Value"
    }
  ],
  "size": 100,
  "sort": [
    {
      "field": "Example Field",
      "order": "ASC"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|[]account_object|True|The list of account information|[ { "rrn": "rrn:uba:us:6bcf6c5b-552d-49a4-a3f5-259e0514585f:account:83002c85d7c6", "name": "jdoe@acme.com", "domain": "tor.acme.com", "disabled": true, "user": { "rrn": "rrn:uba:us:6bcf6c5b-552d-49a4-a3f5-259e0514585f:user:83002c85d7c6", "name": "John Doe" }, "authentication_service": "ACTIVE_DIRECTORY" } ]|
|metadata|investigation_metadata|True|The pagination parameters used to generate this page result|{"index": 0,"size": 1,"total_data": 1,"total_pages": 1}|
  
Example output:

```
{
  "data": [
    {
      "authentication_service": "ACTIVE_DIRECTORY",
      "disabled": true,
      "domain": "tor.acme.com",
      "name": "jdoe@acme.com",
      "rrn": "rrn:uba:us:6bcf6c5b-552d-49a4-a3f5-259e0514585f:account:83002c85d7c6",
      "user": {
        "name": "John Doe",
        "rrn": "rrn:uba:us:6bcf6c5b-552d-49a4-a3f5-259e0514585f:user:83002c85d7c6"
      }
    }
  ],
  "metadata": {
    "index": 0,
    "size": 1,
    "total_data": 1,
    "total_pages": 1
  }
}
```

#### Search Alerts

This action is used to allows the user to search for alerts that match the given criteria

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|aggregates|[]aggregate_object|None|False|Aggregations to apply for all matching results|None|[{}]|None|None|
|end_time|date|None|False|An optional-ISO formatted timestamp, where only investigations whose createTime is before this date will be returned, if provided a start time will also need provided. If no times are provided a default of 6 months will be used|None|2020-06-01T12:11:13+05:30|None|None|
|field_ids|[]string|None|False|Additional fields to include for each alert. No additional fields are included if field_ids is empty|None|[]|None|None|
|index|integer|0|False|Zero-based index of the page to retrieve, where value must be greater than or equal to 0|None|1|None|None|
|leql|string|None|False|The LEQL 'WHERE' clause to match against|None||None|None|
|rrns_only|boolean|False|False|Indicates whether the response returns only the alert Rapid7 Resource Names (RRNs) or the alert RRNs and the alert details. If rrns_only is set to TRUE, the response returns the RRNs only. If rrns_only is set to FALSE or is unspecified, the response returns the RRNs and the alert details|None|False|None|None|
|size|integer|100|False|Amount of data for a page to retrieve, where its value must be greater than 0 or less than or equal to 100|None|100|None|None|
|sorts|[]sort_object|None|False|The sort order to apply to the matching results., where possible field values are RRN, PRIORITY, CREATED TIME, and order values are ASCENDING_NULLS_LAST, ASCENDING_NULLS_FIRST, DESCENDING_NULLS_LAST, DESCENDING_NULLS_FIRST|None|[{"field_id": "Example Field", "order": "ASCENDING_NULLS_LAST"}]|None|None|
|start_time|date|None|False|An optional ISO-formatted timestamp, where only investigations whose createTime is after this date will be returned, if provided an end time will also need provided. If no times are provided a default of 6 months will be used|None|2020-06-01T12:11:13+05:30|None|None|
|terms|[]terms_object|None|False|The search terms to match against|None||None|None|
  
Example input:

```
{
  "aggregates": [
    {}
  ],
  "end_time": "2020-06-01T12:11:13+05:30",
  "field_ids": [],
  "index": 0,
  "leql": "",
  "rrns_only": false,
  "size": 100,
  "sorts": [
    {
      "field_id": "Example Field",
      "order": "ASCENDING_NULLS_LAST"
    }
  ],
  "start_time": "2020-06-01T12:11:13+05:30",
  "terms": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|aggregates|[]aggregate_response_object|False|The aggregation results|[{"name": "example_id", "type": "BUCKET", "value": "example_value", "field_ids": ["example_field"], "buckets": [{"keys": ["example_key"], "count":1}]}]|
|alerts|[]alert_object|False|A list of found alerts|[{ "alerted_at": "2023-12-04T13:59:06.349Z","created_at": "2023-12-04T13:59:06.757109Z","disposition": "UNDECIDED","external_id": "12345678-abcd-cdef-1234-12345abc","external_source": "IDR ABA","fields": [],"ingested_at": "2023-12-04T13:59:06.751813Z","investigation_rrn":"rrn:investigation:us:12345678-abcd-cdef-1234-12345abc:investigation:ABCDEFGHI","organization": {"customer_id": "12345678-abcd-cdef-1234-12345abc","customer_name": "Dev Test","flags": [],"id": "12345678-abcd-cdef-1234-12345abc","name": "Dev Test","product_token": "abcdefgh12345abc","region": "us1"},"permissions": {"canEdit": false},"priority": "LOW","responsibility": "MDR","rrn":"rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:alert:1:12345678-abcd-cdef-1234-12345abc","rule": {"mitre_tcodes": ["Credential Access","T1110"],"rrn": "rrn:cba:::detection-rule:ABCDEFGHIJK","version_rrn": "rrn:cba:::detection-rule:version:ABCDEFGHIJK"},"rule_keys_of_interest": [{"key": "result","values": ["SUCCESS"]},{"key": "account","values": ["test_account"]},{"key": "geoip_country_code","values": ["US"]},{"key": "source_ip","values": ["1.1.1.1"]}],"rule_matching_keys": [{"key": "entryType","values": ["ingress_auth"]},{"key": "orgId","values": ["12345678-abcd-cdef-1234-12345abc"]}],"status": "OPEN","tags": [],"title": "MVD Verification","type": "MVD Verification","updated_at": "2023-12-05T11:51:39.29059Z","version": 8 }]|
|metadata|investigation_metadata|True|The pagination parameters used to generate this page result|{"index": 0,"size": 1,"total_data": 1,"total_pages": 1}|
|region_failures|[]region_failure_object|False|The regions where the request failed to execute. The presence of items in this field indicates partial failure|[{"region": "US", "message": "example_message"}]|
|rrns|[]string|False|A list of the rrns for the found alerts|["rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:alert:1:12345678-abcd-cdef-1234-12345abg", "rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:alert:1:12345678-abcd-cdef-1234-12345abd"]|
  
Example output:

```
{
  "aggregates": [
    {
      "buckets": [
        {
          "count": 1,
          "keys": [
            "example_key"
          ]
        }
      ],
      "field_ids": [
        "example_field"
      ],
      "name": "example_id",
      "type": "BUCKET",
      "value": "example_value"
    }
  ],
  "alerts": [
    {
      "alerted_at": "2023-12-04T13:59:06.349Z",
      "created_at": "2023-12-04T13:59:06.757109Z",
      "disposition": "UNDECIDED",
      "external_id": "12345678-abcd-cdef-1234-12345abc",
      "external_source": "IDR ABA",
      "fields": [],
      "ingested_at": "2023-12-04T13:59:06.751813Z",
      "investigation_rrn": "rrn:investigation:us:12345678-abcd-cdef-1234-12345abc:investigation:ABCDEFGHI",
      "organization": {
        "customer_id": "12345678-abcd-cdef-1234-12345abc",
        "customer_name": "Dev Test",
        "flags": [],
        "id": "12345678-abcd-cdef-1234-12345abc",
        "name": "Dev Test",
        "product_token": "abcdefgh12345abc",
        "region": "us1"
      },
      "permissions": {
        "canEdit": false
      },
      "priority": "LOW",
      "responsibility": "MDR",
      "rrn": "rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:alert:1:12345678-abcd-cdef-1234-12345abc",
      "rule": {
        "mitre_tcodes": [
          "Credential Access",
          "T1110"
        ],
        "rrn": "rrn:cba:::detection-rule:ABCDEFGHIJK",
        "version_rrn": "rrn:cba:::detection-rule:version:ABCDEFGHIJK"
      },
      "rule_keys_of_interest": [
        {
          "key": "result",
          "values": [
            "SUCCESS"
          ]
        },
        {
          "key": "account",
          "values": [
            "test_account"
          ]
        },
        {
          "key": "geoip_country_code",
          "values": [
            "US"
          ]
        },
        {
          "key": "source_ip",
          "values": [
            "1.1.1.1"
          ]
        }
      ],
      "rule_matching_keys": [
        {
          "key": "entryType",
          "values": [
            "ingress_auth"
          ]
        },
        {
          "key": "orgId",
          "values": [
            "12345678-abcd-cdef-1234-12345abc"
          ]
        }
      ],
      "status": "OPEN",
      "tags": [],
      "title": "MVD Verification",
      "type": "MVD Verification",
      "updated_at": "2023-12-05T11:51:39.29059Z",
      "version": 8
    }
  ],
  "metadata": {
    "index": 0,
    "size": 1,
    "total_data": 1,
    "total_pages": 1
  },
  "region_failures": [
    {
      "message": "example_message",
      "region": "US"
    }
  ],
  "rrns": [
    "rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:alert:1:12345678-abcd-cdef-1234-12345abg",
    "rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:alert:1:12345678-abcd-cdef-1234-12345abd"
  ]
}
```

#### Search Investigations

This action is used to allows to search for investigations that match the given criteria

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|end_time|date|None|False|The ending time when investigations were created|None|2020-09-06 12:07:55.136666+00:00|None|None|
|index|integer|0|True|Zero-based index of the page to retrieve, where value must be greater than or equal to 0|None|1|None|None|
|search|[]object|None|False|The criteria for which entities to return|None|[{"field": "Example Field", "operator": "EQUALS", "value": "Test"}]|None|None|
|size|integer|100|True|Amount of data for a page to retrieve, where its value must be greater than 0 or less than or equal to 100|None|100|None|None|
|sort|[]object|None|False|The sorting information, where possible field values are RRN, PRIORITY, CREATED TIME, and order values are ASC, DESC|None|[{"field": "Example Field", "order": "ASC"}]|None|None|
|start_time|date|None|False|The starting time from when investigations were created|None|2020-09-06 12:07:55.136666+00:00|None|None|
  
Example input:

```
{
  "end_time": "2020-09-06 12:07:55.136666+00:00",
  "index": 0,
  "search": [
    {
      "field": "Example Field",
      "operator": "EQUALS",
      "value": "Test"
    }
  ],
  "size": 100,
  "sort": [
    {
      "field": "Example Field",
      "order": "ASC"
    }
  ],
  "start_time": "2020-09-06 12:07:55.136666+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|investigations|[]investigation|True|A list of found investigations|[{"assignee": {"email": "user@example.com", "name": "Ellen Example"}, "created_time": "2018-06-06T16:56:42Z", "disposition": "BENIGN", "first_alert_time": "2018-06-06T16:56:42Z", "last_accessed": "2018-06-06T16:56:42Z", "latest_alert_time": "2018-06-06T16:56:42Z", "organization_id": "174e4f99-2ac7-4481-9301-4d24c34baf06", "priority": "CRITICAL", "rrn": "rrn:example", "source": "ALERT", "status": "OPEN", "title": "Example Title"}]|
|metadata|investigation_metadata|True|The pagination parameters used to generate this page result|{'index': 0, 'size': 1, 'total_data': 1, 'total_pages': 1}|
  
Example output:

```
{
  "investigations": [
    {
      "assignee": {
        "email": "user@example.com",
        "name": "Ellen Example"
      },
      "created_time": "2018-06-06T16:56:42Z",
      "disposition": "BENIGN",
      "first_alert_time": "2018-06-06T16:56:42Z",
      "last_accessed": "2018-06-06T16:56:42Z",
      "latest_alert_time": "2018-06-06T16:56:42Z",
      "organization_id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
      "priority": "CRITICAL",
      "rrn": "rrn:example",
      "source": "ALERT",
      "status": "OPEN",
      "title": "Example Title"
    }
  ],
  "metadata": {
    "index": 0,
    "size": 1,
    "total_data": 1,
    "total_pages": 1
  }
}
```

#### Set Disposition of Investigation

This action is used to allows to change the disposition of the investigation with the given ID or RRN

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|disposition|string|None|True|Investigation's disposition|["BENIGN", "MALICIOUS", "NOT_APPLICABLE"]|BENIGN|None|None|
|id|string|None|True|The ID or RRN of the investigation to change the disposition of|None|rrn:investigation:example:11111111-1111-1111-1111-111111111111:investigation:11111111|None|None|
  
Example input:

```
{
  "disposition": "BENIGN",
  "id": "rrn:investigation:example:11111111-1111-1111-1111-111111111111:investigation:11111111"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|investigation|investigation|True|The investigation for which the disposition was set|{'assignee': {'email': 'user@example.com', 'name': 'Ellen Example'}, 'created_time': '2018-06-06T16:56:42Z', 'disposition': 'BENIGN', 'first_alert_time': '2018-06-06T16:56:42Z', 'last_accessed': '2018-06-06T16:56:42Z', 'latest_alert_time': '2018-06-06T16:56:42Z', 'organization_id': '174e4f99-2ac7-4481-9301-4d24c34baf06', 'priority': 'CRITICAL', 'rrn': 'rrn:example', 'source': 'ALERT', 'status': 'OPEN', 'title': 'Example Title'}|
  
Example output:

```
{
  "investigation": {
    "assignee": {
      "email": "user@example.com",
      "name": "Ellen Example"
    },
    "created_time": "2018-06-06T16:56:42Z",
    "disposition": "BENIGN",
    "first_alert_time": "2018-06-06T16:56:42Z",
    "last_accessed": "2018-06-06T16:56:42Z",
    "latest_alert_time": "2018-06-06T16:56:42Z",
    "organization_id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
    "priority": "CRITICAL",
    "rrn": "rrn:example",
    "source": "ALERT",
    "status": "OPEN",
    "title": "Example Title"
  }
}
```

#### Set Priority of Investigation

This action is used to allows to change the priority of the investigation with the given ID or RRN

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|The ID or RRN of the investigation to change the priority of|None|rrn:investigation:example:11111111-1111-1111-1111-111111111111:investigation:11111111|None|None|
|priority|string|None|True|Investigation's priority|["UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL"]|LOW|None|None|
  
Example input:

```
{
  "id": "rrn:investigation:example:11111111-1111-1111-1111-111111111111:investigation:11111111",
  "priority": "LOW"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|investigation|investigation|True|The investigation for which the priority was set|{'assignee': {'email': 'user@example.com', 'name': 'Ellen Example'}, 'created_time': '2018-06-06T16:56:42Z', 'disposition': 'BENIGN', 'first_alert_time': '2018-06-06T16:56:42Z', 'last_accessed': '2018-06-06T16:56:42Z', 'latest_alert_time': '2018-06-06T16:56:42Z', 'organization_id': '174e4f99-2ac7-4481-9301-4d24c34baf06', 'priority': 'CRITICAL', 'rrn': 'rrn:example', 'source': 'ALERT', 'status': 'OPEN', 'title': 'Example Title'}|
  
Example output:

```
{
  "investigation": {
    "assignee": {
      "email": "user@example.com",
      "name": "Ellen Example"
    },
    "created_time": "2018-06-06T16:56:42Z",
    "disposition": "BENIGN",
    "first_alert_time": "2018-06-06T16:56:42Z",
    "last_accessed": "2018-06-06T16:56:42Z",
    "latest_alert_time": "2018-06-06T16:56:42Z",
    "organization_id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
    "priority": "CRITICAL",
    "rrn": "rrn:example",
    "source": "ALERT",
    "status": "OPEN",
    "title": "Example Title"
  }
}
```

#### Set Status of Investigation

This action is used to set the status of the investigation with the given ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|The ID of the investigation to change the status of|None|174e4f99-2ac7-4481-9301-4d24c34baf06|None|None|
|status|string|CLOSED|True|The new status for the investigation|["OPEN", "CLOSED"]|CLOSED|None|None|
  
Example input:

```
{
  "id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
  "status": "CLOSED"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|investigation|investigation|True|The investigation for which the status was set|{'assignee': {'email': 'user@example.com', 'name': 'Ellen Example'}, 'created_time': '2018-06-06T16:56:42Z', 'disposition': 'BENIGN', 'first_alert_time': '2018-06-06T16:56:42Z', 'last_accessed': '2018-06-06T16:56:42Z', 'latest_alert_time': '2018-06-06T16:56:42Z', 'organization_id': '174e4f99-2ac7-4481-9301-4d24c34baf06', 'priority': 'CRITICAL', 'rrn': 'rrn:example', 'source': 'ALERT', 'status': 'OPEN', 'title': 'Example Title'}|
  
Example output:

```
{
  "investigation": {
    "assignee": {
      "email": "user@example.com",
      "name": "Ellen Example"
    },
    "created_time": "2018-06-06T16:56:42Z",
    "disposition": "BENIGN",
    "first_alert_time": "2018-06-06T16:56:42Z",
    "last_accessed": "2018-06-06T16:56:42Z",
    "latest_alert_time": "2018-06-06T16:56:42Z",
    "organization_id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
    "priority": "CRITICAL",
    "rrn": "rrn:example",
    "source": "ALERT",
    "status": "OPEN",
    "title": "Example Title"
  }
}
```

#### Update Alert

This action is used to updates information for a single alert

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_rrn|string|None|True|The unique identifier of the alert|None|rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:alert:1:12345678-abcd-cdef-1234-12345abg|None|None|
|assignee_id|string|None|False|The new user to assign to the alert|None|8205375a-1234-4652-8098-870d656bc693|None|None|
|comment|string|None|False|The reason for updating the alert, which is captured in the alert audit log for tracking purposes|None|Updated alert priority by automation through InsightConnect|None|None|
|disposition|string|None|False|The alert disposition|["", "UNMAPPED", "UNDECIDED", "MALICIOUS", "BENIGN", "UNKNOWN", "NOT_APPLICABLE", "SECURITY_TEST", "FALSE_POSITIVE"]|MALICIOUS|None|None|
|investigation_rrn|string|None|False|The RRN of the investigation to add the alert to|None|rrn:investigation:us:12345678-abcd-cdef-1234-12345abc:investigation:ABCDEFGHI|None|None|
|priority|string|None|False|The alert priority|["", "UNMAPPED", "INFO", "LOW", "MEDIUM", "HIGH", "CRITICAL"]|INFO|None|None|
|status|string|None|False|The alert status|["", "UNMAPPED", "OPEN", "INVESTIGATING", "WAITING", "CLOSED"]|OPEN|None|None|
  
Example input:

```
{
  "alert_rrn": "rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:alert:1:12345678-abcd-cdef-1234-12345abg",
  "assignee_id": "8205375a-1234-4652-8098-870d656bc693",
  "comment": "Updated alert priority by automation through InsightConnect",
  "disposition": "MALICIOUS",
  "investigation_rrn": "rrn:investigation:us:12345678-abcd-cdef-1234-12345abc:investigation:ABCDEFGHI",
  "priority": "INFO",
  "status": "OPEN"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alert|alert_object|False|The updated alert|{'alerted_at': '2023-12-04T13:59:06.349Z', 'created_at': '2023-12-04T13:59:06.757109Z', 'disposition': 'UNDECIDED', 'external_id': '12345678-abcd-cdef-1234-12345abc', 'external_source': 'IDR ABA', 'fields': [], 'ingested_at': '2023-12-04T13:59:06.751813Z', 'investigation_rrn': 'rrn:investigation:us:12345678-abcd-cdef-1234-12345abc:investigation:ABCDEFGHI', 'organization': {'customer_id': '12345678-abcd-cdef-1234-12345abc', 'customer_name': 'Dev Test', 'flags': [], 'id': '12345678-abcd-cdef-1234-12345abc', 'name': 'Dev Test', 'product_token': 'abcdefgh12345abc', 'region': 'us1'}, 'permissions': {'canEdit': 'false'}, 'priority': 'LOW', 'responsibility': 'MDR', 'rrn': 'rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:alert:1:12345678-abcd-cdef-1234-12345abc', 'rule': {'mitre_tcodes': ['Credential Access', 'T1110'], 'rrn': 'rrn:cba:::detection-rule:ABCDEFGHIJK', 'version_rrn': 'rrn:cba:::detection-rule:version:ABCDEFGHIJK'}, 'rule_keys_of_interest': [{'key': 'result', 'values': ['SUCCESS']}, {'key': 'account', 'values': ['test_account']}, {'key': 'geoip_country_code', 'values': ['US']}, {'key': 'source_ip', 'values': ['1.1.1.1']}], 'rule_matching_keys': [{'key': 'entryType', 'values': ['ingress_auth']}, {'key': 'orgId', 'values': ['12345678-abcd-cdef-1234-12345abc']}], 'status': 'OPEN', 'tags': [], 'title': 'MVD Verification', 'type': 'MVD Verification', 'updated_at': '2023-12-05T11:51:39.29059Z', 'version': 8}|
  
Example output:

```
{
  "alert": {
    "alerted_at": "2023-12-04T13:59:06.349Z",
    "created_at": "2023-12-04T13:59:06.757109Z",
    "disposition": "UNDECIDED",
    "external_id": "12345678-abcd-cdef-1234-12345abc",
    "external_source": "IDR ABA",
    "fields": [],
    "ingested_at": "2023-12-04T13:59:06.751813Z",
    "investigation_rrn": "rrn:investigation:us:12345678-abcd-cdef-1234-12345abc:investigation:ABCDEFGHI",
    "organization": {
      "customer_id": "12345678-abcd-cdef-1234-12345abc",
      "customer_name": "Dev Test",
      "flags": [],
      "id": "12345678-abcd-cdef-1234-12345abc",
      "name": "Dev Test",
      "product_token": "abcdefgh12345abc",
      "region": "us1"
    },
    "permissions": {
      "canEdit": "false"
    },
    "priority": "LOW",
    "responsibility": "MDR",
    "rrn": "rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:alert:1:12345678-abcd-cdef-1234-12345abc",
    "rule": {
      "mitre_tcodes": [
        "Credential Access",
        "T1110"
      ],
      "rrn": "rrn:cba:::detection-rule:ABCDEFGHIJK",
      "version_rrn": "rrn:cba:::detection-rule:version:ABCDEFGHIJK"
    },
    "rule_keys_of_interest": [
      {
        "key": "result",
        "values": [
          "SUCCESS"
        ]
      },
      {
        "key": "account",
        "values": [
          "test_account"
        ]
      },
      {
        "key": "geoip_country_code",
        "values": [
          "US"
        ]
      },
      {
        "key": "source_ip",
        "values": [
          "1.1.1.1"
        ]
      }
    ],
    "rule_matching_keys": [
      {
        "key": "entryType",
        "values": [
          "ingress_auth"
        ]
      },
      {
        "key": "orgId",
        "values": [
          "12345678-abcd-cdef-1234-12345abc"
        ]
      }
    ],
    "status": "OPEN",
    "tags": [],
    "title": "MVD Verification",
    "type": "MVD Verification",
    "updated_at": "2023-12-05T11:51:39.29059Z",
    "version": 8
  }
}
```

#### Update Investigation

This action is used to allows to update existing investigation by ID or RRN

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|disposition|string|None|False|Investigation's disposition|["", "BENIGN", "MALICIOUS", "NOT_APPLICABLE"]|BENIGN|None|None|
|email|string|None|False|A user's email address for investigation to be assigned|None|user@example.com|None|None|
|id|string|None|True|The identifier of investigation to be update (ID or RRN)|None|rrn:investigation:example:11111111-1111-1111-1111-111111111111:investigation:11111111|None|None|
|priority|string|None|False|Investigation's priority|["", "UNSPECIFIED", "LOW", "MEDIUM", "HIGH", "CRITICAL"]|LOW|None|None|
|status|string|None|False|Investigation's status|["", "OPEN", "INVESTIGATING", "CLOSED"]|OPEN|None|None|
|title|string|None|False|Investigation's title|None|Example Title|None|None|
  
Example input:

```
{
  "disposition": "BENIGN",
  "email": "user@example.com",
  "id": "rrn:investigation:example:11111111-1111-1111-1111-111111111111:investigation:11111111",
  "priority": "LOW",
  "status": "OPEN",
  "title": "Example Title"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|investigation|investigation|True|The body of the specified investigation|{'assignee': {'email': 'user@example.com', 'name': 'Ellen Example'}, 'created_time': '2018-06-06T16:56:42Z', 'disposition': 'BENIGN', 'first_alert_time': '2018-06-06T16:56:42Z', 'last_accessed': '2018-06-06T16:56:42Z', 'latest_alert_time': '2018-06-06T16:56:42Z', 'organization_id': '174e4f99-2ac7-4481-9301-4d24c34baf06', 'priority': 'CRITICAL', 'rrn': 'rrn:example', 'source': 'ALERT', 'status': 'OPEN', 'title': 'Example Title'}|
  
Example output:

```
{
  "investigation": {
    "assignee": {
      "email": "user@example.com",
      "name": "Ellen Example"
    },
    "created_time": "2018-06-06T16:56:42Z",
    "disposition": "BENIGN",
    "first_alert_time": "2018-06-06T16:56:42Z",
    "last_accessed": "2018-06-06T16:56:42Z",
    "latest_alert_time": "2018-06-06T16:56:42Z",
    "organization_id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
    "priority": "CRITICAL",
    "rrn": "rrn:example",
    "source": "ALERT",
    "status": "OPEN",
    "title": "Example Title"
  }
}
```

#### Upload Attachment

This action is used to upload an attachment

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|file_content|bytes|None|True|Base64 encoded content of the file|None|dGVzdA==|None|None|
|filename|string|None|True|Name of the file, which should contain the file extension|None|test.txt|None|None|
  
Example input:

```
{
  "file_content": "dGVzdA==",
  "filename": "test.txt"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|attachment|[]attachment|False|Attachment details|[{"rrn": "rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890", "creator": {"type": "USER", "name": "Example User"}, "created_time": "2022-08-19T13:00:58.645Z", "file_name": "test.txt", "mime_type": "text/plain", "size": 4, "scan_status": "CLEAN"}]|
|success|boolean|True|Whether the action was successful or not|True|
  
Example output:

```
{
  "attachment": [
    {
      "created_time": "2022-08-19T13:00:58.645Z",
      "creator": {
        "name": "Example User",
        "type": "USER"
      },
      "file_name": "test.txt",
      "mime_type": "text/plain",
      "rrn": "rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890",
      "scan_status": "CLEAN",
      "size": 4
    }
  ],
  "success": true
}
```
### Triggers


#### Get New Alerts

This trigger is used to get New Alerts

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|aggregates|[]aggregate_object|None|False|Aggregations to apply for all matching results|None|[{}]|None|None|
|field_ids|[]string|None|False|Additional fields to include for each alert. No additional fields are included if field_ids is empty|None|[]|None|None|
|frequency|integer|15|False|Poll frequency in seconds|None|15|None|None|
|leql|string|None|False|The LEQL 'WHERE' clause to match against|None||None|None|
|terms|[]terms_object|None|False|The search terms to match against|None||None|None|
  
Example input:

```
{
  "aggregates": [
    {}
  ],
  "field_ids": [],
  "frequency": 15,
  "leql": "",
  "terms": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alert|alert_object|False|Alert|{'alerted_at': '2023-12-04T13:59:06.349Z', 'created_at': '2023-12-04T13:59:06.757109Z', 'disposition': 'UNDECIDED', 'external_id': '12345678-abcd-cdef-1234-12345abc', 'external_source': 'IDR ABA', 'fields': [], 'ingested_at': '2023-12-04T13:59:06.751813Z', 'investigation_rrn': 'rrn:investigation:us:12345678-abcd-cdef-1234-12345abc:investigation:ABCDEFGHI', 'organization': {'customer_id': '12345678-abcd-cdef-1234-12345abc', 'customer_name': 'Dev Test', 'flags': [], 'id': '12345678-abcd-cdef-1234-12345abc', 'name': 'Dev Test', 'product_token': 'abcdefgh12345abc', 'region': 'us1'}, 'permissions': {'canEdit': 'false'}, 'priority': 'LOW', 'responsibility': 'MDR', 'rrn': 'rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:alert:1:12345678-abcd-cdef-1234-12345abc', 'rule': {'mitre_tcodes': ['Credential Access', 'T1110'], 'rrn': 'rrn:cba:::detection-rule:ABCDEFGHIJK', 'version_rrn': 'rrn:cba:::detection-rule:version:ABCDEFGHIJK'}, 'rule_keys_of_interest': [{'key': 'result', 'values': ['SUCCESS']}, {'key': 'account', 'values': ['test_account']}, {'key': 'geoip_country_code', 'values': ['US']}, {'key': 'source_ip', 'values': ['1.1.1.1']}], 'rule_matching_keys': [{'key': 'entryType', 'values': ['ingress_auth']}, {'key': 'orgId', 'values': ['12345678-abcd-cdef-1234-12345abc']}], 'status': 'OPEN', 'tags': [], 'title': 'MVD Verification', 'type': 'MVD Verification', 'updated_at': '2023-12-05T11:51:39.29059Z', 'version': 8}|
  
Example output:

```
{
  "alert": {
    "alerted_at": "2023-12-04T13:59:06.349Z",
    "created_at": "2023-12-04T13:59:06.757109Z",
    "disposition": "UNDECIDED",
    "external_id": "12345678-abcd-cdef-1234-12345abc",
    "external_source": "IDR ABA",
    "fields": [],
    "ingested_at": "2023-12-04T13:59:06.751813Z",
    "investigation_rrn": "rrn:investigation:us:12345678-abcd-cdef-1234-12345abc:investigation:ABCDEFGHI",
    "organization": {
      "customer_id": "12345678-abcd-cdef-1234-12345abc",
      "customer_name": "Dev Test",
      "flags": [],
      "id": "12345678-abcd-cdef-1234-12345abc",
      "name": "Dev Test",
      "product_token": "abcdefgh12345abc",
      "region": "us1"
    },
    "permissions": {
      "canEdit": "false"
    },
    "priority": "LOW",
    "responsibility": "MDR",
    "rrn": "rrn:alerts:us1:12345678-abcd-cdef-1234-12345abc:alert:1:12345678-abcd-cdef-1234-12345abc",
    "rule": {
      "mitre_tcodes": [
        "Credential Access",
        "T1110"
      ],
      "rrn": "rrn:cba:::detection-rule:ABCDEFGHIJK",
      "version_rrn": "rrn:cba:::detection-rule:version:ABCDEFGHIJK"
    },
    "rule_keys_of_interest": [
      {
        "key": "result",
        "values": [
          "SUCCESS"
        ]
      },
      {
        "key": "account",
        "values": [
          "test_account"
        ]
      },
      {
        "key": "geoip_country_code",
        "values": [
          "US"
        ]
      },
      {
        "key": "source_ip",
        "values": [
          "1.1.1.1"
        ]
      }
    ],
    "rule_matching_keys": [
      {
        "key": "entryType",
        "values": [
          "ingress_auth"
        ]
      },
      {
        "key": "orgId",
        "values": [
          "12345678-abcd-cdef-1234-12345abc"
        ]
      }
    ],
    "status": "OPEN",
    "tags": [],
    "title": "MVD Verification",
    "type": "MVD Verification",
    "updated_at": "2023-12-05T11:51:39.29059Z",
    "version": 8
  }
}
```

#### Get New Investigations

This trigger is used to get New Investigations

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|15|False|Poll frequency in seconds|None|15|None|None|
|search|[]object|None|False|The criteria for which entities to return|None|[{"field": "Example Field", "operator": "EQUALS", "value": "Test"}]|None|None|
  
Example input:

```
{
  "frequency": 15,
  "search": [
    {
      "field": "Example Field",
      "operator": "EQUALS",
      "value": "Test"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|investigation|investigation|True|A new investigation|{'assignee': {'email': 'user@example.com', 'name': 'Ellen Example'}, 'created_time': '2018-06-06T16:56:42Z', 'disposition': 'BENIGN', 'first_alert_time': '2018-06-06T16:56:42Z', 'last_accessed': '2018-06-06T16:56:42Z', 'latest_alert_time': '2018-06-06T16:56:42Z', 'organization_id': '174e4f99-2ac7-4481-9301-4d24c34baf06', 'priority': 'CRITICAL', 'rrn': 'rrn:example', 'source': 'ALERT', 'status': 'OPEN', 'title': 'Example Title'}|
  
Example output:

```
{
  "investigation": {
    "assignee": {
      "email": "user@example.com",
      "name": "Ellen Example"
    },
    "created_time": "2018-06-06T16:56:42Z",
    "disposition": "BENIGN",
    "first_alert_time": "2018-06-06T16:56:42Z",
    "last_accessed": "2018-06-06T16:56:42Z",
    "latest_alert_time": "2018-06-06T16:56:42Z",
    "organization_id": "174e4f99-2ac7-4481-9301-4d24c34baf06",
    "priority": "CRITICAL",
    "rrn": "rrn:example",
    "source": "ALERT",
    "status": "OPEN",
    "title": "Example Title"
  }
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**investigation_metadata**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Index|integer|None|False|The zero-based index of the page retrieved|None|
|Size|integer|None|False|The size of the page requested|None|
|Total Data|integer|None|False|The total number of results available with the given filter parameters|None|
|Total Pages|integer|None|False|The total number of pages available with the given filter parameters|None|
  
**alert**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alert Source|string|None|False|The source of the alert|None|
|Alert Type|string|None|False|The type of an alert|None|
|Alert Type Description|string|None|False|An optional description of this type of alert|None|
|Created Time|string|None|False|The time when the alert was created|None|
|Detection Rule RRN|string|None|False|The time when the alert was created|None|
|First Event Time|string|None|False|The time the first event involved in this alert occurred|None|
|Alert ID|string|None|False|The identifier of an alert|None|
|Latest Event Time|string|None|False|The time the latest event involved in this alert occurred|None|
|Title|string|None|False|The title of the alert|None|
  
**assignee**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Email|string|None|False|The email of the assigned user|None|
|Name|string|None|False|The name of the assigned user|None|
  
**investigation**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Assignee|assignee|None|False|The user assigned to this investigation, if any|None|
|Created Time|string|None|False|The time the investigation was created as an ISO formatted timestamp|None|
|Disposition|string|None|False|The disposition of this investigation, where possible values are BENIGN, MALICIOUS, NOT_APPLICABLE, and UNSPECIFIED|None|
|First Alert Time|string|None|False|The create time of the first alert belonging to this investigation|None|
|Last Accessed|string|None|False|The time investigation was last viewed or modified|None|
|Latest Alert Time|string|None|False|The create time of the most recent alert belonging to this investigation|None|
|Organization ID|string|None|False|The id of the organization that owns this investigation|None|
|Priority|string|None|False|The investigations priority, where possible values are CRITICAL, HIGH, MEDIUM, LOW, and UNKNOWN|None|
|Responsibility|string|None|False|Indicates the party responsible for the alert.|None|
|RRN|string|None|False|The RRN of the investigation|None|
|Source|string|None|False|The source of this investigation|None|
|Status|string|None|False|The status of the investigation|None|
|Tags|[]string|None|False|The tags applied to the alert.|None|
|Title|string|None|False|Investigation title|None|
  
**threat**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Indicator Count|integer|None|False|The number of indicators in this threat|2|
|Name|string|None|False|The name of the threat|bad-vrius|
|Note|string|None|False|Notes about this threat|test|
|Published|boolean|None|False|Indicates whether this threat has been published|False|
  
**link**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HREF|string|None|None|HREF|None|
|Relation|string|None|None|Relation|None|
  
**eventData**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|As Signature Creation Time|string|None|False|As signature creation time|None|
|As Signature Version|string|None|False|As signature version|None|
|AV Signature Creation Time|string|None|False|AV signature creation time|None|
|AV Signature Version|string|None|False|AV signature version|None|
|BMS State|string|None|False|BMS state|None|
|Data|[]object|None|False|Data|None|
|Engine Version|string|None|False|Engine version|None|
|IOAV State|string|None|False|IOAV state|None|
|Last As Signature Age|string|None|False|Last as signature age|None|
|Last AV Signature Age|string|None|False|Last AV signature age|None|
|Last Full Scan Age|string|None|False|Last full scan age|None|
|Last Full Scan End Time|string|None|False|Last full scan end time|None|
|Last Full Scan Source|string|None|False|Last full scan source|None|
|Last Full Scan Start Time|string|None|False|Last full scan start time|None|
|Last Quick Scan Age|string|None|False|Last quick scan age|None|
|Last Quick Scan End Time|string|None|False|Last quick scan end time|None|
|Last Quick Scan Source|string|None|False|Last quick scan source|None|
|Last Quick Scan Start Time|string|None|False|Last quick scan start time|None|
|NRI Engine Version|string|None|False|NRI engine version|None|
|NRI Signature Version|string|None|False|NRI signature version|None|
|OA State|string|None|False|OA state|None|
|Platform Version|string|None|False|Platform version|None|
|Product Name|string|None|False|Product name|None|
|Product Status|string|None|False|Product status|None|
|RTP State|string|None|False|RTP state|None|
  
**message**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Destination Asset|string|None|None|None|None|
|Destination Asset Address|string|None|None|None|None|
|Destination Local Account|string|None|None|None|None|
|Logon Type|string|None|None|None|None|
|New Authentication|string|None|None|None|None|
|Result|string|None|None|None|None|
|Service|string|None|None|None|None|
|Source Asset Address|string|None|None|None|None|
|Source JSON|source_json|None|None|None|None|
|Timestamp|string|None|None|None|None|
  
**events**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Labels|[]string|None|None|List of labels|None|
|Links|[]link|None|None|Links|None|
|Log ID|string|None|None|Log ID|None|
|Message|message|None|None|Message|None|
|Sequence Number|integer|None|None|Sequence number|None|
|Sequence Number String|string|None|None|Sequence number string|None|
|Timestamp|integer|None|None|Timestamp|None|
  
**results_statistics**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|LEQL|object|None|False|The LEQL 'WHERE' clause to match against|None|
|Logs|array|None|False|Holds the Log ID of the matching log entry|None|
|Search Stats|object|None|False|Holds data regarding the query execution|None|
|statistics|statistics|None|False|Holds the overall statistical results|None|
  
**statistics**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|All Exact Results|boolean|None|False|Boolean indicating whether groups are calculated approximately (approximated if a groupby query involves over 10,000 groups)|None|
|Cardinality|integer|None|False|Always 0|None|
|From|integer|None|False|The start of the time range for the query, as a UNIX timestamp in milliseconds|None|
|Granularity|integer|None|False|The time window in milliseconds for each time slice in the time series|None|
|Groups|[]object|None|False|Holds the overall result for each group in a 'groupby' query|None|
|Groups Time Series|[]object|None|False|For 'groupby' queries, holds the timeseries object for each group|None|
|Key|string|None|False|The key which the function of the 'calculate' clause is applied to|None|
|Others|object|None|False|Not yet implemented|None|
|Stats|object|None|False|Holds the overall result when query does not contain a 'groupby' clause|None|
|Status|integer|None|False|Holds a status code for the query, potentially different from the status code of the response|None|
|Time Series|object|None|False|Holds the query results for each timeslice (each partition of the time_range), for non-'groupby' queries|None|
|To|integer|None|False|The end of the time range for the query, as a UNIX timestamp in milliseconds|None|
|Type|string|None|False|The type of function performed, for example, "count", "max", "average", "standarddeviation"|None|
  
**source_json**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Computer Name|string|None|False|None|None|
|Event Code|integer|None|False|None|None|
|Event Data|eventData|None|False|None|None|
|Insertion Strings|[]string|None|False|Insertion Strings|None|
|Is Domain Controller|boolean|None|False|None|None|
|SID|string|None|False|None|None|
|Source Name|string|None|False|Source Name|None|
|Time Written|string|None|False|None|None|
  
**links**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|HREF|string|None|False|HREF|None|
|REL|string|None|False|REL|None|
  
**user_data**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Platform Managed|string|None|False|Platform managed|None|
  
**logsets_info**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|ID|None|
|IP Address|string|None|False|The IP address that the Log Search system receives log entries from|None|
|Links|[]links|None|False|Links|None|
|Name|string|None|False|Name|None|
|Retention Period|string|None|False|Log retention period|None|
|RRN|string|None|False|RRN|None|
|Source Type|string|None|False|A categorization of logs which defines how log entries are received by a server|None|
|Structures|[]string|None|False|Structures are internal entities which may apply some additional processing to log entries written to this log|None|
|Token Seed|string|None|False|The seed used to generate the log token (if the logs source type is "token")|None|
|Tokens|[]string|None|False|The log token(s) used for writing to the log. This only applies to token type logs|None|
|User Data|user_data|None|False|User data|None|
  
**during**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|From|integer|None|False|Time range start value|None|
|Time Range|string|None|False|Time range description|None|
|To|integer|None|False|Time range end value|None|
  
**leql**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|During|during|None|False|Query duration data|None|
|Statement|string|None|False|Logentries Query Language statement|None|
  
**query**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Query ID|None|
|LEQL|leql|None|False|LEQL data|None|
|Logs|[]string|None|False|Query logs|None|
|Name|string|None|False|Query name|None|
  
**creator**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|The name of who or what created a resource|None|
|Type|string|None|False|A type that denotes who or what created a resource|None|
  
**attachment**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created Time|date|None|False|The time the attachment was created as an ISO formatted timestamp|None|
|Creator|creator|None|False|Who or what created the attachment|None|
|File Name|string|None|False|The original filename of the uploaded attachment|None|
|MIME Type|string|None|False|The MIME type of the attachment|None|
|RRN|string|None|False|The RRN of the attachment|None|
|Scan Status|string|None|False|The scan status of the attachment, indicating whether the attachment has been scanned and, if so, the result. INFECTED or PENDING attachments may not be downloaded|None|
|Size|integer|None|False|The size in bytes of the attachment|None|
  
**comment**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attachments|[]attachment|None|False|List of attachments associated with this comment|[{"rrn": "rrn:collaboration:us:44d88612-fea8-a8f3-6de8-2e1278abb02f:attachment:1234567890", "creator": {"type": "USER", "name": "Example User"}, "created_time": "2022-08-19T13:00:58.645Z", "file_name": "test.txt", "mime_type": "text/plain", "size": 4, "scan_status": "CLEAN"}]|
|Body|string|None|False|The body of the comment|None|
|Created Time|date|None|False|The time the comment was created as an ISO formatted timestamp|None|
|Creator|creator|None|False|Who or what created the comment|None|
|RRN|string|None|False|The RRN of the comment|None|
|Target|string|None|False|The target where the comment belongs to|None|
|Visibility|string|None|False|Who can view the comment|None|
  
**user**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Domiain|string|None|False|The domain this user is associated with.|None|
|First Name|string|None|False|The first name of this user, if known.|None|
|Last Name|string|None|False|The last name of this user, if known.|None|
|Name|string|None|False|The name of this user.|None|
|RRN|string|None|False|The unique identifier for this user.|None|
  
**asset**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|The user friendly name for this asset.|None|
|RRN|string|None|False|The unique identifier for this asset.|None|
  
**alert_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alerted at|string|None|False|The timestamp associated with the underlying event or evidence that InsightIDR detected in the source system.|None|
|Assignee|assignee_object|None|False|The user assigned to the alert.|None|
|Created at|string|None|False|The timestamp when InsightIDR finished creating the alert in the Alerts experience.|None|
|Disposition|string|None|False|The disposition of the alert.|None|
|External ID|string|None|False|The identifier of the alert in the system, identified by external_source.|None|
|External Source|string|None|False|The source of the alert.|None|
|Fields|[]object|None|False|Additional fields specified in the request.|None|
|Ingested at|string|None|False|The timestamp when the event or evidence from the source system was received by the Alerts experience in InsightIDR.|None|
|Investigation RRN|string|None|False|The RRN of the investigation that the alert is part of.|None|
|Monitored|boolean|None|False|Indicates whether monitoring for the organization was active at the time of the alert.|None|
|organization|organization_object|None|False|The details of the organization that the alert belongs to.|None|
|Permissions|permissions_object|None|False|The permissions the current caller has for the alert.|None|
|Priority|string|None|False|The priority of the alert.|None|
|Responsibility|string|None|False|Indicates the party responsible for the alert.|None|
|RRN|string|None|False|The unique identifier for this alert.|None|
|Rule|rule_object|None|False|The details about the alert's detection rule.|None|
|Rule Keys of Interest|[]object|None|False|The keys and values used when matching detection rule logic.|None|
|Rule Matching Keys|[]object|None|False|The keys and values used when matching detection rule logic.|None|
|Status|string|None|False|The status of the alert.|None|
|Status Transitions|status_transitions_object|None|False|Information about when the alert status was changed.|None|
|Tags|[]string|None|False|The tags applied to the alert.|None|
|Title|string|None|False|The description of the alert.|None|
|Type|string|None|False|The type of alert.|None|
|Updated at|string|None|False|The timestamp when the alert was last updated in InsightIDR.|None|
|Version|integer|None|False|The version of the alert.|None|
  
**organization_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Customer Code|string|None|False|The customer code for the organization.|None|
|Customer Group|string|None|False|The customer group responsible for the organization.|None|
|Customer ID|string|None|False|The unique identifier of the customer.|None|
|Customer Name|string|None|False|The display name of the customer.|None|
|Flags|[]string|None|False|The flags associated with the organization.|None|
|ID|string|None|False|The unique identifier of the organization.|None|
|Name|string|None|False|The display name of the organization.|None|
|Product Token|string|None|False|The Platform productToken associated with the organization's product.|None|
|Region|string|None|False|The region that the organization is assigned to.|None|
  
**rule_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Mitre Tcodes|[]string|None|False|The mitreTCodes associated with the detection rule.|None|
|Name|string|None|False|The display name for the detection rule.|None|
|RRN|string|None|False|The unique identifier of the detection rule.|None|
|Version RRN|string|None|False|The version RRN of the detection rule.|None|
  
**assignee_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|At|string|None|False|The timestamp when the user was assigned.|None|
|Email|string|None|False|The email address of the user.|None|
|First Name|string|None|False|The displayed first name of the user.|None|
|ID|string|None|False|The unique identifier of the user.|None|
|Last Name|string|None|False|The displayed last name of the user.|None|
  
**status_transitions_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Seconds to first closed|integer|None|False|The number of seconds between when the alert was created and when the alert moved to the CLOSED status.|None|
|Seconds to first investigating|integer|None|False|The number of seconds between when the alert was created and when the alert moved to the INVESTIGATING status, or when it moved directly to the CLOSED status.|None|
  
**permissions_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Can edit|boolean|None|False|Indicates whether the current caller can edit the alert.|None|
  
**terms_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Field IDs|[]string|None|False|The identifier of the field for the values to match against.|[]|
|Operator|string|EQUALS|False|The search operator to apply.|EQUALS|
|Terms|[]|None|True|The value for the field to match against. Values are separated by an OR operator.|[]|
  
**aggregate_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Count order|string|None|True|The sort order for the count.|None|
|Fields|[]field_object|None|True|The field identifiers to aggregate by.|None|
|Name|string|None|True|The identifier of the aggregation, which you specify. Identifiers should be unique and are included in the response.|None|
|Type|string|MEDIAN|False|Type of aggregate.|None|
  
**region_failure_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|message|string|None|False|A description of the failure.|example_message|
|region|string|None|False|The region where the request failed.|US|
  
**bucket_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|count|integer|None|False|The number of alerts in this bucket.|1|
|keys|[]string|None|False|The values for the selected field identifiers in this bucket, in matching order.|["example_key"]|
  
**aggregate_response_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Buckets|[]bucket_object|None|None|The buckets that the aggregation results are grouped into.|[{"keys": ["example_key"], "count": 1}]|
|Field IDs|[]string|None|False|The field identifiers that were aggregated by.|["example_field"]|
|Name|string|None|False|The identifier of the aggregation, which was specified in the request.|example_id|
|Type|string|None|False|Type of aggregate.|BUCKET|
|Value|string|None|False|The single-value result of the requested query.|example_value|
  
**field_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Field ID|string|None|True|The field to aggregate on.|None|
|Interval|string|None|False|For fields that support histograms (such as number and date fields), the interval for each bucket. For date fields, the interval is interpreted as the number of seconds.|None|
|Order|string|None|True|The sort order for the fields.|None|
  
**sort_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Field ID|string|None|True|The field to aggregate on.|None|
|Order|string|None|True|The sort order for the fields.|None|
  
**evidence_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created at|string|None|False|The timestamp when the evidence was created.|None|
|Data|object|None|False|The evidence data.|None|
|Evented at|string|None|False|The timestamp when the event that triggered the alert occurred in the source system.|None|
|External Source|string|None|False|The source of the evidence.|None|
|External Type|string|None|False|The type of the evidence.|None|
|RRN|string|None|False|The unique RRN of the evidence.|None|
|Updated at|string|None|False|The timestamp when the evidence was last updated.|None|
|Version|integer|None|False|The version of the evidence.|None|
  
**actor_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Display Name|string|None|False|The display name of the actor (for example, John Doe or user@example.com).|None|
|ID|string|None|False|The identifier of the actor.|None|
|RRN|string|None|False|The unique RRN of the actor.|None|
|Type|string|None|False|The type of actor (for example, ASSET, ACCOUNT, or IP_ADDRESS).|None|
|User ID|string|None|False|User ID for an actor.|None|
  
**search_accounts_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Field|string|None|False|The field to search within.|None|
|Operator|string|None|False|The search operation to perform. All operators are case-insensitive when operating on Strings|None|
|Value|string|None|False|The value to search for.|None|
  
**sort_accounts_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Field|string|None|False|The field to sort by.|None|
|Order|string|None|False|The sorting direction. Sorting is case-insensitive when sorting Strings.|None|
  
**account_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Authentication Service|string|None|True|The service to which this account is tied, which is responsible for authenticating this account.|None|
|Disabled|boolean|None|True|The unique RRN of the account.|None|
|Domain|string|None|False|The domain that this account is associated with.|None|
|Name|string|None|True|The name for this account.|None|
|RRN|string|None|True|The unique RRN of the account.|None|
|User|user_object|None|True|The user this account is associated with.|None|
  
**user_object**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|True|The name for this user.|None|
|RRN|string|None|True|The unique RRN of the user.|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 11.0.8 - Remove use of session from the connection object to prevent session timeouts.
* 11.0.7 - Adding request id to the plugin for traceability
* 11.0.6 - Updated `disposition` values for `create_investigation` and `update_alert` action | SDK bump to 6.3.6
* 11.0.5 - Added new disposition of the alert
* 11.0.4 - Added support for parsing improperly formatted JSON-like strings | SDK bump to 6.3.3
* 11.0.3 - Added log entry validation using regular expressions | SDK bump to 6.2.6
* 11.0.2 - Updating descriptions for 'set_priority_of_investigation' & 'set_disposition_of_investigation'
* 11.0.1 - Updating `Advanced Query on Log` description
* 11.0.0 - Updating schema for query actions (`advanced_query_on_log`, `advanced_query_on_log_set` & `query`) to account for missing keys/invalid mapping in the schema
* 10.3.4 - Bumping requirements.txt | SDK bump to 6.2.2
* 10.3.3 - Bumping requirements.txt | SDK bump to 6.2.0
* 10.3.2 - Initial updates for fedramp compliance | Updated SDK to the latest version
* 10.3.1 - `Advanced Query On Log / Log Set` - Fixed issue where results >500 returned none | Update SDK
* 10.3.0 - New Action Added: Update Alert
* 10.2.0 - New Trigger Added: `Get New Investigations`
* 10.1.1 - Updated query schemas to allow message to be an object or string | Updated SDK
* 10.1.0 - New Trigger Added: `Get New Alerts`
* 10.0.0 - Actions: `List Investigations` Sort options updated | `Get Investigation`, `List Investigations`, `Create Investigation`, `Update Investigation` `Set Priority of Investigation`, `Set Disposition of Investigation`, `Set Status of Investigation Action`, `Assign User to Investigation`, `Seach Investigations`, `Get a Log`, `Get All Logs`, `Search Alerts` output now includes additional fields
* 9.0.0 - Actions: `Advanced Query On Log` - Now allows for either log id or log name to be used
* 8.2.0 - Actions: `Advanced Query On Log Set` and `Advanced Query On Log` - optimized data fetching mechanisms
* 8.1.1 - Extended error logging for all the actions
* 8.1.0 - New actions added: `Search Accounts` and `Get Account Information`
* 8.0.0 - Update schema for `Investigation` and `Statistics` | Update dependency for aiohttp | New actions added `Get Alert Information`, `Search Alerts`, `Retrieve Evidence for a Single Alert` and `Retrieve Actors for a Single Alert` | Fixed issue where index was not getting correctly passed through to `List Investigations` action from the user
* 7.0.0 - Action: `Advanced Query On Log Set` - Fixed error where statistical queries would always return 0.0 | Action: `Advanced Query On Log Set` - Increase the maximum results returned from 50 to 500 |  Action: `Advanced Query On Log` - Add new output type for statistical queries | Updated schemas to ensure all are correct and added new schema validation to unit tests
* 6.0.1 - Action: `Advanced Query On Log` - Increase the maximum results returned from 50 to 500
* 6.0.0 - Action: `Advanced Query On Log Set` - Add new output type for statistical queries.
* 5.1.2 - Action: `Advanced Query on Log Set` - Fix JSONDecoderError | Action: `Query` - Update spec and help.md to show it queries log IDs, not query IDs
* 5.1.1 - Action: `List Investigations` - Now receiving size input | Actions: `Advanced Query On Log` & `Advanced Query On Log Set` - Acronym LQL has been updated to LEQL
* 5.1.0 - New actions added: `get_user_information` and `get_asset_information`
* 5.0.1 - Update the endpoint `get_a_saved_query` reaches out to
* 5.0.0 - Update `List Investigations` inputs
* 4.4.1 - `List Alerts for Investigation`: fix issue with retrieving `detection_rule_rrn`
* 4.4.0 - `List Alerts for Investigation`: changed schema output for `detection_rule_rrn`
* 4.3.0 - `Query`: Add new parameter `most_recent_first`
* 4.2.1 - `Create Investigation`, `Update Investigation`: Fix issue where action fails when email address field is not empty
* 4.2.0 - New action added: Replace Indicators
* 4.1.1 - Advanced Query on Log Set Action: Updated EndPoint Agent enum to Endpoint Agent in log_set
* 4.1.0 - Add new actions `List Comments`, `Create Comment`, `Delete Comment`, `List Attachments`, `Upload Attachment`, `Download Attachment`, `Delete Attachment`, `Get Attachment Information`
* 4.0.1 - Fix issue with `Get Query Results` and `Get All Saved Queries` actions
* 4.0.0 - Add new actions Create Investigation, Search Investigations, Update Investigation, Set Investigation Priority, Set Investigation Disposition, and List Alerts for Investigation | Update actions List Investigations, Set Status of Investigation, Assign User to Investigation | Enabled cloud
* 3.2.0 - Add new actions Get A Saved Query and Get All Saved Queries
* 3.1.5 - Patch issue parsing labels in Advanced Query on Log and Advanced Query on Log Set actions
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

* [Rapid7 InsightIDR](https://www.rapid7.com/products/insightidr/)

## References

* [Rapid7 InsightIDR](https://www.rapid7.com/products/insightidr/)