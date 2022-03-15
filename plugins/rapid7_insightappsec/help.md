# Description

[InsightAppSec’s](https://www.rapid7.com/products/insightappsec/) DAST capabilities and InsightConnect’s automation prowess can help you simplify your SDLC Process with this scan management plugin. The need for automation becomes paramount in the fast moving landscape of modern web scanning and automating you web app scanning with this plugin can save you loads of time to allow you to focus on remediating issues to get your app into product faster!

This plugin utilizes the [Rapid7 InsightAppSec API](https://insightappsec.help.rapid7.com/docs/get-started-with-the-insightappsec-api).

# Key Features

* Create and configure scans
* Run scans and return results

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

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.0 - Update plugin spec with changing title for action Submit scan | Update keywords
* 1.0.3 - Send plugin name and version in the User-Agent string to vendor
* 1.0.2 - Update to v4 Python plugin runtime | Add example inputs
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

## References

* [InsightAppSec API](https://insightappsec.help.rapid7.com/docs/get-started-with-the-insightappsec-api)

