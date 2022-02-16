# Description

[VMware Carbon Black EDR](https://www.carbonblack.com/products/edr/) is the most complete endpoint detection and response solution available to security teams. The InsightConnect plugin allows you to automate information collection, endpoint isolation and hash blacklisting.

This plugin utilizes the [VMware Carbon Black EDR REST API](https://developer.carbonblack.com/guide/enterprise-response/).

# Key Features

* Investigate endpoints
* Blacklist hashes
* Isolate endpoints

# Requirements

* Requires an API Key from VMware Carbon Black EDR

# Supported Product Versions

_There are no supported product versions listed._

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_key|credential_secret_key|None|True|API token found in your Carbon Black profile|None|None|
|ssl_verify|boolean|True|True|SSL certificate verification|None|None|
|url|string|https://127.0.0.1/api/bit9platform/v1|True|Carbon Black Server API URL|None|None|

Example input:

```
```

## Technical Details

### Actions

#### Uninstall sensor

This action uninstalls a sensor given a sensor ID.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|False|The sensor ID|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Whether or not the uninstall was successful|

Example output:

```
```

#### List Alerts

This action is used to list alerts with given parameters.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|False|Accepts the same data as the search box on the Process Search page|None|None|
|rows|integer|10|False|How many rows of data to return. Default is 10|None|None|
|start|integer|0|False|What row of data to start at. Default is 0|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alerts|[]alert|False|The lists of alerts|

Example output:

```

[{
  "username": "SYSTEM",
  "alert_type": "watchlist.hit.query.process",
  "sensor_criticality": 3,
  "modload_count": 0,
  "report_score": 75,
  "watchlist_id": "11",
  "sensor_id": 1,
  "feed_name": "My Watchlists",
  "created_time": "2017-09-11T17:50:03.377Z",
  "ioc_type": "query",
  "watchlist_name": "Watchlist",
  "ioc_confidence": 0.5,
  "ioc_attr": "{\"highlights\": [\"c:\\\\windows\\\\carbonblack\\\\PREPREPREcb.exePOSTPOSTPOST\", \"PREPREPREcb.exePOSTPOSTPOST\"]}",
  "alert_severity": 50.625,
  "crossproc_count": 0,
  "group": "default group",
  "hostname": "win-6epacunb1i1",
  "filemod_count": 0,
  "resolved_time": "2017-09-11T18:11:32.09Z",
  "comms_ip": "52.122.36.18",
  "netconn_count": 1,
  "interface_ip": "172.19.33.201",
  "status": "Resolved",
  "observed_hosts": {
      "numFound": 3,
      "hostCount": 1,
      "globalCount": 3,
      "hostnames": [{
          "name": "win-6epacunb1i1",
          "value": 27893
      }],
      "accurateHostCount": true,
      "processCount": 1,
      "numDocs": "84136",
      "processTotal": 1
  },
  "process_path": "c:\\windows\\carbonblack\\cb.exe",
  "process_name": "cb.exe",
  "process_unique_id": "00000001-0000-0414-01d3-20c7b4fdd3cf-015e2e1f45f7",
  "process_id": "00000001-0000-0414-01d3-20c7b4fdd3cf",
  "_version_": 1578267828122812416,
  "regmod_count": 0,
  "md5": "e472001ffe350a80f4c1f3322180ca53",
  "segment_id": 773801463,
  "total_hosts": 1,
  "feed_id": -1,
  "assigned_to": "irteam",
  "os_type": "windows",
  "childproc_count": 0,
  "unique_id": "a743ee18-ce1d-4fb3-adc5-f05a77c8996c",
  "feed_rating": 3
}]

```

#### Delete Feed

This action is used to delete a feed.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|force|boolean|None|True|Force deletion of all matches if multiple matches found|None|None|
|id|string|None|True|The ID of the feed|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Whether or not the deletion was successful|

Example output:

```

{
  "success": true
}

```

#### List Binaries

This action is used to list binaries with given parameters.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|False|Accepts the same data as the search box on the Process Search page|None|None|
|rows|integer|10|False|How many rows of data to return. Default is 10|None|None|
|start|integer|0|False|What row of data to start at. Default is 0|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|binaries|[]binary|False|The list of binaries|

Example output:

```

[{
  "host_count": 1,
  "original_filename": "bcryptprimitives.dll",
  "legal_copyright": "Microsoft Corporation. All rights reserved.",
  "digsig_result": "Signed",
  "observed_filename": [
      "C:\\Windows\\SysWOW64\\bcryptprimitives.dll"
  ],
  "product_version": "6.3.9600.18344",
  "facet_id": 737484,
  "digsig_issuer": "Microsoft Windows Production PCA 2011",
  "digsig_result_code": "0",
  "server_added_timestamp": "2017-08-30T02:37:08.977Z",
  "digsig_sign_time": "2017-08-03T10:45:00Z",
  "digsig_prog_name": "Microsoft Windows",
  "orig_mod_len": 340880,
  "is_executable_image": false,
  "is_64bit": false,
  "md5": "026B0CB0683E48164F43AADBE50E5506",
  "digsig_subject": "Microsoft Windows",
  "digsig_publisher": "Microsoft Corporation",
  "endpoint": [
      "WIN-6EPACUNB1I1|1"
  ],
  "group": [
      "Default Group"
  ],
  "event_partition_id": [
      98566909329408
  ],
  "watchlists": [{
      "wid": "7",
      "value": "2017-08-30T02:40:02.488Z"
  }],
  "file_version": "6.3.9600.18344 (winblue_ltsb.160518-1031)",
  "signed": "Signed",
  "copied_mod_len": 0,
  "company_name": "Microsoft Corporation",
  "internal_name": "bcryptprimitives.dll",
  "timestamp": "2017-08-30T02:37:08.977Z",
  "cb_version": 612,
  "os_type": "Windows",
  "file_desc": "Windows Cryptographic Primitives Library",
  "product_name": "Microsoft Windows Operating System",
  "last_seen": "2017-08-30T02:40:02.727Z"
}]

```

#### Add Feed

This action is used to add a feed.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|cert|file|None|False|Certificate file|None|None|
|enabled|boolean|None|False|Enable feed|None|None|
|feed_url|string|None|False|The URL of the feed to add|None|None|
|force|boolean|False|False|Add feed even if the feed URL is already in use|None|None|
|key|file|None|False|Key|None|None|
|password|password|None|False|Password|None|None|
|use_proxy|boolean|None|False|Whether or not to use proxy|None|None|
|username|string|None|False|Username|None|None|
|validate_server_cert|boolean|None|False|Whether or not to validate server certificate|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|integer|False|The ID of the added feed|

Example output:

```

{
  "id": 5
}

```

#### Blacklist Hash

This action is used to ban a hash given its MD5.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|md5_hash|string|None|True|An MD5 hash|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Status of request - true if successful, false otherwise|

Example output:

```

{
  "success": true
}

```

#### List Watchlists

This action is used to list all watchlists.

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|watchlists|[]watchlist|False|The list of watchlists|

Example output:

```

[{
  "last_hit_count": 8,
  "description": "",
  "search_query": "q=process_name%3Aconhost.exe",
  "from_alliance": false,
  "enabled": true,
  "search_timestamp": "2017-09-24 17:00:03.143824",
  "index_type": "events",
  "readonly": false,
  "alliance_id": null,
  "total_hits": "30368",
  "date_added": "2017-09-21 19:26:10.844270+00:00",
  "group_id": -1,
  "total_tags": "3461",
  "id": "12",
  "last_hit": "2017-09-24 17:00:03.329069+00:00",
  "name": "Conhost"
}]

```

#### Delete Watchlist

This action is used to delete a watchlist.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|force|boolean|None|True|Force deletion of all matches if multiple matches found|None|None|
|id|string|None|True|The ID of the watchlist|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Whether or not the deletion was successful|

Example output:

```

{
  "success": true
}

```

#### List Processes

This action is used to list processes with given parameters.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|query|string|None|False|Accepts the same data as the search box on the Process Search page|None|None|
|rows|integer|10|False|How many rows of data to return. Default is 10|None|None|
|start|integer|0|False|What row of data to start at. Default is 0|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|processes|[]process|False|The list of processes|

Example output:

```

[{
  "process_md5": "e0c7813a97ca7947ff5c18a8f3b61a45",
  "sensor_id": 1,
  "filtering_known_dlls": false,
  "modload_count": 0,
  "parent_unique_id": "00000001-0000-0250-01d3-202c7755d833-000000000001",
  "emet_count": 0,
  "cmdline": "C:\\Windows\\system32\\services.exe",
  "filemod_count": 0,
  "id": "00000001-0000-02a8-01d3-202c7d4bb023",
  "parent_name": "wininit.exe",
  "parent_md5": "000000000000000000000000000000",
  "group": "default group",
  "parent_id": "00000001-0000-0250-01d3-202c7755d833",
  "hostname": "win-6epacunb1i1",
  "last_update": "2017-08-29T13:07:37.238Z",
  "start": "2017-08-28T18:35:57.663Z",
  "comms_ip": 885592626,
  "regmod_count": 0,
  "interface_ip": -1407252262,
  "process_pid": 680,
  "username": "SYSTEM",
  "terminated": false,
  "process_name": "services.exe",
  "emet_config": "",
  "last_server_update": "2017-08-29T13:12:35.593Z",
  "path": "c:\\windows\\system32\\services.exe",
  "netconn_count": 0,
  "parent_pid": 592,
  "crossproc_count": 0,
  "segment_id": 1504012355063,
  "host_type": "server",
  "processblock_count": 0,
  "os_type": "windows",
  "childproc_count": 19,
  "unique_id": "00000001-0000-02a8-01d3-202c7d4bb023-015e2e1f45f7"
}]

```

#### List Sensors

This action is used to list all sensors.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|groupid|string|None|False|The sensor group ID|None|None|
|hostname|string|None|False|The sensor hostname|None|None|
|id|string|None|False|The sensor ID|None|None|
|ip|string|None|False|The sensor IP address|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|sensors|[]sensor|False|The list of sensors|

Example output:

```
[
    {
      "systemvolume_total_size": "107267223552",
      "os_environment_display_string": "Windows 7 Enterprise Service Pack 1, 64-bit",
      "clock_delta": "0",
      "supports_cblr": true,
      "sensor_uptime": "7655",
      "last_update": "2018-09-19 09:06:09.970817-07:00",
      "physical_memory_size": "1073274880",
      "build_id": 2,
      "uptime": "8757",
      "is_isolating": false,
      "computer_dns_name": "cb-sensor-win7",
      "emet_report_setting": " (GPO configured)",
      "id": 1,
      "emet_process_count": 0,
      "emet_is_gpo": false,
      "power_state": 0,
      "network_isolation_enabled": false,
      "systemvolume_free_size": "78565584896",
      "status": "Online",
      "num_eventlog_bytes": "11800",
      "sensor_health_message": "Elevated memory usage",
      "build_version_string": "006.001.002.71109",
      "computer_sid": "S-1-5-21-2519757177-4078746215-1447329238",
      "next_checkin_time": "2018-09-19 09:06:32.092306-07:00",
      "node_id": 0,
      "cookie": 1389712705,
      "emet_exploit_action": " (Locally configured)",
      "computer_name": "CB-SENSOR-WIN7",
      "license_expiration": "1990-01-01 00:00:00-08:00",
      "supports_isolation": true,
      "parity_host_id": "0",
      "supports_2nd_gen_modloads": false,
      "network_adapters": "10.4.26.148,00505694808c|",
      "sensor_health_status": 90,
      "registration_time": "2018-09-19 06:58:31.543400-07:00",
      "restart_queued": false,
      "num_storefiles_bytes": "0",
      "os_environment_id": 1,
      "shard_id": 0,
      "boot_id": "0",
      "last_checkin_time": "2018-09-19 09:06:03.096077-07:00",
      "os_type": 1,
      "group_id": 1,
      "display": true,
      "uninstall": false
    }
]
```

#### Get Binary

This action is used to retrieve a binary by its MD5 hash.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hash|string|None|True|An MD5 hash|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|binary|bytes|False|A resulting binary, Base64-encoded|

Example output:

```

{
  "binary": "b'MZ\\x00\\x00'"
}

```

#### Update Alert

This action is used to update or resolve an alert.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|id|string|None|True|Unique ID of the alert. Example: 1cb11d0d-f86b-415d-aeb3-05f085973fbb|None|None|
|status|string|Resolved|True|The status to update|['Resolved', 'Unresolved', 'In Progress', 'False Positive']|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Whether or not the update was successful|

Example output:

```

{
  "success": true
}

```

#### Add Watchlist

This action is used to add a watchlist.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|index_type|string|modules|True|Either modules or events for binary and process watchlists, respectively|['modules', 'events']|None|
|name|string|None|True|Watchlist name|None|None|
|query|string|None|True|Raw Carbon Black query that this watchlist matches|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|id|string|False|The ID of the created watchlist|

Example output:

```

{
  "id": 3
}

```

#### Isolate Sensor

This action is used to isolate a sensor from the network.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hostname|string|None|False|Hostname of the sensor to isolate|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Whether or not the isolation was successful|

Example output:

```

{
  "success": true
}

```

#### List Feeds

This action is used to list all feeds.

##### Input

_This action does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|feeds|[]feed|False|The list of feeds|

Example output:

```

[{
  "provider_url": "https://www.bit9.com/solutions/cloud-services/",
  "ssl_client_crt": null,
  "local_rating": null,
  "requires_who": null,
  "icon_small": "",
  "id": 13,
  "category": "Bit9 + Carbon Black First Party",
  "display_name": "Bit9 Software Reputation Service Trust",
  "use_proxy": null,
  "feed_url": "https://api.alliance.carbonblack.com/feed/SRSTrust",
  "username": null,
  "validate_server_cert": null,
  "ssl_client_key": null,
  "manually_added": false,
  "password": null,
  "icon": "",
  "provider_rating": 3,
  "name": "SRSTrust",
  "tech_data": "It is necessary to share MD5s of observed binaries with the Carbon Black Alliance to use this feed",
  "requires": null,
  "enabled": false,
  "summary": "The Bit9 Software Reputation Service (SRS) feed provides a level of software trustworthness",
  "requires_what": null,
  "order": 2
}]

```

#### Unisolate Sensor

This action is used to bring a sensor back into the network.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|hostname|string|None|False|Hostname of the sensor to unisolate|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|success|boolean|False|Whether or not the unisolation was successful|

Example output:

```

{
  "success": true
}

```

### Triggers

#### New Alert

This trigger is used to fire when a new alert is found.

##### Input

_This trigger does not contain any inputs._

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alert|alert|False|Carbon Black alert|

Example output:

```

{
  "username": "SYSTEM",
  "alert_type": "watchlist.hit.query.process",
  "sensor_criticality": 3,
  "modload_count": 0,
  "report_score": 75,
  "watchlist_id": "11",
  "sensor_id": 1,
  "feed_name": "My Watchlists",
  "created_time": "2017-09-11T17:50:03.377Z",
  "ioc_type": "query",
  "watchlist_name": "Watchlist",
  "ioc_confidence": 0.5,
  "ioc_attr": "{\"highlights\": [\"c:\\\\windows\\\\carbonblack\\\\PREPREPREcb.exePOSTPOSTPOST\", \"PREPREPREcb.exePOSTPOSTPOST\"]}",
  "alert_severity": 50.625,
  "crossproc_count": 0,
  "group": "default group",
  "hostname": "win-6epacunb1i1",
  "filemod_count": 0,
  "resolved_time": "2017-09-11T18:11:32.09Z",
  "comms_ip": "52.122.36.18",
  "netconn_count": 1,
  "interface_ip": "172.19.33.201",
  "status": "Resolved",
  "observed_hosts": {
      "numFound": 3,
      "hostCount": 1,
      "globalCount": 3,
      "hostnames": [{
          "name": "win-6epacunb1i1",
          "value": 27893
      }],
      "accurateHostCount": true,
      "processCount": 1,
      "numDocs": "84136",
      "processTotal": 1
  },
  "process_path": "c:\\windows\\carbonblack\\cb.exe",
  "process_name": "cb.exe",
  "process_unique_id": "00000001-0000-0414-01d3-20c7b4fdd3cf-015e2e1f45f7",
  "process_id": "00000001-0000-0414-01d3-20c7b4fdd3cf",
  "_version_": 1578267828122812416,
  "regmod_count": 0,
  "md5": "e472001ffe350a80f4c1f3322180ca53",
  "segment_id": 773801463,
  "total_hosts": 1,
  "feed_id": -1,
  "assigned_to": "irteam",
  "os_type": "windows",
  "childproc_count": 0,
  "unique_id": "a743ee18-ce1d-4fb3-adc5-f05a77c8996c",
  "feed_rating": 3
}

```

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 3.2.0 - Add uninstall sensor action | upgrade to insightconnect-plugin-runtime
* 3.1.11 - Correct spelling in help.md
* 3.1.10 - Rebrand plugin
* 3.1.9 - Pin to latest version of cbapi (1.6.2) to fix broken isolate() function
* 3.1.8 - New spec and help.md format for the Extension Library
* 3.1.7 - Fix issue where Delete Watchlist action would not run successfully
* 3.1.6 - Fix issue where output from the New Alert trigger did not match the output schema
* 3.1.5 - Update connection tests
* 3.1.4 - Update descriptions
* 3.1.3 - Pull the ConnectionCacheKey update from SDK
* 3.1.2 - Fixed List Sensors action from failing when sensor doesn't exist
* 3.1.1 - New input parameters for List Sensors action
* 3.1.0 - Added action List Sensors
* 3.0.0 - Plugin audited and various minor bugs corrected
* 2.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 1.0.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [VMware Carbon Black EDR REST API](https://developer.carbonblack.com/guide/enterprise-response/)
