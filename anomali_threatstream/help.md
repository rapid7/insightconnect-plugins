# Description

[Anomali ThreatStream](https://www.anomali.com/) is an operational threat intelligence stream, automating collection and integration that enables security teams to analyze and respond to threats.
The Anomali ThreatStream InsightConnect plugin allows you lookup hashes, IP addresses, URLs, observables. It also allows importing observables.
This plugin utilizes the Anomali ThreatStream API, which is located with the cloud instance at `http://<Anomali ThreatStream API host>/optic-doc/ThreatStream_OnlineHelp.htm`.

# Key Features

* Lookup hashes, IP addresses, and URLs
* Import observables
* Get observables

# Requirements

* Anomali Threatstream username
* Anomali ThreatStream instance URL
* Anomali Threatstream API key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|Anomali ThreatStream username|None|
|threatstream_url|string|None|True|URL for the ThreatStream instance. Example\: https\://ts.example.com|None|
|api_key|credential_secret_key|None|True|Anomali ThreatStream API key|None|

## Technical Details

### Actions

#### Lookup IP Address

This action is used to lookup an IP address in Anomali.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ip_address|string|None|False|IP address|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]result|False|Results returned|

Example output:

```
{
  "results": [
    {
      "asn": "26496",
      "classification": "private",
      "confidence": "100",
      "country": "US",
      "date_first": "2018-09-06T23:01:26",
      "date_last": "2018-09-06T23:01:26",
      "detail2": "imported by user 1000000012",
      "id": 1000000181,
      "itype": "mal_url",
      "lat": 33.6119,
      "lon": -111.8906,
      "org": "GoDaddy.com, LLC",
      "resource_uri": "/api/v1/intelligence/1000000181/",
      "severity": "very-high",
      "source": "Test Name 1",
      "source_feed_id": 1000000004,
      "srcip": "107.180.51.15",
      "state": "active",
      "update_id": "2075600",
      "url": "http://aadroid.net/wp-content/plugins/coming-soon/themes/default/images/seedprod-credit.png"
    }
  ]
}
```

#### Lookup URL

This action is used to lookup a URL in Anomali.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|False|URL|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]result|False|Results returned|

Example output:

```
{
  "results": [
    {
      "asn": "26496",
      "classification": "private",
      "confidence": "100",
      "country": "US",
      "date_first": "2018-09-06T23:01:26",
      "date_last": "2018-09-06T23:01:26",
      "detail2": "imported by user 1000000012",
      "id": 1000000178,
      "itype": "mal_url",
      "lat": 33.6119,
      "lon": -111.8906,
      "org": "GoDaddy.com, LLC",
      "resource_uri": "/api/v1/intelligence/1000000178/",
      "severity": "very-high",
      "source": "Test Name 1",
      "source_feed_id": 1000000004,
      "srcip": "107.180.51.15",
      "state": "active",
      "update_id": "2075597",
      "url": "http://aadroid.net/wp-includes/js/jquery/jquery.js"
    }
  ]
}
```

#### Lookup Hash

This action is used to lookup a file hash in Anomali.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hash|string|None|False|Hash|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]result|False|Results returned|

Example output:

```
{
  "results": []
}
```

#### Get Observables

This action is used to get observables.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|value|string|None|False|Value|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]result|False|Results returned|

Example output:

```
{
  "results": [
    {
      "classification": "private",
      "confidence": "17",
      "date_first": "2019-10-16T16:12:48",
      "date_last": "2019-10-21T14:01:39",
      "detail": "Delivery",
      "detail2": "imported by user 121",
      "domain": "window.google",
      "id": 112879000,
      "import_session_id": 205,
      "itype": "apt_domain",
      "maltype": "Delivery",
      "resource_uri": "/api/v1/intelligence/112879000/",
      "severity": "very-high",
      "source": "user@example.com",
      "srcip": "127.0.53.53",
      "state": "active",
      "update_id": "272270002"
    }
  ]
}
```

#### Import Observable

This action is used to import observable(s) into Anomali with approval.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file|file|None|True|File of data to be imported into Anomali|None|
|observable_settings|observable_settings|None|False|Settings needed for importing an observable that needs approval|None|

Observable Settings

  Each mapping can have nothing passed or an iType:
  * When passing unstructured data via `file` its best that mappings be set.
  * A list of iTypes can be located here `https://<Amonali Server>//optic-doc/ThreatStream_OnlineHelp.htm#appendices/app_indicators.htm`

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|import_observable_response|False|Results from importing observable(s)|

Example output:

```
{
  "results": {
    "job_id": "00bc2d03-c608-4824-863d-0a7c9126615a",
    "success": true,
    "import_session_id": "1000000344"
  }
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

If you're unable to import data without approval, the Anomali user configured in InsightConnect will need to have `approver` permissions.

# Version History

* 3.0.1 - Update actions to use SSL Verify from connection settings
* 3.0.0 - Add new action Get Observables | Rename action Add Approval Indicator to Import Observable | Add connection test
* 2.0.0 - Support optional server SSL/TLS certificate validation
* 1.1.0 - New action Add Approval Indicator
* 1.0.0 - Initial plugin

# Links

## References

* [Anomali ThreatStream](https://www.anomali.com/)

