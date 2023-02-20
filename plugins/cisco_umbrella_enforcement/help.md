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
|ssl_verify|boolean|True|True|Boolean value to indicate whether to add SSL verify to requests|None|True|

Example input:

```
{
  "api_key": "9de5069c5afe602b2ea0a04b66beb2c0",
  "ssl_verify": true
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
|name|string|None|True|Domain name|None|internetbadguys.bad-v5.com|

Example input:

```
{
  "name": "internetbadguys.bad-v5.com"
}
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
|alertTime|string|None|True|The time the event was sent to Umbrella|None|2013-02-08T09:30:26Z|
|deviceId|string|None|True|The ID of the device sending the event|None|12345678-1234-1234-1234-123456789123|
|deviceVersion|string|None|True|The version of the device sending the event|None|https://example.com|
|disableDstSafeguards|boolean|False|False|True bypasses validations normally performed against submitted events|None|False|
|dstDomain|string|None|True|The destination domain specified following RFC 3986 encoding guidelines|None|https://example.com|
|dstIP|string|None|False|The destination UP of the domain, specified in IPv4 dotted-decimal notation|None|https://example.com|
|dstUrl|string|None|True|The destination URL specified following RFC 3986 encoding guidelines|None|https://example.com|
|eventDescription|string|None|False|Variant or other descriptior of event type|None|None|
|eventHash|string|None|False|A unique hash of the event|None|9de5069c5afe602b2ea0a04b66beb2c0|
|eventSeverity|string|None|False|The partner threat level or rating|None|severe, bad, high|
|eventTime|string|None|True|The time the event was detected|None|2013-02-08T09:30:26Z|
|eventType|string|None|False|Common name or classification of threat|None|severe|
|externalURL|string|None|False|External page containing additional information about event|None|None|
|fileHash|string|None|False|SHA-1 of file reported by appliance|None|02699626f388ed830012e5b787640e71c56d42d8|
|fileName|string|None|False|Path to file exhibiting malicious behaviour|None|/path/to/file|
|protocolVersion|string|https://example.com|True|The version of the protocol for the API|None|https://example.com|
|providerName|string|Security Platform|True|The provider name for the API|None|Security Platform|
|src|string|None|False|The first IP or hostname associated with the infected device|None|None|

Example input:

```
{
  "alertTime": "2013-02-08T09:30:26Z",
  "deviceId": "12345678-1234-1234-1234-123456789123",
  "deviceVersion": "1.0a",
  "disableDstSafeguards": false,
  "dstDomain": "www.internetbadguys.com",
  "dstIP": "8.8.8.8",
  "dstUrl": "http://internetbadguys.com/security?foo=there%20are%20spaces%20here",
  "eventHash": "9de5069c5afe602b2ea0a04b66beb2c0",
  "eventSeverity": "severe, bad, high",
  "eventTime": "2013-02-08T09:30:26Z",
  "eventType": "severe",
  "fileHash": "02699626f388ed830012e5b787640e71c56d42d8",
  "fileName": "/path/to/file",
  "protocolVersion": "1.0a",
  "providerName": "Security Platform"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ID|object|True|List of added IDs|

Example output:

```
{
  'ID': {'id': '5a050d19,1d08,4dd0,b8b4-6b34da9e4135'}
}
```

#### Delete Domain by ID

This action is used to delete domain from user domain list by ID.
The delete command should include the numerical identifier (ID) as specified in the LIST endpoint or the actual domain name you'd like to delete.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|ID|integer|None|True|Unique ID number of domain|None|1234567|

Example input:

```
{
  "ID": 1234567
}
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

* 2.0.0 - Action - Add event: Renamed inputs `DstURL` to `DstUrl` and `ID` to `deviceId` | Actions - Delete domains: Updated to return `{'success': True}` | Action - Add Event: Changed input from one object to multiple individual inputs | Refactored all the code to improve quality | Upgraded from `komand` to `insight-connect` | New feature: Added option to toggle SSL verify
* 1.0.1 - New spec and help.md format for the Extension Library
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Cisco Umbrella Enforcement](https://enforcement-api.readme.io/)
* [Generic Event Format](https://docs.umbrella.com/developer/enforcement-api/generic-event-format2/)
* [Authentication](https://docs.umbrella.com/developer/enforcement-api/authentication-and-versioning/)

