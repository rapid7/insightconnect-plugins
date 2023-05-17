# Description

[Check Point SandBlast](https://www.checkpoint.com/solutions/zero-day-protection/) is a multilayered security technology provides protection against advanced cyber attacks. The Checkpoint Sand Blast plugin extends the Sand Blast service and enables report status and suspicious file upload.

# Key Features

* Suspicious file analysis

# Requirements

* Requires an API Key from the product

# Supported Product Versions

* CheckPoint 2023-05-15

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|API Key|None|TE_API_KEY_grH54uBqMleMweizSuQdifIdfhoqPe2mGCPeOx3E|
|service_address|string|https://example.com|True|The Service Address|None|https://example.com|
|using_cloud_server|boolean|True|True|Set to true if using the cloud version|None|True|

Example input:

```
{
  "api_key": "TE_API_KEY_grH54uBqMleMweizSuQdifIdfhoqPe2mGCPeOx3E",
  "service_address": "te.checkpoint.com",
  "using_cloud_server": true
}
```

## Technical Details

### Actions

#### Query Report

This action is used to query the status of a file.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|features|string|None|False|Features|None|te|
|file_digest|string|None|True|Hash of the file|None|9de5069c5afe602b2ea0a04b66beb2c0|
|file_digest_type|string|None|True|The type of hash used for the digest|['md5', 'sha1', 'sha2']|md5|
|file_name|string|None|False|File name|None|https://example.com|
|file_type|string|None|False|The file extension|None|png|
|quota|boolean|None|False|Quota|None|False|

Example input:

```
{
  "features": "te",
  "file_digest": "0800fc577294c34e0b28ad2839435945",
  "file_digest_type": "md5",
  "file_name": "hash.png",
  "file_type": "png",
  "quota": false
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|found|boolean|False|Returns true if file found|True|
|query_response|object|False|Status of requested features|{}|

Example output:

```
{
  "query_response": {
    "status": {
      "code": 1001,
      "label": "FOUND",
      "message": "The request has been fully answered."
    },
    "md5": "c2efcd148a4739a2f5676a513aa905f6",
    "file_type": "png",
    "file_name": "",
    "features": [
      "te"
    ],
    "te": {
      "trust": 0,
      "images": [
        {
          "report": {
            "verdict": "benign"
          },
          "status": "found",
          "id": "e50e99f3-5963-4573-af9e-e3f4750b55e2",
          "revision": 1
        },
        {
          "report": {
            "verdict": "benign"
          },
          "status": "found",
          "id": "5e5de275-a103-4f67-b55b-47532918fa59",
          "revision": 1
        }
      ],
      "score": -2147483648,
      "combined_verdict": "benign",
      "status": {
        "code": 1001,
        "label": "FOUND",
        "message": "The request has been fully answered."
      }
    }
  },
  "found": true
}
```

#### Upload

This action is used to upload a file for analysis.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|file_bytes|bytes|None|True|The file bytes|None|txt|
|file_name|string|None|True|The name of the file|None|YmxhaA==|
|file_type|string|None|False|File extension e.g. DOCX, PDF|None|https://example.com|

Example input:

```
{
  "file_bytes": "txt",
  "file_name": "YmxhaA==",
  "file_type": "blah.txt"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|results|upload_response|False|Results from the upload|{}|

Example output:

```
{
  "upload_response": {
    "status": {
      "code": 1001,
      "label": "FOUND",
      "message": "The request has been fully answered."
    },
    "sha1": "2668914d800de7a488d3221e370f468eeb561cc5",
    "md5": "c2efcd148a4739a2f5676a513aa905f6",
    "file_type": "png",
    "file_name": "icon.png",
    "features": [
      "te"
    ],
    "te": {
      "trust": 0,
      "images": [
        {
          "report": {
            "verdict": "benign"
          },
          "status": "found",
          "id": "e50e99f3-5963-4573-af9e-e3f4750b55e2",
          "revision": 1
        },
        {
          "report": {
            "verdict": "benign"
          },
          "status": "found",
          "id": "5e5de275-a103-4f67-b55b-47532918fa59",
          "revision": 1
        }
      ],
      "score": -2147483648,
      "combined_verdict": "benign",
      "status": {
        "code": 1001,
        "label": "FOUND",
        "message": "The request has been fully answered."
      }
    }
  }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

When using the local version of Check Point SandBlast the query report action must take a SHA1 hash

# Version History

* 1.0.3 - Update requests to version 2.20.0
* 1.0.2 - Update Check Point branding
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Initial plugin

# Links

* [Check Point website](https://www.checkpoint.com/)

## References

* [Check Point website](https://www.checkpoint.com/)
