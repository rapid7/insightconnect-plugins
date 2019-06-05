# Anomali ThreatStream

## About

[Anomali ThreatStream](https://www.anomali.com/) is an operationalized threat intelligence stream, automating collection and integration that enables security teams to analyze and respond to threats.
This plugin utilizes the Anomali ThreatStream API, which is located with the cloud instance at `http://<Anomali ThreatStream API host>/optic-doc/ThreatStream_OnlineHelp.htm`.

## Actions

### Lookup IP Address

This action is used to lookup an IP address in Anomali.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ip_address|string|None|False|IP address|None|

#### Output

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

### Lookup URL

This action is used to lookup a URL in Anomali.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|False|URL|None|

#### Output

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

### Lookup Hash

This action is used to lookup a file hash in Anomali.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hash|string|None|False|Hash|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]result|False|Results returned|

Example output:

```
{
  "results": []
}
```

### Add Approval Indicator

This action is used to import indicator(s) into Anomali with approval.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file|file|None|False|File of data to be imported into Anomali|None|
|indicator_settings|indicator_settings|None|False|Settings needed for importing an indicator that needs approval|None|

Indicator Settings

  Each mapping can have nothing passed or an iType:
  * When passing unstructured data via `file` its best that mappings be set.
  * A list of iTypes can be located here `https://<Amonali Server>//optic-doc/ThreatStream_OnlineHelp.htm#appendices/app_indicators.htm`

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|import_indicator_response|False|Results from adding indicator(s)|

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

## Triggers

This plugin does not contain any triggers.

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|Anomali ThreatStream username|None|
|threatstream_url|string|None|True|URL for the ThreatStream instance. Example\: https\://ts.example.com|None|
|api_key|credential_secret_key|None|True|Anomali ThreatStream API key|None|

## Troubleshooting

If you're unable to import data without approval, the Anomali user configured in InsightConnect will need to have `approver` permissions.

## Versions

* 1.0.0 - Initial plugin
* 1.1.0 - New action Add Approval Indicator
* 2.0.0 - Support optional server SSL/TLS certificate validation

## Workflows

Examples:

* Hash an email attachment, then pass the hash of the attachment to Anomali for IOC enrichment.

## References

* [Anomali ThreatStream](https://www.anomali.com/)
