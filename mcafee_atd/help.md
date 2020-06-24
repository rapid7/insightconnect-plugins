# Description

[McAfee Advanced Threat Defense](https://www.mcafee.com/enterprise/en-us/products/advanced-threat-defense.html) provides an API framework for external applications to access core McAfeeATD functions through the REST protocol.

# Key Features

* Check if a hash is blacklisted
* Check the analysis status
* Submit a URL for analysis

# Requirements

* Username and password
* Base URL for McAfee ATD

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password|None|{"username":"user1", "password":"mypassword"}|
|port|integer|443|False|The port number for provided host|None|443|
|url|string|None|True|Base URL for the McAfee Advanced Threat Defense server|None|https://www.example.com|
|verify_ssl|boolean|True|False|Verify the server's TLS/SSL certificate|None|True|

Example input:

```
{
  "credentials": {
    "username":"user1",
    "password":"mypassword"
  },
  "port": 443,
  "url": "https://www.example.com",
  "verify_ssl": true
}
```

## Technical Details

### Actions

#### Submit URL

This action is used to submit a URL for dynamic analysis. It accepts a URL to analyze or a URL that points to a file to analyze.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|submit_type|string|URL submission|False|URL to submit for analysis or file to analyze from a URL|['URL submission', 'File from URL']|None|
|url|string|None|True|URL for analysis|None|https://www.example.com|

Example input:

```
{
  "url": "https://www.example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|submit_url_info|submit_url_info|False|Information about submitted URL|

Example output:

```
{
  "submit_url_info": {
    "estimatedTime": 0,
    "fileId": "",
    "filesWait": 0,
    "mimeType": "application/url",
    "results": [
      {
        "cache": 0,
        "destIp": "",
        "file": "https://example.com",
        "md5": "03C63305A49C1342D4FA9988B635973E",
        "messageId": "",
        "sha1": "",
        "sha256": "",
        "size": "18",
        "srcIp": "",
        "submitType": "1",
        "taskId": 29,
        "url": "https://example.com"
      }
    ],
    "subId": 29,
    "success": true
  }
}
```

#### Check Analysis Status

This action checks the analysis status.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|analysis_id|integer|None|True|Task ID or job ID value which is returned in submission step|None|13|
|type|string|task|False|Type of ID, default value is task|['task', 'job']|None|

Example input:

```
{
  "analysis_id": 13
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|job_results|job|False|Return information about given Job ID|
|results|output|False|Return information about given Task ID|
|success|boolean|False|Success status of analysis ID|

Example output:

```
{
  "results": {
    "PEInfo": "0",
    "asmListing": "0",
    "family": "0",
    "filename": "test.txt",
    "istate": 1,
    "jobid": 13,
    "md5": "0B47F671BC6328623DFA10851D418E55",
    "status": "Completed",
    "submitTime": "2020-06-20 19: 11: 44",
    "summaryFiles": "0",
    "taskid": 13,
    "useLogs": "0",
    "userid": 1,
    "vmDesc": "Only Down Selectors",
    "vmName": "Analyzer Profile 1",
    "vmProfile": "1"
  },
  "success": true
}
```

#### Check Hash Status

This action is used to check if a user submitted hash value is either blacklisted or whitelisted.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|MD5 Hash to submit|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|object|True|Return information about given MD5 Hash|
|success|boolean|True|Success status of submit Hash request|

Example output:

```
{
  "results": {
    "9de5069c5afe602b2ea0a04b66beb2c0": "Previously submitted"
  },
  "success": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.2.0 - New action Submit URL
* 1.1.0 - New action Check Analysis Status
* 1.0.0 - Initial plugin

# Links

## References

* [McAfee Advanced Threat Defense](https://www.mcafee.com/enterprise/en-us/products/advanced-threat-defense.html)
