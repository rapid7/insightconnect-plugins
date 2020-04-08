# Description

Uses the Google BigQuery plugin to run queries on Google Cloud Platform.

# Key Features

* Run a query and return the result
* BigQuery BI Engine
* BigQuery GIS

# Requirements

* Requires service account key credentials

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|auth_provider_x509_cert_url|string|https://www.googleapis.com/oauth2/v1/certs|False|OAUTH2 Auth Provider x509 Cert URL|None|https://www.googleapis.com/oauth2/v1/certs|
|auth_uri|string|https://accounts.google.com/o/oauth2/auth|True|OAUTH2 Auth URI|None|https://accounts.google.com/o/oauth2/auth|
|client_email|string|None|True|Client email from service credentials|None|user@example.com|
|client_id|string|None|True|Client ID|None|111111111111111111111|
|client_x509_cert_url|string|None|True|Client certificate URL from service credentials|None|https://www.googleapis.com/robot/v1/metadata/x509/user%40example.com|
|private_key|credential_asymmetric_key|None|True|Private Key from service credentials|None|{"privateKey": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBEFENByuihkiY9w0BAQAZAAAAAAbb3AbHDbS09uUlXOLPH\n+AAAAAAA1bbAAAAAbAbb11=\n-----END PRIVATE KEY-----\n}|
|private_key_id|string|None|True|Private Key ID from service credentials|None|18181818e18181c181d1e18cee1b8e18c1818d1a|
|project_id|string|None|True|Project ID from service credentials|None|spherical-voice-171717|
|token_uri|string|https://oauth2.googleapis.com/token|False|OAUTH2 Token URI|None|https://oauth2.googleapis.com/token|

## Technical Details

### Actions

#### Query

This action is used to get all results from a query.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|Domain to retrieve users from|None|SELECT * FROM (SELECT "apple" AS fruit, "carrot" AS vegetable)|

Example input:

```
{
  "query": "SELECT * FROM (SELECT \"apple\" AS fruit, \"carrot\" AS vegetable)"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|[]object|True|Query result|

Example output:

```
{
  "result": [
    {"fruit": "apple", "vegetable": "carrot"}
  ]
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._
## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Google BigQuery](https://cloud.google.com/bigquery)
