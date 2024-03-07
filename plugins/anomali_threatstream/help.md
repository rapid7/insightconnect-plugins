# Description

[Anomali ThreatStream](https://www.anomali.com/) is an operational threat intelligence stream, automating collection and integration that enables security teams to analyze and respond to threats.
The Anomali ThreatStream InsightConnect plugin allows you lookup hashes, IP addresses, URLs, observables. It also allows importing observables.
This plugin utilizes the Anomali ThreatStream API, which is located with the cloud instance at `http://<Anomali ThreatStream API host>/optic-doc/ThreatStream_OnlineHelp.htm`.

# Key Features

* Lookup hashes, IP addresses, and URLs
* Import observables
* Get observables

# Requirements

* Anomali ThreatStream username
* Anomali ThreatStream instance URL
* Anomali ThreatStream API key

# Documentation

## Setup
  
The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|Anomali ThreatStream API key|None|9de5069c5afe602b2ea0a04b66beb2c0|
|ssl_verify|boolean|True|True|Verify the server's SSL/TLS certificate|None|True|
|url|string|None|True|URL for the ThreatStream instance|None|https://ts.example.com|
|username|string|None|True|Anomali ThreatStream username|None|user1|
  
Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "ssl_verify": true,
  "url": "https://ts.example.com",
  "username": "user1"
}
```

## Technical Details

### Actions


#### Get Observables
  
This action is used to get observables

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|value|string|None|False|Value|None|Example observable|
  
Example input:

```
{
  "value": "Example observable"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]result|False|Results returned|[ { "status": "/api/v1/submit/101/", "detail": "/api/v1/submit/101/report/", "id": 101, "platform": "WINDOWS7" }, { "status": "/api/v1/submit/100/", "detail": "/api/v1/submit/100/report/", "id": 100, "platform": "WINDOWSXP" } ]|
  
Example output:

```
{
  "results": [
    {
      "detail": "/api/v1/submit/101/report/",
      "id": 101,
      "platform": "WINDOWS7",
      "status": "/api/v1/submit/101/"
    },
    {
      "detail": "/api/v1/submit/100/report/",
      "id": 100,
      "platform": "WINDOWSXP",
      "status": "/api/v1/submit/100/"
    }
  ]
}
```

#### Get Sandbox Report
  
This action is used to get a sandbox report

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|report_id|string|None|True|Report ID|None|101|
  
Example input:

