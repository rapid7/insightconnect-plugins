# Description

AT&T Cybersecurity [Alienvault OTX](https://otx.alienvault.com/) is an open threat exchange service.
The AT&T CyberSecurity Alienvault OTX InsightConnect plugin allows you to retrieve details about an indicator.

This plugin utilizes the Python library [OTXv2](https://github.com/AlienVault-OTX/OTX-Python-SDK).

# Key Features

* Retrieve details about an indicator

# Requirements

* AlienVault Open Threat Exchange API key
* AlienVault Open Threat Exchange instance URL

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|AlienVault Open Threat Exchange API key|None|
|url|string|https://otx.alienvault.com/|True|AlienVault Open Threat Exchange URL|None|

## Technical Details

### Actions

#### Get Indicator Details

This action is used to return details about an indicator.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|indicator_type|string|None|True|Indicator type to search|['IPv4', 'IPv6', 'URL', 'HOSTNAME']|
|indicator|string|None|True|Indicator to search in OTX|None|
|section|string|None|True|Section of information returned from the searched|['general', 'geo', 'malware', 'passive_dns', 'reputation', 'url_list', 'full']|

When using a different section other than `full` on a given indicator type, some only allow a few sections.
Below is a list for each indicator type and the sections they support.

|Indicator Type|Section|
|--------------|-------|
|IPv4|['general', 'geo', 'malware', 'url_list', 'passive_dns', 'reputation', 'full']|
|IPv6|['general', 'geo', 'malware', 'url_list', 'passive_dns', 'reputation', 'full']|
|URL|['general', 'url_list', 'full']|
|HOSTNAME|['general', 'geo', 'malware', 'url_list', 'passive_dns', 'full']|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|indicator_detail_full|False|Indicator results|

Example output:

```
{
  "general": {
    "sections": [
      "general",
      "geo",
      "reputation",
      "url_list",
      "passive_dns",
      "malware",
      "nids_list",
      "http_scans"
    ],
    "city": "Seoul",
    "area_code": 0,
    "pulse_info": {
      "count": 0,
      "references": [],
      "pulses": []
    },
    "continent_code": "AS",
    "country_name": "Korea, Republic of",
    "dma_code": 0,
    "country_code": "KR",
    "flag_url": "/static/img/flags/kr.png",
    "asn": "AS9318 SK Broadband Co Ltd",
    "city_data": true,
    "indicator": "175.126.38.143",
    "whois": "http://whois.domaintools.com/175.126.38.143",
    "type_title": "IPv4",
    "region": "11",
    "charset": 0,
    "longitude": 126.9783,
    "country_code3": "KOR",
    "reputation": 0,
    "base_indicator": {},
    "latitude": 37.5985,
    "type": "IPv4",
    "flag_title": "Korea, Republic of"
  },
  "reputation": {},
  "geo": {
    "flag_url": "/static/img/flags/kr.png",
    "city_data": true,
    "city": "Seoul",
    "region": "11",
    "charset": 0,
    "area_code": 0,
    "continent_code": "AS",
    "country_code3": "KOR",
    "latitude": 37.5985,
    "longitude": 126.9783,
    "country_code": "KR",
    "country_name": "Korea, Republic of",
    "asn": "AS9318 SK Broadband Co Ltd",
    "dma_code": 0,
    "flag_title": "Korea, Republic of"
  },
  "malware": {
    "data": [],
    "next": "https://otx.alienvault.com/api/v1/indicators/IPv6/175.126.38.143/malware?page=2"
  },
  "url_list": {
    "has_next": false,
    "actual_size": 4,
    "url_list": [
      {
        "domain": "wnbbeauty.com",
        "url": "http://www.wnbbeauty.com/assets/images/favicon.ico",
        "hostname": "www.wnbbeauty.com",
        "httpcode": 200,
        "gsb": [],
        "result": {
          "urlworker": {
            "ip": "175.126.38.143",
            "http_code": 200
          },
          "safebrowsing": {
            "matches": []
          }
        },
        "date": "2019-02-26T14:29:06",
        "encoded": "http%3A//www.wnbbeauty.com/assets/images/favicon.ico"
      },
      {
        "domain": "wnbcorp.com",
        "url": "http://wnbcorp.com/",
        "hostname": "wnbcorp.com",
        "httpcode": 200,
        "gsb": [],
        "result": {
          "urlworker": {
            "ip": "175.126.38.143",
            "http_code": 200
          },
          "safebrowsing": {
            "matches": []
          }
        },
        "date": "2019-02-06T02:40:30",
        "encoded": "http%3A//wnbcorp.com/"
      },
      {
        "domain": "wnbbeauty.com",
        "url": "http://wnbbeauty.com/assets/docs/%EC%9D%B4%EB%A0%A5%EC%84%9C%20%EB%B0%8F%20%EC%9E%90%EA%B8%B0%EC%86%8C%EA%B0%9C%EC%84%9C_%EC%9B%8C%EB%84%88%EB%B9%84.hwp",
        "hostname": "wnbbeauty.com",
        "httpcode": 200,
        "gsb": [],
        "result": {
          "urlworker": {
            "ip": "175.126.38.143",
            "http_code": 200
          },
          "safebrowsing": {
            "matches": []
          }
        },
        "date": "2019-01-26T20:09:55",
        "encoded": "http%3A//wnbbeauty.com/assets/docs/%25EC%259D%25B4%25EB%25A0%25A5%25EC%2584%259C%2520%25EB%25B0%258F%2520%25EC%259E%2590%25EA%25B8%25B0%25EC%2586%258C%25EA%25B0%259C%25EC%2584%259C_%25EC%259B%258C%25EB%2584%2588%25EB%25B9%2584.hwp"
      },
      {
        "domain": "lingostack.com",
        "url": "http://lingostack.com/",
        "hostname": "lingostack.com",
        "httpcode": 200,
        "gsb": [],
        "result": {
          "urlworker": {
            "ip": "175.126.38.143",
            "http_code": 200
          },
          "safebrowsing": {
            "matches": []
          }
        },
        "date": "2017-06-15T20:56:51",
        "encoded": "http%3A//lingostack.com/"
      }
    ],
    "page_num": 1,
    "limit": 10,
    "full_size": 4,
    "paged": true
  },
  "passive_dns": {
    "passive_dns": [
      {
        "last": "Tue, 26 Feb 2019 14:45:47 GMT",
        "indicator_link": "/indicator/hostname/www.wnbbeauty.com",
        "hostname": "www.wnbbeauty.com",
        "address": "175.126.38.143",
        "flag_url": "/static/img/flags/kr.png",
        "flag_title": "Korea, Republic of",
        "asset_type": "hostname",
        "first": "Tue, 26 Feb 2019 14:45:47 GMT"
      }
    ],
    "count": 1
  }
}
```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 2.0.0 - New spec and help.md format update for the Hub | Variable names updated as acronyms
* 1.0.1 - Update custom type and added HOSTNAME as a supported indicator type for Get Indicator Details
* 1.0.0 - Initial plugin

# Links

## References

* [Alienvault OTX](https://otx.alienvault.com/)
* [OTXv2](https://github.com/AlienVault-OTX/OTX-Python-SDK)

