# Description

[Blockade](https://www.blockade.com) brings antivirus-like capabilities to users who run the Chrome browser.
This plugin utilizes the [Blockade Cloud Node API](https://github.com/blockadeio/cloud_node).

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|None|None|
|api_key|string|None|False|None|None|
|email|string|None|False|None|None|

## Technical Details

### Actions

#### Add Indicators

This action is used to add indicators to the cloud node.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|indicators|[]string|None|False|Indicators as array e.g. [ 'c9867172dca8b07d06566c78c7265ff2', '8f55ea93778722e32403b0c961295aed' ]|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|writeCount|integer|False|None|
|message|string|False|None|
|success|boolean|False|None|

#### Get Events

This action is used to get list of indicators from the cloud node.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|eventsCount|integer|False|None|
|events|[]string|False|List of events|
|success|boolean|True|None|

#### Add User

This action is used to add a cloud node user. The connection must contain the API key and email of an admin user to work.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|user_name|string|None|True|Name of new user|None|
|user_role|string|None|True|Role of new user|['analyst', 'admin']|
|user_email|string|None|True|Email of new user|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|role|string|False|None|
|name|string|False|None|
|success|boolean|True|None|
|message|string|True|None|
|api_key|string|False|None|
|email|string|False|None|

#### Get Indicators

This action is used to get list of indicators from the cloud node.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|db_route|string|None|False|Database name, leave empty if only a single database is used|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|indicators|[]string|True|List of indicators|
|indicatorCount|integer|True|None|
|success|boolean|True|None|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

The `Get Indicators` and `Get Events` actions do not require authentication.

# Version History

* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## Source Code

https://github.com/rapid7/insightconnect-plugins

## References

* [Blockade](https://www.blockade.com)
* [Blockade Cloud Node API](https//api.blockade.co://github.com/blockadeio/cloud_node)

