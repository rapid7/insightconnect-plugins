# Description

Phishtank is a community-driven anti-phishing site where users submit suspected phishes and other users 'vote' if it is a phish or not. This plugin utilizes the Phishtank API to look up URLs in the PhishTank database

# Key Features

* Submit URLs to identify reported phishing links

# Requirements

* PhishTank API key

# Supported Product Versions

* 2024-20-03

# Documentation

## Setup

This plugin requires a PhishTank API key to authenticate.

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_secret_key|None|True|The API key to use|None|secret_key|

Example input:

```
{
  "credentials": "secret_key"
}
```

## Technical Details

### Actions

#### Check URL

This action is used to submit a URL to PhishTank

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|url|string|None|True|URL to Submit|None|example.com|
  
Example input:

```
{
  "url": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|in_database|boolean|False|If the URL is in the PhishTank database|False|
|phish_detail_url|string|False|PhishTank detail URL for the phish, where you can view data about the phish, including a screenshot and the community votes|http://data.phishtank.com/data/online-valid.json|
|phish_id|string|False|The ID number by which PhishTank refers to a phish submission|9014567|
|submitted_at|date|False|The date and time at which this phish was reported to PhishTank|2009-06-20 15:37:31+00:00|
|url|string|False|Submitted URL|example.com|
|valid|boolean|False|Whether the phish is valid or not|True|
|verified|boolean|False|Whether or not this phish has been verified by the PhishTank community|True|
|verified_at|date|False|The date and time at which the phish was verified as valid by the PhishTank community|2009-06-20 15:37:31+00:00|
  
Example output:

```
{
  "in_database": false,
  "phish_detail_url": "http://data.phishtank.com/data/online-valid.json",
  "phish_id": 9014567,
  "submitted_at": "2009-06-20 15:37:31+00:00",
  "url": "example.com",
  "valid": true,
  "verified": true,
  "verified_at": "2009-06-20 15:37:31+00:00"
}
```
### Triggers
  
*This plugin does not contain any triggers.*

### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History

* 1.0.3 - Version bumped requirements.txt | Updated SDK
* 1.0.2 - Update requests library
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.4 - SSL bug fix in SDK
* 0.1.3 - Fix API usage
* 0.1.2 - Fix connection test
* 0.1.1 - Fix bug with `verified_at` containing `None` type value and improve connection title and description
* 0.1.0 - Initial plugin

# Links

* [PhishTank](https://www.phishtank.com/)

## References

* [PhishTank](https://www.phishtank.com/)
* [PhishTank API](https://www.phishtank.com/api_info.php)
