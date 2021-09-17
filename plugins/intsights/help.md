# Description

[IntSights](https://intsights.com/) is disrupting external threat intelligence with a combination of human and automated collection, intelligent analysis, and strategic threat hunting that turns the clear, deep, and dark webs into an intelligence resource that any company can deploy

# Key Features

Identify key features of plugin.

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

# Supported Product Versions

_There are no supported product versions listed._

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|account_id|credential_secret_key|None|True|Account ID for IntSights|None|9de5069c5afe602b2ea0a04b|
|api_key|credential_secret_key|None|True|API key for IntSights|None|bffce7a2e653eb3e499b69238c6ed672727a642e6f07c19fe19b4d59c7a2d2a61078d1601ded75bac3859fc5c204279402ccf141e1999edf9deb47951f96f4c1|

Example input:

```
{
  "account_id": "9de5069c5afe602b2ea0a04b",
  "api_key": "cc805d5fab1fd71a4ab352a9c533e65fb2d5b885518f4e565e68847223b8e6b85cb48f3afad842726d99239c9e36505c64b0dc9a061d9e507d833277ada336ab"
}
```

## Technical Details

### Actions

#### Takedown Request

This action is used to request a takedown for a given alert in Intsights.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_id|string|None|True|Alert's unique ID|None|None|
|target|string|Domain|True|Target|['Website', 'Domain']|Domain|

Example input:

```
{
  "target": "Domain"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|object|True|Response from IntSights|

Example output:

```
```

#### Get Complete Alert by ID

This action is used to get an alert's complete details for a given alert ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_id|string|None|True|Alert's unique ID|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|assets|[]string|True|List of assets|
|assignees|[]string|True|List of assignees|
|details|object|True|Alert Details|
|found_date|date|True|Alert found date|
|id|string|True|Alert ID|
|is_closed|boolean|True|Is alert closed|
|is_flagged|boolean|True|Is alert flagged|
|leak_name|string|False|Name of the leak DBs in data leakage alerts|
|takedown_status|string|True|Alert remediation status|
|update_date|date|True|Alert update date|

Example output:

```
```

#### Rescan Indicator

This action is used to force an indicator scan in Intsights TIP system.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|indicator_value|string|None|True|IOC value in type file hash|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|True|Status|
|task_id|string|True|Task ID|

Example output:

```
```

#### Get Indicator Scan Status

This action is used to get the scan status of an indicator in Insights TIP system.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|task_id|string|None|True|A string representing the request ID|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|True|Status|
|task_id|string|True|Task ID|

Example output:

```
```

#### Get Alerts

This action is used to search Alerts based on criteria.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_type|string|None|False|Comma separated list of alert types. Allowed values - AttackIndication, DataLeakage, Phishing, BrandSecurity, ExploitableData, vip|None|None|
|assigned|boolean|None|False|Show assigned/unAssigned alerts|None|True|
|found_date_from|number|None|False|Start date to fetch from in Unix Millisecond Timestamp|None|0|
|found_date_to|number|None|False|End date to fetch to in Unix Millisecond Timestamp|None|None|
|has_indicators|boolean|None|False|Show alerts with IOCs results|None|False|
|is_closed|boolean|None|False|Is closed/open alerts|None|False|
|is_flagged|boolean|None|False|Show flagged/unflagged alerts|None|True|
|matched_asset_value|string|None|False|Comma separated list|None|None|
|network_type|string|None|False|Comma separated list of network type. Allowed values - ClearWeb, DarkWeb|None|None|
|remediation_status|string|None|False|Comma separated list of remediation status. Allowed values - InProgress, Pending, CancellationInProgress, Cancelled, CompletedSuccessfully, Failed|None|None|
|severity|string|None|False|Comma separated list of alerts severity. Allowed values - High, Medium, Low|None|None|
|source_date_from|number|None|False|Start date to fetch from in Unix Millisecond Timestamp|None|None|
|source_date_to|number|None|False|End date to fetch to in Unix Millisecond Timestamp|None|None|
|source_type|string|None|False|Comma separated list of alerts source type. Allowed values - ApplicationStores, BlackMarkets, HackingForums, SocialMedia, PasteSites, Others|None|None|

Example input:

```
{
  "assigned": true,
  "found_date_from": 0,
  "has_indicators": false,
  "is_closed": false,
  "is_flagged": true
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alert_ids|[]string|True|List of alert IDs|

Example output:

```
```

#### Enrich Indicator

This action is used to submit an indicator to IntSights for investigation and return the results.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|indicator_value|string|None|True|Value of the indicator|None|https://example.com|

Example input:

```
{
  "indicator_value": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|object|True|Data|
|original_value|string|True|Original value|
|status|string|True|Status|

Example output:

```
```

#### Get Indicator by Value

This action this action will search indicators in Intsights TIP.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|indicator_value|string|None|True|Value of the indicator|None|https://example.com|

Example input:

```
{
  "indicator_value": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|first_seen|string|True|First Seen|
|geo_location|string|True|GEO Location|
|last_seen|string|True|Last Seen|
|last_update|string|True|Last Update|
|related_campaigns|[]string|True|Related Campaigns|
|related_malware|[]string|True|Related Malware|
|related_threat_actors|[]string|True|Related Threat Actors|
|score|integer|True|Score|
|severity|string|True|Severity|
|sources|[]source|True|Sources|
|system_tags|[]string|True|System Tags|
|tags|[]string|True|Tags|
|type|string|True|Type|
|value|string|True|Value|
|whitelist|string|True|Whitelist|

Example output:

```
```

### Triggers

#### New Alert

This trigger is used to run when a new alert that matches the given criteria is created in IntSights.

##### Input

_This trigger does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|[]string|True|Response|

Example output:

```
```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [IntSights](https://intsights.com/)

