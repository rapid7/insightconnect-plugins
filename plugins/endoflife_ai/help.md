# Description

[endoflife.ai](https://endoflife.ai) provides end-of-life dates, support status and EOL Risk Scores for 500+ software products. This plugin uses the [endoflife.ai API](https://endoflife.ai/api) to enrich assets, findings and tickets with lifecycle data for triage

# Key Features

* Look up the support status, end-of-life date and EOL Risk Score of one product version
* List every tracked version of a product with its dates and status
* Check a whole list of product and version pairs in one action for stack-wide triage

# Requirements

* No account is required. An optional API key from [endoflife.ai](https://endoflife.ai/api) raises the daily request limit

# Supported Product Versions

* endoflife.ai API v1

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|False|Optional API key from endoflife.ai. Sent as the X-API-Key header and raises the daily request limit|None|8e4f2a1c9b7d3e6f0a5c2b8d1e7f4a9c|None|None|
|url|string|https://api.endoflife.ai|True|Base URL of the endoflife.ai API|None|https://api.endoflife.ai|None|None|

Example input:

```
{
  "api_key": "8e4f2a1c9b7d3e6f0a5c2b8d1e7f4a9c",
  "url": "https://api.endoflife.ai"
}
```

The connection test calls `GET /v1` on the configured URL and confirms it answers like the endoflife.ai API.

Only the product slug and version are sent to api.endoflife.ai. No asset names, hostnames or other data leave InsightConnect.

## Technical Details

### Actions


#### Check Batch

This action is used to check a list of product and version pairs and return one result per pair. Items are sent to `POST /v1/batch` in chunks of five, which every tier of the API accepts, so long lists work with or without an API key. Unknown pairs come back with `found` set to `false` rather than failing the action.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|items|[]batch_item|None|True|Product and version pairs to check|None|[{"product": "nodejs", "version": "20"}, {"product": "postgresql", "version": "13"}]|None|None|
  
Example input:

```
{
  "items": [
    {
      "product": "nodejs",
      "version": "20"
    },
    {
      "product": "postgresql",
      "version": "13"
    }
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|integer|True|Number of results|2|
|eol_count|integer|True|Number of found pairs whose status is eol|2|
|found_count|integer|True|Number of pairs that were found|2|
|results|[]batch_result|True|One result per input pair, in input order|[{"product": "nodejs", "version": "20", "found": true, "status": "eol", "eol_date": "2026-04-30", "days_past_eol": 145, "score": 60, "band": "High", "grade": "C", "cisa_kev_exposure": 0, "extended_support_available": true, "eol_date_source": "vendor-fetched", "eol_date_confidence": "high", "product_url": "https://endoflife.ai/nodejs"}]|
  
Example output:

```
{
  "count": 3,
  "eol_count": 2,
  "found_count": 2,
  "results": [
    {
      "band": "High",
      "cisa_kev_exposure": 0,
      "days_past_eol": 145,
      "eol_date": "2026-04-30",
      "eol_date_confidence": "high",
      "eol_date_source": "vendor-fetched",
      "extended_support_available": true,
      "found": true,
      "grade": "C",
      "product": "nodejs",
      "product_url": "https://endoflife.ai/nodejs",
      "score": 60,
      "status": "eol",
      "version": "20"
    },
    {
      "band": "High",
      "cisa_kev_exposure": 0,
      "days_past_eol": 313,
      "eol_date": "2025-11-13",
      "eol_date_confidence": "high",
      "eol_date_source": "vendor-fetched",
      "extended_support_available": true,
      "found": true,
      "grade": "C",
      "product": "postgresql",
      "product_url": "https://endoflife.ai/postgresql",
      "score": 60,
      "status": "eol",
      "version": "13"
    },
    {
      "found": false,
      "message": "Version not found",
      "product": "nodejs",
      "version": "99"
    }
  ]
}
```

#### Get Product

This action is used to list every tracked version of a product with its dates, status and EOL Risk Score

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|product|string|None|True|Product slug as used on endoflife.ai, for example nodejs, windows-server or postgresql|None|nodejs|None|None|
  
Example input:

```
{
  "product": "nodejs"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|found|boolean|True|Whether the product is tracked by endoflife.ai|True|
|message|string|False|The API's explanation when the product was not found|Product "not-a-product" not found|
|product|string|False|Product slug|nodejs|
|product_url|string|False|Link to the product page on endoflife.ai|https://endoflife.ai/nodejs|
|version_count|integer|False|Number of tracked versions|20|
|versions|[]version|False|Tracked versions with their dates, status and score|[{"version": "20", "status": "eol", "eol_date": "2026-04-30", "release_date": "2023-04-18", "latest_release": "20.20.2", "days_past_eol": 145, "score": 60, "band": "High", "grade": "C", "cisa_kev_exposure": 0, "extended_support_available": true, "eol_date_source": "vendor-fetched", "eol_date_confidence": "high", "score_card_url": "https://endoflife.ai/score/nodejs/20"}]|
  
Example output:

```
{
  "found": true,
  "product": "nodejs",
  "product_url": "https://endoflife.ai/nodejs",
  "version_count": 1,
  "versions": [
    {
      "band": "High",
      "cisa_kev_exposure": 0,
      "days_past_eol": 145,
      "eol_date": "2026-04-30",
      "eol_date_confidence": "high",
      "eol_date_source": "vendor-fetched",
      "extended_support_available": true,
      "grade": "C",
      "latest_release": "20.20.2",
      "release_date": "2023-04-18",
      "score": 60,
      "score_card_url": "https://endoflife.ai/score/nodejs/20",
      "status": "eol",
      "version": "20"
    }
  ]
}
```

#### Get Version Status

This action is used to get the support status, end-of-life date and EOL Risk Score of one product version. When the product or version is not tracked the action succeeds with `found` set to `false` and the API's explanation in `message`, so a workflow can branch on it.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|product|string|None|True|Product slug as used on endoflife.ai, for example nodejs, windows-server or postgresql|None|nodejs|None|None|
|version|string|None|True|Release cycle of the product, for example 20 for Node.js 20.x or 2019 for Windows Server 2019|None|20|None|None|
  
Example input:

```
{
  "product": "nodejs",
  "version": "20"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|band|string|False|Risk band of the score, one of Low, Moderate, High or Critical|High|
|cisa_kev_exposure|integer|False|Score factor for the product's presence in the CISA Known Exploited Vulnerabilities catalog|0|
|days_past_eol|integer|False|Days since the end-of-life date, empty until it has passed|145|
|days_until_eol|integer|False|Days until the end-of-life date, empty once it has passed|120|
|eol_date|string|False|End-of-life date in YYYY-MM-DD format, empty when no date is published|2026-04-30|
|eol_date_confidence|string|False|Confidence in the end-of-life date, one of high, medium or low|high|
|eol_date_source|string|False|Provenance of the end-of-life date, for example vendor-fetched, vendor-verified or upstream|vendor-fetched|
|extended_support_available|boolean|False|Whether a commercial extended-support option is known for this product|True|
|found|boolean|True|Whether the product and version are tracked by endoflife.ai|True|
|grade|string|False|Letter grade of the score from A to F|C|
|message|string|False|The API's explanation when the product or version was not found|Version "99" not found for "nodejs"|
|product|string|False|Product slug|nodejs|
|product_url|string|False|Link to the product page on endoflife.ai|https://endoflife.ai/nodejs|
|score|integer|False|EOL Risk Score from 0 (lowest risk) to 100 (highest risk)|60|
|status|string|False|Support status, one of active, warn (end of life within 90 days) or eol|eol|
|version|string|False|Release cycle matched by the API|20|
  
Example output:

```
{
  "band": "High",
  "cisa_kev_exposure": 0,
  "days_past_eol": 145,
  "eol_date": "2026-04-30",
  "eol_date_confidence": "high",
  "eol_date_source": "vendor-fetched",
  "extended_support_available": true,
  "found": true,
  "grade": "C",
  "product": "nodejs",
  "product_url": "https://endoflife.ai/nodejs",
  "score": 60,
  "status": "eol",
  "version": "20"
}
```

Example output when the version is not tracked:

```
{
  "found": false,
  "message": "Version \"99\" not found for \"nodejs\""
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**batch_item**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Product|string|None|True|Product slug, for example nodejs|None|
|Version|string|None|False|Release cycle, for example 20. When omitted the highest-risk version of the product is returned|None|
  
**batch_result**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Band|string|None|False|Risk band of the score|None|
|CISA KEV Exposure|integer|None|False|Score factor for the product's presence in the CISA KEV catalog|None|
|Days Past EOL|integer|None|False|Days since the end-of-life date|None|
|Days Until EOL|integer|None|False|Days until the end-of-life date|None|
|EOL Date|string|None|False|End-of-life date in YYYY-MM-DD format|None|
|EOL Date Confidence|string|None|False|Confidence in the end-of-life date|None|
|EOL Date Source|string|None|False|Provenance of the end-of-life date|None|
|Extended Support Available|boolean|None|False|Whether a commercial extended-support option is known|None|
|Found|boolean|None|True|Whether the product and version were found|None|
|Grade|string|None|False|Letter grade of the score|None|
|Message|string|None|False|The API's explanation when the product or version was not found|None|
|Product|string|None|True|Product slug as submitted|None|
|Product URL|string|None|False|Link to the product page on endoflife.ai|None|
|Score|integer|None|False|EOL Risk Score from 0 to 100|None|
|Status|string|None|False|Support status, one of active, warn or eol|None|
|Version|string|None|False|Version as submitted|None|
  
**version**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Band|string|None|True|Risk band of the score, one of Low, Moderate, High or Critical|None|
|CISA KEV Exposure|integer|None|False|Score factor for the product's presence in the CISA Known Exploited Vulnerabilities catalog|None|
|Days Past EOL|integer|None|False|Days since the end-of-life date, empty until it has passed|None|
|Days Until EOL|integer|None|False|Days until the end-of-life date, empty once it has passed|None|
|EOL Date|string|None|False|End-of-life date in YYYY-MM-DD format, empty when no date is published|None|
|EOL Date Confidence|string|None|False|Confidence in the end-of-life date, one of high, medium or low|None|
|EOL Date Source|string|None|False|Provenance of the end-of-life date, for example vendor-fetched, vendor-verified or upstream|None|
|Extended Support Available|boolean|None|False|Whether a commercial extended-support option is known for this product|None|
|Extended Support Date|string|None|False|End of the vendor's own extended or paid support phase where one is published|None|
|Grade|string|None|True|Letter grade of the score from A to F|None|
|Latest Release|string|None|False|Latest patch release of the cycle known to endoflife.ai|None|
|Release Date|string|None|False|Release date of the cycle in YYYY-MM-DD format|None|
|Score|integer|None|True|EOL Risk Score from 0 (lowest risk) to 100 (highest risk)|None|
|Score Card URL|string|None|False|Link to the score card for this version on endoflife.ai|None|
|Status|string|None|True|Support status, one of active, warn (end of life within 90 days) or eol|None|
|Version|string|None|True|Release cycle of the product, for example 20 or 2019|None|


## Troubleshooting

* Anonymous requests share a daily limit per source IP address. A `429` response means the limit was hit; set an API key in the connection to raise it
* A `found` output of `false` means the product or version is not tracked by endoflife.ai. Product slugs are lowercase, for example `nodejs`, `windows-server`, `postgresql`. The `message` output carries the API's own explanation and, for unknown products, suggested slugs
* Versions are matched by release cycle, for example `20` for Node.js 20.x, `2019` for Windows Server 2019, `8.0` for .NET 8
* Only the product slug and version are sent to api.endoflife.ai. No asset names, hostnames or other data leave InsightConnect

# Version History

* 1.0.0 - Initial plugin

# Links

* [endoflife.ai](https://endoflife.ai)

## References

* [endoflife.ai API documentation](https://endoflife.ai/api)
* [EOL Risk Score methodology](https://endoflife.ai/risk-score)
* [OpenAPI specification](https://api.endoflife.ai/openapi.json)
