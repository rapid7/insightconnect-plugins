# Description

[McAfee Advanced Threat Defense](https://www.mcafee.com/enterprise/en-us/products/advanced-threat-defense.html) provides an API framework for external applications to access core McAfeeATD functions through the REST protocol.

# Key Features

* Check if a hash is blacklisted

# Requirements

* Username and password
* Base URL for McAfee ATD

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password|None|{"username":"user1", "password":"mypassword"}|
|port|integer|443|False|The port number for provided host|None|443|
|url|string|None|True|Base URL for the McAfee Advanced Threat Defense server|None|https://www.example.com|
|verify_ssl|boolean|True|False|Verify the server's TLS/SSL certificate|None|True|

Example input:

```
{
  "credentials": {
    "username":"user1",
    "password":"mypassword"
  },
  "port": 443,
  "url": "https://www.example.com",
  "verify_ssl": true
}
```

## Technical Details

### Actions

#### Check Hash Status

This action is used to check if a user submitted hash value is either blacklisted or whitelisted.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|MD5 Hash to submit|None|9de5069c5afe602b2ea0a04b66beb2c0|

Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|object|True|Return information about given MD5 Hash|
|success|boolean|True|Success status of submit Hash request|

Example output:

```
{
  "results": {
    "9de5069c5afe602b2ea0a04b66beb2c0": "Previously submitted"
  },
  "success": true
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [McAfee Advanced Threat Defense](https://www.mcafee.com/enterprise/en-us/products/advanced-threat-defense.html)
