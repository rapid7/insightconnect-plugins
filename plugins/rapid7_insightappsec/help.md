# Description

DAST capabilities and InsightConnects automation prowess can help you simplify your SDLC Process with this scan management plugin. The need for automation becomes paramount in the fast moving landscape of modern web scanning and automating you web app scanning with this plugin can save you loads of time to allow you to focus on remediating issues to get your app into product faster!

# Key Features

* Create and configure scans
* Run scans and return results
* Get Vulnerabilities
* Get Vulnerability
* Get Vulnerability Discoveries
* Get Vulnerability Discovery
* Create Schedule

# Requirements

* Requires an API Key from Insight platform

# Supported Product Versions

* Rapid7 InsightAppSec 19.08.2024

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|The API key for InsightAppSec|None|abc12345-abc1-2345-abc1-abc123456789|None|None|
|url|string|https://us.api.insight.rapid7.com|True|The region specific URL endpoint for InsightAppSec|None|https://us.api.insight.rapid7.com|None|None|

Example input:

```
{
  "api_key": "abc12345-abc1-2345-abc1-abc123456789",
  "url": "https://us.api.insight.rapid7.com"
}
```

## Technical Details

### Actions


#### Create Scan Config

This action is used to create a new scan configuration

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|app_id|string|None|True|App UUID|None|78c85b01-2a23-404d-ac5a-18324d8e3bda|None|None|
|attack_template_id|string|None|True|Attack template UUID|None|11111111-0000-0000-0000-000000000000|None|None|
|config_description|string|None|False|The description of the scan configuration|None|Description for scan config|None|None|
|config_name|string|None|True|The name of the scan configuration|None|Scan Config 1|None|None|
  
Example input:

