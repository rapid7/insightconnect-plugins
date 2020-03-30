# Description

[Check Point SandBlast](https://www.checkpoint.com/solutions/zero-day-protection/) is a multilayered security technology provides protection against advanced cyber attacks. The Checkpoint Sand Blast plugin extends the Sand Blast service and enables report status and suspicious file upload.

# Key Features

* Suspicious file analysis

# Requirements

* Requires an API Key from the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|API Key|None|
|service_address|string|te.checkpoint.com|True|The Service Address|None|
|using_cloud_server|boolean|True|True|Set to true if using the cloud version|None|

## Technical Details

### Actions

#### Query Report

This action is used to query the status of a file.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|features|string|None|False|Features|None|
|file_digest|string|None|True|Hash of the file|None|
|file_digest_type|string|None|True|The type of hash used for the digest|['md5', 'sha1', 'sha2']|
|file_name|string|None|False|File name|None|
|file_type|string|None|False|The file extension|None|
|quota|boolean|None|False|Quota|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|found|boolean|False|Returns true if file found|
|query_response|object|False|Status of requested features|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_bytes|bytes|None|True|The file bytes|None|
|file_name|string|None|True|The name of the file|None|
|file_type|string|None|False|File extension e.g. DOCX, PDF|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|upload_response|False|Results from the upload|

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

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Initial plugin

# Links

## References

* [Check Point website](https://www.checkpoint.com/)
