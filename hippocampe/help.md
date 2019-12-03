# Description

[Hippocampe](https://github.com/TheHive-Project/Hippocampe) is a threat feed aggregator, which creates a threat feed memory and allows queries through a REST API or from a Web UI. Hippocampe aggregates feeds from the Internet in an Elasticsearch cluster. It has a REST API which allows to search into its 'memory'. It is based on a Python script which fetchs URLs corresponding to feeds, parses and indexes them. The Hippocampe plugin allows for advanced queries and management of your Hippocampe feeds.

This plugin utilizes the [Hippocampe API](https://github.com/TheHive-Project/Hippocampe/blob/master/docs/api_guide.md).

# Key Features

* Query Hippocampe for new threats
* Manage Hippocampe feeds

# Requirements

* A Hippocampe instance

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|Address of a working Hippocampe instance, including the port number (e.g. https://10.0.0.2:5000)|None|

## Technical Details

### Actions

#### Jobs

This action is used to return every report generated at the end of the indexing process.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|jobs|[]job|True|List of all jobs, with their reports|

Example output:

```
{
  "jobs": [
    {
      "id": "AWjj8EeTMGzve7ED9XM9",
      "startTime": "20190213T000001+0100",
      "status": "ongoing"
    }
  ]
}
```

#### Sources

This action is used to return all the known sources with their metadata.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sources|[]source|True|List of sources|

Example output:

```
{
  "sources": [
    {
      "coreIntelligence": "ip",
      "description": "GreenSnow is a team consisting of the best specialists in computer security, we harvest a large number of IPs from different computers located around the world. GreenSnow is comparable with SpamHaus.org for attacks of any kind except for spam. Our list is updated automatically and you can withdraw at any time your IP address if it has been listed.",
      "firstQuery": "20190213T000212+0100",
      "lastQuery": "20190213T000212+0100",
      "link": "http://blocklist.greensnow.co/greensnow.txt",
      "score": -100,
      "type": "greensnowIP",
      "source": "http://blocklist.greensnow.co/greensnow.txt"
    },
    {
      "coreIntelligence": "domain",
      "description": "This file contains phishing sites listed in the hpHosts database This should ONLY be downloaded by those wanting to block phishing sites and nothing else, and requires manual merging.",
      "firstQuery": "20190213T000207+0100",
      "lastQuery": "20190213T000207+0100",
      "link": "https://hosts-file.net/psh.txt",
      "score": -100,
      "type": "host_file_pshDOMAIN",
      "source": "https://hosts-file.net/psh.txt"
    },
    {
      "coreIntelligence": "url",
      "description": "OpenPhish is a repository of active phishing sites that offers free phishing intelligence feeds to its partners",
      "firstQuery": "20190213T000015+0100",
      "lastQuery": "20190213T000015+0100",
      "link": "https://openphish.com/feed.txt",
      "score": -100,
      "type": "openphishFree_feedURL",
      "source": "https://openphish.com/feed.txt"
    }
  ]
}
```

#### Monitor Sources

This action is used to return merged results from freshness, last_query, sched_report, size_by_source.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|monitor_results|[]monitor_result|True|Merged results from 4 other services for each source|

Example output:

```
{
  "monitor_results": [
    {
      "source": "http://blocklist.greensnow.co/greensnow.txt",
      "freshness": "OK",
      "lastQuery": "20190213T000212+0100",
      "schedReport": "OK",
      "size": 2740
    },
    {
      "source": "https://zeustracker.abuse.ch/blocklist.php?download=ipblocklist",
      "freshness": "OK",
      "lastQuery": "20190213T154124+0100",
      "schedReport": "OK",
      "size": 113
    }
  ]
}
```

#### Last Status

This action is used to check if the indexation went well.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|last_statuses|[]last_status|True|List of last statuses for every source (OK or NOK)|

Example output:

```
{
  "last_statuses": [
    "source": "https://palevotracker.abuse.ch/blocklists.php?download=ipblocklist",
    "lastStatus": "NOK"
  ]
}
```

#### New

This action is used to return all elements with Hippocampe/new.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|new_elements|[]new_element|True|All elements listed as Hippocampe/new|

Example output:

```
{
  "new_elements": []
}
```

#### Scheduled Report

This action is used to check if an indexation has been launched within threshold (by default 12 days, can be changed in Hippocampe/core/conf/hippo/hippo.conf).

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|launched_indexations|[]launched_indexation|True|List of launch statuses, one per source|

Example output:

```
{
  "launched_indexations": [
    {
      "schedReport": "OK",
      "source": "http://blocklist.greensnow.co/greensnow.txt"
    },
    {
      "schedReport": "OK",
      "source": "https://torstatus.blutmagie.de/ip_list_exit.php/Tor_ip_list_EXIT.csv"
    },
    {
      "schedReport": "OK",
      "source": "https://zeustracker.abuse.ch/blocklist.php?download=ipblocklist"
    }
  ]
}
```

#### Last Query

This action is used to return the last query date for every source.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|last_queries|[]last_query|True|List of last query times for every source|

Example output:

```
{
  "last_queries": [
    {
      "source": "http://blocklist.greensnow.co/greensnow.txt",
      "lastQuery": "20190213T000212+0100"
    },
    {
      "source": "http://cinsscore.com/list/ci-badguys.txt",
      "lastQuery": "20190213T000132+0100"
    },
    {
      "source": "https://zeustracker.abuse.ch/blocklist.php?download=ipblocklist",
      "lastQuery": "20190213T154124+0100"
    }
  ]
}
```

#### Distinct

This action is used to return all distinct values that match the given intelligence types.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|intelligence_types|[]string|None|True|Intelligence types, e.g. 'ip' or 'url'|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|values|object|True|Matching distinct values, one key per intelligence type|

Example output:

```
{
  "values": {
    "ip": [
      "58.210.156.132",
      "58.210.156.141",
      "223.255.6.242",
      "223.255.42.98"
    ]
  }
}
```

#### Freshness

This action is used to check if the feeds are up to date. A threshold can be defined in Hippocampe/core/conf/hippo/hippo.conf (by default 1 day).

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|freshness_statuses|[]freshness_status|True|List of all feeds with their freshness statuses|

Example output:

```
{
  "freshness_statuses": [
    {
      "freshness": "OK",
      "feed": "http://blocklist.greensnow.co/greensnow.txt"
    },
    {
      "freshness": "OK",
      "feed": "http://cinsscore.com/list/ci-badguys.txt"
    },
    {
      "freshness": "OK",
      "feed": "http://data.phishtank.com/data/online-valid.csv"
    },
    {
      "freshness": "OK",
      "feed": "https://zeustracker.abuse.ch/blocklist.php?download=ipblocklist"
    }
  ]
}
```

#### Hipposcore

This action is used to return a score for each of the given observables. The score is ranged between 0 and -100 (0 = observable unknown, -100 = super evil observable).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|observables|[]observable|None|True|Observables to score|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scores|[]score|True|List of given observables with their corresponding score|

Example output:

```
{
  "scores": [
    {
      "hipposcore": 0,
      "observable": "223.184.173.74"
    },
    {
      "hipposcore": -86.47,
      "observable": "perugemstones.com"
    }
  ]
}
```

#### Size by Source

This action is used to return the size (number of elements) for every source.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sizes|[]size|True|List of sources with corresponding sizes|

Example output:

```
{
  "sizes": [
    {
      "name": "http://blocklist.greensnow.co/greensnow.txt",
      "size": 2740
    },
    {
      "name": "http://cinsscore.com/list/ci-badguys.txt",
      "size": 15000
    },
    {
      "name": "https://torstatus.blutmagie.de/ip_list_exit.php/Tor_ip_list_EXIT.csv",
      "size": 0
    },
    {
      "name": "https://zeustracker.abuse.ch/blocklist.php?download=ipblocklist",
      "size": 113
    }
  ]
}
```

#### Hipposched

This action is used to schedule the launch of shadowbook (for automatic indexation).

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|time|string|None|True|Job frequency in crontab syntax, e.g. `* */12 * * *`|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|schedule|string|True|Newly set job frequency|

Example output:

```
{
  "schedule": "* */12 * * *"
}
```

#### Size by Type

This action is used to return the size (number of elements) for every type.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sizes|[]size|True|List of types with corresponding sizes|

Example output:

```
{
  "sizes": [
    {
      "name": "domain",
      "size": 225268
    },
    {
      "name": "ip",
      "size": 19447
    },
    {
      "name": "url",
      "size": 1736
    }
  ]
}
```

#### Shadowbook

This action is used to return the current job ID and status. If the service is indexing at the moment, this action will raise an error.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|job_status|string|True|Status of the job|
|job_id|string|True|ID of the job|

Example output:

```
{
  "source": "AVSQjAYZGLawP2pF8zFV",
  "status": "ongoing"
}
```

#### Type

This action is used to return all the known types.

##### Input

This action does not contain any inputs.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|types|[]string|True|List of types|

Example output:

```
{
  "types": [
    "domain",
    "ip",
    "url"
  ]
}
```

#### More

This action is used to return intelligence about given observables.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|observables|[]observable|None|True|Observables to get intelligence about|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|[]intelligence|True|List of results, one per observable|

Example output:

```
{
  "results": [
    {
      "observable": "223.184.173.74",
      "records": []
    },
    {
      "observable": "perugemstones.com",
      "records": [
        {
          "domain": "perugemstones.com",
          "extra": [
            "20171117",
            "20130417"
          ],
          "firstAppearance": "20190213T000058+0100",
          "hipposcore": -86.47,
          "idSource": "AWjj8JodMGzve7ED9ZUM",
          "lastAppearance": "20190213T000058+0100",
          "nextvalidation": "",
          "original_reference-why_it_was_listed": "safebrowsing.clients.google.com",
          "source": "http://mirror1.malwaredomains.com/files/domains.txt",
          "type": "attackpage"
        }
      ]
    }
  ]
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
* 1.0.0 - Initial plugin

# Links

## References

* [Hippocampe](https://github.com/TheHive-Project/Hippocampe)
* [Hippocampe API](https://github.com/TheHive-Project/Hippocampe/blob/master/docs/api_guide.md)

