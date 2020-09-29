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
  "credentials": "{\"username\":\"user@example.com\", \"password\":\"mypassword\"}",
  "url": "admin.zscalerbeta.net"
}
```

## Technical Details

### Actions

#### Blacklist URL

This action is used to add or remove URLs from a blacklist. These URLs will appear in the "Blocked Malicious URLs" section on the Advanced Threats Policy page.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|blacklist_state|boolean|True|False|True to blacklist a URL, false to unblacklist a URL|None|True|
|urls|[]string|None|True|A given set of one or more URLs to update in the blacklist. URLs must include the scheme (http, https, etc)|None|["https://www.example.com", "http://rapid7.com"]|

Example input:

```
{
  "blacklist_state": true,
  "urls": [
    "https://www.example.com",
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
|urls|[]string|None|True|The given set of URLs to be looked up. URLs must not include the scheme (http, https, etc)|None|["example.com", "rapid7.com"]|

Example input:

```
{
  "urls": [
    "example.com",
    "rapid7.com"
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

#### url_categorization

|Name|Type|Required|Description|
|----|----|--------|-----------|
|URL|string|False|Checked URL|
|URL Classifications|[]string|False|URL classifications|
|URL classifications with security alert|[]string|False|URL classifications with security alert|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.1.0 - New action Blacklist URL
* 1.0.0 - Initial plugin

# Links

## References

* [Zscaler](https://www.zscaler.com/)
