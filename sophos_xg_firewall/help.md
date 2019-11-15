# Description

[Sophos XG Firewall](https://www.sophos.com/en-us/products/next-gen-firewall.aspx) is a next generation endpoint protection and enterprise firewall.
This plugin utilizes the [Sophos XG Firewall API](https://www.sophos.com/en-us/support/documentation/sophos-xg-firewall.aspx).

The Sophos XG Firewall plugin allows you to manage your Sophos XG Firewall through policies. 

# Key Features

* Manage your network policies 

# Requirements

* Sophos credentials
* Address and port of your Sophos box

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|username|string|None|True|Username to access Sophos XG API|None|
|host|string|None|True|Sophos XG address e.g sophosxg.company.com|None|
|password|password|None|True|Password to access Sophos XG API|None|
|port|integer|4444|True|Webadmin port for Sophos XG e.g. 4444|None|

## Technical Details

### Actions

#### Create User Policy

This action is used to create a user based firewall policy.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy|userpolicy|None|False|User Policy Settings|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|Returns the response from creating a policy|

Example output:

```

{
  "status_code": "200",
  "status_response": "Configuration applied successfully.",
  "invalid_params": "None"
}

```

#### Create PublicNonHTTPBased Policy

This action is used to create a public HTTP based policy.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy|publicnonhttpbasedpolicy|None|False|PublicHTTPBased policy settings|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|Returns the response from creating a policy|

Example output:

```

{
  "status_code": "200",
  "status_response": "Configuration applied successfully.",
  "invalid_params": "None"
}

```

#### Create Network Policy

This action is used to create a network based firewall policy.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy|networkpolicy|None|False|Network policy settings|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|Returns the response from creating a policy|

Example output:

```

{
  "status_code": "200",
  "status_response": "Configuration applied successfully.",
  "invalid_params": "None"
}

```

#### Create NonHTTPBased Policy


This action is used to create a non-HTTP based policy.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|policy|nonhttpbasedpolicy|None|False|NonHTTPBased policy settings|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|response|response|False|Returns the response from creating a policy|

Example output:

```

{
  "status_code": "200",
  "status_response": "Configuration applied successfully.",
  "invalid_params": "None"
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

To enable API access within Sophos XG, the setting is located in Backup & Firmware. You will need to specify the IP that will be making calls to Sophos XG appliance.

# Version History

* 2.0.0 - Update to new credential types
* 1.0.0 - Support web server mode | Update to v2 Python plugin architecture
* 0.1.0 - Initial plugin

# Links

## References

* [Sophos XG Firewall](https://www.sophos.com/en-us/products/next-gen-firewall.aspx)
* [Sophos XG Firewall API](https://www.sophos.com/en-us/support/documentation/sophos-xg-firewall.aspx)

