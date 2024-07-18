# Description

[VMware Carbon Black EDR](https://www.carbonblack.com/products/edr/) is the most complete endpoint detection and response solution available to security teams. The InsightConnect plugin allows you to automate information collection, endpoint isolation and hash blacklisting.

This plugin utilizes the [VMware Carbon Black EDR REST API](https://developer.carbonblack.com/guide/enterprise-response/).

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
|alerts|[]alert|False|The lists of alerts|None|
  
Example output:

```
{
  "alerts": [
    {
      "Created Time": "",
      "Feed ID": {},
      "Feed Name": {},
      "Feed Rating": {},
      "Hostname": "",
      "IOC Attributes": {},
      "IOC Confidence": {},
      "MD5": {},
      "OS Type": {},
      "Report Score": 0,
      "Sensor Criticality": {},
      "Sensor ID": {},
      "Severity": 0,
      "Status": {},
      "Type": {},
      "Unique ID": {}
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
|binaries|[]binary|False|The list of binaries|None|
  
Example output:

```
{
  "binaries": [
    {
      "Alliance Score Virustotal": {},
      "Carbon Black Version": {},
      "Company Name": {},
      "Copied Mod Length": {},
      "Digital Signature Issuer": {},
      "Digital Signature Program Name": "",
      "Digital Signature Publisher": {},
      "Digital Signature Result": {},
      "Digital Signature Result Code": {},
      "Digital Signature Subject": {},
      "Digital Signature Times": {},
      "Endpoint": {},
      "File Description": {},
      "File Version": {},
      "Group": {},
      "Host Count": {},
      "Internal Name": {},
      "Is 64-bit": {},
      "Is Executable Image": "true",
      "Last Seen": {},
      "Legal Copyright": {},
      "Legal Trademark": {},
      "MD5": {},
      "OS Types": {},
      "Observed Filename": [
        {}
      ],
      "Original Filename": {},
      "Original Mod Length": 0,
      "Private Build": {},
      "Product Name": {},
      "Product Version": {},
      "Server Added Timestamp": {},
      "Signed": {},
      "Special Build": {},
      "Timestamp": ""
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
|feeds|[]feed|False|The list of feeds|None|
  
Example output:

```
{
  "feeds": [
    {
      "Category": {},
      "Display Name": {},
      "Enabled": {},
      "Feed URL": {},
      "ID": {},
      "Icon": {},
      "Icon Small": "",
      "Local Rating": 0,
      "Manually Added": {},
      "Name": {},
      "Order": {},
      "Password": {},
      "Provider Rating": 0,
      "Provider URL": "",
      "Requires": {},
      "Requires What": {},
      "Requires Who": {},
      "SSL Client Certificate": {},
      "SSL Client Key": {},
      "Summary": {},
      "Tech Data": {},
      "Use Proxy": "true",
      "Username": {},
      "Validate Server Cert": {}
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
|processes|[]process|False|The list of processes|None|
  
Example output:

```
{
  "processes": [
    {
      "Binaries": {},
      "CMD Line": {},
      "Childproc Count": {},
      "Comms IP": {},
      "Crossproc Count": {},
      "EMET Count": {},
      "Filemod Complete": [
        {}
      ],
      "Filemod Count": {},
      "Filtering Known Downloads": "true",
      "Group": {},
      "Host Type": {},
      "Hostname": {},
      "ID": {},
      "Interface IP": {},
      "Last Update": {},
      "MD5": {},
      "Mod Load": 0,
      "Name": {},
      "Netconn Count": {},
      "OS Type": {},
      "PID": {},
      "Parent Name": {},
      "Parent PID": {},
      "Parent Unique ID": {},
      "Path": {},
      "Process Block Count": {},
      "Regmod Count": {},
      "Segment ID": {},
      "Sensor ID": {},
      "Start": {},
      "Terminated": {},
      "UID": "",
      "Unique ID": {},
      "Username": {}
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
|sensors|[]sensor|False|The list of sensors|None|
  
Example output:

```
{
  "sensors": [
    {
      "Boot ID": {},
      "Build ID": {},
      "Build Version String": {},
      "Computer DNS Name": {},
      "Computer Name": {},
      "Computer SID": {},
      "Cookie": {},
      "Display": {},
      "Event Log Flush Time": {},
      "Found": {},
      "Group ID": {},
      "ID": 0,
      "Is Isolating": "true",
      "Last Checkin Time": {},
      "License Expiration": {},
      "Network Adapters": {},
      "Network Isolation Enabled": {},
      "Next Check-In Time": {},
      "Notes": {},
      "OS Environment Display String": {},
      "OS Environment ID": {},
      "Physical Memory Size": {},
      "Registration Time": {},
      "Sensor Health Message": {},
      "Sensor Health Status": {},
      "Sensor Uptime": {},
      "Systemvolume Free Size": {},
      "Systemvolume Total Size": "",
      "Uninstall": {},
      "Uptime": {}
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
|watchlists|[]watchlist|False|The list of watchlists|None|
  
Example output:

```
{
  "watchlists": [
    {
      "Alliance ID": {},
      "Date Added": {},
      "Enabled": "true",
      "From Alliance": {},
      "Group ID": {},
      "Index Type": {},
      "Last Hit": {},
      "Last Hit Count": 0,
      "List Query": {},
      "List Timestamp": "",
      "Name": "",
      "Readonly": {},
      "Total Hits": {},
      "Total Tags": {}
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
|alert|alert|False|Carbon Black alert|None|
  
Example output:

```
{
  "alert": {
    "Created Time": "",
    "Feed ID": {},
    "Feed Name": {},
    "Feed Rating": {},
    "Hostname": "",
    "IOC Attributes": {},
    "IOC Confidence": {},
    "MD5": {},
    "OS Type": {},
    "Report Score": 0,
    "Sensor Criticality": {},
    "Sensor ID": {},
    "Severity": 0,
    "Status": {},
    "Type": {},
    "Unique ID": {}
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

This plugin does not contain any troubleshooting information.

# Version History

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