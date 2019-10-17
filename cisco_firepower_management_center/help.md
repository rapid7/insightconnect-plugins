# Cisco Firepower Management Center

## About

[Cisco Firepower Management Center](https://www.cisco.com/c/en/us/products/security/firepower-management-center/index.html) is your administrative nerve center for managing critical Cisco network security solutions.

## Actions

### Block URL Policy

This action is used to create a new block URL policy.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|access_policy|string|None|True|Access Policy name|None|
|rule_name|string|None|True|Name for Access Rule to be created|None|
|url_objects|[]url_object|None|True|URL Objects to block|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|string|True|Success|

Example output:

```
{
    "success": True
}   
```

## Triggers

_This plugin does not contain any triggers._

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|server|string|None|False|Enter the address for the server|None|
|username_and_password|credential_username_password|None|True|Cisco username and password|None|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

## Workflows

Examples:

* Block URL policy for phishing email

## Versions

* 1.0.0 - Initial plugin

## References

* [Cisco Firepower Management Center](https://www.cisco.com/c/en/us/products/security/firepower-management-center/index.html)

## Custom Output Types

### url_object

|Name|Type|Required|Description|
|----|----|--------|-----------|
|name|string|True|Name of URL object|
|url|string|True|URL to block (max 400 chars)|
