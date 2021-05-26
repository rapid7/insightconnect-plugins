# Description

Devo is the cloud-native logging and security analytics solution that delivers real-time visibility for security and operations teams

# Key Features

Identify key features of plugin.

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product's user interface

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|authentication_token|credential_secret_key|None|True|Authentication Token|None|9de5069c5afe602b2ea0a04b66beb2c0|
|region|string|None|True|Region|['US', 'Europe', 'Spain (VDC)']|None|

Example input:

```
{
  "authentication_token": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

## Technical Details

### Actions

#### 

This action is used to .

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|True|Query|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]object|True|Results|

Example output:

```
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

* [devo](LINK TO PRODUCT/VENDOR WEBSITE)
