# Description

[Zscaler](https://www.zscaler.com/) is a SaaS security platform that provides fast, secure connections between client applications, regardless of device, location, or network.

# Key Features

* Lookup categories for a given URL

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

#### Get Sandbox Report for Hash

This action is used to get a full report for an MD5 hash of a file that was analyzed by Sandbox.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|MD5 hash to analyze|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|full_report|object|True|Full report of an analyzed MD5 hash|

Example output:

```
```

#### Lookup URL

This action is used to look up the categorization of a given set of URLs.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|urls|[]string|None|True|The given set of URLs to be looked up|None|["example.com", "rapid7.com"]|

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

* 1.1.0 - New action Get Sandbox Report for Hash
* 1.0.0 - Initial plugin

# Links

## References

* [Zscaler](https://www.zscaler.com/)
