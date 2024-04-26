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
* Get IOCs by Filter
* Get Cyber Terms by Filter
* Get IOCs for Cyber Term
* Get CVEs for Cyber Term
* Close Alert

# Requirements

* Requires an Account ID for Threat Command
* Requires API key for Threat Command

# Supported Product Versions

* 2.4.0

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|account_id|string|None|True|Account ID for Threat Command|None|9de5069c5afe602b2ea0a04b|None|None|
|api_key|credential_secret_key|None|True|API key for Threat Command|None|cc805d5fab1fd71a4ab352a9c533e65fb2d5b885518f4e565e68847223b8e6b85cb48f3afad842726d99239c9e36505c64b0dc9a061d9e507d833277ada336ab|None|None|

Example input:

```
{
  "account_id": "9de5069c5afe602b2ea0a04b",
  "api_key": "cc805d5fab1fd71a4ab352a9c533e65fb2d5b885518f4e565e68847223b8e6b85cb48f3afad842726d99239c9e36505c64b0dc9a061d9e507d833277ada336ab"
}
```

## Technical Details

### Actions


#### Add CVEs

This action is used to add CVEs to account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cve_id|[]string|None|False|List of CVE IDs|None|["CVE-2020-0711"]|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|failure|[]cve_failure_type|True|Failure details|[ { "cveId": "CVE-1999-003", "failReason": "Invalid CVE format" } ]|
|success_amount|integer|True|Amount of successfully added CVEs|2|
  
Example output:

```
{
  "failure": [
    {
      "cveId": "CVE-1999-003",
      "failReason": "Invalid CVE format"
    }
  ],
  "success_amount": 2
}
```

#### Add Manual Alert

