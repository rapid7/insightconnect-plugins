
# FullContact

## About

[FullContact](https://www.fullcontact.com) keeps all your contacts in one place and automatically up-to-date with the FullContact Address Book.
The output of this plugin is the JSON data returned by FullContact.

## Actions

### Lookup Phone Number

This action is used to obtain information by phone number.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|phone|string|None|True|Phone number prefixed with +country code E.g. +12223334444|None|

For the phone lookup service, phone numbers should be prefixed
with + followed by country code, e.g. +12223334444).  The country
code for U.S. is +1.  For a complete list of country codes, see
`https://countrycode.org`

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|person_info|person|False|Personal information|

### Lookup Stats

This action is used to retrieve stats by name.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|family_name|string|None|False|Last name of person|None|
|given_name|string|None|False|First name of person|None|
|unspecific_name|string|None|False|Name of person (Leave empty if Given or Family Name is used)|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|name_info|name|False|Name statistics|

### Lookup Email

This action is used to obtain information by email address.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|Email address|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|person_info|person|False|None|

### Validate Email

This action is used to check whether an email address is disposable.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|email|string|None|True|Email address|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|validity_info|validity|False|Validity information|

## Triggers

This plugin does not contain any triggers.

## Connection

To use this plugin, you must have a FullContact application key.
Sign up at `https://app.fullcontact.com/welcome`.

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|token|credential_secret_key|None|True|API Token (required)|None|
|server|string|https\://api.fullcontact.com/v2/|False|API Server|None|

## Troubleshooting

All input items should not be surrounded by quotes.

Error values use the standard HTTP codes (200 OK, 404 Not Found, etc)

Occasionally the FullContact servers may respond with a "try again"
status (202).  This plugin will sleep for an interval of 10 seconds
and then make the request one further time.

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - Original look_up_by_* and validate_email actions
* 0.1.2 - Added look_up_name_stats action
* 0.1.3 - Added retry for 202
* 1.0.0 - Clean up spec, pass validation, and bad indention for validity type
* 2.0.0 - Update to v2 architecture | Support web server mode | Update to new credential types
* 2.0.2 - Regenerate with latest Go SDK to solve bug with triggers

## Workflows

Examples:

* User enrichment
* Fraud detection

## References

* [FullContact API](https://www.fullcontact.com/developer/docs/)
* [FullContact Application Key](https://app.fullcontact.com/welcome)
* [Country Code](https://countrycode.org)
