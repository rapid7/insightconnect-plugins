# Description

[Proofpoint URL Defense](https://www.proofpoint.com/us) is a service designed to handle emails that contain 
malicious URLs. This plugin decodes URLs that are encoded by Proofpoints URL Defense service using ppdecode.

# Key Features

* Decode a URL to its original form

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### URL Decode

This action is used to take a Proofpoint URL and decode it to the original URL.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|encoded_url|string|None|True|Proofpoint encoded URL or URL parameters e.g http-3A__www.example.org_url&d=BwdwBAg&c=TIwfCwdwWnrHy3gMA_uzZorHPsT2wfwvKrwfU|None|http-3A__www.example.org_url&d=BwdwBAg&c=TIwfCwdwWnrHy3gMA_uzZorHPsT2wfwvKrwf|

Example input:

```
{
  "encoded_url": "http-3A__www.example.org_url\u0026d=BwdwBAg\u0026c=TIwfCwdwWnrHy3gMA_uzZorHPsT2wfwvKrwf"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|decoded|boolean|True|Was decode successful, if not, the original URL will be returned|
|decoded_url|string|False|Decoded Proofpoint URL|

Example output:

```
{
  "decoded_url": "http://www.example.org/url",
  "decode_success": true
}
```


### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.2.1 - Update to use the `insightconnect-python-3-38-slim-plugin:4` Docker image | Update plugin.spec.yaml to include `cloud_ready`
* 1.2.0 - Update to URL Decode to add `decoded` as an output variable 
* 1.1.0 - Update to URL Decode action to add support for v3 links
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Bug fix with decode parsing
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Proofpoint URL Defense](https://www.proofpoint.com/us/products/targeted-attack-protection)
* [Proofpoint decode utility](https://help.proofpoint.com/@api/deki/files/177/URLDefenseDecode.py?revision=2)
