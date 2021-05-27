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
|region|string|None|True|Region|['USA', 'EU', 'VDC (Spain)']|None|

Example input:

```
{
  "authentication_token": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

## Technical Details

### Actions

#### Query Logs

This action is used to run a LINQ query against the logs.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|from_date|string|None|True|Earliest date to query events from, will accept relative or absolute times. e.g. 1/1/2020, 2 hours ago, 1/1/2020T12:00:00, Now|None|5 minutes ago|
|query|string|None|True|Query|None|from from demo.ecommerce.data select *|
|to_date|string|Now|True|Lastest date to query events from, will accept relative or absolute times. e.g. 1/1/2020, 2 hours ago, 1/1/2020T12:00:00, Now|None|Now|

Example input:

```
{
  "from_date": "5 minutes ago",
  "query": "from from demo.ecommerce.data select *",
  "to_date": "Now"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|query_result|True|An object containing information and results about the query that was run|

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
