# Description

[Threat Command](https://intsights.com/) by Rapid7 is disrupting external threat intelligence with a combination of human and automated collection, intelligent analysis, and strategic threat hunting that turns the clear, deep, and dark webs into an intelligence resource that any company can deploy

# Key Features

* Get Indicator by Value
* Enrich Indicator
* Get Alerts
* Get Complete Alert by ID
* Takedown Request
* Add Manual Alert
* Get CVE by ID
* Get CVE List
* Delete CVE
* Add CVE

# Requirements

* Requires an Account ID for Threat Command
* Requires API key for Threat Command

# Supported Product Versions

* 2.4.0

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|account_id|string|None|True|Account ID for Threat Command|None|9de5069c5afe602b2ea0a04b|
|api_key|credential_secret_key|None|True|API key for Threat Command|None|bffce7a2e653eb3e499b69238c6ed672727a642e6f07c19fe19b4d59c7a2d2a61078d1601ded75bac3859fc5c204279402ccf141e1999edf9deb47951f96f4c1|

Example input:

```
{
  "account_id": "9de5069c5afe602b2ea0a04b",
  "api_key": "cc805d5fab1fd71a4ab352a9c533e65fb2d5b885518f4e565e68847223b8e6b85cb48f3afad842726d99239c9e36505c64b0dc9a061d9e507d833277ada336ab"
}
```

## Technical Details

### Actions

#### Get IOCs by Filter

Get Indicators of Compromise by Filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|first_seen_from|date|None|False|Filter by first seen date (IOC first-seen date is greater than)|None|2000-12-31T00:00:00Z|
|first_seen_to|date|None|False|Filter by first seen date (IOC first-seen date is less than)|None|2000-12-31T00:00:00Z|
|kill_chain_phases|[]string|None|False|Filter by source IDs (Allowed values, Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command and Control, Actions on Objective)|None|["Command and Control"]|
|last_seen_from|date|None|False|Filter by last seen date (IOC last-seen date is greater than)|None|2000-12-31T00:00:00Z|
|last_seen_to|date|None|False|Filter by last seen date (IOC last-seen date is less than)|None|2000-12-31T00:00:00Z|
|last_updated_from|date|None|True|Filter by last update date (IOC update date is greater than)|None|2000-12-31T00:00:00Z|
|last_updated_to|date|None|False|Filter by last update date (IOC update date is less than)|None|2000-12-31T00:00:00Z|
|limit|integer|1000|False|Limit the results amount per page (1-1000)|None|1000|
|offset|string|None|False|Getting the next page of IOCs from offset|None|2020-01-01T20:01:27.344Z|
|severity|[]string|None|False|Filter by IOC severity (Allowed values, High, Medium, Low)|None|["High"]|
|source_ids|[]string|None|False|Filter by source IDs|None|["123450000012345000001233"]|
|status|string|None|False|Filter by IOC status|['', 'Active', 'Retired']|Active|
|type|[]string|None|False|Filter by IOC type (Allowed values, IpAddresses, Urls, Domainds, Hashes, Emails)|None|["IpAddresses"]|

Example input:

```
{
  "first_seen_from": "2000-12-31T00:00:00Z",
  "first_seen_to": "2000-12-31T00:00:00Z",
  "kill_chain_phases": [
    "Command and Control"
  ],
  "last_seen_from": "2000-12-31T00:00:00Z",
  "last_seen_to": "2000-12-31T00:00:00Z",
  "last_updated_from": "2000-12-31T00:00:00Z",
  "last_updated_to": "2000-12-31T00:00:00Z",
  "limit": 1000,
  "offset": "2020-01-01T20:01:27.344Z",
  "severity": [
    "High"
  ],
  "source_ids": [
    "123450000012345000001233"
  ],
  "status": "Active",
  "type": [
    "IpAddresses"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|content|[]ioc_content|False|List of IOCs that match filters|{ "content": [ { "value": "rapid7.com", "type": "Domains", "severity": "High", "score": 100, "whitelisted": false, "firstSeen": "2020-01-01T20:01:27.344Z", "lastSeen": "2020-01-30T16:18:51.148Z", "lastUpdateDate": "2020-02-21T23:00:51.268Z", "geolocation": "US", "tags": [ "MyTag_1" ], "relatedMalware": [ "doppeldridex", "dridex" ], "relatedCampaigns": [ "SolarWinds" ], "relatedThreatActors": [ "doppelspider" ], "reportedFeeds": [ { "ID": "SampleID", "Name": "AlienVault OTX", "ConfidenceLevel": 3 } ] } ], "nextOffset": "2022-11-18T16:59:01.626Z" }|
|nextOffset|string|False|The offset to the next page of IOCs|2020-01-01T20:01:27.344Z|


Example output:

```
{
  "content": [
    {
      "value": "rapid7.com",
      "type": "Domains",
      "severity": "High",
      "score": 100,
      "whitelisted": false,
      "firstSeen": "2020-01-01T20:01:27.344Z",
      "lastSeen": "2020-01-30T16:18:51.148Z",
      "lastUpdateDate": "2020-02-21T23:00:51.268Z",
      "geolocation": "US",
      "tags": [
        "MyTag_1"
      ],
      "relatedMalware": [
        "doppeldridex",
        "dridex"
      ],
      "relatedCampaigns": [
        "SolarWinds"
      ],
      "relatedThreatActors": [
        "doppelspider"
      ],
      "reportedFeeds": [
        {
          "id": "SampleID",
          "name": "AlienVault OTX",
          "confidenceLevel": 3
        }
      ]
    }
  ],
  "nextOffset": "2022-11-18T16:59:01.626Z"
}
```

#### Get CVE by ID

This action is used to get CVE's list from account.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|cve_id|[]string|None|False|Specific CVE IDs|None|["CVE-2020-0711"]|

Example input:

```
{
  "cve_id": [
    "CVE-2020-0711"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|content|[]content|False|Response content|{ "content": [ { "cveId": "CVE-2020-7064", "cpe": [ { "Value": "cpe:2.3:a:php:php:*:*:*:*:*:*:*:*", "Range": { "VersionStartIncluding": "7.2.0", "VersionEndIncluding": "", "VersionStartExcluding": "", "VersionEndExcluding": "7.2.9" }, "Title": "Php", "VendorProduct": "Php Php" } ], "publishedDate": "2020-04-01T04:15:00.000Z", "updateDate": "2021-10-25T10:14:52.978Z", "severity": "Low", "intsightsScore": 36, "cvssScore": 5.4, "mentionsAmount": 39, "mentionsPerSource": { "PasteSite": 0, "HackingForum": 0, "InstantMessage": 0, "DarkWeb": 0, "ClearWebCyberBlogs": 0, "CodeRepositories": 9, "Exploit": 0, "SocialMedia": 30 }, "firstMentionDate": "2020-03-19T15:09:00.000Z", "lastMentionDate": "2021-07-22T20:41:00.000Z", "exploitAvailability": false, "vulnerabilityOrigin": [ "API" ], "relatedThreatActors": [], "relatedMalware": [], "relatedCampaigns": [] } ], }|
Example output:

```
{
  "content": [
    {
      "cveId": "CVE-2020-7064",
      "cpe": [
        {
          "Value": "cpe:2.3:a:php:php:*:*:*:*:*:*:*:*",
          "Range": {
            "VersionStartIncluding": "7.2.0",
            "VersionEndIncluding": "",
            "VersionStartExcluding": "",
            "VersionEndExcluding": "7.2.9"
          },
          "Title": "Php",
          "VendorProduct": "Php Php"
        }
      ],
      "publishedDate": "2020-04-01T04:15:00.000Z",
      "updateDate": "2021-10-25T10:14:52.978Z",
      "severity": "Low",
      "intsightsScore": 36,
      "cvssScore": 5.4,
      "mentionsAmount": 39,
      "mentionsPerSource": {
        "PasteSite": 0,
        "HackingForum": 0,
        "InstantMessage": 0,
        "DarkWeb": 0,
        "ClearWebCyberBlogs": 0,
        "CodeRepositories": 9,
        "Exploit": 0,
        "SocialMedia": 30
      },
      "firstMentionDate": "2020-03-19T15:09:00.000Z",
      "lastMentionDate": "2021-07-22T20:41:00.000Z",
      "exploitAvailability": false,
      "vulnerabilityOrigin": [
        "API"
      ],
      "relatedThreatActors": [],
      "relatedMalware": [],
      "relatedCampaigns": []
    }
  ],
}
```

#### Add Manual Alert

This action will create a manual alert with the provided parameters.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|description|string|None|True|Alert description|None|Suspicious addresses|
|found_date|string|None|False|Alert found date|None|2020-01-01|
|images|[]image|None|False|Alert images|None|[{"Type": "jpeg","Data": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="}]|
|severity|string|None|True|Alert severity|['High', 'Medium', 'Low']|Medium|
|source_date|string|None|False|Alert source date|None|2020-02-01|
|source_network_type|string|None|True|Source network type|['ClearWeb', 'DarkWeb']|DarkWeb|
|source_type|string|None|True|Source type|['Application Store', 'Cyber Security Blog', 'Hacking News', 'Cyber Crime Forum', 'Hacktivism Forum', 'Social Media', 'Facebook', 'Twitter', 'LinkedIn', 'Google Plus', 'VK', 'Vimeo', 'YouTube', 'IRC Channel', 'IOC Block List', 'Credit Card Black Market', 'Paste Site', 'Data Leakage Website', 'Leaked Database', 'File Sharing Website', 'Gray Hat Website', 'Black Market', 'WHOIS servers', 'Company Website', 'Wikileaks', 'Pinterest', 'Tumblr', 'Instagram', 'Telegram', 'Webmail', 'Malware Analysis', 'Firehol', 'VRA']|Webmail|
|source_url|string|None|True|Source URL|None|https://example.com|
|sub_type|string|None|True|Alert sub type, needs to correlate with the selected "Type"|None|SuspiciousEmailAddress|
|title|string|None|True|Alert title|None|New Alert|
|type|string|None|True|Alert type|['AttackIndication', 'DataLeakage', 'Phishing', 'BrandSecurity', 'ExploitableData', 'vip']|Phishing|

Example input:

```
{
  "description": "Suspicious addresses",
  "found_date": "2020-01-01",
  "images": [],
  "severity": "Medium",
  "source_date": "2020-02-01",
  "source_network_type": "DarkWeb",
  "source_type": "Webmail",
  "source_url": "https://example.com",
  "sub_type": "SuspiciousEmailAddress",
  "title": "New Alert",
  "type": "Phishing"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|alert_id|string|True|New created alert ID|6156586e8eadf90008176450|

Example output:

```
{
  "alert_id": "6156586e8eadf90008176450"
}
```

#### Takedown Request

Request a takedown for a given alert in Threat Command

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_id|string|None|True|Alert's unique ID|None|44d88612fea8a8f36de82e12|
|target|string|Domain|True|Target|['Website', 'Domain']|Domain|

Example input:

```
{
  "alert_id": "44d88612fea8a8f36de82e12",
  "target": "Domain"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|status|boolean|True|Status from Threat Command|True|

Example output:

```
{
  "status": true
}
```

#### Get Complete Alert by ID

This action is used to get an alert's complete details for a given alert ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_id|string|None|True|Alert's unique ID|None|44d88612fea8a8f36de82e12|

Example input:

```
{
  "alert_id": "44d88612fea8a8f36de82e12"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|id|string|False|Alert ID|6156118e186a05000774ee46|
|assets|[]asset|True|List of assets|[ { "Type": "Domain", "Value": "https://example.com" } ]|
|assignees|[]string|True|List of assignees|[]|
|details|alert_details|True|Alert details|{ "Description": "APIDescription", "Images": [ "61efc2286b02dcd558929918" ], "Severity": "High", "Source": { "NetworkType": "ClearWeb", "Type": "Application Store", "URL": "https://example.com" }, "SubType": "SuspiciousEmailAddress", "Tags": [], "Title": "Alerttest3", "Type": "Phishing" }|
|found_date|date|False|Alert found date|2018-01-01 20:01:27.344000+00:00|
|update_date|date|False|Alert update date|2018-01-01 20:01:27.344000+00:00|
|takedown_status|string|False|Alert remediation status|NotSent|
|is_closed|boolean|True|Is alert closed|False|
|is_flagged|boolean|True|Is alert flagged|False|
|leak_name|string|False|Name of the leak DBs in data leakage alerts|example.com|


Example output:

```
{
  "assets": [
    {
      "Type": "Domain",
      "Value": "https://example.com"
    }
  ],
  "assignees": [],
  "details": {
    "Description": "APIDescription",
    "Images": [
      "61efc2286b02dcd558929918"
    ],
    "Severity": "High",
    "Source": {
      "NetworkType": "ClearWeb",
      "Type": "Application Store",
      "URL": "https://example.com"
    },
    "SubType": "SuspiciousEmailAddress",
    "Tags": [],
    "Title": "Alerttest3",
    "Type": "Phishing"
  },
  "found_date": "2018-01-01T20:01:27.344Z",
  "id": "6156118e186a05000774ee46",
  "is_closed": false,
  "is_flagged": false,
  "takedown_status": "NotSent",
  "update_date": "2018-01-01T20:01:27.344Z",
  "leak_name": "example.com"
}
```

#### Get Alerts

This action is used to search Alerts based on criteria.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_type|[]string|None|False|List of alert types. Allowed values: AttackIndication, DataLeakage, Phishing, BrandSecurity, ExploitableData, vip|None|["Phishing"]|
|assigned|string|None|False|Show assigned/unassigned alerts|['Assigned', 'Unassigned', '']|Assigned|
|found_date_from|string|None|False|Start date (when alert found event) to fetch from in Unix Millisecond Timestamp|None|0|
|found_date_to|string|None|False|End date (when alert found event) to fetch to in Unix Millisecond Timestamp|None|1633047102456|
|has_indicators|boolean|None|False|Show alerts with IOCs results|None|False|
|is_closed|string|None|False|Status of the alert, either closed or open|['Closed', 'Open', '']|Closed|
|is_flagged|string|None|False|Show flagged/unflagged alerts|['Flagged', 'Unflagged', '']|Flagged|
|matched_asset_value|[]string|None|False|List of matched asset values. Examples: IP address, domain name, company name|None|["example.com"]|
|network_type|[]string|None|False|List of network type. Allowed values: ClearWeb, DarkWeb|None|["DarkWeb"]|
|remediation_status|[]string|None|False|List of remediation statuses. Allowed values: InProgress, Pending, CancellationInProgress, Cancelled, CompletedSuccessfully, Failed|None|["InProgress", "Pending"]|
|severity|[]string|None|False|List of alerts severity. Allowed values: High, Medium, Low|None|["Low"]|
|source_date_from|string|None|False|Start date (when the event occurred) to fetch from in Unix Millisecond Timestamp|None|1633047083142|
|source_date_to|string|None|False|End date (when the event occurred) to fetch to in Unix Millisecond Timestamp|None|1633047102456|
|source_type|[]string|None|False|List of alerts source type. Allowed values: Application Store, Cyber Security Blog, Hacking News, Cyber Crime Forum, Hacktivism Forum, Social Media, Facebook, Twitter, LinkedIn, Google Plus, VK, Vimeo, YouTube, IRC Channel, IOC Block List, Credit Card Black Market, Paste Site, Data Leakage Website, Leaked Database, File Sharing Website, Gray Hat Website, Black Market, WHOIS servers, Company Website, Wikileaks, Pinterest, Tumblr, Instagram, Telegram, Webmail, Malware Analysis, Firehol, VRA, Other|None|["Application Store"]|

Example input:

```
{
  "alert_type": [
    "Phishing"
  ],
  "assigned": "Assigned",
  "found_date_from": 0,
  "found_date_to": 1633047102456,
  "has_indicators": false,
  "is_closed": "Closed",
  "is_flagged": "Flagged",
  "matched_asset_value": [
    "example.com"
  ],
  "network_type": [
    "DarkWeb"
  ],
  "remediation_status": [
    "InProgress",
    "Pending"
  ],
  "severity": [
    "Low"
  ],
  "source_date_from": 1633047083142,
  "source_date_to": 1633047102456,
  "source_type": [
    "Application Store"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|alert_ids|[]string|True|List of alert IDs|["6155f7b7c6e9d40008b4bb0d","6155f801186a050007745d29"]|

Example output:

```
{
  "alert_ids": [
    "6155f7b7c6e9d40008b4bb0d",
    "6155f801186a050007745d29"
  ]
}
```

#### Enrich Indicator

This action is used to submit an indicator to Threat Command for investigation and return the results.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|indicator_value|string|None|True|Value of the indicator. Examples: IP address, URL, domain name, hash|None|example.com|

Example input:

```
{
  "indicator_value": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|data|object|False|Data|{ "Subdomains": [ "itunes", "apps" ], "Tags": [], "Type": "Domains", "Value": "example.com", "Whitelisted": true, "IsKnownIoc": false, "RelatedHashes": { "downloaded": [ "5d8c914e53bf34fdeac7441b99fe412240a1211fe2e074dfb2...", "7d2970c279d399214f83f140bb509441e9ae7262f98e8ae41f..." ], "referencing": [ "004b5bb9d28f03397ab3462863cd5902", "00f44bc82df0e8808b70abad0993bdb3" ], "communicating": [ "03b0f52b4d517d2a4f8a7994acd26adb77b8c7d9b25ef37c9a...", "09277de376a14f6475a242ca9ad4743dc81bd951853228d625..." ] }, "RelatedThreatActors": [], "Sources": [], "Whois": { "Current": { "RegistrantDetails": [ { "City": "Cupertino", "Country": "UNITED STATES", "CountryCode": "US", "PostalCode": "95014", "Telephone": "14089961010", "State": "", "Address": "One Apple Park Way", "Email": "user@example.com", "Fax": "14089741560", "Name": "Apple Inc.", "Organization": "Apple Inc." } ], "RegistrationDetails": { "CreatedDate": "1987-02-19T00:00:00.000Z", "ExpiresDate": "2022-02-20T05:00:00.000Z", "NameServers": [ "b.ns.apple.com", "a.ns.apple.com" ], "Statuses": [ "clientTransferProhibited", "serverDeleteProhibited" ], "UpdatedDate": "2021-02-16T01:26:20.000Z" } }, "History": [ { "RegistrantDetails": [ { "Address": "1 Infinite Loop", "Country": "UNITED STATES", "Fax": "14089741560", "Name": "Domain Administrator", "Telephone": "14089961010", "State": "CA", "City": "Cupertino", "CountryCode": "", "Email": "user@example.com", "Organization": "Apple Inc.", "PostalCode": "95014" }, { "Address": "1 Infinite Loop", "CountryCode": "", "Email": "user@example.com", "Fax": "14089741560", "Organization": "Apple Inc.", "Telephone": "14089961010", "City": "Cupertino", "Country": "UNITED STATES", "Name": "Domain Administrator", "PostalCode": "95014", "State": "CA" } ], "RegistrationDetails": { "CreatedDate": "1987-02-19T01:27:12.000Z", "ExpiresDate": "2021-02-20T01:27:12.000Z", "NameServers": [ "ADNS1.APPLE.COM", "ADNS2.APPLE.COM" ], "Statuses": [ "clientTransferProhibited" ], "UpdatedDate": "2012-12-04T01:27:12.000Z" } }, { "RegistrantDetails": [ { "City": "Cupertino", "CountryCode": "", "Email": "user@example.com", "Fax": "", "Name": "Domain Administrator", "State": "CA", "Telephone": "14089961010", "Address": "1 Infinite Loop", "Organization": "Apple Inc.", "PostalCode": "95014", "Country": "UNITED STATES" }, { "Address": "1 Infinite Loop", "City": "Cupertino", "Fax": "", "PostalCode": "95014", "State": "CA", "Telephone": "14089961010", "Country": "UNITED STATES", "CountryCode": "", "Email": "user@example.com", "Name": "Domain Administrator", "Organization": "Apple Inc." } ], "RegistrationDetails": { "UpdatedDate": "2012-12-04T13:10:47.000Z", "CreatedDate": "1987-02-19T13:10:47.000Z", "ExpiresDate": "2021-02-20T13:10:47.000Z", "NameServers": [ "ADNS1.APPLE.COM", "ADNS2.APPLE.COM" ], "Statuses": [ "clientTransferProhibited" ] } } ] }, "DnsRecords": [ { "Type": "NS", "Value": "a.ns.apple.com.", "Count": 123, "FirstResolved": null, "LastResolved": null }, { "FirstResolved": null, "LastResolved": null, "Type": "NS", "Value": "b.ns.apple.com.", "Count": 123 } ], "RelatedMalwares": [], "Resolutions": [ { "ResolvedIpAddress": "17.253.144.10", "ASN": 714, "FirstResolved": "2020-10-09T02:47:17.000Z", "LastResolved": "2021-09-18T13:35:55.000Z", "Location": "US", "Operator": "Apple Inc.", "ReportingSources": [ "Farsight", "VirusTotal" ] }, { "ResolvedIpAddress": "17.142.160.59", "ASN": 714, "FirstResolved": "2014-07-09T16:35:28.000Z", "LastResolved": "2020-10-09T03:00:19.000Z", "Location": "US", "Operator": "Apple Inc.", "ReportingSources": [ "Farsight", "VirusTotal" ] } ], "SystemTags": [], "RelatedCampaigns": [], "Severity": { "Score": 0, "Value": "Low" } }|
|original_value|string|True|Original value|example.com|
|status|string|True|Status|Done|

Example output:

```
{
  "data": {
    "Subdomains": [
      "itunes",
      "apps"
    ],
    "Tags": [],
    "Type": "Domains",
    "Value": "example.com",
    "Whitelisted": true,
    "IsKnownIoc": false,
    "RelatedHashes": {
      "downloaded": [
        "5d8c914e53bf34fdeac7441b99fe412240a1211fe2e074dfb2...",
        "7d2970c279d399214f83f140bb509441e9ae7262f98e8ae41f..."
      ],
      "referencing": [
        "004b5bb9d28f03397ab3462863cd5902",
        "00f44bc82df0e8808b70abad0993bdb3"
      ],
      "communicating": [
        "03b0f52b4d517d2a4f8a7994acd26adb77b8c7d9b25ef37c9a...",
        "09277de376a14f6475a242ca9ad4743dc81bd951853228d625..."
      ]
    },
    "RelatedThreatActors": [],
    "Sources": [],
    "Whois": {
      "Current": {
        "RegistrantDetails": [
          {
            "City": "Cupertino",
            "Country": "UNITED STATES",
            "CountryCode": "US",
            "PostalCode": "95014",
            "Telephone": "14089961010",
            "State": "",
            "Address": "One Apple Park Way",
            "Email": "user@example.com",
            "Fax": "14089741560",
            "Name": "Apple Inc.",
            "Organization": "Apple Inc."
          }
        ],
        "RegistrationDetails": {
          "CreatedDate": "1987-02-19T00:00:00.000Z",
          "ExpiresDate": "2022-02-20T05:00:00.000Z",
          "NameServers": [
            "b.ns.apple.com",
            "a.ns.apple.com"
          ],
          "Statuses": [
            "clientTransferProhibited",
            "serverDeleteProhibited"
          ],
          "UpdatedDate": "2021-02-16T01:26:20.000Z"
        }
      },
      "History": [
        {
          "RegistrantDetails": [
            {
              "Address": "1 Infinite Loop",
              "Country": "UNITED STATES",
              "Fax": "14089741560",
              "Name": "Domain Administrator",
              "Telephone": "14089961010",
              "State": "CA",
              "City": "Cupertino",
              "CountryCode": "",
              "Email": "user@example.com",
              "Organization": "Apple Inc.",
              "PostalCode": "95014"
            },
            {
              "Address": "1 Infinite Loop",
              "CountryCode": "",
              "Email": "user@example.com",
              "Fax": "14089741560",
              "Organization": "Apple Inc.",
              "Telephone": "14089961010",
              "City": "Cupertino",
              "Country": "UNITED STATES",
              "Name": "Domain Administrator",
              "PostalCode": "95014",
              "State": "CA"
            }
          ],
          "RegistrationDetails": {
            "CreatedDate": "1987-02-19T01:27:12.000Z",
            "ExpiresDate": "2021-02-20T01:27:12.000Z",
            "NameServers": [
              "ADNS1.APPLE.COM",
              "ADNS2.APPLE.COM"
            ],
            "Statuses": [
              "clientTransferProhibited"
            ],
            "UpdatedDate": "2012-12-04T01:27:12.000Z"
          }
        },
        {
          "RegistrantDetails": [
            {
              "City": "Cupertino",
              "CountryCode": "",
              "Email": "user@example.com",
              "Fax": "",
              "Name": "Domain Administrator",
              "State": "CA",
              "Telephone": "14089961010",
              "Address": "1 Infinite Loop",
              "Organization": "Apple Inc.",
              "PostalCode": "95014",
              "Country": "UNITED STATES"
            },
            {
              "Address": "1 Infinite Loop",
              "City": "Cupertino",
              "Fax": "",
              "PostalCode": "95014",
              "State": "CA",
              "Telephone": "14089961010",
              "Country": "UNITED STATES",
              "CountryCode": "",
              "Email": "user@example.com",
              "Name": "Domain Administrator",
              "Organization": "Apple Inc."
            }
          ],
          "RegistrationDetails": {
            "UpdatedDate": "2012-12-04T13:10:47.000Z",
            "CreatedDate": "1987-02-19T13:10:47.000Z",
            "ExpiresDate": "2021-02-20T13:10:47.000Z",
            "NameServers": [
              "ADNS1.APPLE.COM",
              "ADNS2.APPLE.COM"
            ],
            "Statuses": [
              "clientTransferProhibited"
            ]
          }
        }
      ]
    },
    "DnsRecords": [
      {
        "Type": "NS",
        "Value": "a.ns.apple.com.",
        "Count": 123,
        "FirstResolved": null,
        "LastResolved": null
      },
      {
        "FirstResolved": null,
        "LastResolved": null,
        "Type": "NS",
        "Value": "b.ns.apple.com.",
        "Count": 123
      }
    ],
    "RelatedMalwares": [],
    "Resolutions": [
      {
        "ResolvedIpAddress": "17.253.144.10",
        "ASN": 714,
        "FirstResolved": "2020-10-09T02:47:17.000Z",
        "LastResolved": "2021-09-18T13:35:55.000Z",
        "Location": "US",
        "Operator": "Apple Inc.",
        "ReportingSources": [
          "Farsight",
          "VirusTotal"
        ]
      },
      {
        "ResolvedIpAddress": "17.142.160.59",
        "ASN": 714,
        "FirstResolved": "2014-07-09T16:35:28.000Z",
        "LastResolved": "2020-10-09T03:00:19.000Z",
        "Location": "US",
        "Operator": "Apple Inc.",
        "ReportingSources": [
          "Farsight",
          "VirusTotal"
        ]
      }
    ],
    "SystemTags": [],
    "RelatedCampaigns": [],
    "Severity": {
      "Score": 0,
      "Value": "Low"
    }
  },
  "original_value": "example.com",
  "status": "Done"
}
```

#### Get Indicator by Value

This action will search indicators in Threat Command TIP.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|indicator_value|string|None|True|Value of the indicator. Examples: IP address, URL, domain name, hash|None|example.com|

Example input:

```
{
  "indicator_value": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|first_seen|string|False|First seen|2020-01-01 20:01:27.344000+00:00|
|geo_location|string|False|Geographic location|US|
|last_seen|string|False|Last seen|2020-01-01 20:01:27.344000+00:00|
|last_update|string|False|Last update|2020-01-01 20:01:27.344000+00:00|
|related_campaigns|[]string|False|Related campaigns|["doppeldridex", "dridex"]|
|related_malware|[]string|False|Related malware|example.com|
|related_threat_actors|[]string|False|Related threat actors|["doppelspider"]|
|score|float|False|Score|10|
|severity|string|False|Severity|Low|
|sources|[]source|False|Sources|[ { "confidenceLevel": 2, "name": "Cyber Threat Alliance" } ]|
|system_tags|[]string|False|System tags|["MyTag_1"]|
|tags|[]string|False|Tags|["MyTag_1"]|
|type|string|False|Type|Domains|
|value|string|False|Indicator value|example.com|
|whitelist|boolean|False|Whitelist|True|
|status|string|False|Status|Active|
|reported_feeds|[]reported_feed|False|Reported Feeds|[ { "ID": "SampleID", "Name": "AlienVault OTX", "ConfidenceLevel": 3 } ]|

Example output:

```
{
  "first_seen": "2020-01-01T20:01:27.344Z",
  "last_seen": "2020-01-01T20:01:27.344Z",
  "last_update": "2020-01-01T20:01:27.344Z",
  "related_campaigns": [],
  "related_malware": [],
  "related_threat_actors": [],
  "score": 10,
  "severity": "Low",
  "sources": [
    {
      "ConfidenceLevel": 2,
      "Name": "Cyber Threat Alliance"
    }
  ],
  "system_tags": [],
  "tags": [],
  "type": "Domains",
  "value": "example.com",
  "whitelist": true
}
```

#### Get CVE List

This action is used to get a partial list of all CVEs from an account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|offset|string|None|False|Offset value for pagination, if empty the first page of results will be returned|None|2000-00-00T00:00:00.000Z::614b8972da44a60005036b01|

Example input:

```
{
  "offset": "2000-00-00T00:00:00.000Z::614b8972da44a60005036b01"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|content|[]content|False|Response content|[ { "cpe": [], "cveId": "CVE-2020-20795", "exploitAvailability": false, "firstMentionDate": "https://example.com", "intsightsScore": 1, "lastMentionDate": "https://example.com", "mentionsAmount": 1, "mentionsPerSource": { "ClearWebCyberBlogs": 0, "CodeRepositories": 0, "DarkWeb": 0, "Exploit": 0, "HackingForum": 0, "InstantMessage": 0, "PasteSite": 0, "SocialMedia": 1 }, "publishedDate": "https://example.com", "relatedCampaigns": [], "relatedMalware": [], "relatedThreatActors": [], "severity": "Low", "updateDate": "https://example.com", "vulnerabilityOrigin": [ "API" ] }, { "cpe": [ { "Range": { "VersionEndExcluding": "2017-08-25" }, "Title": "Voten", "Value": "https://example.com*:*:*:*:*:*:*:*", "VendorProduct": "Voten Voten" } ], "cveId": "CVE-2018-7663", "cvssScore": "https://example.com", "exploitAvailability": false, "firstMentionDate": "https://example.com", "intsightsScore": 28, "lastMentionDate": "https://example.com", "mentionsAmount": 20, "mentionsPerSource": { "ClearWebCyberBlogs": 0, "CodeRepositories": 1, "DarkWeb": 0, "Exploit": 0, "HackingForum": 0, "InstantMessage": 0, "PasteSite": 0, "SocialMedia": 19 }, "publishedDate": "https://example.com", "relatedCampaigns": [], "relatedMalware": [], "relatedThreatActors": [], "severity": "Low", "updateDate": "https://example.com", "vulnerabilityOrigin": [ "API" ] } ]|
|next_offset|string|False|Next offset value for pagination|2000-00-00T00:00:00.000Z::614b8972da44a60005036b01|

Example output:

```
{
  "content": [
    {
      "cpe": [],
      "cveId": "CVE-2020-20795",
      "exploitAvailability": false,
      "firstMentionDate": "https://example.com",
      "intsightsScore": 1,
      "lastMentionDate": "https://example.com",
      "mentionsAmount": 1,
      "mentionsPerSource": {
        "ClearWebCyberBlogs": 0,
        "CodeRepositories": 0,
        "DarkWeb": 0,
        "Exploit": 0,
        "HackingForum": 0,
        "InstantMessage": 0,
        "PasteSite": 0,
        "SocialMedia": 1
      },
      "publishedDate": "https://example.com",
      "relatedCampaigns": [],
      "relatedMalware": [],
      "relatedThreatActors": [],
      "severity": "Low",
      "updateDate": "https://example.com",
      "vulnerabilityOrigin": [
        "API"
      ]
    },
    {
      "cpe": [
        {
          "Range": {
            "VersionEndExcluding": "2017-08-25"
          },
          "Title": "Voten",
          "Value": "https://example.com*:*:*:*:*:*:*:*",
          "VendorProduct": "Voten Voten"
        }
      ],
      "cveId": "CVE-2018-7663",
      "cvssScore": "https://example.com",
      "exploitAvailability": false,
      "firstMentionDate": "https://example.com",
      "intsightsScore": 28,
      "lastMentionDate": "https://example.com",
      "mentionsAmount": 20,
      "mentionsPerSource": {
        "ClearWebCyberBlogs": 0,
        "CodeRepositories": 1,
        "DarkWeb": 0,
        "Exploit": 0,
        "HackingForum": 0,
        "InstantMessage": 0,
        "PasteSite": 0,
        "SocialMedia": 19
      },
      "publishedDate": "https://example.com",
      "relatedCampaigns": [],
      "relatedMalware": [],
      "relatedThreatActors": [],
      "severity": "Low",
      "updateDate": "https://example.com",
      "vulnerabilityOrigin": [
        "API"
      ]
    }
  ],
  "next_offset": "2000-00-00T00:00:00.000Z::614b8972da44a60005036b01",
}
```

#### Add CVEs

This action is used to add CVEs to account.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|cve_id|[]string|None|False|List of CVE IDs|None|["CVE-2020-0711"]|

Example input:

```
{
  "cve_id": [
    "CVE-2020-0711"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success_amount|integer|True|Amount of successfully added CVEs|2|
|failure|[]cve_failure_type|True|Failure details|[ { "cveId": "CVE-1999-003", "failReason": "Invalid CVE format" } ]|

Example output:

```
{
  "success_amount": 2,
  "failure": [
    {
      "cveId": "CVE-1999-003",
      "failReason": "Invalid CVE format"
    }
  ]
}
```

#### Delete CVEs

This action is used to delete CVEs from account.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|cve_id|[]string|None|False|List of CVE IDs|None|["CVE-2020-0711"]|

Example input:

```
{
  "cve_id": [
    "CVE-2020-0711"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success_amount|integer|True|Amount of successfully deleted CVEs|3|
|failure|[]cve_failure_type|True|Failure details|[]|

Example output:

```
{
  "failure": [],
  "success_amount": 3
}
```


### Triggers

#### New Alert

This trigger will run when a new alert that matches the given criteria is created in Threat Command.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|alert_type|[]string|None|False|List of alert types. Allowed values: AttackIndication, DataLeakage, Phishing, BrandSecurity, ExploitableData, vip|None|["Phishing"]|
|assigned|string|None|False|Show assigned/unassigned alerts|['Assigned', 'Unassigned', '']|Assigned|
|found_date_from|string|None|False|Start date (when alert found event) to fetch from in Unix Millisecond Timestamp|None|0|
|found_date_to|string|None|False|End date (when alert found event) to fetch to in Unix Millisecond Timestamp|None|1633047102456|
|frequency|integer|60|False|Poll frequency in seconds|None|60|
|has_indicators|boolean|None|False|Shows alerts with IOC results|None|False|
|is_closed|string|None|False|Status of the alert, either closed or open|['Closed', 'Open', '']|Closed|
|is_flagged|string|None|False|Show flagged/unflagged alerts|['Flagged', 'Unflagged', '']|Flagged|
|matched_asset_value|[]string|None|False|List of matched asset values. Examples: IP address, domain name, company name|None|["example.com"]|
|network_type|[]string|None|False|List of network types. Allowed values: ClearWeb, DarkWeb|None|["DarkWeb"]|
|remediation_status|[]string|None|False|List of remediation statuses. Allowed values: InProgress, Pending, CancellationInProgress, Cancelled, CompletedSuccessfully, Failed|None|["InProgress", "Pending"]|
|severity|[]string|None|False|List of alerts severity. Allowed values: High, Medium, Low|None|["Low"]|
|source_date_from|string|None|False|Start date (when the event occured) to fetch from in Unix Millisecond Timestamp|None|1633047083142|
|source_date_from_enum|string|None|False|Start date to fetch from with options, such as choose Hour to pull alerts in the last hour|['Hour', 'Day', 'Week', '']|Hour|
|source_date_to|string|None|False|End date (when the event occured) to fetch to in Unix Millisecond Timestamp|None|1633047102456|
|source_type|[]string|None|False|List of alert's source type. Allowed values: Application Store, Cyber Security Blog, Hacking News, Cyber Crime Forum, Hacktivism Forum, Social Media, Facebook, Twitter, LinkedIn, Google Plus, VK, Vimeo, YouTube, IRC Channel, IOC Block List, Credit Card Black Market, Paste Site, Data Leakage Website, Leaked Database, File Sharing Website, Gray Hat Website, Black Market, WHOIS servers, Company Website, Wikileaks, Pinterest, Tumblr, Instagram, Telegram, Webmail, Malware Analysis, Firehol, VRA, Other|None|["Application Store"]|

Example input:

```
{
  "alert_type": [
    "Phishing"
  ],
  "assigned": "Assigned",
  "found_date_from": 0,
  "found_date_to": 1633047102456,
  "frequency": 60,
  "has_indicators": false,
  "is_closed": "Closed",
  "is_flagged": "Flagged",
  "matched_asset_value": [
    "example.com"
  ],
  "network_type": [
    "DarkWeb"
  ],
  "remediation_status": [
    "InProgress",
    "Pending"
  ],
  "severity": [
    "Low"
  ],
  "source_date_from": 1633047083142,
  "source_date_from_enum": "Hour",
  "source_date_to": 1633047102456,
  "source_type": [
    "Application Store"
  ]
}
{
  "alert_type": [
    "Phishing"
  ],
  "assigned": "Assigned",
  "found_date_from": 0,
  "found_date_to": 1633047102456,
  "frequency": 60,
  "has_indicators": false,
  "is_closed": "Closed",
  "is_flagged": "Flagged",
  "matched_asset_value": [
    "example.com"
  ],
  "network_type": [
    "DarkWeb"
  ],
  "remediation_status": [
    "InProgress",
    "Pending"
  ],
  "severity": [
    "Low"
  ],
  "source_date_from": "",
  "source_date_from_enum": "Hour",
  "source_date_to": "",
  "source_type": [
    "Application Store"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|alert_ids|[]string|True|List of alert IDs|["618305318f3b3c0007d2cac0"]|

Example output:

```
{
  "alert_ids": [
    "618305318f3b3c0007d2cac0"
  ]
}
```

### Custom Output Types

#### image

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Data|string|True|Data|
|Type|string|True|Type|

#### source

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Confidence Level|integer|True|Level of confidence|
|Name|string|True|Name|

#### reported_feed

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|string|False|ID|
|Confidence Level|integer|False|Level of confidence|
|Name|string|False|Name|

#### alert_source

|Name|Type|Required|Description|
|---|----|--------|-----------|
|Type|string|True|Type|
|URL|string|False|URL|
|Email|string|False|Email|
|Network Type|string|False|Network type|
|Date|string|False|Date|

#### alert_tags

|Name|Type|Required|Description|
|---|----|--------|-----------|
|ID|string|True|ID|
|Name|string|True|Name|
|Created By|string|True|Created by|

#### alert_details

|Name|Type|Required|Description|
|---|----|--------|-----------|
|Type|string|True|Type|
|Sub Type|string|True|Sub type|
|Severity|string|True|Severity|
|Source|alert_source|True|Source|
|Title|string|True|Title|
|Description|string|False|Description|
|Images|[]string|False|Images|
|Tags|[]alert_tags|False|Tags|
|Related IOCs|[]string|False|Related IOCs|

#### asset

|Name|Type|Required|Description|
|---|----|--------|-----------|
|Type|string|True|Asset type|
|Value|string|True|Asset value|

#### range

|Name|Type|Required|Description|
|---|----|--------|-----------|
|Version End Excluding|string|False|Version end excluding|
|Version End Including|string|False|Version end including|
|Version Start Excluding|string|False|Version start excluding|
|Version Start Including|string|False|Version start including|

#### asset

|Name|Type|Required|Description|
|---|----|--------|-----------|
|Range|range|False|Range|
|Title|string|False|Title|
|Vendor Product|string|False|Vendor product|
|Value|string|False|Asset value|

#### mentionsPerSource

|Name|Type|Required|Description|
|---|----|--------|-----------|
|Clear Web Cyber Blogs|integer|False|Clear web cyber blogs|
|Code Repositories|integer|False|Code repositories|
|Dark Web|integer|False|Dark web|
|Exploit|integer|False|Exploit|
|Hacking Forum|integer|False|Hacking forum|
|Instant Message|integer|False|Instant message|
|Paste Site|integer|False|Paste site|
|Social Media|integer|False|Social media|

#### content

|Name|Type|Required|Description|
|----|----|--------|-----------|
|CVE ID|string|False|CVE ID|
|CPE|[]cpe|False|CPE|
|Published Date|string|False|Published date|
|Update Date|string|False|Update date|
|Severity|string|False|Severity|
|IntSights Score|float|False|IntSights score|
|CVSS Score|float|False|Common Vulnerability Scoring System score|
|Mentions Amount|integer|False|Mentions amount|
|Mentions Per Source|mentionsPerSource|False|Mentions per source|
|First Mention Date|string|False|First mention date|
|Last Mention Date|string|False|Last mention date|
|Exploit Availability|boolean|False|Exploit availability|
|Vulnerability Origin|[]string|False|Vulnerability origin|
|Related Malware|[]string|False|Related malware|
|Related Campaigns|[]string|False|Related campaigns|
|Related Threat Actors|[]string|False|Related threat actors|

#### cve_failure_type

|Name|Type|Required|Description|
|---|----|--------|-----------|
|CVE ID|range|True|CVE ID|
|Fail Reason|string|True|Fail reason|

#### ioc_content

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Indicator Value|string|False|Indicator value|
|Type|string|False|Type|
|Severity|string|False|Severity|
|Score|float|False|Score|
|Whitelisted|boolean|False|Whitelisted|
|First Seen|string|False|First seen|
|Last Seen|string|False|Last seen|
|Last Update Date|string|False|Last update date|
|Geographic Location|string|False|Geographic location|
|Tags|[]string|False|Tags|
|Related Malware|[]string|False|Related malware|
|Related Campaigns|[]string|False|Related campaigns|
|Related Threat Actors|[]string|False|Related threat actors|
|Status|string|False|Status|
|Reported Feeds|[]reported_feed|False|Reported Feeds|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 5.0.0 - Add action Get IOCs By Filter which returns a list of paginated IOC data based on input filters applied against IOC properties | Fix Bug relating to mismatched property names of output types geolocation, sources, and reported feeds for Get Indicator by Value action
* 4.0.0 - Rename Plugin to Threat Command | Update descriptions to Threat Command | Update Get Indicator By Value to use API V3 | Remove Rescan Indicator and Get Indicator Scan Status | Update Get CVE List to request one page of results only
* 3.2.0 - Fix is_closed bug in trigger | Add new input `source_date_from_enum` in trigger which allows user to specifiy Source Date From using ENUM rather than timestamp/string
* 3.1.0 - Add new actions Add CVEs, Delete CVEs and Get CVE List
* 3.0.1 - Fix issue where New Alert trigger sends empty list when there are no new alerts
* 3.0.0 - Add `assets` custom output type in Add Manual Alert action | Fix missing URL bug in DarkWeb Webmail alerts in Add Manual Alert action
* 2.0.0 - Add new trigger New Alert | Add new action Get CVE by ID
* 1.0.0 - Initial plugin

# Links

* [Threat Command](https://www.rapid7.com/products/threat-command)

## References

* [Threat Command](https://www.rapid7.com/products/threat-command)
