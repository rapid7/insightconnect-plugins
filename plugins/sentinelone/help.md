# Description

[SentinelOne](https://www.sentinelone.com/) is a next-gen cybersecurity company focused on protecting the enterprise through the endpoint. The SentinelOne plugin allows you to manage and mitigate all your security operations through SentinelOne.

This plugin utilizes the SentinelOne API, the documentation is located in the SentinelOne console.

# Key Features

* Get activities
* Get activity types
* Blacklist hashes
* Run agent actions
* Reload agent modules
* Get information about agents
* Search agents
* Get information about agent applications
* Create, get and cancel query
* Create IOC threat
* Enable and disable agent
* Fetch files
* Get events
* Get information about threats
* Manage threats
* Quarantine endpoints
* Run remote scripts
* Check account name availability
* Execute scans
* Trigger workflows on security alerts

# Requirements

* SentinelOne API key

# Supported Product Versions

* 2.1.0

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|apiKey|credential_secret_key|None|True|Credential secret API key|None|9de5069c5afe602b2ea0a04b66beb2c0|
|instance|string|None|True|SentinelOne Console instance e.g. https://<example-instance>.sentinelone.net|None|example-instance|
|userType|string|Console user|True|Type of user|['Console user', 'Service user']|Console user|

Example input:

```
{
  "apiKey": "9de5069c5afe602b2ea0a04b66beb2c0",
  "instance": "example-instance",
  "userType": "Console user"
}
```

## Technical Details

### Actions

#### Get Activities

This action is used to get a list of activities.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|accountIds|[]string|None|False|List of Account IDs to filter by|None|["400000000000000000"]|
|activityTypes|[]string|None|False|Return only these activity codes|None|["22", "23"]|
|agentIds|[]string|None|False|Return activities related to specified agent IDs|None|["9000000000000000"]|
|countOnly|boolean|None|False|If true, only total number of items will be returned, without any of the actual objects|None|False|
|createdAtBetween|string|None|False|Return activities created within this range (inclusive), example 1514978764288-1514978999999|None|1514978764288-1514978999999|
|createdAtGt|date|None|False|Return activities created after or at this date in ISO-8601, example 2020-12-18T18:49:26.257525Z|None|2020-12-18T18:49:26.257525Z|
|createdAtGte|date|None|False|Return activities created after or at this date in ISO-8601, example 2020-12-18T18:49:26.257525Z|None|2020-12-20T18:49:26.257525Z|
|createdAtLt|date|None|False|Return activities created before this date in ISO-8601|None|2020-12-20T18:49:26.257525Z|
|createdAtLte|date|None|False|Return activities created before or at this date in ISO-8601, example 2020-12-18T18:49:26.257525Z|None|2020-12-20T18:49:26.257525Z|
|groupIds|[]string|None|False|List of Group IDs|None|["500000000000000000"]|
|ids|[]string|None|False|List of Activity IDs|None|["800000000000000008"]|
|includeHidden|boolean|None|False|Include internal activities hidden from display|None|True|
|limit|integer|10|False|Limit number of returned items (1-1000)|None|10|
|siteIds|[]string|None|False|List of Site IDs to filter by|None|["5000000000000001"]|
|skip|integer|None|False|Skip first number of items (0-1000). Will return the number entries specified in the 'limit' input (default is 10)|None|1|
|skipCount|boolean|None|False|If true, total number of items will not be calculated, which speeds up execution time|None|False|
|sortBy|string|createdAt|False|The column to sort the results by|['id', 'activityType', 'createdAt']|createdAt|
|sortOrder|string|asc|False|Sort direction|['asc', 'desc']|asc|
|threatIds|[]string|None|False|Return activities related to specified threat IDs|None|["100000000000000000"]|
|userEmail|string|None|False|Email of the user who invoked the activity (If applicable)|None|user@example.com|
|userIds|[]string|None|False|The user who invoked the activity (If applicable)|None|["500000000000000003"]|

Example input:

```
{
  "accountIds": [
    "400000000000000000"
  ],
  "activityTypes": [
    "22",
    "23"
  ],
  "agentIds": [
    "9000000000000000"
  ],
  "countOnly": false,
  "createdAtBetween": "1514978764288-1514978999999",
  "createdAtGt": "2020-12-18T18:49:26.257525Z",
  "createdAtGte": "2020-12-20T18:49:26.257525Z",
  "createdAtLt": "2020-12-20T18:49:26.257525Z",
  "createdAtLte": "2020-12-20T18:49:26.257525Z",
  "groupIds": [
    "500000000000000000"
  ],
  "ids": [
    "800000000000000008"
  ],
  "includeHidden": true,
  "limit": 10,
  "siteIds": [
    "5000000000000001"
  ],
  "skip": 1,
  "skipCount": false,
  "sortBy": "createdAt",
  "sortOrder": "asc",
  "threatIds": [
    "100000000000000000"
  ],
  "userEmail": "user@example.com",
  "userIds": [
    "500000000000000003"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|[]activity|True|List of activities obtained for the given filters|[]|
|totalItems|integer|False|Total number of activities found matching your query|100|

Example output:

```
{
  "data": [
    {
      "accountId": "400000000000000000",
      "accountName": "Example",
      "activityType": 22,
      "agentId": "9000000000000000",
      "createdAt": "2020-12-18T20:49:26.257525Z",
      "data": {
        "accountName": "Example",
        "computerName": "so-agent-win12",
        "confidenceLevel": "malicious",
        "fileContentHash": "02699626f388ed830012e5b787640e71c56d42d8",
        "fileDisplayName": "test.txt",
        "filePath": "\\Device\\HarddiskVolume2\\Users\\Administrator\\Desktop\\test.txt",
        "groupName": "Default Group",
        "siteName": "Example",
        "threatClassification": "Trojan",
        "threatClassificationSource": "Cloud"
      },
      "groupId": "500000000000000000",
      "groupName": "Default Group",
      "id": "800000000000000008",
      "primaryDescription": "Threat with confidence level malicious detected: test.txt",
      "secondaryDescription": "02699626f388ed830012e5b787640e71c56d42d8",
      "siteId": "5000000000000001",
      "siteName": "Example",
      "threatId": "100000000000000000",
      "updatedAt": "2020-12-18T20:49:26.257525Z"
    }
  ],
  "totalItems": 10
}
```

#### Get Activity Types

This action is used to get a list of activity types.

##### Input

*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|activityTypes|[]activityTypes|True|List of activity types|[]|

Example output:

```
{
  "activityTypes": [
    {
      "id": 1234,
      "descriptionTemplate": "The Management user {{ username }} created Account {{ account_name }}.",
      "action": "Account Created"
    }
  ]
}
```

#### Run Agent Action

This action is used to perform actions relating to your SentinelOne agents. This will help manage your assets connected to your SentinelOne console. Documentation for these actions can be found at https://yoururl.sentinelone.net/api-doc/api-details?category=agent-actions.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|None|True|Agent action to run|['abort-scan', 'connect', 'decommission', 'disconnect', 'fetch-logs', 'initiate-scan', 'restart-machine', 'shutdown', 'uninstall']|connect|
|filter|object|None|True|Applied filter - only matched agents will be affected by the requested action. Leave empty to apply the action on all applicable agents. Note - decommission, disconnect, restart-machine, shutdown and uninstall actions require that one of the following filter arguments be supplied - ids, groupIds, or filterId|None|{"ids": ["1000000000000000000"]}|

Example input:

```
{
  "action": "connect",
  "filter": {
    "ids": [
      "1000000000000000000"
    ]
  }
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|affected|integer|False|Number of entities affected by the requested operation|1|

Example output:

```
{
  "affected": 1
}
```

#### Agents Reload

This action is used to reload an agent module (applies to Windows agents only).

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|filter|object|None|True|Applied filter - only matched agents will be affected by the requested action. Leave empty to apply the action on all applicable agents|None|{"ids": ["1000000000000000000"]}|
|module|string|None|True|Agent module to reload|['monitor', 'static', 'agent', 'log']|monitor|

Example input:

```
{
  "filter": {
    "ids": [
      "1000000000000000000"
    ]
  },
  "module": "monitor"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|affected|integer|False|Number of entities affected by the requested operation|1|

Example output:

```
{
  "affected": 1
}
```

#### Count Summary

This action is used to summary of agents by numbers.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|accountIds|[]string|None|False|List of Account IDs to filter by|None|["4000000000000000000"]|
|siteIds|[]string|None|False|List of Site IDs to filter by|None|["500000000000000000"]|

Example input:

```
{
  "accountIds": [
    "4000000000000000000"
  ],
  "siteIds": [
    "500000000000000000"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|decommissioned|integer|False|Number of decommissioned agents|0|
|infected|integer|False|Number of agents with at least one active threat|1|
|online|integer|False|Number of online agents|2|
|outOfDate|integer|False|Number of agents running an older software version|1|
|total|integer|False|Number of installed active agents|2|
|upToDate|integer|False|Number of agents with the most up-to-date software version|2|

Example output:

```
{
  "decommissioned": 0,
  "infected": 1,
  "online": 2,
  "outOfDate": 1,
  "total": 2,
  "upToDate": 2
}
```

#### Agents Applications

This action is used to retrieve running applications for a specific agent.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|ids|[]string|None|True|Agent ID list|None|["1000000000000000000"]|

Example input:

```
{
  "ids": [
    "1000000000000000000"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|[]agentApplications|True|List of installed applications|[]|

Example output:

```
{
  "data": [
    {
      "installedDate": "2023-01-01T00:00:00.000000Z",
      "name": "Example App1",
      "publisher": "Microsoft Corporation",
      "size": 1234,
      "version": "1.0.4.5"
    },
    {
      "installedDate": "2023-01-01T00:00:00.000000Z",
      "name": "Example App2",
      "publisher": "Example Publisher",
      "size": 1111,
      "version": "1.0.5.6"
    }
  ]
}
```

#### Blacklist

This action is used to blacklist and unblacklist a SHA1 hash. The blacklist is attempted for Linux, Windows, and MacOS operating systems and for all sites that the user has permission to manage.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|blacklistState|boolean|True|True|True to create blacklist hash, false to unblacklist hash|None|True|
|description|string|Hash blacklisted from InsightConnect|False|Description for why the hash is blacklisted|None|Hash blacklisted from InsightConnect|
|hash|string|None|True|Create a blacklist item from a SHA1 hash|None|3395856ce81f2b7382dee72602f798b642f14140|

Example input:

```
{
  "blacklistState": true,
  "description": "Hash blacklisted from InsightConnect",
  "hash": "3395856ce81f2b7382dee72602f798b642f14140"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|message|string|True|Return details about action results|The given hash has been blacklisted|
|success|boolean|True|Return true if blacklist item was created or deleted|True|

Example output:

```
{
  "message": "The given hash has been blacklisted",
  "success": true
}
```

#### Blacklist by Content Hash

This action is used to add hashed content to global blacklist. The input makes use of contentHash from the threat summary.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|hash|string|None|True|Content hash to add to blacklist|None|3395856ce81f2b7382dee72602f798b642f14140|

Example input:

```
{
  "hash": "3395856ce81f2b7382dee72602f798b642f14140"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|affected|integer|False|Number of entities affected by the requested operation|1|

Example output:

```
{
  "affected": 1
}
```

#### Cancel Running Query
  
This action is used to stop a Deep Visibility Query by queryId.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|queryId|string|None|True|QueryId obtained when creating a query under Create Query|None|qd94e330ac025d525b5948bdf897b955e|

Example input:

```
{
  "queryId": "qd94e330ac025d525b5948bdf897b955e"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|querySuccess|False|SentinelOne API call response data|{}|

Example output:

```
{
  "response": {
    "success": "FINISHED"
  }
}
```

#### Create IOC Threat

This action is used to create a threat from an IOC event.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agentId|string|None|True|Agent ID for the slim threat|None|1000000000000000000|
|groupId|string|None|False|ID of the group|None|1000000000000000001|
|hash|string|None|True|SHA1 hash|None|A94A8FE5CCB19BA61C4C0873D391E987982FBBD3|
|note|string|None|False|Note added to the created threat|None|Example note|
|path|string|None|False|File path|None|path|

Example input:

```
{
  "agentId": "1000000000000000000",
  "groupId": "1000000000000000001",
  "hash": "A94A8FE5CCB19BA61C4C0873D391E987982FBBD3",
  "note": "Example note",
  "path": "path"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|affected|integer|False|Number of entities affected by the requested operation|1|

Example output:

```
{
  "affected": 1
}
```

#### Create Query

This action is used to start a Deep Visibility Query and get the queryId. You can use the queryId for other commands, such as Get Events and Get Query Status.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|accountIds|[]string|None|False|List of account IDs to filter by|None|["225494730938491234", "225494730938491235"]|
|fromDate|date|None|True|Events created after this timestamp|None|2021-03-01T04:49:26+00:00|
|groupIds|[]string|None|False|List of group IDs to filter by|None|["225494730938491234", "225494730938491235"]|
|isVerbose|boolean|None|False|Show all fields or just priority fields|None|True|
|limit|integer|100|False|Limit number of returned items (1-20000)|None|10|
|query|string|None|True|Events matching the query search term will be returned|None|AgentName IS NOT EMPTY|
|queryType|[]string|None|False|Query search type|None|["events"]|
|siteIds|[]string|None|False|List of site IDs to filter by|None|["225494730938491234", "225494730938491235"]|
|tenant|boolean|None|False|Indicates a Global (tenant) scope request|None|True|
|toDate|date|None|True|Events created before or at this timestamp|None|2021-03-23T04:49:26+00:00|

Example input:

```
{
  "accountIds": [
    "225494730938491234",
    "225494730938491235"
  ],
  "fromDate": "2021-03-01T04:49:26+00:00",
  "groupIds": [
    "225494730938491234",
    "225494730938491235"
  ],
  "isVerbose": true,
  "limit": 10,
  "query": "AgentName IS NOT EMPTY",
  "queryType": [
    "events"
  ],
  "siteIds": [
    "225494730938491234",
    "225494730938491235"
  ],
  "tenant": true,
  "toDate": "2021-03-23T04:49:26+00:00"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|queryId|string|False|The ID of the created query|qd94e330ac025d525b5948bdf897b955e|

Example output:

```
{
  "queryId": "qd94e330ac025d525b5948bdf897b955e"
}
```

#### Disable Agent

This action is used to disable agents that match the filter.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|False|Agent to perform disable action on. Accepts IP address, MAC address, hostname, UUID or agent ID. Leave empty to perform action on all applicable Agents|None|hostname123|
|expirationTime|date|None|False|Agents will be re-enabled after this timestamp|None|2020-02-27 04:49:26.257525+00:00|
|expirationTimezone|string|Central Standard Time (North America) [CST]|False|Timezone for the expiration timestamp. Set with expiration time|['Australian Central Daylight Saving Time [ACDT]', 'Australian Central Standard Time [ACST]', 'Acre Time [ACT]', 'Atlantic Daylight Time [ADT]', 'Australian Eastern Daylight Saving Time [AEDT]', 'Australian Eastern Standard Time [AEST]', 'Australian Eastern Time [AET]', 'Afghanistan Time [AFT]', 'Alaska Daylight Time [AKDT]', 'Alaska Standard Time [AKST]', 'Alma-Ata Time [ALMT]', 'Amazon Summer Time (Brazil) [AMST]', 'Amazon Time (Brazil) [AMT]', 'Armenia Time [AMT]', 'Anadyr Time [ANAT]', 'Aqtobe Time [AQTT]', 'Argentina Time [ART]', 'Arabia Standard Time [AST]', 'Atlantic Standard Time [AST]', 'Australian Western Standard Time [AWST]', 'Azores Summer Time [AZOST]', 'Azores Standard Time [AZOT]', 'Azerbaijan Time [AZT]', 'Brunei Time [BNT]', 'British Indian Ocean Time [BIOT]', 'Baker Island Time [BIT]', 'Bolivia Time [BOT]', 'Brasilia Summer Time [BRST]', 'Brasilia Time [BRT]', 'Bangladesh Standard Time [BST]', 'Bougainville Standard Time [BST]', 'Bhutan Time [BTT]', 'Central Africa Time [CAT]', 'Cocos Islands Time [CCT]', 'Central Daylight Time (North America) [CDT]', 'Cuba Daylight Time [CDT]', 'Central European Summer Time [CEST]', 'Central European Time [CET]', 'Chatham Daylight Time [CHADT]', 'Chatham Standard Time [CHAST]', 'Choibalsan Standard Time [CHOT]', 'Choibalsan Summer Time [CHOST]', 'Chamorro Standard Time [CHST]', 'Chuuk Time [CHUT]', 'Clipperton Island Standard Time [CIST]', 'Central Indonesia Time [WITA]', 'Cook Island Time [CKT]', 'Chile Summer Time [CLST]', 'Chile Standard Time [CLT]', 'Colombia Summer Time [COST]', 'Colombia Time [COT]', 'Central Standard Time (North America) [CST]', 'China Standard Time [CST]', 'Cuba Standard Time [CST]', 'Central Time [CT]', 'Cape Verde Time [CVT]', 'Christmas Island Time [CXT]', 'Davis Time [DAVT]', 'Dumont dUrville Time [DDUT]', 'AIX-specific equivalent of Central European Time [DFT]', 'Easter Island Summer Time [EASST]', 'Easter Island Standard Time [EAST]', 'East Africa Time [EAT]', 'Ecuador Time [ECT]', 'Eastern Daylight Time (North America) [EDT]', 'Eastern European Summer Time [EEST]', 'Eastern European Time [EET]', 'Eastern Greenland Summer Time [EGST]', 'Eastern Greenland Time [EGT]', 'Eastern Indonesian Time [WIT]', 'Eastern Standard Time (North America) [EST]', 'Further-eastern European Time [FET]', 'Fiji Time [FJT]', 'Falkland Islands Summer Time [FKST]', 'Falkland Islands Time [FKT]', 'Fernando de Noronha Time [FNT]', 'Galapagos Time [GALT]', 'Gambier Islands Time [GAMT]', 'Georgia Standard Time [GET]', 'French Guiana Time [GFT]', 'Gilbert Island Time [GILT]', 'Gambier Island Time [GIT]', 'Greenwich Mean Time [GMT]', 'South Georgia and the South Sandwich Islands Time [GST]', 'Gulf Standard Time [GST]', 'Guyana Time [GYT]', 'Hawaii-Aleutian Daylight Time [HDT]', 'Heure Avancee Europe Centrale French-language name for CEST [HAEC]', 'Hawaii-Aleutian Standard Time [HST]', 'Hong Kong Time [HKT]', 'Heard and McDonald Islands Time [HMT]', 'Hovd Time [HOVT]', 'Indochina Time [ICT]', 'International Day Line West time zone [IDLW]', 'Israel Daylight Time [IDT]', 'Indian Ocean Time [IOT]', 'Iran Daylight Time [IRDT]', 'Irkutsk Time [IRKT]', 'Iran Standard Time [IRST]', 'Indian Standard Time [IST]', 'Irish Standard Time [IST]', 'Israel Standard Time [IST]', 'Japan Standard Time [JST]', 'Kaliningrad Time [KALT]', 'Kyrgyzstan Time [KGT]', 'Kosrae Time [KOST]', 'Krasnoyarsk Time [KRAT]', 'Korea Standard Time [KST]', 'Lord Howe Standard Time [LHST]', 'Lord Howe Summer Time [LHST]', 'Line Islands Time [LINT]', 'Magadan Time [MAGT]', 'Marquesas Islands Time [MART]', 'Mawson Station Time [MAWT]', 'Mountain Daylight Time (North America) [MDT]', 'Middle European Time [MET]', 'Middle European Summer Time [MEST]', 'Marshall Islands Time [MHT]', 'Macquarie Island Station Time [MIST]', 'Marquesas Islands Time [MIT]', 'Myanmar Standard Time [MMT]', 'Moscow Time [MSK]', 'Malaysia Standard Time [MST]', 'Mountain Standard Time (North America) [MST]', 'Mauritius Time [MUT]', 'Maldives Time [MVT]', 'Malaysia Time [MYT]', 'New Caledonia Time [NCT]', 'Newfoundland Daylight Time [NDT]', 'Norfolk Island Time [NFT]', 'Novosibirsk Time [NOVT]', 'Nepal Time [NPT]', 'Newfoundland Standard Time [NST]', 'Newfoundland Time [NT]', 'Niue Time [NUT]', 'New Zealand Daylight Time [NZDT]', 'New Zealand Standard Time [NZST]', 'Omsk Time [OMST]', 'Oral Time [ORAT]', 'Pacific Daylight Time (North America) [PDT]', 'Peru Time [PET]', 'Kamchatka Time [PETT]', 'Papua New Guinea Time [PGT]', 'Phoenix Island Time [PHOT]', 'Philippine Time [PHT]', 'Pakistan Standard Time [PKT]', 'Saint Pierre and Miquelon Daylight Time [PMDT]', 'Saint Pierre and Miquelon Standard Time [PMST]', 'Pohnpei Standard Time [PONT]', 'Pacific Standard Time (North America) [PST]', 'Philippine Standard Time [PST]', 'Palau Time [PWT]', 'Paraguay Summer Time [PYST]', 'Paraguay Time [PYT]', 'Reunion Time [RET]', 'Rothera Research Station Time [ROTT]', 'Sakhalin Island Time [SAKT]', 'Samara Time [SAMT]', 'South African Standard Time [SAST]', 'Solomon Islands Time [SBT]', 'Seychelles Time [SCT]', 'Samoa Daylight Time [SDT]', 'Singapore Time [SGT]', 'Sri Lanka Standard Time [SLST]', 'Srednekolymsk Time [SRET]', 'Suriname Time [SRT]', 'Samoa Standard Time [SST]', 'Singapore Standard Time [SST]', 'Showa Station Time [SYOT]', 'Tahiti Time [TAHT]', 'Thailand Standard Time [THA]', 'French Southern and Antarctic Time [TFT]', 'Tajikistan Time [TJT]', 'Tokelau Time [TKT]', 'Timor Leste Time [TLT]', 'Turkmenistan Time [TMT]', 'Turkey Time [TRT]', 'Tonga Time [TOT]', 'Tuvalu Time [TVT]', 'Ulaanbaatar Summer Time [ULAST]', 'Ulaanbaatar Standard Time [ULAT]', 'Coordinated Universal Time [UTC]', 'Uruguay Summer Time [UYST]', 'Uruguay Standard Time [UYT]', 'Uzbekistan Time [UZT]', 'Venezuelan Standard Time [VET]', 'Vladivostok Time [VLAT]', 'Volgograd Time [VOLT]', 'Vostok Station Time [VOST]', 'Vanuatu Time [VUT]', 'Wake Island Time [WAKT]', 'West Africa Summer Time [WAST]', 'West Africa Time [WAT]', 'Western European Summer Time [WEST]', 'Western European Time [WET]', 'Western Indonesian Time [WIB]', 'West Greenland Summer Time [WGST]', 'West Greenland Time [WGT]', 'Western Standard Time [WST]', 'Yakutsk Time [YAKT]', 'Yekaterinburg Time [YEKT]']|Central Standard Time (North America) [CST]|
|filter|object|None|False|Filter to apply action on specified agents. Leave empty to perform action on all applicable Agents|None|{}|
|reboot|boolean|False|True|Set true to reboot the endpoint, false to skip rebooting|None|True|

Example input:

```
{
  "agent": "hostname123",
  "expiration_time": "2020-02-27T04:49:26.257525Z",
  "expiration_timezone": "Central Standard Time (North America) [CST]",
  "filter": {
    "updatedAt__gt": "2019-02-27T04:49:26.257525Z"
  },
  "reboot": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|affected|integer|True|Number of entities affected by the requested operation|1|

Example output:

```
{
  "affected": 1
}
```

#### Enable Agent

This action is used to enable agents that match the filter.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|False|Agent to perform disable action on. Accepts IP address, MAC address, hostname, UUID or agent ID. Leave empty to perform action on all applicable Agents|None|hostname123|
|filter|object|None|False|Filter to apply action on specified agents. Leave empty to perform action on all applicable Agents|None|{}|
|reboot|boolean|None|True|Set true to reboot the endpoint, false to skip rebooting|None|True|

Example input:

```
{
  "agent": "hostname123",
  "filter": {
    "updatedAt__gt": "2019-02-27T04:49:26.257525Z"
  },
  "reboot": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|affected|integer|True|Number of entities affected by the requested operation|1|

Example output:

```
{
  "affected": 1
}
```

#### Fetch File

This action is used to fetch file for a specific agent ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agentId|string|None|True|Agent ID|None|1000000000000000000|
|filePath|string|None|True|File path of file to fetch. If a file can be fetched, it will be uploaded to the SentinelOne console for download|None|C:/windows/system32/winevt/logs/application.evtx|
|password|password|None|True|File encryption password. The password cannot contain whitespace and must be 10 or more characters with a mix of upper and lower case letters, numbers, and symbols|None|MySecretPass123!|

Example input:

```
{
  "agentId": "1000000000000000000",
  "filePath": "C:/windows/system32/winevt/logs/application.evtx",
  "password": "MySecretPass123!"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|True|File fetch response status|True|

Example output:

```
{
  "success": true
}
```

#### Get Agent Details

This action is used to retrieve agent details.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|True|Agent to retrieve device information from. Accepts IP address, MAC address, hostname, UUID or agent ID|None|hostname123|
|operationalState|string|Any|False|Agent operational state|['Any', 'na', 'fully_disabled', 'partially_disabled', 'disabled_error']|na|

Example input:

```
{
  "agent": "hostname123",
  "operationalState": "na"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|agent|agentData|False|Detailed information about agent found|{}|

Example output:

```
{
  "agent": {
    "accountId": "000000000000000002",
    "accountName": "ExampleName2",
    "activeThreats": 0,
    "agentVersion": "1.0.2.3",
    "allowRemoteShell": false,
    "appsVulnerabilityStatus": "up_to_date",
    "computerName": "hostname123",
    "consoleMigrationStatus": "N/A",
    "coreCount": 1,
    "cpuCount": 1,
    "cpuId": "CPU A0 v1 @ 3.00GHz",
    "createdAt": "2023-01-01T00:00:00.000000Z",
    "domain": "WORKGROUP",
    "encryptedApplications": false,
    "externalIp": "198.51.100.1",
    "firewallEnabled": true,
    "groupId": "000000000000000001",
    "groupIp": "1.2.3.x",
    "groupName": "Example Group",
    "id": "0000000000000000002",
    "inRemoteShellSession": false,
    "infected": false,
    "installerType": ".exe",
    "isActive": true,
    "isDecommissioned": false,
    "isPendingUninstall": false,
    "isUninstalled": false,
    "isUpToDate": true,
    "lastActiveDate": "2023-01-01T00:00:00.000000Z",
    "lastIpToMgmt": "198.51.100.1",
    "locationEnabled": true,
    "locationType": "fallback",
    "locations": [
      {
        "id": "000000000000000001",
        "name": "Fallback",
        "scope": "global"
      }
    ],
    "machineType": "server",
    "mitigationMode": "protect",
    "mitigationModeSuspicious": "detect",
    "modelName": "Example Model",
    "networkInterfaces": [
      {
        "id": "000000000000000002",
        "inet": [
          "198.51.100.1"
        ],
        "inet6": [
          "2001:db8:8:4::2"
        ],
        "name": "Ethernet",
        "physical": "12-23-45-67-89-12"
      }
    ],
    "networkQuarantineEnabled": false,
    "networkStatus": "disconnected",
    "operationalState": "na",
    "operationalStateExpiration": "None",
    "osArch": "64 bit",
    "osName": "System Name",
    "osRevision": "9200",
    "osStartTime": "2023-01-01T00:00:00Z",
    "osType": "windows",
    "osUsername": "None",
    "rangerStatus": "NotApplicable",
    "rangerVersion": "None",
    "registeredAt": "2023-01-01T00:00:00.000000Z",
    "remoteProfilingState": "disabled",
    "remoteProfilingStateExpiration": "None",
    "scanAbortedAt": "None",
    "scanFinishedAt": "2023-01-01T00:00:00.000000Z",
    "scanStartedAt": "2023-01-01T00:00:00.000000Z",
    "scanStatus": "finished",
    "siteId": "00000000000000001",
    "siteName": "Example",
    "threatRebootRequired": false,
    "totalMemory": 1023,
    "updatedAt": "2023-01-01T00:00:00.000000Z",
    "uuid": "9de5069c5afe602b2ea0a04b66beb2c0"
  }
}
```

#### Get Events

This action is used to get all Deep Visibility events from a queryId.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|limit|integer|None|False|Limit number of returned items (1-1000), if no limit is provided returns all the results up to 20,000|None|10|
|queryId|string|None|True|QueryId obtained when creating a query under Create Query|None|qd94e330ac025d525b5948bdf897b955e|
|subQuery|string|None|False|Sub query to run on the data that was already pulled|None|AgentName IS NOT EMPTY|

Example input:

```
{
  "limit": 10,
  "queryId": "qd94e330ac025d525b5948bdf897b955e",
  "subQuery": "AgentName IS NOT EMPTY"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|errors|[]object|False|Errors|[]|
|events|[]eventData|False|Response events data|[]|

Example output:

```
{
  "events": [
    {
      "accountId": "0000000000000000001",
      "agentDomain": "WORKGROUP",
      "agentGroupId": "0000000000000000001",
      "agentId": "0000000000000000001",
      "agentInfected": true,
      "agentIp": "198.51.100.1",
      "agentIsActive": true,
      "agentIsDecommissioned": false,
      "agentMachineType": "laptop",
      "agentName": "ExampleName1",
      "agentNetworkStatus": "connected",
      "agentOs": "windows",
      "agentTimestamp": "2023-10-23T00:00:00.000Z",
      "agentUuid": "b7b2d39171be4ae1af90f93d7ed20f07",
      "createdAt": "2023-10-23T00:00:00.000Z",
      "endpointMachineType": "desktop",
      "endpointName": "ExampleName1",
      "endpointOs": "windows",
      "eventTime": "2023-10-23T00:00:00.000Z",
      "eventType": "Task Update",
      "id": "000000000000000001",
      "isAgentVersionFullySupportedForPg": false,
      "isAgentVersionFullySupportedForPgMessage": "Example message",
      "lastActivatedAt": "2023-10-23T00:00:00.000Z",
      "objectType": "scheduled_task",
      "parentProcessUniqueKey": "ABCD1234",
      "pid": "1234",
      "processGroupId": "ABCD1234",
      "processIntegrityLevel": "INTEGRITY_LEVEL_UNKNOWN",
      "processStartTime": "2023-10-23T00:00:00.000Z",
      "processUniqueKey": "ABCD1234",
      "relatedToThreat": "False",
      "siteId": "0000000000000000001",
      "storyline": "ABCD1234",
      "taskName": "Example Name",
      "trueContext": "ABCD1234"
    },
    {
      "accountId": "0000000000000000001",
      "agentDomain": "WORKGROUP",
      "agentGroupId": "0000000000000000001",
      "agentId": "0000000000000000001",
      "agentInfected": true,
      "agentIp": "198.51.100.1",
      "agentIsActive": true,
      "agentIsDecommissioned": false,
      "agentMachineType": "laptop",
      "agentName": "ExampleName1",
      "agentNetworkStatus": "connected",
      "agentOs": "windows",
      "agentTimestamp": "2023-10-23T00:00:00.000Z",
      "agentUuid": "b7b2d39171be4ae1af90f93d7ed20f07",
      "createdAt": "2023-10-23T00:00:00.000Z",
      "endpointMachineType": "desktop",
      "endpointName": "ExampleName1",
      "endpointOs": "windows",
      "eventTime": "2023-10-23T00:00:00.000Z",
      "eventType": "Task Update",
      "id": "000000000000000002",
      "isAgentVersionFullySupportedForPg": false,
      "isAgentVersionFullySupportedForPgMessage": "Example message",
      "lastActivatedAt": "2023-10-23T00:00:00.000Z",
      "objectType": "scheduled_task",
      "parentProcessUniqueKey": "ABCD1234",
      "pid": "1234",
      "processGroupId": "ABCD1234",
      "processIntegrityLevel": "INTEGRITY_LEVEL_UNKNOWN",
      "processStartTime": "2023-10-23T00:00:00.000Z",
      "processUniqueKey": "ABCD1234",
      "relatedToThreat": "False",
      "siteId": "0000000000000000001",
      "storyline": "ABCD1234",
      "taskName": "Example Name",
      "trueContext": "ABCD1234"
    }
  ]
}
```

#### Get Events by Type

This action is used to get Deep Visibility results from the query that matches the given event type.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|eventType|string|None|True|Event type for Autocomplete|['Process Exit', 'Process Modification', 'Process Creation', 'Duplicate Process Handle', 'Duplicate Thread Handle', 'Open Remote Process Handle', 'Remote Thread Creation', 'Remote Process Termination', 'Command Script', 'IP Connect', 'IP Listen', 'File Modification', 'File Creation', 'File Scan', 'File Deletion', 'File Rename', 'Pre Execution Detection', 'Login', 'Logout', 'GET', 'OPTIONS', 'POST', 'PUT', 'DELETE', 'CONNECT', 'HEAD', 'DNS Resolved', 'DNS Unresolved', 'Task Register', 'Task Update', 'Task Start', 'Task Trigger', 'Task Delete', 'Registry Key Create', 'Registry Key Rename', 'Registry Key Delete', 'Registry Key Export', 'Registry Key Security Changed', 'Registry Key Import', 'Registry Value Modified', 'Registry Value Create', 'Registry Value Delete', 'Behavioral Indicators', 'Module Load']|Registry Key Create|
|limit|integer|None|False|Limit number of returned items (1-1000), if no limit is provided returns all the results up to 20,000|None|10|
|queryId|string|None|True|QueryId obtained when creating a query under Create Query|None|qd94e330ac025d525b5948bdf897b955e|
|subQuery|string|None|False|Sub query to run on the data that was already pulled|None|AgentName IS NOT EMPTY|

Example input:

```
{
  "eventType": "Registry Key Create",
  "limit": 10,
  "queryId": "qd94e330ac025d525b5948bdf897b955e",
  "subQuery": "AgentName IS NOT EMPTY"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|errors|[]object|False|Errors|[]|
|events|[]eventData|False|Response events data|[]|

Example output:

```
{
  "events": [
    {
      "accountId": "0000000000000000001",
      "agentDomain": "WORKGROUP",
      "agentGroupId": "0000000000000000001",
      "agentId": "0000000000000000001",
      "agentInfected": true,
      "agentIp": "198.51.100.1",
      "agentIsActive": true,
      "agentIsDecommissioned": false,
      "agentMachineType": "laptop",
      "agentName": "ExampleName1",
      "agentNetworkStatus": "connected",
      "agentOs": "windows",
      "agentTimestamp": "2023-10-23T00:00:00.000Z",
      "agentUuid": "b7b2d39171be4ae1af90f93d7ed20f07",
      "createdAt": "2023-10-23T00:00:00.000Z",
      "endpointMachineType": "desktop",
      "endpointName": "ExampleName1",
      "endpointOs": "windows",
      "eventTime": "2023-10-23T00:00:00.000Z",
      "eventType": "Task Update",
      "id": "000000000000000001",
      "isAgentVersionFullySupportedForPg": false,
      "isAgentVersionFullySupportedForPgMessage": "Example message",
      "lastActivatedAt": "2023-10-23T00:00:00.000Z",
      "objectType": "scheduled_task",
      "parentProcessUniqueKey": "ABCD1234",
      "pid": "1234",
      "processGroupId": "ABCD1234",
      "processIntegrityLevel": "INTEGRITY_LEVEL_UNKNOWN",
      "processStartTime": "2023-10-23T00:00:00.000Z",
      "processUniqueKey": "ABCD1234",
      "relatedToThreat": "False",
      "siteId": "0000000000000000001",
      "storyline": "ABCD1234",
      "taskName": "Example Name",
      "trueContext": "ABCD1234"
    },
    {
      "accountId": "0000000000000000001",
      "agentDomain": "WORKGROUP",
      "agentGroupId": "0000000000000000001",
      "agentId": "0000000000000000001",
      "agentInfected": true,
      "agentIp": "198.51.100.1",
      "agentIsActive": true,
      "agentIsDecommissioned": false,
      "agentMachineType": "laptop",
      "agentName": "ExampleName1",
      "agentNetworkStatus": "connected",
      "agentOs": "windows",
      "agentTimestamp": "2023-10-23T00:00:00.000Z",
      "agentUuid": "b7b2d39171be4ae1af90f93d7ed20f07",
      "createdAt": "2023-10-23T00:00:00.000Z",
      "endpointMachineType": "desktop",
      "endpointName": "ExampleName1",
      "endpointOs": "windows",
      "eventTime": "2023-10-23T00:00:00.000Z",
      "eventType": "Task Update",
      "id": "000000000000000002",
      "isAgentVersionFullySupportedForPg": false,
      "isAgentVersionFullySupportedForPgMessage": "Example message",
      "lastActivatedAt": "2023-10-23T00:00:00.000Z",
      "objectType": "scheduled_task",
      "parentProcessUniqueKey": "ABCD1234",
      "pid": "1234",
      "processGroupId": "ABCD1234",
      "processIntegrityLevel": "INTEGRITY_LEVEL_UNKNOWN",
      "processStartTime": "2023-10-23T00:00:00.000Z",
      "processUniqueKey": "ABCD1234",
      "relatedToThreat": "False",
      "siteId": "0000000000000000001",
      "storyline": "ABCD1234",
      "taskName": "Example Name",
      "trueContext": "ABCD1234"
    }
  ]
}
```

#### Get Query Status

This action is used to get that status of a Deep Visibility Query.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|queryId|string|None|True|QueryId obtained when creating a query under Create Query|None|qd94e330ac025d525b5948bdf897b955e|

Example input:

```
{
  "queryId": "qd94e330ac025d525b5948bdf897b955e"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|response|queryStatus|False|Information about the status of the given query|{}|

Example output:

```
{
  "response": {
    "progressStatus": 100,
    "queryModeInfo": {
      "lastActivatedAt": "2022-07-31T08:11:01+00:00",
      "mode": "scalyr"
    },
    "responseState": "FINISHED"
  }
}
```

#### Get Threat Summary

This action gets summary of all threats.

##### Input

*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|data|[]threatData|False|Data|[]|
|errors|[]object|False|Errors|[]|
|pagination|pagination|False|Pagination|{}|

Example output:

```
{
  "data": [
    {
      "agentOsType": "windows",
      "automaticallyResolved": false,
      "cloudVerdict": "black",
      "id": "566535959618699500",
      "engines": [
        "reputation"
      ],
      "fileContentHash": "3395856ce81f2b7382dee72602f798b642f14140",
      "fromCloud": false,
      "mitigationMode": "protect",
      "mitigationReport": {
        "quarantine": {
          "status": "success"
        },
        "kill": {
          "status": "success"
        }
      },
      "rank": 7,
      "siteName": "Rapid7",
      "whiteningOptions": [
        "hash"
      ],
      "agentComputerName": "vagrant-pc",
      "collectionId": "433377870883088367",
      "createdAt": "2019-02-21T16:05:49.251201Z",
      "mitigationStatus": "active",
      "classificationSource": "Static",
      "resolved": true,
      "accountName": "SentinelOne",
      "fileVerificationType": "NotSigned",
      "siteId": "521580416395045459",
      "fileIsExecutable": false,
      "fromScan": false,
      "agentNetworkStatus": "disconnecting",
      "createdDate": "2019-02-21T16:05:49.175000Z",
      "accountId": "433241117337583618",
      "initiatedBy": "agentPolicy",
      "initiatedByDescription": "Agent Policy",
      "threatAgentVersion": "3.0.1.3",
      "username": "vagrant-pc\\vagrant",
      "agentVersion": "3.0.1.3",
      "classifierName": "STATIC",
      "fileExtensionType": "Executable",
      "agentDomain": "WORKGROUP",
      "fileIsSystem": false,
      "agentInfected": false,
      "isCertValid": false,
      "isInteractiveSession": false,
      "isPartialStory": false,
      "updatedAt": "2020-05-28T21:53:36.064425Z",
      "agentId": "560700200554747611",
      "agentMachineType": "desktop",
      "classification": "Malware",
      "markedAsBenign": false,
      "threatName": "EICAR.com",
      "agentIsDecommissioned": true,
      "description": "malware detected - not mitigated yet (static engin...",
      "fileDisplayName": "EICAR.com",
      "agentIp": "198.51.100.100",
      "agentIsActive": false,
      "fileObjectId": "F0F63E0588AAC528",
      "filePath": "\\Device\\HarddiskVolume2\\Users\\vagrant\\Desktop\\EICA...",
      "maliciousGroupId": "542D14600CEBA01D"
    }
  ],
  "pagination": {
    "totalItems": 1
  }
}
```

#### Mark as Benign

This action is used to mark a threat as resolved.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|targetScope|string|None|True|Scope to be used for exclusions|['group', 'site', 'tenant', 'account']|site|
|threatId|string|None|True|ID of a threat|None|1000000000000000000|
|whiteningOption|string|None|False|Selected whitening option|['', 'browser-type', 'certificate', 'file-type', 'file_hash', 'path']|path|

Example input:

```
{
  "targetScope": "site",
  "threatId": "1000000000000000000",
  "whiteningOption": "path"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|affected|integer|False|Number of entities affected by the requested operation|1|

Example output:

```
{
  "affected": 1
}
```

#### Mark as Threat

This action is used to mark a suspicious threat as a threat.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|targetScope|string|None|True|Scope to be used for exclusions|['group', 'site', 'tenant']|site|
|threatId|string|None|True|ID of a threat|None|1000000000000000000|
|whiteningOption|string|None|False|Selected whitening option|['', 'browser-type', 'certificate', 'file-type', 'file_hash', 'path']|path|

Example input:

```
{
  "targetScope": "site",
  "threatId": "1000000000000000000",
  "whiteningOption": "path"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|affected|integer|False|Number of entities affected by the requested operation|1|

Example output:

```
{
  "affected": 1
}
```

#### Mitigate Threat

This action is used to apply a mitigation action to a threat.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|action|string|None|True|Mitigation action|['rollback-remediation', 'quarantine', 'kill', 'remediate', 'un-quarantine']|quarantine|
|threatId|string|None|True|ID of a threat|None|1000000000000000000|

Example input:

```
{
  "action": "quarantine",
  "threatId": "1000000000000000000"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|affected|integer|False|Number of entities affected by the requested operation|1|

Example output:

```
{
  "affected": 1
}
```

#### Available Name

This action is used to check if the account name is available.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|name|string|None|True|Account name to validate|None|example|

Example input:

```
{
  "name": "example"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|available|boolean|True|Whether the account name is available|True|

Example output:

```
{
  "available": true
}
```

#### Quarantine

This action is used to isolate (quarantine) endpoint from the network.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|True|Agent to perform quarantine action on. Accepts IP address, MAC address, hostname, UUID or agent ID|None|hostname123|
|quarantineState|boolean|None|True|True to quarantine host, false to unquarantine host|None|True|
|whitelist|[]string|None|False|This list contains a set of devices that should not be blocked. This can include IPs, hostnames, UUIDs and agent IDs|None|["198.51.100.100", "hostname123", "901345720792880606", "28db47168fa54f89aeed99769ac8d4dc"]|

Example input:

```
{
  "agent": "hostname123",
  "quarantineState": true,
  "whitelist": [
    "198.51.100.100",
    "hostname123",
    "901345720792880606",
    "9de5069c5afe602b2ea0a04b66beb2c0"
  ]
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|affected|integer|False|Number of entities affected by the requested operation|1|

Example output:

```
{
  "affected": 1
}
```

#### Run Remote Script

This action is used to run a remote script.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|code|string|None|False|Code from a third-party application, such as DUO or Google Authenticator, required to elevate the protected actions session|None|123456|
|ids|[]string|None|False|IDs of the agents to execute the script on. If no IDs provided, the script will run on ALL applicable agents. This id can be retrieved by using the get agent details action if neccessary|None|["100000000000000000"]|
|inputParameters|string|None|False|Parameters which will be passed to the remote script (may or may not be required, depending on script)|None|input_parameter1|
|outputDestination|string|None|True|Output destination of any script output|['Local', 'None', 'SentinelCloud']|SentinelCloud|
|outputDirectory|string|None|False|Output Directory (Only relevant if Local is selected for Output Destination)|None|/tmp/script_output|
|password|string|None|False|Password (Only relevant if SentinelCloud is selected for Output Destination). At least 10 characters and no whitespace|None|Password123??|
|scriptId|string|None|True|ID of the script to run (select the ID of a SentinelOne or user script from SentinelOne console)|None|1234567891234|
|taskDescription|string|None|True|Task Description|None|Task Description|
|timeout|integer|3600|False|Script runtime timeout (in seconds) for current execution (Value between 60 and 172800 seconds)|None|3600|

Example input:

```
{
  "code": "123456",
  "ids": [
    "100000000000000000"
  ],
  "inputParameters": "input_parameter1",
  "outputDestination": "Local",
  "outputDirectory": "/tmp/script_output",
  "password": "Password123??",
  "scriptId": 1234567891234,
  "taskDescription": "Task Description",
  "timeout": 3600
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|affected|integer|True|Number of entities affected by requested operation. For detailed output from running the script, log onto the SentinelOne console. Note this may be lower than the number of agent ids submitted if the script cannot be run on a particular agent e.g. due to OS type|1|

Example output:

```
{
  "affected": 1
}
```

#### Search Agents

This action searches for agents by IP address, MAC address, hostname, or device ID. It can also return all active or inactive agents when no agent address is provided using the `agent_active` parameter.
Note that retrieving all active agents can return a very large amount of data depending on the number of agents you have in your environment.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agent|string|None|False|Agent to retrieve device information from. Accepts IP address, MAC address, hostname, UUID or agent ID. If empty, this action will return all active or inactive agents depending on the value of the Agent Active input|None|hostname123|
|agentActive|string||False|Return a list of active, inactive or all agents when Agent input is not specified. Note that leaving it empty can return a very large amount of data|['True', 'False', '']|True|
|operationalState|string|Any|False|Agent operational state|['Any', 'na', 'fully_disabled', 'partially_disabled', 'disabled_error']|na|

Example input:

```
{
  "agent": "hostname123",
  "agentActive": "True",
  "operationalState": "na"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|agents|[]agentData|False|Detailed information about agents found|[]|

Example output:

```
{
  "agents": [
    {
      "accountId": "000000000000000001",
      "accountName": "ExampleName",
      "activeThreats": 0,
      "agentVersion": "1.0.2.3",
      "allowRemoteShell": false,
      "appsVulnerabilityStatus": "up_to_date",
      "computerName": "hostname123",
      "consoleMigrationStatus": "N/A",
      "coreCount": 1,
      "cpuCount": 1,
      "cpuId": "CPU A0 v1 @ 3.00GHz",
      "createdAt": "2023-01-01T00:00:00.000000Z",
      "domain": "WORKGROUP",
      "encryptedApplications": false,
      "externalIp": "198.51.100.1",
      "firewallEnabled": true,
      "groupId": "000000000000000001",
      "groupIp": "1.2.3.x",
      "groupName": "Example Group",
      "id": "0000000000000000001",
      "inRemoteShellSession": false,
      "infected": false,
      "installerType": ".exe",
      "isActive": true,
      "isDecommissioned": false,
      "isPendingUninstall": false,
      "isUninstalled": false,
      "isUpToDate": true,
      "lastActiveDate": "2023-01-01T00:00:00.000000Z",
      "lastIpToMgmt": "198.51.100.1",
      "locationEnabled": true,
      "locationType": "fallback",
      "locations": [
        {
          "id": "000000000000000001",
          "name": "Fallback",
          "scope": "global"
        }
      ],
      "machineType": "server",
      "mitigationMode": "protect",
      "mitigationModeSuspicious": "detect",
      "modelName": "Example Model",
      "networkInterfaces": [
        {
          "id": "000000000000000001",
          "inet": [
            "198.51.100.1"
          ],
          "inet6": [
            "2001:db8:8:4::1"
          ],
          "name": "Ethernet",
          "physical": "12-34-56-67-89-12"
        }
      ],
      "networkQuarantineEnabled": false,
      "networkStatus": "disconnected",
      "operationalState": "na",
      "operationalStateExpiration": "None",
      "osArch": "64 bit",
      "osName": "System Name",
      "osRevision": "9200",
      "osStartTime": "2023-01-01T00:00:00Z",
      "osType": "windows",
      "osUsername": "None",
      "rangerStatus": "NotApplicable",
      "rangerVersion": "None",
      "registeredAt": "2023-01-01T00:00:00.000000Z",
      "remoteProfilingState": "disabled",
      "remoteProfilingStateExpiration": "None",
      "scanAbortedAt": "None",
      "scanFinishedAt": "2023-01-01T00:00:00.000000Z",
      "scanStartedAt": "2023-01-01T00:00:00.000000Z",
      "scanStatus": "finished",
      "siteId": "00000000000000001",
      "siteName": "Rapid7",
      "threatRebootRequired": false,
      "totalMemory": 1023,
      "updatedAt": "2023-01-01T00:00:00.000000Z",
      "uuid": "9de5069c5afe602b2ea0a04b66beb2c0"
    }
  ]
}
```

#### Fetch Threats File

This action is used to fetch a file associated with the threat that matches the filter. Your user role must have permissions to Fetch Threat File - Admin, IR Team, SOC.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|Threat ID|None|939039647215561624|
|password|password|None|True|File encryption password. The password cannot contain whitespace and must be 10 or more characters with a mix of upper and lower case letters, numbers, and symbols|None|R@pid7Insightc0nnect|

Example input:

```
{
  "id": 939039647215561624,
  "password": "R@pid7Insightc0nnect"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|file|file|True|Base64 encoded threat file|{ "file": { "filename": "report.txt", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==" } }|

Example output:

```
{
  "file": {
    "filename": "report.txt",
    "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="
  }
}
```

#### Update Analyst Verdict

This action is used to update analyst verdict.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|analystVerdict|string|None|True|Analyst verdict|['true positive', 'suspicious', 'false positive', 'undefined']|true positive|
|incidentIds|[]string|None|True|A list of alert or threat IDs on which we may update the analyst verdict|None|["1118189762920424575", "1118189762920424576"]|
|type|string|None|True|Type of incidents|['threats', 'alerts']|threats|

Example input:

```
{
  "analystVerdict": "true positive",
  "incidentIds": [
    "1118189762920424575",
    "1118189762920424576"
  ],
  "type": "threats"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|affected|integer|False|Number of entities affected by the requested operation|1|

Example output:

```
{
  "affected": 1
}
```

#### Update Incident Status

This action is used to update incident status.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|incidentIds|[]string|None|True|A list of alert or threat IDs to update the incident status on|None|["1118189762920424575", "1118189762920424576"]|
|incidentStatus|string|None|True|Incident status|['unresolved', 'in progress', 'resolved']|resolved|
|type|string|None|True|Type of incidents|['threats', 'alerts']|threats|

Example input:

```
{
  "incidentIds": [
    "1118189762920424575",
    "1118189762920424576"
  ],
  "incidentStatus": "resolved",
  "type": "threats"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|affected|integer|False|Number of entities affected by the requested operation|1|

Example output:

```
{
  "affected": 1
}
```

### Triggers

#### Get Threats

This trigger is used to get threats.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|agentIsActive|boolean|True|False|Include agents currently connected to the management console|None|True|
|classifications|[]string|None|False|List of classifications to search|None|[""]|
|engines|[]string|None|False|Included engines|None|[""]|
|frequency|integer|5|False|Poll frequency in seconds|None|5|
|resolved|boolean|None|False|Set True to only trigger on resolved threats|None|True|

Example input:

```
{
  "agentIsActive": true,
  "frequency": 5,
  "resolved": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|threat|threatData|False|Threat|{ 'threat': { 'agentComputerName':'vagrant-pc', 'agentDomain':'WORKGROUP', 'agentId':'560700200554747611' }}|

Example output:

```
{
  "threat": {
    "agentComputerName": "example-pc",
    "agentDomain": "WORKGROUP",
    "agentId": "1234567890",
    "agentInfected": false,
    "agentIp": "xxx.xxx.xxx.xxx",
    "agentIsActive": true,
    "agentIsDecommissioned": false,
    "agentMachineType": "desktop",
    "agentNetworkStatus": "connected",
    "agentOsType": "windows",
    "agentVersion": "3.0.1.3",
    "classification": "Malware",
    "classificationSource": "Engine",
    "classifierName": "BLACKLIST",
    "cloudVerdict": "black",
    "collectionId": "1234567890",
    "createdAt": "2019-02-13T15:05:21.948892Z",
    "createdDate": "2019-02-13T15:05:21.605000Z",
    "description": "malware detected - not mitigated yet (static engine)",
    "engines": [
      "reputation"
    ],
    "fileContentHash": "02699626f388ed830012e5b787640e71c56d42d8",
    "fileDisplayName": "{D5EEFA7C-3EA6-4B78-BED3-56CB49156FD1}-EICAR.com",
    "fileExtensionType": "Executable",
    "fileIsExecutable": false,
    "fileIsSystem": false,
    "fileObjectId": "1234567890",
    "filePath": "\\Device\\HarddiskVolume2\\ProgramData\\Microsoft\\Windows Defender\\LocalCopy\\{ABCDEF}-EICAR.com",
    "fileVerificationType": "NotSigned",
    "fromCloud": false,
    "fromScan": false,
    "id": "1234567890",
    "isCertValid": false,
    "isInteractiveSession": false,
    "isPartialStory": false,
    "maliciousGroupId": "1234567890",
    "mitigationMode": "protect",
    "mitigationReport": {
      "kill": {
        "status": "success"
      },
      "quarantine": {
        "status": "success"
      }
    },
    "mitigationStatus": "mitigated",
    "rank": 7,
    "resolved": false,
    "siteId": "1234567890",
    "siteName": "Rapid7",
    "threatAgentVersion": "3.0.1.3",
    "updatedAt": "2019-02-13T15:05:22.274291Z",
    "whiteningOptions": [
      "hash"
    ]
  }
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**activityTypes**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Action|string|None|False|Action described in the activity|Account Created|
|Description Template|string|None|False|Activity description template as seen in activity page|The Management user {{ username }} created Account {{ account_name }}.|
|Type ID|integer|None|False|Activity type ID|1234|
  
**activity**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Account ID|string|None|False|Related account (If applicable)|100000000000000000|
|Account Name|string|None|False|Related account name (If applicable)|Example account|
|Activity Type|integer|None|False|Activity type|27|
|Activity UUID|string|None|False|Activity UUID|9de5069c-5afe-602b-2ea0-a04b66beb2c0|
|Agent ID|string|None|False|Related agent (If applicable)|100000000000000000|
|Agent Updated Version|string|None|False|Agent's new version (If applicable)|22.2.5.806|
|Comments|string|None|False|Comments|Example comment|
|Created At|string|None|False|Activity creation time (UTC)|2023-09-22 18:05:42.413981+00:00|
|Data|object|None|False|Extra activity specific data|{}|
|Description|string|None|False|Extra activity information|Example description|
|Group ID|string|None|False|Related group (If applicable)|100000000000000000|
|Group Name|string|None|False|Related group name (If applicable)|Example group|
|Hash|string|None|False|Threat file hash (If applicable)|02699626f388ed830012e5b787640e71c56d42d8|
|ID|string|None|False|Activity ID|100000000000000000|
|OS Family|string|None|False|Agent's OS type (if applicable)|windows|
|Primary Description|string|None|False|Primary description|Example description|
|Secondary Description|string|None|False|Secondary description|Example description|
|Site ID|string|None|False|Related site (If applicable)|100000000000000000|
|Site Name|string|None|False|Related site name (If applicable)|Example site|
|Threat ID|string|None|False|Related threat (If applicable)|100000000000000000|
|Updated At|string|None|False|Activity last updated time (UTC)|2023-09-22 19:23:09.368802+00:00|
|UserId|string|None|False|The user who invoked the activity (If applicable)|100000000000000000|
  
**agentApplications**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Installed Date|string|None|False|Date when application installed|2023-01-01 11:11:11+00:00|
|Name|string|None|False|Name of installed application|Example App Name|
|Publisher|string|None|False|Publisher of installed application|Example Publisher|
|Size|integer|None|False|Size of installed application|1234|
|Version|string|None|False|Version of installed application|1.2.3.4|
  
**pagination**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Next Cursor|string|None|False|Next cursor|eyJpZF9jb2x1bW4iOiAiaWQiLCAiaWRfdmFsdWUiOiAiNTM4NTAxODk4OTM4NTQ4MjI0IiwgInNvcnRfYnlfY29sdW1uIjogImFnZW50VGltZXN0YW1wIiwgInNvcnRfYnlfdmFsdWUiOiAiMjAyMS0wMy0yMlQxMjoyMDozNC40NDFaIiwgInNvcnRfb3JkZXIiOiAiZGVzYyJ=|
|Total Items|integer|None|False|Total items|10|
  
**threatData**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent Computer Name|string|None|False|Agent computer name|LAPTOP-R7|
|Agent Domain|string|None|False|Agent domain|WORKGROUP|
|Agent ID|string|None|False|Agent ID|225494730938493804|
|Agent Infected|boolean|None|False|Agent infected|False|
|Agent IP|string|None|False|Agent IP|192.0.2.0|
|Agent is Active|boolean|None|False|Agent is active|True|
|Agent is Decommissioned|boolean|None|False|Agent is decommissioned|False|
|Agent Machine Type|string|None|False|Agent machine type|laptop|
|Agent Network Status|string|None|False|Agent network status|connected|
|Agent OS Type|string|None|False|Agent OS type|windows|
|Agent Version|string|None|False|Agent version|1.0.2.4|
|Annotation|string|None|False|Annotation|Automatically resolved by SentinelOne Console|
|Browser Type|string|None|False|Browser type|Example Browser Type|
|Cert ID|string|None|False|Cert ID|225494730938493804|
|Classification|string|None|False|Classification|Malware|
|Classification Source|string|None|False|Classification source|Static|
|Classifier Name|string|None|False|Classifier name|LOGIC|
|Cloud Verdict|string|None|False|Cloud verdict|black|
|Collection ID|string|None|False|Collection ID|225494730938493804|
|Created At|string|None|False|Created At|2023-01-01 10:00:00+00:00|
|Created Date|string|None|False|Created date|2023-01-01 10:00:00+00:00|
|Description|string|None|False|Description|malware detected - not mitigated yet (static engine)|
|Engines|[]string|None|False|Engines|['penetration']|
|File Content Hash|string|None|False|File content hash|ffffffffffffffffffffffffffffffffffffffff|
|File Data|object|None|False|File data|{}|
|File Display Name|string|None|False|File display name|test.exe|
|File Extension Type|string|None|False|File extension type|Executable|
|File is Dotnet|boolean|None|False|File is dotnet|False|
|File is Executable|boolean|None|False|File is executable|False|
|File is System|boolean|None|False|File is system|False|
|File Malicious Content|boolean|None|False|File malicious content|False|
|File Object ID|string|None|False|File object ID|0AAA0AAA0AAA0AAA|
|File Path|string|None|False|File path|\\Device\\HarddiskVolume\\example\\test.exe|
|File Verification Type|string|None|False|File verification type|NotSigned|
|From Cloud|boolean|None|False|From cloud|False|
|From Scan|boolean|None|False|From scan|False|
|ID|string|None|False|ID|225494730938493804|
|In Quarantine|boolean|None|False|In quarantine|False|
|Indicators|[]integer|None|False|Indicators|[1, 2, 3]|
|Is Cert Valid|boolean|None|False|Is cert valid|True|
|Is Interactive Session|boolean|None|False|Is interactive session|True|
|Is Partial Story|boolean|None|False|Is partial story|False|
|Malicious Group ID|string|None|False|Malicious group ID|225494730938493804|
|Malicious Process Arguments|string|None|False|Malicious process arguments|C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe|
|Marked as Benign|boolean|None|False|Marked as Benign|False|
|Mitigation Mode|string|None|False|Mitigation mode|protect|
|Mitigation Report|object|None|False|Mitigation report|{}|
|Mitigation Status|string|None|False|Mitigation status|mitigated|
|Rank|integer|None|False|Rank|5|
|Resolved|boolean|None|False|Resolved|False|
|Site ID|string|None|False|Site ID|225494730938493804|
|Site Name|string|None|False|Site name|Example Site|
|Threat Agent Version|string|None|False|Threat agent version|1.0.3.4|
|Threat Name|string|None|False|Threat name|test.exe|
|Updated At|string|None|False|Updated at|2023-01-01 10:00:00+00:00|
|Username|string|None|False|Username|user1|
|Whitening Options|[]string|None|False|Whitening options|['hash']|
  
**location**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|ID|string|None|False|Location ID|1|
|Name|string|None|False|Location name|Example Location|
|Scope|string|None|False|Location scope|global|
  
**activeDirectory**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Computer Distinguished Name|string|None|False|Computer distinguished name|Example Name|
|Computer Member Of|[]string|None|False|Computer member of|['example']|
|Last User Distinguished Name|string|None|False|Last user distinguished name|Example Name|
|Last User Member Of|[]string|None|False|Last user member of|['example']|
  
**networkInterfaces**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Gateway IP|string|None|False|The default gateway IP|198.51.100.1|
|Gateway MAC Address|string|None|False|The default gateway MAC address|00:00:00:00:00:01|
|ID|string|None|False|ID|1|
|IPv4 Addresses|[]string|None|False|IPv4 addresses|['198.51.100.1']|
|IPv6 Addresses|[]string|None|False|IPv6 addresses|['ffff::ffff:ffff:ffff:ffff']|
|Name|string|None|False|Name|Ethernet0|
|Physical|string|None|False|Interface's MAC address|00:00:00:00:00:01|
  
**agentData**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Account ID|string|None|False|A reference to the containing account|1|
|Account Name|string|None|False|Name of the containing account|Account1|
|Active Directory|activeDirectory|None|False|Active Directory data|{}|
|Active Threats|integer|None|False|Current number of active threats|5|
|Agent Version|string|None|False|Agent version|1.0.3.4|
|Allow Remote Shell|boolean|None|False|Agent is capable and policy enabled for remote shell|True|
|Apps Vulnerability Status|string|None|False|Apps vulnerability status|patch_required|
|Cloud Providers|object|None|False|Cloud providers for this agent|{}|
|Computer Name|string|None|False|Computer name|Computer1|
|Console Migration Status|string|None|False|What step the agent is at in the process of migrating to another console, if any|N/A|
|Core Count|integer|None|False|Number of CPU cores|10|
|CPU Count|integer|None|False|Number of CPUs|4|
|CPU ID|string|None|False|CPU model|CPU A0 v1 @ 3.00GHz|
|Created At|string|None|False|Created at date|2023-01-01 00:00:00+00:00|
|Domain|string|None|False|Network domain|WORKGROUP|
|Encrypted Applications|boolean|None|False|Disk encryption status|False|
|External ID|string|None|False|External id set by customer|1|
|External IP|string|None|False|External IPv4 address|198.51.100.1|
|Firewall Enabled|boolean|None|False|Firewall enabled|True|
|Group ID|string|None|False|A reference to the containing network group|1|
|Group IP|string|None|False|IP Address subnet|198.51.100.x|
|Group Name|string|None|False|Name of the containing network group|Group1|
|Group Updated At|string|None|False|Date of when the group was last updated|2023-01-01 00:00:00+00:00|
|ID|string|None|False|Agent ID|1|
|In Remote Shell Session|boolean|None|False|Is the Agent in a remote shell session|True|
|Infected|boolean|None|False|Indicates if the Agent has active threats|False|
|Installer Type|string|None|False|Installer package type (file extension)|.msi|
|Is Active|boolean|None|False|Indicates if the agent was recently active|True|
|Is Decommissioned|boolean|None|False|Is Agent decommissioned|False|
|Is Pending Uninstall|boolean|None|False|Agent with a pending uninstall request|False|
|Is Uninstalled|boolean|None|False|Indicates if Agent was removed from the device|False|
|Is Up to Date|boolean|None|False|Indicates if the agent version is up to date|True|
|Last Active Date|string|None|False|Last active date|2023-01-01 00:00:00+00:00|
|Last IP to Management Console|string|None|False|The last IP used to connect to the Management console|198.51.100.1|
|Last Logged In User Name|string|None|False|Last logged in user name|user1|
|License Key|string|None|False|License key|BC017-06777-14871-160C4|
|Location Enabled|boolean|None|False|Location enabled|True|
|Location Type|string|None|False|Reported location type|fallback|
|Locations|[]location|None|False|A list of locations reported by the Agent|[]|
|Machine Type|string|None|False|Machine type|desktop|
|Mitigation Mode|string|None|False|Agent mitigation mode policy|protect|
|Mitigation Mode Suspicious|string|None|False|Mitigation mode policy for suspicious activity|detect|
|Model Name|string|None|False|Model name|Example Model Name|
|Network Interfaces|[]networkInterfaces|None|False|Device's network interfaces|[]|
|Network Quarantine Enabled|boolean|None|False|Network quarantine enabled|True|
|Network Status|string|None|False|Agent's network connectivity status|connected|
|Operational State|string|None|False|Agent operational state|na|
|Operational State Expiration|string|None|False|Agent operational state expiration|2023-01-01 00:00:00+00:00|
|OS Arch|string|None|False|OS Arch|64 bit|
|OS Name|string|None|False|Os name|Windows 11|
|OS Revision|string|None|False|OS revision|1234|
|OS Start Time|string|None|False|Last boot time|2023-01-01 00:00:00+00:00|
|OS Type|string|None|False|OS type|windows|
|OS Username|string|None|False|Os username|user1|
|Policy Updated At|string|None|False|Date of when the policy was last updated|2023-01-01 00:00:00+00:00|
|Ranger Status|string|None|False|Is Agent disabled as a Ranger|Enabled|
|Ranger Version|string|None|False|The version of Ranger|1.2.3.4|
|Registered At|string|None|False|Time of first registration to management console (similar to createdAt)|2023-01-01 00:00:00+00:00|
|Remote Profiling State|string|None|False|Agent remote profiling state|disabled|
|Remote Profiling State Expiration|string|None|False|Agent remote profiling state expiration in seconds|3600|
|Scan Aborted At|string|None|False|Abort time of last scan|2023-01-01 00:00:00+00:00|
|Scan Finished At|string|None|False|Finish time of last scan|2023-01-01 00:00:00+00:00|
|Scan Started At|string|None|False|Start time of last scan|2023-01-01 00:00:00+00:00|
|Scan Status|string|None|False|Last scan status|finished|
|Site ID|string|None|False|A reference to the containing site|1|
|Site Name|string|None|False|Name of the containing site|Example Site Name|
|Threat Reboot Required|boolean|None|False|Has at least one threat with at least one mitigation action that is pending reboot to succeed|False|
|Total Memory|integer|None|False|Memory size (MB)|10|
|Updated at|string|None|False|Last updated date|2023-01-01 00:00:00+00:00|
|User Actions Needed|[]string|None|False|A list of pending user actions|['example action']|
|UUID|string|None|False|Agent's universally unique identifier|b7b2d39171be4ae1af90f93d7ed20f07|
  
**queryModeInfo**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Last Activated At|string|None|False|The date when query mode was last activated|2022-07-31 08:11:01+00:00|
|Mode|string|None|False|The query mode|scalyr|
  
**queryStatus**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Progress Status|integer|None|False|Query loading status in percentage|100|
|Query Mode Info|queryModeInfo|None|False|Query mode info|{}|
|Response Error|string|None|False|Response error|Timerange start cannot be greater than timerange end|
|Response State|string|None|False|Response state|FINISHED|
  
**querySuccess**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Success|string|None|False|Request success status|FINISHED|
  
**eventData**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Agent Domain|string|None|False|Agent domain|WORKGROUP|
|Agent Group ID|string|None|False|Agent group ID|1|
|Agent ID|string|None|False|Agent ID|1|
|Agent Infected|boolean|None|False|Agent infected|False|
|Agent IP|string|None|False|Agent IP|198.51.100.1|
|Agent is Active|boolean|None|False|Agent is active|True|
|Agent is Decommissioned|boolean|None|False|Agent is decommissioned|False|
|Agent Machine Type|string|None|False|Agent machine type|desktop|
|Agent Name|string|None|False|Agent name|ExampleName1|
|Agent Network Status|string|None|False|Agent network status|connected|
|Agent OS|string|None|False|Agent Operating System|windows|
|Agent Timestamp|string|None|False|Agent timestamp|2023-01-01 00:00:00+00:00|
|Agent UUID|string|None|False|Agent UUID|b7b2d39171be4ae1af90f93d7ed20f07|
|Agent Version|string|None|False|Agent version|1.0.3.4|
|Attributes|[]object|None|False|Attributes|[]|
|Child Process Count|string|None|False|Child process count|0|
|Connection Status|string|None|False|Connection status|SUCCESS|
|Created At|string|None|False|Created at|2023-01-01 00:00:00+00:00|
|Direction|string|None|False|Direction|OUTGOING|
|DNS Response|string|None|False|DNS response|1.2.3.4;4.3.2.1;|
|Destination IP|string|None|False|Destination IP|198.51.100.1|
|Destination Port|integer|None|False|Object type|8000|
|Endpoint Machine Type|string|None|False|Endpoint machine type|desktop|
|Endpoint Name|string|None|False|Endpoint name|ExampleName1|
|Endpoint OS|string|None|False|Endpoint OS|windows|
|Event Time|string|None|False|Event time|2023-01-01 00:00:00+00:00|
|Event Type|string|None|False|Event type|Process Creation|
|File Full Name|string|None|False|File full name|C:\\PROGRAMDATA\\Microsoft\\1234|
|File ID|string|None|False|File ID|ABCD1234|
|File MD5|string|None|False|File MD5|1a79a4d60de6718e8e5b326e338ae533|
|File SHA1|string|None|False|File SHA1|c3499c2729730a7f807efb8676a92dcb6f8a3f8f|
|File SHA256|string|None|False|File SHA256|1b4f0e9851971998e732078544c96b36c3d01cedf7caa332359d6f1d83567014|
|File Size|string|None|False|File size|1234|
|File Type|string|None|False|File type|image|
|Forensic URL|string|None|False|Forensic URL|example.com|
|ID|string|None|False|ID|1|
|Indicator Category|string|None|False|Indicator category|General|
|Indicator Description|string|None|False|Indicator description|Example Description|
|Indicator Metadata|string|None|False|Indicator metadata|Example Metadata|
|Indicator Name|string|None|False|Indicator name|ProcessEnumeration|
|Logins Base Type|string|None|False|Logins base type|example|
|Logins User Name|string|None|False|Logins user name|user1|
|MD5|string|None|False|MD5|1a79a4d60de6718e8e5b326e338ae533|
|Network Method|string|None|False|Network method|GET|
|Network Source|string|None|False|Network source|Example Source|
|Network URL|string|None|False|Network URL|example.com|
|Object Type|string|None|False|Object type|file|
|Old File MD5|string|None|False|Old file MD5|1a79a4d60de6718e8e5b326e338ae533|
|Old File Name|string|None|False|Old file name|example.txt|
|Old File SHA1|string|None|False|Old file SHA1|c3499c2729730a7f807efb8676a92dcb6f8a3f8f|
|Old File SHA256|string|None|False|Old file SHA256|50d858e0985ecc7f60418aaf0cc5ab587f42c2570a884095a9e8ccacd0f6545c|
|Parent PID|string|None|False|Parent PID|1234|
|Parent Process Group ID|string|None|False|Parent process group ID|1234|
|Parent Process is Malicious|boolean|None|False|Parent process is malicious|False|
|Parent Process Name|string|None|False|Parent process name|example.exe|
|Parent Process Start Time|string|None|False|Parent process start time|2023-01-01 00:00:00+00:00|
|Parent Process Unique Key|string|None|False|Parent process unique key|ABCD1234|
|PID|string|None|False|PID|1234|
|Process CMD|string|None|False|Process CMD|C:\Windows\system32\example.exe|
|Process Display Name|string|None|False|Process display name|Example Process|
|Process Group ID|string|None|False|Process group ID|ABCD1234|
|Process Image Path|string|None|False|Process image path|C:\\test\\example.exe|
|Process Image SHA1 Hash|string|None|False|Process image SHA1 hash|c3499c2729730a7f807efb8676a92dcb6f8a3f8f|
|Process Integrity Level|string|None|False|Process integrity level|SYSTEM|
|Process is Malicious|boolean|None|False|Process is malicious|False|
|Process is Redirected Command Processor|string|None|False|Process is redirected command processor|True|
|Process is WOW64|string|None|False|Process is WOW64|True|
|Process Name|string|None|False|Process name|example.exe|
|Process Root|string|None|False|Process root|False|
|Process Session ID|string|None|False|Process session ID|0|
|Process Start Time|string|None|False|Process start time|2023-01-01 00:00:00+00:00|
|Process Sub System|string|None|False|Process sub system|SYS_WIN32|
|Process Unique Key|string|None|False|Process unique key|ABCD1234|
|Process User Name|string|None|False|Process user name|user1|
|Publisher|string|None|False|Publisher|Rapid7|
|Registry ID|string|None|False|Registry ID|ABCD1234|
|Registry Path|string|None|False|Registry path|MACHINE\\SYSTEM\\Ids\\{1234}|
|Related to Threat|string|None|False|Related to threat|False|
|RPID|string|None|False|RPID|ABCD1234|
|SHA1|string|None|False|SHA1|c3499c2729730a7f807efb8676a92dcb6f8a3f8f|
|SHA256|string|None|False|SHA256|50d858e0985ecc7f60418aaf0cc5ab587f42c2570a884095a9e8ccacd0f6545c|
|Signature Signed Invalid Reason|string|None|False|Signature signed invalid reason|Example Reason|
|Signed Status|string|None|False|Signed status|signed|
|Site Name|string|None|False|Site name|Rapid7|
|Source IP|string|None|False|Source IP|198.51.100.1|
|Source Port|integer|None|False|Source port|8000|
|Task Name|string|None|False|Task name|Example Name|
|Task Path|string|None|False|Task path|C:\\Program Files\\example.exe|
|Threat Status|string|None|False|Threat status|Example Status|
|TID|string|None|False|TID|1234|
|True Context|string|None|False|True context|ABCD1234|
|User|string|None|False|User|user1|
|Verified Status|string|None|False|Verified status|verified|


## Troubleshooting

* To convert `threat` into an array use Type Converter Plugin
* For the Trigger settings, only set the Resolved field to False if solely resolved threats should be retrieved (i.e. setting to False will not include unresolved threats)
* The Run Remote Script action may require starting a protected actions session to function properly. To do this, in the `code` input field, enter the passcode from a third-party app, such as Duo Mobile or Google Authenticator, set up in two-factor authentication. Entering the code is not required each time you run the action, because the session is valid for 30 minutes

# Version History

* 9.0.0 - Set `cloud_ready` to `true` in plugin spec | Rename URL input to Instance in connection | Code refactor
* 8.1.0 - Added New actions: Fetch file for agent ID and Run remote script. Updated description for Trigger resolved field
* 8.0.1 - Search Agents: Remove duplicate results when Case Sensitive is false
* 8.0.0 - Connection: Added Service user (API only user type) authentication | Removed Basic Authentication
* 7.1.0 - Update for Blacklist action: Fix for unblocked action | Update for Quarantine action: unification of the output data when action fails | Add troubleshooting information about use Type Converter | Mark as Benign action: update description 
* 7.0.0 - Add new actions Update Analyst Verdict and Update Incident Status | Fix Get Agent Details and Search Agents actions to handle more response scenarios | Add option to authentication with API key
* 6.2.0 - New actions Create Query, Get Query Status, Cancel Running Query, Get Events, Get Events By Type
* 6.1.0 - Add new actions Disable Agent and Enable Agent
* 6.0.0 - Add `operational_state` field to input of Get Agent Details and Search Agent actions | Update schema to return new outputs such as Active Directory, firewall, location, and quarantine information for Get Agent Details and Search Agent actions | Use API version 2.1 | Update capitalization according to style in Activities List action for Created Than Date and Less Than Dates inputs to Greater than Date and Less than Date
* 5.0.1 - Correct spelling in help.md
* 5.0.0 - Consolidate various Agent actions | Use API version 2.1 where possible | Delete obsolete Blacklist by IOC Hash and Agent Processes
* 4.1.1 - Update the Get Threat Summary action to return all threat summaries instead of 10
* 4.1.0 - Add case sensitivity option for Agent lookups
* 4.0.1 - Fix Agent Active parameter in Get Agent Details action | Update Quarantine action whitelist for IP addresses
* 4.0.0 - Update ID input for Fetch Threats File action to a string
* 3.1.0 - Add new action Fetch Threats File
* 3.0.0 - Update help.md for the Extension Library | Update title in action Blacklist by IOC Hash, Get Activities, Count Summary and Connect to Network
* 2.1.1 - Upgrade trigger Get Threats to only return threats since trigger start
* 2.1.0 - Add `agent_active` field to input in action Search Agents
* 2.0.0 - Upgrade trigger input Agent is Active to default true
* 1.4.0 - New actions Quarantine, Get Agent Details, Search Agents
* 1.3.0 - Add new action Blacklist
* 1.2.2 - Update error message in Connection
* 1.2.1 - Update to use the `komand/python-3-37-slim-plugin` Docker image to reduce plugin size
* 1.2.0 - New spec and help.md format for the Extension Library | New actions activities_list, activities_types, agents_abort_scan, agents_connect, agents_decommission, agents_disconnect, agents_fetch_logs, agents_initiate, agents_processes, agents_reload, agents_restart, agents_shutdown, agents_summary, agents_uninstall, apps_by_agent_ids, name_available
* 1.1.0 - New trigger Get Threats | New actions Mitigate Threat, Mark as Benign, Mark as Threat and Create IOC Threat
* 1.0.1 - Update to add Blacklist by IOC Hash and Blacklist by Content Hash
* 1.0.0 - Initial plugin

# Links

* [SentinelOne Product Page](https://www.sentinelone.com/)

## References

* [SentinelOne Product Page](https://www.sentinelone.com/)