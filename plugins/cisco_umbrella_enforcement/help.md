# Description

[Cisco Umbrella Enforcement](https://docs.umbrella.com/developer/networkdevices-api/) allows partners and customers with their own homegrown SIEM/Threat Intelligence Platform (TIP) environments to inject events and/or threat intelligence into their Umbrella environment. These events are then instantly converted into visibility and enforcement that can extend beyond the perimeter and thus the reach of the systems that might have generated those events or threat intelligence.
The Cisco Umbrella Enforcement InsightConnect plugin allows you to inherit the ability to send security events from platform/service/appliance within a customer environment to the Cisco security cloud for enforcement.
This plugin utilizes the [Cisco Umbrella Enforcement API](https://enforcement-api.readme.io/).

# Key Features

* Delete domain from user domain list
* Retrieve list of domains already added to the shared customer's domain list
* Post a malware event to the customer's domain list

# Requirements

* Cisco Umbrella Enforcement API key

# Supported Product Versions

_There are no supported product versions listed._

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|Cisco Umbrella Management API key|None|9de5069c5afe602b2ea0a04b66beb2c0|
|ssl_verify|boolean|False|True|Boolean value to indicate whether to add SSL verify to requests|None|None|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

## Technical Details

### Actions

#### List Domains

This action is used to gather the lists of domains already added to the shared customer's domain list.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|domains|domains|False|Array containing domains in the domain list|

Example output:

```

{
  "data": [
    {
      "ID": 28699715,
      "lastSeenAt": 1502820244,
      "name": "internetbadguys.bad-v5.com"
    },
    {
      "ID": 28699717,
      "lastSeenAt": 1502820244,
      "name": "internetbadguys.bad-v6.com"
    }
  ],
  "meta": {
    "limit": 200,
    "next": "",
    "page": 1,
    "prev": ""
  }
}

```

#### Delete Domain by Name

This action is used to delete domain from user domain list.
The delete comand should include the numerical identifier (ID) as specified in the LIST endpoint or the actual domain name you'd like to delete.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|name|string|None|True|Domain name|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|True|Action status [success | error]|

Example output:

```

{
  "status": "success"
}

```

#### Add Event

This action is used to post a malware event for processing and optionally adds it to the customer's domain list.
It accepts an array of JSON objects of the [Generic Event Format](https://docs.umbrella.com/developer/enforcement-api/generic-event-format2/).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|events|[]event|None|True|Generic event format field. More info at https://docs.umbrella.com/developer/enforcement-api/generic-event-format2/|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|object|True|List of added IDs|

Example output:

```

{
  "ID": [
    "42216a75,da20,4a1e,93bc-b07edfacc1f3"
  ]
}

```

#### Delete Domain by ID

This action is used to delete domain from user domain list by ID.
The delete comand should include the numerical identifier (ID) as specified in the LIST endpoint or the actual domain name you'd like to delete.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ID|integer|None|True|Unique ID number of domain|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|True|Action status [success | error]|

Example output:

```

{
  "status": "success"
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.2 - Bug fix: Fix 'Key not found' by setting SSL certificate verify to False 
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Cisco Umbrella Enforcement](https://enforcement-api.readme.io/)
* [Generic Event Format](https://docs.umbrella.com/developer/enforcement-api/generic-event-format2/)
* [Authentication](https://docs.umbrella.com/developer/enforcement-api/authentication-and-versioning/)

