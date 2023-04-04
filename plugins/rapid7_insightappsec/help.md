# Description

[InsightAppSec’s](https://www.rapid7.com/products/insightappsec/) DAST capabilities and InsightConnect’s automation prowess can help you simplify your SDLC Process with this scan management plugin. The need for automation becomes paramount in the fast moving landscape of modern web scanning and automating you web app scanning with this plugin can save you loads of time to allow you to focus on remediating issues to get your app into product faster!

This plugin utilizes the [Rapid7 InsightAppSec API](https://docs.rapid7.com/insightappsec/api-get-started).

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

* Rapid7 InsightAppSec

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|The API key for InsightAppSec|None|abc12345-abc1-2345-abc1-abc123456789|
|url|string|https://us.api.insight.rapid7.com|True|The region specific URL endpoint for InsightAppSec|None|https://us.api.insight.rapid7.com|

Example input:

```
{
  "api_key": {
      "secretKey": "abc12345-abc1-2345-abc1-abc123456789"
  },
  "url": "https://us.api.insight.rapid7.com"
}
```

## Technical Details

### Actions

#### Get Vulnerability Discovery

This action is used to get a vulnerability discovery.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|vulnerabilityDiscoveryId|string|None|True|Unique identifier for discovery|None|497f6eca-6276-4993-bfeb-53cbbbba6f08|
|vulnerabilityId|string|None|True|Unique identifier for vulnerability|None|497f6eca-6276-4993-bfeb-53cbbbba6f08|

Example input:

```
{
  "vulnerabilityDiscoveryId": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "vulnerabilityId": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|vulnerabilityDiscovery|discoveryItem|False|Vulnerability discovery item|{}|

Example output:

```
{
  "vulnerabilityDiscovery":{
    "id":"58972aa5-aa97-455e-90b7-cf569dbd75d0",
    "vulnerability":{
      "id":"58972aa5-aa97-455e-90b7-cf569dbd75d5"
    },
    "scan":{
      "id":"68972aa5-aa97-455e-90b7-cf569dbd75d5"
    },
    "discovered":"2023-01-01T11:11:11.111111",
    "links":[
      {
        "rel":"self",
        "href":"https://example.com"
      }
    ]
  }
}
```

#### Get Vulnerability Discoveries

This action is used to get a page of Vulnerability Discoveries, based on supplied pagination parameters. The default sort for Vulnerability Discoveries is 'discovered' (descending).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|index|integer|None|False|The 0-based index of the page of data desired (default: 0)|None|1|
|pageToken|string|None|False|The page token, used as an alternative to index|None|NDM0NTk0NTIyOjo6X1M6OjpiYW5hbmFz|
|size|integer|None|False|The size of the page of data desired (min: 1, max: 1000, default: 50)|None|1|
|sort|string|None|False|The sort terms and (optional) directions for the desired ordering of data|None|vulnerabilitydiscovery.discovered,DESC|
|vulnerabilityId|string|None|True|Unique identifier for vulnerability|None|497f6eca-6276-4993-bfeb-53cbbbba6f08|

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
|----|----|--------|-----------|-------|
|data|[]discoveryItem|False|Vulnerability discovery items|[]|
|links|[]linkDetails|False|List of links|[]|
|metadata|pageMetadata|False|Page metadata|{}|

Example output:

```
{
  "data":[
    {
      "id":"58972aa5-aa97-455e-90b7-cf569dbd75d0",
      "vulnerability":{
        "id":"58972aa5-aa97-455e-90b7-cf569dbd75d5"
      },
      "scan":{
        "id":"68972aa5-aa97-455e-90b7-cf569dbd75d5"
      },
      "discovered":"2023-01-01T11:11:11.111111",
      "links":[
        {
          "rel":"self",
          "href":"https://example.com"
        }
      ]
    }
  ],
  "metadata":{
    "index":0,
    "size":1,
    "sort":"vulnerabilitydiscovery.discovered,DESC",
    "totalData":2,
    "totalPages":2,
    "pageToken":"MTYyNTcyNTY0ODo6Ol"
  },
  "links":[
    {
      "rel":"self",
      "href":"https://example.com"
    }
  ]
}
```

#### Create Schedule

This action is used to create a new schedule.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|enabled|boolean|True|True|Whether the schedule is enabled|None|True|
|firstStart|date|None|True|The first start date and time of the schedule|None|2023-03-17T13:00:19Z|
|frequency|frequencyInput|None|False|The frequency describes how (and if) the schedule should repeat. If frequency and recurrence rule are given then the recurrence rule will be used|None|{}|
|lastStart|date|None|False|The last start date and time of the schedule|None|2023-04-17T13:00:19Z|
|name|string|None|True|Name of the schedule|None|Example Schedule|
|rrule|string|None|False|The recurrence rule describes how (and if) the schedule should repeat. If frequency and recurrence rule are given then the recurrence rule will be used|None|FREQ=WEEKLY;INTERVAL=1;BYDAY=TU;COUNT=10|
|scanConfigId|string|None|True|The scan config ID of the schedule|None|9de5069c-5afe-602b-2ea0-a04b66beb2c0|

More information about the frequency and recurrence rule parameters can be found [here](https://help.rapid7.com/insightappsec/en-us/api/v1/docs.html#tag/Schedules).

Example input:

```
{
  "enabled": true,
  "firstStart": "2023-03-17T13:00:19Z",
  "frequency": {
    "interval": 12,
    "type": "HOURLY"
  },
  "lastStart": "2023-04-17T13:00:19Z",
  "name": "New Schedule",
  "rrule": "FREQ=WEEKLY;INTERVAL=1;BYDAY=TU;COUNT=10",
  "scanConfigId": "9de5069c-5afe-602b-2ea0-a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|True|Whether the action was successful|True|

Example output:

```
{
  "success": true
}
```

#### Submit Scan

This action is used to submit a new scan.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_config_id|string|None|True|UUID of the scan config to use|None|a709c972-cb1f-4790-bfce-6ab74653900c|

Example input:

```
{
  "scan_config_id": "a709c972-cb1f-4790-bfce-6ab74653900c"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|Status code of the request|

Example output:

```
{
  "status": 201
}
```

#### Create Scan Config

This action is used to create a new scan configuration.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|app_id|string|None|True|App UUID|None|78c85b01-2a23-404d-ac5a-18324d8e3bda|
|attack_template_id|string|None|True|Attack template UUID|None|11111111-0000-0000-0000-000000000000|
|config_description|string|None|False|The description of the scan configuration|None|Description for scan config|
|config_name|string|None|True|The name of the scan configuration|None|Scan Config 1|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|Status code of the request|

Example output:

```
{
  "status": 201
}
```

#### Get Scan Config

This action is used to get a scan configuration.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_config_id|string|None|True|Scan configuration UUID|None|6a33ae79-5ebd-44a9-9a0a-f269876e90c9|

Example input:

```
{
  "scan_config_id": "6a33ae79-5ebd-44a9-9a0a-f269876e90c9"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|app_id|string|False|App UUID|
|attack_template_id|string|False|Attack template UUID|
|config_description|string|False|The description of the scan configuration|
|config_name|string|False|The name of the scan configuration|
|errors|[]string|False|A list of errors that detail any current validation failures|
|id|string|False|The UUID of the scan configuration|
|links|[]link|False|A list of links|

Example output:

```
{
  "id": "a709c972-cb1f-4790-bfce-6ab74653900c",
  "config_name": "update_test",
  "config_description": "testing update",
  "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda",
  "attack_template_id": "11111111-0000-0000-0000-000000000000",
  "errors": [
    "Seed URL list must not be empty",
    "Crawling Scope Constraint list must not be empty"
  ],
  "links": [
    {
      "rel": "self",
      "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs/a709c972-cb1f-4790-bfce-6ab74653900c"
    }
  ]
}
```

#### Update Scan Config

This action is used to update an existing scan configuration.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|app_id|string|None|True|App UUID|None|78c85b01-2a23-404d-ac5a-18324d8e3bda|
|attack_template_id|string|None|True|Attack template UUID|None|11111111-0000-0000-0000-000000000000|
|config_description|string|None|False|The description of the scan configuration|None|Description of scan config|
|config_name|string|None|True|The name of the scan configuration|None|Scan Config 1|
|scan_config_id|string|None|True|Scan configuration UUID|None|a709c972-cb1f-4790-bfce-6ab74653900c|

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

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|Status code of the request|

Example output:

```
{
  "status": 200
}
```

#### Delete Scan Config

This action is used to delete an existing scan config.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_config_id|string|None|True|Scan configuration UUID|None|4569288e-2bb4-416e-a4ee-4f7add18afe0|

Example input:

```
{
  "scan_config_id": "4569288e-2bb4-416e-a4ee-4f7add18afe0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|Status code of the request|

Example output:

```
{
  "status": 204
}
```

#### Get Scan Configs

This action is used to get a page of scan configurations, based on supplied pagination parameters.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|index|integer|None|False|The page index to start form. If blank, index will be 0|None|0|
|size|integer|None|False|The number of entries on each page. If blank, size will be 50|None|0|
|sort|string|None|False|How to sort the scan configs. If blank, sort will be alphabetical by scan config name|None|scanconfig.name,DESC|

Example input:

```
{
  "index": 0,
  "size": 0,
  "sort": "scanconfig.name,DESC"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan_configs|[]scan_config|False|A list of scan configurations|

Example output:

```
{
  "scan_configs": [
    {
      "id": "6a33ae79-5ebd-44a9-9a0a-f269876e90c9",
      "config_name": "Test_create_action",
      "config_description": "test create",
      "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda",
      "attack_template_id": "11111111-0000-0000-0000-000000000000",
      "errors": [
        "Seed URL list must not be empty",
        "Crawling Scope Constraint list must not be empty"
      ],
      "links": [
        {
          "rel": "self",
          "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs/6a33ae79-5ebd-44a9-9a0a-f269876e90c9"
        }
      ]
    },
    {
      "id": "0173ce58-369b-4d89-87d6-ef9cb59f8e38",
      "config_name": "Test_create_action",
      "config_description": "test create",
      "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda",
      "attack_template_id": "11111111-0000-0000-0000-000000000000",
      "errors": [
        "Seed URL list must not be empty",
        "Crawling Scope Constraint list must not be empty"
      ],
      "links": [
        {
          "rel": "self",
          "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs/0173ce58-369b-4d89-87d6-ef9cb59f8e38"
        }
      ]
    },
    {
      "id": "a709c972-cb1f-4790-bfce-6ab74653900c",
      "config_name": "update_test",
      "config_description": "testing update",
      "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda",
      "attack_template_id": "11111111-0000-0000-0000-000000000000",
      "errors": [],
      "links": [
        {
          "rel": "self",
          "href": "https://us.api.insight.rapid7.com:443/ias/v1/scan-configs/a709c972-cb1f-4790-bfce-6ab74653900c"
        }
      ]
    }
  ]
}
```

#### Get Scan

This action is used to get a scan.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_id|string|None|True|The scans UUID|None|b0b343aa-7fc2-4a9a-bc18-5ac64df7791a|

Example input:

```
{
  "scan_id": "b0b343aa-7fc2-4a9a-bc18-5ac64df7791a"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan|scan|False|Information on the scan|

Example output:

```
{
  "scan": {
    "id": "b0b343aa-7fc2-4a9a-bc18-5ac64df7791a",
    "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda",
    "scan_config_id": "a709c972-cb1f-4790-bfce-6ab74653900c",
    "submitter": {
      "type": "USER",
      "id": "5b278d63-8fac-4910-978e-8e281039b790"
    },
    "submit_time": "2019-01-08T22:04:46.402",
    "completion_time": "2019-01-08T22:53:38.385",
    "status": "COMPLETE",
    "failure_reason": "",
    "links": [
      {
        "rel": "self",
        "href": "https://us.api.insight.rapid7.com:443/ias/v1/scans/b0b343aa-7fc2-4a9a-bc18-5ac64df7791a"
      }
    ]
  }
}
```

#### Get Scans

This action is used to get a page of scans, based on supplied pagination parameters.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|index|integer|None|False|The page index to start form. If blank, index will be 0|None|0|
|size|integer|None|False|The number of entries on each page. If blank, size will be 50|None|50|
|sort|string|None|False|How to sort the scans. If blank, sort will be alphabetical by scan name|None|scan.submit_time,DESC|

Example input:

```
{
  "index": 0,
  "size": 50,
  "sort": "scan.submit_time,DESC"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scans|[]scan|False|A list of scans|

Example output:

```
{
  "scans": [
    {
      "id": "b0b343aa-7fc2-4a9a-bc18-5ac64df7791a",
      "app_id": "78c85b01-2a23-404d-ac5a-18324d8e3bda",
      "scan_config_id": "a709c972-cb1f-4790-bfce-6ab74653900c",
      "submitter": {
        "type": "USER",
        "id": "5b278d63-8fac-4910-978e-8e281039b790"
      },
      "submit_time": "2019-01-08T22:04:46.402",
      "completion_time": "2019-01-08T22:53:38.385",
      "status": "COMPLETE",
      "failure_reason": "",
      "links": [
        {
          "rel": "self",
          "href": "https://us.api.insight.rapid7.com:443/ias/v1/scans/b0b343aa-7fc2-4a9a-bc18-5ac64df7791a"
        }
      ]
    }
  ]
}
```

#### Delete Scan

This action is used to delete a scan.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_id|string|None|True|The scans UUID|None|b0b343aa-7fc2-4a9a-bc18-5ac64df7791a|

Example input:

```
{
  "scan_id": "b0b343aa-7fc2-4a9a-bc18-5ac64df7791a"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|Status code of the request|

Example output:

```
{
  "status": 204
}
```

#### Submit Scan Action

This action is used to submit a new scan action.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|Pause|True|Action to take|['Pause', 'Resume', 'Stop', 'Cancel', 'Authenticate']|Pause|
|scan_id|string|None|True|Scan UUID|None|008eaffe-90ce-4de9-8601-40414391c21c|

Example input:

```
{
  "action": "Pause",
  "scan_id": "008eaffe-90ce-4de9-8601-40414391c21c"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|integer|False|Status code of the request|

Example output:

```
{
  "status": 200
}
```

#### Get Scan Engine Events

This action is used to get the engine events from a scan.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_id|string|None|True|Scan UUID|None|c762adbe-1636-4c70-9787-5f22c2dc5af8|

Example input:

```
{
  "scan_id": "c762adbe-1636-4c70-9787-5f22c2dc5af8"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|events|[]event_log|False|An array of event logs and their dates|

Example output:

```
{
  "events": [
    {
      "time": "2019-01-09T20:18:39.536",
      "event": "Scan is awaiting scheduling"
    }
  ]
}
```

#### Get Scan Execution Details

This action is used to get real-time details of the execution of a scan.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_id|string|None|True|Scan UUID|None|c762adbe-1636-4c70-9787-5f22c2dc5af8|

Example input:

```
{
  "scan_id": "c762adbe-1636-4c70-9787-5f22c2dc5af8"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|details|scan_details|False|Detailed information about the scan|

Example output:

```
{
  "details": {
    "logged_in": false,
    "links_in_queue": 0,
    "links_crawled": 0,
    "attacks_in_queue": 0,
    "attacked": 0,
    "vulnerable": 0,
    "requests": 0,
    "failed_requests": 0,
    "network_speed": 0,
    "drip_delay": 0
  }
}
```

#### Get Scan Platform Events

This action is used to get the platform events from a scan.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_id|string|None|True|Scan UUID|None|c762adbe-1636-4c70-9787-5f22c2dc5af8|

Example input:

```
{
  "scan_id": "c762adbe-1636-4c70-9787-5f22c2dc5af8"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|events|[]event_log|False|An array of event logs and their dates|

Example output:

```
{
  "events": [
    {
      "time": "2019-01-09T20:18:47.751",
      "event": "Sending scan state action START"
    },
    {
      "time": "2019-01-09T20:18:50.464",
      "event": "Sending scan state action CANCEL"
    }
  ]
}
```

#### Get Vulnerabilities

This action is used to get a page of Vulnerabilities, based on supplied pagination parameters. The default sort for Vulnerabilities is 'severity' (descending); for a full list of sortable properties, refer to the Search Catalog detailed in the Search API.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|index|integer|None|False|The 0-based index of the page of data desired (default: 0)|None|1|
|pageToken|string|None|False|The page token, used as an alternative to index|None|NDM0NTk0NTIyOjo6X1M6OjpiYW5hbmFz|
|size|integer|None|False|The size of the page of data desired (min: 1, max: 1000, default: 50)|None|1|
|sort|string|None|False|The sort terms and (optional) directions for the desired ordering of data|None|vulnerability.severity,DESC|

Example input:

```
{
  "index": 1,
  "size": 1,
  "sort": "vulnerability.severity,DESC",
  "pageToken": "NDM0NTk0NTIyOjo6X1M6OjpiYW5hbmFz"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|data|[]vulnerabilityItem|False|List of vulnerability data|[]|
|links|[]linkDetails|False|List of links|[]|
|metadata|pageMetadata|False|Page metadata|{}|

Example output:

```
{
  "metadata": {
    "size": 1,
    "totalData": 1,
    "pageToken": "NDM0NTk0NTIyOjo6X1M6OjpiYW5hbmFz",
    "index": 1,
    "sort": "scan.submit_time,DESC,scan.status",
    "totalPages": 1
  },
  "data": [
    {
      "app": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      },
      "severity": "SAFE",
      "vectorString": "example",
      "newlyDiscovered": true,
      "insightUiUrl": "sample.com",
      "lastDiscovered": "2021-08-03T14:07:37",
      "firstDiscovered": "2021-08-03T14:07:37",
      "vulnerabilityScore": 1.5,
      "variances": [
        {
          "attackExchanges": [
            {
              "request": "example",
              "response": "example",
              "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
            }
          ],
          "originalValue": "example",
          "attackValue": "example",
          "attack": {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
          },
          "module": {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
          },
          "proofDescription": "example",
          "originalExchange": {
            "request": "example",
            "response": "example",
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
          },
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "proof": "example",
          "message": "example"
        }
      ],
      "links": [
        {
          "profile": "example",
          "rel": "example",
          "name": "example",
          "href": "example.com"
        }
      ],
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "rootCause": {
        "method": "GET",
        "parameter": "example",
        "url": "example.com"
      },
      "status": "UNREVIEWED"
    }
  ],
  "links": [
    {
      "profile": "example",
      "rel": "example",
      "name": "example",
      "href": "example.com"
    }
  ]
}
```

#### Get Vulnerability

This action is used to get a vulnerability.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|vulnerabilityId|string|None|True|Unique identifier for vulnerability|None|497f6eca-6276-4993-bfeb-53cbbbba6f08|

Example input:

```
{
  "vulnerabilityId": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|vulnerability|vulnerabilityItem|False|Vulnerability item|{}|

Example output:

```
{
  "vulnerability": {
    "app": {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
    },
    "severity": "SAFE",
    "vectorString": "example",
    "newlyDiscovered": true,
    "insightUiUrl": "sample.com",
    "lastDiscovered": "2021-08-03T14:07:37",
    "firstDiscovered": "2021-08-03T14:07:37",
    "vulnerabilityScore": 1.5,
    "variances": [
      {
        "attackExchanges": [
          {
            "request": "example",
            "response": "example",
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
          }
        ],
        "originalValue": "example",
        "attackValue": "example",
        "attack": {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
        },
        "module": {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
        },
        "proofDescription": "example",
        "originalExchange": {
          "request": "example",
          "response": "example",
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08"
        },
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "proof": "example",
        "message": "example"
      }
    ],
    "links": [
      {
        "profile": "example",
        "rel": "example",
        "name": "example",
        "href": "example.com"
      }
    ],
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "rootCause": {
      "method": "GET",
      "parameter": "example",
      "url": "example.com"
    },
    "status": "UNREVIEWED"
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Tasks

_This plugin does not contain any tasks._

### Custom Output Types

#### discoveryItem

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Discovered|string|False|The time the vulnerability discovery was discovered|
|Scan|objectId|False|The ID of the module|

#### event_log

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Event|string|False|The log event|
|Time|date|False|The time at which the log event occurred|

#### exchangeObject

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|The ID of the Exchange|
|Request|string|False|The critical section of the request payload|
|Response|string|False|The critical section of the response payload|

#### frequencyInput

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Interval|integer|False|The interval of the frequency|
|Type|string|False|The type of the frequency|

#### link

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Href|string|False|Href|
|Rel|string|False|rel|

#### linkDetails

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Href|string|False|Href|
|Name|string|False|Name|
|Profile|string|False|Profile|
|Rel|string|False|Rel|

#### objectId

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|Unique identifier for object|

#### pageMetadata

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Index|integer|False|Page index|
|Page Token|string|False|Page token|
|Size|integer|False|Page size|
|Sort|string|False|Sort details|
|Total Data|integer|False|Total data|
|Total Pages|integer|False|Total pages|

#### rootCause

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Method|string|False|The HTTP method|
|Parameter|string|False|The parameter from the URL|
|URL|string|False|The URL|

#### scan

|Name|Type|Required|Description|
|----|----|--------|-----------|
|App ID|string|False|App UUID|
|Completion Time|date|False|The time the scan was completed|
|Failure Reason|string|False|The reason the scan may have failed|
|ID|string|False|Scan UUID|
|Links|[]link|False|A list of links|
|Scan Config ID|string|False|Scan configs UUID|
|Status|string|False|The status of the scan|
|Submit Time|date|False|The time the scan was submitted|
|Submitter|submitter|False|The submitter of the scan|

#### scan_config

|Name|Type|Required|Description|
|----|----|--------|-----------|
|App ID|string|False|App UUID|
|Attack Template ID|string|False|Attack template UUID|
|Description|string|False|The description of the scan configuration|
|Name|string|False|The name of the scan configuration|
|Errors|[]string|False|A list of errors that detail any current validation failures|
|UUID|string|False|The UUID of the scan configuration|
|Links|[]link|False|A list of links|

#### scan_details

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Attacked|integer|False|The number of attacks already performed|
|Attacks in Queue|integer|False|The number of links in the attacking queue|
|Drip Delay|number|False|The current delay between HTTP requests|
|Failed Requests|integer|False|The number of failed HTTP requests|
|Links Crawled|integer|False|The number of links already crawled|
|Links in Queue|integer|False|The number of links in the crawling queue|
|Logged-In|boolean|False|A flag which indicates if the scan is using authentication during the scan|
|Network Speed|number|False|A throughput indicator|
|Requests|integer|False|The number of HTTP requests which have been executed|
|Vulnerable|integer|False|The number of potential findings|

#### submitter

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|The submitters UUID|
|Type|string|False|The type of the submitter e.g. USER|

#### variance

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Attack|objectId|False|The ID of the attack|
|Attack Exchanges|[]exchangeObject|False|The HTTP exchange executed as part of the attack|
|Attack Value|string|False|The value of a variable used to attack|
|ID|string|False|The ID of the variance|
|Message|string|False|A message that may highlight the result of the attack|
|Module|objectId|False|The ID of the module|
|Original Exchange|exchangeObject|False|The HTTP exchange executed as part of the attack|
|Original Value|string|False|The value of a variable prior to being attacked|
|Proof|string|False|A proof that may highlight the result of the attack|
|Proof Description|string|False|A description of the proof that may highlight the result of the attack|

#### vulnerabilityItem

|Name|Type|Required|Description|
|----|----|--------|-----------|
|App|objectId|False|The ID of the module|
|First Discovered|string|False|The time the vulnerability was first discovered|
|ID|string|False|The ID of the vulnerability|
|Insight UI URL|string|False|Direct link to the Vulnerability on InsightAppSec UI. Require InsightAppSec login before use|
|Last Discovered|string|False|The time the vulnerability was last discovered|
|Links|[]linkDetails|False|List of links|
|Newly Discovered|boolean|False|Indicates that the vulnerability has been found in the latest scan and has not been discovered before|
|Root Cause|rootCause|False|A descriptor for the location of the vulnerability|
|Severity|string|False|The severity of the vulnerability. Expected values: 'SAFE' 'INFORMATIONAL' 'LOW' 'MEDIUM' 'HIGH'|
|Status|string|False|The status of the vulnerability. Expected values: 'UNREVIEWED' 'FALSE_POSITIVE' 'VERIFIED' 'IGNORED' 'REMEDIATED' 'DUPLICATE'|
|Variances|[]variance|False|Evidence found that indicates the presence of a vulnerability|
|Vector String|string|False|Textual representation of the metric values used to determine the CVSS score|
|Vulnerability Score|float|False|CVSS score which represents the severity of an information security vulnerability|

## Troubleshooting

More information about the frequency and recurrence rule parameters used in the Create Schedule action can be found [here](https://help.rapid7.com/insightappsec/en-us/api/v1/docs.html#tag/Schedules).

# Version History

* 1.1.0 - Add new actions: `Get Vulnerabilities`, `Get Vulnerability`, `Create Schedule`, `Get Vulnerability Discovery`, `Get Vulnerability Discoveries`
* 1.0.4 - Fix typo in title for Submit Scan action | Update keywords
* 1.0.3 - Send plugin name and version in the User-Agent string to vendor
* 1.0.2 - Update to v4 Python plugin runtime | Add example inputs
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

* [InsightAppSec API](https://docs.rapid7.com/insightappsec/api-get-started)

## References

* [InsightAppSec API](https://docs.rapid7.com/insightappsec/api-get-started)
