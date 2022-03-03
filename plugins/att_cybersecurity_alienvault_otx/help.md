# Description

AT&T Cybersecurity [Alienvault OTX](https://otx.alienvault.com/) is an open threat exchange service.
The AT&T CyberSecurity Alienvault OTX InsightConnect plugin allows you to retrieve details about an indicator.

This plugin utilizes the Python library [OTXv2](https://github.com/AlienVault-OTX/OTX-Python-SDK).

# Key Features

* Retrieve details about an indicator

# Requirements

* AlienVault Open Threat Exchange API key
* AlienVault Open Threat Exchange instance URL

# Supported Product Versions

* OTX DirectConnect API v1 2022-03-29T14:00:00Z

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|AlienVault Open Threat Exchange API key|None|3395856ce81f2b7382dee72602f798b642f14140|
|url|string|https://example.com|True|AlienVault Open Threat Exchange URL|None|https://otx.alienvault.com|

Example input:

```
{
  "api_key": "3395856ce81f2b7382dee72602f798b642f14140",
  "url": "https://otx.alienvault.com"
}
```

## Technical Details

### Actions

#### Get Indicator Details

This action is used to return details about an indicator.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|indicator|string|None|True|Indicator to search in OTX|None|https://example.com|
|indicator_type|string|None|True|Indicator type to search|['IPv4', 'IPv6', 'URL', 'HOSTNAME']|URL|
|section|string|None|True|Section of information returned from the searched|['general', 'geo', 'malware', 'passive_dns', 'reputation', 'url_list', 'full']|general|

When using a different section other than `full` on a given indicator type, some only allow a few sections.
Below is a list for each indicator type and the sections they support.

|Indicator Type|Section|
|--------------|-------|
|IPv4|['general', 'geo', 'malware', 'url_list', 'passive_dns', 'reputation', 'full']|
|IPv6|['general', 'geo', 'malware', 'url_list', 'passive_dns', 'reputation', 'full']|
|URL|['general', 'url_list', 'full']|
|HOSTNAME|['general', 'geo', 'malware', 'url_list', 'passive_dns', 'full']|

Example input:

```
{
  "indicator": "https://example.com",
  "indicator_type": "URL",
  "section": "general"
}
```

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

_This plugin does not contain any triggers._

### Custom Output Types

#### _id

|Name|Type|Required|Description|
|----|----|--------|-----------|
|$ID|string|False|$ID|

#### activities

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Data|data|False|Data|
|Data Key|string|False|Data key|
|Domain|string|False|Domain|
|File|string|False|File|
|First Date|string|False|First date|
|Last Date|string|False|Last date|
|MD5 hash|string|False|MD5 hash|
|Name|string|False|Name|
|Source|string|False|Source|
|Status|integer|False|Status|
|URL|string|False|URL|
|Visible|string|False|Visible|
|VT|string|False|VT|

#### author

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Avatar URL|string|False|Avatar URL|
|ID|string|False|ID|
|Is Following|boolean|False|Is following|
|Is Subscribed|boolean|False|Is subscribed|
|Username|string|False|Username|

#### base_indicator

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access Reason|string|False|Access reason|
|Access Type|string|False|Access type|
|Content|string|False|Content|
|Description|string|False|Description|
|ID|integer|False|ID|
|Indicator|string|False|Indicator|
|Title|string|False|Title|
|Type|string|False|Type|

#### counts

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Malware Domain|integer|False|Malware domain|

#### data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Domain|string|False|Domain|
|File|string|False|File|
|MD5|string|False|MD5|
|URL|string|False|URL|
|Virus Total|VT|False|Virus Total|

#### data_malware

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Datetime|integer|False|Datetime|
|Hash|string|False|Hash|

#### date_added

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Sec|integer|False|Sec|
|Usec|integer|False|Usec|

#### general

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Area Code|integer|False|Area code|
|ASN|string|False|Autonomous System Number|
|Base Indicator|base_indicator|False|Base indicator|
|Charset|integer|False|Charset|
|City|string|False|City|
|City Data|boolean|False|City data|
|Continent Code|string|False|Continent code|
|Country Code|string|False|Country code|
|Country Code3|string|False|Country code3|
|Country Name|string|False|Country name|
|DMA Code|integer|False|DMA code|
|Flag Title|string|False|Flag title|
|Flag URL|string|False|Flag URL|
|Indicator|string|False|Indicator|
|Latitude|float|False|Latitude|
|Longitude|float|False|Longitude|
|Postal Code|string|False|Postal code|
|Pulse Info|pulse_info|False|Pulse info|
|Region|string|False|Region|
|Reputation|integer|False|Reputation|
|Sections|[]string|False|Sections|
|Type|string|False|Type|
|Type Title|string|False|Type title|
|WHOIS|string|False|WHOIS|

#### geo

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Area Code|integer|False|Area code|
|ASN|string|False|Autonomous System Number|
|Charset|integer|False|Charset|
|City|string|False|City|
|City Data|boolean|False|City data|
|Continent Code|string|False|Continent code|
|Country Code|string|False|Country code|
|Country Code3|string|False|Country code3|
|Country Name|string|False|Country name|
|DMA Code|integer|False|DMA code|
|Flag Title|string|False|Flag title|
|Flag URL|string|False|Flag URL|
|Latitude|float|False|Latitude|
|Longitude|float|False|Longitude|
|Postal Code|string|False|Postal code|
|Region|string|False|Region|

#### groups

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|integer|False|Group ID|
|Name|string|False|Group name|

#### indicator_detail_full

|Name|Type|Required|Description|
|----|----|--------|-----------|
|General|general|False|General|
|Geo|geo|False|Geo|
|Malware|malware|False|Malware|
|Passive DNS|passive_dns|False|Passive DNS|
|Reputation|reputation|False|Reputation|
|URL List|url_list|False|URL list|

#### indicator_type_counts

|Name|Type|Required|Description|
|----|----|--------|-----------|
|IPv4|integer|False|IPv4|
|URL|integer|False|URL count|
|Domain|integer|False|Domain count|
|Email|integer|False|Email|
|Hostname|integer|False|Hostname count|

#### malware

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Count|integer|False|Count|
|Data|[]data_malware|False|Data|
|Next|string|False|Next|
|Previous|string|False|Previous|
|Size|integer|False|Size|

#### observation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Adversary|string|False|Adversary|
|Author ID|integer|False|Author ID|
|Author Name|string|False|Author name|
|Avatar URL|string|False|Avatar URL|
|Cloned From|string|False|Cloned from|
|Comment Count|integer|False|Comment count|
|Created|string|False|Created|
|Description|string|False|Description|
|Downvotes Count|float|False|Downvotes count|
|Export Count|integer|False|Export count|
|Extract Source|[]string|False|Extract source|
|Follower Count|integer|False|Follower count|
|Groups|[]groups|False|Groups|
|ID|string|False|ID|
|Indicator Type Counts|indicator_type_counts|False|Indicator type counts|
|Industries|[]string|False|Industries|
|Is Following|boolean|False|Is following|
|Is Subscribed|boolean|False|Is subscribed|
|Is Subscribing|boolean|False|Is subscribing|
|Locked|boolean|False|Locked|
|Modified|string|False|Modified|
|Name|string|False|Name|
|Public|integer|False|Public|
|Pulse Source|string|False|Pulse source|
|References|[]string|False|References|
|Revision|integer|False|Revision|
|Subscriber Count|integer|False|Subscriber count|
|Tags|[]string|False|Tags|
|Targeted Countries|[]string|False|Targeted countries|
|TLP|string|False|Traffic Light Protocol|
|Upvotes Count|float|False|Upvotes count|
|User Subscriber Count|integer|False|User subscriber count|
|Validator Count|integer|False|Validator count|
|Vote|integer|False|Vote|
|Votes Count|number|False|Votes count|

#### passive_dns

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Count|integer|False|Count|
|Passive DNS|[]passive_dns_nest|False|Passive DNS|

#### passive_dns_nest

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Address|string|False|Address|
|Asset Type|string|False|Asset type|
|First|string|False|First|
|Flag Title|string|False|Flag title|
|Flag URL|string|False|Flag URL|
|Hostname|string|False|Hostname|
|Indicator Link|string|False|Indicator link|
|Last|string|False|Last|

#### pulse_info

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Count|integer|False|Count|
|Pulses|[]pulses|False|Pulses|
|References|[]string|False|References|

#### pulses

|Name|Type|Required|Description|
|----|----|--------|-----------|
|TLP|string|False|Traffic Light Protocol|
|Adversary|string|False|Adversary|
|Author|author|False|Author|
|Cloned From|string|False|Cloned from|
|Comment Count|integer|False|Comment count|
|Created|string|False|Created|
|Description|string|False|Description|
|Downvotes Count|float|False|Downvotes count|
|Export Count|integer|False|Export count|
|Follower Count|integer|False|Follower count|
|Groups|[]groups|False|Groups|
|ID|string|False|ID|
|In Group|boolean|False|In group|
|Indicator Count|integer|False|Indicator count|
|Indicator Type Counts|indicator_type_counts|False|Indicator type counts|
|Industries|[]object|False|Industries|
|Is Author|boolean|False|Is author|
|Is Following|boolean|False|Is following|
|Is Modified|boolean|False|Is modified|
|Is Subscribing|boolean|False|Is subscribing|
|Locked|boolean|False|Locked|
|Modified|string|False|Modified|
|Modified Text|string|False|Modified text|
|Name|string|False|Name|
|Observation|observation|False|Observation|
|Public|integer|False|Public|
|Pulse Source|string|False|Pulse source|
|References|[]string|False|References|
|Subscriber Count|integer|False|Subscriber count|
|Tags|[]string|False|Tags|
|Targeted Countries|[]object|False|Targeted countries|
|Threat Hunter Scannable|boolean|False|Threat hunter scannable|
|Upvotes Count|float|False|Upvotes count|
|Validator Count|integer|False|Validator count|
|Vote|integer|False|Vote|
|Votes Count|number|False|Votes count|

#### reputation

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Reputation|reputation_details|False|Reputation|

#### reputation_details

|Name|Type|Required|Description|
|----|----|--------|-----------|
| Id|_id|False| id|
|Activities|[]activities|False|Activities|
|Address|string|False|Address|
|Allow Ping|string|False|Allow ping|
|As|string|False|As|
|City|string|False|City|
|Country|string|False|Country|
|Counts|counts|False|Counts|
|Date Added|date_added|False|Date added|
|Domains|[]string|False|Domains|
|First Seen|string|False|First seen|
|Last Seen|string|False|Last seen|
|Lat|integer|False|Lat|
|Lon|integer|False|Lon|
|Matched Blacklist|[]string|False|Matched blacklist|
|Matched Whitelist|[]string|False|Matched whitelist|
|Organization|string|False|Organization|
|Reputation Rel|string|False|Reputation rel|
|Reputation Rel Checked|integer|False|Reputation rel checked|
|Reputation Value|string|False|Reputation value|
|Reputation Value Checked|integer|False|Reputation value checked|
|Server Type|string|False|Server type|
|State|integer|False|State|
|Status|integer|False|Status|
|Threat Score|integer|False|Threat score|
|Up|integer|False|Up|

#### result

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Safebrowsing|safebrowsing|False|Safebrowsing|
|URL worker|urlworker|False|URL worker|

#### result_url_list_nest

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Safe Browsing|safebrowsing|False|Safe browsing|
|URL Worker|urlworker|False|URL worker|

#### safebrowsing

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Matches|[]string|False|Matches|

#### url_list

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Actual Size|integer|False|Actual size|
|Full Size|integer|False|Full size|
|Has Next|boolean|False|Has next|
|Limit|integer|False|Limit|
|Page Number|integer|False|Page number|
|Paged|boolean|False|Paged|
|URL List|[]url_list_nest|False|URL list|

#### url_list_nest

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Date|string|False|Date|
|Domain|string|False|Domain|
|Encoded|string|False|URL encoded string|
|GSB|[]string|False|GSB|
|Hostname|string|False|Hostname|
|HTTP Code|integer|False|HTTP code|
|Result|result_url_list_nest|False|Result|
|URL|string|False|URL|

#### urlworker

|Name|Type|Required|Description|
|----|----|--------|-----------|
|HTTP Code|integer|False|HTTP code|
|IP|string|False|IP|

#### VT

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Signature|string|False|Signature|

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 3.0.0 - Update custom output types in plugin.spec | Add input examples | Code refactor
* 2.0.0 - New spec and help.md format update for the Extension Library | Variable names updated as acronyms
* 1.0.1 - Update custom type and added HOSTNAME as a supported indicator type for Get Indicator Details
* 1.0.0 - Initial plugin

# Links

## References

* [Alienvault OTX](https://otx.alienvault.com/)
* [OTXv2](https://github.com/AlienVault-OTX/OTX-Python-SDK)