```
{
  "report_id": 101
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|sandbox_report|sandbox_report|True|Sandbox report|None|
  
Example output:

```
{
  "sandbox_report": {
    "domains": [
      "star-mini.c10r.facebook.com",
      "pagead46.l.doubleclick.net",
      "star.c10r.facebook.com",
      "us-u.openx.net"
    ],
    "info": {
      "category": "URL",
      "confidence": 0,
      "duration": 302,
      "ended": "2019-12-04 21:09:32",
      "is_malicious": false,
      "is_suspicious": false,
      "is_unknown": false,
      "started": "2019-12-04 21:04:30"
    },
    "screenshots": [
      "http://domain.com/userUploads/2019-12-04/20191204_201304_userId-121_tmpsandbox-report-full-PaRfUDscreenshot_00.png",
      "http://domain.com/userUploads/2019-12-04/20191204_201305_userId-121_tmpsandbox-report-full-PaRfUDscreenshot_01.png",
      "http://domain.com/userUploads/2019-12-04/20191204_201305_userId-121_tmpsandbox-report-full-PaRfUDscreenshot_02.png"
    ],
    "signatures": [
      {
        "data": [
          {
            "operation": "Window detected",
            "process": "Window Recorder",
            "value": "More than 3 window changes detected"
          }
        ],
        "description": "Found graphical window changes (likely an installer)",
        "severity": "-2.0"
      },
      {
        "data": [
          {
            "operation": "File opened",
            "process": "C:\\Program Files (x86)\\Internet Explorer\\iexplore.exe",
            "value": "C:\\Program Files (x86)\\Java\\jre1.8.0_191\\bin\\msvcr100.dll"
          }
        ],
        "description": "Uses new MSVCR Dlls",
        "severity": "-1.0"
      }
    ]
  }
}
```

#### Import Observable
  
This action is used to import observable(s) into Anomali ThreatStream with approval

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|file|file|None|True|File of data to be imported into Anomali ThreatStream|None|setup.exe|
|observable_settings|observable_settings|None|False|Settings needed for importing an observable that needs approval|None|none|
  
Example input:

```
{
  "file": "setup.exe",
  "observable_settings": "none"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|import_observable_response|False|Results from importing observable(s)|None|
  
Example output:

```
{
  "results": {
    "job_id": "00bc2d03-c608-4824-863d-0a7c9126615a",
    "success": true,
    "import_session_id": "1000000344"
  }
}
```

#### Lookup Hash
  
This action is used to lookup a file hash in Anomali ThreatStream

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|hash|string|None|False|Hash|None|275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f|
  
Example input:

```
{
  "hash": "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]result|False|Results returned|None|
  
Example output:

```
{
  "results": [
    {
      "classification": "private",
      "confidence": "17",
      "date_first": "2019-10-16T16:12:48",
      "date_last": "2019-10-21T14:01:39",
      "detail": "Delivery",
      "detail2": "imported by user 121",
      "domain": "window.google",
      "id": 112879000,
      "import_session_id": 205,
      "itype": "apt_domain",
      "maltype": "Delivery",
      "resource_uri": "/api/v1/intelligence/112879000/",
      "severity": "very-high",
      "source": "user@example.com",
      "srcip": "127.0.53.53",
      "state": "active",
      "update_id": "272270002"
    }
  ]
}
```

#### Lookup IP Address
  
This action is used to lookup an IP address in Anomali ThreatStream

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ip_address|string|None|False|IP address|None|192.168.1.1|
  
Example input:

```
{
  "ip_address": "192.168.1.1"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]result|False|Results returned|None|
  
Example output:

```
{
  "results": [
    {
      "asn": "26496",
      "classification": "private",
      "confidence": "100",
      "country": "US",
      "date_first": "2018-09-06T23:01:26",
      "date_last": "2018-09-06T23:01:26",
      "detail2": "imported by user 1000000012",
      "id": 1000000181,
      "itype": "mal_url",
      "lat": 33.6119,
      "lon": -111.8906,
      "org": "GoDaddy.com, LLC",
      "resource_uri": "/api/v1/intelligence/1000000181/",
      "severity": "very-high",
      "source": "Test Name 1",
      "source_feed_id": 1000000004,
      "srcip": "107.180.51.15",
      "state": "active",
      "update_id": "2075600",
      "url": "http://aadroid.net/wp-content/plugins/coming-soon/themes/default/images/seedprod-credit.png"
    }
  ]
}
```

#### Lookup URL
  
This action is used to lookup a URL in Anomali ThreatStream

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|url|string|None|False|URL|None|https://example.com|
  
Example input:

```
{
  "url": "https://example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|results|[]result|False|Results returned|None|
  
Example output:

```
{
  "results": [
    {
      "asn": "26496",
      "classification": "private",
      "confidence": "100",
      "country": "US",
      "date_first": "2018-09-06T23:01:26",
      "date_last": "2018-09-06T23:01:26",
      "detail2": "imported by user 1000000012",
      "id": 1000000178,
      "itype": "mal_url",
      "lat": 33.6119,
      "lon": -111.8906,
      "org": "GoDaddy.com, LLC",
      "resource_uri": "/api/v1/intelligence/1000000178/",
      "severity": "very-high",
      "source": "Test Name 1",
      "source_feed_id": 1000000004,
      "srcip": "107.180.51.15",
      "state": "active",
      "update_id": "2075597",
      "url": "http://aadroid.net/wp-includes/js/jquery/jquery.js"
    }
  ]
}
```

#### Submit File
  
This action is used to submit a file to a ThreatStream sandbox

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|classification|string|private|False|Classification of the Sandbox submission, either public or private|["private", "public"]|private|
|detail|string|None|False|A comma-separated list that provides additional details for the indicator. This information is displayed in the Tag column of the ThreatStream UI|None|Credential-Exposure,compromised_email|
|file|file|None|True|File to detonate|None|setup.exe|
|platform|string|None|True|Platform on which the submitted URL or file will be run|["ALL", "ANDROID4.4", "ANDROID5.1", "ANDROID6.0", "MACOSX", "WINDOWSXP", "WINDOWSXPNATIVE", "WINDOWS7", "WINDOWS7NATIVE", "WINDOWS7OFFICE2010", "WINDOWS7OFFICE2013", "WINDOWS10", "WINDOWS10x64"]|WINDOWS7|
|use_premium_sandbox|boolean|None|True|Specify whether the premium sandbox should be used for detonation|None|True|
  
Example input:

```
{
  "classification": "private",
  "detail": "Credential-Exposure,compromised_email",
  "file": "setup.exe",
  "platform": "WINDOWS7",
  "use_premium_sandbox": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|reports|[]report|False|Reports containing submission details|[ { "Details": {}, "ID": 0, "Platform": {}, "Status": "" } ]|
|success|boolean|False|Operation status|True|
  
Example output:

```
{
  "success": true,
  "reports": [
    {
      "status": "/api/v1/submit/101/",
      "detail": "/api/v1/submit/101/report/",
      "id": 101,
      "platform": "WINDOWS7"
    },
    {
      "status": "/api/v1/submit/100/",
      "detail": "/api/v1/submit/100/report/",
      "id": 100,
      "platform": "WINDOWSXP"
    }
  ]
}
```

#### Submit URL
  
This action is used to submit a URL to a ThreatStream sandbox

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|classification|string|private|False|Classification of the sandbox submission, either public or private|["private", "public"]|private|
|detail|string|None|False|A comma-separated list that provides additional details for the indicator. This information is displayed in the tag column of the ThreatStream UI|None|Credential-Exposure,compromised_email|
|platform|string|None|True|Platform on which the submitted URL or file will be run|["ALL", "ANDROID4.4", "ANDROID5.1", "ANDROID6.0", "MACOSX", "WINDOWSXP", "WINDOWSXPNATIVE", "WINDOWS7", "WINDOWS7NATIVE", "WINDOWS7OFFICE2010", "WINDOWS7OFFICE2013", "WINDOWS10", "WINDOWS10x64"]|WINDOWS7|
|url|string|None|True|URL to detonate|None|https://example.com/setup.exe|
|use_premium_sandbox|boolean|None|True|Specify whether the premium sandbox should be used for detonation|None|True|
  
Example input:

```
{
  "classification": "private",
  "detail": "Credential-Exposure,compromised_email",
  "platform": "WINDOWS7",
  "url": "https://example.com/setup.exe",
  "use_premium_sandbox": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|reports|[]report|False|Reports containing submission details|[ { "Details": {}, "ID": 0, "Platform": {}, "Status": "" } ]|
|success|boolean|False|Operation status|True|

Example output:

```
{
  "success": true,
  "reports": [
    {
      "status": "/api/v1/submit/101/",
      "detail": "/api/v1/submit/101/report/",
      "id": 101,
      "platform": "WINDOWS7"
    },
    {
      "status": "/api/v1/submit/100/",
      "detail": "/api/v1/submit/100/report/",
      "id": 100,
      "platform": "WINDOWSXP"
    }
  ]
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**meta**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Limit|integer|None|None|Limit|None|
|Offset|integer|None|None|Offset|None|
|Total Count|integer|None|None|Total Count|None|
  
**result**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ASN|string|None|None|Autonomous system number|None|
|Classification|string|None|None|Classification|None|
|Confidence|string|None|None|Confidence level|None|
|Country|string|None|None|Country|None|
|Date First|string|None|None|Date first|None|
|Date Last|string|None|None|Date last|None|
|Details|string|None|None|Details|None|
|Domain|string|None|None|Domain|None|
|Email|string|None|None|Email|None|
|ID|integer|None|None|ID|None|
|Itype|string|None|None|Itype|None|
|Latitude|number|None|None|Latitude|None|
|Longitude|number|None|None|Longitude|None|
|MD5|string|None|None|MD5 Hash|None|
|Organization|string|None|None|Organization|None|
|Resource URI|string|None|None|Resource URI|None|
|Severity|string|None|None|Severity|None|
|Source|string|None|None|Source|None|
|Source Feed ID|integer|None|None|Source Feed ID|None|
|Source IP|string|None|None|Source IP|None|
|State|string|None|None|State|None|
|Update ID|string|None|None|Update ID|None|
|URL|string|None|None|URL|None|
  
**observable_settings**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Classification|string|private|True|Classification of the observable|None|
|Confidence|integer|None|None|Confidence value assigned to the observable. Confidence score can range from 0-100, in increasing order of confidence|None|
|Domain Mapping|string|None|False|Indicator type to assign if a specific type is not associated with an observable|None|
|Email Mapping|string|None|False|Indicator type to assign if a specific type is not associated with an observable|None|
|Expiration Time Stamp|date|None|None|Time stamp of when intelligence will expire on ThreatStream|None|
|IP Mapping|string|None|False|Indicator type to assign if a specific type is not associated with an observable|None|
|MD5 Mapping|string|None|False|Indicator type to assign if a specific type is not associated with an observable|None|
|Notes|[]string|None|None|Additional details for the observable. This information is displayed in the Tags column of the ThreatStream UI e.g ['note1', 'note2', 'note3']|None|
|Severity|string||None|Severity you want to assign to the observable when it is imported|None|
|Source Confidence Weight|integer|None|None|Specifies the ratio between the amount of the source confidence of each observable and the ThreatStream confidence|None|
|Threat Type|string|None|False|Type of threat associated with the imported observables|None|
|Trusted Circles|[]integer|None|None|ID of the trusted circle to which this threat data should be imported. If you want to import the threat data to multiple trusted circles, enter the list of comma-separated IDs e.g [1,2,3]|None|
|URL Mapping|string|None|False|Indicator type to assign if a specific type is not associated with an observable|None|
  
**import_observable_response**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Import Session ID|string|None|None|ID for import session|None|
|Job ID|string|None|None|Job ID|None|
|Success|boolean|None|None|If import was successful|None|
  
**report**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Details|string|None|None|None|None|
|ID|integer|None|None|Submission ID|None|
|Platform|string|None|None|Platform on which the submitted URL or file will be run|None|
|Status|string|None|None|None|None|
  
**info**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Category|string|None|True|Category|None|
|Confidence|int|None|True|Confidence|None|
|Duration|int|None|True|Duration|None|
|Ended|string|None|True|Ended|None|
|Is Malicious|boolean|None|True|Is malicious|None|
|Is Suspicious|boolean|None|True|Is suspicious|None|
|Is Unknown|boolean|None|True|Is unknown|None|
|Started|string|None|True|Started|None|
  
**sandbox_report**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Domains|[]string|None|True|Domains|None|
|Info|info|None|True|Info|None|
|Screenshots|[]string|None|True|Screenshots|None|
|Signatures|[]object|None|True|Signatures|None|


## Troubleshooting

If you're unable to import data without approval, the Anomali user configured in InsightConnect will need to have `approver` permissions.

# Version History

* 3.1.2 - Update SDK to newest version
* 3.1.1 - Mask API key from URLs in log output
* 3.1.0 - Add new actions Submit File, Submit URL and Get Sandbox Report
* 3.0.2 - New spec and help.md format for the Extension Library
* 3.0.1 - Update actions to use SSL Verify from connection settings
* 3.0.0 - Add new action Get Observables | Rename action Add Approval Indicator to Import Observable | Add connection test
* 2.0.0 - Support optional server SSL/TLS certificate validation
* 1.1.0 - New action Add Approval Indicator
* 1.0.0 - Initial plugin

# Links

* [Anomali](https://www.anomali.com/)

## References

* [Anomali ThreatStream](https://www.ui.threatstream.com/)
