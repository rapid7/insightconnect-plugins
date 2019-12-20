# Description

The [URLScan](https://urlscan.io/) plugin uses URLScan to analyze URLs for malicious indicators.

This plugin utilizes the [URLScan API](https://urlscan.io/about-api/) to search for URLs and retrieve reports
on potential malicous indicators.

# Key Features

* Launch a scan on a URL
* Retrieve reports on a URL

# Requirements

* A URLScan API key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|False|urlscan API key. Not required for the search action|None|

## Technical Details

### Actions

#### Search

This action is used to search urlscan.io.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|q|string|None|True|The query term (ElasticSearch simple query string) e.g domain:urlscan.io, default is *|None|
|sort|string|_score|True|Sorting, specificied via $sort_field:$sort_order|None|
|size|integer|100|True|Number of results returned|None|
|offset|integer|0|True|Offset of first result (for paginating)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]results|False|UrlScan.io Results|
|total|integer|False|Total number of results returned|

Example output:

```
[
   {
      "_id":"9b135a8b-d6ba-4d39-a93c-de0cd4378dcc",
      "page":{
         "asn":"AS24940",
         "asnname":"HETZNER-AS, DE",
         "city":"",
         "country":"DE",
         "domain":"urlscan.io",
         "ip":"148.251.45.170",
         "ptr":"urlscan.io",
         "server":"nginx",
         "url":"https://urlscan.io/"
      },
      "result":"https://urlscan.io/api/v1/result/9b135a8b-d6ba-4d39-a93c-de0cd4378dcc",
      "stats":{
         "consoleMsgs":0,
         "dataLength":835633,
         "encodedDataLength":296287,
         "requests":30,
         "uniqIPs":6
      },
      "task":{
         "method":"api",
         "source":"api",
         "time":"2019-01-03T16:00:28.529Z",
         "url":"http://urlscan.io",
         "visibility":"public"
      },
      "uniq_countries":2
   }
]
```

#### Submit URL for Scan

This action is used to submit a URL to generate a scan report that can be retrieved later.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|The URL to scan|None|
|public|boolean|False|True|Set to false for a private scan|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan_id|string|True|UUID of the scan to query later|

Example output:

```
{
  "scan_id": "557a7923-c597-4a84-982c-665ece8fa6ed"}
}
```

#### Get Scan Results

This action is used to get the results of a scan.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|scan_id|string|None|True|UUID of the scan to retrieve|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan_results|scan_results|True|Results of the scan report|

Example output:

```
{
    "scan_results": {
        "requests": [
            {
                "request": {
                    "requestId": "47A4C275E4F9888784CC56FB194AC950",
                    "loaderId": "47A4C275E4F9888784CC56FB194AC950",
                    "documentURL": "https://www.google.com/?gws_rd=ssl",
                    "request": {
                        "url": "https://www.google.com/?gws_rd=ssl",
                        "method": "GET",
                        "headers": {
                            "Upgrade-Insecure-Requests": "1",
                            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
                        },
                        "mixedContentType": "none",
                        "initialPriority": "VeryHigh",
                        "referrerPolicy": "no-referrer-when-downgrade"
                    },
                    "timestamp": 30579913.395083,
                    "wallTime": 1546278138.193554,
                    "initiator": {
                        "type": "other"
                    },
                    "redirectResponse": {
                        "url": "http://www.google.com/",
                        "status": 302,
                        "statusText": "Found",
                        "headers": {
                            "Location": "https://www.google.com/?gws_rd=ssl",
                            "Cache-Control": "private",
                            "Content-Type": "text/html; charset=UTF-8",
                            "P3P": "CP=\"This is not a P3P policy! See g.co/p3phelp for more info.\"",
                            "Date": "Mon, 31 Dec 2018 17:42:18 GMT",
                            "Server": "gws",
                            "Content-Length": "231",
                            "X-XSS-Protection": "1; mode=block",
                            "X-Frame-Options": "SAMEORIGIN",
                            "Set-Cookie": "1P_JAR=2018-12-31-17; expires=Wed, 30-Jan-2019 17:42:18 GMT; path=/; domain=.google.com\nNID=152=LSC4Vcy981xZ6F9BrZAaF97wP1t8VKPLhPkBHnU5wG7ZfQDpurZphSUPpw4T3ErINvKmLpFIxrCfyzhtXHBDhlrJ5G412FYdCaEiSet37hsN5YmBbfUhBj5UjmzdSLwOLBY_T1tYis2rd-hTr12etNJ78s5N5NU7_MeNg408s0Y; expires=Tue, 02-Jul-2019 17:42:18 GMT; path=/; domain=.google.com; HttpOnly\nCONSENT=WP.2752ea; expires=Fri, 01-Jan-2038 00:00:00 GMT; path=/; domain=.google.com"
                        },
                        "mimeType": "text/html",
                        "requestHeaders": {
                            "Host": "www.google.com",
                            "Connection": "keep-alive",
                            "Pragma": "no-cache",
                            "Cache-Control": "no-cache",
                            "Upgrade-Insecure-Requests": "1",
                            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                            "Accept-Encoding": "gzip, deflate"
                        },
                        "remoteIPAddress": "[2a00:1450:4001:820::2004]",
                        "remotePort": 80,
                        "encodedDataLength": 803,
                        "timing": {
                            "requestTime": 30579913.345846,
                            "proxyStart": -1,
                            "proxyEnd": -1,
                            "dnsStart": -1,
                            "dnsEnd": -1,
                            "connectStart": -1,
                            "connectEnd": -1,
                            "sslStart": -1,
                            "sslEnd": -1,
                            "workerStart": -1,
                            "workerReady": -1,
                            "sendStart": 0.519,
                            "sendEnd": 0.547,
                            "pushStart": 0,
                            "pushEnd": 0,
                            "receiveHeadersEnd": 48.809
                        },
                        "protocol": "http/1.1",
                        "securityState": "neutral"
                    },
                    "type": "Document",
                    "frameId": "1DEBC07916E13CAB920D1FF70099D072",
                    "hasUserGesture": false
                }
            }
        ],
        "cookies": [
            {
                "name": "NID",
                "value": "152=SXZkTJ2B0OtwUgtuhshFOwo6pZpdK_wT392bPKcfDvT8f6F3rAUFzdUHOZZZHUliugUP9ObePB8GoXkOtP7sPQMEupWyL0y5WrUIrBKlaXP3ZIpwDxhQuz9XqTJGKtz56Z9zzDFX5wcfepb5dKacMCtpQAdSrMPabeC2Idu538Y",
                "domain": ".google.com",
                "path": "/",
                "expires": 1562089338.309606,
                "size": 178,
                "httpOnly": true,
                "secure": false,
                "session": false
            }
        ],
        "console": [],
        "links": [
            {
                "href": "https://store.google.com/?utm_source=hp_header&utm_medium=google_oo&utm_campaign=GS100042",
                "text": "Store"
            }
        ],
        "timing": {
            "beginNavigation": "2018-12-31T17:42:18.143Z",
            "frameStartedLoading": "2018-12-31T17:42:18.312Z",
            "frameNavigated": "2018-12-31T17:42:18.314Z",
            "domContentEventFired": "2018-12-31T17:42:18.425Z",
            "loadEventFired": "2018-12-31T17:42:18.795Z",
            "frameStoppedLoading": "2018-12-31T17:42:18.795Z"
        },
        "globals": [
            {
                "prop": "onselectstart",
                "type": "object"
            },
            {
                "prop": "onselectionchange",
                "type": "object"
            }
        ],
        "screenshotURL": "google.com"
    }
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 2.1.3 - New spec and help.md format for the Hub
* 2.1.2 - Set User-Agent string to Rapid7 InsightConnect | Update to use the `komand/python-3-37-slim-plugin:3` Docker image to reduce plugin size | Run plugin as least privileged user | Improve error handling and logging | Fix issue in Submit URL for Scan action where improper POST body was sent
* 2.1.1 - Add error messaging to Get Scan Results action to provide assistance for unavailable scan results | Update to Python 3.7 Slim SDK (plugin size reduction)
* 2.1.0 - Added ScreenshotURL to get scan results output
* 2.0.0 - Fixed issue where output of Get Scan Results did not match API output | Update connection input to secret key instead of token | Updates to help
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Urlscan.io](https://urlscan.io/)
* [Urlscan API](https://urlscan.io/about-api/)

