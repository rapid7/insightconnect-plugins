# Description

[PhishTank](https://www.phishtank.com/) is a community-driven anti-phishing site where users submit suspected phishes and other users "vote" if it is a phish or not. This plugin utilizes the [PhishTank API](https://www.phishtank.com/api_info.php) to look up URLs in the PhishTank database.

# Key Features

* Submit URLs to identify reported phishing links

# Requirements

* PhishTank API key

# Documentation

## Setup

This plugin requires a PhishTank API key to authenticate.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|string|None|False|API key to use to connect (Empty for unauthenticated access)|None|

## Technical Details

### Actions

#### Check URL

This action is used to submit a URL to PhishTank.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|URL to Submit|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|verified|boolean|False|Whether or not this phish has been verified by the PhishTank community|
|submitted_at|date|False|The date and time at which this phish was reported to PhishTank|
|url|string|False|Submitted URL|
|verified_at|date|False|The date and time at which the phish was verified as valid by the PhishTank community|
|phish_id|string|False|The ID number by which PhishTank refers to a phish submission|
|valid|boolean|False|Whether the phish is valid or not|
|phish_detail_url|string|False|PhishTank detail URL for the phish, where you can view data about the phish, including a screenshot and the community votes|
|in_database|boolean|False|If the URL is in the PhishTank database|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.4 - SSL bug fix in SDK
* 0.1.3 - Fix API usage
* 0.1.2 - Fix connection test
* 0.1.1 - Fix bug with `verified_at` containing `None` type value and improve connection title and description
* 0.1.0 - Initial plugin

# Links

## References

* [PhishTank](https://www.phishtank.com/)
* [PhishTank API](https://www.phishtank.com/api_info.php)

