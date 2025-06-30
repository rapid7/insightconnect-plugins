# Description

[VMware Carbon Black EDR](https://www.carbonblack.com/products/edr/) is the most complete endpoint detection and response solution available to security teams. The InsightConnect plugin allows you to automate information collection, endpoint isolation and hash blacklisting. This plugin utilizes the [VMware Carbon Black EDR REST API](https://developer.carbonblack.com/guide/enterprise-response/)

# Key Features

* Investigate endpoints
* Blacklist hashes
* Isolate endpoints
* Uninstall endpoints

# Requirements

* Requires an API Key from VMware Carbon Black EDR

# Supported Product Versions

* 6.0-6.2x Carbon Black EDR API

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_key|credential_secret_key|None|True|API token found in your Carbon Black profile|None|{"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"}|None|None|
|ssl_verify|boolean|True|True|SSL certificate verification|None|True|None|None|
|url|string|https://127.0.0.1/api/bit9platform/v1|True|Carbon Black Server API URL|None|https://127.0.0.1/api/bit9platform/v1|None|None|

Example input:

```
{
  "api_key": {
    "secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"
  },
  "ssl_verify": true,
  "url": "https://127.0.0.1/api/bit9platform/v1"
}
```

## Technical Details

### Actions


#### Add Feed

This action is used to adds a feed

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|cert|file|None|False|Certificate file|None|{"filename": "name", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="}|None|None|
|enabled|boolean|None|False|Enable feed|None|True|None|None|
|feed_url|string|None|False|The URL of the feed to add|None|https://example.com|None|None|
|force|boolean|False|False|Add feed even if the feed URL is already in use|None|False|None|None|
|key|file|None|False|Key|None|{"filename": "<name>", "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg=="}|None|None|
|password|password|None|False|Password|None|mypassword|None|None|
|use_proxy|boolean|None|False|Whether or not to use proxy|None|True|None|None|
|username|string|None|False|Username|None|user1|None|None|
|validate_server_cert|boolean|None|False|Whether or not to validate server certificate|None|True|None|None|
  
Example input:

```
{
  "cert": {
    "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
    "filename": "name"
  },
  "enabled": true,
  "feed_url": "https://example.com",
  "force": false,
  "key": {
    "content": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
    "filename": "<name>"
  },
  "password": "mypassword",
  "use_proxy": true,
  "username": "user1",
  "validate_server_cert": true
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|integer|False|The ID of the added feed|5|
  
Example output:

```
{
  "id": 5
}
```

#### Add Watchlist

This action is used to adds a watchlist

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|index_type|string|modules|True|Either modules or events for binary and process watchlists, respectively|["modules", "events", ""]|modules|None|None|
|name|string|None|True|Watchlist name|None|examplename|None|None|
|query|string|None|True|Raw Carbon Black query that this watchlist matches|None|test|None|None|
  
Example input:

```
{
  "index_type": "modules",
  "name": "examplename",
  "query": "test"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|id|string|False|The ID of the created watchlist|3|
  
Example output:

```
{
  "id": 3
}
```

#### Blacklist Hash

This action is used to ban a hash given its MD5

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|md5_hash|string|None|True|An MD5 hash|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
  
Example input:

```
{
  "md5_hash": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Status of request - true if successful, false otherwise|True|
  
Example output:

```
{
  "success": true
}
```

#### Delete Feed

This action is used to deletes a feed

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|force|boolean|None|True|Force deletion of all matches if multiple matches found|None|True|None|None|
|id|string|None|True|The ID of the feed|None|example_protection|None|None|
  
Example input:

```
{
  "force": true,
  "id": "example_protection"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Whether or not the deletion was successful|False|
  
Example output:

```
{
  "success": false
}
```

#### Delete Watchlist

This action is used to deletes a watchlist

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|force|boolean|None|True|Force deletion of all matches if multiple matches found|None|False|None|None|
|id|string|None|True|The ID of the watchlist|None|1234|None|None|
  
Example input:

```
{
  "force": false,
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Whether or not the deletion was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Get Binary

This action is used to retrieve a binary by its MD5 Hash

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|hash|string|None|True|An MD5 hash|None|9de5069c5afe602b2ea0a04b66beb2c0|None|None|
  
Example input:

```
{
  "hash": "9de5069c5afe602b2ea0a04b66beb2c0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|binary|bytes|False|A resulting binary, Base64-encoded|b'MZ\x00\x00'|
  
Example output:

```
{
  "binary": "b'MZ\\x00\\x00'"
}
```

#### Isolate Sensor

This action is used to isolates a sensor from the network

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|hostname|string|None|False|Hostname of the sensor to isolate|None|cb-response-example|None|None|
  
Example input:

```
{
  "hostname": "cb-response-example"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Whether or not the isolation was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### List Alerts

This action is used to list Carbon Black alerts with given parameters

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|False|Accepts the same data as the search box on the Process Search page|None|domain:www.carbonblack.com|None|None|
|rows|integer|10|False|How many rows of data to return. Default is 10|None|10|None|None|
|start|integer|0|False|What row of data to start at. Default is 0|None|0|None|None|
  
Example input:

```
{
  "query": "domain:www.carbonblack.com",
  "rows": 10,
  "start": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alerts|[]alert|False|The lists of alerts|[{ "username": "SYSTEM", "alert_type": "watchlist.hit.query.process", "sensor_criticality": 3, "modload_count": 0, "report_score": 75, "watchlist_id": "11", "sensor_id": 1, "feed_name": "My Watchlists", "created_time": "2017-09-11T17:50:03.377Z", "ioc_type": "query", "watchlist_name": "Watchlist", "ioc_confidence": 0.5, "ioc_attr": "{\"highlights\": [\"c:\\\\windows\\\\carbonblack\\\\PREPREPREcb.exePOSTPOSTPOST\", \"PREPREPREcb.exePOSTPOSTPOST\"]}", "alert_severity": 50.625, "crossproc_count": 0, "group": "default group", "hostname": "win-6epacunb1i1", "filemod_count": 0, "resolved_time": "2017-09-11T18:11:32.09Z", "comms_ip": "52.122.36.18", "netconn_count": 1, "interface_ip": "192.168.0.0", "status": "Resolved", "observed_hosts": { "numFound": 3, "hostCount": 1, "globalCount": 3, "hostnames": [{ "name": "test", "value": 27893 }], "accurateHostCount": true, "processCount": 1, "numDocs": "84136", "processTotal": 1 }, "process_path": "c:\\windows\\carbonblack\\cb.exe", "process_name": "cb.exe", "process_unique_id": "00000001-0000-0414-01d3-dhdhd22-00000", "process_id": "00000001-0000-0414-01d3-dshdh33", "_version_": 171716252222, "regmod_count": 0, "md5": "e486696996948733u333", "segment_id": 7721463, "total_hosts": 1, "feed_id": -1, "assigned_to": "irteam", "os_type": "windows", "childproc_count": 0, "unique_id": "a7772-c8829292-4fb3-abbabhhs-f05a77c8996c", "feed_rating": 3 }]|
  
Example output:

```
{
  "alerts": [
    {
      "_version_": 171716252222,
      "alert_severity": 50.625,
      "alert_type": "watchlist.hit.query.process",
      "assigned_to": "irteam",
      "childproc_count": 0,
      "comms_ip": "52.122.36.18",
      "created_time": "2017-09-11T17:50:03.377Z",
      "crossproc_count": 0,
      "feed_id": -1,
      "feed_name": "My Watchlists",
      "feed_rating": 3,
      "filemod_count": 0,
      "group": "default group",
      "hostname": "win-6epacunb1i1",
      "interface_ip": "192.168.0.0",
      "ioc_attr": "{\"highlights\": [\"c:\\\\windows\\\\carbonblack\\\\PREPREPREcb.exePOSTPOSTPOST\", \"PREPREPREcb.exePOSTPOSTPOST\"]}",
      "ioc_confidence": 0.5,
      "ioc_type": "query",
      "md5": "e486696996948733u333",
      "modload_count": 0,
      "netconn_count": 1,
      "observed_hosts": {
        "accurateHostCount": true,
        "globalCount": 3,
        "hostCount": 1,
        "hostnames": [
          {
            "name": "test",
            "value": 27893
          }
        ],
        "numDocs": "84136",
        "numFound": 3,
        "processCount": 1,
        "processTotal": 1
      },
      "os_type": "windows",
      "process_id": "00000001-0000-0414-01d3-dshdh33",
      "process_name": "cb.exe",
      "process_path": "c:\\windows\\carbonblack\\cb.exe",
      "process_unique_id": "00000001-0000-0414-01d3-dhdhd22-00000",
      "regmod_count": 0,
      "report_score": 75,
      "resolved_time": "2017-09-11T18:11:32.09Z",
      "segment_id": 7721463,
      "sensor_criticality": 3,
      "sensor_id": 1,
      "status": "Resolved",
      "total_hosts": 1,
      "unique_id": "a7772-c8829292-4fb3-abbabhhs-f05a77c8996c",
      "username": "SYSTEM",
      "watchlist_id": "11",
      "watchlist_name": "Watchlist"
    }
  ]
}
```

#### List Binaries

This action is used to list Carbon Black binaries with given parameters

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|False|Accepts the same data as the search box on the Process Search page|None|domain:www.carbonblack.com|None|None|
|rows|integer|10|False|How many rows of data to return. Default is 10|None|10|None|None|
|start|integer|0|False|What row of data to start at. Default is 0|None|0|None|None|
  
Example input:

```
{
  "query": "domain:www.carbonblack.com",
  "rows": 10,
  "start": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|binaries|[]binary|False|The list of binaries|[{ "host_count": 1, "original_filename": "bcryptprimitives.dll", "legal_copyright": "Microsoft Corporation. All rights reserved.", "digsig_result": "Signed", "observed_filename": [ "C:\\Windows\\SysWOW64\\bcryptprimitives.dll" ], "product_version": "6.3.9600.18344", "facet_id": 737484, "digsig_issuer": "Microsoft Windows Production PCA 2011", "digsig_result_code": "0", "server_added_timestamp": "2017-08-30T02:37:08.977Z", "digsig_sign_time": "2017-08-03T10:45:00Z", "digsig_prog_name": "Microsoft Windows", "orig_mod_len": 340880, "is_executable_image": false, "is_64bit": false, "md5": "0DHDB367SXX3", "digsig_subject": "Microsoft Windows", "digsig_publisher": "Microsoft Corporation", "endpoint": [ "WIN-6EPACUNB1I1|1" ], "group": [ "Default Group" ], "event_partition_id": [ 98566909329408 ], "watchlists": [{ "wid": "7", "value": "2017-08-30T02:40:02.488Z" }], "file_version": "6.3.9600.18344 (winblue_ltsb.160518-1031)", "signed": "Signed", "copied_mod_len": 0, "company_name": "Microsoft Corporation", "internal_name": "bcryptprimitives.dll", "timestamp": "2017-08-30T02:37:08.977Z", "cb_version": 612, "os_type": "Windows", "file_desc": "Windows Cryptographic Primitives Library", "product_name": "Microsoft Windows Operating System", "last_seen": "2017-08-30T02:40:02.727Z" }]|
  
Example output:

```
{
  "binaries": [
    {
      "cb_version": 612,
      "company_name": "Microsoft Corporation",
      "copied_mod_len": 0,
      "digsig_issuer": "Microsoft Windows Production PCA 2011",
      "digsig_prog_name": "Microsoft Windows",
      "digsig_publisher": "Microsoft Corporation",
      "digsig_result": "Signed",
      "digsig_result_code": "0",
      "digsig_sign_time": "2017-08-03T10:45:00Z",
      "digsig_subject": "Microsoft Windows",
      "endpoint": [
        "WIN-6EPACUNB1I1|1"
      ],
      "event_partition_id": [
        98566909329408
      ],
      "facet_id": 737484,
      "file_desc": "Windows Cryptographic Primitives Library",
      "file_version": "6.3.9600.18344 (winblue_ltsb.160518-1031)",
      "group": [
        "Default Group"
      ],
      "host_count": 1,
      "internal_name": "bcryptprimitives.dll",
      "is_64bit": false,
      "is_executable_image": false,
      "last_seen": "2017-08-30T02:40:02.727Z",
      "legal_copyright": "Microsoft Corporation. All rights reserved.",
      "md5": "0DHDB367SXX3",
      "observed_filename": [
        "C:\\Windows\\SysWOW64\\bcryptprimitives.dll"
      ],
      "orig_mod_len": 340880,
      "original_filename": "bcryptprimitives.dll",
      "os_type": "Windows",
      "product_name": "Microsoft Windows Operating System",
      "product_version": "6.3.9600.18344",
      "server_added_timestamp": "2017-08-30T02:37:08.977Z",
      "signed": "Signed",
      "timestamp": "2017-08-30T02:37:08.977Z",
      "watchlists": [
        {
          "value": "2017-08-30T02:40:02.488Z",
          "wid": "7"
        }
      ]
    }
  ]
}
```

#### List Feeds

This action is used to list all feeds

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|feeds|[]feed|False|The list of feeds|[{ "provider_url": "https://www.bit9.com/solutions/cloud-services/", "ssl_client_crt": null, "local_rating": null, "requires_who": null, "icon_small": "", "id": 132, "category": "Bit9 + Carbon Black First Party", "display_name": "Bit9 Software Reputation Service Trust", "use_proxy": null, "feed_url": "https://api.alliance.carbonblack.com/feed/SRSTrust", "username": null, "validate_server_cert": null, "ssl_client_key": null, "manually_added": false, "password": null, "icon": "", "provider_rating": 3, "name": "SRSTrust", "tech_data": "It is necessary to share MD5s of observed binaries with the Carbon Black Alliance to use this feed", "requires": null, "enabled": false, "summary": "The Bit9 Software Reputation Service (SRS) feed provides a level of software trustworthness", "requires_what": null, "order": 2 }]|
  
Example output:

```
{
  "feeds": [
    {
      "category": "Bit9 + Carbon Black First Party",
      "display_name": "Bit9 Software Reputation Service Trust",
      "enabled": false,
      "feed_url": "https://api.alliance.carbonblack.com/feed/SRSTrust",
      "icon": "",
      "icon_small": "",
      "id": 132,
      "local_rating": null,
      "manually_added": false,
      "name": "SRSTrust",
      "order": 2,
      "password": null,
      "provider_rating": 3,
      "provider_url": "https://www.bit9.com/solutions/cloud-services/",
      "requires": null,
      "requires_what": null,
      "requires_who": null,
      "ssl_client_crt": null,
      "ssl_client_key": null,
      "summary": "The Bit9 Software Reputation Service (SRS) feed provides a level of software trustworthness",
      "tech_data": "It is necessary to share MD5s of observed binaries with the Carbon Black Alliance to use this feed",
      "use_proxy": null,
      "username": null,
      "validate_server_cert": null
    }
  ]
}
```

#### List Processes

This action is used to list Carbon Black processes with given parameters

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|query|string|None|False|Accepts the same data as the search box on the Process Search page|None|domain:www.carbonblack.com|None|None|
|rows|integer|10|False|How many rows of data to return. Default is 10|None|10|None|None|
|start|integer|0|False|What row of data to start at. Default is 0|None|0|None|None|
  
Example input:

```
{
  "query": "domain:www.carbonblack.com",
  "rows": 10,
  "start": 0
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|processes|[]process|False|The list of processes|[{ "process_md5": "e0c7813a97ca7947ff5c18a8f3b61a45", "sensor_id": 1, "filtering_known_dlls": false, "modload_count": 0, "parent_unique_id": "00000001-0000-0250-01d3-202c7755d833-000000000001", "emet_count": 0, "cmdline": "C:\\Windows\\system32\\services.exe", "filemod_count": 0, "id": "00000001-0000-02a8-01d3-202c7d4bb023", "parent_name": "wininit.exe", "parent_md5": "000000000000000000000000000000", "group": "default group", "parent_id": "00000001-0000-0250-01d3-202c7755d833", "hostname": "win-6epacunb1i1", "last_update": "2017-08-29T13:07:37.238Z", "start": "2017-08-28T18:35:57.663Z", "comms_ip": 885592626, "regmod_count": 0, "interface_ip": -1407252262, "process_pid": 680, "username": "SYSTEM", "terminated": false, "process_name": "services.exe", "emet_config": "", "last_server_update": "2017-08-29T13:12:35.593Z", "path": "c:\\windows\\system32\\services.exe", "netconn_count": 0, "parent_pid": 592, "crossproc_count": 0, "segment_id": 1504012355063, "host_type": "server", "processblock_count": 0, "os_type": "windows", "childproc_count": 19, "unique_id": "00000001-0000-02a8-01d3-202c7d4bb023-015e2e1f45f7" }] |
  
Example output:

```
{
  "processes": [
    {
      "childproc_count": 19,
      "cmdline": "C:\\Windows\\system32\\services.exe",
      "comms_ip": 885592626,
      "crossproc_count": 0,
      "emet_config": "",
      "emet_count": 0,
      "filemod_count": 0,
      "filtering_known_dlls": false,
      "group": "default group",
      "host_type": "server",
      "hostname": "win-6epacunb1i1",
      "id": "00000001-0000-02a8-01d3-202c7d4bb023",
      "interface_ip": -1407252262,
      "last_server_update": "2017-08-29T13:12:35.593Z",
      "last_update": "2017-08-29T13:07:37.238Z",
      "modload_count": 0,
      "netconn_count": 0,
      "os_type": "windows",
      "parent_id": "00000001-0000-0250-01d3-202c7755d833",
      "parent_md5": "000000000000000000000000000000",
      "parent_name": "wininit.exe",
      "parent_pid": 592,
      "parent_unique_id": "00000001-0000-0250-01d3-202c7755d833-000000000001",
      "path": "c:\\windows\\system32\\services.exe",
      "process_md5": "e0c7813a97ca7947ff5c18a8f3b61a45",
      "process_name": "services.exe",
      "process_pid": 680,
      "processblock_count": 0,
      "regmod_count": 0,
      "segment_id": 1504012355063,
      "sensor_id": 1,
      "start": "2017-08-28T18:35:57.663Z",
      "terminated": false,
      "unique_id": "00000001-0000-02a8-01d3-202c7d4bb023-015e2e1f45f7",
      "username": "SYSTEM"
    }
  ]
}
```

#### List Sensors

This action is used to list all sensors

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|groupid|string|None|False|The sensor group ID|None|50|None|None|
|hostname|string|None|False|The sensor hostname|None|cb-response-example|None|None|
|id|string|None|False|The sensor ID|None|1234|None|None|
|ip|string|None|False|The sensor IP address|None|192.0.2.0|None|None|
  
Example input:

```
{
  "groupid": 50,
  "hostname": "cb-response-example",
  "id": 1234,
  "ip": "192.0.2.0"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|sensors|[]sensor|False|The list of sensors|[ { "systemvolume_total_size": "107267223552", "os_environment_display_string": "Windows 7 Enterprise Service Pack 1, 64-bit", "clock_delta": "0", "supports_cblr": true, "sensor_uptime": "7655", "last_update": "2018-09-19 09:06:09.970817-07:00", "physical_memory_size": "1073274880", "build_id": 2, "uptime": "8757", "is_isolating": false, "computer_dns_name": "cb-sensor-win7", "emet_report_setting": " (GPO configured)", "id": 1, "emet_process_count": 0, "emet_is_gpo": false, "power_state": 0, "network_isolation_enabled": false, "systemvolume_free_size": "78565584896", "status": "Online", "num_eventlog_bytes": "11800", "sensor_health_message": "Elevated memory usage", "build_version_string": "006.001.002.71109", "computer_sid": "S-1-5-21-2519757177-4078746215-1447329238", "next_checkin_time": "2018-09-19 09:06:32.092306-07:00", "node_id": 0, "cookie": 1389712705, "emet_exploit_action": " (Locally configured)", "computer_name": "CB-SENSOR-WIN7", "license_expiration": "1990-01-01 00:00:00-08:00", "supports_isolation": true, "parity_host_id": "0", "supports_2nd_gen_modloads": false, "network_adapters": "10.4.26.148,00505694808c|", "sensor_health_status": 90, "registration_time": "2018-09-19 06:58:31.543400-07:00", "restart_queued": false, "num_storefiles_bytes": "0", "os_environment_id": 1, "shard_id": 0, "boot_id": "0", "last_checkin_time": "2018-09-19 09:06:03.096077-07:00", "os_type": 1, "group_id": 1, "display": true, "uninstall": false } ]|
  
Example output:

```
{
  "sensors": [
    {
      "boot_id": "0",
      "build_id": 2,
      "build_version_string": "006.001.002.71109",
      "clock_delta": "0",
      "computer_dns_name": "cb-sensor-win7",
      "computer_name": "CB-SENSOR-WIN7",
      "computer_sid": "S-1-5-21-2519757177-4078746215-1447329238",
      "cookie": 1389712705,
      "display": true,
      "emet_exploit_action": " (Locally configured)",
      "emet_is_gpo": false,
      "emet_process_count": 0,
      "emet_report_setting": " (GPO configured)",
      "group_id": 1,
      "id": 1,
      "is_isolating": false,
      "last_checkin_time": "2018-09-19 09:06:03.096077-07:00",
      "last_update": "2018-09-19 09:06:09.970817-07:00",
      "license_expiration": "1990-01-01 00:00:00-08:00",
      "network_adapters": "10.4.26.148,00505694808c|",
      "network_isolation_enabled": false,
      "next_checkin_time": "2018-09-19 09:06:32.092306-07:00",
      "node_id": 0,
      "num_eventlog_bytes": "11800",
      "num_storefiles_bytes": "0",
      "os_environment_display_string": "Windows 7 Enterprise Service Pack 1, 64-bit",
      "os_environment_id": 1,
      "os_type": 1,
      "parity_host_id": "0",
      "physical_memory_size": "1073274880",
      "power_state": 0,
      "registration_time": "2018-09-19 06:58:31.543400-07:00",
      "restart_queued": false,
      "sensor_health_message": "Elevated memory usage",
      "sensor_health_status": 90,
      "sensor_uptime": "7655",
      "shard_id": 0,
      "status": "Online",
      "supports_2nd_gen_modloads": false,
      "supports_cblr": true,
      "supports_isolation": true,
      "systemvolume_free_size": "78565584896",
      "systemvolume_total_size": "107267223552",
      "uninstall": false,
      "uptime": "8757"
    }
  ]
}
```

#### List Watchlists

This action is used to list all watchlists

##### Input
  
*This action does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|watchlists|[]watchlist|False|The list of watchlists|[{ "last_hit_count": 8, "description": "", "search_query": "q=process_name%3Aconhost.exe", "from_alliance": false, "enabled": true, "search_timestamp": "2017-09-24 17:00:03.143824", "index_type": "events", "readonly": false, "alliance_id": null, "total_hits": "30368", "date_added": "2017-09-21 19:26:10.844270+00:00", "group_id": -1, "total_tags": "34261", "id": "123", "last_hit": "2017-09-24 17:00:03.329069+00:00", "name": "Conhost" }]|
  
Example output:

```
{
  "watchlists": [
    {
      "alliance_id": null,
      "date_added": "2017-09-21 19:26:10.844270+00:00",
      "description": "",
      "enabled": true,
      "from_alliance": false,
      "group_id": -1,
      "id": "123",
      "index_type": "events",
      "last_hit": "2017-09-24 17:00:03.329069+00:00",
      "last_hit_count": 8,
      "name": "Conhost",
      "readonly": false,
      "search_query": "q=process_name%3Aconhost.exe",
      "search_timestamp": "2017-09-24 17:00:03.143824",
      "total_hits": "30368",
      "total_tags": "34261"
    }
  ]
}
```

#### Uninstall Sensor

This action is used to uninstalls a sensor given a sensor ID

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|False|The sensor ID|None|1234|None|None|
  
Example input:

```
{
  "id": 1234
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Whether or not the uninstall was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Unisolate Sensor

This action is used to brings a sensor back into the network

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|hostname|string|None|False|Hostname of the sensor to unisolate|None|cb-response-example|None|None|
  
Example input:

```
{
  "hostname": "cb-response-example"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Whether or not the unisolation was successful|True|
  
Example output:

```
{
  "success": true
}
```

#### Update Alert

This action is used to updates or Resolves an Alert in Carbon Black

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|id|string|None|True|Unique ID of the alert. |None|1cb11d0d-f86b-415d-aeb3-05f085973fbb|None|None|
|status|string|Resolved|True|The status to update|["Resolved", "Unresolved", "In Progress", "False Positive", ""]|Resolved|None|None|
  
Example input:

```
{
  "id": "1cb11d0d-f86b-415d-aeb3-05f085973fbb",
  "status": "Resolved"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|success|boolean|False|Whether or not the update was successful|True|
  
Example output:

```
{
  "success": true
}
```
### Triggers


#### New Alert

This trigger is used to fires when a new alert is found

##### Input
  
*This trigger does not contain any inputs.*

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|alert|alert|False|Carbon Black alert|{ "username": "SYSTEM", "alert_type": "watchlist.hit.query.process", "sensor_criticality": 3, "modload_count": 0, "report_score": 75, "watchlist_id": "11", "sensor_id": 1, "feed_name": "My Watchlists", "created_time": "2017-09-11T17:50:03.377Z", "ioc_type": "query", "watchlist_name": "Watchlist", "ioc_confidence": 0.5, "ioc_attr": "{\"highlights\": [\"c:\\\\windows\\\\carbonblack\\\\PREPREPREcb.exePOSTPOSTPOST\", \"PREPREPREcb.exePOSTPOSTPOST\"]}", "alert_severity": 50.625, "crossproc_count": 0, "group": "default group", "hostname": "win-6epacunb1i1", "filemod_count": 0, "resolved_time": "2017-09-11T18:11:32.09Z", "comms_ip": "52.122.36.18", "netconn_count": 1, "interface_ip": "172.19.33.201", "status": "Resolved", "observed_hosts": { "numFound": 3, "hostCount": 1, "globalCount": 3, "hostnames": [{ "name": "win-6epacunb1i1", "value": 27893 }], "accurateHostCount": true, "processCount": 1, "numDocs": "84136", "processTotal": 1 }, "process_path": "c:\\windows\\carbonblack\\cb.exe", "process_name": "cb.exe", "process_unique_id": "00000001-0000-0414-01d3-20c7b4fdd3cf-015e2e1f45f7", "process_id": "00000001-0000-0414-01d3-20c7b4fdd3cf", "_version_": 1578267828122812416, "regmod_count": 0, "md5": "e472001ffe350a80f4c1f3322180ca53", "segment_id": 773801463, "total_hosts": 1, "feed_id": -1, "assigned_to": "irteam", "os_type": "windows", "childproc_count": 0, "unique_id": "a743ee18-ce1d-4fb3-adc5-f05a77c8996c", "feed_rating": 3 }|
  
Example output:

```
{
  "alert": {
    "_version_": 1578267828122812416,
    "alert_severity": 50.625,
    "alert_type": "watchlist.hit.query.process",
    "assigned_to": "irteam",
    "childproc_count": 0,
    "comms_ip": "52.122.36.18",
    "created_time": "2017-09-11T17:50:03.377Z",
    "crossproc_count": 0,
    "feed_id": -1,
    "feed_name": "My Watchlists",
    "feed_rating": 3,
    "filemod_count": 0,
    "group": "default group",
    "hostname": "win-6epacunb1i1",
    "interface_ip": "172.19.33.201",
    "ioc_attr": "{\"highlights\": [\"c:\\\\windows\\\\carbonblack\\\\PREPREPREcb.exePOSTPOSTPOST\", \"PREPREPREcb.exePOSTPOSTPOST\"]}",
    "ioc_confidence": 0.5,
    "ioc_type": "query",
    "md5": "e472001ffe350a80f4c1f3322180ca53",
    "modload_count": 0,
    "netconn_count": 1,
    "observed_hosts": {
      "accurateHostCount": true,
      "globalCount": 3,
      "hostCount": 1,
      "hostnames": [
        {
          "name": "win-6epacunb1i1",
          "value": 27893
        }
      ],
      "numDocs": "84136",
      "numFound": 3,
      "processCount": 1,
      "processTotal": 1
    },
    "os_type": "windows",
    "process_id": "00000001-0000-0414-01d3-20c7b4fdd3cf",
    "process_name": "cb.exe",
    "process_path": "c:\\windows\\carbonblack\\cb.exe",
    "process_unique_id": "00000001-0000-0414-01d3-20c7b4fdd3cf-015e2e1f45f7",
    "regmod_count": 0,
    "report_score": 75,
    "resolved_time": "2017-09-11T18:11:32.09Z",
    "segment_id": 773801463,
    "sensor_criticality": 3,
    "sensor_id": 1,
    "status": "Resolved",
    "total_hosts": 1,
    "unique_id": "a743ee18-ce1d-4fb3-adc5-f05a77c8996c",
    "username": "SYSTEM",
    "watchlist_id": "11",
    "watchlist_name": "Watchlist"
  }
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**alert**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Severity|number|None|False|None|None|
|Type|string|None|False|None|None|
|Created Time|date|None|False|None|None|
|Feed ID|integer|None|False|None|None|
|Feed Name|string|None|False|None|None|
|Feed Rating|number|None|False|None|None|
|Hostname|string|None|False|None|None|
|IOC Attributes|string|None|False|None|None|
|IOC Confidence|number|None|False|None|None|
|MD5|string|None|False|None|None|
|OS Type|string|None|False|None|None|
|Report Score|integer|None|False|None|None|
|Sensor Criticality|number|None|False|None|None|
|Sensor ID|integer|None|False|None|None|
|Status|string|None|False|None|None|
|Unique ID|string|None|False|None|None|
  
**process**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Binaries|object|None|False|None|None|
|Childproc Count|integer|None|False|None|None|
|CMD Line|string|None|False|None|None|
|Comms IP|integer|None|False|None|None|
|Crossproc Count|integer|None|False|None|None|
|EMET Count|integer|None|False|None|None|
|Filemod Complete|[]string|None|False|None|None|
|Filemod Count|integer|None|False|None|None|
|Filtering Known Downloads|boolean|None|False|None|None|
|Group|string|None|False|None|None|
|Host Type|string|None|False|None|None|
|Hostname|string|None|False|None|None|
|ID|string|None|False|None|None|
|Interface IP|integer|None|False|None|None|
|Last Update|string|None|False|None|None|
|Mod Load|integer|None|False|None|None|
|Netconn Count|integer|None|False|None|None|
|OS Type|string|None|False|None|None|
|Parent Name|string|None|False|None|None|
|Parent PID|integer|None|False|None|None|
|Parent Unique ID|string|None|False|None|None|
|Path|string|None|False|None|None|
|MD5|string|None|False|None|None|
|Name|string|None|False|None|None|
|PID|integer|None|False|None|None|
|Process Block Count|integer|None|False|None|None|
|Regmod Count|integer|None|False|None|None|
|Segment ID|integer|None|False|None|None|
|Sensor ID|integer|None|False|None|None|
|Start|string|None|False|None|None|
|Terminated|boolean|None|False|None|None|
|UID|string|None|False|None|None|
|Unique ID|string|None|False|None|None|
|Username|string|None|False|None|None|
  
**binary**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alliance Score Virustotal|string|None|False|If enabled and the hit count is greater than one, the number of [VirusTotal](http://virustotal.com) hits for this MD5|None|
|Carbon Black Version|integer|None|False|None|None|
|Company Name|string|None|False|If present, company name from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)|None|
|Copied Mod Length|integer|None|False|Bytes copied from remote host. If file is greater than 25MB this will be less than orig_mod_len|None|
|Digital Signature Issuer|string|None|False|If signed and present, the issuer name|None|
|Digital Signature Program Name|string|None|False|If signed and present, the program name|None|
|Digital Signature Publisher|string|None|False|If signed and present, the publisher name|None|
|Digital Signature Result|string|None|False|Digital signature status; One of Signed, Unsigned, Expired, Bad Signature, Invalid Signature, Invalid Chain, Untrusted Root, Explicit Distrust|None|
|Digital Signature Result Code|string|None|False|HRESULT_FROM_WIN32 for the result of the digital signature operation via [WinVerifyTrust](http://msdn.microsoft.com/en-us/library/windows/desktop/aa388208)|None|
|Digital Signature Times|string|None|False|If signed, the timestamp of the signature in GMT|None|
|Digital Signature Subject|string|None|False|If signed and present, the subject|None|
|Endpoint|[]string|None|False|None|None|
|File Description|string|None|False|If present, file description from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)|None|
|File Version|string|None|False|If present, file version from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)|None|
|Group|[]string|None|False|None|None|
|Host Count|integer|None|False|Count of unique endpoints which have ever reported this binary|None|
|Internal Name|string|None|False|If present, internal name from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)|None|
|Is 64-bit|boolean|None|False|True if x64|None|
|Is Executable Image|boolean|None|False|True if an EXE|None|
|Last Seen|date|None|False|None|None|
|Legal Copyright|string|None|False|If present, legal copyright from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)|None|
|Legal Trademark|string|None|False|If present, legal trademark from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)|None|
|MD5|string|None|False|The MD5 hash of this binary|None|
|Observed Filename|[]string|None|False|The set of unique filenames this binary has been seen as|None|
|Original Mod Length|integer|None|False|Filesize in bytes|None|
|Original Filename|string|None|False|If present, original filename from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)|None|
|OS Types|string|None|False|Operating system type of this binary; one of windows, linux, osx|None|
|Private Build|string|None|False|If present, private build from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)|None|
|Product Name|string|None|False|If present, product name from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)|None|
|Product Version|string|None|False|If present, product version from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)|None|
|Server Added Timestamp|string|None|False|The first time this binary was received on the server in the server GMT time|None|
|Signed|string|None|False|Digital signature status. One of Signed, Unsigned, Expired, Bad Signature, Invalid Signature, Invalid Chain, Untrusted Root, Explicit Distrust|None|
|Special Build|string|None|False|If present, special build from [FileVersionInformation](http://msdn.microsoft.com/en-us/library/system.diagnostics.fileversioninfo.aspx)|None|
|Timestamp|date|None|False|None|None|
  
**watchlist**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Alliance ID|integer|None|False|None|None|
|Date Added|date|None|False|None|None|
|Enabled|boolean|None|False|None|None|
|From Alliance|boolean|None|False|None|None|
|Group ID|integer|None|False|None|None|
|Index Type|string|None|False|Index to search for this watchlist|None|
|Last Hit|date|None|False|None|None|
|Last Hit Count|integer|None|False|None|None|
|List Query|string|None|False|URL-encoded search query associated with this watchlist|None|
|List Timestamp|date|None|False|None|None|
|Name|string|None|False|None|None|
|Readonly|boolean|None|False|None|None|
|Total Hits|string|None|False|None|None|
|Total Tags|string|None|False|None|None|
  
**feed**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Category|string|None|False|None|None|
|Display Name|string|None|False|None|None|
|Enabled|boolean|None|False|None|None|
|Feed URL|string|None|False|None|None|
|Icon|bytes|None|False|None|None|
|Icon Small|bytes|None|False|None|None|
|ID|integer|None|False|None|None|
|Local Rating|integer|None|False|None|None|
|Manually Added|boolean|None|False|None|None|
|Name|string|None|False|None|None|
|Order|integer|None|False|None|None|
|Password|string|None|False|None|None|
|Provider Rating|number|None|False|None|None|
|Provider URL|string|None|False|None|None|
|Requires|string|None|False|None|None|
|Requires What|string|None|False|None|None|
|Requires Who|string|None|False|None|None|
|SSL Client Certificate|string|None|False|None|None|
|SSL Client Key|string|None|False|None|None|
|Summary|string|None|False|None|None|
|Tech Data|string|None|False|None|None|
|Use Proxy|boolean|None|False|None|None|
|Username|string|None|False|None|None|
|Validate Server Cert|boolean|None|False|None|None|
  
**sensor**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Boot ID|string|None|None|Boot ID|None|
|Build ID|integer|None|None|Sensor build ID|None|
|Build Version String|string|None|None|Build version string|None|
|Computer DNS Name|string|None|None|DNS name of the computer|None|
|Computer Name|string|None|None|Computer name|None|
|Computer SID|string|None|None|Computer SID|None|
|Cookie|integer|None|None|Cookie|None|
|Display|boolean|None|None|Display|None|
|Event Log Flush Time|string|None|None|Event log flush time|None|
|Found|boolean|None|None|If sensor was found|None|
|Group ID|integer|None|None|Group ID|None|
|ID|integer|None|None|Sensor ID|None|
|Is Isolating|boolean|None|None|Is sensor isolated|None|
|Last Checkin Time|string|None|None|Last checkin time|None|
|License Expiration|string|None|None|License expiration|None|
|Network Adapters|string|None|None|Network adapters|None|
|Network Isolation Enabled|boolean|None|None|Network isolation enabled|None|
|Next Check-In Time|string|None|None|Next check-in time|None|
|Notes|string|None|None|Notes|None|
|OS Environment Display String|string|None|None|OS environment display string|None|
|OS Environment ID|integer|None|None|OS environment ID|None|
|Physical Memory Size|string|None|None|Physical memory size|None|
|Registration Time|string|None|None|Registration time|None|
|Sensor Health Message|string|None|None|Sensor health message|None|
|Sensor Health Status|integer|None|None|Sensor health status|None|
|Sensor Uptime|string|None|None|How long the sensor has been up|None|
|Systemvolume Free Size|string|None|None|Systemvolume free size|None|
|Systemvolume Total Size|string|None|None|Total size of system volume|None|
|Uninstall|boolean|None|None|Uninstall|None|
|Uptime|string|None|None|Uptime|None|


## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 3.3.2 - Resolving Snyk Vulnerabilities | SDK Bump to latest version (6.3.7)
* 3.3.1 - SDK Bump to latest version (6.3.6)
* 3.3.0 - Adding 'validators', 'urllib3', 'requests', 'certifi' and bumping 'cbapi' to '1.7.10' to address snyk vulnerabilities | 'SDK' bump and Plugin refresh
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

* [CarbonBlackEDR](https://www.vmware.com/products/endpoint-detection-and-response.html)

## References

* [VMware Carbon Black EDR REST API](https://developer.carbonblack.com/guide/enterprise-response/)
* [VMware Carbon Black EDR REST API 6.0-6.2x](https://developer.carbonblack.com/reference/enterprise-response/6.1/rest-api/)