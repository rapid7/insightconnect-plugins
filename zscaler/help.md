# Description

[Zscaler](https://www.zscaler.com/) is a SaaS security platform that provides fast, secure connections between client applications, regardless of device, location, or network.

# Key Features

* Lookup categories for a given URL
* Add or remove URLs from blacklist

# Requirements

* [Requires a Zscaler organization API Key](https://help.zscaler.com/zia/api-getting-started#RetrieveAPIKey)
* Requires a Zscaler username and password

# Documentation

## Setup

To locate your base URI and key:

1. Log in to the ZIA Admin Portal using your admin credentials.
2. Go to **Administration > API Key Management**.

In order to view the API Key Management page, the admin must be assigned an admin role that includes the Authentication Configuration functional scope.

In the **Organization API Key** tab, the base URI and key details are displayed within the table.

For more information see the [Zscalar getting started guide](https://help.zscaler.com/zia/api-getting-started) on obtaining the API key and base URL.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Enter organization API key|None|14M2d25A7c12|
|credentials|credential_username_password|None|True|Username and password to access Zscaler|None|{"username":"user@example.com", "password":"mypassword"}|
|url|string|None|True|Base URL, see https://help.zscaler.com/zia/api-getting-started#RetrieveAPIKey for details|None|admin.zscalerbeta.net|

Example input:

```
{
  "api_key": "14M2d25A7c12",
  "credentials": {
    "username":"user@example.com",
    "password":"mypassword"
  },
  "url": "admin.zscalerbeta.net"
}
```

## Technical Details

### Actions

#### Get Sandbox Report for Hash

This action is used to get a full report for an MD5 hash of a file that was analyzed by Sandbox.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|MD5 hash to get report|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|full_report|full_report|True|Full report of an analyzed MD5 hash|

Example output:

```
{
  "full_report": {
    "Full Details": {
      "Summary": {
        "Status": "COMPLETED",
        "Category": "EXECS",
        "FileType": "EXE",
        "StartTime": 1520333667,
        "Duration": 520797
      },
      "Classification": {
        "Type": "MALICIOUS",
        "Category": "ADWARE",
        "Score": 76,
        "DetectedMalware": "Adware.Generic.48627"
      },
      "FileProperties": {
        "FileType": "EXE",
        "FileSize": 23323,
        "MD5": "afcb861561f7416c5e852001d31f8921",
        "SHA1": "1dce4aacf1e17418ebc05d6d2e9034a8271185f9",
        "Sha256": "fc9003461e52006be0188e1fc1b7656c81e930ec78a93eb7ab21fdff3e566314",
        "Issuer": "",
        "DigitalCerificate": "",
        "SSDeep": "384:YcBdTF8O3Fnp7JWmbiV2SBsJmnnB76RF/ewf4XXI9volVL9EFlfnvY1NvJml7Wc:lZF8OXJWmbLW0mnnp6X6rfLC3Osl6c",
        "RootCA": ""
      },
      "SystemSummary": [
        {
          "Risk": "LOW",
          "Signature": "Binary contains paths to debug symbols",
          "SignatureSources": [
            "c:\\Work\\w32_not_a_virus\\Not_a_virus\\Not_a_virus\\Release\\Not_a_virus.pdb source: 5A9E736319EE0000_5A9E736E00000000.exe"
          ]
        }
      ],
      "SecurityBypass": [
        {
          "Risk": "LOW",
          "Signature": "Entrypoint lies outside standard sections",
          "SignatureSources": [
            "section where entry point is pointing to: .Stone"
          ]
        }
      ],
      "Persistence": [
        {
          "Risk": "LOW",
          "Signature": "PE file contains sections with non-standard names",
          "SignatureSources": [
            "",
            "section name: .Stone"
          ]
        }
      ]
    }
  }
}
```

#### Blacklist URL

This action is used to add or remove URLs from a blacklist. These URLs will appear in the "Blocked Malicious URLs" section on the Advanced Threats Policy page.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|blacklist_state|boolean|True|False|True to blacklist a URL, false to unblacklist a URL|None|True|
|urls|[]string|None|True|A given set of one or more URLs or domains to update in the blacklist|None|["www.example.com", "http://rapid7.com"]|

Example input:

```
{
  "blacklist_state": true,
  "urls": [
    "www.example.com",
    "http://rapid7.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Whether or not the request succeeded|

Example output:

```
{
  "success": true
}
```

#### Lookup URL

This action is used to look up the categorization of a given set of URLs.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|urls|[]string|None|True|The given set of URLs or domains to be looked up|None|["example.com", "https://rapid7.com"]|

Example input:

```
{
  "urls": [
    "example.com",
    "https://rapid7.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url_categorization|[]url_categorization|True|Information about given URLs|

Example output:

```
{
  "url_categorization": [
    {
      "url": "example.com",
      "urlClassifications": [
        "REFERENCE_SITES",
        "INTERNET_SERVICES"
      ],
      "urlClassificationsWithSecurityAlert": []
    },
    {
      "url": "rapid7.com",
      "urlClassifications": [
        "CORPORATE_MARKETING",
        "PROFESSIONAL_SERVICES"
      ],
      "urlClassificationsWithSecurityAlert": []
    }
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### Classification

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Category|string|False|Category|
|Detected Malware|string|False|Detected malware|
|Score|integer|False|Score|
|Type|string|False|Type|

#### FileProperties

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Digital Cerificate|string|False|Digital cerificate|
|File Size|integer|False|File size|
|File Type|string|False|File type|
|Issuer|string|False|Issuer|
|MD5|string|False|MD5|
|Root CA|string|False|Root CA|
|SHA1|string|False|SHA1|
|SS Deep|string|False|SS deep|
|SHA256|string|False|SHA256|

#### FullDetails

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Classification|Classification|False|Classification|
|File Properties|FileProperties|False|File properties|
|Networking|[]PersistenceSummary|False|Networking|
|Persistence|[]PersistenceSummary|False|Persistence|
|Security Bypass|[]PersistenceSummary|False|Security bypass|
|Stealth|[]PersistenceSummary|False|Stealth|
|Summary|Summary|False|Summary|
|System Summary|[]PersistenceSummary|False|System summary|

#### PersistenceSummary

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Risk|string|False|Risk|
|Signature|string|False|Signature|
|Signature Sources|[]string|False|Signature sources|

#### Summary

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Category|string|False|Category|
|Duration|integer|False|Duration|
|File Type|string|False|File type|
|Start Time|integer|False|Start time|
|Status|string|False|Status|

#### full_report

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Full Details|FullDetails|False|Full details|

#### url_categorization

|Name|Type|Required|Description|
|----|----|--------|-----------|
|URL|string|False|Checked URL|
|URL Classifications|[]string|False|URL classifications|
|URL classifications with security alert|[]string|False|URL classifications with security alert|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.2.0 - New action Get Sandbox Report for Hash
* 1.1.2 - Support both domains and URL inputs in the Blacklist URL and Lookup URL actions
* 1.1.1 - Improve documentation around action inputs
* 1.1.0 - New action Blacklist URL
* 1.0.0 - Initial plugin

# Links

## References

* [Zscaler](https://www.zscaler.com/)
