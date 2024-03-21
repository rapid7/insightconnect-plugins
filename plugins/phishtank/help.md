# Description

Phishtank is a community-driven anti-phishing site where users submit suspected phishes and other users 'vote' if it is a phish or not. This plugin utilizes the Phishtank API to look up URLs in the PhishTank database.

# Key Features
  
* Submit URLs to identify reported phishing links

# Requirements
  
* PhishTank API key

# Supported Product Versions
  
* 2024-20-03

# Documentation

## Setup
  
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
|submitted_at|date|False|The date and time at which this phish was reported to PhishTank|<date><time>|
|url|string|False|Submitted URL|example.com|
|valid|boolean|False|Whether the phish is valid or not|True|
|verified|boolean|False|Whether or not this phish has been verified by the PhishTank community|True|
|verified_at|date|False|The date and time at which the phish was verified as valid by the PhishTank community|<date><time>|
  
Example output:

```
{
  "in_database": false,
  "phish_detail_url": "http://data.phishtank.com/data/online-valid.json",
  "phish_id": 9014567,
  "submitted_at": "<date><time>",
  "url": "example.com",
  "valid": true,
  "verified": true,
  "verified_at": "<date><time>"
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
  
*This plugin does not contain a version history.*

# Links


## References
  
* [PhishTank](https://www.phishtank.com/)  
* [PhishTank API](https://www.phishtank.com/api_info.php)