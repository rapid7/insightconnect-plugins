# Description

[EchoTrail](https://www.echotrail.io/products/insights/) is a database of executable behavioral analytics, searchable
by filename or SHA256 or MD5 hash. Search our Insights database manually
for an [example](https://www.echotrail.io/insights/search/) of the type of analytics we provide.

Users can lookup filenames and hashes within their automation workflows using the EchoTrail Insights plugin for
Rapid7 InsightConnect.

This plugin utilizes the [EchoTrail API](https://api.echotrail.io).

# Key Features

* Lookup filenames
* Lookup hashes

# Requirements

* API key
* API server

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|server|string|https\://api.echotrail.io\:443|True|EchoTrail API Server|None|
|api_key|credential_secret_key|None|True|API Key|None|

## Technical Details

### Actions

#### Filename Lookup

This action is used to search for a Windows filename by name to obtain process behavioral analytics.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filename|string|None|True|Filename to lookup|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rank|number|False|Execution rank|
|host_prev|float|False|Host prevalence|
|eps|float|False|EchoTrail prevalence score|
|description|string|False|Overview description of the executable|
|intel|string|False|Additional intelligence about this executable|
|paths|[]paths|False|Common paths|
|parents|[]parents|False|Common parents|
|children|[]children|False|Common children|
|grandparents|[]grandparents|False|Common grandparents|
|hashes|[]hashes|False|Common hashes|
|network|[]network|False|Common Outgoing Network Ports|

Example output:

```
{
  "description": "The Windows Command Prompt is the built-in Windows command line interpreter.\n\nTypical Path: c:\\windows\\system32\nTypical Hash: ec436aeee41857eee5875efdb7166fe043349db5f58f3ee9fc4ff7f50005767f",
  "eps": "95.73",
  "rank": 3,
  "host_prev": "93.9",
  "intel": "Cmd.exe is likely the most abused Windows process in any kind of attack (targeted, opportunistic, IP theft, financial theft, activist focused). It garners this kind of recognition because it is the default Windows command line console and interpreter. It is difficult, or at least extremely uncommon, for an entire attack lifecycle to not depend on cmd.exe anywhere in its execution...",
  "children": [
      [
          "find.exe",
          "39.48"
      ],
      [
          "conhost.exe",
          "29.76"
      ],
      [
          "netstat.exe",
          "13.45"
      ],
      [
          "powershell.exe",
          "5.19"
      ]
  ],
  "grandparents": [
      [
          "services.exe",
          "98.63"
      ],
      [
          "shoretel.exe",
          "0.52"
      ],
      [
          "svchost.exe",
          "0.22"
      ],
      [
          "explorer.exe",
          "0.09"
      ]
  ],
  "hashes": [
      [
          "ec436aeee41857eee5875efdb7166fe043349db5f58f3ee9fc4ff7f50005767f",
          "69.98"
      ],
      [
          "9f7ebb79def0bf8cccb5a902db11746375af3fe618355fe5a69c69e4bcd50ac9",
          "13.58"
      ],
      [
          "6f88fb88ffb0f1d5465c2826e5b4f523598b1b8378377c8378ffebc171bad18b",
          "8.14"
      ],
      [
          "9a7c58bd98d70631aa1473f7b57b426db367d72429a5455b433a05ee251f3236",
          "2.55"
      ],
      [
          "e6c49f7ce186dc4c9da2c393469b070c0f1b95a01d281ae2b89538da453d1583",
          "0.16"
      ]
  ],
  "network": [
      [
          "443",
          "37.12"
      ],
      [
          "389",
          "32.12"
      ]
  ],
  "parents": [
      [
          "ltsvc.exe",
          "98.73"
      ],
      [
          "shoretel.exe",
          "0.41"
      ],
      [
          "clipboardmastertools.exe",
          "0.22"
      ],
      [
          "remsh.exe",
          "0.08"
      ],
  ],
  "paths": [
      [
          "c:\\windows\\system32",
          "99.24"
      ],
      [
          "c:\\windows\\syswow64",
          "0.76"
      ],
      [
          "c:\\windows",
          "0.00"
      ]
  ]
}
```

#### Hash Lookup

This action is used to search for a Windows executable by SHA256 or MD5 hash.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|hash|string|None|True|SHA256 or MD5 Hash Lookup|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|rank|number|False|Execution rank|
|host_prev|float|False|Host prevalance|
|eps|float|False|Prevalence score|
|description|string|False|Overview description of the executable|
|intel|string|False|Additional intelligence about this executable|
|paths|[]paths|False|Common paths|
|parents|[]parents|False|Common parents|
|children|[]children|False|Common children|
|grandparents|[]grandparents|False|Common grandparents|
|filenames|[]filenames|False|Common filenames|
|network|[]network|False|Common Outgoing Network Ports|

Example output:

```
{
  "description": "The Windows Command Prompt is the built-in Windows command line interpreter.\n\nTypical Path: c:\\windows\\system32\nTypical Filename: cmd.exe",
  "eps": "95.73",
  "rank": 3,
  "host_prev": "93.9",
  "intel": "Cmd.exe is likely the most abused Windows process in any kind of attack (targeted, opportunistic, IP theft, financial theft, activist focused). It garners this kind of recognition because it is the default Windows command line console and interpreter. It is difficult, or at least extremely uncommon, for an entire attack lifecycle to not depend on cmd.exe anywhere in its execution...",
  "children": [
      [
          "find.exe",
          "39.48"
      ],
      [
          "conhost.exe",
          "29.76"
      ],
      [
          "netstat.exe",
          "13.45"
      ],
      [
          "powershell.exe",
          "5.19"
      ]
  ],
  "filenames": [
      [
          "cmd.exe",
          "100.00"
      ]
  ],
  "grandparents": [
      [
          "services.exe",
          "98.63"
      ],
      [
          "shoretel.exe",
          "0.52"
      ],
      [
          "cbmlauncher.exe",
          "0.28"
      ],
      [
          "svchost.exe",
          "0.22"
      ]
  ],
  "network": [
      [
          "443",
          "37.12"
      ],
      [
          "389",
          "32.12"
      ]
  ],
  "parents": [
      [
          "ltsvc.exe",
          "98.73"
      ],
      [
          "shoretel.exe",
          "0.41"
      ],
      [
          "clipboardmastertools.exe",
          "0.22"
      ],
      [
          "remsh.exe",
          "0.08"
      ]
  ],
  "paths": [
      [
          "c:\\windows\\system32",
          "99.24"
      ],
      [
          "c:\\windows\\syswow64",
          "0.76"
      ],
      [
          "c:\\windows",
          "0.00"
      ]
  ]
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Initial plugin

# Links

## References

* [EchoTrail](https://www.echotrail.io)
* [EchoTrail Example](https://www.echotrail.io/insights/search/powershell.exe)
* [EchoTrail API](https://www.echotrail.io/docs/api/)

