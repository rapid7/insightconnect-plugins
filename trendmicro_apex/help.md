# Description

Trend Micro Apex offers modern advanced automated threat detection and response.  Apex agents have more than antivirus
capabilities, they are an extension of the Apex threat management system.  
This plugin works for the on-premise or Apex SaaS configurations.

# Key Features

* Reporting suspicious IP addresses, URLs and other similar content
* Reporting suspicious files and their contents

# Requirements

* API URL for Apex SaaS or Apex on-premise
* API Key
* Application ID

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|API key paired with the Application ID|None|
|application_id|credential_secret_key|None|True|Application ID to communicate to the Apex Security Manager|None|
|url|string|None|True|URL with port number of the Apex Security Manager.|None|

Example input:

```
{
  "api_key": {
      "secretKey": "CU1874A2-G782-47X1-B6J3-1014A92624BC"
  },
  "application_id": {
      "secretKey": "909D88H7-3458-42RN-92FF-012V3CU3D294"
  },
  "url": "https://host.example.com:443"
}
```

## Technical Details

### Actions

#### Add to UDSO List

This action is used to add an IP address, email or similar info to the UDSO list.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|content|string|None|True|The item to be filed as suspicious. data_type affects character limit.  URL/DOMAIN are 2046 characters max, SHA is 40 characters max|None|
|data_type|string|URL|True|Format of the data, character length of content is affected by this|['IP', 'URL', 'FILE_SHA1', 'DOMAIN']|
|expiry_date|int|30|False|Number of days to allow this rule to be active|None|
|notes|string|None|False|Notes about why the file is being quarantined (256 characters max)|None|
|scan_action|string|LOG|True|What action to do with the data sent|['BLOCK', 'LOG']|

Example input:

```
{
  "content": "1.2.3.4"
  "scan_action": "BLOCK",
  "data_type": "IP",
  "expiry_date": 44,
  "notes": "block sesame streets IP address"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether or not the action was successful|

Example output:

```
{
  "success": true
}
```

#### Add File to UDSO List

This action is used to add a file to the UDSO list of the Apex Security Manager.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file|file|None|True|File to be marked as suspicious|None|
|notes|string|None|False|Notes about why the file is being quarantined (256 characters max)|None|
|scan_action|string|LOG|True|What action to do with the data sent|['BLOCK', 'LOG', 'QUARANTINE']|

Example input:

```
{
  "file": {
    "filename": "file.txt",
    "content": "c2xpamJvb20="
  },
  "scan_action": "BLOCK",
  "notes": "This is the most suspicious file I have ever seen"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether or not the action was successful|

Example output:

```
{
  "success": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Trend Micro Apex test accounts are subject to an expiration policy. Sign up for a new account if the becomes expired.
[link](https://www.trendmicro.com/en_ca/business/products/user-protection/sps/endpoint.html). Look for "Try for Free"

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [Trend Micro Apex](https://www.trendmicro.com/en_ca/business/products/user-protection/sps/endpoint.html)
* [Apex API](https://beta-community-trendmicro.cs23.force.com/automationcenter/apex-central/api)
