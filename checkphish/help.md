# Description

CheckPhish is a free scanner to detect phishing & fraudulent sites in real-time

# Key Features

* Perform a scan and retrive scan results for potentially malicious URLs

# Requirements

* Requires an API Key from the product, instructions on how to obtain the API key can be found [here](https://checkphish.ai/docs/checkphish-api/#requestApiKey)
  
# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|CheckPhish API Key|None|1A2B3CC4D5E67F8901G2HI345J6K7L89|

Example input:

```
{
  "api_key": "1A2B3CC4D5E67F8901G2HI345J6K7L89"
}
```

## Technical Details

### Actions

#### Scan URL

This action is used to scan a URL and retrieve scan results.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|url|string|None|True|URL you wish to scan and get results for|None|https://example.com|

Example input:

```
{
  "url": "https://example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan_results|scan_url|True|Scan results|

Example output:

```
{
  "job_id": "bce8a057-441b-4634-8e21-349e8167e0fb",
  "status": "DONE",
  "url": "http://example.com/",
  "url_sha256": "a395e2130500750d34703f66c62c50ce99be0c7272b6763f6508c6bd473f1d74",
  "disposition": "clean",
  "brand": "unknown",
  "insights": "https://checkphish.ai/insights/url/1620588003962/a395e2130500750d34703f66c62c50ce99be0c7272b6763f6508c6bd473f1d74",
  "resolved": false,
  "screenshot_path": "https://www.example.com/20210509/a395e2130500750d34703f66c62c50ce99be0c7272b6763f6508c6bd473f1d74.png",
  "error": false
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### scan_url

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Brand|string|False|Brand|
|Disposition|string|False|Disposition|
|Error|boolean|False|Error|
|Insights|string|False|Insights URL|
|Job ID|string|False|Job ID|
|Resolved|boolean|False|Resolved|
|Screenshot Path|string|False|Screenshot Path|
|Status|string|False|Status|
|URL|string|False|URL|
|URL SHA256|string|False|URL SHA256|


## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [CheckPhish](https://checkphish.ai/)
