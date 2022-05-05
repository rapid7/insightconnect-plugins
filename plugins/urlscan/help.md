# Description

The [URLScan](https://urlscan.io/) plugin uses URLScan to analyze URLs for malicious indicators.

This plugin utilizes the [URLScan API](https://urlscan.io/about-api/) to search for URLs and retrieve reports
on potential malicous indicators.

# Key Features

* Launch a scan on a URL
* Retrieve reports on a URL

# Requirements

* A URLScan API key

# Supported Product Versions

* urlscan.io API v1

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|False|urlscan API key. Not required for the search action|None|{"secretKey": "381cd93b-1946-9c73-1946-c916075eb9a3"}|

Example input:

```
{
  "api_key": {
    "secretKey": “381cd93b-1946-9c73-1946-c916075eb9a3"
  }
}
```

## Technical Details

### Actions

#### Search

This action is used to search urlscan.io.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|input_type|string|Custom|True|Type of provided query. Set 'custom' to provide custom query, set 'url' to search information about provided URL, set 'domain' to search information about provided domain|['URL', 'Domain', 'Custom']|Domain|
|q|string|example.com|True|The query term (ElasticSearch simple query string), default is *. If 'Input Type' input is set to URL or domain, provide only the URL or domain|None|example.com|
|sort|string|_score|True|Sorting, specificied via $sort_field:$sort_order|None|_score|

Example input:

```
{
  "input_type": "Domain",
  "q": "example.com",
  "sort": "_score"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|has_more|boolean|False|Whether or not the source has more entities|
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

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|public|boolean|False|True|Set to false for a private scan|None|True|
|url|string|None|True|The URL to scan|None|http://www.example.com|

Example input:

```
{
  "public": true,
  "url": "http://www.example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan_id|string|True|UUID of the scan to query later|
|was_scan_skipped|boolean|True|If true scan was skipped, false if scan was executed|

Example output:

```
{
  "was_scan_skipped": false,
  "scan_id": "557a7923-c597-4a84-982c-665ece8fa6ed"}
}
```

#### Get Scan Results

This action is used to get the results of a scan.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|scan_id|string|None|True|UUID of the scan to retrieve|None|b1f3dab-ad7e-e2790803d6d0-76wFGijr|

Example input:

```
{
  "scan_id": "b1f3dab-ad7e-e2790803d6d0-76wFGijr"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|lists|object|True|Results of the lists|
|meta|object|True|Results of the meta|
|page|object|True|Results of the page|
|scan_results|scan_results|True|Results of the scan report|
|stats|object|True|Results of the stats|
|task|object|True|Results of the task|
|verdicts|object|True|Results of the verdicts|

Example output:

```
{
  "body": {
    "log": "rapid7/urlscan.io:2.1.6. Step name: get_scan_results\n",
    "status": "ok",
    "meta": {},
    "output": {
      "scan_results": {
        "requests": [
          {
            "request": {
              "requestId": "386C002BED228B39A8D98E70118F9AD1",
              "loaderId": "386C002BED228B39A8D98E70118F9AD1",
              "documentURL": "http://mapleleafjobs.net/lp/b/?q=&l=Galena+Park%2C+TX&sflp=T1UW9baml8b-33j6b-21&show=true&rdt=a&osd=2020-05-27+02%3A38",
              "request": {
                "url": "http://mapleleafjobs.net/lp/b/?q=&l=Galena+Park%2C+TX&sflp=T1UW9baml8b-33j6b-21&show=true&rdt=a&osd=2020-05-27+02%3A38",
                "method": "GET",
                "headers": {
                  "Upgrade-Insecure-Requests": "1",
                  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
                },
                "mixedContentType": "none",
                "initialPriority": "VeryHigh",
                "referrerPolicy": "no-referrer-when-downgrade"
              },
              "timestamp": 2592035.057441,
              "wallTime": 1590591796.704884,
              "initiator": {
                "type": "other"
              },
              "redirectResponse": {
                "url": "https://rd.mapleleafjobs.net/a/?x=T1UW9baml8b-33j6b-21",
                "status": 302,
                "statusText": "",
                "headers": {
                  "status": "302",
                  "date": "Wed, 27 May 2020 15:03:16 GMT",
                  "content-length": "0",
                  "location": "http://mapleleafjobs.net/lp/b/?q=&l=Galena+Park%2C+TX&sflp=T1UW9baml8b-33j6b-21&show=true&rdt=a&osd=2020-05-27+02%3A38",
                  "set-cookie": "AWSALB=Ekqsts7yKPZ5T6KoJbMkOruoWEVlTbnEbJS0Tk+SR0DBUAx3XeNy+oXC7h/2KpknDvMvRRhQmUMB69pFPpdiJFwk2kAFlp9ITucBg+fb83rlO7mqOlEkqGu7fhxM; Expires=Wed, 03 Jun 2020 15:03:16 GMT; Path=/\nAWSALBCORS=Ekqsts7yKPZ5T6KoJbMkOruoWEVlTbnEbJS0Tk+SR0DBUAx3XeNy+oXC7h/2KpknDvMvRRhQmUMB69pFPpdiJFwk2kAFlp9ITucBg+fb83rlO7mqOlEkqGu7fhxM; Expires=Wed, 03 Jun 2020 15:03:16 GMT; Path=/; SameSite=None; Secure",
                  "server": "nginx/1.14.1",
                  "referer": ""
                },
                "mimeType": "",
                "requestHeaders": {
                  ":method": "GET",
                  ":authority": "rd.mapleleafjobs.net",
                  ":scheme": "https",
                  ":path": "/a/?x=T1UW9baml8b-33j6b-21",
                  "pragma": "no-cache",
                  "cache-control": "no-cache",
                  "upgrade-insecure-requests": "1",
                  "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                  "sec-fetch-site": "none",
                  "sec-fetch-mode": "navigate",
                  "sec-fetch-user": "?1",
                  "sec-fetch-dest": "document",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "en-US"
                },
                "remoteIPAddress": "52.54.3.79",
                "remotePort": 443,
                "fromPrefetchCache": false,
                "encodedDataLength": 487,
                "timing": {
                  "requestTime": 2592034.929732,
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
                  "sendStart": 1.133,
                  "sendEnd": 1.258,
                  "pushStart": 0,
                  "pushEnd": 0,
                  "receiveHeadersEnd": 127.148
                },
                "protocol": "h2",
                "securityState": "secure",
                "securityDetails": {
                  "protocol": "TLS 1.2",
                  "keyExchange": "ECDHE_RSA",
                  "keyExchangeGroup": "P-256",
                  "cipher": "AES_128_GCM",
                  "certificateId": 0,
                  "subjectName": "adaptationjobs.com",
                  "sanList": [
                    "adaptationjobs.com"
                  ],
                  "issuer": "Amazon",
                  "validFrom": 1579478400,
                  "validTo": 1613822400,
                  "signedCertificateTimestampList": [],
                  "certificateTransparencyCompliance": "unknown"
                }
              },
              "type": "Document",
              "frameId": "0F98044EF86BF67BBDB7D3C690630EBB",
              "hasUserGesture": false
            },
            "requests": [
              {
                "requestId": "386C002BED228B39A8D98E70118F9AD1",
                "loaderId": "386C002BED228B39A8D98E70118F9AD1",
                "documentURL": "https://s.mapleleafjobs.net/f/a/1_Qyh4s9oyxnFuau29s_HA~~/AAF10QA~/RgRgsQBWP0Q2aHR0cHM6Ly9yZC5tYXBsZWxlYWZqb2JzLm5ldC9hLz94PVQxVVc5YmFtbDhiLTMzajZiLTIxVwNzcGNCCgAoVnvOXtJ8SVxSHWFtYmVyLm1hbGxldHRAcGFjaWZpY2xpZmUuY29tWAQAAABM",
                "request": {
                  "url": "https://s.mapleleafjobs.net/f/a/1_Qyh4s9oyxnFuau29s_HA~~/AAF10QA~/RgRgsQBWP0Q2aHR0cHM6Ly9yZC5tYXBsZWxlYWZqb2JzLm5ldC9hLz94PVQxVVc5YmFtbDhiLTMzajZiLTIxVwNzcGNCCgAoVnvOXtJ8SVxSHWFtYmVyLm1hbGxldHRAcGFjaWZpY2xpZmUuY29tWAQAAABM",
                  "method": "GET",
                  "headers": {
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
                  },
                  "mixedContentType": "none",
                  "initialPriority": "VeryHigh",
                  "referrerPolicy": "no-referrer-when-downgrade"
                },
                "timestamp": 2592034.131691,
                "wallTime": 1590591795.779065,
                "initiator": {
                  "type": "other"
                },
                "type": "Document",
                "frameId": "0F98044EF86BF67BBDB7D3C690630EBB",
                "hasUserGesture": false
              }
            ],
            "response": {
              "encodedDataLength": 3235,
              "dataLength": 6028,
              "requestId": "386C002BED228B39A8D98E70118F9AD1",
              "type": "Document",
              "response": {
                "url": "http://mapleleafjobs.net/lp/b/?q=&l=Galena+Park%2C+TX&sflp=T1UW9baml8b-33j6b-21&show=true&rdt=a&osd=2020-05-27+02%3A38",
                "status": 200,
                "statusText": "",
                "headers": {
                  "Date": "Wed, 27 May 2020 15:03:16 GMT",
                  "Content-Type": "text/html;charset=ISO-8859-1",
                  "Transfer-Encoding": "chunked",
                  "Connection": "keep-alive",
                  "Set-Cookie": "AWSALB=Q9B2lVvJ+xsnpojaDQwOkSVdvm6kXoU7mAtXWMBuYazy5mEEt0ukwUdM5Yl36qVcJe8Lmiy+i3nR60ln+GPyJGdB0YuI1b9qFBQo5j2cjZrC6XuxFelHCBUtrcrc; Expires=Wed, 03 Jun 2020 15:03:16 GMT; Path=/\nAWSALBCORS=Q9B2lVvJ+xsnpojaDQwOkSVdvm6kXoU7mAtXWMBuYazy5mEEt0ukwUdM5Yl36qVcJe8Lmiy+i3nR60ln+GPyJGdB0YuI1b9qFBQo5j2cjZrC6XuxFelHCBUtrcrc; Expires=Wed, 03 Jun 2020 15:03:16 GMT; Path=/; SameSite=None\nJSESSIONID=C3242C772E5033900D23D3E08483D144; Path=/; HttpOnly",
                  "Server": "nginx/1.14.1",
                  "X-Content-Type-Options": "nosniff",
                  "X-XSS-Protection": "1; mode=block",
                  "Cache-Control": "no-cache, no-store, max-age=0, must-revalidate",
                  "Pragma": "no-cache",
                  "Expires": "0",
                  "X-Frame-Options": "DENY",
                  "Content-Language": "en-US",
                  "Content-Encoding": "gzip"
                },
                "mimeType": "text/html",
                "requestHeaders": {
                  "Host": "mapleleafjobs.net",
                  "Connection": "keep-alive",
                  "Pragma": "no-cache",
                  "Cache-Control": "no-cache",
                  "Upgrade-Insecure-Requests": "1",
                  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                  "Accept-Encoding": "gzip, deflate",
                  "Accept-Language": "en-US"
                },
                "remoteIPAddress": "18.214.176.230",
                "remotePort": 80,
                "fromPrefetchCache": false,
                "encodedDataLength": 881,
                "timing": {
                  "requestTime": 2592035.057688,
                  "proxyStart": -1,
                  "proxyEnd": -1,
                  "dnsStart": 0.406,
                  "dnsEnd": 12.838,
                  "connectStart": 12.838,
                  "connectEnd": 30.397,
                  "sslStart": -1,
                  "sslEnd": -1,
                  "workerStart": -1,
                  "workerReady": -1,
                  "sendStart": 30.437,
                  "sendEnd": 30.486,
                  "pushStart": 0,
                  "pushEnd": 0,
                  "receiveHeadersEnd": 246.646
                },
                "protocol": "http/1.1",
                "securityState": "insecure",
                "securityHeaders": [
                  {
                    "name": "X-Content-Type-Options",
                    "value": "nosniff"
                  },
                  {
                    "name": "X-Frame-Options",
                    "value": "DENY"
                  },
                  {
                    "name": "X-Xss-Protection",
                    "value": "1; mode=block"
                  }
                ]
              },
              "hash": "35b24ad03e4473bcb53e10c8d38e9821ee25f0160d4160bbce83c2bf7d2af58e",
              "size": 6028,
              "asn": {
                "ip": "18.214.176.230",
                "asn": "14618",
                "country": "US",
                "registrar": "arin",
                "date": "2005-11-04",
                "description": "AMAZON-AES, US",
                "route": "18.208.0.0/13",
                "name": "AMAZON-AES"
              },
              "geoip": {
                "range": [
                  316055552,
                  316063743
                ],
                "country": "US",
                "region": "VA",
                "eu": "0",
                "timezone": "America/New_York",
                "city": "Ashburn",
                "ll": [
                  39.0481,
                  -77.4728
                ],
                "metro": 511,
                "area": 1000,
                "country_name": "United States"
              },
              "rdns": {
                "ip": "18.214.176.230",
                "ptr": "ec2-18-214-176-230.compute-1.amazonaws.com"
              },
              "hashmatches": []
            }
          }
        ],
        "cookies": [
          {
            "name": "gdpr_status",
            "value": "1",
            "domain": ".media.net",
            "path": "/",
            "expires": 1606575798.655975,
            "size": 12,
            "httpOnly": false,
            "secure": true,
            "session": false,
            "sameSite": "None",
            "priority": "Medium"
          }
        ],
        "console": [],
        "links": [
          {
            "href": "http://web.mapleleafjobs.net/web?q=eyJzb3VyY2UiOiJMZWFkIDUgbWVkaWEgQXBpIiwidXJsIjoiaHR0cHM6Ly9hcGkubDVzcnYubmV0L2pvYl9zZWFyY2gvYXBpL2RpcmVjdF9lbWFpbC9nZXRfam9iLnNydj90b2tlblx1MDAzZG5NWXBxNTZabGxzbiUyRnRvWnY4MU52UVZwJTJCNktvQlZJTGppWDNDRDBmTDNtb242YzRtblFsNTJFNVJ5MTRpNnB0b1p5RlRUWDglMkI3anZPejczR1FnNko2dFU5QkVxOERIemtmYklEQ0RwMW5yVCUyRjNnTW9nWFlSR0FHWXhMNllQMmJ5UXVCT1NnN1pxMG5pUHV5JTJCUzkwaDVWZVFMdmVTQ1FlSVpNSmtTMG5udnBPN3F4NFpKdXI5a1dPU2d1eE1GODdyQlNSWTFwTk1Dd2wxaHUlMkZrTHFpNVZ4NElHRWJyZzM1SUhTWlZTWU9JMVFsWU5ubUpvMFolMkZBakRVU2xwQm85N0tiTTJCdXZlcVpvdmE5TXNPdGc4MXlpS1clMkZ5bkxBblZ5S1RqbnFhcjdBVTN3cVhxb1dna01iRHU5SjVkWnNHZTBRWUtwOTQ0TmVvWnQ3NnZPSHg5Sk41b0swQXBDNDVsYlI4Tm5NNWdWTGxheGNBOUFaRlB5NUhoOXM0STlnWkoiLCJjcGMiOiIwLjEiLCJnY3BjIjoiMC4xMCIsInppcGNvZGUiOiI3NzU0NyIsInNvdXJjZU5hbWUiOiJMZWFkIDUgbWVkaWEgQXBpIiwiY2l0eSI6IkdhbGVuYSBQYXJrIiwic3RhdGUiOiJUWCIsImNvbXBhbnkiOiJBU1NVUkFOQ0UgSW5kZXBlbmRlbnQgQWdlbnRzIiwicmVmZXJlbmNlIjoiIiwicmFkaXVzIjoiMzAiLCJscENsaWNrVHlwZSI6IlNGTFAiLCJscENhY2hlS2V5IjoiVDFVVzliYW1sOGItMzNqNmItMjEiLCJjb3VudHJ5IjoiVVMiLCJpc1dlYlRlbmFudCI6ZmFsc2V9",
            "text": "Click\n\t\t\t\t\t\tHere"
          }
        ],
        "timing": {
          "beginNavigation": "2020-05-27T15:03:15.778Z",
          "frameStartedLoading": "2020-05-27T15:03:19.089Z",
          "frameNavigated": "2020-05-27T15:03:19.089Z",
          "frameStoppedLoading": "2020-05-27T15:03:19.089Z",
          "loadEventFired": "2020-05-27T15:03:18.676Z",
          "domContentEventFired": "2020-05-27T15:03:18.677Z"
        },
        "globals": [
          {
            "prop": "onformdata",
            "type": "object"
          }
        ],
        "screenshotURL": "https://urlscan.io/screenshots/105d1aac-ccc0-4393-b421-da95bd4faafd.png"
      },
      "task": {
        "uuid": "105d1aac-ccc0-4393-b421-da95bd4faafd",
        "time": "2020-05-27T15:03:15.638Z",
        "url": "https://s.mapleleafjobs.net/f/a/1_Qyh4s9oyxnFuau29s_HA~~/AAF10QA~/RgRgsQBWP0Q2aHR0cHM6Ly9yZC5tYXBsZWxlYWZqb2JzLm5ldC9hLz94PVQxVVc5YmFtbDhiLTMzajZiLTIxVwNzcGNCCgAoVnvOXtJ8SVxSHWFtYmVyLm1hbGxldHRAcGFjaWZpY2xpZmUuY29tWAQAAABM",
        "visibility": "public",
        "options": {
          "useragent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        },
        "method": "api",
        "source": "db0274c6",
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "reportURL": "https://urlscan.io/result/105d1aac-ccc0-4393-b421-da95bd4faafd/",
        "screenshotURL": "https://urlscan.io/screenshots/105d1aac-ccc0-4393-b421-da95bd4faafd.png",
        "domURL": "https://urlscan.io/dom/105d1aac-ccc0-4393-b421-da95bd4faafd/"
      },
      "page": {
        "url": "http://mapleleafjobs.net/lp/b/?q=&l=Galena+Park%2C+TX&sflp=T1UW9baml8b-33j6b-21&show=true&rdt=a&osd=2020-05-27+02%3A38",
        "domain": "mapleleafjobs.net",
        "country": "US",
        "city": "Ashburn",
        "server": "nginx/1.14.1",
        "ip": "18.214.176.230",
        "ptr": "ec2-18-214-176-230.compute-1.amazonaws.com",
        "asn": "AS14618",
        "asnname": "AMAZON-AES, US"
      },
      "lists": {
        "ips": [
          "2600:9000:2047:a800:5:a48e:90c0:93a1"
        ],
        "countries": [
          "US"
        ],
        "asns": [
          "16509"
        ],
        "domains": [
          "contextual.media.net"
        ],
        "servers": [
          "Apache"
        ],
        "urls": [
          "https://lg3.media.net/bqi.php?lf=3&&gdpr=1&prid=8PR634MLX&vi=1590591798400790261&cid=8CUI30N5I&crid=445834682&ugd=4&cc=FR&sc=IDF&requrl=http%3A%2F%2Fmapleleafjobs.net%2Flp%2Fb%2F%3F%26zip%3DGalena%2520Park%2C%2520TX%26gender%3Dm%26age%3D23%26query%3D%2520Jobs%26q%3D%26l%3DGalena%2BPark%252C%2BTX%26sflp%3DT1UW9baml8b-33j6b-21%26show%3Dtrue%26rdt%3Da%26osd%3D2020-05-27%2B02%253A38%23mnetcrid%3D445834682%23&pid=8PO16L3O6&hvsid=00001590591798609013824209921126&cme=dkn17oQksqrwS3B2Uq3A3I9awCHcU6Q6OxcmRhxLS2imvVRtHMIUqI61H2P3nucJNiKLTkIxGadbd0GHJP4HwsFR5rXfqlR5G0vQ8M7jvMIUPDwWAyRumws5iNDIv-CcnmFXSeUlKDY%3D%7C%7CNDHRnZ9Gz3KXlI-i9OnZqQ%3D%3D%7CWN0fyNFfzAitqWVgiJ20xYGRjxegOsKM7wykmvobgQY%3D%7CN7fu2vKt8_s%3D%7CFfdm3T7X3xzrTID4QruTSsIGuh-3HG4jE4jDzktVlaWlKSILyaJ5XTp5-Gc2tjZN8QxeIDAMEGl2zq-bS6MvTkl8i3YUNnp2PjbuoHVoNhzcaWSunKgO5ScbWL2GO7tEqGjli9O_KGLN6CWNp2fTgwfaoLOyKAi4M69UWFwt5HzWiGsnmUgDVi-KCWno6u_DVFb0LPpcoE2PGowRb1oy2qAV8HwhLYV6Q54jeVjPD5E%3D%7CsRBSg3CPSiQ%3D%7C&abpl=2&l2wsip=2886781338&l2ch=0&dytm=1590591798596&l3l=%7B%7D&l3d=%7B%7D&vgd_isiolc=1&vgd_uspa=0&kbbq=%26sde%3D1%26adepth%3D1%26ddepth%3D1&tdAdd[]=%7C%40%7Csde%3D1%7C%40%7Cadepth%3D1%7C%40%7Cddepth%3D1%7C%40%7Cfsap%3D0&vgd_sc=IDF&verid=3111299&upk=1590591798.11857&sttm=1590591798350&l1ch=1&vgd_l1rakh=1590591798116212157&startTime=1590591798342&npgv=1"
        ],
        "linkDomains": [
          "web.mapleleafjobs.net"
        ],
        "certificates": [
          {
            "subjectName": "*.bootstrapcdn.com",
            "issuer": "Sectigo RSA Domain Validation Secure Server CA",
            "validFrom": 1568419200,
            "validTo": 1602633599
          }
        ],
        "hashes": [
          "35b24ad03e4473bcb53e10c8d38e9821ee25f0160d4160bbce83c2bf7d2af58e"
        ]
      },
      "meta": {
        "processors": {
          "geoip": {
            "state": "done",
            "data": [
              {
                "ip": "18.214.176.230",
                "geoip": {
                  "range": [
                    316055552,
                    316063743
                  ],
                  "country": "US",
                  "region": "VA",
                  "eu": "0",
                  "timezone": "America/New_York",
                  "city": "Ashburn",
                  "ll": [
                    39.0481,
                    -77.4728
                  ],
                  "metro": 511,
                  "area": 1000,
                  "country_name": "United States"
                }
              }
            ]
          },
          "wappa": {
            "state": "done",
            "data": [
              {
                "app": "Bootstrap",
                "confidence": [
                  {
                    "pattern": "html /<link[^>]+?href=\"[^\"]*bootstrap(?:\\.min)?\\.css/i",
                    "confidence": 100
                  },
                  {
                    "pattern": "script /(?:\\/([\\d.]+))?(?:\\/js)?\\/bootstrap(?:\\.min)?\\.js/i",
                    "confidence": 100
                  }
                ],
                "confidenceTotal": 100,
                "version": "3.4.0",
                "icon": "Bootstrap.png",
                "website": "https://getbootstrap.com",
                "categories": [
                  {
                    "name": "Web Frameworks",
                    "priority": 7
                  }
                ]
              }
            ]
          },
          "rdns": {
            "state": "done",
            "data": [
              {
                "ip": "18.214.176.230",
                "ptr": "ec2-18-214-176-230.compute-1.amazonaws.com"
              }
            ]
          },
          "asn": {
            "state": "done",
            "data": [
              {
                "ip": "18.214.176.230",
                "asn": "14618",
                "country": "US",
                "registrar": "arin",
                "date": "2005-11-04",
                "description": "AMAZON-AES, US",
                "route": "18.208.0.0/13",
                "name": "AMAZON-AES"
              }
            ]
          },
          "done": {
            "state": "done",
            "data": {
              "state": "done"
            }
          }
        }
      },
      "stats": {
        "resourceStats": [
          {
            "count": 20,
            "size": 1237331,
            "encodedSize": 403802,
            "latency": 0,
            "countries": [
              "DE",
              "US",
              "NL"
            ],
            "ips": [
              "[2a00:1450:4001:809::200a]"
            ],
            "type": "Script",
            "compression": "3.1",
            "percentage": null
          }
        ],
        "protocolStats": [
          {
            "count": 39,
            "size": 1583859,
            "encodedSize": 628016,
            "ips": [
              "[2001:4de0:ac19::1:b:2a]"
            ],
            "countries": [
              "NL"
            ],
            "securityState": {},
            "protocol": "h2"
          }
        ],
        "tlsStats": [
          {
            "count": 40,
            "size": 1604209,
            "encodedSize": 648724,
            "ips": [
              "[2001:4de0:ac19::1:b:2a]"
            ],
            "countries": [
              "NL",
              "DE",
              "US"
            ],
            "protocols": {
              "TLS 1.3 /  / AES_128_GCM": 14,
              "TLS 1.2 / ECDHE_RSA / AES_128_GCM": 2,
              "TLS 1.3 /  / AES_256_GCM": 24
            },
            "securityState": "secure"
          }
        ],
        "serverStats": [
          {
            "count": 24,
            "size": 753731,
            "encodedSize": 366600,
            "ips": [
              "72.247.224.27"
            ],
            "countries": [
              "US"
            ],
            "server": "Apache"
          }
        ],
        "domainStats": [
          {
            "count": 18,
            "ips": [
              "72.247.224.27"
            ],
            "domain": "contextual.media.net",
            "size": 753601,
            "encodedSize": 365808,
            "countries": [
              "US"
            ],
            "index": 20,
            "initiators": [
              "mapleleafjobs.net",
              "contextual.media.net"
            ],
            "redirects": 0
          }
        ],
        "regDomainStats": [
          {
            "count": 24,
            "ips": [
              "72.247.224.27"
            ],
            "regDomain": "media.net",
            "size": 753731,
            "encodedSize": 366600,
            "countries": [],
            "index": 20,
            "subDomains": [],
            "redirects": 0
          }
        ],
        "secureRequests": 40,
        "securePercentage": 87,
        "IPv6Percentage": 60,
        "uniqCountries": 3,
        "totalLinks": 1,
        "malicious": 0,
        "adBlocked": 0,
        "ipStats": [
          {
            "requests": 1,
            "domains": [
              "s.mapleleafjobs.net"
            ],
            "ip": "2600:9000:2047:a800:5:a48e:90c0:93a1",
            "asn": {
              "ip": "2600:9000:2047:a800:5:a48e:90c0:93a1",
              "asn": "16509",
              "country": "US",
              "registrar": "arin",
              "date": "2000-05-04",
              "description": "AMAZON-02, US",
              "route": "2600:9000:2047::/48",
              "name": "AMAZON-02"
            },
            "dns": {},
            "geoip": {
              "range": "",
              "country": "US",
              "region": "",
              "city": "",
              "ll": [
                37.751,
                -97.822
              ],
              "metro": 0,
              "area": 100,
              "eu": "0",
              "timezone": "America/Chicago",
              "country_name": "United States"
            },
            "size": 0,
            "encodedSize": 278,
            "countries": [
              "US"
            ],
            "index": 0,
            "ipv6": true,
            "redirects": 1,
            "count": null
          }
        ]
      },
      "verdicts": {
        "overall": {
          "score": 0,
          "categories": [],
          "brands": [],
          "tags": [],
          "malicious": false,
          "hasVerdicts": 0
        },
        "urlscan": {
          "score": 0,
          "categories": [],
          "brands": [],
          "tags": [],
          "detectionDetails": [],
          "malicious": false
        },
        "engines": {
          "score": 0,
          "malicious": [],
          "benign": [],
          "maliciousTotal": 0,
          "benignTotal": 0,
          "verdicts": [],
          "enginesTotal": 0
        },
        "community": {
          "score": 0,
          "votes": [],
          "votesTotal": 0,
          "votesMalicious": 0,
          "votesBenign": 0,
          "tags": [],
          "categories": []
        }
      }
    }
  },
  "version": "v1",
  "type": "action_event"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 4.0.2 - Fix error handling while submit URL which is in blacklist of URLScan API | Update SDK to version 4
* 4.0.1 - Fix issue with not compatible types in custom output type for Get Scan Result action | Add unit tests for Get Scan Result | Refactor existing unit tests
* 4.0.0 - Improve pagination in Search action
* 3.0.1 - Add unit test for Submit URL for Scan action | Add error handling for HTTP 429 status code in Submit URL for Scan action
* 3.0.0 - Major version bump to ensure awareness of a breaking change related to the addition of the `was_scan_skipped` output in Submit URL for Scan action in the previous version
* 2.3.0 - Add logger when submitted domain is in blacklist for Submit URL for Scan action
* 2.2.0 - Add new input Input Type in Search action
* 2.1.8 - Correct spelling in help.md
* 2.1.7 - Add missing outputs to Get Scan Results action
* 2.1.6 - Add default input
* 2.1.5 - Add example input
* 2.1.4 - Use input and output constants | Added "f" strings
* 2.1.3 - New spec and help.md format for the Extension Library
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
