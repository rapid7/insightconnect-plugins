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
|url|string|None|True|API URL|None|admin.zscalerbeta.net|

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

#### Blacklist URL

This action is used to add or remove  URLs from a blacklist.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|blacklist_state|boolean|True|False|True to blacklist a domain, false to unblacklist a domain|None|True|
|urls|[]string|None|True|A given set of one or more domain name to update in the blacklist|None|["example.com", "rapid7.com"]|

Example input:

```
{
  "blacklist_state": true,
  "urls": [
    "example.com",
    "rapid7.com"
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

* 1.1.0 - New action Blacklist URL
* 1.0.0 - Initial plugin

# Links

## References

* [Zscaler](https://www.zscaler.com/)
