# Description

[Recorded Future](https://www.recordedfuture.com/) arms threat analysts, security operators, and incident
  responders to rapidly connect the dots and reveal unknown threats. Using the Recorded Future plugin for Rapid7
InsightConnect, users can search domain lists, entity lists, and more.

Use Recorded Future within an automation workflow to quickly assist with threat analysis, incident response, and
vulnerability management.

Note: When a plugin action that causes a file to be downloaded is invoked, the file data is parsed internally and
returned in the [STIX](https://stixproject.github.io/about/) format.

# Key Features

* Search domain and IP lists
* Download risk lists
* Lookup and search hashes

# Requirements

* Recorded Future API key

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|API Key|None|9de5069c5afe602b2ea0a04b66beb2c0|

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
|alert|alert|True|Alert Details|

Example output:

```
{
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
                    },
                    {
                      "id": "url:https://www.sesin.at/",
                      "name": "https://www.sesin.at/",
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
            },
            {
              "timestamp": "2020-10-02T00:25:00.000Z",
              "criticalityLabel": "High",
              "evidenceString": "1 sighting on 1 source: Recorded Future Vulnerability Analysis. CVSS v3.1 Score (8.3) calculated using NIST reported CVSS Base Score (9.8) and Recorded Future Temporal Metrics. Base vector string: CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H. Temporal vector string: E:U/RL:X/RC:U. Most recent link (Oct 2, 2020): https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2015-4719",
              "rule": "NIST Severity: High",
              "criticality": 3
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
|list|string|None|False|The risk list to retrieve, left this field blank to retrieve default risk list|['Historically Reported by Insikt Group', 'Compromised URL', 'Historically Reported as a Defanged URL', 'Historically Reported by DHS AIS', 'Historically Reported Fraudulent Content', 'Historically Reported in Threat List', 'Large', 'Historically Detected Malicious Browser Exploits', 'Historically Detected Malware Distribution', 'Historically Detected Cryptocurrency Mining Techniques', 'Historically Detected Phishing Techniques', 'Active Phishing URL', 'Positive Malware Verdict', 'Ransomware Distribution URL', 'Recently Reported by Insikt Group', 'Recently Reported as a Defanged URL', 'Recently Reported by DHS AIS', 'Recently Reported Fraudulent Content', 'Recently Detected Malicious Browser Exploits', 'Recently Detected Malware Distribution', 'Recently Detected Cryptocurrency Mining Techniques', 'Recently Detected Phishing Techniques', 'Recently Referenced by Insikt Group', 'Recently Reported Spam or Unwanted Content', 'Recently Detected Suspicious Content', 'Recently Active URL on Weaponized Domain', 'Historically Referenced by Insikt Group', 'Historically Reported Spam or Unwanted Content', 'Historically Detected Suspicious Content']|Historically Reported by Insikt Group|

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
      "@xmlns:FileObj": "http://cybox.mitre.org/objects#FileObject-2",
      "@xmlns:RF": "http://stix.recordedfuture.com/",
      "@xmlns:URIObj": "http://cybox.mitre.org/objects#URIObject-2",
      "@xmlns:cybox": "http://cybox.mitre.org/cybox-2",
      "@xmlns:cyboxCommon": "http://cybox.mitre.org/common-2",
      "@xmlns:cyboxVocabs": "http://cybox.mitre.org/default_vocabularies-2",
      "@xmlns:indicator": "http://stix.mitre.org/Indicator-2",
      "@xmlns:stix": "http://stix.mitre.org/stix-1",
      "@xmlns:stixCommon": "http://stix.mitre.org/common-1",
      "@xmlns:stixVocabs": "http://stix.mitre.org/default_vocabularies-1",
      "@xmlns:ttp": "http://stix.mitre.org/TTP-1",
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
                "stixCommon:Reference": "https://app.recordedfuture.com/live/sc/entity/url%!A(MISSING)http%!A(MISSING)%!F(MISSING)%!F(MISSING)bolizarsospos.com%!F(MISSING)raph9xccgxt"
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
|riskRule|string|None|False|Risk rule od data|['Historically Reported by Insikt Group', 'C&C URL', 'Compromised URL', 'Historically Reported as a Defanged URL', 'Historically Reported by DHS AIS', 'Historically Reported Fraudulent Content', 'Historically Reported in Threat List', 'Historically Detected Malicious Browser Exploits', 'Historically Detected Malware Distribution', 'Historically Detected Cryptocurrency Mining Techniques', 'Historically Detected Phishing Techniques', 'Active Phishing URL', 'Positive Malware Verdict', 'Ransomware Distribution URL', 'Recently Reported by Insikt Group', 'Recently Reported as a Defanged URL', 'Recently Reported by DHS AIS', 'Recently Reported Fraudulent Content', 'Recently Detected Malicious Browser Exploits', 'Recently Detected Malware Distribution', 'Recently Detected Cryptocurrency Mining Techniques', 'Recently Detected Phishing Techniques', 'Recently Referenced by Insikt Group', 'Recently Reported Spam or Unwanted Content', 'Recently Detected Suspicious Content', 'Recently Active URL on Weaponized Domain', 'Historically Referenced by Insikt Group', 'Historically Reported Spam or Unwanted Content', 'Historically Detected Suspicious Content']|Historically Reported by Insikt Group|
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
|data|search_data|True|Search result|

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
|risk_rules|[]risk_rule|True|Risk Rules for URL|

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
|risk_rules|[]risk_rule|False|Risk Rules|

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
|data|search_data|False|Data|

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
|risk_rules|[]risk_rule|False|Risk Rules|

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
|data|search_data|False|Data|

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
|entities|[]entity|False|Entities|

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
|list|string|None|False|The risk list to retrieve, leaving the list parameter blank results in the default risk list|['active_phishing_url', 'blacklisted_dns_name', 'cc_dns_name', 'cc_nameserver', 'cc_url', 'compromised_url', 'historical_malware_analysis_dns_name', 'historically_linked_to_cyber_attack', 'large', 'ransomware_distribution_url', 'ransomware_payment_dns_name', 'recent_fast_flux_dns_name', 'recent_malware_analysis_dns_name', 'recently_linked_to_cyber_attack', 'recently_resolved_to_host_of_many_ddns_names', 'recently_resolved_to_malicious_ip', 'recently_resolved_to_suspicious_ip', 'recently_resolved_to_unusual_ip', 'recently_resolved_to_very_malicious_ip', 'sinkhole_dns_name', 'typosquat_similarity__dns_sandwich', 'typosquat_similarity__typo_or_homograph']|active_phishing_url|

Example input:

```
{
  "list": "active_phishing_url"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|False|Risk List|

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
|data|vulnerability_search_data|False|Data|

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
|riskRule|string|None|False|Filters the results by risk rule|['Threat Actor Used Infrastructure', 'Historically Reported by Insikt Group', 'Inside Possible Bogus BGP Route', 'Historical Botnet Traffic', 'Nameserver for C&C Server', 'Historical C&C Server', 'Cyber Exploit Signal - Critical', 'Cyber Exploit Signal - Important', 'Cyber Exploit Signal - Medium', 'Recent Host of Many DDNS Names', 'Historically Reported as a Defanged IP', 'Historically Reported by DHS AIS', 'Resolution of Fast Flux DNS Name', 'Historically Reported in Threat List', 'Historical Honeypot Sighting', 'Honeypot Host', 'Recently Active C&C Server', 'Recent C&C Server', 'Historically Linked to Intrusion Method', 'Historically Linked to APT', 'Historically Linked to Cyber Attack', 'Malicious Packet Source', 'Malware Delivery', 'Historical Multicategory Blacklist', 'Historical Open Proxies', 'Phishing Host', 'Historical Positive Malware Verdict', 'Recorded Future Predictive Risk Model', 'Actively Communicating C&C Server', 'Recently Reported by Insikt Group', 'Recent Spam Source', 'Recent SSH/Dictionary Attacker', 'Recent Bad SSL Association', 'Recent Threat Researcher', 'Recently Defaced Site', 'Historically Referenced by Insikt Group', 'Trending in Recorded Future Analyst Community', 'Historical Spam Source', 'Historical SSH/Dictionary Attacker', 'Historical Bad SSL Association', 'Historical Threat Researcher', 'Tor Node', 'Unusual IP', 'Vulnerable Host']|Malware Delivery|
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
|data|search_data|False|Data|

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
|risk_rules|[]risk_rule|False|Risk Rules|

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
|list|string|None|False|The risk list to retrieve, leaving the list parameter blank results in the default risk list|['large', 'linked_to_attack_vector', 'linked_to_cyber_attack', 'linked_to_malware', 'linked_to_vulnerability', 'positive_malware_verdict', 'threat_researcher']|positive_malware_verdict|

Example input:

```
{
  "list": "positive_malware_verdict"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|False|Risk List|

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
|data|search_data|False|Data|

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
        "intelCard": "https://app.recordedfuture.com/live/sc/entity/hash...",
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
        "intelCard": "https://app.recordedfuture.com/live/sc/entity/hash...",
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
|entities|[]entity|False|Entities|

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

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|entity|entity|False|Entity|
|timestamps|timestamps|False|Timestamps|

Example output:

```
{
  "data": {
    "entity": {
      "id": "ShciZX",
      "name": "AfterMidnight",
      "type": "Malware"
    },
    "timestamps": {
      "firstSeen": "2013-09-02T21:10:52.988Z",
      "lastSeen": "2020-03-11T12:10:48.788Z"
    }
  }
}
```

#### Lookup Domain

This action is used to return information about a specific domain entry.

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
|analystNotes|[]string|False|Notes from an analyst|
|counts|[]counts|False|Counts|
|enterpriseLists|[]enterpriseLists|False|Enterprise lists|
|entity|entity|False|Entity|
|intelCard|string|False|Intel card|
|metrics|[]metrics|False|Metrics|
|relatedEntities|[]relatedEntities|False|Related entities|
|risk|risk|False|Risk|
|sightings|[]sightings|False|Sightings|
|threatLists|[]string|False|Threat lists|
|timestamps|timestamps|False|Timestamps|

Example output:

```
{
  "data": {
    "entity": {
      "id": "idn:google.com",
      "name": "google.com",
      "type": "InternetDomainName"
    },
    "timestamps": {
      "firstSeen": "2009-01-23T02:00:08.000Z",
      "lastSeen": "2019-07-25T15:44:00.328Z"
    }
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
|analystNotes|[]string|False|Notes from an analyst|
|counts|[]counts|False|Counts|
|enterpriseLists|[]enterpriseLists|False|Enterprise lists|
|entity|entity|False|Entity|
|hashAlgorithm|string|False|Hash Algorithm|
|intelCard|string|False|Intel card|
|metrics|[]metrics|False|Metrics|
|relatedEntities|[]relatedEntities|False|Related entities|
|risk|risk|False|Risk|
|sightings|[]sightings|False|Sightings|
|threatLists|[]string|False|Threat Lists|
|timestamps|timestamps|False|Timestamps|

Example output:

```
{
  "data": {
    "risk": {
      "criticalityLabel": "Malicious",
      "score": 68,
      "evidenceDetails": [
        {
          "timestamp": "2015-06-17T15:09:38.000Z",
          "criticalityLabel": "Unusual",
          "evidenceString": "3 sightings on 1 source: Kaspersky Securelist and Lab. Most recent link (Jun 17, 2015): https://securelist.ru/blog/issledovaniya/25905/modul-duqu-2-0-soxranyayushhij-prisutstvie-v-seti/",
          "rule": "Threat Researcher",
          "criticality": 1
        },
        {
          "timestamp": "2015-06-17T15:09:38.000Z",
          "criticalityLabel": "Suspicious",
          "evidenceString": "6 sightings on 3 sources: Kaspersky Securelist and Lab, Hei Shou, www.hx95.com. 2 related malwares: Duqu2, Computer Worm. Most recent link (Jun 17, 2015): https://securelist.ru/blog/issledovaniya/25905/modul-duqu-2-0-soxranyayushhij-prisutstvie-v-seti/",
          "rule": "Linked to Malware",
          "criticality": 2
        },
        {
          "timestamp": "2015-06-14T00:00:00.000Z",
          "criticalityLabel": "Malicious",
          "evidenceString": "1 sighting on 1 source: VirusTotal. Most recent link (Jun 14, 2015): https://www.virustotal.com/en/file/bc4ae56434b45818f57724f4cd19354a13e5964fd097d1933a30e2e31c9bdfa5/analysis/",
          "rule": "Positive Malware Verdict",
          "criticality": 3
        }
      ],
      "riskString": "3/12",
      "rules": 3,
      "criticality": 3,
      "riskSummary": "3 of 12 Risk Rules currently observed."
    },
    "analystNotes": []
  },
  "warnings": [
    "Unknown field nope"
  ]
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
|analystNotes|[]string|False|Notes from an analyst|
|counts|[]counts|False|Counts|
|enterpriseLists|[]enterpriseLists|False|Enterprise lists|
|entity|entity|False|Entity|
|metrics|[]metrics|False|Metrics|
|relatedEntities|[]relatedEntities|False|Related entities|
|risk|risk|False|Risk|
|sightings|[]sightings|False|Sightings|
|timestamps|timestamps|False|Timestamps|

Example output:

```
{
  "entity": {
    "id": "url:http://www.google.com",
    "name": "http://www.google.com",
    "type": "URL"
  },
  "timestamps": {
    "firstSeen": "2019-07-26T00:00:00.000Z",
    "lastSeen": "2019-07-26T23:59:59.000Z"
  }
}

```

#### Download IP Addresses Risk List

This action is used to fetch a risk list of the IP addresses that match a specified filtration rule.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|list|string|None|False|The risk list to retrieve, leaving the list parameter blank results in the default risk list|['current_cc_server', 'cyber_exploit_signal_medium', 'historical_bad_ssl_association', 'historical_botnet_traffic', 'historical_cc_server', 'historical_honeypot_sighting', 'historical_multicategory_blacklist', 'historical_open_proxies', 'historical_positive_malware_verdict', 'historical_spam_source', 'historical_sshdictionary_attacker', 'historical_threat_researcher', 'historically_linked_to_apt', 'historically_linked_to_cyber_attack', 'historically_linked_to_intrusion_method', 'honeypot_host', 'inside_possible_bogus_bgp_route', 'large', 'malicious_packet_source', 'malware_delivery', 'nameserver_for_cc_server', 'phishing_host', 'recent_botnet_traffic', 'recent_cc_server', 'recent_honeypot_sighting', 'recent_host_of_many_ddns_names', 'recent_multicategory_blacklist', 'recent_open_proxies', 'recent_positive_malware_verdict', 'recent_spam_source', 'recent_sshdictionary_attacker', 'recent_threat_researcher', 'recently_linked_to_apt', 'recently_linked_to_cyber_attack', 'recently_linked_to_intrusion_method', 'resolution_of_fast_flux_dns_name', 'tor_node', 'unusual_ip', 'vulnerable_host']|malware_delivery|

Example input:

```
{
  "list": "malware_delivery"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|False|Risk List|

Example output:

```
{
  "stix:STIX_Package": {
    "@xmlns": "http://xml/metadataSharing.xsd",
    "@xmlns:indicator": "http://stix.mitre.org/Indicator-2",
    "@xmlns:stix": "http://stix.mitre.org/stix-1",
    "@xmlns:ttp": "http://stix.mitre.org/TTP-1",
    "stix:STIX_Header": {
      "stix:Description": "Recorded Future STIX"
    },
    "@id": "RF:Package-9144eafb-a082-49d1-97a1-e7ceb4d8e955",
    "@timestamp": "2020-04-01T12:10:12.058Z",
    "@xmlns:FileObj": "http://cybox.mitre.org/objects#FileObject-2",
    "@xmlns:stixCommon": "http://stix.mitre.org/common-1",
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
              "stixCommon:Reference": "https://app.recordedfuture.com/live/sc/entity/ip%!..."
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
              "stixCommon:Reference": "https://app.recordedfuture.com/live/sc/entity/ip%!..."
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
    "@xmlns:RF": "http://stix.recordedfuture.com/",
    "@xmlns:cybox": "http://cybox.mitre.org/cybox-2",
    "@xmlns:cyboxCommon": "http://cybox.mitre.org/common-2",
    "@xmlns:stixVocabs": "http://stix.mitre.org/default_vocabularies-1",
    "@version": "1.2",
    "@xmlns:AddressObj": "http://cybox.mitre.org/objects#AddressObject-2",
    "@xmlns:cyboxVocabs": "http://cybox.mitre.org/default_vocabularies-2"
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
|analystNotes|[]string|False|Notes from an analyst|
|counts|[]counts|False|Counts|
|enterpriseLists|[]enterpriseLists|False|Enterprise lists|
|entity|entity|False|Entity|
|found|boolean|False|Has the IP been found in Recorded Future|
|intelCard|string|False|Intel card|
|location|location|False|Location|
|metrics|[]metrics|False|Metrics|
|relatedEntities|[]relatedEntities|False|Related entities|
|risk|risk|False|Risk|
|riskyCIDRIPs|[]riskyCIDRIP|False|Risky CIDR IPs|
|sightings|[]sightings|False|Sightings|
|threatLists|[]threatLists|False|Threat lists|
|timestamps|timestamps|False|Timestamps|

Example output:

```
{
  "entity": {
    "id": "ip:8.8.8.8",
    "name": "8.8.8.8",
    "type": "IpAddress"
  },
  "timestamps": {
    "firstSeen": "2010-04-27T12:46:51.000Z",
    "lastSeen": "2019-07-26T15:26:50.084Z"
  }
}
```

#### Download Vulnerability Risk List

This action is used to fetch a risk list of vulnerabilities matching a specified filtration rule.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|list|string|None|False|The risk list to retrieve, leaving the list parameter blank results in the default risk list|['cyber_exploit_signal_critical', 'cyber_exploit_signal_important', 'cyber_exploit_signal_medium', 'historical_scanner_uptake', 'historically_linked_to_exploit_kit', 'historically_linked_to_malware', 'historically_linked_to_ransomware', 'historically_linked_to_remote_access_trojan', 'large', 'linked_to_recent_cyber_exploit', 'nist_severity_critical', 'nist_severity_high', 'nist_severity_low', 'nist_severity_medium', 'recent_scanner_uptake', 'recently_linked_to_exploit_kit', 'recently_linked_to_malware', 'recently_linked_to_ransomware', 'recently_linked_to_remote_access_trojan', 'web_reporting_prior_to_nvd_disclosure']|nist_severity_critical|

Example input:

```
{
  "list": "nist_severity_critical"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|risk_list|object|False|Risk List|

Example output:

```
{
  "stix:STIX_Package": {
    "@xmlns": "http://xml/metadataSharing.xsd",
    "@xmlns:RF": "http://stix.recordedfuture.com/",
    "@xmlns:cybox": "http://cybox.mitre.org/cybox-2",
    "@xmlns:et": "http://stix.mitre.org/ExploitTarget-1",
    "@xmlns:stix": "http://stix.mitre.org/stix-1",
    "@xmlns:stixCommon": "http://stix.mitre.org/common-1",
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
              "stixCommon:Reference": "https://app.recordedfuture.com/live/sc/entity/dXhB..."
            }
          }
        },
        {
          "et:Vulnerability": {
            "et:CVE_ID": "CVE-2020-6820",
            "et:References": {
              "stixCommon:Reference": "https://app.recordedfuture.com/live/sc/entity/dXhB..."
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
|risk_rules|[]risk_rule|False|Risk Rules|

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
|data|vulnerability_search_data|False|Data|

Example output:

```
{
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
    "intelCard": "https://app.recordedfuture.com/live/sc/entity/OjOAdZ",
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

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

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
