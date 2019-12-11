# Description

The AbuseIPDB InsightConnect plugin enables the look up of IP reports, provides list and details of blacklisted IPs, and submission of abusive IPs.

This plugin utilizes [AbuseIPDB API v2](https://docs.abuseipdb.com).

# Key Features

* Report abusive IPs
* Get blacklisted IPs
* Get IP details

# Requirements

* Requires a [free AbuseIPDB account](https://www.abuseipdb.com/register) and accompanying API Key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_secret_key|None|True|API key|None|

## Technical Details

### Actions

#### Report IP

This action is used to report an abusive IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|categories|string|None|True|Comma delineated list of category IDs e.g. 10,12,15. Entire list is available at https://www.abuseipdb.com/categories|None|
|comment|string|None|False|Describe the type of malicious activity e.g. Brute forcing Wordpress login|None|
|ip|string|None|True|IPv4 or IPv6 address to report e.g. 8.8.8.8, ::1|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|abuseConfidenceScore|integer|False|Confidence that reported IP is abusive|
|ipAddress|string|False|IP address submitted|
|success|boolean|True|Submission success|

Example output:

```
{
  "ipAddress": "127.0.0.1",
  "abuseConfidenceScore": 52,
  "success": true
}
```

If AbuseIPDB returns an empty JSON body, success will be set to false.

Failure Example:

```
{
  "success": false
}
```

#### Check IP

This action is used to look up an IP address in the database.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|string|None|True|IPv4 or IPv6 address e.g. 8.8.8.8, ::1|None|
|days|string|30|True|Check for IP reports in the last x days|None|
|verbose|boolean|True|True|When set, reports will include the comment (if any) and the reporter's user ID number (0 if reported anonymously)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|abuseConfidenceScore|integer|False|Confidence of Abuse|
|countryCode|string|False|Code of country IP is registered in|
|countryName|string|False|Name of Country IP is registered in|
|domain|string|False|Domain Name of IP|
|found|boolean|False|Whether an IP address was found in the database|
|ipAddress|string|False|Queried IP Address|
|ipVersion|integer|False|Version of IP Address|
|isPublic|boolean|False|Whether or not the IP Address is public|
|isWhitelisted|boolean|False|Whether or not IP Address is whitelisted|
|isp|string|False|Internet Service Provider for IP|
|lastReportedAt|string|False|Date of last report|
|numDistinctUsers|integer|False|Number of distinct users who reported IP|
|reports|[]report|False|List of reports|
|totalReports|integer|False|Total number of reports of abuse|
|usageType|string|False|How IP is used|

Example output:

```
{
  "ipAddress": "118.25.6.39",
  "isPublic": true,
  "ipVersion": 4,
  "isWhitelisted": false,
  "abuseConfidenceScore": 100,
  "countryCode": "CN",
  "countryName": "China",
  "usageType": "Data Center/Web Hosting/Transit",
  "isp": "Tencent Cloud Computing (Beijing) Co. Ltd",
  "domain": "tencent.com",
  "totalReports": 1,
  "numDistinctUsers": 1,
  "lastReportedAt": "2018-12-20T20:55:14+00:00",
  "reports": [
    {
      "reportedAt": "2018-12-20T20:55:14+00:00",
      "comment": "Dec 20 20:55:14 srv206 sshd[13937]: Invalid user oracle from 118.25.6.39",
      "categories": [
        18,
        22
      ],
      "reporterId": 1,
      "reporterCountryCode": "US",
      "reporterCountryName": "United States"
    }
  ],
  "found": true
}
```

If AbuseIPDB could not find the input address, found will be set to false.

Failure Example:

```
{
  "found": false
}
```

#### Check CIDR

This action is used to look up a CIDR address in the database.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|cidr|string|None|True|IPv4 address block in CIDR notation e.g. 207.126.144.0/20|None|
|days|string|30|True|Check for CIDR reports in the last x days|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|addressSpaceDesc|string|False|Address space description|
|found|boolean|True|Whether the CIDR was found in the database|
|maxAddress|string|False|Maximum address|
|minAddress|string|False|Minimum address|
|netmask|string|False|Netmask|
|networkAddress|string|False|Network address|
|numPossibleHosts|integer|False|Number of possible hosts|
|reportedAddress|[]reportedIPs|False|List of reported IPs|

Example output:

```
{
  "networkAddress": "1.2.3.0",
  "netmask": "255.255.255.0",
  "minAddress": "1.2.3.1",
  "maxAddress": "1.2.3.254",
  "numPossibleHosts": 254,
  "addressSpaceDesc": "Internet",
  "reportedAddress": [
    {
      "ipAddress": "1.2.3.4",
      "numReports": 3,
      "mostRecentReport": "2019-08-28T21:08:34+01:00",
      "abuseConfidenceScore": 11,
      "countryCode": "AU"
    }
  ],
  "found": true
}
```

If AbuseIPDB could not find the input CIDR, found will be set to false.

Failure Example:

```
{
  "found: false
}
```

#### Get Blacklist

This action is used to list of blacklisted IP addresses.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|confidenceMinimum|string|None|True|Minimum confidence to filter by|None|
|limit|string|None|False|Max length of blacklist|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|blacklist|[]blacklisted|False|List of abusive IPs|
|success|boolean|True|Was the blacklist successfully retrieved|

Example output:

```
  "blacklist": [
    {
      "ipAddress": "5.188.10.179",
      "abuseConfidenceScore": 100
    },
    {
      "ipAddress": "185.222.209.14",
      "abuseConfidenceScore": 100
    },
    {
      "ipAddress": "191.96.249.183",
      "abuseConfidenceScore": 100
    }
  ],
  "success": true
```

If AbuseIPD fails to return the Blacklist, success will be set to false.

Failure Example:

```
{
  "success": false
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

#### blacklisted

|Name|Type|Required|Description|
|----|----|--------|-----------|
|abuseConfidenceScore|string|True|Confidence that IP is abusive|
|ipAddress|string|True|IP Address of abusive IP|

#### report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|categories|[]integer|True|List of categories|
|comment|string|True|Comment by reporter|
|reportedAt|string|True|Date and time of report|
|reporterCountryCode|string|True|Country code of the reporter|
|reporterCountryName|string|True|Name of country reporter is from|
|reporterId|integer|True|ID number of reporter|

#### reportedIPs

|Name|Type|Required|Description|
|----|----|--------|-----------|
|abuseConfidenceScore|integer|False|Confidence that this IP is abusive|
|countryCode|string|False|Country code of IP|
|ipAddress|string|False|IP Address of reported resource|
|mostRecentReport|string|False|Most recent report for this IP|
|numReports|integer|False|Number of reports of this IP|

## Troubleshooting

There's a rate limit on the free API service. The following error messags `429 Client Error: Too Many Requests for url` indicates that threshold has been hit.

# Version History

* 5.0.1 - New spec and help.md format for the Hub
* 5.0.0 - Mark certain outputs as optional as they are not always returned by the AbuseIPDB service | Clean output of null values
* 4.0.1 - Transform null value of various output properties of Check IP action to false or empty string.
* 4.0.0 - Update to APIv2 and new action Get Blacklist
* 3.0.1 - Improve error handling in the Check IP, Check CIDR, and Report IP actions | Update to use the `komand/python-3-37-slim-plugin` Docker image to reduce plugin size | Run plugin as least privileged user | Add connection test
* 3.0.0 - Support new credential_secret_key type
* 2.0.0 - Add `found` output to Check IP action | Support new credential type
* 1.0.0 - Initial plugin

# Links

## References

* [AbuseIPDB](https://www.abuseipdb.com)
* [AbuseIPDB API](https://docs.abuseipdb.com)

