# Description

[Zscaler](https://www.zscaler.com/) is a SaaS security platform that provides fast, secure connections between client applications, regardless of device, location, or network.

# Key Features

* Lookup categories for a given URL
* Blacklist or unblacklist URLs
* Create user
* Delete user
* Get users
* Get URL category by name
* Update URLs of URL category

# Requirements

* [Requires a Zscaler organization API Key](https://help.zscaler.com/zia/api-getting-started#RetrieveAPIKey)
* Requires a Zscaler username and password
* [Requires a Zscaler base URI](https://help.zscaler.com/zia/api-getting-started#RetrieveAPIKey), such as: https://admin.zscalerbeta.net

# Supported Product Versions

* Zscaler API 2023-02-20

# Documentation

## Setup

To locate your base URI and key:

1. Log in to the ZIA Admin Portal using your admin credentials.
2. Go to **Administration > API Key Management**.

In order to view the API Key Management page, the admin must be assigned an admin role that includes the Authentication Configuration functional scope.

In the **Organization API Key** tab, the base URI and key details are displayed within the table.

For more information see the [Zscaler getting started guide](https://help.zscaler.com/zia/api-getting-started) on obtaining the API key and base URL.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Enter organization API key|None|14M2d25A7c12|
|credentials|credential_username_password|None|True|Username and password to access Zscaler|None|{"username":"user@example.com", "password":"mypassword"}|
|url|string|None|True|Base URL, ex. 'https://admin.zscalerbeta.net'. See https://help.zscaler.com/zia/api-getting-started#RetrieveAPIKey for details|None|https://admin.zscalerbeta.net|

Example input:

```
{
  "api_key": "14M2d25A7c12",
  "credentials": {
    "username":"user@example.com",
    "password":"mypassword"
  },
  "url": "https://admin.zscalerbeta.net"
}
```

## Technical Details

### Actions

#### Get Blacklist URL

This action is used to get blacklisted URLs.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|blacklisted_urls|[]string|False|URLs added to the blacklist|

Example output:

```
{
  "blacklisted_urls": [
    "domain.com",
    "example.com",
    "example1.com",
    "example2.com",
    "example3.com",
    "example4.com",
    "example5.com"
  ]
}
```

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
|activate_configuration|boolean|False|True|Set to true to activate configuration changes|None|False|
|blacklist_state|boolean|True|False|True to blacklist a URL, false to unblacklist a URL|None|True|
|urls|[]string|None|True|A given set of one or more URLs or domains to update in the blacklist|None|["www.example.com", "http://rapid7.com"]|

Example input:

```
{
  "activate_configuration": false,
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
|status|string|True|Activation status for a configuration change|
|success|boolean|True|Whether or not the request succeeded|

Example output:

```
{
  "success": true,
  "status": "PENDING"
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

#### Get Users

This action gets a list of all users and allows user filtering by name, department, or group. The name search parameter performs a partial match. The dept and group parameters perform a 'starts with' match.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|department|string|None|False|Filters by department name|None|Department Name|
|group|string|None|False|Filters by group name|None|Group Name|
|name|string|None|False|Filters by user name|None|John|
|page|integer|None|False|Specifies the page offset|None|1|
|pageSize|integer|None|False|Specifies the page size|None|100|

Example input:

```
{
  "department": "Department Name",
  "group": "Group Name",
  "name": "John",
  "page": 1,
  "pageSize": 100
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|users|[]user|False|List of organization users|[]|

Example output:

```
{
  "users": [
    {
      "id": 123456789,
      "name": "Sample user",
      "email": "user@example.com",
      "groups": [
        {
          "id": 123456789,
          "name": "Test Group"
        }
      ],
      "department": {
        "id": 123456789,
        "name": "Test Department"
      },
      "adminUser": false,
      "isNonEditable": false,
      "deleted": false
    }
  ]
}
```

#### Delete User

This action deletes the user for the specified ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|userId|integer|None|True|The unique identifier for the user|None|12345678|

Example input:

```
{
  "userId": 12345678
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|success|boolean|False|Whether or not the request succeeded|True|

Example output:

```
{
  "success": true
}
```

#### Create User

This action adds a new user. A user can belong to multiple groups, but can only belong to one department.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|comments|string|None|False|Additional information about this user|None|Example comment|
|departmentName|string|None|True|Department a user belongs to|None|Department Name|
|email|string|None|True|User email consists of a user name and domain name. It does not have to be a valid email address, but it must be unique and its domain must belong to the organization|None|user@example.com|
|groupNames|[]string|None|True|List of groups a user belongs to|None|["Group Name"]|
|name|string|None|True|User name|None|John|
|password|password|None|True|User's password. Applicable only when authentication type is Hosted DB. Password strength must follow what is defined in the auth settings|None|password12!|
|tempAuthEmail|string|None|False|If you enabled one-time tokens or links, enter the email address to which the Zscaler service sends the tokens or links. If this is empty, the service sends the email to the User email|None|user@example.com|

Example input:

```
{
  "comments": "Example comment",
  "departmentName": "Department Name",
  "email": "user@example.com",
  "groupNames": [
    "Group Name"
  ],
  "name": "John",
  "password": "password12!",
  "tempAuthEmail": "user@example.com"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|user|user|False|An organization user|{}|

Example output:

```
{
  "user": {
    "id": 123456789,
    "name": "Sample user",
    "email": "user@example.com",
    "groups": [
      {
        "id": 123456789,
        "name": "Test Group",
        "idpId": 123456789,
        "comments": "Sample comment"
      }
    ],
    "department": {
      "id": 123456789,
      "name": "Test Department",
      "idpId": 123456789,
      "comments": "Sample comment",
      "deleted": false
    },
    "comments": "Sample comment",
    "tempAuthEmail": "user@example.com",
    "adminUser": false
  }
}
```

#### Get URL Category by Name

This action gets the URL category information for the specified name.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|customUrlCategoryName|string|None|False|Name of the custom URL category to be returned. If this field is filled then the 'URL Category Name' input will be ignored|None|Custom Category Example|
|urlCategoryName|string|Adult Sex Education|False|Name of the URL category to be returned. This field will be ignored if the 'Custom URL Category Name' input is filled|['Adult Sex Education', 'Adult Themes', 'Advertising', 'Alcohol/Tobacco', 'Alt/New Age', 'Anonymizer', 'Art/Culture', 'Blogs', 'Body Art', 'CDN', 'Classifieds', 'Computer Hacking', 'Continuing Education/Colleges', 'Copyright Infringement', 'Corporate Marketing', 'Cult', 'Custom Encrypted Content', 'DNS Over HTTPS Services', 'Dining/Restaurant', 'Discussion Forum', 'Dynamic DNS Host', 'Entertainment', 'Family Issues', 'FileHost', 'Finance', 'Gambling', 'Government', 'Health', 'History', 'Hobbies/Leisure', 'Image Host', 'Internet Services', 'Job/Employment Search', 'K-12', 'K-12 Sex Education', 'Lifestyle', 'Lingerie/Bikini', 'Marijuana', 'Mature Humor', 'Militancy/Hate and Extremism', 'Military', 'Miscellaneous or Unknown', 'Music and Audio Streaming', 'Newly Registered and Observed Domains', 'Newly Revived Domains', 'News and Media', 'Non Categorizable', 'Nudity', 'Online Auctions', 'Online Chat', 'Online Shopping', 'Online Trading, Brokerage, Insurance', 'Online and Other Games', 'Operating System and Software Updates', 'Other Adult Material', 'Other Business and Economy', 'Other Drugs', 'Other Education', 'Other Entertainment/Recreation', 'Other Government and Politics', 'Other Illegal or Questionable', 'Other Information Technology', 'Other Internet Communication', 'Other Miscellaneous', 'Other Religion', 'Other Security', 'Other Shopping and Auctions', 'Other Social and Family Issues', 'Other Society and Lifestyle', 'Peer-to-Peer Site', 'Politics', 'Pornography', 'Portals', 'Profanity', 'Professional Services', 'Questionable', 'Radio', 'Real Estate', 'Reference Sites', 'Remote Access Tools', 'Safe Search Engine', 'Science/Tech', 'Shareware Download', 'Social Issues', 'Social Networking', 'Social Networking Adult', 'Social Networking Games', 'Special Interests/Social Organizations', 'Sports', 'Spyware/Adware', 'Tasteless', 'Television/Movies', 'Traditional Religion', 'Translators', 'Travel', 'User-Defined', 'Vehicles', 'Video Streaming', 'Violence', 'Weapons/Bomb', 'Web Conferencing', 'Web Host', 'Web Search', 'Webmail', 'Zscaler Proxy IPs']|Travel|

Example input:

```
{
  "customUrlCategoryName": "Custom Category Example",
  "urlCategoryName": "Travel"
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|urlCategory|urlCategory|False|Information about the given URL category|{}|

Example output:

```
{
  "urlCategory": {
    "id": "CUSTOM_01",
    "configuredName": "Custom Category Example",
    "superCategory": "USER_DEFINED",
    "keywords": [
      "key1"
    ],
    "keywordsRetainingParentCategory": [
      "test1"
    ],
    "urls": [
      "example.com"
    ],
    "dbCategorizedUrls": [],
    "customCategory": true,
    "scopes": [
      {
        "type": "ORGANIZATION"
      },
      {
        "type": "DEPARTMENT",
        "scopeEntities": [
          {
            "id": 12345678,
            "name": "Test Department"
          }
        ]
      },
      {
        "type": "LOCATION",
        "scopeEntities": [
          {
            "id": 12345678,
            "name": "Location Example"
          }
        ]
      },
      {
        "scopeGroupMemberEntities": [],
        "type": "LOCATION",
        "scopeEntities": [
          {
            "id": 12345678,
            "name": "Location Group Example"
          }
        ]
      }
    ],
    "editable": true,
    "description": "Example Description",
    "type": "URL_CATEGORY",
    "val": 123,
    "customUrlsCount": 1,
    "urlsRetainingParentCategoryCount": 0,
    "customIpRangesCount": 0,
    "ipRangesRetainingParentCategoryCount": 0
  }
}
```

#### Update URLs of URL Category

This action adds or removes URLs for the specified URL category.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|None|True|The action applied to the URLs|['Add to the list', 'Remove from the list']|Add to the list|
|customUrlCategoryName|string|None|False|Name of the custom URL category to be returned. If this field is filled then the 'URL Category Name' input will be ignored|None|Custom Category Example|
|urlCategoryName|string|Adult Sex Education|False|Name of the URL category to be returned. This field will be ignored if the 'Custom URL Category Name' input is filled|['Adult Sex Education', 'Adult Themes', 'Advertising', 'Alcohol/Tobacco', 'Alt/New Age', 'Anonymizer', 'Art/Culture', 'Blogs', 'Body Art', 'CDN', 'Classifieds', 'Computer Hacking', 'Continuing Education/Colleges', 'Copyright Infringement', 'Corporate Marketing', 'Cult', 'Custom Encrypted Content', 'DNS Over HTTPS Services', 'Dining/Restaurant', 'Discussion Forum', 'Dynamic DNS Host', 'Entertainment', 'Family Issues', 'FileHost', 'Finance', 'Gambling', 'Government', 'Health', 'History', 'Hobbies/Leisure', 'Image Host', 'Internet Services', 'Job/Employment Search', 'K-12', 'K-12 Sex Education', 'Lifestyle', 'Lingerie/Bikini', 'Marijuana', 'Mature Humor', 'Militancy/Hate and Extremism', 'Military', 'Miscellaneous or Unknown', 'Music and Audio Streaming', 'Newly Registered and Observed Domains', 'Newly Revived Domains', 'News and Media', 'Non Categorizable', 'Nudity', 'Online Auctions', 'Online Chat', 'Online Shopping', 'Online Trading, Brokerage, Insurance', 'Online and Other Games', 'Operating System and Software Updates', 'Other Adult Material', 'Other Business and Economy', 'Other Drugs', 'Other Education', 'Other Entertainment/Recreation', 'Other Government and Politics', 'Other Illegal or Questionable', 'Other Information Technology', 'Other Internet Communication', 'Other Miscellaneous', 'Other Religion', 'Other Security', 'Other Shopping and Auctions', 'Other Social and Family Issues', 'Other Society and Lifestyle', 'Peer-to-Peer Site', 'Politics', 'Pornography', 'Portals', 'Profanity', 'Professional Services', 'Questionable', 'Radio', 'Real Estate', 'Reference Sites', 'Remote Access Tools', 'Safe Search Engine', 'Science/Tech', 'Shareware Download', 'Social Issues', 'Social Networking', 'Social Networking Adult', 'Social Networking Games', 'Special Interests/Social Organizations', 'Sports', 'Spyware/Adware', 'Tasteless', 'Television/Movies', 'Traditional Religion', 'Translators', 'Travel', 'User-Defined', 'Vehicles', 'Video Streaming', 'Violence', 'Weapons/Bomb', 'Web Conferencing', 'Web Host', 'Web Search', 'Webmail', 'Zscaler Proxy IPs']|Travel|
|urlList|[]string|None|True|List of the URLs to be updated|None|["example.com", "example1.com"]|

Example input:

```
{
  "action": "Add to the list",
  "customUrlCategoryName": "Custom Category Example",
  "urlCategoryName": "Travel",
  "urlList": [
    "example.com",
    "example1.com"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
|----|----|--------|-----------|-------|
|urlCategory|urlCategory|False|Information about the updated URL category|{}|

Example output:

```
{
  "urlCategory": {
    "id": "CUSTOM_01",
    "configuredName": "Custom Category Example",
    "superCategory": "USER_DEFINED",
    "keywords": [
      "key1"
    ],
    "keywordsRetainingParentCategory": [
      "test1"
    ],
    "urls": [
      "example.com"
    ],
    "dbCategorizedUrls": [],
    "customCategory": true,
    "scopes": [
      {
        "type": "ORGANIZATION"
      },
      {
        "type": "DEPARTMENT",
        "scopeEntities": [
          {
            "id": 12345678,
            "name": "Test Department"
          }
        ]
      },
      {
        "type": "LOCATION",
        "scopeEntities": [
          {
            "id": 12345678,
            "name": "Location Example"
          }
        ]
      },
      {
        "scopeGroupMemberEntities": [],
        "type": "LOCATION_GROUP",
        "scopeEntities": [
          {
            "id": 12345678,
            "name": "Location Group Example"
          }
        ]
      }
    ],
    "editable": true,
    "description": "Example Description",
    "type": "URL_CATEGORY",
    "val": 123,
    "customUrlsCount": 1,
    "urlsRetainingParentCategoryCount": 0,
    "customIpRangesCount": 0,
    "ipRangesRetainingParentCategoryCount": 0
  }
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
|Digital Certificate|string|False|Digital certificate|
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

#### department

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Comments|string|False|Additional information about this department|
|Deleted|boolean|False|Is department deleted|
|ID|integer|False|Department ID|
|IdpId|integer|False|Identity provider (IdP) ID|
|Name|string|False|Department name|

#### group

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Comments|string|False|Additional information about the group|
|ID|integer|False|Unique identifier for the group|
|IdpId|integer|False|Unique identifier for the identity provider (IdP)|
|Name|string|False|Group name|

#### user

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Admin User|boolean|False|True if this user is an Admin user|
|Comments|string|False|Additional information about this user|
|Deleted|boolean|False|Is user deleted|
|Department|department|False|Department a user belongs to|
|Email|string|False|User email consists of a user name and domain name. It does not have to be a valid email address, but it must be unique and its domain must belong to the organization|
|Groups|[]group|False|List of groups a user belongs to|
|ID|integer|False|User ID|
|Is Non Editable|boolean|False|Is user non-editable|
|Name|string|False|User name|
|Temporary Authentication Email|string|False|If you enabled one-time tokens or links, enter the email address to which the Zscaler service sends the tokens or links. If this is empty, the service sends the email to the User email|
|Type|string|False|User type. Provided only if this user is not an end user|

#### adminScope

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Scope Entities|[]entityReference|False|Based on the admin scope type, the entities can be the ID/name pair of departments, locations, or location groups|
|Scope Group Member Entities|[]entityReference|False|List of ID/name pairs of locations within the location group|
|Type|string|False|The admin scope type|

#### entityReference

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Extensions|object|False|Extensions|
|ID|integer|False|Identifier that uniquely identifies an entity|
|Name|string|False|The configured name of the entity|

#### urlCategory

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Configured Name|string|False|Name of the URL category|
|Custom Category|boolean|False|Whether the URL category is custom. Up to 48 custom URL categories can be added per organization|
|Custom IP Ranges Count|integer|False|The number of custom IP address ranges associated to the URL category|
|Custom URLs Count|integer|False|The number of custom URLs associated to the URL category|
|DB Categorized URLs|[]string|False|URLs added to a custom URL category are also retained under the original parent URL category (i.e., the predefined category the URL previously belonged to). The URLs entered are covered by policies that reference the original parent URL category as well as those that reference the custom URL category|
|Description|string|False|Description of the URL category. Contains tag name and needs to be localized on client side in case of predefined category, else it contains the user-entered description which does not have localization support|
|Editable|boolean|False|Value is set to false for custom URL category when due to scope user does not have edit permission|
|ID|string|False|The identifier of the URL category|
|IP Ranges|[]string|False|Custom IP address ranges associated with a URL category. Up to 2000 custom IP address ranges and retaining parent custom IP address ranges can be added, per organization, across all categories|
|IP Ranges Retaining Parent Category|[]string|False|The retaining parent custom IP address ranges associated with a URL category. Up to 2000 custom IP ranges and retaining parent custom IP address ranges can be added, per organization, across all categories|
|IP Ranges Retaining Parent Category Count|integer|False|The number of custom IP address ranges associated to the URL category, that also need to be retained under the original parent category|
|Keywords|[]string|False|Custom keywords associated with a URL category. Up to 2048 custom keywords can be added per organization across all categories|
|Keywords Retaining Parent Category|[]string|False|Retained custom keywords from the parent URL category that is associated to a URL category. Up to 2048 retained parent keywords can be added per organization across all categories (including bandwidth classes)|
|Scopes|[]adminScope|False|Scope of the custom categories|
|Super Category|string|False|Super Category of the URL category|
|Type|string|False|Type of the URL category|
|URL Keyword Counts|urlKeywordCounts|False|URL and keyword counts for the URL category|
|URLs|[]string|False|Custom URLs to add to a URL category. Up to 25,000 custom URLs can be added per organization across all categories (including bandwidth classes)|
|URLs Retaining Parent Category Count|integer|False|The number of custom URLs associated to the URL category, that also need to be retained under the original parent category|

#### urlKeywordCounts

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Retain Parent Keyword Count|integer|False|Count of total keywords with retain parent category|
|Retain Parent URL Count|integer|False|Count of URLs with retain parent category|
|Total Keyword Count|integer|False|Total keyword count for the category|
|Total URL Count|integer|False|Custom URL count for the category|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.5.0 - Add Actions: `Create User`, `Delete User`, `Get Users`, `Get URL Category by Name`, `Update URLs of URL Category`
* 1.4.0 - Add Activate Configuration input in Blacklist URL action
* 1.3.0 - Add Get Blacklist URL action
* 1.2.1 - Usability updates and updated icon
* 1.2.0 - New action Get Sandbox Report for Hash
* 1.1.2 - Support both domains and URL inputs in the Blacklist URL and Lookup URL actions
* 1.1.1 - Improve documentation around action inputs
* 1.1.0 - New action Blacklist URL
* 1.0.0 - Initial plugin

# Links

* [Zscaler](https://www.zscaler.com/)

## References

* [Zscaler](https://www.zscaler.com/)