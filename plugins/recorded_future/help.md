# Description

[Recorded Future](https://www.recordedfuture.com/) arms threat analysts, security operators, and incident
  responders to rapidly connect the dots and reveal unknown threats. Using the Recorded Future plugin for Rapid7
InsightConnect, users can search domain lists, entity lists, and more.

Use Recorded Future within an automation workflow to quickly assist with threat analysis, incident response, and
vulnerability management.

Note: When a plugin action that causes a file to be downloaded is invoked, the file data is parsed internally and
returned in the [STIX](https://stixproject.github.io/about/) format.

# Key Features

* Search domain, hash, malware, vulnerability, entity, URL and IP lists
* Download risk lists
* Lookup alert, domain, hash, malware, vulnerability, entity, URL and IP

# Requirements

* Recorded Future API key

# Supported Product Versions

* Recorded Future API 2022-04-09

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|API key|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "api_key": {
    "secretKey":"9de5069c5afe602b2ea0a04b66beb2c0"
  }
}
```

## Technical Details

### Actions

#### Lookup Alert

This action is used to get information about an Alert.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_id|string|None|True|Alert ID|None|fhS1El|

Example input:

```
{
  "alert_id": "fhS1El"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alert|alert|True|Alert details|
|result_found|boolean|True|Whether the result was found|

Example output:

```
{
  "result_found": true,
  "alert": {
    "review": {
      "status": "no-action"
    },
    "entities": [
      {
        "entity": {
          "id": "faymwJ",
          "name": "CVE-2015-4719",
          "type": "CyberVulnerability",
          "description": "The client API authentication mechanism in Pexip Infinity before 10 allows remote attackers to gain privileges via a crafted request."
        },
        "risk": {
          "criticalityLabel": "High",
          "documents": [
            {
              "references": [
                {
                  "fragment": "CVE-2015-4719 (infinity).",
                  "entities": [
                    {
                      "id": "faymwJ",
                      "name": "CVE-2015-4719",
                      "type": "CyberVulnerability",
                      "description": "The client API authentication mechanism in Pexip Infinity before 10 allows remote attackers to gain privileges via a crafted request."
                    }
                  ],
                  "language": "eng"
                }
              ],
              "source": {
                "id": "Z3TZAQ",
                "name": "Sesin at",
                "type": "Source"
              },
              "url": "https://www.sesin.at/2020/10/02/cve-2015-4719-infinity/",
              "title": "CVE-2015-4719 (infinity)"
            },
            {
              "references": [
                {
                  "fragment": "New post from https://t.co/uXvPWJy6tj (CVE-2015-4719 (infinity)) has been published on https://t.co/Aw7GbAXNJr.",
                  "entities": [
                    {
                      "id": "faymwJ",
                      "name": "CVE-2015-4719",
                      "type": "CyberVulnerability",
                      "description": "The client API authentication mechanism in Pexip Infinity before 10 allows remote attackers to gain privileges via a crafted request."
                    },
                    {
                      "id": "url:https://www.sesin.at/2020/10/02/cve-2015-4719-infinity/",
                      "name": "https://www.sesin.at/2020/10/02/cve-2015-4719-infinity/",
                      "type": "URL"
                    }
                  ],
                  "language": "eng"
                }
              ],
              "source": {
                "id": "BV5",
                "name": "Twitter",
                "type": "Source"
              },
              "url": "https://twitter.com/WolfgangSesin/statuses/1311902525512126464",
              "title": "New post from https://t.co/uXvPWJy6tj (CVE-2015-4719 (infinity)) has been published on https://t.co/Aw7GbAXNJr"
            }
          ],
          "evidence": [
            {
              "timestamp": "2020-09-25T07:17:09.000Z",
              "criticalityLabel": "Low",
              "evidenceString": "8 sightings on 8 sources including: SecurityDatabase Alerts Monitor Last 100 Alerts, vulmon.com, @NetHaxBot, @VulmonFeeds, @VulnSME. Most recent tweet: New/Modified vulnerability published September 23, 2020 at 07:15PM on the NVD: CVE-2015-4719 https://t.co/oso1bdme0I The client API authentication mechanism in Pexip Infinity before 10 allows remote attackers to gain privileges via a crafted request. Most recent link (Sep 25, 2020): https://twitter.com/SecRiskRptSME/statuses/1309391474354802688",
              "rule": "Linked to Recent Cyber Exploit",
              "criticality": 1
            }
          ],
          "criticality": 3
        },
        "trend": {},
        "documents": []
      }
    ],
    "url": "https://app.recordedfuture.com/live/sc/notification/?id=fhS1El",
    "rule": {
      "url": "https://app.recordedfuture.com/live/sc/ViewIdkobra_view_report_item_alert_editor?view_opts=%7B%22reportId%22%3A%22feScJA%22%2C%22bTitle%22%3Atrue%2C%22title%22%3A%22Global+Vulnerability+Risk%2C+Vulnerabilities%2C+New+Exploit+Chatter%22%7D&state.bNavbar=false",
      "name": "Global Vulnerability Risk, Vulnerabilities, New Exploit Chatter",
      "id": "feScJA"
    },
    "triggered": "2020-10-02T06:55:23.996Z",
    "id": "fhS1El",
    "counts": {
      "references": 2,
      "entities": 1,
      "documents": 2
    },
    "title": "Global Vulnerability Risk, Vulnerabilities, New Exploit Chatter - ... is n...",
    "type": "ENTITY"
  }
}
```

#### Download URL Risk List

This action returns a risk list of URLs matching a filtration.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|list|string|None|False|The risk list to retrieve, left this field blank to retrieve default risk list|['Historically Reported by Insikt Group', 'C&C URL', 'Compromised URL', 'Historically Reported as a Defanged URL', 'Historically Reported by DHS AIS', 'Historically Reported Fraudulent Content', 'Historically Reported in Threat List', 'Large', 'Historically Detected Malicious Browser Exploits', 'Historically Detected Malware Distribution', 'Historically Detected Cryptocurrency Mining Techniques', 'Historically Detected Phishing Techniques', 'Active Phishing URL', 'Positive Malware Verdict', 'Ransomware Distribution URL', 'Recently Reported by Insikt Group', 'Recently Reported as a Defanged URL', 'Recently Reported by DHS AIS', 'Recently Reported Fraudulent Content', 'Recently Detected Malicious Browser Exploits', 'Recently Detected Malware Distribution', 'Recently Detected Cryptocurrency Mining Techniques', 'Recently Detected Phishing Techniques', 'Recent Ransomware Distribution URL', 'Recently Referenced by Insikt Group', 'Recently Reported Spam or Unwanted Content', 'Recently Detected Suspicious Content', 'Recently Active URL on Weaponized Domain', 'Historically Referenced by Insikt Group', 'Historically Reported Spam or Unwanted Content', 'Historically Detected Suspicious Content']|Historically Reported by Insikt Group|

Example input:

```
{
  "list": "Historically Reported by Insikt Group"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|True|Risk list of matching URLs|

Example output:

```
{
  "risk_list": {
    "stix:STIX_Package": {
      "@id": "RF:Package-3010d88d-7551-4e3e-a5c7-27120c6a7fb9",
      "@timestamp": "2020-09-29T16:56:54.355Z",
      "@version": "1.2",
      "@xmlns": "http://xml/metadataSharing.xsd",
      "@xmlns:FileObj": "http://example.com",
      "@xmlns:RF": "http://example.com",
      "@xmlns:URIObj": "http://example.com",
      "@xmlns:cybox": "http://cybox.mitre.org/cybox-2",
      "@xmlns:cyboxCommon": "http://example.com",
      "@xmlns:cyboxVocabs": "http://example.com",
      "@xmlns:indicator": "http://example.com",
      "@xmlns:stix": "http://example.com",
      "@xmlns:stixCommon": "http://example.com",
      "@xmlns:stixVocabs": "http://example.com",
      "@xmlns:ttp": "http://example.com",
      "stix:Indicators": {
        "stix:Indicator": [
          {
            "@id": "RF:Indicator-7cbc818a-4b71-360f-9764-350ad972f259",
            "@timestamp": "2020-09-29T16:56:54.355Z",
            "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
            "@xsi:type": "indicator:IndicatorType",
            "indicator:Confidence": {
              "stixCommon:Description": "Recorded Future Risk Score",
              "stixCommon:Value": "91"
            },
            "indicator:Description": "Current risk: Very Malicious.Triggers 3 of 29 rules",
            "indicator:Indicated_TTP": [
              {
                "stixCommon:Confidence": {
                  "stixCommon:Value": {
                    "#text": "Low",
                    "@xsi:type": "stixVocabs:HighMediumLowVocab-1.0"
                  }
                },
                "stixCommon:TTP": {
                  "@id": "RF:TTP-5b76b9e8-c56a-329f-93e5-607d53910606",
                  "@timestamp": "2019-12-07T23:10:05.000Z",
                  "@xsi:type": "ttp:TTPType",
                  "ttp:Description": "4 sightings on 1 source: Recorded Future URL Analysis.",
                  "ttp:Title": "Risk Rule: Historically Detected Malicious Browser Exploits"
                }
              }
            ],
            "indicator:Observable": {
              "@id": "RF:Observable-dfaf650a-752f-3888-b23e-d26acd059d71",
              "cybox:Object": {
                "@id": "RF:URL-29171cf8-fcc0-35ff-a06e-4c56a52584c0",
                "cybox:Properties": {
                  "@xsi:type": "URIObj:URIObjectType",
                  "URIObj:Value": {
                    "#text": "http://bolizarsospos.com/raph9xccgxt",
                    "@condition": "Equals"
                  }
                }
              }
            },
            "indicator:Producer": {
              "stixCommon:Description": "Recorded Future",
              "stixCommon:References": {
                "stixCommon:Reference": "http://example.com"
              }
            },
            "indicator:Title": "URL http://bolizarsospos.com/raph9xccgxt",
            "indicator:Type": {
              "#text": "URL Watchlist",
              "@xsi:type": "stixVocabs:IndicatorTypeVocab-1.1"
            },
            "indicator:Valid_Time_Position": {
              "indicator:End_Time": {
                "#text": "2020-09-29T23:59:59.000Z",
                "@precision": "second"
              },
              "indicator:Start_Time": {
                "#text": "2020-09-29T00:00:00.000Z",
                "@precision": "second"
              }
            }
          }
        ]
      },
      "stix:STIX_Header": {
        "stix:Description": "Recorded Future STIX"
      }
    }
  }
}
```

#### Search URLs

This action is used to search for data related to URLs.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|direction|string|None|False|Sort results ascending/descending|['asc', 'desc']|asc|
|from|number|None|False|Number of initial records to skip|None|0|
|limit|number|10|False|Number of results to retrieve, up to 100|None|10|
|orderby|string|None|False|Which property to sort the results by|['Created', 'Criticality', 'Lastseen', 'Firstseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|Riskscore|
|riskRule|string|None|False|Risk rule of data|['Historically Reported by Insikt Group', 'C&C URL', 'Compromised URL', 'Historically Reported as a Defanged URL', 'Historically Reported by DHS AIS', 'Historically Reported Fraudulent Content', 'Historically Reported in Threat List', 'Historically Detected Malicious Browser Exploits', 'Historically Detected Malware Distribution', 'Historically Detected Cryptocurrency Mining Techniques', 'Historically Detected Phishing Techniques', 'Active Phishing URL', 'Positive Malware Verdict', 'Ransomware Distribution URL', 'Recently Reported by Insikt Group', 'Recently Reported as a Defanged URL', 'Recently Reported by DHS AIS', 'Recently Reported Fraudulent Content', 'Recently Detected Malicious Browser Exploits', 'Recently Detected Malware Distribution', 'Recently Detected Cryptocurrency Mining Techniques', 'Recently Detected Phishing Techniques', 'Recent Ransomware Distribution URL', 'Recently Referenced by Insikt Group', 'Recently Reported Spam or Unwanted Content', 'Recently Detected Suspicious Content', 'Recently Active URL on Weaponized Domain', 'Historically Referenced by Insikt Group', 'Historically Reported Spam or Unwanted Content', 'Historically Detected Suspicious Content']|Historically Reported by Insikt Group|
|riskScore|string|None|False|Risk score of data|None|[0,100]|

Example input:

```
{
  "direction": "asc",
  "from": 0,
  "limit": 10,
  "orderby": "Riskscore",
  "riskRule": "Historically Reported by Insikt Group",
  "riskScore": "[0,100]"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]url_search_data|True|Search result|

Example output:

```
{
  "data": {
    "results": [
      {
        "analystNotes": [
          {
            "source": {
              "id": "VKz42X",
              "name": "Insikt Group",
              "type": "Source"
            },
            "attributes": {
              "validated_on": "2018-04-24T04:00:00.000Z",
              "published": "2018-04-24T04:00:00.000Z",
              "text": "On April 24, 2018 around 7:30am EST, MyEtherWallet (MEW) shared via Twitter that a number of Domain Name System (DNS) registration servers were hijacked to redirect users to a phishing site, including Google Public DNS 8.8.8.8/8.8.4.4. Those who were redirected to the phishing site were prompted to enter their MEW account information, allowing attackers to gain access to their account and ultimately steal their cryptocurrency. It is not certain exactly how much money the cyber criminals were able to steal total. Current estimates are around $150,000 or 216 Ether. Around 1:30pm EST later the same day, MyEtherWallet tweeted that the issue had been resolved. MyEtherWallet is a popular cryptocurrency web app designed for users to store and send ether and ethereum-based tokens.",
              "topic": {
                "id": "TXSFt0",
                "name": "Flash Report",
                "type": "Topic",
                "description": "Overview analysis of a current event. Can include technical details and indicators of compromise."
              },
              "title": "MyEtherWallet DNS servers hijacked",
              "note_entities": [
                {
                  "id": "Smo9TW",
                  "name": "MyEtherWallet.com",
                  "type": "Company"
                }
              ],
              "context_entities": [
                {
                  "id": "ip:8.8.4.4",
                  "name": "8.8.4.4",
                  "type": "IpAddress"
                }
              ],
              "validation_urls": [
                {
                  "id": "url:url:https://www.coindesk.com/150k-stolen-myetherwallet-users-dns-server-hijacking/",
                  "name": "url:https://www.coindesk.com/150k-stolen-myetherwallet-users-dns-server-hijacking/",
                  "type": "URL"
                }
              ]
            },
            "id": "V3-CAc"
          }
        ],
        "enterpriseLists": [],
        "timestamps": {
          "firstSeen": "2020-09-24T00:00:00.000Z",
          "lastSeen": "2020-09-24T23:59:59.000Z"
        },
        "risk": {
          "criticalityLabel": "Unusual",
          "score": 5,
          "evidenceDetails": [
            {
              "mitigationString": "",
              "timestamp": "2018-04-24T00:00:00.000Z",
              "criticalityLabel": "Unusual",
              "evidenceString": "1 sighting on 1 source: Insikt Group. 1 report: MyEtherWallet DNS servers hijacked (Apr 24, 2018).",
              "rule": "Historically Reported by Insikt Group",
              "criticality": 1
            }
          ],
          "riskString": "1/29",
          "rules": 1,
          "criticality": 1,
          "riskSummary": "1 of 29 Risk Rules currently observed."
        },
        "sightings": [],
        "entity": {
          "id": "url:https://myetherwallet.com/",
          "name": "https://myetherwallet.com/",
          "type": "URL"
        },
        "counts": [
          {
            "count": 1,
            "date": "2018-04-24"
          }
        ],
        "metrics": [
          {
            "type": "whitlistedCount",
            "value": 0
          }
        ],
        "relatedEntities": []
      }
    ]
  },
  "counts": {
    "returned": 1,
    "total": 157
  }
}

```

#### List URL Risk Rules

This action is used to list available filtration rules for URL risk lists.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_rules|[]risk_rule|True|Risk rules for URL|

Example output:

```
{
  "risk_rules": [
    {
      "count": 2239,
      "criticality": 3,
      "criticalityLabel": "Malicious",
      "description": "Compromised URL",
      "name": "compromisedUrl",
      "relatedEntities": []
    }
  ]
}
```

#### List IP Addresses Risk Rules

This action is used to list available filtration rules for IP address risk lists.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_rules|[]risk_rule|True|Risk rules|

Example output:

```
{
  "risk_rules": [
    {
      "count": 75508,
      "criticality": 1,
      "criticalityLabel": "Unusual",
      "description": "Historical Threat Researcher",
      "name": "threatResearcher",
      "relatedEntities": []
    },
    {
      "count": 517,
      "criticality": 2,
      "criticalityLabel": "Suspicious",
      "description": "Recently Reported as a Defanged IP",
      "name": "recentDefanged",
      "relatedEntities": []
    },
    {
      "count": 102959,
      "criticality": 1,
      "criticalityLabel": "Unusual",
      "description": "Vulnerable Host",
      "name": "vulnerableHost",
      "relatedEntities": []
    }
  ]
}
```

#### Search Domains

This action is used to search for results related to a specific parent domain.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|direction|string|asc|True|Sort results ascending/descending|['asc', 'desc']|asc|
|from|number|0|True|Number of initial records to skip|None|0|
|limit|number|None|True|Number of results to retrieve, up to 100|None|10|
|orderby|string|None|True|Which property to sort the results by|['Created', 'Firstseen', 'Lastseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|Riskscore|
|parent|string|None|True|Parent domain, if any|None|example.com|
|riskRule|string|None|False|Filters the results by risk rule|['Historically Reported by Insikt Group', 'Newly Registered Certificate With Potential for Abuse - DNS Sandwich', 'Newly Registered Certificate With Potential for Abuse - Typo or Homograph', 'C&C Nameserver', 'C&C DNS Name', 'C&C URL', 'Compromised URL', 'Historical COVID-19-Related Domain Lure', 'Recently Resolved to Host of Many DDNS Names', 'Historically Reported as a Defanged DNS Name', 'Historically Reported by DHS AIS', 'Recent Fast Flux DNS Name', 'Historically Reported Fraudulent Content', 'Historically Reported in Threat List', 'Historically Linked to Cyber Attack', 'Historical Malware Analysis DNS Name', 'Historically Detected Malware Operation', 'Historically Detected Cryptocurrency Mining Techniques', 'Blacklisted DNS Name', 'Historical Phishing Lure', 'Historically Detected Phishing Techniques', 'Active Phishing URL', 'Recorded Future Predictive Risk Model', 'Historical Punycode Domain', 'Ransomware Distribution URL', 'Ransomware Payment DNS Name', 'Recently Reported by Insikt Group', 'Recent COVID-19-Related Domain Lure - Malicious', 'Recent COVID-19-Related Domain Lure - Suspicious', 'Recently Reported as a Defanged DNS Name', 'Recently Reported by DHS AIS', 'Recently Reported Fraudulent Content', 'Recently Linked to Cyber Attack', 'Recent Malware Analysis DNS Name', 'Recently Detected Malware Operation', 'Recently Detected Cryptocurrency Mining Techniques', 'Recent Phishing Lure - Malicious', 'Recent Phishing Lure - Suspicious', 'Recently Detected Phishing Techniques', 'Recent Punycode Domain', 'Recently Referenced by Insikt Group', 'Recently Reported Spam or Unwanted Content', 'URL Recently Linked to Suspicious Content', 'Recent Threat Researcher', 'Recent Typosquat Similarity - DNS Sandwich', 'Recent Typosquat Similarity - Typo or Homograph', 'Recently Active Weaponized Domain', 'Recently Defaced Site', 'Historically Referenced by Insikt Group', 'Recently Resolved to Malicious IP', 'Recently Resolved to Suspicious IP', 'Recently Resolved to Unusual IP', 'Recently Resolved to Very Malicious IP', 'Trending in Recorded Future Analyst Community', 'Historically Reported Spam or Unwanted Content', 'URL Historically Linked to Suspicious Content', 'Historical Threat Researcher', 'Historical Typosquat Similarity - DNS Sandwich', 'Historical Typosquat Similarity - Typo or Homograph', 'Historically Active Weaponized Domain']|Active Phishing URL|
|riskScore|string|None|False|Filters the results by risk score|None|[1,100]|

Example input:

```
{
  "direction": "asc",
  "from": 0,
  "limit": 10,
  "orderby": "Riskscore",
  "parent": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]domain_search_data|True|Data|

Example output:

```
{
  "counts": {
    "returned": 10,
    "total": 10
  },
  "data": {
    "results": [
      {
        "entity": {
          "id": "idn:blog.recordedfuture.com",
          "name": "blog.recordedfuture.com",
          "type": "InternetDomainName"
        },
        "timestamps": {
          "firstSeen": "2015-09-25T19:27:11.627Z",
          "lastSeen": "2016-11-27T19:53:27.582Z"
        }
      },
      {
        "entity": {
          "id": "idn:api.recordedfuture.com",
          "name": "api.recordedfuture.com",
          "type": "InternetDomainName"
        },
        "timestamps": {
          "firstSeen": "2016-12-19T16:49:10.381Z",
          "lastSeen": "2020-03-25T18:55:20.407Z"
        }
      }
    ]
  }
}
```

#### List Domain Risk Rules

This action is used to list available filtration rules for domain risk lists.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_rules|[]risk_rule|True|Risk rules|

Example output:

```

{
  "risk_rules": [
    {
      "count": 1473,
      "criticality": 3,
      "criticalityLabel": "Malicious",
      "description": "COVID-19-Related Domain Lure",
      "name": "covidLure",
      "relatedEntities": []
    },
    {
      "count": 21739,
      "criticality": 2,
      "criticalityLabel": "Suspicious",
      "description": "Newly Registered Certificate With Potential for Abuse - DNS Sandwich",
      "name": "certTyposquatSandwich",
      "relatedEntities": []
    },
    {
      "count": 134360,
      "criticality": 2,
      "criticalityLabel": "Suspicious",
      "description": "Newly Registered Certificate With Potential for Abuse - Typo or Homograph",
      "name": "certTyposquatTypo",
      "relatedEntities": []
    }
  ]
}

```

#### Search Malware

This action is used to search for data related to malware.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|direction|string|asc|True|Sort results ascending/descending|['asc', 'desc']|asc|
|firstSeen|string|None|False|Filters the results by first seen|None|2016-06-15 07:54:38.286000|
|freetext|string|None|False|Freetext search|None|example|
|from|number|0|True|Number of initial records to skip|None|0|
|limit|number|None|True|Number of results to retrieve, up to 100|None|10|
|list|string|None|False|Filters the results by list ID|None|fKXuF0|
|orderby|string|None|True|Which property to sort the results by|['Created', 'Lastseen', 'Firstseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|Riskscore|

Example input:

```
{
  "direction": "asc",
  "firstSeen": "2016-06-15 07:54:38.286000",
  "freetext": "example",
  "from": 0,
  "limit": 10,
  "list": "fKXuF0",
  "orderby": "Riskscore"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]malware_search_data|True|Data|

Example output:

```
{
  "counts": {
    "returned": 9,
    "total": 9
  },
  "data": {
    "results": [
      {
        "timestamps": {
          "firstSeen": "2017-03-14T09:00:46.277Z",
          "lastSeen": "2020-03-27T14:01:41.045Z"
        },
        "entity": {
          "id": "S0Vzwu",
          "name": "PetrWrap",
          "type": "Malware"
        }
      },
      {
        "entity": {
          "id": "QyiNON",
          "name": "Green Petya",
          "type": "Malware"
        },
        "timestamps": {
          "firstSeen": "2016-05-19T08:04:12.603Z",
          "lastSeen": "2020-03-27T14:01:41.045Z"
        }
      }
    ]
  }
}
```

#### Search Entity Lists

This action is used to perform a freetext search across all Recorded Future entity types (IP address, domain, hash, malware, and vulnerability).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|freetext|string|None|True|Freetext search|None|example|

Example input:

```
{
  "freetext": "example"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entities|[]entity|True|Entities|

Example output:

```
{
  "data": {
    "results": [
      {
        "entity": {
          "description": "Honeypot detections for malware IRC network traffi...",
          "id": "report:OjanJ0",
          "name": "Nothink.org: Malware IRC Network Traffic Blacklist",
          "type": "EntityList"
        }
      },
      {
        "entity": {
          "type": "EntityList",
          "description": "All domains on this list should be considered dang...",
          "id": "report:Oe5eg5",
          "name": "MalwareDomainList: Malicious URL Reports"
        }
      }
    ]
  },
  "counts": {
    "returned": 5,
    "total": 5
  }
}
```

#### Download Domain Risk List

This action returns a risk list of domains matching a filtration rule.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|list|string|None|False|The risk list to retrieve, leaving the list parameter blank results in the default risk list|['Historically Reported by Insikt Group', 'C&C Nameserver', 'C&C DNS Name', 'Compromised URL', 'Historical COVID-19-Related Domain Lure', 'Recently Resolved to Host of Many DDNS Names', 'Historically Reported as a Defanged DNS Name', 'Historically Reported by DHS AIS', 'Recent Fast Flux DNS Name', 'Historically Reported Fraudulent Content', 'Historically Reported in Threat List', 'Historically Linked to Cyber Attack', 'Historical Malware Analysis DNS Name', 'Historically Detected Malware Operation', 'Historically Detected Cryptocurrency Mining Techniques', 'Blacklisted DNS Name', 'Historical Phishing Lure', 'Historically Detected Phishing Techniques', 'Active Phishing URL', 'Recorded Future Predictive Risk Model', 'Historical Punycode Domain', 'Ransomware Distribution URL', 'Ransomware Payment DNS Name', 'Recently Reported by Insikt Group', 'Recent COVID-19-Related Domain Lure - Malicious', 'Recent COVID-19-Related Domain Lure - Suspicious', 'Recently Reported as a Defanged DNS Name', 'Recently Reported by DHS AIS', 'Recently Reported Fraudulent Content', 'Recently Linked to Cyber Attack', 'Recent Malware Analysis DNS Name', 'Recently Detected Malware Operation', 'Recently Detected Cryptocurrency Mining Techniques', 'Recent Phishing Lure - Malicious', 'Recent Phishing Lure - Suspicious', 'Recently Detected Phishing Techniques', 'Recent Punycode Domain', 'Recently Referenced by Insikt Group', 'Recently Reported Spam or Unwanted Content', 'Recent Threat Researcher', 'Recently Active Weaponized Domain', 'Recently Defaced Site', 'Historically Referenced by Insikt Group', 'Recently Resolved to Malicious IP', 'Recently Resolved to Suspicious IP', 'Recently Resolved to Unusual IP', 'Recently Resolved to Very Malicious IP', 'Trending in Recorded Future Analyst Community', 'Historically Reported Spam or Unwanted Content', 'Historical Threat Researcher', 'Historically Active Weaponized Domain']|Active Phishing URL|

Example input:

```
{
  "list": "Active Phishing URL"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|True|Risk list|

Example output:

```
{
  "stix:STIX_Package": {
    "@xmlns:FileObj": "http://example.com",
    "@xmlns:cybox": "http://cybox.mitre.org/cybox-2",
    "@xmlns:indicator": "http://example.com",
    "@xmlns:stix": "http://example.com",
    "@xmlns:stixCommon": "http://example.com",
    "@id": "RF:Package-54aacd87-04f9-41b8-ae7d-f42eb0247d02",
    "@version": "1.2",
    "@xmlns:stixVocabs": "http://example.com",
    "@xmlns:ttp": "http://example.com",
    "stix:Indicators": {
      "stix:Indicator": [
        {
          "indicator:Description": "Current risk: Malicious.Triggers 5 of 46 rules",
          "indicator:Indicated_TTP": [
            {
              "stixCommon:Confidence": {
                "stixCommon:Value": {
                  "#text": "Low",
                  "@xsi:type": "stixVocabs:HighMediumLowVocab-1.0"
                }
              },
              "stixCommon:TTP": {
                "@id": "RF:TTP-9ae8f382-c7be-36c2-86a1-b530694de07c",
                "@timestamp": "2021-03-08T09:20:53.876Z",
                "@xsi:type": "ttp:TTPType",
                "ttp:Description": "1 sighting on 1 source: PhishTank: Phishing Report...",
                "ttp:Title": "Risk Rule: Active Phishing URL"
              }
            },
            {
              "stixCommon:Confidence": {
                "stixCommon:Value": {
                  "#text": "Medium",
                  "@xsi:type": "stixVocabs:HighMediumLowVocab-1.0"
                }
              },
              "stixCommon:TTP": {
                "ttp:Title": "Risk Rule: Recently Resolved to Malicious IP",
                "@id": "RF:TTP-d24a0fba-58c6-3d06-9601-68cf1928a7fb",
                "@timestamp": "2021-03-08T09:20:53.885Z",
                "@xsi:type": "ttp:TTPType",
                "ttp:Description": "From DNS resolution data collected by Recorded Fut..."
              }
            }
          ],
          "indicator:Observable": {
            "@id": "RF:Observable-11bb6be2-4c0a-37fd-b656-f5a1da2d3185",
            "cybox:Object": {
              "@id": "RF:DomainName-13691b17-6e0b-3345-a062-d6a27ac2f616",
              "cybox:Properties": {
                "@type": "FQDN",
                "@xsi:type": "DomainNameObj:DomainNameObjectType",
                "DomainNameObj:Value": {
                  "#text": "groupwhatsappbokp18.wikaba.com",
                  "@condition": "Equals"
                }
              }
            }
          },
          "indicator:Producer": {
            "stixCommon:Description": "Recorded Future",
            "stixCommon:References": {
              "stixCommon:Reference": "http://example.com"
            }
          },
          "indicator:Valid_Time_Position": {
            "indicator:End_Time": {
              "@precision": "second",
              "#text": "2021-03-07T12:29:15.165Z"
            },
            "indicator:Start_Time": {
              "#text": "2021-02-22T23:39:49.769Z",
              "@precision": "second"
            }
          },
          "@xsi:type": "indicator:IndicatorType",
          "@timestamp": "2021-03-08T12:25:06.596Z",
          "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
          "indicator:Confidence": {
            "stixCommon:Description": "Recorded Future Risk Score",
            "stixCommon:Value": "77"
          },
          "indicator:Title": "Domain groupwhatsappbokp18.wikaba.com",
          "indicator:Type": {
            "#text": "Domain Watchlist",
            "@xsi:type": "stixVocabs:IndicatorTypeVocab-1.1"
          },
          "@id": "RF:Indicator-0579d6f3-8f65-3857-826a-ee26c89b5277"
        },
        {
          "@xsi:type": "indicator:IndicatorType",
          "indicator:Confidence": {
            "stixCommon:Value": "77",
            "stixCommon:Description": "Recorded Future Risk Score"
          },
          "indicator:Producer": {
            "stixCommon:Description": "Recorded Future",
            "stixCommon:References": {
              "stixCommon:Reference": "http://example.com"
            }
          },
          "indicator:Type": {
            "@xsi:type": "stixVocabs:IndicatorTypeVocab-1.1",
            "#text": "Domain Watchlist"
          },
          "indicator:Title": "Domain secure-paypal06.servehttp.com",
          "indicator:Valid_Time_Position": {
            "indicator:End_Time": {
              "#text": "2021-03-06T22:51:08.340Z",
              "@precision": "second"
            },
            "indicator:Start_Time": {
              "#text": "2021-02-25T07:48:55.485Z",
              "@precision": "second"
            }
          },
          "@id": "RF:Indicator-7ac5b845-d79a-34da-9eb0-f07d9553808b",
          "@timestamp": "2021-03-08T12:25:06.596Z",
          "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
          "indicator:Description": "Current risk: Malicious.Triggers 5 of 46 rules",
          "indicator:Indicated_TTP": [
            {
              "stixCommon:Confidence": {
                "stixCommon:Value": {
                  "#text": "Low",
                  "@xsi:type": "stixVocabs:HighMediumLowVocab-1.0"
                }
              },
              "stixCommon:TTP": {
                "ttp:Description": "1 sighting on 1 source: PhishTank: Phishing Report...",
                "ttp:Title": "Risk Rule: Active Phishing URL",
                "@id": "RF:TTP-95174e67-d168-34e6-8f95-d54e2734bc32",
                "@timestamp": "2021-03-07T23:08:00.982Z",
                "@xsi:type": "ttp:TTPType"
              }
            },
            {
              "stixCommon:Confidence": {
                "stixCommon:Value": {
                  "#text": "Low",
                  "@xsi:type": "stixVocabs:HighMediumLowVocab-1.0"
                }
              },
              "stixCommon:TTP": {
                "@xsi:type": "ttp:TTPType",
                "ttp:Description": "From DNS resolution data collected by Recorded Fut...",
                "ttp:Title": "Risk Rule: Recently Resolved to Suspicious IP",
                "@id": "RF:TTP-59f917a3-c686-3097-8a9f-cee4394dac38",
                "@timestamp": "2021-03-07T23:08:00.991Z"
              }
            }
          ],
          "indicator:Observable": {
            "cybox:Object": {
              "@id": "RF:DomainName-d9ea6f3f-8707-3f78-8a6b-7c64eba49f10",
              "cybox:Properties": {
                "@type": "FQDN",
                "@xsi:type": "DomainNameObj:DomainNameObjectType",
                "DomainNameObj:Value": {
                  "#text": "secure-paypal06.servehttp.com",
                  "@condition": "Equals"
                }
              }
            },
            "@id": "RF:Observable-30dec8fb-af9e-3de4-b36f-b291804532cf"
          }
        }
      ]
    },
    "@timestamp": "2021-03-08T12:25:06.596Z",
    "@xmlns:cyboxVocabs": "http://example.com",
    "stix:STIX_Header": {
      "stix:Description": "Recorded Future STIX"
    },
    "@xmlns": "http://xml/metadataSharing.xsd",
    "@xmlns:RF": "http://example.com",
    "@xmlns:cyboxCommon": "http://example.com",
    "@xmlns:DomainNameObj": "http://cybox.mitre.org/objects#DomainNameObject-1"
  }
}
```

#### Search Vulnerabilities

This action is used to search for data related to vulnerabilities.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|direction|string|asc|True|Sort results ascending/descending|['asc', 'desc']|asc|
|freetext|string|None|True|Text query|None|example|
|from|number|0|True|Number of initial records to skip|None|0|
|limit|number|None|True|Number of results to retrieve, up to 100|None|10|
|orderby|string|None|True|Which property to sort the results by|['Created', 'Lastseen', 'Firstseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|Riskscore|
|riskRule|string|None|False|Filters the results by risk rule|['Historically Reported by Insikt Group', 'Web Reporting Prior to CVSS Score', 'Cyber Exploit Signal - Critical', 'Cyber Exploit Signal - Important', 'Cyber Exploit Signal - Medium', 'Historical Suspected Exploit/Tool Development in the Wild', 'Historical Observed Exploit/Tool Development in the Wild', 'Historically Exploited in the Wild by Malware', 'Linked to Historical Cyber Exploit', 'Historically Linked to Exploit Kit', 'Historically Linked to Malware', 'Historically Linked to Remote Access Trojan', 'Historically Linked to Ransomware', 'Linked to Recent Cyber Exploit', 'Recently Linked to Exploit Kit', 'Recently Linked to Malware', 'Recently Linked to Remote Access Trojan', 'Recently Linked to Ransomware', 'Exploited in the Wild by Malware', 'NIST Severity - Critical', 'Duplicate of Vulnerability in NVD', 'NIST Severity - High', 'NIST Severity - Low', 'NIST Severity - Medium', 'Web Reporting Prior to NVD Disclosure', 'Historical Unverified Proof of Concept Available', 'Historical Verified Proof of Concept Available', 'Historical Verified Proof of Concept Available Using Remote Execution', 'Recently Reported by Insikt Group', 'Recent Suspected Exploit/Tool Development in the Wild', 'Exploited in the Wild by Recently Active Malware', 'Recent Unverified Proof of Concept Available', 'Recent Verified Proof of Concept Available', 'Recent Verified Proof of Concept Available Using Remote Execution', 'Recently Referenced by Insikt Group', 'Recently Linked to Penetration Testing Tools', 'Historically Referenced by Insikt Group', 'Historically Linked to Penetration Testing Tools']|NIST Severity - Critical|
|riskScore|string|None|False|Filters the results by risk score|None|[1,100]|

Example input:

```
{
  "direction": "asc",
  "freetext": "example",
  "from": 0,
  "limit": 10,
  "orderby": "Riskscore",
  "riskRule": "NIST Severity - Critical",
  "riskScore": "[1,100]"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]vulnerability_search_data|True|Data|

Example output:

```
{
  "data": {
    "results": [
      {
        "entity": {
          "description": "Microsoft .NET Framework 2.0, 3.5, 3.5.1, 4.5.2, 4...",
          "id": "UDtzUu",
          "name": "CVE-2017-8759",
          "type": "CyberVulnerability"
        },
        "timestamps": {
          "firstSeen": "2017-09-12T17:04:02.573Z",
          "lastSeen": "2020-04-05T16:49:09.358Z"
        }
      },
      {
        "entity": {
          "id": "JI5lb_",
          "name": "CVE-2012-0158",
          "type": "CyberVulnerability",
          "description": "The (1) ListView, (2) ListView2, (3) TreeView, and..."
        },
        "timestamps": {
          "lastSeen": "2020-04-06T08:25:41.231Z",
          "firstSeen": "2012-04-10T21:55:01.687Z"
        }
      }
    ]
  },
  "counts": {
    "returned": 10,
    "total": 10
  }
}
```

#### Search IP Addresses

This action is used to for data related to a specified IP range.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|direction|string|asc|True|Sort results ascending/descending|['asc', 'desc']|asc|
|from|number|0|True|Number of initial records to skip|None|0|
|ip_range|string|None|True|IP address range to search|None|198.51.100.0/24|
|limit|number|None|True|Number of results to retrieve, up to 100|None|10|
|orderby|string|None|True|Which property to sort the results by|['Created', 'Lastseen', 'Firstseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|Lastseen|
|riskRule|string|None|False|Filters the results by risk rule|['Threat Actor Used Infrastructure', 'Historically Reported by Insikt Group', 'Inside Possible Bogus BGP Route', 'Historical Botnet Traffic', 'Recently Communicating With C&C Server', 'Nameserver for C&C Server', 'Historical C&C Server', 'Cyber Exploit Signal - Critical', 'Cyber Exploit Signal - Important', 'Cyber Exploit Signal - Medium', 'Recent Host of Many DDNS Names', 'Historically Reported as a Defanged IP', 'Historically Reported by DHS AIS', 'Resolution of Fast Flux DNS Name', 'Historically Reported in Threat List', 'Historical Honeypot Sighting', 'Honeypot Host', 'Recently Active C&C Server', 'Recent C&C Server', 'Historically Linked to Intrusion Method', 'Historically Linked to APT', 'Historically Linked to Cyber Attack', 'Malicious Packet Source', 'Malware Delivery', 'Historical Multicategory Blacklist', 'Historical Open Proxies', 'Phishing Host', 'Historical Positive Malware Verdict', 'Recorded Future Predictive Risk Model', 'Actively Communicating C&C Server', 'Recently Reported by Insikt Group', 'Recent Botnet Traffic', 'Current C&C Server', 'Recently Reported as a Defanged IP', 'Recently Reported by DHS AIS', 'Recent Honeypot Sighting', 'Recently Linked to Intrusion Method', 'Recently Linked to APT', 'Recently Linked to Cyber Attack', 'Recent Multicategory Blacklist', 'Recent Open Proxies', 'Recent Positive Malware Verdict', 'Recently Referenced by Insikt Group', 'Recent Spam Source', 'Recent SSH/Dictionary Attacker', 'Recent Bad SSL Association', 'Recent Threat Researcher', 'Recently Defaced Site', 'Historically Referenced by Insikt Group', 'Trending in Recorded Future Analyst Community', 'Historical Spam Source', 'Historical SSH/Dictionary Attacker', 'Historical Bad SSL Association', 'Historical Threat Researcher', 'Tor Node', 'Unusual IP', 'Vulnerable Host']|Malware Delivery|
|riskScore|string|None|False|Filters the results by risk score|None|[1,100]|

Example input:

```
{
  "direction": "asc",
  "from": 0,
  "ip_range": "198.51.100.0/24",
  "limit": 10,
  "orderby": "Lastseen",
  "riskRule": "Malware Delivery",
  "riskScore": "[1,100]"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]ip_search_data|True|Data|

Example output:

```
{
  "data": {
    "results": [
      {
        "entity": {
          "name": "209.0.0.0/15",
          "type": "IpAddress",
          "id": "ip:209.0.0.0/15"
        },
        "timestamps": {
          "firstSeen": "2020-01-29T10:04:41.359Z",
          "lastSeen": "2020-01-29T10:04:41.359Z"
        }
      },
      {
        "entity": {
          "id": "ip:209.0.0.230",
          "name": "209.0.0.230",
          "type": "IpAddress"
        },
        "timestamps": {
          "firstSeen": "2019-04-27T11:24:53.497Z",
          "lastSeen": "2019-09-22T09:23:53.397Z"
        }
      }
    ]
  },
  "counts": {
    "returned": 10,
    "total": 230
  }
}
```

#### List Vulnerability Risk Rules

This action is used to retrieve available filtration rules for vulnerability risk lists.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_rules|[]risk_rule|True|Risk rules|

Example output:

```
{
  "risk_rules": [
    {
      "count": 4127,
      "criticality": 2,
      "criticalityLabel": "Medium",
      "description": "Historical Verified Proof of Concept Available Usi...",
      "name": "pocVerifiedRemote",
      "relatedEntities": []
    },
    {
      "count": 3,
      "criticality": 3,
      "criticalityLabel": "High",
      "description": "Recent Verified Proof of Concept Available",
      "name": "recentPocVerified",
      "relatedEntities": []
    }
  ]
}
```

#### Download Hash Risk List

This action is used to returns a list of hashes matching a specified risk rule.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|list|string|None|False|The risk list to retrieve, leaving the list parameter blank results in the default risk list|['Historically Reported in Threat List', 'Large', 'Linked to Attack Vector', 'Linked to Cyber Attack', 'Linked to Malware', 'Linked to Vulnerability', 'Malware SSL Certificate Fingerprint', 'Observed in Underground Virus Testing Sites', 'Positive Malware Verdict', 'Recently Active Targeting Vulnerabilities in the Wild', 'Referenced by Insikt Group', 'Reported by DHS AIS', 'Reported by Insikt Group', 'Threat Researcher', 'Trending in Recorded Future Analyst Community']|Positive Malware Verdict|

Example input:

```
{
  "list": "Positive Malware Verdict"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|True|Risk list|

Example output:

```
{
  "risk_list": {
    "stix:STIX_Package": {
      "@id": "RF:Package-83248179-6985-47ad-b182-2e236c81b3f9",
      "@timestamp": "2021-03-17T12:40:03.438Z",
      "@version": "1.2",
      "@xmlns": "http://xml/metadataSharing.xsd",
      "@xmlns:FileObj": "http://example.com",
      "@xmlns:RF": "http://example.com",
      "@xmlns:cybox": "http://cybox.mitre.org/cybox-2",
      "@xmlns:cyboxCommon": "http://example.com",
      "@xmlns:cyboxVocabs": "http://example.com",
      "@xmlns:indicator": "http://example.com",
      "@xmlns:stix": "http://example.com",
      "@xmlns:stixCommon": "http://example.com",
      "@xmlns:stixVocabs": "http://example.com",
      "@xmlns:ttp": "http://example.com",
      "stix:Indicators": {
        "stix:Indicator": [
          {
            "@id": "RF:Indicator-e14a49ac-556b-3358-b2e7-8d3b9e013aa3",
            "@timestamp": "2021-03-17T12:40:03.438Z",
            "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
            "@xsi:type": "indicator:IndicatorType",
            "indicator:Confidence": {
              "stixCommon:Description": "Recorded Future Risk Score",
              "stixCommon:Value": "89"
            },
            "indicator:Description": "Current risk: Malicious.Triggers 7 of 13 rules",
            "indicator:Indicated_TTP": [
              {
                "stixCommon:Confidence": {
                  "stixCommon:Value": {
                    "#text": "Low",
                    "@xsi:type": "stixVocabs:HighMediumLowVocab-1.0"
                  }
                },
                "stixCommon:TTP": {
                  "@id": "RF:TTP-a78cfeaa-e468-3621-831f-5809f8d6f255",
                  "@timestamp": "2021-03-16T00:00:00.000Z",
                  "@xsi:type": "ttp:TTPType",
                  "ttp:Description": "99 sightings on 5 sources: Security Affairs, McAfee, RSA Blogs, US CERT CISA Bulletins, Recorded Future. Most recent link (Mar 16, 2021): https://www.mcafee.com/enterprise/en-us/assets/reports/rp-operation-dianxun.pdf",
                  "ttp:Title": "Risk Rule: Threat Researcher"
                }
              }
            ],
            "indicator:Observable": {
              "@id": "RF:Observable-d61de1d4-568c-33fb-b73e-c67a4640e7b9",
              "cybox:Object": {
                "@id": "RF:File-3bbda3a0-997c-3617-914a-2cdcf6fc42ad",
                "cybox:Properties": {
                  "@xsi:type": "FileObj:FileObjectType",
                  "FileObj:Hashes": {
                    "cyboxCommon:Hash": {
                      "cyboxCommon:Simple_Hash_Value": {
                        "#text": "f34d5f2d4577ed6d9ceec516c1f5a744",
                        "@condition": "Equals"
                      },
                      "cyboxCommon:Type": {
                        "#text": "MD5",
                        "@xsi:type": "cyboxVocabs:HashNameVocab-1.0"
                      }
                    }
                  }
                }
              }
            },
            "indicator:Producer": {
              "stixCommon:Description": "Recorded Future",
              "stixCommon:References": {
                "stixCommon:Reference": "http://example.com"
              }
            },
            "indicator:Title": "MD5-hash f34d5f2d4577ed6d9ceec516c1f5a744",
            "indicator:Type": {
              "#text": "File Hash Watchlist",
              "@xsi:type": "stixVocabs:IndicatorTypeVocab-1.1"
            },
            "indicator:Valid_Time_Position": {
              "indicator:End_Time": {
                "#text": "2021-03-16T21:42:27.746Z",
                "@precision": "second"
              },
              "indicator:Start_Time": {
                "#text": "2014-02-20T07:31:50.884Z",
                "@precision": "second"
              }
            }
          }
        ]
      },
      "stix:STIX_Header": {
        "stix:Description": "Recorded Future STIX"
      }
    }
  }
}
```

#### Search Hashes

This action is used to search for data related to hashes of a specified type.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|algorithm|string|None|True|Hashing algorithm to search by|['MD5', 'SHA-1', 'SHA-256']|SHA-1|
|direction|string|asc|True|Sort results ascending/descending|['asc', 'desc']|asc|
|from|number|0|True|Number of initial records to skip|None|0|
|limit|number|None|True|Number of results to retrieve, up to 100|None|10|
|orderby|string|None|True|Which property to sort the results by|['Created', 'Lastseen', 'Firstseen', 'Modified', 'Riskscore', 'Rules', 'Sevendayshits', 'Sixtydayshits', 'Totalhits']|Riskscore|
|riskRule|string|None|False|Filters the results by risk rule|['Reported by Insikt Group', 'Historically Reported in Threat List', 'Linked to Cyber Attack', 'Linked to Malware', 'Linked to Attack Vector', 'Linked to Vulnerability', 'Malware SSL Certificate Fingerprint', 'Observed in Underground Virus Testing Sites', 'Positive Malware Verdict', 'Recently Active Targeting Vulnerabilities in the Wild', 'Referenced by Insikt Group', 'Trending in Recorded Future Analyst Community', 'Threat Researcher']|Positive Malware Verdict|
|riskScore|string|None|False|Filters the results by risk score|None|[1,100]|

Example input:

```
{
  "algorithm": "SHA-1",
  "direction": "asc",
  "from": 0,
  "limit": 10,
  "orderby": "Riskscore",
  "riskRule": "Positive Malware Verdict",
  "riskScore": "[1,100]"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|[]hash_search_data|True|Data|

Example output:

```
{
  "counts": {
    "returned": 10,
    "total": 78366
  },
  "data": {
    "results": [
      {
        "entity": {
          "id": "hash:c48786b8d8dc9d4ac0764ecb28044135",
          "name": "c48786b8d8dc9d4ac0764ecb28044135",
          "type": "Hash"
        },
        "relatedEntities": [
          {
            "type": "RelatedHash",
            "entities": [
              {
                "count": 4,
                "entity": {
                  "name": "1101a6b0736ad5cb9ed57b0e062248396488545383f9cd2759...",
                  "type": "Hash",
                  "id": "hash:1101a6b0736ad5cb9ed57b0e062248396488545383f9c..."
                }
              },
            ]
          }
        ],
        "risk": {
          "riskSummary": "2 of 12 Risk Rules currently observed.",
          "rules": 2,
          "score": 25,
          "criticality": 2,
          "criticalityLabel": "Suspicious",
          "evidenceDetails": [
            {
              "evidenceString": "1 sighting on 1 source: VirusTotal. Most recent li...",
              "mitigationString": "",
              "rule": "Linked to Malware",
              "timestamp": "2020-02-02T20:07:51.000Z",
              "criticality": 2,
              "criticalityLabel": "Suspicious"
            },
            {
              "criticalityLabel": "Suspicious",
              "evidenceString": "1 sighting on 1 source: VirusTotal. Mitigated by R...",
              "mitigationString": "Mitigated by ReversingLabs reputation.",
              "rule": "Positive Malware Verdict",
              "timestamp": "2020-02-02T00:00:00.000Z",
              "criticality": 2
            }
          ],
          "riskString": "2/12"
        },
        "sightings": [
          {
            "url": "https://www.virustotal.com/gui/file/1101a6b0736ad5...",
            "fragment": "last_seen - 2020-02-02 20:07:51 1101a6b0736ad5cb9e...",
            "published": "2020-02-02T20:07:51.000Z",
            "source": "VirusTotal",
            "title": "Antivirus scan for 1101a6b0736ad5cb9ed57b0e0622483...",
            "type": "first"
          },
          {
            "fragment": "ReversingLabs report for SHA-256 1101a6b0736ad5cb9...",
            "published": "2020-02-01T09:38:05.000Z",
            "source": "ReversingLabs",
            "title": "ReversingLabs scan for SHA-256 1101a6b0736ad5cb9ed...",
            "type": "recentInfoSec",
            "url": "https://a1000.reversinglabs.com/accounts/login/?ne..."
          }
        ],
        "threatLists": [],
        "analystNotes": [],
        "counts": [
          {
            "count": 2,
            "date": "2020-02-01"
          }
        ],
        "hashAlgorithm": "MD5",
        "intelCard": "http://example.com",
        "metrics": [
          {
            "type": "pasteHits",
            "value": 0
          }
        ],
        "timestamps": {
          "firstSeen": "2020-02-03T18:03:49.580Z",
          "lastSeen": "2020-02-09T06:38:12.726Z"
        }
      },
      {
        "analystNotes": [],
        "hashAlgorithm": "MD5",
        "relatedEntities": [
          {
            "entities": [
              {
                "count": 7,
                "entity": {
                  "id": "hash:d7a95886c8dc5021fa4dda5176c59e4f3e590b49efa51...",
                  "name": "d7a95886c8dc5021fa4dda5176c59e4f3e590b49efa510b740...",
                  "type": "Hash"
                }
              }
            ],
            "type": "RelatedHash"
          }
        ],
        "timestamps": {
          "firstSeen": "2019-04-24T08:13:55.161Z",
          "lastSeen": "2019-10-02T19:47:27.938Z"
        },
        "risk": {
          "rules": 2,
          "score": 25,
          "criticality": 2,
          "criticalityLabel": "Suspicious",
          "evidenceDetails": [
            {
              "timestamp": "2019-04-23T19:17:02.000Z",
              "criticality": 2,
              "criticalityLabel": "Suspicious",
              "evidenceString": "1 sighting on 1 source: VirusTotal. Most recent li...",
              "mitigationString": "",
              "rule": "Linked to Malware"
            }
          ],
          "riskString": "2/12",
          "riskSummary": "2 of 12 Risk Rules currently observed."
        },
        "sightings": [
          {
            "type": "mostRecent",
            "url": "https://a1000.reversinglabs.com/accounts/login/?ne...",
            "fragment": "ReversingLabs report for SHA-256 d7a95886c8dc5021f...",
            "published": "2019-04-23T20:20:44.000Z",
            "source": "ReversingLabs",
            "title": "ReversingLabs scan for SHA-256 d7a95886c8dc5021fa4..."
          },
          {
            "fragment": "ReversingLabs report for SHA-256 d7a95886c8dc5021f...",
            "published": "2019-04-23T20:20:44.000Z",
            "source": "ReversingLabs",
            "title": "ReversingLabs scan for SHA-256 d7a95886c8dc5021fa4...",
            "type": "recentInfoSec",
            "url": "https://a1000.reversinglabs.com/accounts/login/?ne..."
          }
        ],
        "threatLists": [],
        "counts": [
          {
            "count": 7,
            "date": "2019-04-23"
          }
        ],
        "entity": {
          "type": "Hash",
          "id": "hash:83fc4b1052f1b8cb9c8da36419a850e1",
          "name": "83fc4b1052f1b8cb9c8da36419a850e1"
        },
        "intelCard": "http://example.com",
        "metrics": [
          {
            "value": 0,
            "type": "pasteHits"
          },
          {
            "type": "darkWebHits",
            "value": 0
          }
        ]
      }
    ]
  }
}
```

#### Lookup Entity List

This action is used to fetch a specified entity list by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|entity_list_id|string|None|True|Entity list ID, obtained from the 'Search Entity lists' action|None|report:Oe5eg5|

Example input:

```
{
  "entity_list_id": "report:Oe5eg5"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entities|[]entity|True|Entities|

Example output:

```
{
  "counts": {
    "returned": 10,
    "total": 2223
  },
  "data": {
    "results": [
      {
        "entity": {
          "id": "url:http://203.172.131.99/personal/?name=download&...",
          "name": "http://203.172.131.99/personal/?name=download&file...",
          "type": "URL"
        }
      },
      {
        "entity": {
          "id": "url:http://188.95.159.100/phpbb/image2/cp.php?i=15",
          "name": "http://188.95.159.100/phpbb/image2/cp.php?i=15",
          "type": "URL"
        }
      }
    ]
  }
}
```

#### Lookup Malware

This action is used to return information about a specific malware entry by ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|malware_ID|string|None|True|Malware ID|None|ShciZX|

Example input:

```
{
  "malware_ID": "ShciZX"
}
```

{
##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|malware_search_data|True|Data|
|result_found|boolean|True|Whether the result was found|

Example output:

```
{
  "result_found": true,
  "data": {
    "analystNotes": [],
    "timestamps": {
      "lastSeen": "2022-02-06T10:48:58.974Z",
      "firstSeen": "2013-09-02T21:10:52.988Z"
    },
    "intelCard": "http://example.com",
    "sightings": [
      {
        "source": "Bank Information Security",
        "url": "https://www.bankinfosecurity.com/leak-reveals-cia-cherryblossom-program-targeting-routers-a-10023",
        "published": "2017-06-19T00:00:00.000Z",
        "fragment": "Previously leaked Vault 7 information, which dated from 2013 to 2016, described programs with such names as AfterMidnight, Athena, Dark Matter, Grasshopper, Hive, Pandemic and Weeping Angel.",
        "type": "recentInfoSec"
      }
    ],
    "entity": {
      "id": "ShciZX",
      "name": "AfterMidnight",
      "type": "Malware"
    },
    "relatedEntities": [
      {
        "entities": [
          {
            "count": 5,
            "entity": {
              "id": "KeKwRK",
              "name": "CWE-20",
              "type": "CyberVulnerability"
            }
          }
        ],
        "type": "RelatedCyberVulnerability"
      }
    ],
    "counts": [
      {
        "date": "2017-07-01",
        "count": 11
      }
    ],
    "metrics": [
      {
        "type": "sevenDaysHits",
        "value": 0
      }
    ]
  }
}
```

#### Lookup Domain

This action is used to return information about a specific domain entry.
It accepts both domains and URLs as input. If a URL is given, it will be stripped to its domain.
For example, `https://www.example.com/path/to/file` will become `www.example.com`.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|False|Add a comment to a domain|None|Domain look up performed by InsightConnect|
|domain|string|None|True|Domain|None|example.com|

Example input:

```
{
  "comment": "Domain look up performed by InsightConnect",
  "domain": "example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|domain_search_data|True|Data|
|result_found|boolean|True|Whether the result was found|

Example output:

```
{
  "result_found": true,
  "data": {
    "analystNotes": [],
    "enterpriseLists": [],
    "risk": {
      "criticalityLabel": "None",
      "riskString": "0/49",
      "rules": 0,
      "criticality": 0,
      "riskSummary": "No Risk Rules are currently observed.",
      "score": 0,
      "evidenceDetails": []
    },
    "intelCard": "http://example.com",
    "sightings": [
      {
        "source": "New Domain Registrations",
        "published": "2017-04-04T00:00:00.000Z",
        "fragment": "The domain example.com has been registered",
        "title": "New domain registration for example.com",
        "type": "first"
      }
    ],
    "entity": {
      "id": "idn:example.com",
      "name": "example.com",
      "type": "InternetDomainName"
    },
    "relatedEntities": [
      {
        "entities": [
          {
            "count": 2,
            "entity": {
              "id": "email:user@example.com",
              "name": "user@example.com",
              "type": "EmailAddress"
            }
          }
        ],
        "type": "RelatedEmailAddress"
      }
    ],
    "timestamps": {
      "lastSeen": "2018-11-26T20:23:12.915Z",
      "firstSeen": "2018-08-03T03:29:57.749Z"
    },
    "threatLists": [],
    "counts": [
      {
        "date": "2017-04-04",
        "count": 2
      }
    ],
    "metrics": [
      {
        "type": "sevenDaysHits",
        "value": 0
      }
    ]
  }
}
```

#### Lookup Hash

This action is used to retrieve information about a specified hash.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|False|Add a comment to a hash|None|Hash look up performed by InsightConnect|
|hash|string|None|True|Hash|None|44d88612fea8a8f36de82e1278abb02f|

Example input:

```
{
  "comment": "Hash look up performed by InsightConnect",
  "hash": "44d88612fea8a8f36de82e1278abb02f"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|hash_search_data|True|Data|
|result_found|boolean|True|Whether the result was found|

Example output:

```
{
  "result_found": true,
  "data": {
    "enterpriseLists": [],
    "risk": {
      "criticalityLabel": "Malicious",
      "riskString": "6/14",
      "rules": 6,
      "criticality": 3,
      "riskSummary": "6 of 14 Risk Rules currently observed.",
      "score": 73,
      "evidenceDetails": [
        {
          "evidenceString": "2 sightings on 1 source: Dancho Danchev's Blog. Most recent link (Apr 29, 2021): https://ddanchev.blogspot.com/2021/04/dancho-danchevs-law-enforcement-and.html",
          "rule": "Threat Researcher",
          "criticality": 1,
          "timestamp": "2021-04-29T17:25:00.000Z",
          "criticalityLabel": "Unusual"
        }
      ]
    },
    "intelCard": "http://example.com",
    "sightings": [
      {
        "source": "PasteBin",
        "url": "https://pastebin.com/ws6iEuJn",
        "published": "2021-10-06T01:02:03.000Z",
        "fragment": "44d88612fea8a8f36de82e1278abb02f",
        "title": "Untitled Paste from Pastebin",
        "type": "recentPaste"
      }
    ],
    "entity": {
      "id": "hash:44d88612fea8a8f36de82e1278abb02f",
      "name": "44d88612fea8a8f36de82e1278abb02f",
      "type": "Hash"
    },
    "relatedEntities": [
      {
        "entities": [
          {
            "count": 6,
            "entity": {
              "id": "0e4eL",
              "name": "Computer virus",
              "type": "MalwareCategory"
            }
          }
        ]
      }
    ],
    "analystNotes": [],
    "hashAlgorithm": "MD5",
    "timestamps": {
      "lastSeen": "2022-03-23T05:51:50.136Z",
      "firstSeen": "2013-10-07T07:56:14.576Z"
    },
    "threatLists": [],
    "counts": [
      {
        "date": "2018-08-21",
        "count": 1
      }
    ],
    "metrics": [
      {
        "type": "sevenDaysHits",
        "value": 0
      }
    ]
  }
}
```

#### Lookup URL

This action is used to retrieve information about a specified URL.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comment|string|None|False|Add a comment to an IP address lookup for Recorded Future|None|URL look up performed by InsightConnect|
|url|string|None|True|URL|None|https://example.com|

Example input:

```
{
  "comment": "URL look up performed by InsightConnect",
  "url": "https://example.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|url_search_data|True|Data|
|result_found|boolean|True|Whether the result was found|

Example output:

```
{
  "result_found": true,
  "data": {
    "analystNotes": [],
    "enterpriseLists": [],
    "timestamps": {
      "lastSeen": "2022-02-03T23:59:59.000Z",
      "firstSeen": "2022-02-03T00:00:00.000Z"
    },
    "risk": {
      "criticalityLabel": "None",
      "riskString": "0/28",
      "rules": 0,
      "criticality": 0,
      "riskSummary": "No Risk Rules are currently observed.",
      "score": 0,
      "evidenceDetails": [
        {
          "evidenceString": "1 sighting on 1 source: External Sensor Data Analysis. No risk observed from an endpoint agent via global telemetry. Last checked: Feb 3, 2022.",
          "rule": "No Risk Observed",
          "criticality": 0,
          "timestamp": "2022-02-03T21:32:02.386Z",
          "criticalityLabel": "None"
        }
      ]
    },
    "sightings": [],
    "entity": {
      "id": "url:https://example.com",
      "name": "https://example.com",
      "type": "URL"
    },
    "relatedEntities": [],
    "counts": [],
    "metrics": [
      {
        "type": "oneDayHits",
        "value": 0
      }
    ]
  }
}
```

#### Download IP Addresses Risk List

This action is used to fetch a risk list of the IP addresses that match a specified filtration rule.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|list|string|None|False|The risk list to retrieve, leaving the list parameter blank results in the default risk list|['Threat Actor Used Infrastructure', 'Historically Reported by Insikt Group', 'Inside Possible Bogus BGP Route', 'Historical Botnet Traffic', 'Recently Communicating With C&C Server', 'Nameserver for C&C Server', 'Historical C&C Server', 'Cyber Exploit Signal - Critical', 'Cyber Exploit Signal - Important', 'Cyber Exploit Signal - Medium', 'Recent Host of Many DDNS Names', 'Historically Reported as a Defanged IP', 'Historically Reported by DHS AIS', 'Resolution of Fast Flux DNS Name', 'Historically Reported in Threat List', 'Historical Honeypot Sighting', 'Large', 'Honeypot Host', 'Recently Active C&C Server', 'Recent C&C Server', 'Historically Linked to Intrusion Method', 'Historically Linked to APT', 'Historically Linked to Cyber Attack', 'Malicious Packet Source', 'Malware Delivery', 'Historical Multicategory Blacklist', 'Historical Open Proxies', 'Phishing Host', 'Historical Positive Malware Verdict', 'Recorded Future Predictive Risk Model', 'Actively Communicating C&C Server', 'Recently Reported by Insikt Group', 'Recent Botnet Traffic', 'Current C&C Server', 'Recently Reported as a Defanged IP', 'Recently Reported by DHS AIS', 'Recent Honeypot Sighting', 'Recently Linked to Intrusion Method', 'Recently Linked to APT', 'Recently Linked to Cyber Attack', 'Recent Multicategory Blacklist', 'Recent Open Proxies', 'Recent Positive Malware Verdict', 'Recently Referenced by Insikt Group', 'Recent Spam Source', 'Recent SSH/Dictionary Attacker', 'Recent Bad SSL Association', 'Recent Threat Researcher', 'Recently Defaced Site', 'Historically Referenced by Insikt Group', 'Trending in Recorded Future Analyst Community', 'Historical Spam Source', 'Historical SSH/Dictionary Attacker', 'Historical Bad SSL Association', 'Historical Threat Researcher', 'Tor Node', 'Unusual IP', 'Vulnerable Host']|Malware Delivery|

Example input:

```
{
  "list": "Malware Delivery"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|True|Risk list|

Example output:

```
{
  "stix:STIX_Package": {
    "@xmlns": "http://xml/metadataSharing.xsd",
    "@xmlns:indicator": "http://example.com",
    "@xmlns:stix": "http://example.com",
    "@xmlns:ttp": "http://example.com",
    "stix:STIX_Header": {
      "stix:Description": "Recorded Future STIX"
    },
    "@id": "RF:Package-9144eafb-a082-49d1-97a1-e7ceb4d8e955",
    "@timestamp": "2020-04-01T12:10:12.058Z",
    "@xmlns:FileObj": "http://example.com",
    "@xmlns:stixCommon": "http://example.com",
    "stix:Indicators": {
      "stix:Indicator": [
        {
          "@timestamp": "2020-04-06T16:10:17.739Z",
          "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
          "@xsi:type": "indicator:IndicatorType",
          "indicator:Description": "Current risk: Suspicious.Triggers 1 of 51 rules",
          "indicator:Indicated_TTP": {
            "stixCommon:Confidence": {
              "stixCommon:Value": {
                "#text": "Medium",
                "@xsi:type": "stixVocabs:HighMediumLowVocab-1.0"
              }
            },
            "stixCommon:TTP": {
              "ttp:Title": "Risk Rule: Current C&C Server",
              "@id": "RF:TTP-42014977-2178-3d3e-b3d1-a3d39961ebca",
              "@timestamp": "2020-04-04T17:31:26.032Z",
              "@xsi:type": "ttp:TTPType",
              "ttp:Description": "1 sighting on 1 source: Cobalt Strike Default Cert..."
            }
          },
          "indicator:Observable": {
            "@id": "RF:Observable-19894357-b884-3cd8-bd49-54540862a4a0",
            "cybox:Object": {
              "@id": "RF:Address-81ec9700-57ba-3f8d-aeb9-f00418d5f31c",
              "cybox:Properties": {
                "@category": "ipv4-addr",
                "@xsi:type": "AddressObj:AddressObjectType",
                "AddressObj:Address_Value": {
                  "#text": "3.10.20.157",
                  "@condition": "Equals"
                }
              }
            }
          },
          "indicator:Producer": {
            "stixCommon:References": {
              "stixCommon:Reference": "http://example.com"
            },
            "stixCommon:Description": "Recorded Future"
          },
          "indicator:Type": {
            "#text": "IP Watchlist",
            "@xsi:type": "stixVocabs:IndicatorTypeVocab-1.1"
          },
          "@id": "RF:Indicator-02ff9864-3b18-332c-be33-35449baed75a",
          "indicator:Confidence": {
            "stixCommon:Description": "Recorded Future Risk Score",
            "stixCommon:Value": "25"
          },
          "indicator:Title": "IP Address 3.10.20.157",
          "indicator:Valid_Time_Position": {
            "indicator:Start_Time": {
              "#text": "2020-04-04T00:00:00.000Z",
              "@precision": "second"
            },
            "indicator:End_Time": {
              "#text": "2020-04-04T23:59:59.000Z",
              "@precision": "second"
            }
          }
        },
        {
          "@timestamp": "2020-04-06T16:10:17.739Z",
          "@xsi:type": "indicator:IndicatorType",
          "indicator:Observable": {
            "@id": "RF:Observable-72d63012-ab31-3324-b994-1dc391fe9299",
            "cybox:Object": {
              "@id": "RF:Address-7aa0590a-8d24-36cc-aee3-a93d4200b564",
              "cybox:Properties": {
                "@category": "ipv4-addr",
                "@xsi:type": "AddressObj:AddressObjectType",
                "AddressObj:Address_Value": {
                  "#text": "5.34.180.206",
                  "@condition": "Equals"
                }
              }
            }
          },
          "indicator:Producer": {
            "stixCommon:Description": "Recorded Future",
            "stixCommon:References": {
              "stixCommon:Reference": "http://example.com"
            }
          },
          "@id": "RF:Indicator-eafa3166-7abc-33af-8789-ede692bf230a",
          "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
          "indicator:Confidence": {
            "stixCommon:Value": "96",
            "stixCommon:Description": "Recorded Future Risk Score"
          },
          "indicator:Description": "Current risk: Very Malicious.Triggers 3 of 51 rule...",
          "indicator:Indicated_TTP": [
            {
              "stixCommon:Confidence": {
                "stixCommon:Value": {
                  "#text": "Low",
                  "@xsi:type": "stixVocabs:HighMediumLowVocab-1.0"
                }
              },
              "stixCommon:TTP": {
                "@xsi:type": "ttp:TTPType",
                "ttp:Description": "Previous sightings on 1 source: Cobalt Strike Defa...",
                "ttp:Title": "Risk Rule: Historically Reported in Threat List",
                "@id": "RF:TTP-538a4df0-0f1f-3a66-82c1-2bb9f030d044",
                "@timestamp": "2020-04-04T18:49:02.868Z"
              }
            },
            {
              "stixCommon:Confidence": {
                "stixCommon:Value": {
                  "#text": "High",
                  "@xsi:type": "stixVocabs:HighMediumLowVocab-1.0"
                }
              },
              "stixCommon:TTP": {
                "@id": "RF:TTP-373ddb7d-61ac-36a4-8f30-31e2650ea421",
                "@timestamp": "2020-01-11T08:02:27.884Z",
                "@xsi:type": "ttp:TTPType",
                "ttp:Description": "1 sighting on 1 source: Recorded Future Command & ...",
                "ttp:Title": "Risk Rule: Current C&C Server"
              }
            }
          ],
          "indicator:Title": "IP Address 5.34.180.206",
          "indicator:Type": {
            "#text": "IP Watchlist",
            "@xsi:type": "stixVocabs:IndicatorTypeVocab-1.1"
          },
          "indicator:Valid_Time_Position": {
            "indicator:End_Time": {
              "#text": "2020-01-11T08:02:27.884Z",
              "@precision": "second"
            },
            "indicator:Start_Time": {
              "#text": "2020-01-11T08:02:27.884Z",
              "@precision": "second"
            }
          }
        }
      ]
    },
    "@xmlns:RF": "http://example.com",
    "@xmlns:cybox": "http://cybox.mitre.org/cybox-2",
    "@xmlns:cyboxCommon": "http://example.com",
    "@xmlns:stixVocabs": "http://example.com",
    "@version": "1.2",
    "@xmlns:AddressObj": "http://cybox.mitre.org/objects#AddressObject-2",
    "@xmlns:cyboxVocabs": "http://example.com"
  }
}
```

#### Lookup IP Address

This action is used to query for data related to a specific IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|IP_address|string|None|True|IP address|None|198.51.100.100|
|comment|string|None|False|Add comment to IP address lookup for Recorded Future|None|IP look up performed by InsightConnect|

Example input:

```
{
  "IP_address": "198.51.100.100",
  "comment": "IP look up performed by InsightConnect"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|ip_search_data|True|Data|
|result_found|boolean|True|Whether the result was found|

Example output:

```
{
  "result_found": true,
  "data": {
    "riskyCIDRIPs": [],
    "enterpriseLists": [],
    "risk": {
      "criticalityLabel": "Suspicious",
      "riskString": "11/64",
      "rules": 11,
      "criticality": 2,
      "riskSummary": "11 of 64 Risk Rules currently observed.",
      "score": 58,
      "evidenceDetails": [
        {
          "evidenceString": "149 sightings on 18 sources including: Acunetix Web Application Security Blog, Recorded Future Malware Detonation, binarydefense.com, HackerOne Hacktivity, ehcgroup.io. 18 related intrusion methods including POS Malware, Source Address Spoofing, DNS Spoofing, njRAT, Mozart. Most recent tweet: @engage_vdms @edgecast @verizondigital https://t.co/65QIJaVmkr reserved https://t.co/uWt2rpURVy resolving to 93.184.216.34 as Adware or spyware by @zscaler (URL: https://t.co/pd3PacufyS ). Most recent link (Jun 25, 2019): https://twitter.com/npandraju/statuses/1143466069803196416",
          "rule": "Historically Linked to Intrusion Method",
          "criticality": 1,
          "timestamp": "2019-06-25T10:28:50.000Z",
          "criticalityLabel": "Unusual"
        }
      ]
    },
    "intelCard": "http://example.com",
    "sightings": [
      {
        "source": "PasteBin",
        "url": "http://pastebin.com/bDJ7rarf",
        "published": "2014-12-16T18:49:06.000Z",
        "fragment": "ip.addr == 93.184.216.34",
        "title": "Untitled",
        "type": "first"
      }
    ],
    "entity": {
      "id": "ip:198.51.100.100",
      "name": "198.51.100.100",
      "type": "IpAddress"
    },
    "relatedEntities": [
      {
        "entities": [
          {
            "count": 85,
            "entity": {
              "id": "0fL5H",
              "name": "Adware",
              "type": "MalwareCategory"
            }
          }
        ],
        "type": "RelatedMalwareCategory"
      },
      {
        "entities": [
          {
            "count": 140,
            "entity": {
              "id": "hash:b71e4d17274636b97179ba2d97c742735b6510eb54f22893d3a2daff2ceb28db",
              "name": "b71e4d17274636b97179ba2d97c742735b6510eb54f22893d3a2daff2ceb28db",
              "type": "Hash"
            }
          }
        ],
        "type": "RelatedProduct"
      }
    ],
    "analystNotes": [],
    "location": {
      "organization": "EdgeCast Networks, Inc.",
      "cidr": {
        "id": "ip:93.184.216.0/24",
        "name": "93.184.216.0/24",
        "type": "IpAddress"
      },
      "location": {
        "continent": "North America",
        "country": "United States"
      },
      "asn": "AS15133"
    },
    "timestamps": {
      "lastSeen": "2022-04-08T10:57:07.595Z",
      "firstSeen": "2014-12-16T18:51:34.533Z"
    },
    "threatLists": [
      {
        "id": "report:TmXa90",
        "name": "Alexa Top 10000 Domains and IP Addresses (White List)",
        "type": "EntityList",
        "description": "This informational list contains the current Alexa Top 10000 Sites, and IP Addresses that have recently been observed by Recorded Future as DNS Name resolutions.IP Address risk scoring uses this list as a evidence of non-maliciousness, but IPs for Alexa Top 500 sites are not categorically whitelisted.DNS resolutions include both IPv4 and IPv6 resolutions, but are not necessarily comprehensive. These DNS Names may resolve to other IP Addresses depending on time and DNS lookup request location.For more information, see support.alexa.com/hc/en-us/articles/200449834-Does-Alexa-have-a-list-of-its-top-ranked-websites-"
      }
    ],
    "counts": [
      {
        "date": "2021-03-26",
        "count": 4
      },
      {
        "date": "2018-01-22",
        "count": 6
      }
    ],
    "metrics": [
      {
        "type": "defangedSightings",
        "value": 15
      },
      {
        "type": "recentBruteForceSightings",
        "value": 1
      }
    ]
  }
}
```

#### Download Vulnerability Risk List

This action is used to fetch a risk list of vulnerabilities matching a specified filtration rule.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|list|string|None|False|The risk list to retrieve, leaving the list parameter blank results in the default risk list|['Historically Reported by Insikt Group', 'Web Reporting Prior to CVSS Score', 'Cyber Exploit Signal - Critical', 'Cyber Exploit Signal - Important', 'Cyber Exploit Signal - Medium', 'Historically Exploited in the Wild by Malware', 'Large', 'Linked to Historical Cyber Exploit', 'Historically Linked to Exploit Kit', 'Historically Linked to Malware', 'Historically Linked to Remote Access Trojan', 'Historically Linked to Ransomware', 'Linked to Recent Cyber Exploit', 'Recently Linked to Exploit Kit', 'Recently Linked to Malware', 'Recently Linked to Remote Access Trojan', 'Recently Linked to Ransomware', 'Exploited in the Wild by Malware', 'NIST Severity - Critical', 'Duplicate of Vulnerability in NVD', 'NIST Severity - High', 'NIST Severity - Low', 'NIST Severity - Medium', 'Web Reporting Prior to NVD Disclosure', 'Historical Unverified Proof of Concept Available', 'Historical Verified Proof of Concept Available', 'Historical Verified Proof of Concept Available Using Remote Execution', 'Recently Reported by Insikt Group', 'Exploited in the Wild by Recently Active Malware', 'Recent Unverified Proof of Concept Available', 'Recent Verified Proof of Concept Available', 'Recent Verified Proof of Concept Available Using Remote Execution', 'Recently Referenced by Insikt Group', 'Recently Linked to Penetration Testing Tools', 'Historically Referenced by Insikt Group', 'Historically Linked to Penetration Testing Tools']|NIST Severity Critical|

Example input:

```
{
  "list": "NIST Severity Critical"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|True|Risk list|

Example output:

```
{
  "stix:STIX_Package": {
    "@xmlns": "http://xml/metadataSharing.xsd",
    "@xmlns:RF": "http://example.com",
    "@xmlns:cybox": "http://cybox.mitre.org/cybox-2",
    "@xmlns:et": "http://example.com",
    "@xmlns:stix": "http://example.com",
    "@xmlns:stixCommon": "http://example.com",
    "stix:Exploit_Targets": {
      "stixCommon:Exploit_Target": [
        {
          "@id": "RF:et-f786d327-c403-3a5a-92c9-cc4678f6289a",
          "@timestamp": "2020-04-06T16:04:47.047Z",
          "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
          "@xsi:type": "et:ExploitTargetType",
          "et:Description": "(Risk Score: 89. Risk Rules: Linked to Historical ...",
          "et:Title": "Vulnerability CVE-2020-6819",
          "et:Vulnerability": {
            "et:CVE_ID": "CVE-2020-6819",
            "et:References": {
              "stixCommon:Reference": "http://example.com"
            }
          }
        },
        {
          "et:Vulnerability": {
            "et:CVE_ID": "CVE-2020-6820",
            "et:References": {
              "stixCommon:Reference": "http://example.com"
            }
          },
          "@id": "RF:et-159738b9-a6c0-3ff8-bef1-fdc9b8a66491",
          "@timestamp": "2020-04-06T16:06:54.652Z",
          "@xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
          "@xsi:type": "et:ExploitTargetType",
          "et:Description": "(Risk Score: 89. Risk Rules: Linked to Historical ...",
          "et:Title": "Vulnerability CVE-2020-6820"
        }
      ]
    },
    "@id": "RF:Package-0db848e9-1de9-4605-b3b3-1bfe6dfc8721",
    "stix:STIX_Header": {
      "stix:Description": "Recorded Future STIX"
    },
    "@version": "1.2",
    "@timestamp": "2020-04-01T12:45:02.780Z"
  }
}
```

#### List Hash Risk Rules

This action is used to list available filtration rules for hash risk lists.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_rules|[]risk_rule|True|Risk rules|

Example output:

```
{
  "risk_rules": [
    {
      "name": "recentActiveMalware",
      "relatedEntities": [
        "aHTyRv"
      ],
      "count": 16164,
      "criticality": 3,
      "criticalityLabel": "Malicious",
      "description": "Recently Active Targeting Vulnerabilities in the W..."
    },
    {
      "criticality": 3,
      "criticalityLabel": "Malicious",
      "description": "Observed in Underground Virus Testing Sites",
      "name": "observedMalwareTesting",
      "relatedEntities": [],
      "count": 1158
    }
  ]
}
```

#### Lookup Vulnerability

This action is used to fetch information about a specific vulnerability by CVE or RF ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|CVE or RF ID|None|CVE-2014-0160|

Example input:

```
{
  "id": "CVE-2014-0160"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|data|vulnerability_search_data|True|Data|
|result_found|boolean|True|Whether the result was found|

Example output:

```
{
  "result_found": true,
  "data": {
    "timestamps": {
      "firstSeen": "2017-03-14T16:59:26.413Z",
      "lastSeen": "2020-04-06T10:05:19.883Z"
    },
    "entity": {
      "description": "The SMBv1 server in Microsoft Windows Vista SP2; W...",
      "id": "S0eb_5",
      "name": "CVE-2017-0147",
      "type": "CyberVulnerability"
    },
    "nvdDescription": "Microsoft PowerPoint 2007 SP3, Word 2007 SP3, PowerPoint 2010 SP2, Word 2010 SP2, PowerPoint 2013 SP1, Word 2013 SP1, and PowerPoint 2013 RT SP1 allow remote attackers to execute arbitrary code or cause a denial of service (memory corruption) via a crafted Office document, aka \"Microsoft Office Memory Corruption Vulnerability.\"",
    "cvss": {
      "accessVector": "NETWORK",
      "lastModified": "2018-10-12T22:09:00.000Z",
      "published": "2015-07-14T21:59:00.000Z",
      "score": 9.3,
      "availability": "COMPLETE",
      "confidentiality": "COMPLETE",
      "version": "2.0",
      "authentication": "NONE",
      "accessComplexity": "MEDIUM",
      "integrity": "COMPLETE"
    },
    "commonNames": [],
    "cvssv3": {},
    "intelCard": "http://example.com",
    "rawrisk": [
      {
        "rule": "linkedToCyberExploit",
        "timestamp": "2017-01-09T20:10:40.000Z"
      },
      {
        "rule": "linkedToIntrusionMethod",
        "timestamp": "2016-10-25T00:00:00.000Z"
      }
    ],
    "metrics": [
      {
        "type": "darkWebHits",
        "value": 15
      },
      {
        "type": "trendVolume",
        "value": 1
      },
      {
        "type": "whitlistedCount",
        "value": 0
      }
    ],
    "cpe": [
      "cpe:2.3:a:microsoft:powerpoint:2013:sp1:*:*:*:*:*:*",
      "cpe:2.3:a:microsoft:powerpoint:2010:sp2:*:*:*:*:*:*",
      "cpe:2.3:a:microsoft:powerpoint:2013:sp1:*:*:rt:*:*:*",
      "cpe:2.3:a:microsoft:word:2013:sp1:*:*:*:*:*:*",
      "cpe:2.3:a:microsoft:word:2007:sp3:*:*:*:*:*:*",
      "cpe:2.3:a:microsoft:powerpoint:2007:sp3:*:*:*:*:*:*",
      "cpe:2.3:a:microsoft:word:2013:sp1:*:*:*:*:x64:*",
      "cpe:2.3:a:microsoft:word:2010:sp2:*:*:*:x64:*:*",
      "cpe:2.3:a:microsoft:word:2013:sp1:*:*:rt:*:*:*",
      "cpe:2.3:a:microsoft:word:2010:sp2:*:*:*:x86:*:*"
    ],
    "analystNotes": [
      {
        "source": {
          "id": "xxxxxx",
          "name": "Example Group",
          "type": "Source"
        },
        "attributes": {
          "validated_on": "2018-07-16T04:00:00.000Z",
          "published": "2018-07-16T04:00:00.000Z",
          "text": "These are notes about the exploit.",
        }
      }
    }
  }
}
```

### Triggers

#### Get New Alerts

This trigger is used to get new alerts.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|frequency|int|10|True|Frequency (in seconds)|None|10|

Example input:

```
{
  "frequency": 10
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alert|alert|True|Alert|

Example output:

```
{
  "alert": {
    "review": {
      "status": "no-action"
    },
    "url": "https://app.recordedfuture.com/live/sc/notification/?id=fnbTO7",
    "rule": {
      "url": "https://app.recordedfuture.com/live/sc/ViewIdkobra_view_report_item_alert_editor?view_opts=%7B%22reportId%22%3A%22feScJA%22%2C%22bTitle%22%3Atrue%2C%22title%22%3A%22Global+Vulnerability+Risk%2C+Vulnerabilities%2C+New+Exploit+Chatter%22%7D&state.bNavbar=false",
      "name": "Global Vulnerability Risk, Vulnerabilities, New Exploit Chatter",
      "id": "deXcBA"
    },
    "triggered": "2020-10-09T16:08:21.948Z",
    "id": "deZcB9",
    "title": "Global Vulnerability Risk, Vulnerabilities, New Exploit Chatter - ... is n...",
    "type": "ENTITY"
  }
}
```

### Custom Output Types

#### alert

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Counts|counts|False|Counts|
|Entities|[]entities|False|Entities|
|ID|string|False|ID|
|Review|review|False|Review|
|Rule|rule|False|Rule|
|Title|string|False|Title|
|Triggered|string|False|Triggered|
|Type|string|False|Type|
|URL|string|False|URL|

#### analystNote

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Attributes|attributes|False|Attributes|
|ID|string|False|ID|
|Source|labels|False|Source|

#### attributes

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Context Entities|[]context_entities|False|Context entities|
|Labels|[]labels|False|Labels|
|Note Entities|[]labels|False|Note entities|
|Published|string|False|Published|
|Text|string|False|Text|
|Title|string|False|Title|
|Title|context_entities|False|Title|
|Validated On|string|False|Validated on|
|Validation URLs|[]labels|False|Validation URLs|

#### CIDR

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|ID|
|Name|string|False|Name|
|Type|string|False|Type|

#### context_entities

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Description|string|False|Description|
|ID|string|False|ID|
|Name|string|False|Name|
|Type|string|False|Type|

#### counts

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Count|integer|False|Count|
|Date|string|False|Date|

#### CVSS

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Access Complexity|string|False|Access complexity|
|Access Vector|string|False|Access vector|
|Authentication|string|False|Authentication|
|Availability|string|False|Availability|
|Confidentiality|string|False|Confidentiality|
|Integrity|string|False|Integrity|
|Last Modified|string|False|Last modified|
|Published|string|False|Published|
|Score|float|False|Score|
|Version|string|False|Version|

#### cvssv3

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Attack Complexity|string|False|Attack complexity|
|Attack Vector|string|False|Attack vector|

#### domain_search_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Analyst Notes|[]analystNote|False|Notes from an analyst|
|Counts|[]counts|False|Counts|
|Enterprise Lists|[]enterpriseLists|False|Enterprise lists|
|Entity|entity|False|Entity|
|Intel Card|string|False|Intel card|
|Metrics|[]metrics|False|Metrics|
|Related Entities|[]relatedEntities|False|Related entities|
|Risk|risk|False|Risk|
|Sightings|[]sightings|False|Sightings|
|Threat Lists|[]threatLists|False|Threat lists|
|Timestamps|timestamps|False|Timestamps|

#### enterpriseLists

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Added|string|False|Added|
|List|list|False|List|

#### entities

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Count|integer|False|Count|
|Entity|entity|False|Entity|

#### entity

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Description|string|False|Description|
|ID|string|False|ID|
|Name|string|False|Name|
|Type|string|False|Type|

#### evidenceDetails

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Criticality|number|False|Criticality|
|Criticality Label|string|False|Criticality label|
|Evidence String|string|False|Evidence string|
|Rule|string|False|Rule|
|Timestamp|string|False|Timestamp|

#### hash_search_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Analyst Notes|[]analystNote|False|Notes from an analyst|
|Counts|[]counts|False|Counts|
|Enterprise Lists|[]enterpriseLists|False|Enterprise lists|
|Entity|entity|False|Entity|
|Hash Algorithm|string|False|Hash algorithm|
|Intel Card|string|False|Intel card|
|Metrics|[]metrics|False|Metrics|
|Related Entities|[]relatedEntities|False|Related entities|
|Risk|risk|False|Risk|
|Sightings|[]sightings|False|Sightings|
|Threat Lists|[]threatLists|False|Threat lists|
|Timestamps|timestamps|False|Timestamps|

#### IP

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|ID|
|Name|string|False|Name|
|Type|string|False|Type|

#### ip_search_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Analyst Notes|[]analystNote|False|Notes from an analyst|
|Counts|[]counts|False|Counts|
|Enterprise Lists|[]enterpriseLists|False|Enterprise lists|
|Entity|entity|False|Entity|
|Intel Card|string|False|Intel card|
|Location|location|False|Location|
|Metrics|[]metrics|False|Metrics|
|Related Entities|[]relatedEntities|False|Related entities|
|Risk|risk|False|Risk|
|Risky CIDR IPs|[]riskyCIDRIP|False|Risky CIDR IPs|
|Sightings|[]sightings|False|Sightings|
|Threat Lists|[]threatLists|False|Threat lists|
|Timestamps|timestamps|False|Timestamps|

#### labels

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|ID|
|Name|string|False|Name|
|Type|string|False|Type|

#### list

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|ID|
|Name|string|False|Name|
|Type|string|False|Type|

#### location

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ASN|string|False|ASN|
|CIDR|cidr|False|Classless Inter-Domain Routing|
|Location|location_data|False|Location|
|Organization|string|False|Organization|

#### location_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|City|string|False|City|
|Continent|string|False|Continent|
|Country|string|False|Country|

#### malware_search_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Analyst Notes|[]analystNote|False|Notes from an analyst|
|Counts|[]counts|False|Counts|
|Entity|entity|False|Entity|
|Intel Card|string|False|Intel card|
|Metrics|[]metrics|False|Metrics|
|Related Entities|[]relatedEntities|False|Related entities|
|Sightings|[]sightings|False|Sightings|
|Timestamps|timestamps|False|Timestamps|

#### metrics

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Type|string|False|Type|
|Value|float|False|Value|

#### rawrisk

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Rule|string|False|Rule|
|Timestamp|string|False|Timestamp|

#### relatedEntities

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Entities|[]entities|False|Entities|
|Type|string|False|Type|

#### review

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Status|string|False|Status|

#### risk

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Criticality|number|False|Criticality|
|Criticality Label|string|False|Criticality label|
|Evidence Details|[]evidenceDetails|False|Evidence details|
|Risk Summary|string|False|Risk summary|
|Rules|integer|False|Rules|
|Score|integer|False|Score|

#### risk_rule

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Criticality|number|False|Criticality|
|Criticality Label|string|False|Criticality label|
|Description|string|False|Description|
|Name|string|False|Name|

#### riskyCIDRIP

|Name|Type|Required|Description|
|----|----|--------|-----------|
|IP|ip|False|IP|
|Score|integer|False|Score|

#### rule

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|ID|
|Name|string|False|Name|
|URL|string|False|URL|

#### sightings

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Fragment|string|False|Fragment|
|Published|string|False|Published|
|Source|string|False|Source|
|Title|string|False|Title|
|Type|string|False|Type|
|URL|string|False|URL|

#### threatLists

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Description|string|False|Description|
|ID|string|False|ID|
|Name|string|False|Name|
|Type|string|False|Type|

#### timestamps

|Name|Type|Required|Description|
|----|----|--------|-----------|
|First Seen|string|False|First seen|
|Last Seen|string|False|Last seen|

#### url_search_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Analyst Notes|[]analystNote|False|Notes from an analyst|
|Counts|[]counts|False|Counts|
|Enterprise Lists|[]enterpriseLists|False|Enterprise lists|
|Entity|entity|False|Entity|
|Metrics|[]metrics|False|Metrics|
|Related Entities|[]relatedEntities|False|Related entities|
|Risk|risk|False|Risk|
|Sightings|[]sightings|False|Sightings|
|Timestamps|timestamps|False|Timestamps|

#### vulnerability_search_data

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Analyst Notes|[]analystNote|False|Analyst notes|
|Common Names|[]string|False|Common names|
|Counts|[]counts|False|Counts|
|CPE|[]string|False|CPE|
|CVSS|cvss|False|CVSS|
|CVSSV3|cvssv3|False|CVSSV3|
|Entity|entity|False|Entity|
|Intel Card|string|False|Intel card|
|Metrics|[]metrics|False|Metrics|
|NVD Description|string|False|NVD description|
|Rawrisk|[]rawrisk|False|Rawrisk|
|Related Entities|[]relatedEntities|False|Related entities|
|Related Links|[]string|False|Related links|
|Risk|risk|False|Risk|
|Sightings|[]sightings|False|Sightings|
|Threat Lists|[]threatLists|False|Threat lists|
|Timestamps|timestamps|False|Timestamps|

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 6.0.1 - Update Pyyaml to version 6.0.0
* 6.0.0 - Handle 404 Not Found Error | Create unit_tests | Update example outputs in help.md | Update keywords | Update key features
* 5.0.1 - Update error handling around a domain that is not found in Lookup Domain
* 5.0.0 - Rewrite all API calls and move them to api.py | Improve error handling | Add more user-friendly cause and assistance messaging using PluginException | Add missing Input, Output, and Component imports and use them in actions | Add the `riskRuleMap` parameter for the Download Risk List actions | Move the `fields` and `riskRuleMap` parameters from actions to util.py | Remove unused `risklist` parameter from the List Risk Rules actions | Remove private variables from the Search actions | Update the available values for the `list` parameter for the Download Risk List actions in plugin.spec.yaml | Add missing titles for input and output parameters for actions in plugin.spec.yaml | Remove blank input from the List Risk Rules actions in plugin.spec.yaml | Add missing titles and descriptions for parameters in custom types | Update custom types for action outputs | Remove unnecessary quotes and new lines from plugin.spec.yaml | Update Python version in Dockerfile | Add USER nobody in Dockerfile | Update xmltodict in requirements.txt | Remove rfapi from requirements.txt | Add output example for the Download Domain Risk List and Download Hash Risk List actions | Add custom types in help.md
* 4.0.4 - Fix issue where Lookup Domain could corrupt non-common domain name extensions
* 4.0.3 - Update Lookup Domain action to accept HTTP and HTTPS URLs as input
* 4.0.2 - Return full `analystNotes` and `threatLists` data outputs in Lookup Domain action
* 4.0.1 - Improve connection error messaging
* 4.0.0 - Remove `fields` input in Lookup Domain, Lookup Hash, Lookup IP Address and Lookup URL actions - all fields will now be returned
* 3.1.2 - Update to request headers to add plugin information
* 3.1.1 - Fix issue where Lookup Alert was returning a generic object
* 3.1.0 - New trigger Get New Alerts
* 3.0.0 - Add input `fields` to Search Domains, Search Hashes, Search IP Addresses, Search Vulnerabilities, Search Malware and Lookup Malware actions | Add `riskRule` and `riskScore` filter criteria to Search Domains, Search Hashes, Search IP Addresses and Search Vulnerabilities actions | Add `list` and `firstSeen` filter criteria to Search Malware action | Update description for `list` parameter in Download IP Addresses Risk List, Download Vulnerability Risk List, Download Domain Risk List and Download Hash Risk List actions
* 2.2.0 - New actions Search URLs, Download URL Risk List and List URL Risk Rules | Update Recorded Future logo | Allow both upper and lowercase CVE in Lookup Vulnerability action
* 2.1.0 - New action Lookup Alert
* 2.0.1 - Add CPE, Analyst Notes, and Related Entities to Lookup Vulnerability action output
* 2.0.0 - Add risk output to Lookup Vulnerability
* 1.5.5 - Fix NoneType has no len() | Fix enums in search hashes
* 1.5.4 - Add example inputs | Fix schema bug where `criticality` output was improperly defined as an integer in List Domain Risk Rules, List Hash Risk Rules, List IP Addresses Risk Rules and List Vulnerability Risk Rules actions
* 1.5.3 - New spec and help.md format for the Extension Library
* 1.5.2 - Fix issue where timestamp for evidenceDetails was set to integer, timestamp is now expected as datetime from RecordedFuture
* 1.5.1 - Fix issue where parameter timestamp in evidenceDetails was set as a string in Lookup IP Address action, timestamp is now an integer
* 1.5.0 - Add support for handling IP addresses not found for action Lookup IP Address | Add found parameter to  action Lookup IP Address
* 1.4.1 - Add missing output and remove extra output for actions Lookup Hash, Lookup Domain, Lookup IP Address and Lookup URL
* 1.4.0 - New action Lookup URL | Add input comment to actions Lookup Hash and Lookup Domain
* 1.3.0 - Add additional output for action Lookup IP Address | Add input fields to action Lookup IP Address
* 1.2.0 - Add additional output for action Lookup Domain | Add input fields to action Lookup Domain
* 1.1.0 - Add additional output for action Lookup Hash | Add input fields to action Lookup Hash
* 1.0.2 - Fix typo in plugin spec
* 1.0.1 - Support web server mode | Use new credential types
* 1.0.0 - Update to v2 Python plugin architecture
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Recorded Future](https://recordedfuture.com)
* [Recorded Future API](https://api.recordedfuture.com/v2)
