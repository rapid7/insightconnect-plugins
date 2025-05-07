# Description

[AbuseIPDB](https://www.abuseipdb.com) is a database of reported malicious IP addresses that are involved in malicious activity such as spamming, hack attempts, DDoS attacks, etc.

This plugin utilizes the [AbuseIPDB API v2](https://docs.abuseipdb.com) to lookup and report malicious IP addresses

# Key Features

* Look up an IP in the AbuseIP database to identify reported malicious IPs
* Get a complete list of reported IPs from AbuseIPDB
* Report an abusive IP address to add to AbuseIP's database

# Requirements

* Requires a [free AbuseIPDB account](https://www.abuseipdb.com/register) and accompanying API Key

# Supported Product Versions

* 2022-07-21

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|credentials|credential_secret_key|None|True|API key from account|None|e73h82c63847f3ff1h5216b556edh153h30430d73bchhe680f70h1d8885fb8bb130b46c7767d6886|None|None|

Example input:

```
{
  "credentials": "e73h82c63847f3ff1h5216b556edh153h30430d73bchhe680f70h1d8885fb8bb130b46c7767d6886"
}
```

## Technical Details

### Actions


#### Check CIDR

This action is used to look up a CIDR address in the database

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cidr|string|None|True|IPv4 address block in CIDR notation e.g. 207.126.144.0/20|None|207.196.144.0/24|None|None|
|days|string|30|True|Check for CIDR reports in the last x days|None|30|None|None|
  
Example input:

```
{
  "cidr": "207.196.144.0/24",
  "days": "30"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|addressSpaceDesc|string|False|Description of address space|Internet|
|found|boolean|True|Whether the CIDR was found in the database|True|
|maxAddress|string|False|Last address in block|207.196.144.255|
|minAddress|string|False|First address in block|207.196.144.0|
|netmask|string|False|Netmask, ie. 24|255.255.255.0|
|networkAddress|string|False|Network address in block|207.196.144.0|
|numPossibleHosts|integer|False|Number of possible hosts|111|
|reportedAddress|[]reportedIPs|False|List of reported IPs|[]|
  
Example output:

```
{
  "addressSpaceDesc": "Internet",
  "found": true,
  "maxAddress": "207.196.144.255",
  "minAddress": "207.196.144.0",
  "netmask": "255.255.255.0",
  "networkAddress": "207.196.144.0",
  "numPossibleHosts": 111,
  "reportedAddress": []
}
```

#### Check IP

This action is used to look up an IP address in the database

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|IPv4 or IPv6 address e.g. 198.51.100.100, ::1, must be subscribed to accept bitmask wider than 255.255.255.0 (/24)|None|198.51.100.100|None|None|
|days|string|30|True|Check for IP reports in the last x days|None|30|None|None|
|verbose|boolean|True|True|When set, reports will include the comment (if any) and the reporter's user ID number (0 if reported anonymously)|None|True|None|None|
  
Example input:

```
{
  "address": "198.51.100.100",
  "days": "30",
  "verbose": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|abuseConfidenceScore|integer|False|Confidence of Abuse|0|
|countryCode|string|False|Code of country IP is registered in|CN|
|countryName|string|False|Name of Country IP is registered in|China|
|domain|string|False|Domain Name of IP|tencent.com|
|found|boolean|False|Whether an IP address was found, indicating it may be malicious|True|
|ipAddress|string|False|Queried IP Address|198.51.100.100|
|ipVersion|integer|False|Version of IP Address|4|
|isPublic|boolean|False|Whether or not the IP Address is public|True|
|isWhitelisted|boolean|False|Whether or not IP Address is whitelisted|True|
|isp|string|False|Internet Service Provider for IP|Tencent Cloud Computing (Beijing) Co. Ltd|
|lastReportedAt|string|False|Date of last report|2022-09-21 13:21:18+00:00|
|numDistinctUsers|integer|False|Number of distinct users who reported IP|0|
|reports|[]report|False|List of reports|[]|
|totalReports|integer|False|Total number of reports of abuse|0|
|usageType|string|False|How IP is used|Reserved|
  
Example output:

```
{
  "abuseConfidenceScore": 0,
  "countryCode": "CN",
  "countryName": "China",
  "domain": "tencent.com",
  "found": true,
  "ipAddress": "198.51.100.100",
  "ipVersion": 4,
  "isPublic": true,
  "isWhitelisted": true,
  "isp": "Tencent Cloud Computing (Beijing) Co. Ltd",
  "lastReportedAt": "2022-09-21 13:21:18+00:00",
  "numDistinctUsers": 0,
  "reports": [],
  "totalReports": 0,
  "usageType": "Reserved"
}
```

#### Get Blacklist

This action is used to list of blacklisted IP addresses

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|confidenceMinimum|string|None|True|Minimum confidence to filter by, scaled 0-100, least to most confident|None|90|None|None|
|limit|string|None|False|Max length of blacklist|None|10|None|None|
  
Example input:

```
{
  "confidenceMinimum": "90",
  "limit": "10"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|blacklist|[]blacklisted|False|List of abusive IPs|[{"ipAddress": "198.51.100.100", "abuseConfidenceScore": "100"}, {"ipAddress": "198.51.100.101", "abuseConfidenceScore": "100"}, {"ipAddress": "198.51.100.102", "abuseConfidenceScore": "100"}]|
|success|boolean|True|Was the blacklist successfully retrieved|True|
  
Example output:

```
{
  "blacklist": [
    {
      "abuseConfidenceScore": "100",
      "ipAddress": "198.51.100.100"
    },
    {
      "abuseConfidenceScore": "100",
      "ipAddress": "198.51.100.101"
    },
    {
      "abuseConfidenceScore": "100",
      "ipAddress": "198.51.100.102"
    }
  ],
  "success": true
}
```

#### Report IP

This action is used to report an abusive IP address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|categories|string|None|True|Comma delineated list of category IDs e.g. 10,12,15. Entire list is available at https://www.abuseipdb.com/categories|None|10,12,15|None|None|
|comment|string|None|False|Describe the type of malicious activity e.g. Brute forcing Wordpress login|None|Brute forcing Wordpress|None|None|
|ip|string|None|True|IPv4 or IPv6 address to report e.g. 198.51.100.100, ::1|None|198.51.100.100|None|None|
  
Example input:

```
{
  "categories": "10,12,15",
  "comment": "Brute forcing Wordpress",
  "ip": "198.51.100.100"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|abuseConfidenceScore|integer|False|Confidence that reported IP is abusive|52|
|ipAddress|string|False|IP address submitted|127.0.0.1|
|success|boolean|True|Submission success|True|
  
Example output:

```
{
  "abuseConfidenceScore": 52,
  "ipAddress": "127.0.0.1",
  "success": true
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**blacklisted**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Abuse Confidence Score|string|None|True|Confidence that IP is abusive|None|
|IP Address|string|None|True|IP Address of abusive IP|None|
  
**report**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Categories|[]integer|None|False|List of categories|None|
|Comment|string|None|False|Comment by reporter|None|
|Reported At|string|None|False|Date and time of report|None|
|Reporter Country Code|string|None|False|Country code of the reporter|None|
|Reporter Country Name|string|None|False|Name of country reporter is from|None|
|Reporter ID|integer|None|False|ID number of reporter|None|
  
**reportedIPs**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Abuse Confidence Score|integer|None|None|Confidence that this IP is abusive|None|
|Country Code|string|None|None|Country code of IP|None|
|IP|string|None|None|IP Address of reported resource|None|
|Most Recent Report|string|None|None|Most recent report for this IP|None|
|Number of Reports|integer|None|None|Number of reports of this IP|None|


## Troubleshooting

* The `success` output field will be set to `false` if the output body is empty, or if the input cannot be found
* There's a rate limit on the free API service. The following error messages `429 Client Error: Too Many Requests for url` indicates that threshold has been hit

# Version History

* 5.1.1 - Updated SDK to the latest version (6.3.3)
* 5.1.0 - Cloud Enabled
* 5.0.9 - Fix incorrect status code for failed connection test
* 5.0.8 - Set cloud_ready flag to false | Changed description for output 'found'
* 5.0.7 - Fix error message in IPv4 search
* 5.0.6 - Fix none type error in Check CIDR action
* 5.0.5 - Correct spelling in help.md
* 5.0.4 - Update to v4 Python plugin runtime
* 5.0.3 - Add example inputs
* 5.0.2 - Changed descriptions | Removed duplicated code | Use output constants | Added "f" strings
* 5.0.1 - New spec and help.md format for the Extension Library
* 5.0.0 - Mark certain outputs as optional as they are not always returned by the AbuseIPDB service | Clean output of null values
* 4.0.1 - Transform null value of various output properties of Check IP action to false or empty string.
* 4.0.0 - Update to APIv2 and new action Get Blacklist
* 3.0.1 - Improve error handling in the Check IP, Check CIDR, and Report IP actions | Update to use the `komand/python-3-37-slim-plugin` Docker image to reduce plugin size | Run plugin as least privileged user | Add connection test
* 3.0.0 - Support new credential_secret_key type
* 2.0.0 - Add `found` output to Check IP action | Support new credential type
* 1.0.0 - Initial plugin

# Links

* [AbuseIPDB](https://www.abuseipdb.com)

## References

* [AbuseIPDB API](https://docs.abuseipdb.com)