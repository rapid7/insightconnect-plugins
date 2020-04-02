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

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|api_key|credential_secret_key|None|True|Enter API key e.g. 1111-2222-3333-4444|None|

The API key is a UUID-v4 [Customer key](https://docs.umbrella.com/developer/enforcement-api/authentication-and-versioning/).

## Technical Details

### Actions

#### List Domains

This action is used to gather the lists of domains already added to the shared customer's domain list.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|meta|meta|True|The meta array shows which page of results is available, the number of results and next and previous available pages to query|
|data|[]data|True|The data array contains the domains in the domain list, along with a unique ID number for each domain|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain name|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|True|Action status [success \| error]|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|events|array|None|True|Array of JSON objects in generic event format. More info at https://docs.umbrella.com/developer/enforcement-api/generic-event-format2/|None|

Example input:

```

[{
    "dstURL": "http://internetbadguys.bad-v5.com/a-bad-url-v1",
    "alertTime": "2013-02-09T11:14:26.0Z",
    "ID": "ba6a59f4-e692-4724-ba36-c28132c761de",
    "deviceVersion": "13.7a",
    "dstDomain": "internetbadguys.bad-v5.com",
    "eventTime": "2013-02-09T09:30:26.0Z",
    "protocolVersion": "1.0a",
    "providerName": "Security Platform",
    "disableDstSafeguards": true,
    "eventHash": "e88b372b1f98882dca933fa8a2589670",
    "fileName": "https://www.fuw.edu.pl/~rwys/pk/notatki_cl.txt",
    "fileHash": "da89127fbe1d78313dbfff610b59ff24874bb983",
    "externalURL": "https://www.fuw.edu.pl/~rwys/pk/notatki_cl.txt",
    "src": "192.168.0.1",
    "eventSeverity": "severe",
    "eventType": "severe",
    "eventDescription": "Some another threat"
  },
  {
    "dstURL": "http://internetbadguys.bad-v6.com/a-bad-url-v2",
    "alertTime": "2013-02-10T11:14:26.0Z",
    "ID": "ba6a59f4-e692-4724-ba36-c28132c761de",
    "deviceVersion": "13.7a",
    "dstDomain": "internetbadguys.bad-v6.com",
    "eventTime": "2013-02-10T09:30:26.0Z",
    "protocolVersion": "1.0a",
    "providerName": "Security Platform"
 }]

```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|True|Id of created event|

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

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|ID|integer|None|True|Unique ID number of domain|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|True|Action status [success \| error]|

Example output:

```

{
  "status": "success"
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode | Update to new credential types
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Cisco Umbrella Enforcement](https://enforcement-api.readme.io/)
* [Generic Event Format](https://docs.umbrella.com/developer/enforcement-api/generic-event-format2/)
* [Authentication](https://docs.umbrella.com/developer/enforcement-api/authentication-and-versioning/)

