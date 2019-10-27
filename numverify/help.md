
# NumVerify

## About

This plugin accesses the [NumVerify](https://numverify.com/) service to validate a phone number.
The output of this plugin is the JSON data returned by NumVerify. It
includes fields such as location, carrier, and line_type.

## Actions

### Validate

This action is used to validate phone number with NumVerify. It accepts a phone number and country code.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|phone_number|string|None|True|Phone number to validate (Prefix with Country Calling Code if Country Code is not set E.g. 12223334444)|None|
|country_code|string|None|False|Country code (see https\://countrycode.org)|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|phone_info|object|False|None|

## Triggers

This plugin does not contain any triggers.

## Connection

To use this plugin, you must have a NumVerify application key. Sign up at [https://numverify.com/product](https://numverify.com/product).

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|token|credential_secret_key|None|True|API Token|None|
|server|string|http\://apilayer.net/api/validate|False|API Server|None|

## Troubleshooting

Error values include "404_not_found" and "invalid_access_key".

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - Undocumented bug fix
* 1.0.0 - Update to v2 architecture | Support web server mode | Update to new credential types
* 1.0.1 - Updating to Go SDK 2.6.4
* 1.0.2 - Regenerate with latest Go SDK to solve bug with triggers

## Workflows

Examples:

* Address validation
* Port checking

## References

* [NumVerify](https://numverify.com/documentation)
* [NumVerify Key](https://numverify.com/product)
* [CountryCode](https://countrycode.org)
