# Description

[Palo Alto MineMeld](https://www.paloaltonetworks.com/) is an open-source application that streamlines the aggregation, enforcement and sharing of threat intelligence.

# Key Features

* Update External Dynamic List

# Requirements

* Username and password 
* Base URL for Palo Alto MineMeld

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|credentials|credential_username_password|None|True|Username and password to access Palo Alto MineMeld|None|{"username":"user1", "password":"mypassword"}|
|port|number|443|False|Palo Alto MineMeld port|None|443|
|ssl_verify|boolean|True|False|Verify TLS/SSL Certificate|None|True|
|url|string|None|True|Palo Alto MindMeld URL|None|https://www.example.com|

Example input:

```
{
  "credentials": "{\"username\":\"user1\", \"password\":\"mypassword\"}",
  "port": 443,
  "ssl_verify": true,
  "url": "https://www.example.com"
}
```

## Technical Details

### Actions

#### Update External Dynamic List

This action is used to add and remove IP addresses and domains to/from an external dynamic list.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|indicator|string|None|True|Indicator type which is IP address, domain name, or URL|None|198.51.100.100|
|list_name|string|None|True|Name of the dynamic list|None|example_list_name|
|operation|string|Add|False|Choose operation to add or remove indicator|['Add', 'Remove']|None|

Example input:

```
{
  "indicator": "198.51.100.100",
  "list_name": "example_list_name"
  "operation": "Add"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|True|Returned true if operation success|

Example output:

```
{
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

* [Palo Alto MineMeld](https://www.paloaltonetworks.com/)
