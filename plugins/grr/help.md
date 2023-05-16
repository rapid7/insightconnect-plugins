# Description

[GRR Rapid Response](https://github.com/google/grr) is an incident response framework that allows you to focus on remote
live forensics. GRR is a python client (agent) that is installed on target systems, and python server infrastructure
that can manage and talk to clients.

The GRR plugin allows you to organize clients and start hunts using GRR.

This plugin utilizes the [GRR Python library](https://github.com/google/grr/tree/master/api_client/python).

# Key Features

* Organize GRR clients
* Start a hunt

# Requirements

* GRR credentials

# Supported Product Versions

_There are no supported product versions listed._

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|api_endpoint|string|None|True|The GRR API Endpoint to connect to|None|www.example.com|
|credentials|credential_username_password|None|True|Username and password|None|{}|
|ssl_verify|boolean|True|True|Verify server's SSL/TLS certificate|None|True|

Example input:

```
{
  "api_endpoint":"www.example.com",
  "credentials":{
    "username":"user",
    "password":"pass"
  },
  "ssl_verify":true
}
```

## Technical Details

### Actions

#### Labeling

This action is used to label clients based on a search query.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|label|[]string|None|True|Label's clients|None|[]|
|query|string|None|True|Search for clients|None|client:client1|

Example input:

```
{
  "label": ["label1", "label2"],
  "query": "client:client1"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|string|False|Labeling complete|

Example output:

```

{
  "results": "All clients have been labeled"
}

```

#### Listing

This action is used to find and list clients based on a search query.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|clients|boolean|None|False|Search clients|None|True|
|grr_binaries|boolean|None|False|List GRR binaries|None|True|
|hunt_approvals|boolean|None|False|List hunt approvals|None|True|
|hunts|boolean|None|False|List hunts|None|True|
|query|string|None|True|Query to search for (e.g. 'host:suspicious.corp.com')|None|host:suspicious.corp.com|

Example input:

```
{
  "clients":true,
  "grr_binaries":true,
  "hunt_approvals":true,
  "hunts":true,
  "query": "host:suspicious.corp.com"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|object|False|Listing results|

Example output:

```

{
  "result": {
    "client0": {
      "hardwareInfo": {
        "biosVersion": "VirtualBox",
        "serialNumber": "0",
        "biosVendor": "innotek GmbH",
        "systemSkuNumber": "Not Specified",
        "biosReleaseDate": "12/01/2006",
        "systemProductName": "VirtualBox",
        "systemFamily": "Virtual Machine",
        "systemUuid": "E9200C28-9075-46CE-A477-A9BAEF46FBE6",
        "biosRomSize": "128 kB",
        "systemManufacturer": "innotek GmbH"
      },
      "osInfo": {
        "machine": "x86_64",
        "kernel": "4.15.0-20-generic",
        "version": "18.4",
        "installDate": "1529100873000000",
        "release": "Ubuntu",
        "system": "Linux",
        "fqdn": "anonymous-VirtualBox"
      },
      "labels": [
        {
          "owner": "admin",
          "name": "suspicious"
        }
      ],
      "knowledgeBase": {
        "osRelease": "Ubuntu",
        "osMinorVersion": 4,
        "os": "Linux",
        "fqdn": "anonymous-VirtualBox",
        "osMajorVersion": 18
      },
      "agentInfo": {
        "clientDescription": "grr linux amd64",
        "buildTime": "2018-03-08 12:12:56",
        "clientVersion": 3220,
        "clientName": "grr"
      },
      "lastClock": "1531947560875707",
      "memorySize": "2090307584",
      "clientId": "C.8956f9766996b204",
      "lastBootedAt": "1531333783000000",
      "age": "1531333800792079",
      "firstSeenAt": "1529101768850237",
      "volumes": [
        {
          "actualAvailableAllocationUnits": "1147463",
          "totalAllocationUnits": "2563397",
          "sectorsPerAllocationUnit": "1",
          "bytesPerSector": "4096",
          "unixvolume": {
            "mountPoint": "/"
          }
        }
      ],
      "interfaces": [
        {
          "macAddress": "AAAAAAAA",
          "ifname": "lo",
          "addresses": [
            {
              "packedBytes": "fwAAAQ==",
              "addressType": "INET"
            },
            {
              "packedBytes": "AAAAAAAAAAAAAAAAAAAAAQ==",
              "addressType": "INET6"
            }
          ]
        },
        {
          "macAddress": "CAAn9SZD",
          "ifname": "enp0s3",
          "addresses": [
            {
              "packedBytes": "CgACDw==",
              "addressType": "INET"
            },
            {
              "packedBytes": "/oAAAAAAAADBDDCBmP7VBQ==",
              "addressType": "INET6"
            }
          ]
        }
      ],
      "lastSeenAt": "1531947561202751",
      "urn": "aff4:/C.8956f9766996b204"
   }
}

```

#### Hunting

This action is used to start a hunt on clients.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|action|string|None|False|Use an action|['STAT', 'HASH', 'DOWNLOAD']|None|
|annotations|[]string|None|False|Annotations to add to exported data. This field can be used to differentiate sets of exported data inside a particular exported type. e.g. data collected by users vs. data collected by cronjob|None|None|
|apply_parsers|boolean|None|False|If 1, apply any relevant parser to the collected data. If 0, return the raw collected data e.g Files or Registry Keys|None|None|
|artifact_list|string|None|False|A list of Artifact class names|None|None|
|attribute_regex|string|None|False|The regular expression|None|None|
|bytes_after|integer|None|False|Include this many bytes after the hit|None|None|
|bytes_before|integer|None|False|Include this many bytes before the hit|None|None|
|ch_username|string|None|False|The user to get Chrome history for. If history_path is not set this will be used to guess the path to the history files|None|None|
|check_chrome|integer|None|False|Checks Chrome|None|None|
|check_firefox|integer|None|False|Checks Chrome|None|None|
|check_ie|boolean|None|False|Checks Internet Explorer|None|None|
|chunk_size|integer|None|False|A heartbeat will be emitted every chunk_size.This could be reduced in case the process times out|None|None|
|client_limit|integer|None|False|Maximum number of clients participating in the hunt. Best practice is for all hunts to use a limit to start with and remove it only when client impact has been assessed by looking at hunt stats. Note that this limit can be overshot by a small number of clients if there are multiple workers running |None|None|
|client_rate|integer|None|False|The maximum number of clients to engage per minute. A rate of 0 means to schedule clients as fast as possible|None|None|
|component_version|string|None|False|Version of Chipsec component to be used|None|None|
|conditions|string|None|False|These conditions will be applied to all files that match the path arguments|['MODIFICATION_TIME', 'ACCESS_TIME', 'INODE_CHANGE_TIME', 'SIZE', 'CONTENTS_REGEX_MATCH', 'CONTENTS_LITERAL_MATCH', 'EXT_FLAGS']|None|
|connection_states|[]string|None|False|Network connection states to match. If a process has any network connections in any status listed here, it will be considered a match|['UNKNOWN', 'CLOSED', 'LISTEN', 'SYN_SENT', 'SYN_RECV', 'ESTABLISHED', 'FIN_WAIT1', 'FIN_WAIT2', 'CLOSE_WAIT', 'CLOSING', 'LAST_ACK', 'TIME_WAIT', 'DELETE_TCB', 'NONE', 'CLOSE']|None|
|convert_values|boolean|None|False|If true, convert values for export-friendly format|None|None|
|cpu_limit|integer|None|False|A limit on the client CPU seconds used by this flow|None|None|
|crash_alert_email|string|None|False|An email address to send mails to when a client crashes during execution of this hunt|None|None|
|data_regex|string|None|False|A regular expression to search for|None|None|
|dependencies|string|USE_CACHED|False|Specifies how dependencies should be handled. Use the knowledgebase as a cache. If knowledgebase isn't present, a new one will be populated|['USE_CACHED', 'IGNORE_DEPS', 'FETCH_NOW']|None|
|description|string|None|False|The description of this hunt|None|None|
|duration|integer|3600|False|Until when should the client stay in the fast poll mode|None|None|
|email|string|None|False|Email address to send to. If not set, mail will be sent to the logged in user|None|None|
|email_address|string|None|False|The email address that messages will be sent to|None|None|
|emails_limit|integer|None|False|The emails limit|None|None|
|expiry_time|integer|None|False|Expiry time for the hunt|None|None|
|export_files_contents|boolean|None|False|If this is true, open files and export their full or partial contents. Note: this may require additional datastore roundtrips and slow down the export process, also exporting file contents may significantly increase size of the exported data|None|None|
|export_files_hashes|boolean|None|False|If this is true, export hashes when dealing with file-related values. The files won't be hashed during the export, hashes will only be exported if they were collected before the export. This option affects exporting VFSFile and StatEntry RDFValues. This is true by default even though it requires extra datastore roundtrips because it's very useful and users expect the hashes to be there|None|None|
|fetch_binaries|boolean|None|False|Fetches Binaries|None|None|
|ff_username|string|None|False|The user to get FireFox history for. If history_path is not set this will be used to guess the path to the history files|None|None|
|field|string|UNSET|False|Field Specification|['UNSET', 'USERNAMES', 'UNAME', 'FQDN', 'HOST_TIPS', 'CLIENT_NAME', 'CLIENT_DESCRIPTION', 'SYSTEM', 'MAC_ADDRESSES', 'KERNEL_VERSION', 'OS_VERSION', 'OS_RELEASE', 'CLIENT_LABELS', 'INSTALL_TIME', 'CLIENT_VERSION', 'LAST_BOOT_TIME', 'CLIENT_CLOCK']|None|
|filefinder_regex|string|None|False|The regular expression which will be used to search|None|None|
|filename_regex|string|None|False|Regex used to filter the list of processes|None|None|
|flow_args|boolean|False|False|Enable high signal regex checks|None|None|
|flow_name|string|None|True|The name of the Flow you want to use|['Interrogate', 'KeepAlive', 'OnlineNotification', 'CacheGrep', 'ChromeHistory', 'FirefoxHistory', 'CheckRunner', 'ArtifactCollectorFlow', 'DumpACPITable', 'DumpFlashImage', 'FileFinder', 'GetMBR', 'ListVolumeShadowCopies', 'Netstat', 'ListProcesses', 'CollectRunKeyBinaries', 'RegistryFinder']|None|
|follow_links|boolean|None|False|Should symbolic links be followed in recursive directory listings|None|None|
|follow_urns|boolean|None|False|If this is true, follow urns and try to export not only the urns themselves, but also the data they are pointing to. Note: this may require additional datastore roundtrips and slow down the export process|None|None|
|get_archive|boolean|None|False|Gets Archived History as well (3 months old)|None|None|
|grep_users|string|None|False|A list of users to check. Default all users on the system|None|None|
|history_path|string|None|False|Path to a profile directory that contains a History file|None|None|
|hunt_name|string|None|False|The name of the class implementing the hunt to run|None|None|
|ignore_interpolation_errors|boolean|None|False|If true, don't die if %%users.homedir%% and similar fail to expand. It's common on windows for some user attributes to be missing if users have never logged in. Enable this when you have multiple artifacts or paths and want to report partial results|None|None|
|integer|boolean|None|False|Integer to trigger this hunt|None|None|
|knowledge_base|string|None|False|An optional knowledge base to use, if not specified we retrieve one from the client object|None|None|
|label|[]string|None|False|Label that triggers this hunt|None|None|
|length|integer|None|False|How far (in bytes) into the file to search or the length of the MBR to read|None|None|
|lightweight|boolean|None|False|Performs a light weight version of the interrogate|None|None|
|listening_only|boolean|None|False|If set, only listening connections are returned|None|None|
|literal|string|None|False|Search for this literal string|None|None|
|log_level|integer|None|False|Set the log level. If set, the log returned will include additional information reported by Chipsec|None|None|
|logging|boolean|None|False|If the logging is set to true, the client sends log, including Chipsec's log|None|None|
|match_mode|string|None|False|Match mode to trigger this hunt|['MATCH_ALL', 'MATCH_ANY']|None|
|max_file_size|string|None|False|The maximum size of files we will download in bytes, 500MB by default|None|None|
|max_findings|integer|None|False|Summarize checks with more than N individual findings|None|None|
|max_last_access_time|integer|None|False|File must be accessed before this time|None|None|
|max_last_inode_change_time|integer|None|False|File's must be changed before this time|None|None|
|max_last_modified_time|integer|None|False|File must be modified before this time|None|None|
|max_size|integer|None|False|The maximum size of files|None|None|
|min_file_size|integer|None|False|Minimum file size in bytes|None|None|
|min_last_access_time|integer|None|False|File must be accessed after this time|None|None|
|min_last_inode_change_time|integer|None|False|File's inode must be changed after this time|None|None|
|min_last_modified_time|integer|None|False|File must be modified after this time|None|None|
|mode|string|None|False|When should searching stop? Stop after one hit or search for all|['FIRST_HIT', 'ALL_HITS']|None|
|network_bytes_limit|integer|None|False|A limit on the total traffic used by this flow|None|None|
|notification_event|string|None|False|An event name for an event listener. An event will be published to this listener once the flow finishes|None|None|
|notify_syslog|boolean|None|False|If true, a message will be written by the client to the syslog before running the action. This can be used for debugging in case the client crashes |None|None|
|on_no_results_error|boolean|None|False|The maximum size of files we will download in bytes, 500MB by default|None|None|
|only_cpe|string|None|False|Limit checks to hosts with cpe strings|None|None|
|only_label|string|None|False|Limit checks to hosts with label strings|None|None|
|only_os|string|None|False|Limit checks to hosts of OS type(s) [Linux|OSX|Windows]|None|None|
|operating_system|string|None|False|Type of operating system to trigger this hunt|['Os_windows', 'Os_linux', 'Os_darwin']|None|
|operator|string|None|False|Operator|['EQUAL', 'LESS_THAN', 'GREATER_THAN']|None|
|output_plugin_name|string|None|False|The name of the output plugin|['EmailOutput', 'BigQueryOutput']|None|
|oversized_file_policy|string|None|False|What should GRR do with files that are larger than max_size|['SKIP', 'HASH_TRUNCATED', 'DOWNLOAD_TRUNCATED']|None|
|paths|string|None|False|A path to glob that can contain %% expansions|None|None|
|pathtype|string|None|False|Type of path access to use|['UNSET', 'OS', 'TSK', 'Registry', 'Memory', 'TMPFILE']|None|
|priority|string|None|False|The priority used for this flow|['LOW_PRIORITY', 'MEDIUM_PRIORITY', 'HIGH_PRIORITY']|None|
|process_non_regular_files|boolean|None|False|Look both into regular files and non-regular files (devices, named pipes, sockets). NOTE: This is very dangerous and should be used with care|None|None|
|queue|string|None|False|The queue to use for the hunt|None|None|
|regex|boolean|None|False|Use a regular expression to trigger this hunt|None|None|
|resolve_links|boolean|None|False|If true, the action will yield stat information for link targets, if false, the stat for the link itself will be returned|None|None|
|restrict_checks|string|None|False|Only run checks with the specified check_ids|None|None|
|split_output_by_artifact|boolean|None|False|If True, use output as a directory and write a separate collection for each artifact collected|None|None|
|start_offest|integer|None|False|Start searching at this file offset|None|None|
|start_offset|integer|None|False|Start searching at this file offset|None|None|
|table_signature_list|string|None|False|Signature of ACPI tables to be dumped|None|None|
|upload_token|boolean|None|False|An upload token to use with the direct upload functionality. This token contains the hmac authenticated policy that determines for how long the client is allowed to upload files to the server. This is comparable to the policy document used by GCS: https://cloud.google.com/storage/docs/xml-api/post-object#policydocument|None|None|
|use_external_stores|boolean|None|False|If true, look in any defined external file stores for files before downloading them, and offer any new files to external stores. This should be true unless the external checks are misbehaving|None|None|
|use_tsk|boolean|None|False|Whether raw filesystem access should be used|None|None|
|value|integer|None|False|Value|None|None|
|xdev|string|None|False|Behavior when ecountering device boundaries while doing recursive searches|['NEVER', 'ALWAYS', 'LOCAL']|None|
|xor_in_key|integer|None|False|When searching memory we need to ensure we dont hit on our own process. This allows us to obfuscate the search string in memory to avoid us finding ourselves|None|None|
|xor_out_key|integer|None|False|When searching memory we need to ensure we dont hit on our own process. This allows us to obfuscate the search string in memory to avoid us finding ourselves|None|None|

Example input:

```
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|results|string|False|Issues found with TruffleHog|

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 3.0.0 - Updated requests version | default values and enum changed for hunting
* 2.0.2 - Correct spelling in help.md
* 2.0.1 - New spec and help.md format for the Extension Library
* 2.0.0 - Add certificate validation to connection
* 1.0.1 - Support web server mode
* 1.0.0 - Initial plugin

# Links

## References

* [GRR](https://github.com/google/grr/tree/master/api_client/python)

