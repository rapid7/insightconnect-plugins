# Description

Submit URLs to the [Google Safe Browsing](https://safebrowsing.google.com/) Service to detect whether a URL is malicious or not.

# Key Features

* URL enrichment

# Requirements

* API Key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_secret_key|None|True|API token|None|

## Technical Details

### Actions

#### Lookup URL

This action is used to lookup URL in Safe Browsing Service.

##### Input

This action is used to submit a URL. It accepts the following options:

* Client ID
* Threat Type
* Threat Entry Type
* Platform Type

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|threat_type_malware|boolean|None|False|Check if URL is of 'malware' threat|None|
|platform_type_any|boolean|None|False|Check URL against any platform|None|
|threat_entry_type_url|boolean|None|False|Check URL against URL threat entry type|None|
|threat_type_unwanted|boolean|None|False|Check if URL is of 'unwanted software' threat|None|
|threat_type_potential|boolean|None|False|Check if URL is of 'potentially harmful application' threat|None|
|client_id|string|None|False|Unique identifier, e.g. 'komand-<your_company>'|None|
|platform_type_all|boolean|None|False|Check URL against all platforms|None|
|threat_entry_type_unspecified|boolean|None|False|Check URL against unspecified threat entry type|None|
|threat_entry_type_executable|boolean|None|False|Check URL against executable threat entry type|None|
|platform_type_linux|boolean|None|False|Check URL against Linux platform|None|
|threat_type_unspecified|boolean|None|False|Check if URL is of 'unspecified' threat|None|
|platform_type_android|boolean|None|False|Check URL against Android platform|None|
|platform_type_windows|boolean|None|False|Check URL against Windows platform|None|
|platform_type_unspecified|boolean|None|False|Check URL against unspecified platform|None|
|platform_type_ios|boolean|None|False|Check URL against iOS platform|None|
|threat_entry_type_ip|boolean|None|False|Check URL against IP range threat entry type|None|
|platform_type_mac|boolean|None|False|Check URL against Mac OS platform|None|
|threat_type_social|boolean|None|False|Check if URL is of 'social engineering/phishing' threat|None|
|urls|[]string|None|True|URLs to check (up to 500)|None|
|platform_type_chrome|boolean|None|False|Check URL against Chrome platform|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|matches|[]match|False|Matches from Google Safe Browsing|
|results|integer|False|Number of results returned|

Example output:

```

{
  "matches": [
    {
      "threatType": "MALWARE",
      "platformType": "ALL_PLATFORMS",
      "threat": {
        "url": "freefilesdownloader.com"
      },
      "cacheDuration": "300s",
      "threatEntryType": "URL",
    }
  ],
  "results": 1,
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

* Only up to 500 URLs can be submitted at a time.
* URLs must be submitted as an array e.g. `[ "harmfulapps.com" ]`
* You can test the plugin with the following example URL harmfulapps.com

# Version History

* 2.0.0 - Obsolete
* 1.0.0 - Support web server mode | Update to new credential types
* 0.1.8 - Bug fix for no results | Updated to v2 architecture
* 0.1.7 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Google Safe Browsing](https://developers.google.com/safe-browsing/)