```
{
  "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda",
  "attack_template_id": "11111111-0000-0000-0000-000000000000",
  "config_description": "Description for scan config",
  "config_name": "Scan Config 1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|integer|False|Status code of the request|201|
  
Example output:

```
{
  "status": 201
}
```

#### Create Schedule

This action is used to create a new schedule

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|enabled|boolean|True|True|Whether the schedule is enabled|None|True|None|None|
|firstStart|date|None|True|The first start date and time of the schedule|None|2023-03-17T13:00:19Z|None|None|
|frequency|frequencyInput|None|False|The frequency describes how (and if) the schedule should repeat. If frequency and recurrence rule are given then the recurrence rule will be used|None|{}|None|None|
|lastStart|date|None|False|The last start date and time of the schedule|None|2023-04-17T13:00:19Z|None|None|
|name|string|None|True|Name of the schedule|None|Example Schedule|None|None|
|rrule|string|None|False|The recurrence rule describes how (and if) the schedule should repeat. If frequency and recurrence rule are given then the recurrence rule will be used|None|FREQ=WEEKLY;INTERVAL=1;BYDAY=TU;COUNT=10|None|None|
|scanConfigId|string|None|True|The scan config ID of the schedule|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|None|None|
  
Example input:

```
{
  "enabled": true,
  "firstStart": "2023-03-17T13:00:19Z",
  "frequency": {},
  "lastStart": "2023-04-17T13:00:19Z",
  "name": "Example Schedule",
  "rrule": "FREQ=WEEKLY;INTERVAL=1;BYDAY=TU;COUNT=10",
  "scanConfigId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete Scan

This action is used to delete a scan

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|scan_id|string|None|True|The scans UUID|None|b0b343aa-7fc2-4a9a-bc18-5ac64df7791a|None|None|
  
Example input:

```
{
  "scan_id": "b0b343aa-7fc2-4a9a-bc18-5ac64df7791a"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|integer|False|Status code of the request|204|
  
Example output:

```
{
  "status": 204
}
```

#### Delete Scan Config

This action is used to delete an existing scan configuration

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|scan_config_id|string|None|True|Scan configuration UUID|None|4569288e-2bb4-416e-a4ee-4f7add18afe0|None|None|
  
Example input:

```
{
  "scan_config_id": "4569288e-2bb4-416e-a4ee-4f7add18afe0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|integer|False|Status code of the request|204|
  
Example output:

```
{
  "status": 204
}
```

#### Get Scan

This action is used to get a scan

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|scan_id|string|None|True|The scans UUID|None|b0b343aa-7fc2-4a9a-bc18-5ac64df7791a|None|None|
  
Example input:

```
{
  "scan_id": "b0b343aa-7fc2-4a9a-bc18-5ac64df7791a"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|scan|scan|False|Information on the scan|{'id': 'b0b343aa-7fc2-4a9a-bc18-5ac64df7791a', 'app_id': '78c85b01-2a23-404d-ac5a-18324d8e3bda', 'scan_config_id': 'a709c972-cb1f-4790-bfce-6ab74653900c', 'submitter': {'type': 'USER', 'id': '5b278d63-8fac-4910-978e-8e281039b790'}, 'submit_time': '2019-01-08T22:04:46.402', 'completion_time': '2019-01-08T22:53:38.385', 'status': 'COMPLETE', 'failure_reason': '', 'links': [{'rel': 'self', 'href': 'https://us.api.insight.rapid7.com:443/ias/v1/scans/b0b343aa-7fc2-4a9a-bc18-5ac64df7791a'}]}|
  
Example output:

```
{
  "scan": {
    "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda",
    "completion_time": "2019-01-08T22:53:38.385",
    "failure_reason": "",
    "id": "b0b343aa-7fc2-4a9a-bc18-5ac64df7791a",
    "links": [
      {
        "href": "https://us.api.insight.rapid7.com:443/ias/v1/scans/b0b343aa-7fc2-4a9a-bc18-5ac64df7791a",
        "rel": "self"
      }
    ],
    "scan_config_id": "a709c972-cb1f-4790-bfce-6ab74653900c",
    "status": "COMPLETE",
    "submit_time": "2019-01-08T22:04:46.402",
    "submitter": {
      "id": "5b278d63-8fac-4910-978e-8e281039b790",
      "type": "USER"
    }
  }
}
```

#### Get Scan Config

This action is used to get a scan configuration

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|scan_config_id|string|None|True|Scan configuration UUID|None|6a33ae79-5ebd-44a9-9a0a-f269876e90c9|None|None|
  
Example input:

```
{
  "scan_config_id": "6a33ae79-5ebd-44a9-9a0a-f269876e90c9"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|app_id|string|False|App UUID|78c85b01-2a23-404d-ac5a-18324d8e3bda|
|attack_template_id|string|False|Attack template UUID|11111111-0000-0000-0000-000000000000|
|config_description|string|False|The description of the scan configuration|testing update|
|config_name|string|False|The name of the scan configuration|update_test|
|errors|[]string|False|A list of errors that detail any current validation failures|["Seed URL list must not be empty", "Crawling Scope Constraint list must not be empty"]|
|id|string|False|The UUID of the scan configuration|a709c972-cb1f-4790-bfce-6ab74653900c|
|links|[]link|False|A list of links|[{"rel": "self", "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs/a709c972-cb1f-4790-bfce-6ab74653900c"}]|
  
Example output:

```
{
  "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda",
  "attack_template_id": "11111111-0000-0000-0000-000000000000",
  "config_description": "testing update",
  "config_name": "update_test",
  "errors": [
    "Seed URL list must not be empty",
    "Crawling Scope Constraint list must not be empty"
  ],
  "id": "a709c972-cb1f-4790-bfce-6ab74653900c",
  "links": [
    {
      "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs/a709c972-cb1f-4790-bfce-6ab74653900c",
      "rel": "self"
    }
  ]
}
```

#### Get Scan Configs

This action is used to get a page of scan configurations, based on supplied pagination parameters

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|index|integer|None|False|The page index to start form. If blank, index will be 0|None|0|None|None|
|size|integer|None|False|The number of entries on each page. If blank, size will be 50|None|0|None|None|
|sort|string|None|False|How to sort the scan configs. If blank, sort will be alphabetical by scan config name|None|scanconfig.name,DESC|None|None|
  
Example input:

```
{
  "index": 0,
  "size": 0,
  "sort": "scanconfig.name,DESC"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|scan_configs|[]scan_config|False|A list of scan configurations|[{"id": "6a33ae79-5ebd-44a9-9a0a-f269876e90c9", "config_name": "Test_create_action", "config_description": "test create", "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda", "attack_template_id": "11111111-0000-0000-0000-000000000000", "errors": ["Seed URL list must not be empty", "Crawling Scope Constraint list must not be empty"], "links": [{"rel": "self", "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs/6a33ae79-5ebd-44a9-9a0a-f269876e90c9"}]}, {"id": "0173ce58-369b-4d89-87d6-ef9cb59f8e38", "config_name": "Test_create_action", "config_description": "test create", "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda", "attack_template_id": "11111111-0000-0000-0000-000000000000", "errors": ["Seed URL list must not be empty", "Crawling Scope Constraint list must not be empty"], "links": [{"rel": "self", "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs/0173ce58-369b-4d89-87d6-ef9cb59f8e38"}]}, {"id": "a709c972-cb1f-4790-bfce-6ab74653900c", "config_name": "update_test", "config_description": "testing update", "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda", "attack_template_id": "11111111-0000-0000-0000-000000000000", "errors": [], "links": [{"rel": "self", "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs/a709c972-cb1f-4790-bfce-6ab74653900c"}]}]|
  
Example output:

```
{
  "scan_configs": [
    {
      "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda",
      "attack_template_id": "11111111-0000-0000-0000-000000000000",
      "config_description": "test create",
      "config_name": "Test_create_action",
      "errors": [
        "Seed URL list must not be empty",
        "Crawling Scope Constraint list must not be empty"
      ],
      "id": "6a33ae79-5ebd-44a9-9a0a-f269876e90c9",
      "links": [
        {
          "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs/6a33ae79-5ebd-44a9-9a0a-f269876e90c9",
          "rel": "self"
        }
      ]
    },
    {
      "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda",
      "attack_template_id": "11111111-0000-0000-0000-000000000000",
      "config_description": "test create",
      "config_name": "Test_create_action",
      "errors": [
        "Seed URL list must not be empty",
        "Crawling Scope Constraint list must not be empty"
      ],
      "id": "0173ce58-369b-4d89-87d6-ef9cb59f8e38",
      "links": [
        {
          "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs/0173ce58-369b-4d89-87d6-ef9cb59f8e38",
          "rel": "self"
        }
      ]
    },
    {
      "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda",
      "attack_template_id": "11111111-0000-0000-0000-000000000000",
      "config_description": "testing update",
      "config_name": "update_test",
      "errors": [],
      "id": "a709c972-cb1f-4790-bfce-6ab74653900c",
      "links": [
        {
          "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs/a709c972-cb1f-4790-bfce-6ab74653900c",
          "rel": "self"
        }
      ]
    }
  ]
}
```

#### Get Scan Engine Events

This action is used to get the engine events from a scan

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|scan_id|string|None|True|Scan UUID|None|c762adbe-1636-4c70-9787-5f22c2dc5af8|None|None|
  
Example input:

```
{
  "scan_id": "c762adbe-1636-4c70-9787-5f22c2dc5af8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|events|[]event_log|False|An array of event logs and their dates|[{"time": "2019-01-09T20:18:39.536", "event": "Scan is awaiting scheduling"}]|
  
Example output:

```
{
  "events": [
    {
      "event": "Scan is awaiting scheduling",
      "time": "2019-01-09T20:18:39.536"
    }
  ]
}
```

#### Get Scan Execution Details

This action is used to get real-time details of the execution of a scan

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|scan_id|string|None|True|Scan UUID|None|c762adbe-1636-4c70-9787-5f22c2dc5af8|None|None|
  
Example input:

```
{
  "scan_id": "c762adbe-1636-4c70-9787-5f22c2dc5af8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|details|scan_details|False|Detailed information about the scan|{'logged_in': False, 'links_in_queue': 0, 'links_crawled': 0, 'attacks_in_queue': 0, 'attacked': 0, 'vulnerable': 0, 'requests': 0, 'failed_requests': 0, 'network_speed': 0, 'drip_delay': 0}|
  
Example output:

```
{
  "details": {
    "attacked": 0,
    "attacks_in_queue": 0,
    "drip_delay": 0,
    "failed_requests": 0,
    "links_crawled": 0,
    "links_in_queue": 0,
    "logged_in": false,
    "network_speed": 0,
    "requests": 0,
    "vulnerable": 0
  }
}
```

#### Get Scan Platform Events

This action is used to get the platform events from a scan

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|scan_id|string|None|True|Scan UUID|None|c762adbe-1636-4c70-9787-5f22c2dc5af8|None|None|
  
Example input:

```
{
  "scan_id": "c762adbe-1636-4c70-9787-5f22c2dc5af8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|events|[]event_log|False|An array of event logs and their dates|[{"time": "2019-01-09T20:18:47.751", "event": "Sending scan state action START"}, {"time": "2019-01-09T20:18:50.464", "event": "Sending scan state action CANCEL"}]|
  
Example output:

```
{
  "events": [
    {
      "event": "Sending scan state action START",
      "time": "2019-01-09T20:18:47.751"
    },
    {
      "event": "Sending scan state action CANCEL",
      "time": "2019-01-09T20:18:50.464"
    }
  ]
}
```

#### Get Scans

This action is used to get a page of scans, based on supplied pagination parameters

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|index|integer|None|False|The page index to start form. If blank, index will be 0|None|0|None|None|
|size|integer|None|False|The number of entries on each page. If blank, size will be 50|None|50|None|None|
|sort|string|None|False|How to sort the scans. If blank, sort will be alphabetical by scan name|None|scan.submit_time,DESC|None|None|
  
Example input:

```
{
  "index": 0,
  "size": 50,
  "sort": "scan.submit_time,DESC"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|scans|[]scan|False|A list of scans|[{"id": "b0b343aa-7fc2-4a9a-bc18-5ac64df7791a", "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda", "scan_config_id": "a709c972-cb1f-4790-bfce-6ab74653900c", "submitter": {"type": "USER", "id": "5b278d63-8fac-4910-978e-8e281039b790"}, "submit_time": "2019-01-08T22:04:46.402", "completion_time": "2019-01-08T22:53:38.385", "status": "COMPLETE", "failure_reason": "", "links": [{"rel": "self", "href": "https://us.api.insight.rapid7.com:443/ias/v1/scans/b0b343aa-7fc2-4a9a-bc18-5ac64df7791a"}]}]|
  
Example output:

```
{
  "scans": [
    {
      "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda",
      "completion_time": "2019-01-08T22:53:38.385",
      "failure_reason": "",
      "id": "b0b343aa-7fc2-4a9a-bc18-5ac64df7791a",
      "links": [
        {
          "href": "https://us.api.insight.rapid7.com:443/ias/v1/scans/b0b343aa-7fc2-4a9a-bc18-5ac64df7791a",
          "rel": "self"
        }
      ],
      "scan_config_id": "a709c972-cb1f-4790-bfce-6ab74653900c",
      "status": "COMPLETE",
      "submit_time": "2019-01-08T22:04:46.402",
      "submitter": {
        "id": "5b278d63-8fac-4910-978e-8e281039b790",
        "type": "USER"
      }
    }
  ]
}
```

#### Get Vulnerabilities

This action is used to get a page of Vulnerabilities, based on supplied pagination parameters. The default sort for 
Vulnerabilities is 'severity' (descending); for a full list of sortable properties, refer to the Search Catalog detailed
 in the Search API

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|index|integer|None|False|The 0-based index of the page of data desired (default: 0)|None|1|None|None|
|pageToken|string|None|False|The page token, used as an alternative to index|None|NDM0NTk0NTIyOjo6X1M6OjpiYW5hbmFz|None|None|
|size|integer|None|False|The size of the page of data desired (min: 1, max: 1000, default: 50)|None|1|None|None|
|sort|string|None|False|The sort terms and (optional) directions for the desired ordering of data|None|vulnerability.severity,DESC|None|None|
  
Example input:

```
{
  "index": 1,
  "pageToken": "NDM0NTk0NTIyOjo6X1M6OjpiYW5hbmFz",
  "size": 1,
  "sort": "vulnerability.severity,DESC"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|[]vulnerabilityItem|False|List of vulnerability data|[{"app": {"id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"}, "severity": "SAFE", "vectorString": "example", "newlyDiscovered": True, "insightUiUrl": "sample.com", "lastDiscovered": "2021-08-03T14:07:37", "firstDiscovered": "2021-08-03T14:07:37", "vulnerabilityScore": 1.5, "variances": [{"attackExchanges": [{"request": "example", "response": "example", "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"}], "originalValue": "example", "attackValue": "example", "attack": {"id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"}, "module": {"id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"}, "proofDescription": "example", "originalExchange": {"request": "example", "response": "example", "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"}, "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08", "proof": "example", "message": "example"}], "links": [{"profile": "example", "rel": "example", "name": "example", "href": "example.com"}], "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08", "rootCause": {"method": "GET", "parameter": "example", "url": "example.com"}, "status": "UNREVIEWED"}]|
|links|[]linkDetails|False|List of links|[{"profile": "example", "rel": "example", "name": "example", "href": "example.com"}]|
|metadata|pageMetadata|False|Page metadata|{'size': 1, 'totalData': 1, 'pageToken': 'NDM0NTk0NTIyOjo6X1M6OjpiYW5hbmFz', 'index': 1, 'sort': 'scan.submit_time,DESC,scan.status', 'totalPages': 1}|
  
Example output:

```
{
  "data": [
    {
      "app": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      },
      "firstDiscovered": "2021-08-03T14:07:37",
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "insightUiUrl": "sample.com",
      "lastDiscovered": "2021-08-03T14:07:37",
      "links": [
        {
          "href": "example.com",
          "name": "example",
          "profile": "example",
          "rel": "example"
        }
      ],
      "newlyDiscovered": true,
      "rootCause": {
        "method": "GET",
        "parameter": "example",
        "url": "example.com"
      },
      "severity": "SAFE",
      "status": "UNREVIEWED",
      "variances": [
        {
          "attack": {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
          },
          "attackExchanges": [
            {
              "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
              "request": "example",
              "response": "example"
            }
          ],
          "attackValue": "example",
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "message": "example",
          "module": {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
          },
          "originalExchange": {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "request": "example",
            "response": "example"
          },
          "originalValue": "example",
          "proof": "example",
          "proofDescription": "example"
        }
      ],
      "vectorString": "example",
      "vulnerabilityScore": 1.5
    }
  ],
  "links": [
    {
      "href": "example.com",
      "name": "example",
      "profile": "example",
      "rel": "example"
    }
  ],
  "metadata": {
    "index": 1,
    "pageToken": "NDM0NTk0NTIyOjo6X1M6OjpiYW5hbmFz",
    "size": 1,
    "sort": "scan.submit_time,DESC,scan.status",
    "totalData": 1,
    "totalPages": 1
  }
}
```

#### Get Vulnerability

This action is used to get a vulnerability

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|vulnerabilityId|string|None|True|Unique identifier for vulnerability|None|497f6eca-6276-4993-bfeb-53cbbbba6f08|None|None|
  
Example input:

```
{
  "vulnerabilityId": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vulnerability|vulnerabilityItem|False|Vulnerability item|{'app': {'id': '497f6eca-6276-4993-bfeb-53cbbbba6f08'}, 'severity': 'SAFE', 'vectorString': 'example', 'newlyDiscovered': True, 'insightUiUrl': 'sample.com', 'lastDiscovered': '2021-08-03T14:07:37', 'firstDiscovered': '2021-08-03T14:07:37', 'vulnerabilityScore': 1.5, 'variances': [{'attackExchanges': [{'request': 'example', 'response': 'example', 'id': '497f6eca-6276-4993-bfeb-53cbbbba6f08'}], 'originalValue': 'example', 'attackValue': 'example', 'attack': {'id': '497f6eca-6276-4993-bfeb-53cbbbba6f08'}, 'module': {'id': '497f6eca-6276-4993-bfeb-53cbbbba6f08'}, 'proofDescription': 'example', 'originalExchange': {'request': 'example', 'response': 'example', 'id': '497f6eca-6276-4993-bfeb-53cbbbba6f08'}, 'id': '497f6eca-6276-4993-bfeb-53cbbbba6f08', 'proof': 'example', 'message': 'example'}], 'links': [{'profile': 'example', 'rel': 'example', 'name': 'example', 'href': 'example.com'}], 'id': '497f6eca-6276-4993-bfeb-53cbbbba6f08', 'rootCause': {'method': 'GET', 'parameter': 'example', 'url': 'example.com'}, 'status': 'UNREVIEWED'}|
  
Example output:

```
{
  "vulnerability": {
    "app": {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
    },
    "firstDiscovered": "2021-08-03T14:07:37",
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "insightUiUrl": "sample.com",
    "lastDiscovered": "2021-08-03T14:07:37",
    "links": [
      {
        "href": "example.com",
        "name": "example",
        "profile": "example",
        "rel": "example"
      }
    ],
    "newlyDiscovered": true,
    "rootCause": {
      "method": "GET",
      "parameter": "example",
      "url": "example.com"
    },
    "severity": "SAFE",
    "status": "UNREVIEWED",
    "variances": [
      {
        "attack": {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
        },
        "attackExchanges": [
          {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "request": "example",
            "response": "example"
          }
        ],
        "attackValue": "example",
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "message": "example",
        "module": {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
        },
        "originalExchange": {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "request": "example",
          "response": "example"
        },
        "originalValue": "example",
        "proof": "example",
        "proofDescription": "example"
      }
    ],
    "vectorString": "example",
    "vulnerabilityScore": 1.5
  }
}
```

#### Get Vulnerability Discoveries

This action is used to get a page of Vulnerability Discoveries, based on supplied pagination parameters. The default 
sort for Vulnerability Discoveries is 'discovered' (descending)

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|index|integer|None|False|The 0-based index of the page of data desired (default: 0)|None|1|None|None|
|pageToken|string|None|False|The page token, used as an alternative to index|None|NDM0NTk0NTIyOjo6X1M6OjpiYW5hbmFz|None|None|
|size|integer|None|False|The size of the page of data desired (min: 1, max: 1000, default: 50)|None|1|None|None|
|sort|string|None|False|The sort terms and (optional) directions for the desired ordering of data|None|vulnerabilitydiscovery.discovered,DESC|None|None|
|vulnerabilityId|string|None|True|Unique identifier for vulnerability|None|497f6eca-6276-4993-bfeb-53cbbbba6f08|None|None|
  
Example input:

```
{
  "index": 1,
  "pageToken": "NDM0NTk0NTIyOjo6X1M6OjpiYW5hbmFz",
  "size": 1,
  "sort": "vulnerabilitydiscovery.discovered,DESC",
  "vulnerabilityId": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|[]discoveryItem|False|Vulnerability discovery items|[{"id": "58972aa5-aa97-455e-90b7-cf569dbd75d0", "vulnerability": {"id": "58972aa5-aa97-455e-90b7-cf569dbd75d5"}, "scan": {"id": "68972aa5-aa97-455e-90b7-cf569dbd75d5"}, "discovered": "2023-01-01T11:11:11.111111", "links": [{"rel": "self", "href": "https://example.com"}]}]|
|links|[]linkDetails|False|List of links|[{"rel": "self", "href": "https://example.com"}]|
|metadata|pageMetadata|False|Page metadata|{'index': 0, 'size': 1, 'sort': 'vulnerabilitydiscovery.discovered,DESC', 'totalData': 2, 'totalPages': 2, 'pageToken': 'MTYyNTcyNTY0ODo6Ol'}|
  
Example output:

```
{
  "data": [
    {
      "discovered": "2023-01-01T11:11:11.111111",
      "id": "58972aa5-aa97-455e-90b7-cf569dbd75d0",
      "links": [
        {
          "href": "https://example.com",
          "rel": "self"
        }
      ],
      "scan": {
        "id": "68972aa5-aa97-455e-90b7-cf569dbd75d5"
      },
      "vulnerability": {
        "id": "58972aa5-aa97-455e-90b7-cf569dbd75d5"
      }
    }
  ],
  "links": [
    {
      "href": "https://example.com",
      "rel": "self"
    }
  ],
  "metadata": {
    "index": 0,
    "pageToken": "MTYyNTcyNTY0ODo6Ol",
    "size": 1,
    "sort": "vulnerabilitydiscovery.discovered,DESC",
    "totalData": 2,
    "totalPages": 2
  }
}
```

#### Get Vulnerability Discovery

This action is used to get a vulnerability discovery

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|vulnerabilityDiscoveryId|string|None|True|Unique identifier for discovery|None|497f6eca-6276-4993-bfeb-53cbbbba6f08|None|None|
|vulnerabilityId|string|None|True|Unique identifier for vulnerability|None|497f6eca-6276-4993-bfeb-53cbbbba6f08|None|None|
  
Example input:

```
{
  "vulnerabilityDiscoveryId": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "vulnerabilityId": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vulnerabilityDiscovery|discoveryItem|False|Vulnerability discovery item|None|
  
Example output:

```
{
  "vulnerabilityDiscovery": {
    "Discovered": "2021-08-03T14:07:37",
    "Scan": {}
  }
}
```

#### Submit Scan

This action is used to submit a new scan

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|scan_config_id|string|None|True|UUID of the scan config to use|None|a709c972-cb1f-4790-bfce-6ab74653900c|None|None|
  
Example input:

```
{
  "scan_config_id": "a709c972-cb1f-4790-bfce-6ab74653900c"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|integer|False|Status code of the request|204|
  
Example output:

```
{
  "status": 204
}
```

#### Submit Scan Action

This action is used to submit a new scan action

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|Pause|True|Action to take|["Pause", "Resume", "Stop", "Cancel", "Authenticate"]|Pause|None|None|
|scan_id|string|None|True|Scan UUID|None|008eaffe-90ce-4de9-8601-40414391c21c|None|None|
  
Example input:

```
{
  "action": "Pause",
  "scan_id": "008eaffe-90ce-4de9-8601-40414391c21c"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|integer|False|Status code of the request|200|
  
Example output:

```
{
  "status": 200
}
```

#### Update Scan Config

This action is used to update an existing scan configuration

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|app_id|string|None|True|App UUID|None|78c85b01-2a23-404d-ac5a-18324d8e3bda|None|None|
|attack_template_id|string|None|True|Attack template UUID|None|11111111-0000-0000-0000-000000000000|None|None|
|config_description|string|None|False|The description of the scan configuration|None|Description of scan config|None|None|
|config_name|string|None|True|The name of the scan configuration|None|Scan Config 1|None|None|
|scan_config_id|string|None|True|Scan configuration UUID|None|a709c972-cb1f-4790-bfce-6ab74653900c|None|None|
  
Example input:

```
{
  "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda",
  "attack_template_id": "11111111-0000-0000-0000-000000000000",
  "config_description": "Description of scan config",
  "config_name": "Scan Config 1",
  "scan_config_id": "a709c972-cb1f-4790-bfce-6ab74653900c"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|integer|False|Status code of the request|204|
  
Example output:

```
{
  "status": 204
}
```
### Triggers


#### New Vulnerabilities

This trigger is used to get information about newly discovered vulnerabilities

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|frequency|integer|1|True|Frequency of data collection in hours. By default, data will be collected every hour|None|1|None|None|
  
Example input:

```
{
  "frequency": 1
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|vulnerabilities|[]vulnerabilityItem|False|List of newly discovered vulnerabilities|[{"id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0", "app": {"id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"}, "rootCause": {"url": "http://example.com", "parameter": "Unnamed", "method": "GET"}, "severity": "INFORMATIONAL", "status": "UNREVIEWED", "firstDiscovered": "2023-03-20T14:29:10.686575", "lastDiscovered": "2023-03-20T14:29:10.686575", "newlyDiscovered": True, "variances": [{"id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0", "originalExchange": {"id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0", "request": "GET /example/path/file.php", "response": "HTTP/1.1 200 OK\\r\\nConnection: close\\r\\nDate: Mon, 20 Mar 2023 11:47:37 GMT\\r\\n"}, "module": {"id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"}, "attack": {"id": "R_02"}, "attackValue": "test", "proof": "test", "attackExchanges": [{"id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0", "request": "GET /example/path/file.php", "response": "HTTP/1.1 200 OK\\r\\nConnection: close\\r\\nDate: Mon, 20 Mar 2023 13:49:33 GMT\\r\\n"}]}], "vectorString": "AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:N", "insightUiUrl": "https://example.com", "links": [{"rel": "self", "href": "https://example.com"}]}]|
  
Example output:

```
{
  "vulnerabilities": [
    {
      "app": {
        "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
      },
      "firstDiscovered": "2023-03-20T14:29:10.686575",
      "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
      "insightUiUrl": "https://example.com",
      "lastDiscovered": "2023-03-20T14:29:10.686575",
      "links": [
        {
          "href": "https://example.com",
          "rel": "self"
        }
      ],
      "newlyDiscovered": true,
      "rootCause": {
        "method": "GET",
        "parameter": "Unnamed",
        "url": "http://example.com"
      },
      "severity": "INFORMATIONAL",
      "status": "UNREVIEWED",
      "variances": [
        {
          "attack": {
            "id": "R_02"
          },
          "attackExchanges": [
            {
              "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
              "request": "GET /example/path/file.php",
              "response": "HTTP/1.1 200 OK\r\nConnection: close\r\nDate: Mon, 20 Mar 2023 13:49:33 GMT\r\n"
            }
          ],
          "attackValue": "test",
          "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
          "module": {
            "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
          },
          "originalExchange": {
            "id": "9de5069c-5afe-602b-2ea0-a04b66beb2c0",
            "request": "GET /example/path/file.php",
            "response": "HTTP/1.1 200 OK\r\nConnection: close\r\nDate: Mon, 20 Mar 2023 11:47:37 GMT\r\n"
          },
          "proof": "test"
        }
      ],
      "vectorString": "AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:N"
    }
  ]
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**link**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Href|string|None|False|Href|None|
|Rel|string|None|False|rel|None|
  
**submitter**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|The submitters UUID|None|
|Type|string|None|False|The type of the submitter e.g. USER|None|
  
**event_log**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Event|string|None|False|The log event|None|
|Time|date|None|False|The time at which the log event occurred|None|
  
**scan_config**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|App ID|string|None|False|App UUID|None|
|Attack Template ID|string|None|False|Attack template UUID|None|
|Description|string|None|False|The description of the scan configuration|None|
|Name|string|None|False|The name of the scan configuration|None|
|Errors|[]string|None|False|A list of errors that detail any current validation failures|None|
|UUID|string|None|False|The UUID of the scan configuration|None|
|Links|[]link|None|False|A list of links|None|
  
**scan**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|App ID|string|None|False|App UUID|None|
|Completion Time|date|None|False|The time the scan was completed|None|
|Failure Reason|string|None|False|The reason the scan may have failed|None|
|ID|string|None|False|Scan UUID|None|
|Links|[]link|None|False|A list of links|None|
|Scan Config ID|string|None|False|Scan configs UUID|None|
|Status|string|None|False|The status of the scan|None|
|Submit Time|date|None|False|The time the scan was submitted|None|
|Submitter|submitter|None|False|The submitter of the scan|None|
  
**scan_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attacked|integer|None|False|The number of attacks already performed|None|
|Attacks in Queue|integer|None|False|The number of links in the attacking queue|None|
|Drip Delay|number|None|False|The current delay between HTTP requests|None|
|Failed Requests|integer|None|False|The number of failed HTTP requests|None|
|Links Crawled|integer|None|False|The number of links already crawled|None|
|Links in Queue|integer|None|False|The number of links in the crawling queue|None|
|Logged-In|boolean|None|False|A flag which indicates if the scan is using authentication during the scan|None|
|Network Speed|number|None|False|A throughput indicator|None|
|Requests|integer|None|False|The number of HTTP requests which have been executed|None|
|Vulnerable|integer|None|False|The number of potential findings|None|
  
**objectId**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Unique identifier for object|497f6eca-6276-4993-bfeb-53cbbbba6f08|
  
**pageMetadata**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Index|integer|None|False|Page index|1|
|Page Token|string|None|False|Page token|NDM0NTk0NTIyOjo6X1M6OjpiYW5hbmFz|
|Size|integer|None|False|Page size|1|
|Sort|string|None|False|Sort details|scan.submit_time,DESC,scan.status|
|Total Data|integer|None|False|Total data|1|
|Total Pages|integer|None|False|Total pages|1|
  
**linkDetails**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Href|string|None|False|The location of the resource|example.com|
|Name|string|None|False|Name|example|
|Profile|string|None|False|Profile|example|
|Rel|string|None|False|Relationship|example|
  
**rootCause**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Method|string|None|False|The HTTP method|GET|
|Parameter|string|None|False|The parameter from the URL|example|
|URL|string|None|False|The URL|example.com|
  
**exchangeObject**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|The ID of the Exchange|497f6eca-6276-4993-bfeb-53cbbbba6f08|
|Request|string|None|False|The critical section of the request payload|example|
|Response|string|None|False|The critical section of the response payload|example|
  
**variance**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Attack|objectId|None|False|The ID of the attack|{}|
|Attack Exchanges|[]exchangeObject|None|False|The HTTP exchange executed as part of the attack|[]|
|Attack Value|string|None|False|The value of a variable used to attack|example|
|ID|string|None|False|The ID of the variance|497f6eca-6276-4993-bfeb-53cbbbba6f08|
|Message|string|None|False|A message that may highlight the result of the attack|example|
|Module|objectId|None|False|The ID of the module|{}|
|Original Exchange|exchangeObject|None|False|The HTTP exchange executed as part of the attack|{}|
|Original Value|string|None|False|The value of a variable prior to being attacked|example|
|Proof|string|None|False|A proof that may highlight the result of the attack|example|
|Proof Description|string|None|False|A description of the proof that may highlight the result of the attack|example|
  
**vulnerabilityItem**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|App|objectId|None|False|The ID of the module|{}|
|First Discovered|string|None|False|The time the vulnerability was first discovered|2021-08-03 14:07:37|
|ID|string|None|False|The ID of the vulnerability|497f6eca-6276-4993-bfeb-53cbbbba6f08|
|Insight UI URL|string|None|False|Direct link to the Vulnerability on InsightAppSec UI. Require InsightAppSec login before use|example.com|
|Last Discovered|string|None|False|The time the vulnerability was last discovered|2021-08-03 14:07:37|
|Links|[]linkDetails|None|False|List of links|[]|
|Newly Discovered|boolean|None|False|Indicates that the vulnerability has been found in the latest scan and has not been discovered before|True|
|Root Cause|rootCause|None|False|A descriptor for the location of the vulnerability|{}|
|Severity|string|None|False|The severity of the vulnerability. Expected values: 'SAFE' 'INFORMATIONAL' 'LOW' 'MEDIUM' 'HIGH'|SAFE|
|Status|string|None|False|The status of the vulnerability. Expected values: 'UNREVIEWED' 'FALSE_POSITIVE' 'VERIFIED' 'IGNORED' 'REMEDIATED' 'DUPLICATE'|UNREVIEWED|
|Variances|[]variance|None|False|Evidence found that indicates the presence of a vulnerability|[]|
|Vector String|string|None|False|Textual representation of the metric values used to determine the CVSS score|example|
|Vulnerability Score|float|None|False|CVSS score which represents the severity of an information security vulnerability|1.5|
  
**frequencyInput**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Interval|integer|1|False|The interval of the frequency|12|
|Type|string|HOURLY|False|The type of the frequency|HOURLY|
  
**discoveryItem**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Discovered|string|None|False|The time the vulnerability discovery was discovered|2021-08-03T14:07:37|
|Scan|objectId|None|False|The ID of the module|{}|


## Troubleshooting

More information about the frequency and recurrence rule parameters used in the Create Schedule action can be found [here](https://help.rapid7.com/insightappsec/en-us/api/v1/docs.html#tag/Schedules).

# Version History

* 1.2.1 - Fix broken URLs for Scans and Vulnerabilities API calls | Update SDK
* 1.2.0 - Add New Vulnerabilities trigger
* 1.1.0 - Add new actions: `Get Vulnerabilities`, `Get Vulnerability`, `Create Schedule`, `Get Vulnerability Discovery`, `Get Vulnerability Discoveries`
* 1.0.4 - Fix typo in title for Submit Scan action | Update keywords
* 1.0.3 - Send plugin name and version in the User-Agent string to vendor
* 1.0.2 - Update to v4 Python plugin runtime | Add example inputs
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

* [Rapid7 InsightAppSec](https://docs.rapid7.com/insightappsec/)

## References

* [Rapid7 InsightAppSec API](https://docs.rapid7.com/insightappsec/api-get-started)