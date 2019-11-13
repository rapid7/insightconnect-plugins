# Description

[Cymon](https://cymon.io/) is the largest open tracker of malware, phishing, botnets, spam, and more.
This plugin utilizes the Cymon public API and implements all its available lookups.

**NOTE:** The Cymon service will be discontinued on April 30, 2019. Please plan to transition off this plugin before then.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|https\://cymon.io\:443|False|API URL|None|
|api_key|credential_secret_key|None|False|API Token (Empty for unauthenticated access)|None|

The connection configuration asks for an API Token and Server. The API Token field is not required,
since Cymon currently allows anonymous access but with a rate limit. For authenticated access, supply the token to allow for more requests.
A default value is provided for the server and should be used unless the Cymon API URL changes.

## Technical Details

### Actions

#### Domain Lookup

This action is used to look up a domain name.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ips|[]string|False|IPs|
|updated|string|False|Updated|
|sources|[]string|False|Sources|
|name|string|False|Name|
|urls|[]string|False|Cymon URL URLs|
|created|string|False|Created|
|found|boolean|False|Found|

Example output:

```

{
  "updated": "2018-08-19T05:06:13Z",
  "name": "google.com",
  "ips": [
    "https://cymon.io/api/nexus/v1/ip/217.23.1.48",
    "https://cymon.io/api/nexus/v1/ip/78.24.221.106",
    "https://cymon.io/api/nexus/v1/ip/172.217.6.46",
    "https://cymon.io/api/nexus/v1/ip/74.125.239.102",
    "https://cymon.io/api/nexus/v1/ip/74.125.224.6",
    "https://cymon.io/api/nexus/v1/ip/74.125.224.3",
    "https://cymon.io/api/nexus/v1/ip/74.125.224.7",
    "https://cymon.io/api/nexus/v1/ip/74.125.224.4",
    "https://cymon.io/api/nexus/v1/ip/74.125.239.128",
    "https://cymon.io/api/nexus/v1/ip/74.125.239.129"
    ...
  ],
  "created": "2015-01-26T12:31:37Z",
  "sources": [
    "malwaredb.malekal.com",
    "malwr.com",
    "ptr",
    "urlquery.net",
    "cleanmx-malware",
    "cleanmx-phishing"
  ],
  "urls": [
    "https://cymon.io/api/nexus/v1/url/https%253A%252F%252Fsites.google.com%252Fsite%252Fagthook%252Fagth.rar%253Fattredirects%253D0",
    "https://cymon.io/api/nexus/v1/url/https%253A%252F%252Fsites.google.com%252Fsite%252Fmainopexiorhost1%252Fhome%252FDoulCi%252520activator.zip%253Fattredirects%253D0%2526d%253D1",
    "https://cymon.io/api/nexus/v1/url/https%253A%252F%252Fdl.google.com%252Ftag%252Fs%252Fappguid%253D%257B8A69D345-D564-463C-AFF1-A69D9E530F96%257D%2526iid%253D%257B0B6B7F91-5260-ABF8-5B4F-75ECE5831804%257D%2526lang%253Dru%2526browser%253D3%2526usagestats%253D0%2526appname%253DGoogle%252520Chrome%2526needsadmin%253Dtrue%252Fupdate2%252Finstallers%252FChromeStandaloneSetup.exe",
    "https://cymon.io/api/nexus/v1/url/https%253A%252F%252Fdrive.google.com%252Fuc%253Fexport%253Ddownload%2526id%253D0B24p1DCLV01DZlp3U21GNERpeVE",
    "https://cymon.io/api/nexus/v1/url/https%253A%252F%252Fdrive.google.com%252Fuc%253Fexport%253Ddownload%2526id%253D0B5y35rkEDlBCNkZIajVmU0VVTDA",
    "https://cymon.io/api/nexus/v1/url/https%253A%252F%252Fdl.google.com%252Ftag%252Fs%252Fappguid%253D%257BD0AB2EBC-931B-4013-9FEB-C9C4C2225C8C%257D%2526iid%253D%257B5DBA3266-A59D-2553-E93A-1D30EACA26D3%257D%2526lang%253Den%2526browser%253D4%2526usagestats%253D0%2526appname%253DGoogle%252520voice%252520and%252520video%252520chat%2526needsadmin%253Dfalse%252Fgoogletalk%252Fgoogletalkplugin%252FGoogleVoiceAndVideoSetup.exe",
    "https://cymon.io/api/nexus/v1/url/https%253A%252F%252Fdl.google.com%252Ftag%252Fs%252Fappguid%253D%257B8A69D345-D564-463C-AFF1-A69D9E530F96%257D%2526iid%253D%257BC611DBC8-566D-2D4D-9CDD-E16C8F8F0776%257D%2526lang%253Den%2526browser%253D4%2526usagestats%253D1%2526appname%253DGoogle%252520Chrome%2526needsadmin%253Dprefers%2526ap%253D2.0-dev%2526installdataindex%253Ddefaultbrowser%252Fupdate2%252Finstallers%252FChromeSetup.exe",
    "https://cymon.io/api/nexus/v1/url/https%253A%252F%252Fdl.google.com%252Ftag%252Fs%252Fappguid%253D%257BD0AB2EBC-931B-4013-9FEB-C9C4C2225C8C%257D%2526iid%253D%257B75D97B7F-0223-9D3B-94E9-069792761382%257D%2526lang%253Dfil%2526browser%253D3%2526usagestats%253D0%2526appname%253DGoogle%252520voice%252520and%252520video%252520chat%2526needsadmin%253Dfalse%252Fgoogletalk%252Fgoogletalkplugin%252FGoogleVoiceAndVideoSetup.exe",
    "https://cymon.io/api/nexus/v1/url/https%253A%252F%252Fdl.google.com%252Ftag%252Fs%252Fappguid%253D%257B8A69D345-D564-463C-AFF1-A69D9E530F96%257D%2526iid%253D%257B898D583E-C7D8-B972-19EA-EB5F8F380DD8%257D%2526lang%253Dtr%2526browser%253D4%2526usagestats%253D0%2526appname%253DGoogle%252520Chrome%2526needsadmin%253Dprefers%2526installdataindex%253Ddefaultbrowser%252Fupdate2%252Finstallers%252FChromeSetup.exe",
    "https://cymon.io/api/nexus/v1/url/https%253A%252F%252Fdl.google.com%252Ftag%252Fs%252Fappguid%253D%257B8A69D345-D564-463C-AFF1-A69D9E530F96%257D%2526iid%253D%257B24C74E52-7553-8F49-AA5F-0EF2F733D37D%257D%2526lang%253Dtr%2526browser%253D4%2526usagestats%253D0%2526appname%253DGoogle%252520Chrome%2526needsadmin%253Dprefers%2526installdataindex%253Ddefaultbrowser%252Fupdate2%252Finstallers%252FChromeSetup.exe",
    "https://cymon.io/api/nexus/v1/url/http%253A%252F%252Fgoogle.com%252Furl%253Fq%253Dhttps%25253A%25252F%25252Fwww.dropbox.com%25252Fs%25252Fci5rbvosxaldq7c%25252FWIRE%25252520TRANSFER%25252+%2528...%2529"
    ...
  ],
  "found": true
}

```

#### Domain Blacklist

This action can be used to retrieve a user defined count of blacklisted domains based on one of the following threat categories:

* malware
* botnet
* spam
* phishing
* malicious activity
* blacklist
* dnsbl

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tag|string|None|True|Tag|['blacklist', 'malware', 'botnet', 'spam', 'phishing', 'malicious activity', 'dnsbl']|
|limit|integer|10|True|Number of Results, 1-5000|None|
|days|integer|None|True|Age of Data in Days|[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|False|Blacklist count|
|url|[]string|False|Cymon URL references|
|addr|[]string|False|Blacklisted domains|

Example output:

```

{
  "count": 657,
  "url": [
    "https://cymon.io/api/nexus/v1/domain/static.vnpt.vn",
    "https://cymon.io/api/nexus/v1/domain/static.vnpt.vn",
    "https://cymon.io/api/nexus/v1/domain/static.vnpt.vn",
    "https://cymon.io/api/nexus/v1/domain/static.vnpt.vn",
    "https://cymon.io/api/nexus/v1/domain/static.vnpt.vn",
    "https://cymon.io/api/nexus/v1/domain/static.vnpt.vn",
    "https://cymon.io/api/nexus/v1/domain/static.vnpt.vn",
    "https://cymon.io/api/nexus/v1/domain/static.vnpt.vn",
    "https://cymon.io/api/nexus/v1/domain/static.vnpt.vn",
    "https://cymon.io/api/nexus/v1/domain/static.vnpt.vn"
  ],
  "name": [
    "static.vnpt.vn",
    "static.vnpt.vn",
    "static.vnpt.vn",
    "static.vnpt.vn",
    "static.vnpt.vn",
    "static.vnpt.vn",
    "static.vnpt.vn",
    "static.vnpt.vn",
    "static.vnpt.vn",
    "static.vnpt.vn"
  ]
}

```

#### Address Blacklist

This action is used to retrieve blacklisted addresses.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tag|string|None|True|Tag|['blacklist', 'malware', 'botnet', 'spam', 'phishing', 'malicious activity', 'dnsbl']|
|limit|integer|10|True|Number of Results, 1-5000|None|
|days|integer|None|True|Age of Data in Days|[1, 2, 3]|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|count|integer|False|Blacklist count|
|url|[]string|False|Cymon URL references|
|addr|[]string|False|Blacklisted addresses|

Example output:

```

{
  "count": 1636,
  "url": [
    "https://cymon.io/api/nexus/v1/ip/89.248.174.55",
    "https://cymon.io/api/nexus/v1/ip/206.81.14.95",
    "https://cymon.io/api/nexus/v1/ip/45.248.86.13",
    "https://cymon.io/api/nexus/v1/ip/123.249.79.233",
    "https://cymon.io/api/nexus/v1/ip/212.237.2.20",
    "https://cymon.io/api/nexus/v1/ip/182.96.249.156",
    "https://cymon.io/api/nexus/v1/ip/123.249.79.214",
    "https://cymon.io/api/nexus/v1/ip/212.237.43.235",
    "https://cymon.io/api/nexus/v1/ip/182.76.113.162",
    "https://cymon.io/api/nexus/v1/ip/88.87.202.71"
  ],
  "addr": [
    "89.248.174.55",
    "206.81.14.95",
    "45.248.86.13",
    "123.249.79.233",
    "212.237.2.20",
    "182.96.249.156",
    "123.249.79.214",
    "212.237.43.235",
    "182.76.113.162",
    "88.87.202.71"
  ]
}

```

#### URL Lookup

This action is used to look up a URL.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|Full URL E.g. http\://faker.su/data/entry/steam/Steam.exe|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ips|[]string|False|Cymon IPs URL|
|updated|string|False|Updated date|
|sources|[]string|False|Sources|
|location|string|False|Location|
|created|string|False|Created date|
|found|boolean|False|Found in database|
|domain|string|False|Cymon Domain URL|

Example output:

```

{
  "updated": "2015-07-06T21:28:38Z",
  "ips": [
    "https://cymon.io/api/nexus/v1/ip/109.68.190.244",
    "https://cymon.io/api/nexus/v1/ip/94.75.240.108"
  ],
  "created": "2015-04-22T14:54:54Z",
  "domain": "https://cymon.io/api/nexus/v1/domain/faker.su",
  "sources": [
    "vxvault",
    "threatlog.com",
    "urlvir.com",
    "virustotal.com"
  ],
  "location": "http://faker.su/data/entry/steam/Steam.exe",
  "found": true
}

```

#### Address Lookup

This action is used to lookup an IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|string|None|True|IP Address|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|updated|string|False|Updated date|
|addr|string|False|IP address|
|created|string|False|Created date|
|sources|[]string|False|Sources|
|urls|string|False|Cymon URL URLs|
|domains|string|False|Cymon doman URLs|
|found|boolean|False|Found in database|
|events|string|False|Events|

Example output:

```

{
  "updated": "2017-12-14T23:03:09Z",
  "addr": "81.177.139.111",
  "created": "2015-10-10T00:43:18Z",
  "sources": [
    "blocklist.de",
    "labs.snort.org",
    "malwr.com",
    "virustotal.com",
    "urlquery.net",
    "google safebrowsing",
    "phishtank",
    "cleanmx-malware"
  ],
  "urls": "https://cymon.io/api/nexus/v1/ip/81.177.139.111/urls",
  "domains": "https://cymon.io/api/nexus/v1/ip/81.177.139.111/domains",
  "found": true,
  "events": "https://cymon.io/api/nexus/v1/ip/81.177.139.111/events"
}

```

### Triggers

#### Poll Domain Blacklist

This trigger is used to poll for a user defined count of blacklisted domains based on one of the following threat categories:

* malware
* botnet
* spam
* phishing
* malicious activity
* blacklist
* dnsbl

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|frequency|integer|300|False|Poll frequency in seconds|None|
|limit|integer|1|True|Number of Results, 1-5000|None|
|days|integer|None|True|Age of Data in Days|[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]|
|tag|string|None|True|Tag|['blacklist', 'malware', 'botnet', 'spam', 'phishing', 'malicious activity', 'dnsbl']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|domain_blacklist|True|Results|

Example output:

```

{
  "count": 636,
  "previous": "None",
  "results": [
    {
      "url": "https://cymon.io/api/nexus/v1/domain/static.vnpt.vn",
      "name": "static.vnpt.vn"
    }
  ],
  "next": "https://cymon.io/api/nexus/v1/blacklist/domain/blacklist/?days=1&limit=1&offset=1"
}

```

#### Poll Address Blacklist

This trigger is used to poll for a user defined count of blacklisted IP addresses based on one of the following threat categories:

* malware
* botnet
* spam
* phishing
* malicious activity
* blacklist
* dnsbl

The poll frequency can be set by the user but its default value is 5 minutes.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|frequency|integer|300|False|Poll frequency in seconds|None|
|limit|integer|1|True|Number of Results, 1-5000|None|
|days|integer|None|True|Age of Data in Days|[1, 2, 3]|
|tag|string|None|True|Tag|['blacklist', 'malware', 'botnet', 'spam', 'phishing', 'malicious activity', 'dnsbl']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|ip_blacklist|False|Results|

Example output:

```

{
  "count": 1581,
  "url": [
    "https://cymon.io/api/nexus/v1/ip/89.248.174.55",
    "https://cymon.io/api/nexus/v1/ip/206.81.14.95",
    "https://cymon.io/api/nexus/v1/ip/45.248.86.13",
    "https://cymon.io/api/nexus/v1/ip/123.249.79.233",
    "https://cymon.io/api/nexus/v1/ip/212.237.2.20",
    "https://cymon.io/api/nexus/v1/ip/182.96.249.156",
    "https://cymon.io/api/nexus/v1/ip/123.249.79.214",
    "https://cymon.io/api/nexus/v1/ip/212.237.43.235",
    "https://cymon.io/api/nexus/v1/ip/182.76.113.162",
    "https://cymon.io/api/nexus/v1/ip/88.87.202.71"
  ],
  "addr": [
    "89.248.174.55",
    "206.81.14.95",
    "45.248.86.13",
    "123.249.79.233",
    "212.237.2.20",
    "182.96.249.156",
    "123.249.79.214",
    "212.237.43.235",
    "182.76.113.162",
    "88.87.202.71"
  ]
}

```

##### Notes

One limitation of this trigger is that subsequent jobs may contain the same domains from previous requests.
The results will not be unique unless the user requested count of domains has been updated by count number of entries by Cymon.
To help reduce non-unique domains in subsequent requests, we recommend choosing a lower count value such as 5 or less and a
longer frequency such as 30 minutes. This may allow enough time to pass so that the next request of domains have been updated by Cymon.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Too large a count (such as 1000 or greater) for the blacklist actions and triggers may cause errors.
It's recommended to request a lower number of items. It's unclear what the maximum count number is from the API,
the count range 1-2000 has been tested and verified working by us.

# Version History

* 1.0.1 - Add discontinuation of Cymon notice
* 1.0.0 - Support web server mode
* 0.1.4 - Bug fix for CI tool incorrectly uploading plugins
* 0.1.3 - Update to v2 Python plugin architecture
* 0.1.2 - SSL bug fix in SDK
* 0.1.1 - Use password type for token, documentation updates
* 0.1.0 - Initial plugin

# Links

## References

* [Cymon](https://cymon.io/)
* [Cymon API](http://docs.cymon.io/)

