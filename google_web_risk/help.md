# Description

[Google Web Risk](https://cloud.google.com/web-risk/) checks URLs against the Google Web Risk service.

# Key Features

* Lookup URL in web risk service

# Requirements

* WebRisk API token

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_secret_key|None|True|API token|None|

## Technical Details

### Actions

#### Lookup URL

This action is used to lookup a URL in Web Risk Service.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|threat_type_malware|boolean|true|false|Check if URL is of 'malware' threat|None|
|threat_type_social|boolean|true|false|Check if URL is of 'social engineering/phishing' threat|None|
|threat_type_unwanted|boolean|true|false|Check if URL is of 'unwanted software' threat|None|
|url|string|None|true|URL to lookup|None|

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
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Google's Web Risk API requires an API key for use. Sign up for the beta [here](https://docs.google.com/forms/d/e/1FAIpQLSf2mccuP6McSrhwOk1FXnsNY6c7xE-Url_pmjvFgz73A8qOxg/viewform)

# Version History

* 2.0.0 - New inputs for lookup action
* 1.0.0 - Initial plugin

# Links

## References

* [Google Web Risk API Documentation](https://cloud.google.com/web-risk/docs/)

