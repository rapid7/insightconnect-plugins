# Description

[Anomali ThreatStream](https://www.anomali.com/) is an operational threat intelligence stream, automating collection and integration that enables security teams to analyze and respond to threats.
The Anomali ThreatStream InsightConnect plugin allows you lookup hashes, IP addresses, URLs, observables. It also allows importing observables.
This plugin utilizes the Anomali ThreatStream API, which is located with the cloud instance at `http://<Anomali ThreatStream API host>/optic-doc/ThreatStream_OnlineHelp.htm`.

# Key Features

* Lookup hashes, IP addresses, and URLs
* Import observables
* Get observables

# Requirements

* Anomali ThreatStream username
* Anomali ThreatStream instance URL
* Anomali ThreatStream API key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|Anomali ThreatStream API key|None|
|ssl_verify|boolean|True|True|Verify the server's SSL/TLS certificate|None|
|url|string|None|True|URL for the ThreatStream instance e.g. https://ts.example.com|None|
|username|string|None|True|Anomali ThreatStream username|None|

## Technical Details

### Actions

#### Submit URL

This action is used to submit a URL to ThreatStream sandbox.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|classification|string|private|False|Classification of the sandbox submission, either public or private|['private', 'public']|
|detail|string|None|False|A comma-separated list that provides additional details for the indicator. This information is displayed in the tag column of the ThreatStream UI. For example, "Credential-Exposure,compromised_email"|None|
|platform|string|None|True|Platform on which the submitted URL or file will be run|['ALL', 'ANDROID4.4', 'ANDROID5.1', 'ANDROID6.0', 'MACOSX', 'WINDOWSXP', 'WINDOWSXPNATIVE', 'WINDOWS7', 'WINDOWS7NATIVE', 'WINDOWS7OFFICE2010', 'WINDOWS7OFFICE2013', 'WINDOWS10', 'WINDOWS10x64']|
|url|string|None|True|URL to detonate|None|
|use_premium_sandbox|boolean|None|True|Specify whether the premium sandbox should be used for detonation|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|reports|[]report|False|Reports containing submission details|
|success|boolean|False|Operation status|

Example Output:

```
```

#### Submit File

This action is used to submit a file to ThreatStream sandbox.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|classification|string|private|False|Classification of the Sandbox submission, either public or private|['private', 'public']|
|detail|string|None|False|A comma-separated list that provides additional details for the indicator. This information is displayed in the Tag column of the ThreatStream UI. For example, "Credential-Exposure,compromised_email"|None|
|file|file|None|True|File to detonate|None|
|platform|string|None|True|Platform on which the submitted URL or file will be run|['ALL', 'ANDROID4.4', 'ANDROID5.1', 'ANDROID6.0', 'MACOSX', 'WINDOWSXP', 'WINDOWSXPNATIVE', 'WINDOWS7', 'WINDOWS7NATIVE', 'WINDOWS7OFFICE2010', 'WINDOWS7OFFICE2013', 'WINDOWS10', 'WINDOWS10x64']|
|use_premium_sandbox|boolean|None|True|Specify whether the premium sandbox should be used for detonation|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|reports|[]report|False|Reports containing submission details|
|success|boolean|False|Operation status|

Example Output:

```
```

#### Lookup URL

This action is used to lookup a URL in Anomali ThreatStream.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|False|URL|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]result|False|Results returned|

Example Output:

```
```

#### Lookup IP Address

This action is used to lookup an IP address in Anomali ThreatStream.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ip_address|string|None|False|IP address|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]result|False|Results returned|

Example Output:

```
```

#### Lookup Hash

This action is used to lookup a file hash in Anomali ThreatStream.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hash|string|None|False|Hash|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]result|False|Results returned|

Example Output:

```
```

#### Import Observable

This action is used to import observable(s) into Anomali ThreatStream with approval.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file|file|None|True|File of data to be imported into Anomali ThreatStream|None|
|observable_settings|observable_settings|None|False|Settings needed for importing an observable that needs approval|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|import_observable_response|False|Results from importing observable(s)|

Example Output:

