# Description

[Datadog](https://www.datadoghq.com/) is a monitoring service for cloud-scale applications, providing monitoring of
servers, databases, tools, and services, through a SaaS-based data analytics platform. Users can post events and
metrics using the Datadog plugin for Rapid7 InsightConnect.

# Key Features

* Post events
* Post metrics

# Requirements

* API key
* App key
* Datadog URL

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|The API key for Datadog|None|
|app_key|string|None|True|Application key|None|
|url|string|None|True|The Datadog URL. Normally https://api.datadoghq.com/api/v1/|None|

## Technical Details

### Actions

#### Post Event

This action is used to post an event.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|event_title|string|None|True|The event title. Limited to 100 characters|None|
|text|string|None|True|The body of the event. Limited to 4000 characters|None|
|date_happened|integer|None|False|POSIX timestamp of the event. Limited to events no older than 1 year, 24 days. If no date is supplied date will be now|None|
|priority|string|None|True|The priority of the event|['normal', 'low']|
|host|string|None|False|Host name to associate with the event. Any tags associated with the host are also applied to this event. if not supplied will be None|None|
|tags|string|None|False|A comma separated list of tags to apply to the event|None|
|alert_type|string|None|True|Event alert type|['error', 'warning', 'info', 'success']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|event|event|False|Event|

Example output:

```
{
  "event": {
    "id": 4785325617371421000,
    "title": "Komand_test",
    "text": "Testing komand",
    "date_happened": 1549490499,
    "handle": "",
    "priority": "normal",
    "related_event_id": [],
    "tags": [
      "environment:test"
    ],
    "url": "https://app.datadoghq.com/event/event?id=4785325617371420593"
  }
}
```

#### Post Metrics

This action is used to post time-series data that can be graphed on Datadog's dashboards. The limit for compressed payloads is 3.2 megabytes (3200000), and 62 megabytes (62914560) for decompressed payloads.
It expects the body of the [timeseries data structure](https://docs.datadoghq.com/api/?lang=bash#post-timeseries-points).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|series|[]object|None|True|Pass a JSON array of the following timeseries format body https://docs.datadoghq.com/api/?lang=bash#post-timeseries-points|None|

Example input:

```
[
  {
    "metric" : "test.metric",
    "points": [
      [ 1554428765, 20 ]
    ],
    "type": "rate",
    "interval": 20,
    "host": "test.example.com",
    "tags": [
      "environment:test"
    ]
  }
]
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|resource|resource|False|None|
|status|integer|False|Status code|

Example output:

```
{
  "resource": {
    "status": "ok"
  },
  "status": 202
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.1.1 - New spec and help.md format for the Hub
* 1.1.0 - New action Post Metrics | Update to use the `komand/python-3-37-slim-plugin` Docker image to reduce plugin size | Run plugin as least privileged user
* 1.0.0 - Initial plugin

# Links

## References

* [Datadog API](https://docs.datadoghq.com/api/?lang=python#overview)

