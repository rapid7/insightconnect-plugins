# Description

[Google Web Risk](https://cloud.google.com/web-risk/) checks URLs against the Google Web Risk service. Use the InsightConnect plugin to automatically evaluate suspicious URLs and take action when you find them.

# Key Features

* Lookup URL in web risk service

# Requirements

* WebRisk API token

# Supported Product Versions

_There are no supported product versions listed._

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_secret_key|None|True|API token|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "credentials": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

## Technical Details

### Actions

#### Lookup URL

This action is used to lookup a URL in Web Risk Service.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|threat_type_malware|boolean|True|False|Check if URL is of 'malware' threat|None|True|
|threat_type_social|boolean|True|False|Check if URL is of 'social engineering/phishing' threat|None|True|
|threat_type_unwanted|boolean|True|False|Check if URL is of 'unwanted software' threat|None|True|
|url|string|None|True|URL to lookup|None|https://example.com|

Example input:

```
{
  "threat_type_malware": true,
  "threat_type_social": true,
  "threat_type_unwanted": true,
  "url": "https://example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|expireTime|string|False|Time at which match should be considered expired|
|threatTypes|[]string|False|Threat types detected|

Example output:

```
{
  "expireTime": "2019-09-23T15:00:01.288672152Z",
  "threatTypes": [
     "MALWARE"
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Google's Web Risk API requires an API key for use. Sign up for the beta [here](https://docs.google.com/forms/d/e/1FAIpQLSf2mccuP6McSrhwOk1FXnsNY6c7xE-Url_pmjvFgz73A8qOxg/viewform)

# Version History

* 2.1.0 - Update SDK runtime | Look up URL action: fix building threat types | Add unit tests
* 2.0.1 - New spec and help.md format for the Extension Library
* 2.0.0 - New inputs for lookup action
* 1.0.0 - Initial plugin

# Links

## References

* [Google Web Risk API Documentation](https://cloud.google.com/web-risk/docs/)