```
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

Example Output:

```
```

#### Submit URL

This action is used to submit a URL to ThreatStream sandbox.

##### Submit File

This action is used to submit a file to ThreatStream sandbox.

##### Lookup IP Address

This action is used to lookup an IP address in Anomali.

##### Lookup URL

This action is used to lookup a URL in Anomali.

##### Get Observables

This action is used to get observables.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|False|URL|None|

##### Import Observable

This action is used to import observable(s) into Anomali with approval.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file|file|None|True|File of data to be imported into Anomali ThreatStream|None|
|observable_settings|observable_settings|None|False|Settings needed for importing an observable that needs approval|None|

Observable Settings

  Each mapping can have nothing passed or an iType:
  * When passing unstructured data via `file` its best that mappings be set.
  * A list of iTypes can be located here `https://<Amonali Server>//optic-doc/ThreatStream_OnlineHelp.htm#appendices/app_indicators.htm`

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|classification|string|private|False|Classification of the Sandbox submission—public or private|['private', 'public']|
|detail|string|None|False|A comma-separated list that provides additional details for the indicator. This information is displayed in the Tag column of the ThreatStream UI. For example, "Credential-Exposure,compromised_email"|None|
|file|file|None|True|File to detonate|None|
|platform|string|None|True|Platform on which the submitted URL or file will be run|['ALL', 'ANDROID4.4', 'ANDROID5.1', 'ANDROID6.0', 'MACOSX', 'WINDOWSXP', 'WINDOWSXPNATIVE', 'WINDOWS7', 'WINDOWS7NATIVE', 'WINDOWS7OFFICE2010', 'WINDOWS7OFFICE2013', 'WINDOWS10', 'WINDOWS10x64']|
|use_premium_sandbox|boolean|None|True|Specify whether the premium sandbox should be used for detonation|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|reports|[]report|False|Reports containing submission details|
|success|boolean|False|Operation status|

Example output:

```
{
  "success": true,
  "reports": [
    {
      "status": "/api/v1/submit/101/",
      "detail": "/api/v1/submit/101/report/",
      "id": 101,
      "platform": "WINDOWS7"
    },
    {
      "status": "/api/v1/submit/100/",
       "detail": "/api/v1/submit/100/report/",
      "id": 100,
      "platform": "WINDOWSXP"
    }
  ]
}
```

##### Submit URL

This action is used to submit a URL to ThreatStream sandbox.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|classification|string|private|False|Classification of the Sandbox submission—public or private|['private', 'public']|
|detail|string|None|False|A comma-separated list that provides additional details for the indicator. This information is displayed in the Tag column of the ThreatStream UI. For example, "Credential-Exposure,compromised_email"|None|
|platform|string|None|True|Platform on which the submitted URL or file will be run|['ALL', 'ANDROID4.4', 'ANDROID5.1', 'ANDROID6.0', 'MACOSX', 'WINDOWSXP', 'WINDOWSXPNATIVE', 'WINDOWS7', 'WINDOWS7NATIVE', 'WINDOWS7OFFICE2010', 'WINDOWS7OFFICE2013', 'WINDOWS10', 'WINDOWS10x64']|
|url|string|None|True|URL to detonate|None|
|use_premium_sandbox|boolean|None|True|Specify whether the premium sandbox should be used for detonation|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|reports|[]report|False|Reports containing submission details|
|success|boolean|False|Operation status|

Example output:

```
{
  "success": true,
  "reports": [
    {
      "status": "/api/v1/submit/101/",
      "detail": "/api/v1/submit/101/report/",
      "id": 101,
      "platform": "WINDOWS7"
    },
    {
      "status": "/api/v1/submit/100/",
       "detail": "/api/v1/submit/100/report/",
      "id": 100,
      "platform": "WINDOWSXP"
    }
  ]
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

If you're unable to import data without approval, the Anomali user configured in InsightConnect will need to have `approver` permissions.

# Version History

* 3.1.0 - Add new actions Submit File and Submit URL
* 3.0.2 - New spec and help.md format for the Hub
* 3.0.1 - Update actions to use SSL Verify from connection settings
* 3.0.0 - Add new action Get Observables | Rename action Add Approval Indicator to Import Observable | Add connection test
* 2.0.0 - Support optional server SSL/TLS certificate validation
* 1.1.0 - New action Add Approval Indicator
* 1.0.0 - Initial plugin

# Links

## References

* [Anomali ThreatStream](https://www.anomali.com/)