This action is used to create a manual alert with the provided parameters

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|description|string|None|True|Alert description|None|Suspicious addresses|None|None|
|found_date|string|None|False|Alert found date|None|2020-01-01|None|None|
|images|[]image|None|False|Alert images|None|[{"Type": "jpeg","Data": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="}]|None|None|
|severity|string|None|True|Alert severity|["High", "Medium", "Low"]|Medium|None|None|
|source_date|string|None|False|Alert source date|None|2020-02-01|None|None|
|source_network_type|string|None|True|Source network type|["ClearWeb", "DarkWeb"]|DarkWeb|None|None|
|source_type|string|None|True|Source type|["Application Store", "Cyber Security Blog", "Hacking News", "Cyber Crime Forum", "Hacktivism Forum", "Social Media", "Facebook", "Twitter", "LinkedIn", "Google Plus", "VK", "Vimeo", "YouTube", "IRC Channel", "IOC Block List", "Credit Card Black Market", "Paste Site", "Data Leakage Website", "Leaked Database", "File Sharing Website", "Gray Hat Website", "Black Market", "WHOIS servers", "Company Website", "Wikileaks", "Pinterest", "Tumblr", "Instagram", "Telegram", "Webmail", "Malware Analysis", "Firehol", "VRA"]|Webmail|None|None|
|source_url|string|None|True|Source URL|None|https://example.com|None|None|
|sub_type|string|None|True|Alert sub type, needs to correlate with the selected "Type"|None|SuspiciousEmailAddress|None|None|
|title|string|None|True|Alert title|None|New Alert|None|None|
|type|string|None|True|Alert type|["AttackIndication", "DataLeakage", "Phishing", "BrandSecurity", "ExploitableData", "vip"]|Phishing|None|None|
  
Example input:

```
{
  "description": "Suspicious addresses",
  "found_date": "2020-01-01",
  "images": [
    {
      "Data": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
      "Type": "jpeg"
    }
  ],
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
| :--- | :--- | :--- | :--- | :--- |
|alert_id|string|True|New created alert ID|6156586e8eadf90008176450|
  
Example output:

```
{
  "alert_id": "6156586e8eadf90008176450"
}
```

#### Close Alert

This action is used to close the alert with the given ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alertId|string|None|True|Alert's unique ID|None|9de5069c5afe602b2ea0a04b|None|None|
|freeText|string|None|False|Alert's comments|None|Example comment|None|None|
|isHidden|boolean|False|True|Alert's hidden status. Delete alert from the account instance - only when reason is False Positive|None|False|None|None|
|rate|integer|None|False|Alert's rate|None|5|None|None|
|reason|string|None|True|Alert's closed reason|["Problem solved", "Informational only", "Problem we are already aware of", "Company owned domain", "Legitimate application/profile", "Not related to my company", "False positive", "Other"]|False Positive|None|None|
  
Example input:

```
{
  "alertId": "9de5069c5afe602b2ea0a04b",
  "freeText": "Example comment",
  "isHidden": false,
  "rate": 5,
  "reason": "False Positive"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|Whether the action was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete CVEs

This action is used to delete CVEs from account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cve_id|[]string|None|False|List of CVE IDs|None|["CVE-2020-0711"]|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|failure|[]cve_failure_type|True|Failure details|[]|
|success_amount|integer|True|Amount of successfully deleted CVEs|3|
  
Example output:

```
{
  "failure": [],
  "success_amount": 3
}
```

#### Enrich Indicator

This action is used to submit an indicator to Threat Command for investigation and return the results

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|indicator_value|string|None|True|Value of the indicator. Examples: IP address, URL, domain name, hash|None|example.com|None|None|
  
Example input:

```
{
  "indicator_value": "example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|object|False|Data|{ "Subdomains": [ "itunes", "apps" ], "Tags": [], "Type": "Domains", "Value": "example.com", "Whitelisted": true, "IsKnownIoc": false, "RelatedHashes": { "downloaded": [ "5d8c914e53bf34fdeac7441b99fe412240a1211fe2e074dfb2...", "7d2970c279d399214f83f140bb509441e9ae7262f98e8ae41f..." ], "referencing": [ "004b5bb9d28f03397ab3462863cd5902", "00f44bc82df0e8808b70abad0993bdb3" ], "communicating": [ "03b0f52b4d517d2a4f8a7994acd26adb77b8c7d9b25ef37c9a...", "09277de376a14f6475a242ca9ad4743dc81bd951853228d625..." ] }, "RelatedThreatActors": [], "Sources": [], "Whois": { "Current": { "RegistrantDetails": [ { "City": "Cupertino", "Country": "UNITED STATES", "CountryCode": "US", "PostalCode": "95014", "Telephone": "14089961010", "State": "", "Address": "One Apple Park Way", "Email": "user@example.com", "Fax": "14089741560", "Name": "Apple Inc.", "Organization": "Apple Inc." } ], "RegistrationDetails": { "CreatedDate": "1987-02-19T00:00:00.000Z", "ExpiresDate": "2022-02-20T05:00:00.000Z", "NameServers": [ "b.ns.apple.com", "a.ns.apple.com" ], "Statuses": [ "clientTransferProhibited", "serverDeleteProhibited" ], "UpdatedDate": "2021-02-16T01:26:20.000Z" } }, "History": [ { "RegistrantDetails": [ { "Address": "1 Infinite Loop", "Country": "UNITED STATES", "Fax": "14089741560", "Name": "Domain Administrator", "Telephone": "14089961010", "State": "CA", "City": "Cupertino", "CountryCode": "", "Email": "user@example.com", "Organization": "Apple Inc.", "PostalCode": "95014" }, { "Address": "1 Infinite Loop", "CountryCode": "", "Email": "user@example.com", "Fax": "14089741560", "Organization": "Apple Inc.", "Telephone": "14089961010", "City": "Cupertino", "Country": "UNITED STATES", "Name": "Domain Administrator", "PostalCode": "95014", "State": "CA" } ], "RegistrationDetails": { "CreatedDate": "1987-02-19T01:27:12.000Z", "ExpiresDate": "2021-02-20T01:27:12.000Z", "NameServers": [ "ADNS1.APPLE.COM", "ADNS2.APPLE.COM" ], "Statuses": [ "clientTransferProhibited" ], "UpdatedDate": "2012-12-04T01:27:12.000Z" } }, { "RegistrantDetails": [ { "City": "Cupertino", "CountryCode": "", "Email": "user@example.com", "Fax": "", "Name": "Domain Administrator", "State": "CA", "Telephone": "14089961010", "Address": "1 Infinite Loop", "Organization": "Apple Inc.", "PostalCode": "95014", "Country": "UNITED STATES" }, { "Address": "1 Infinite Loop", "City": "Cupertino", "Fax": "", "PostalCode": "95014", "State": "CA", "Telephone": "14089961010", "Country": "UNITED STATES", "CountryCode": "", "Email": "user@example.com", "Name": "Domain Administrator", "Organization": "Apple Inc." } ], "RegistrationDetails": { "UpdatedDate": "2012-12-04T13:10:47.000Z", "CreatedDate": "1987-02-19T13:10:47.000Z", "ExpiresDate": "2021-02-20T13:10:47.000Z", "NameServers": [ "ADNS1.APPLE.COM", "ADNS2.APPLE.COM" ], "Statuses": [ "clientTransferProhibited" ] } } ] }, "DnsRecords": [ { "Type": "NS", "Value": "a.ns.apple.com.", "Count": 123, "FirstResolved": null, "LastResolved": null }, { "FirstResolved": null, "LastResolved": null, "Type": "NS", "Value": "b.ns.apple.com.", "Count": 123 } ], "RelatedMalwares": [], "Resolutions": [ { "ResolvedIpAddress": "17.253.144.10", "ASN": 714, "FirstResolved": "2020-10-09T02:47:17.000Z", "LastResolved": "2021-09-18T13:35:55.000Z", "Location": "US", "Operator": "Apple Inc.", "ReportingSources": [ "Farsight", "VirusTotal" ] }, { "ResolvedIpAddress": "17.142.160.59", "ASN": 714, "FirstResolved": "2014-07-09T16:35:28.000Z", "LastResolved": "2020-10-09T03:00:19.000Z", "Location": "US", "Operator": "Apple Inc.", "ReportingSources": [ "Farsight", "VirusTotal" ] } ], "SystemTags": [], "RelatedCampaigns": [], "Severity": { "Score": 0, "Value": "Low" } }|
|original_value|string|True|Original value|example.com|
|status|string|True|Status|Done|
  
Example output:

```
{
  "data": {
    "DnsRecords": [
      {
        "Count": 123,
        "FirstResolved": null,
        "LastResolved": null,
        "Type": "NS",
        "Value": "a.ns.apple.com."
      },
      {
        "Count": 123,
        "FirstResolved": null,
        "LastResolved": null,
        "Type": "NS",
        "Value": "b.ns.apple.com."
      }
    ],
    "IsKnownIoc": false,
    "RelatedCampaigns": [],
    "RelatedHashes": {
      "communicating": [
        "03b0f52b4d517d2a4f8a7994acd26adb77b8c7d9b25ef37c9a...",
        "09277de376a14f6475a242ca9ad4743dc81bd951853228d625..."
      ],
      "downloaded": [
        "5d8c914e53bf34fdeac7441b99fe412240a1211fe2e074dfb2...",
        "7d2970c279d399214f83f140bb509441e9ae7262f98e8ae41f..."
      ],
      "referencing": [
        "004b5bb9d28f03397ab3462863cd5902",
        "00f44bc82df0e8808b70abad0993bdb3"
      ]
    },
    "RelatedMalwares": [],
    "RelatedThreatActors": [],
    "Resolutions": [
      {
        "ASN": 714,
        "FirstResolved": "2020-10-09T02:47:17.000Z",
        "LastResolved": "2021-09-18T13:35:55.000Z",
        "Location": "US",
        "Operator": "Apple Inc.",
        "ReportingSources": [
          "Farsight",
          "VirusTotal"
        ],
        "ResolvedIpAddress": "17.253.144.10"
      },
      {
        "ASN": 714,
        "FirstResolved": "2014-07-09T16:35:28.000Z",
        "LastResolved": "2020-10-09T03:00:19.000Z",
        "Location": "US",
        "Operator": "Apple Inc.",
        "ReportingSources": [
          "Farsight",
          "VirusTotal"
        ],
        "ResolvedIpAddress": "17.142.160.59"
      }
    ],
    "Severity": {
      "Score": 0,
      "Value": "Low"
    },
    "Sources": [],
    "Subdomains": [
      "itunes",
      "apps"
    ],
    "SystemTags": [],
    "Tags": [],
    "Type": "Domains",
    "Value": "example.com",
    "Whitelisted": true,
    "Whois": {
      "Current": {
        "RegistrantDetails": [
          {
            "Address": "One Apple Park Way",
            "City": "Cupertino",
            "Country": "UNITED STATES",
            "CountryCode": "US",
            "Email": "user@example.com",
            "Fax": "14089741560",
            "Name": "Apple Inc.",
            "Organization": "Apple Inc.",
            "PostalCode": "95014",
            "State": "",
            "Telephone": "14089961010"
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
              "City": "Cupertino",
              "Country": "UNITED STATES",
              "CountryCode": "",
              "Email": "user@example.com",
              "Fax": "14089741560",
              "Name": "Domain Administrator",
              "Organization": "Apple Inc.",
              "PostalCode": "95014",
              "State": "CA",
              "Telephone": "14089961010"
            },
            {
              "Address": "1 Infinite Loop",
              "City": "Cupertino",
              "Country": "UNITED STATES",
              "CountryCode": "",
              "Email": "user@example.com",
              "Fax": "14089741560",
              "Name": "Domain Administrator",
              "Organization": "Apple Inc.",
              "PostalCode": "95014",
              "State": "CA",
              "Telephone": "14089961010"
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
              "Address": "1 Infinite Loop",
              "City": "Cupertino",
              "Country": "UNITED STATES",
              "CountryCode": "",
              "Email": "user@example.com",
              "Fax": "",
              "Name": "Domain Administrator",
              "Organization": "Apple Inc.",
              "PostalCode": "95014",
              "State": "CA",
              "Telephone": "14089961010"
            },
            {
              "Address": "1 Infinite Loop",
              "City": "Cupertino",
              "Country": "UNITED STATES",
              "CountryCode": "",
              "Email": "user@example.com",
              "Fax": "",
              "Name": "Domain Administrator",
              "Organization": "Apple Inc.",
              "PostalCode": "95014",
              "State": "CA",
              "Telephone": "14089961010"
            }
          ],
          "RegistrationDetails": {
            "CreatedDate": "1987-02-19T13:10:47.000Z",
            "ExpiresDate": "2021-02-20T13:10:47.000Z",
            "NameServers": [
              "ADNS1.APPLE.COM",
              "ADNS2.APPLE.COM"
            ],
            "Statuses": [
              "clientTransferProhibited"
            ],
            "UpdatedDate": "2012-12-04T13:10:47.000Z"
          }
        }
      ]
    }
  },
  "original_value": "example.com",
  "status": "Done"
}
```

#### Get Alerts

This action is used to search alerts based on criteria

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_type|[]string|None|False|List of alert types. Allowed values: AttackIndication, DataLeakage, Phishing, BrandSecurity, ExploitableData, vip|None|["Phishing"]|None|None|
|assigned|string|None|False|Show assigned/unassigned alerts|["Assigned", "Unassigned", ""]|Assigned|None|None|
|found_date_from|string|None|False|Start date (when alert found event) to fetch from in Unix Millisecond Timestamp|None|0|None|None|
|found_date_to|string|None|False|End date (when alert found event) to fetch to in Unix Millisecond Timestamp|None|1633047102456|None|None|
|has_indicators|boolean|None|False|Show alerts with IOCs results|None|False|None|None|
|is_closed|string|None|False|Status of the alert, either closed or open|["Closed", "Open", ""]|Closed|None|None|
|is_flagged|string|None|False|Show flagged/unflagged alerts|["Flagged", "Unflagged", ""]|Flagged|None|None|
|matched_asset_value|[]string|None|False|List of matched asset values. Examples: IP address, domain name, company name|None|["example.com"]|None|None|
|network_type|[]string|None|False|List of network type. Allowed values: ClearWeb, DarkWeb|None|["DarkWeb"]|None|None|
|remediation_status|[]string|None|False|List of remediation statuses. Allowed values: InProgress, Pending, CancellationInProgress, Cancelled, CompletedSuccessfully, Failed|None|["InProgress", "Pending"]|None|None|
|severity|[]string|None|False|List of alerts severity. Allowed values: High, Medium, Low|None|["Low"]|None|None|
|source_date_from|string|None|False|Start date (when the event occurred) to fetch from in Unix Millisecond Timestamp|None|1633047083142|None|None|
|source_date_to|string|None|False|End date (when the event occurred) to fetch to in Unix Millisecond Timestamp|None|1633047102456|None|None|
|source_type|[]string|None|False|List of alerts source type. Allowed values: Application Store, Cyber Security Blog, Hacking News, Cyber Crime Forum, Hacktivism Forum, Social Media, Facebook, Twitter, LinkedIn, Google Plus, VK, Vimeo, YouTube, IRC Channel, IOC Block List, Credit Card Black Market, Paste Site, Data Leakage Website, Leaked Database, File Sharing Website, Gray Hat Website, Black Market, WHOIS servers, Company Website, Wikileaks, Pinterest, Tumblr, Instagram, Telegram, Webmail, Malware Analysis, Firehol, VRA, Other|None|["Application Store"]|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
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

#### Get Complete Alert by ID

This action is used to get an alert's complete details for a given alert ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_id|string|None|True|Alert's unique ID|None|44d88612fea8a8f36de82e12|None|None|
  
Example input:

```
{
  "alert_id": "44d88612fea8a8f36de82e12"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|assets|[]asset|True|List of assets|[ { "Type": "Domain", "Value": "https://example.com" } ]|
|assignees|[]string|True|List of assignees|[]|
|details|alert_details|True|Alert details|{ "Description": "APIDescription", "Images": [ "61efc2286b02dcd558929918" ], "Severity": "High", "Source": { "NetworkType": "ClearWeb", "Type": "Application Store", "URL": "https://example.com" }, "SubType": "SuspiciousEmailAddress", "Tags": [], "Title": "Alerttest3", "Type": "Phishing" }|
|found_date|date|False|Alert found date|2018-01-01 20:01:27.344000+00:00|
|id|string|False|Alert ID|6156118e186a05000774ee46|
|is_closed|boolean|True|Is alert closed|False|
|is_flagged|boolean|True|Is alert flagged|False|
|leak_name|string|False|Name of the leak DBs in data leakage alerts|example.com|
|takedown_status|string|False|Alert remediation status|NotSent|
|update_date|date|False|Alert update date|2018-01-01 20:01:27.344000+00:00|
  
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
  "found_date": "2018-01-01 20:01:27.344000+00:00",
  "id": "6156118e186a05000774ee46",
  "is_closed": false,
  "is_flagged": false,
  "leak_name": "example.com",
  "takedown_status": "NotSent",
  "update_date": "2018-01-01 20:01:27.344000+00:00"
}
```

#### Get CVE by ID

This action is used to get a list of CVE's with a list of IDs from an account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cve_id|[]string|None|False|Specific CVE IDs|None|["CVE-2020-0711"]|None|None|
  
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
| :--- | :--- | :--- | :--- | :--- |
|content|[]content|False|Response content|[ { "cveId": "CVE-2020-7064", "cpe": [ { "Value": "cpe:2.3:a:php:php:*:*:*:*:*:*:*:*", "Range": { "VersionStartIncluding": "7.2.0", "VersionEndIncluding": "", "VersionStartExcluding": "", "VersionEndExcluding": "7.2.9" }, "Title": "Php", "VendorProduct": "Php Php" } ], "publishedDate": "2020-04-01T04:15:00.000Z", "updateDate": "2021-10-25T10:14:52.978Z", "severity": "Low", "intsightsScore": 36, "cvssScore": 5.4, "mentionsAmount": 39, "mentionsPerSource": { "PasteSite": 0, "HackingForum": 0, "InstantMessage": 0, "DarkWeb": 0, "ClearWebCyberBlogs": 0, "CodeRepositories": 9, "Exploit": 0, "SocialMedia": 30 }, "firstMentionDate": "2020-03-19T15:09:00.000Z", "lastMentionDate": "2021-07-22T20:41:00.000Z", "exploitAvailability": false, "vulnerabilityOrigin": [ "API" ], "relatedThreatActors": [], "relatedMalware": [], "relatedCampaigns": [] } ]|
  
Example output:

```
{
  "content": [
    {
      "cpe": [
        {
          "Range": {
            "VersionEndExcluding": "7.2.9",
            "VersionEndIncluding": "",
            "VersionStartExcluding": "",
            "VersionStartIncluding": "7.2.0"
          },
          "Title": "Php",
          "Value": "cpe:2.3:a:php:php:*:*:*:*:*:*:*:*",
          "VendorProduct": "Php Php"
        }
      ],
      "cveId": "CVE-2020-7064",
      "cvssScore": 5.4,
      "exploitAvailability": false,
      "firstMentionDate": "2020-03-19T15:09:00.000Z",
      "intsightsScore": 36,
      "lastMentionDate": "2021-07-22T20:41:00.000Z",
      "mentionsAmount": 39,
      "mentionsPerSource": {
        "ClearWebCyberBlogs": 0,
        "CodeRepositories": 9,
        "DarkWeb": 0,
        "Exploit": 0,
        "HackingForum": 0,
        "InstantMessage": 0,
        "PasteSite": 0,
        "SocialMedia": 30
      },
      "publishedDate": "2020-04-01T04:15:00.000Z",
      "relatedCampaigns": [],
      "relatedMalware": [],
      "relatedThreatActors": [],
      "severity": "Low",
      "updateDate": "2021-10-25T10:14:52.978Z",
      "vulnerabilityOrigin": [
        "API"
      ]
    }
  ]
}
```

#### Get CVE List

This action is used to get a partial list of all CVEs from an account

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|offset|string|None|False|Offset value for pagination, if empty the first page of results will be returned|None|2000-00-00T00:00:00.000Z::614b8972da44a60005036b01|None|None|
  
Example input:

```
{
  "offset": "2000-00-00T00:00:00.000Z::614b8972da44a60005036b01"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
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
  "next_offset": "2000-00-00T00:00:00.000Z::614b8972da44a60005036b01"
}
```

#### Get CVEs for Cyber Term

This action is used to get the Common Vulnerabilities and Exposures that are related to a cyber term

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cyberTermId|string|None|True|Cyber term unique ID|None|311g8204kf82mr1234ab987o|None|None|
  
Example input:

```
{
  "cyberTermId": "311g8204kf82mr1234ab987o"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|cyberTermCves|[]cyberTermCve|True|List of Common Vulnerabilities and Exposures related to the cyber term|[]|
  
Example output:

```
{
  "cyberTermCves": []
}
```

#### Get Cyber Terms by Filter

This action is used to get cyber terms for given filters

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|lastUpdateFrom|date|None|False|Filter by last update date is greater than the given value (in ISO 8601 format)|None|2022-09-29 13:45:55.627000+00:00|None|None|
|lastUpdateTo|date|None|False|Filter by last update date is less than the given value (in ISO 8601 format)|None|2022-09-30 13:45:55.627000+00:00|None|None|
|limit|integer|None|False|Limit the results amount per chunk. Default value: 200|None|100|None|None|
|offset|string|None|False|Request the next page of cyber terms|None|2022-09-29T13:45:55.627Z::9de5069c5afe602b2ea0a04b66beb2c0|None|None|
|origin|[]string|None|False|Filter by one or more nationalities|None|["Korea, Republic of"]|None|None|
|search|string|None|False|Filter by free text, which can be the cyber term name or ID|None|9de5069c5afe602b2ea0a04b|None|None|
|severity|[]string|None|False|Filter by one or more cyber term severities. Allowed values: High, Medium, Low|None|["Medium", "High"]|None|None|
|targetCountry|[]string|None|False|Filter by one or more targeted countries|None|["United Status"]|None|None|
|targetSector|[]string|None|False|Filter by one or more targeted sectors|None|["Electronics"]|None|None|
|ttp|[]string|None|False|Filter by one or more TTPs|None|["Code Execution"]|None|None|
|type|[]string|None|False|Filter by one or more cyber term types. Allowed values: ThreatActor, Malware, Campaign|None|["ThreatActor"]|None|None|
  
Example input:

```
{
  "lastUpdateFrom": "2022-09-29 13:45:55.627000+00:00",
  "lastUpdateTo": "2022-09-30 13:45:55.627000+00:00",
  "limit": 100,
  "offset": "2022-09-29T13:45:55.627Z::9de5069c5afe602b2ea0a04b66beb2c0",
  "origin": [
    "Korea, Republic of"
  ],
  "search": "9de5069c5afe602b2ea0a04b",
  "severity": [
    "Medium",
    "High"
  ],
  "targetCountry": [
    "United Status"
  ],
  "targetSector": [
    "Electronics"
  ],
  "ttp": [
    "Code Execution"
  ],
  "type": [
    "ThreatActor"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|cyberTerms|[]cyberTerm|False|List of cyber terms that match the given filters|[]|
|nextOffset|string|False|Indicator of the next page of cyber terms|2022-09-29T13:45:55.627Z::9de5069c5afe602b2ea0a04b66beb2c0|
  
Example output:

```
{
  "cyberTerms": [],
  "nextOffset": "2022-09-29T13:45:55.627Z::9de5069c5afe602b2ea0a04b66beb2c0"
}
```

#### Get Indicator by Value

This action is used to search indicators in Threat Command TIP

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|indicator_value|string|None|True|Value of the indicator. Examples: IP address, URL, domain name, hash|None|6c62e74dd5d99fc2d610bd84114990a2|None|None|
  
Example input:

```
{
  "indicator_value": "6c62e74dd5d99fc2d610bd84114990a2"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|first_seen|string|False|First seen|2020-01-01 20:01:27.344000+00:00|
|geo_location|string|False|Geographic location|US|
|last_seen|string|False|Last seen|2020-01-01 20:01:27.344000+00:00|
|last_update|string|False|Last update|2020-01-01 20:01:27.344000+00:00|
|related_campaigns|[]string|False|Related campaigns|["doppeldridex", "dridex"]|
|related_malware|[]string|False|Related malware|example.com|
|related_threat_actors|[]string|False|Related threat actors|["doppelspider"]|
|reported_feeds|[]reported_feed|False|Reported Feeds|[ { "ID": "SampleID", "Name": "AlienVault OTX", "ConfidenceLevel": 3 } ]|
|score|float|False|Score|10|
|severity|string|False|Severity|Low|
|sources|[]source|False|Sources|[ { "confidenceLevel": 2, "name": "Cyber Threat Alliance" } ]|
|status|string|False|Status|Active|
|subtype|string|False|SubType Value|MD5|
|system_tags|[]string|False|System tags|["MyTag_1"]|
|tags|[]string|False|Tags|["MyTag_1"]|
|type|string|False|Type|Hashes|
|value|string|False|Indicator value|6c62e74dd5d99fc2d610bd84114990a2|
|whitelist|boolean|False|Whitelist|True|
  
Example output:

```
{
  "first_seen": "2020-01-01 20:01:27.344000+00:00",
  "geo_location": "US",
  "last_seen": "2020-01-01 20:01:27.344000+00:00",
  "last_update": "2020-01-01 20:01:27.344000+00:00",
  "related_campaigns": [
    "doppeldridex",
    "dridex"
  ],
  "related_malware": "example.com",
  "related_threat_actors": [
    "doppelspider"
  ],
  "reported_feeds": [
    {
      "ConfidenceLevel": 3,
      "ID": "SampleID",
      "Name": "AlienVault OTX"
    }
  ],
  "score": 10,
  "severity": "Low",
  "sources": [
    {
      "confidenceLevel": 2,
      "name": "Cyber Threat Alliance"
    }
  ],
  "status": "Active",
  "subtype": "MD5",
  "system_tags": [
    "MyTag_1"
  ],
  "tags": [
    "MyTag_1"
  ],
  "type": "Hashes",
  "value": "6c62e74dd5d99fc2d610bd84114990a2",
  "whitelist": true
}
```

#### Get IOCs by Filter

This action is used to get Indicators of Compromise by Filter

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|enterprise_tactics|[]string|None|False|Filter by MITRE ATT&CK Enterprise tactic. Allowed values 'Reconnaissance', 'Resource Development', 'Initial Access', 'Execution', 'Persistence', 'Privilege Escalation', 'Defense Evasion', 'Credential Access', 'Discovery', 'Lateral Movement', 'Collection', 'Command and Control', 'Exfiltration', 'Impact'|None|["Reconnaissance"]|None|None|
|first_seen_from|date|None|False|Filter by first seen date (IOC first-seen date is greater than)|None|2000-12-31T00:00:00Z|None|None|
|first_seen_to|date|None|False|Filter by first seen date (IOC first-seen date is less than)|None|2000-12-31T00:00:00Z|None|None|
|kill_chain_phases|[]string|None|False|Filter by phase of Lockheed-Martin intrusion kill chain (Allowed values: Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command and Control, Actions on Objective)|None|["Command and Control"]|None|None|
|last_seen_from|date|None|False|Filter by last seen date (IOC last-seen date is greater than)|None|2000-12-31T00:00:00Z|None|None|
|last_seen_to|date|None|False|Filter by last seen date (IOC last-seen date is less than)|None|2000-12-31T00:00:00Z|None|None|
|last_updated_from|date|None|True|Filter by last update date (IOC update date is greater than)|None|2000-12-31T00:00:00Z|None|None|
|last_updated_to|date|None|False|Filter by last update date (IOC update date is less than)|None|2000-12-31T00:00:00Z|None|None|
|limit|integer|1000|False|Limit the results amount per page (1-1000)|None|1000|None|None|
|offset|string|None|False|Getting the next page of IOCs from offset|None|2020-01-01T20:01:27.344Z|None|None|
|severity|[]string|None|False|Filter by IOC severity (Allowed values: High, Medium, Low)|None|["High"]|None|None|
|source_ids|[]string|None|False|Filter by source IDs|None|["123450000012345000001233"]|None|None|
|status|string|None|False|Filter by IOC status|["", "Active", "Retired"]|Active|None|None|
|type|[]string|None|False|Filter by IOC type (Allowed values: IpAddresses, Urls, Domains, Hashes, Emails)|None|["IpAddresses"]|None|None|
  
Example input:

```
{
  "enterprise_tactics": [
    "Reconnaissance"
  ],
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
| :--- | :--- | :--- | :--- | :--- |
|content|[]ioc_content|False|List of IOCs that match filters|{ "content": [ { "value": "rapid7.com", "type": "Domains", "severity": "High", "score": 100, "whitelisted": false, "firstSeen": "2020-01-01T20:01:27.344Z", "lastSeen": "2020-01-30T16:18:51.148Z", "lastUpdateDate": "2020-02-21T23:00:51.268Z", "geolocation": "US", "tags": [ "MyTag_1" ], "relatedMalware": [ "doppeldridex", "dridex" ], "relatedCampaigns": [ "SolarWinds" ], "relatedThreatActors": [ "doppelspider" ], "reportedFeeds": [ { "ID": "SampleID", "Name": "AlienVault OTX", "ConfidenceLevel": 3 } ] } ], "nextOffset": "2022-11-18T16:59:01.626Z" }|
|nextOffset|string|False|The offset to the next page of IOCs|2020-01-01T20:01:27.344Z|
  
Example output:

```
{
  "content": {
    "content": [
      {
        "firstSeen": "2020-01-01T20:01:27.344Z",
        "geolocation": "US",
        "lastSeen": "2020-01-30T16:18:51.148Z",
        "lastUpdateDate": "2020-02-21T23:00:51.268Z",
        "relatedCampaigns": [
          "SolarWinds"
        ],
        "relatedMalware": [
          "doppeldridex",
          "dridex"
        ],
        "relatedThreatActors": [
          "doppelspider"
        ],
        "reportedFeeds": [
          {
            "ConfidenceLevel": 3,
            "ID": "SampleID",
            "Name": "AlienVault OTX"
          }
        ],
        "score": 100,
        "severity": "High",
        "tags": [
          "MyTag_1"
        ],
        "type": "Domains",
        "value": "rapid7.com",
        "whitelisted": false
      }
    ],
    "nextOffset": "2022-11-18T16:59:01.626Z"
  },
  "nextOffset": "2020-01-01T20:01:27.344Z"
}
```

#### Get IOCs for Cyber Term

This action is used to gets cyber term IOCs by cyber term ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cyberTermId|string|None|True|Cyber term unique ID|None|593e74cfc022ac015814f8d9|None|None|
|iocType|[]string|None|False|IOC types to include. Allowed values "IpAddresses", "Urls", "Domains", "Hashes", "Emails"|None|["IpAddresses"]|None|None|
|limit|integer|None|False|Desired number of results. Default value 100. Size range 1-1000|None|100|None|None|
|offset|string|None|False|Request the next page of IOCs|None|2020-08-13T12:17:08.755Z|None|None|
  
Example input:

```
{
  "cyberTermId": "593e74cfc022ac015814f8d9",
  "iocType": [
    "IpAddresses"
  ],
  "limit": 100,
  "offset": "2020-08-13T12:17:08.755Z"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|iocs|[]indicator|False|List of IOCs|[]|
|nextOffset|string|False|Next offset value for pagination|2020-08-13T12:17:08.755Z|
  
Example output:

```
{
  "iocs": [],
  "nextOffset": "2020-08-13T12:17:08.755Z"
}
```

#### Takedown Request

This action is used to request a takedown for a given alert in Threat Command

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_id|string|None|True|Alert's unique ID|None|44d88612fea8a8f36de82e12|None|None|
|target|string|Domain|True|Target|["Website", "Domain"]|Domain|None|None|
  
Example input:

```
{
  "alert_id": "44d88612fea8a8f36de82e12",
  "target": "Domain"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|status|boolean|True|Status from Threat Command|True|
  
Example output:

```
{
  "status": true
}
```
### Triggers


#### New Alert

This trigger is used to triggers when a new alert that matches the given criteria is created in Threat Command

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|alert_type|[]string|None|False|List of alert types. Allowed values: AttackIndication, DataLeakage, Phishing, BrandSecurity, ExploitableData, vip|None|["Phishing"]|None|None|
|assigned|string|None|False|Show assigned/unassigned alerts|["Assigned", "Unassigned", ""]|Assigned|None|None|
|found_date_from|string|None|False|Start date (when alert found event) to fetch from in Unix Millisecond Timestamp|None|0|None|None|
|found_date_to|string|None|False|End date (when alert found event) to fetch to in Unix Millisecond Timestamp|None|1633047102456|None|None|
|frequency|integer|60|False|Poll frequency in seconds|None|60|None|None|
|has_indicators|boolean|None|False|Shows alerts with IOC results|None|False|None|None|
|is_closed|string|None|False|Status of the alert, either closed or open|["Closed", "Open", ""]|Closed|None|None|
|is_flagged|string|None|False|Show flagged/unflagged alerts|["Flagged", "Unflagged", ""]|Flagged|None|None|
|matched_asset_value|[]string|None|False|List of matched asset values. Examples: IP address, domain name, company name|None|["example.com"]|None|None|
|network_type|[]string|None|False|List of network types. Allowed values: ClearWeb, DarkWeb|None|["DarkWeb"]|None|None|
|remediation_status|[]string|None|False|List of remediation statuses. Allowed values: InProgress, Pending, CancellationInProgress, Cancelled, CompletedSuccessfully, Failed|None|["InProgress", "Pending"]|None|None|
|severity|[]string|None|False|List of alerts severity. Allowed values: High, Medium, Low|None|["Low"]|None|None|
|source_date_from|string|None|False|Start date (when the event occured) to fetch from in Unix Millisecond Timestamp|None|1633047083142|None|None|
|source_date_from_enum|string|None|False|Start date to fetch from with options, such as choose Hour to pull alerts in the last hour|["Hour", "Day", "Week", ""]|Hour|None|None|
|source_date_to|string|None|False|End date (when the event occured) to fetch to in Unix Millisecond Timestamp|None|1633047102456|None|None|
|source_type|[]string|None|False|List of alert's source type. Allowed values: Application Store, Cyber Security Blog, Hacking News, Cyber Crime Forum, Hacktivism Forum, Social Media, Facebook, Twitter, LinkedIn, Google Plus, VK, Vimeo, YouTube, IRC Channel, IOC Block List, Credit Card Black Market, Paste Site, Data Leakage Website, Leaked Database, File Sharing Website, Gray Hat Website, Black Market, WHOIS servers, Company Website, Wikileaks, Pinterest, Tumblr, Instagram, Telegram, Webmail, Malware Analysis, Firehol, VRA, Other|None|["Application Store"]|None|None|
  
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
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alert_ids|[]string|True|List of alert IDs|["618305318f3b3c0007d2cac0"]|
  
Example output:

```
{
  "alert_ids": [
    "618305318f3b3c0007d2cac0"
  ]
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**source**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Confidence Level|integer|None|True|Level of confidence|None|
|Name|string|None|True|Name|None|
  
**reported_feed**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Confidence Level|integer|None|False|Level of confidence|None|
|ID|string|None|False|ID|None|
|Name|string|None|False|Name|None|
  
**image**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Data|string|None|True|Data|None|
|Type|string|None|True|Type|None|
  
**alert_source**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Date|string|None|False|Date|None|
|Email|string|None|False|Email|None|
|Network Type|string|None|False|Network type|None|
|Type|string|None|True|Type|None|
|URL|string|None|False|URL|None|
  
**alert_tags**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Created By|string|None|True|Created by|None|
|Name|string|None|True|Name|None|
|ID|string|None|True|ID|None|
  
**alert_details**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Description|string|None|False|Description|None|
|Images|[]string|None|False|Images|None|
|Related IOCs|[]string|None|False|Related IOCs|None|
|Severity|string|None|True|Severity|None|
|Source|alert_source|None|True|Source|None|
|Sub Type|string|None|True|Sub type|None|
|Tags|[]alert_tags|None|False|Tags|None|
|Title|string|None|True|Title|None|
|Type|string|None|True|Type|None|
  
**asset**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Type|string|None|True|Asset type|None|
|Value|string|None|True|Asset value|None|
  
**range**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Version End Excluding|string|None|False|Version end excluding|None|
|Version End Including|string|None|False|Version end including|None|
|Version Start Excluding|string|None|False|Version start excluding|None|
|Version Start Including|string|None|False|Version start including|None|
  
**cpe**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Range|range|None|False|Range|None|
|Title|string|None|False|Title|None|
|Value|string|None|False|Value|None|
|Vendor Product|string|None|False|Vendor product|None|
  
**mentionsPerSource**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Clear Web Cyber Blogs|integer|None|False|Clear web cyber blogs|None|
|Code Repositories|integer|None|False|Code repositories|None|
|Dark Web|integer|None|False|Dark web|None|
|Exploit|integer|None|False|Exploit|None|
|Hacking Forum|integer|None|False|Hacking forum|None|
|Instant Message|integer|None|False|Instant message|None|
|Paste Site|integer|None|False|Paste site|None|
|Social Media|integer|None|False|Social media|None|
  
**content**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CPE|[]cpe|None|False|CPE|None|
|CVE ID|string|None|False|CVE ID|None|
|CVSS Score|float|None|False|Common Vulnerability Scoring System score|None|
|Exploit Availability|boolean|None|False|Exploit availability|None|
|First Mention Date|string|None|False|First mention date|None|
|IntSights Score|float|None|False|IntSights score|None|
|Last Mention Date|string|None|False|Last mention date|None|
|Mentions Amount|integer|None|False|Mentions amount|None|
|Mentions Per Source|mentionsPerSource|None|False|Mentions per source|None|
|Published Date|string|None|False|Published date|None|
|Related Campaigns|[]string|None|False|Related campaigns|None|
|Related Malware|[]string|None|False|Related malware|None|
|Related Threat Actors|[]string|None|False|Related threat actors|None|
|Severity|string|None|False|Severity|None|
|Update Date|string|None|False|Update date|None|
|Vulnerability Origin|[]string|None|False|Vulnerability origin|None|
  
**cve_failure_type**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CVE ID|string|None|True|CVE ID|None|
|Fail Reason|string|None|True|Fail reason|None|
  
**ioc_content**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|First Seen|string|None|False|First seen|None|
|Geographic Location|string|None|False|Geographic location|None|
|Last Seen|string|None|False|Last seen|None|
|Last Update Date|string|None|False|Last update date|None|
|Related Campaigns|[]string|None|False|Related campaigns|None|
|Related Malware|[]string|None|False|Related malware|None|
|Related Threat Actors|[]string|None|False|Related threat actors|None|
|Reported Feeds|[]reported_feed|None|False|Reported Feeds|None|
|Score|float|None|False|Score|None|
|Severity|string|None|False|Severity|None|
|Status|string|None|False|Status|None|
|Tags|[]string|None|False|Tags|None|
|Type|string|None|False|Type|None|
|Indicator Value|string|None|False|Indicator value|None|
|Whitelisted|boolean|None|False|Whitelisted|None|
  
**indicator**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Reporting Feeds|[]string|None|False|Reporting feeds list|["Example Reporting Feeds"]|
|Severity|string|None|False|Severity type|Low|
|Status|string|None|False|IOC status|Retired|
|Type|string|None|False|IOC type|IpAddresses|
|Update Date|string|None|False|IOC update date|2019-12-10T08:13:43.800Z|
|Value|string|None|False|IOC value|198.50.191.194|
|Whitelisted|boolean|None|False|Whitelisted|True|
  
**cyberTermCve**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|CVE ID|string|None|False|The identifier of the CVE|CVE-2005-11111|
|Published Date|string|None|False|Date when CVE was published|2022-09-29 13:45:55.627000+00:00|
|Vendor Products|[]string|None|False|Vendor's product list|["Example Product"]|
  
**technique**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Name|string|None|False|Name of the technique|PowerShell|
|URL|string|None|False|URL|https://example.com|
  
**mitreAttack**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Tactic|string|None|False|MITRE ATT&CK tactic name related to the cyber term|Execution|
|Techniques|[]technique|None|False|List of MITRE ATT&CK technique names and URLs of the MITRE description|[]|
  
**cyberTerm**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Additional Information|string|None|False|Additional information about the cyber term|Example information|
|Aliases|[]string|None|False|Aliases of the cyber term|["Example Alias"]|
|Created Date|string|None|False|The date the cyber term was first reported|2020-07-29 13:36:44.794000+00:00|
|ID|string|None|False|ID of the cyber term|9de5069c5afe602b2ea0a04b|
|Mitre Attack|[]mitreAttack|None|False|MITRE ATT&CK tactics and techniques of the cyber term, divided by tactics|[]|
|Origins|[]string|None|False|List of origin nationalities|["United States"]|
|Overview|string|None|False|Overview of the cyber term|Example overview|
|Related Campaigns|[]string|None|False|Related campaign names|["SolarWinds"]|
|Related Malware|[]string|None|False|Related malware names|["emotet"]|
|Related Threat Actors|[]string|None|False|Related threat actor names|["Lazarus"]|
|Severity|string|None|False|Severity of the cyber term|High|
|Target Countries|[]string|None|False|List of targeted countries|["Germany"]|
|Target Sectors|[]string|None|False|List of targeted sectors|["Computer Software & Services"]|
|TTPs|[]string|None|False|List of TTPs|["Code Execution"]|
|Type|string|None|False|Type of the cyber term|ThreatActor|
|Updated Date|string|None|False|The date the cyber term was last updated|2021-04-14 08:21:57.021000+00:00|
|Value|string|None|False|Name of the cyber term|Example Name|


## Troubleshooting
  
*There is no troubleshooting for this plugin.*

# Version History

* 5.2.0 - Update exception presets in API and unit tests | New `subtype` output to `get_indicator_by_value` action
* 5.1.1 - Better handling of response from the threat connect API when using the `takedown_request` action | Bumped to use the newest version of the SDK | Updated old unit tests / added new unit tests
* 5.1.0 - Add actions -> `Get Cyber Terms by Filter`, `Get IOCs for Cyber Term`, `Get CVEs for Cyber Term`, `Close Alert`. Add new input for `Get IOCs By Filter` action
* 5.0.0 - Add action Get IOCs By Filter which returns a list of paginated IOC data based on input filters applied against IOC properties | Fix Bug relating to mismatched property names of output types geolocation, sources, and reported feeds for Get Indicator by Value action
* 4.0.0 - Rename Plugin to Threat Command | Update descriptions to Threat Command | Update Get Indicator By Value to use API V3 | Remove Rescan Indicator and Get Indicator Scan Status | Update Get CVE List to request one page of results only
* 3.2.0 - Fix is_closed bug in trigger | Add new input `source_date_from_enum` in trigger which allows user to specifiy Source Date From using ENUM rather than timestamp/string
* 3.1.0 - Add new actions Add CVEs, Delete CVEs and Get CVE List
* 3.0.1 - Fix issue where New Alert trigger sends empty list when there are no new alerts
* 3.0.0 - Add `assets` custom output type in Add Manual Alert action | Fix missing URL bug in DarkWeb Webmail alerts in Add Manual Alert action
* 2.0.0 - Add new trigger New Alert | Add new action Get CVE by ID
* 1.0.0 - Initial plugin

# Links

* [Threat Command](https://intsights.com/)

## References

* [Threat Command](https://www.rapid7.com/products/threat-command)
