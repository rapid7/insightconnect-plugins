# Description

ANY.RUN Sandbox is an online interactive sandbox for malware analysis, a tool for detection, monitoring, and research of cyber threats in real time

# Key Features

* Submit a file or URL to ANY.RUN for analysis using the following OS - Windows, Linux, Android
* Retrieve report details for a given analysis ID in various formats - HTML, STIX, JSON
* Retrieve malicious or suspicious IOCs for a given analysis ID.
* View history of analysis tasks.
* View analysis verdict.
* Download analysis network traffic dumps.
* Perform deep searches, look up threats online, and enrich your security solutions using ANY.RUN TI Lookup.
* Retrieve IP, Domain, URL, MD5, SHA256, SHA1 reputation.
* Load fresh IPv4, URL, and Domain-Name indicators.

# Requirements

* Requires an ANY.RUN Sandbox or ANY.RUN TI Lookup API key without a prefix
* Available on ANY.RUN plans with API access, including trial

# Supported Product Versions

* ANY.RUN API 2026-03-20

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|sandbox_api_key|credential_secret_key|None|False|API key for ANY.RUN Sandbox|None|WbTbwa4KFk77eQNffMJynWXm49jLwGjwPMKM9Xc4|None|None|
|ti_feeds_api_key|credential_secret_key|None|False|API key for ANY.RUN TI Feeds|None|WbTbwa4KFk77eQNffMJynWXm49jLwGjwPMKM9Xc4|None|None|
|ti_lookup_api_key|credential_secret_key|None|False|API key for ANY.RUN TI Lookup|None|WbTbwa4KFk77eQNffMJynWXm49jLwGjwPMKM9Xc4|None|None|

Example input:

```
{
  "sandbox_api_key": "WbTbwa4KFk77eQNffMJynWXm49jLwGjwPMKM9Xc4",
  "ti_feeds_api_key": "WbTbwa4KFk77eQNffMJynWXm49jLwGjwPMKM9Xc4",
  "ti_lookup_api_key": "WbTbwa4KFk77eQNffMJynWXm49jLwGjwPMKM9Xc4"
}
```

## Technical Details

### Actions


#### Android File Analysis

This action is used to run File analysis using Android VM

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|env_locale|string||False|Operation System language. Use locale identifier or country name Example - ( "en-US" or "Brazil"). Case insensitive|None|en-US|None|None|
|file_content|bytes|None|True|File bytes|None|bytes|None|None|
|filename|string|None|True|Filename|None|malware.zip|None|None|
|opt_auto_delete_after|string||False|Specify after what period of time this report should be deleted|["", "day", "week", "2 weeks", "month"]|month|None|None|
|opt_network_connect|boolean|True|False|Network connection state|None|True|None|None|
|opt_network_fakenet|boolean|False|False|FakeNet feature status|None|False|None|None|
|opt_network_geo|string||False|TOR geo location option|None|fastest|None|None|
|opt_network_mitm|boolean|False|False|HTTPS MITM proxy option|None|False|None|None|
|opt_network_residential_proxy|boolean|False|False|Residential Proxy option|None|False|None|None|
|opt_network_residential_proxy_geo|string||False|Residential Proxy Geo option|None|fastest|None|None|
|opt_network_tor|boolean|False|False|TOR using|None|False|None|None|
|opt_privacy_type|string|bylink|False|Privacy settings|["", "public", "bylink", "owner", "byteam"]|bylink|None|None|
|opt_timeout|integer|240|False|Timeout option, size range 10-660|None|240|None|None|
|user_tags|string||False|Append User Tags to new analysis. Only characters a-z, A-Z, 0-9, hyphen (-), and comma (,) are allowed. Max tag length - 16 characters. Max unique tags per analysis - 8|None|insight-connect|None|None|
  
Example input:

```
{
  "env_locale": "",
  "file_content": "bytes",
  "filename": "malware.zip",
  "opt_auto_delete_after": "",
  "opt_network_connect": true,
  "opt_network_fakenet": false,
  "opt_network_geo": "",
  "opt_network_mitm": false,
  "opt_network_residential_proxy": false,
  "opt_network_residential_proxy_geo": "",
  "opt_network_tor": false,
  "opt_privacy_type": "bylink",
  "opt_timeout": 240,
  "user_tags": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|analysis_url|string|False|Link to the interactive analysis|0cf223f2-530e-4a50-b68f-563045268648|
|analysis_uuid|string|False|Analysis UUID|0ec0a4cc-72a4-41b9-8a13-9f283b3b4e15|
  
Example output:

```
{
  "analysis_url": "0cf223f2-530e-4a50-b68f-563045268648",
  "analysis_uuid": "0ec0a4cc-72a4-41b9-8a13-9f283b3b4e15"
}
```

#### Android URL Analysis

This action is used to run URL analysis using Android VM

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|env_locale|string||False|Operation System language. Use locale identifier or country name Example - ( "en-US" or "Brazil"). Case insensitive|None|en-US|None|None|
|obj_url|string|None|True|Target URL. Size range 5-512. Example -> (http/https)://(your-link)|None|https://example.org|None|None|
|opt_auto_delete_after|string||False|Specify after what period of time this report should be deleted|["", "day", "week", "2 weeks", "month"]|month|None|None|
|opt_network_connect|boolean|True|False|Network connection state|None|True|None|None|
|opt_network_fakenet|boolean|False|False|FakeNet feature status|None|False|None|None|
|opt_network_geo|string||False|TOR geo location option|None|fastest|None|None|
|opt_network_mitm|boolean|False|False|HTTPS MITM proxy option|None|False|None|None|
|opt_network_residential_proxy|boolean|False|False|Residential Proxy option|None|False|None|None|
|opt_network_residential_proxy_geo|string||False|Residential Proxy Geo option|None|fastest|None|None|
|opt_network_tor|boolean|False|False|TOR using|None|False|None|None|
|opt_privacy_type|string|bylink|False|Privacy settings|["", "public", "bylink", "owner", "byteam"]|bylink|None|None|
|opt_timeout|integer|120|False|Timeout option, size range 10-660|None|120|None|None|
|user_tags|string||False|Append User Tags to new analysis. Only characters a-z, A-Z, 0-9, hyphen (-), and comma (,) are allowed. Max tag length - 16 characters. Max unique tags per analysis - 8|None|insight-connect|None|None|
  
Example input:

```
{
  "env_locale": "",
  "obj_url": "https://example.org",
  "opt_auto_delete_after": "",
  "opt_network_connect": true,
  "opt_network_fakenet": false,
  "opt_network_geo": "",
  "opt_network_mitm": false,
  "opt_network_residential_proxy": false,
  "opt_network_residential_proxy_geo": "",
  "opt_network_tor": false,
  "opt_privacy_type": "bylink",
  "opt_timeout": 120,
  "user_tags": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|analysis_url|string|False|Link to the interactive analysis|0cf223f2-530e-4a50-b68f-563045268648|
|analysis_uuid|string|False|Analysis UUID|0ec0a4cc-72a4-41b9-8a13-9f283b3b4e15|
  
Example output:

```
{
  "analysis_url": "0cf223f2-530e-4a50-b68f-563045268648",
  "analysis_uuid": "0ec0a4cc-72a4-41b9-8a13-9f283b3b4e15"
}
```

#### Download PCAP

This action is used to download a PCAP file

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|analysis_uuid|string|None|True|Analysis UUID|None|0cf223f2-530e-4a50-b68f-563045268648|None|None|
  
Example input:

```
{
  "analysis_uuid": "0cf223f2-530e-4a50-b68f-563045268648"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|pcap|file|False|SAnalysis PCAP|file|
  
Example output:

```
{
  "pcap": "file"
}
```

#### Get Analysis History

This action is used to get last analyses from the user's history and their basic information

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|limit|integer|0|False|Specify the number of analyses in the result set (not more than 100)|None|25|None|None|
|skip|integer|0|False|Skip the specified number of analyses|None|25|None|None|
|team|boolean|False|False|Leave this field blank to get your history or specify to get team history|None|False|None|None|
  
Example input:

```
{
  "limit": 0,
  "skip": 0,
  "team": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|analyses|[]analysis|False|Analyses history|[{"related":"https://app.any.run/tasks/82ab98a6-b406-4ba5-8deb-...","json":"https://api.any.run/report/82ab98a6-b406-4ba5-8deb...","file":"https://content.any.run/tasks/82ab98a6-b406-4ba5-8...","hashes":{"head_hash":"0145ad575b213b1703cb94c6c3568a2e","md5":"926e6146fdb288e932a1846029ad07db","sha1":"fc73d7c62e324cad4240fbaf7a6d53716ecc4de7","sha256":"f6df99db2023558798d234f9c118497db8ec83da37682f8868...","ssdeep":"768:s+QiSf3rhTePO38fXbEmJS2Iro2wFW0kEeu:svXj5ePO3C..."},"misp":"https://api.any.run/report/82ab98a6-b406-4ba5-8deb...","name":"http://pastebin.com/raw/xGXyTALF","pcap":"https://content.any.run/tasks/82ab98a6-b406-4ba5-8...","tags":[],"verdict":"No threats detected","date":"2020-04-23T21:00:13.890Z"},{"date":"2020-04-20T02:14:11.452Z","file":"https://content.any.run/tasks/923fa62b-2689-4e6a-b...","hashes":{"sha256":"71f34b8bda00b54713e92cb8aee8c04a11ea5dea650b07f4b1...","ssdeep":"3:N1KdJMP2:CO2","head_hash":"780024dc16cb4331cdf98d18eb111bb4","md5":"780024dc16cb4331cdf98d18eb111bb4","sha1":"dfc3414b0e62c18787631322ae7a8c7489e845c9"},"json":"https://api.any.run/report/923fa62b-2689-4e6a-be76...","pcap":"https://content.any.run/tasks/923fa62b-2689-4e6a-b...","tags":[],"misp":"https://api.any.run/report/923fa62b-2689-4e6a-be76...","name":"http://clicnews.com","related":"https://app.any.run/tasks/923fa62b-2689-4e6a-be76-...","verdict":"Malicious activity"}]|
  
Example output:

```
{
  "analyses": [
    {
      "date": "2020-04-23T21:00:13.890Z",
      "file": "https://content.any.run/tasks/82ab98a6-b406-4ba5-8...",
      "hashes": {
        "head_hash": "0145ad575b213b1703cb94c6c3568a2e",
        "md5": "926e6146fdb288e932a1846029ad07db",
        "sha1": "fc73d7c62e324cad4240fbaf7a6d53716ecc4de7",
        "sha256": "f6df99db2023558798d234f9c118497db8ec83da37682f8868...",
        "ssdeep": "768:s+QiSf3rhTePO38fXbEmJS2Iro2wFW0kEeu:svXj5ePO3C..."
      },
      "json": "https://api.any.run/report/82ab98a6-b406-4ba5-8deb...",
      "misp": "https://api.any.run/report/82ab98a6-b406-4ba5-8deb...",
      "name": "http://pastebin.com/raw/xGXyTALF",
      "pcap": "https://content.any.run/tasks/82ab98a6-b406-4ba5-8...",
      "related": "https://app.any.run/tasks/82ab98a6-b406-4ba5-8deb-...",
      "tags": [],
      "verdict": "No threats detected"
    },
    {
      "date": "2020-04-20T02:14:11.452Z",
      "file": "https://content.any.run/tasks/923fa62b-2689-4e6a-b...",
      "hashes": {
        "head_hash": "780024dc16cb4331cdf98d18eb111bb4",
        "md5": "780024dc16cb4331cdf98d18eb111bb4",
        "sha1": "dfc3414b0e62c18787631322ae7a8c7489e845c9",
        "sha256": "71f34b8bda00b54713e92cb8aee8c04a11ea5dea650b07f4b1...",
        "ssdeep": "3:N1KdJMP2:CO2"
      },
      "json": "https://api.any.run/report/923fa62b-2689-4e6a-be76...",
      "misp": "https://api.any.run/report/923fa62b-2689-4e6a-be76...",
      "name": "http://clicnews.com",
      "pcap": "https://content.any.run/tasks/923fa62b-2689-4e6a-b...",
      "related": "https://app.any.run/tasks/923fa62b-2689-4e6a-be76-...",
      "tags": [],
      "verdict": "Malicious activity"
    }
  ]
}
```

#### Get Analysis Report

This action is used to get detailed JSON, HTML or STIX report for analysis

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|analysis_uuid|string|None|True|Analysis UUID|None|0cf223f2-530e-4a50-b68f-563045268648|None|None|
|format|string|html|True|Report file in JSON, HTML or STIX format|["html", "json", "stix"]|html|None|None|
  
Example input:

```
{
  "analysis_uuid": "0cf223f2-530e-4a50-b68f-563045268648",
  "format": "html"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|analysis_url|string|False|Link to the interactive analysis|0cf223f2-530e-4a50-b68f-563045268648|
|analysis_uuid|string|False|Analysis UUID|0cf223f2-530e-4a50-b68f-563045268648|
|report|file|False|Report file|file|
  
Example output:

```
{
  "analysis_url": "0cf223f2-530e-4a50-b68f-563045268648",
  "analysis_uuid": "0cf223f2-530e-4a50-b68f-563045268648",
  "report": "file"
}
```

#### Get Analysis Verdict

This action is used to get the verdict of a specific analysis

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|analysis_uuid|string|None|True|Analysis UUID|None|0cf223f2-530e-4a50-b68f-563045268648|None|None|
  
Example input:

```
{
  "analysis_uuid": "0cf223f2-530e-4a50-b68f-563045268648"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|verdict|string|False|Analysis verdict. Can be 'Malicious', 'Suspicious' or 'No threads detected'|Malicious|
  
Example output:

```
{
  "verdict": "Malicious"
}
```

#### Get Intelligence

This action is used to make a query to the ANY.RUN Threat Intelligence database using flexible searches for Indicators 
of Compromise (IOCs), Indicators of Attack(IOAs), and Indicators of Behavior (IOBs) to investigate and gather extensive 
and in-depth information on cyber threats

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|lookup_depth|int|180|True|Specify the number of days from the current date for which you want to lookup|None|180|None|None|
|query|string|None|True|Raw query with necessary filters. Supports condition concatenation with AND, OR, NOT and Parentheses ()|None|domainName:"\rvonline.hu" OR url:"*\rvonline.hu*"|None|None|
  
Example input:

```
{
  "lookup_depth": 180,
  "query": "domainName:\"\\rvonline.hu\" OR url:\"*\\rvonline.hu*\""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|lookup_url|string|False|Link to the TI Lookup Query|https://intelligence.any.run/analysis/lookup#{%22query%22:%22http://171.22.28.221/5c06c05b7b34e8e6.php%22,%22dateRange%22:180}|
|report|file|False|Lookup Summary JSON|file|
  
Example output:

```
{
  "lookup_url": "https://intelligence.any.run/analysis/lookup#{%22query%22:%22http://171.22.28.221/5c06c05b7b34e8e6.php%22,%22dateRange%22:180}",
  "report": "file"
}
```

#### Get IOC

This action is used to get malicious and suspicious IOCs in CSV format from the analysis if available

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|analysis_uuid|string|None|True|Analysis UUID|None|0cf223f2-530e-4a50-b68f-563045268648|None|None|
  
Example input:

```
{
  "analysis_uuid": "0cf223f2-530e-4a50-b68f-563045268648"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|count|int|False|The number of found IOCs|None|
|report|file|False|Suspicious and Malicious IOCs CSV|file|
  
Example output:

```
{
  "count": 0,
  "report": "file"
}
```

#### Get Reputation

This action is used to check URL/IP/Domain/File reputation

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|entity_type|string|url|True|Entity type to search in database|["url", "hash", "destination_ip", "domain_name"]|url|None|None|
|entity_value|string|None|True|URL (Size range 2-256) or Hash (SHA256, SHA1, MD5) or Domain or IP|None|https://suspicious.url|None|None|
|lookup_depth|int|180|True|Specify the number of days from the current date for which you want to lookup|None|180|None|None|
  
Example input:

```
{
  "entity_type": "url",
  "entity_value": "https://suspicious.url",
  "lookup_depth": 180
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|asowner|string|False|IOC-related autonomous system owner|cloudflarenet|
|file_extension|string|False|IOC-related file extension|exe|
|filename|string|False|IOC-related filename|passwords|
|filepath|string|False|IOC-related filepath|/home/username/documents/project.docx|
|geo|string|False|IOC-related geo country code|us|
|industries|string|False|A comma-separated list of IOC-related industries|health,banking,finance|
|last_analyses|string|False|A comma-separated list of IOC-related analyses|https://app.any.run/tasks/f3ebe6be-3089-42ab-8c16-2477250b30bc,https://app.any.run/tasks/f3ebe6be-3089-42ab-8c16-2912250b30bc|
|last_modified|string|False|Last analysis date|2026-03-27 06:31:44|
|lookup_url|string|False|Link to the TI Lookup Query|https://intelligence.any.run/analysis/lookup#{%22query%22:%22http://171.22.28.221/5c06c05b7b34e8e6.php%22,%22dateRange%22:180}|
|md5|string|False|IOC-related MD5 hash|1f3870be274f6c49b3e31a0c6728957f|
|port|string|False|IOC-related port number|90|
|sha1|string|False|IOC-related SHA1 hash|a9993e364706816aba3e25717850c26c9cd0d89d|
|sha256|string|False|IOC-related SHA256 hash|ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad|
|ssdeep|string|False|IOC-related ssdeep|3072:aB...y:ab...y|
|tags|string|False|A comma-separated list of IOC-related tags|asyncrat,stealer,botnet|
|verdict|string|False|Analysis verdict. Can be 'Malicious', 'Suspicious' or 'No threads detected'|Malicious|
  
Example output:

```
{
  "asowner": "cloudflarenet",
  "file_extension": "exe",
  "filename": "passwords",
  "filepath": "/home/username/documents/project.docx",
  "geo": "us",
  "industries": "health,banking,finance",
  "last_analyses": "https://app.any.run/tasks/f3ebe6be-3089-42ab-8c16-2477250b30bc,https://app.any.run/tasks/f3ebe6be-3089-42ab-8c16-2912250b30bc",
  "last_modified": "2026-03-27 06:31:44",
  "lookup_url": "https://intelligence.any.run/analysis/lookup#{%22query%22:%22http://171.22.28.221/5c06c05b7b34e8e6.php%22,%22dateRange%22:180}",
  "md5": "1f3870be274f6c49b3e31a0c6728957f",
  "port": 90,
  "sha1": "a9993e364706816aba3e25717850c26c9cd0d89d",
  "sha256": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad",
  "ssdeep": "3072:aB...y:ab...y",
  "tags": "asyncrat,stealer,botnet",
  "verdict": "Malicious"
}
```

#### Linux File Analysis

This action is used to run File analysis using Linux VM

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|env_locale|string||False|Operation System language. Use locale identifier or country name Example - ( "en-US" or "Brazil"). Case insensitive|None|en-US|None|None|
|env_os|string|ubuntu|True|Operation System. Supports ubuntu, debian|["ubuntu", "debian"]|ubuntu|None|None|
|file_content|bytes|None|True|File bytes|None|bytes|None|None|
|filename|string|None|True|Filename|None|malware.zip|None|None|
|obj_ext_cmd|string|None|False|Optional command line|None|cmd|None|None|
|obj_ext_extension|boolean|True|False|Change extension to valid|None|True|None|None|
|obj_ext_startfolder|string|temp|False|Start object from|["", "desktop", "home", "downloads", "temp"]|temp|None|None|
|opt_auto_delete_after|string||False|Specify after what period of time this report should be deleted|["", "day", "week", "2 weeks", "month"]|month|None|None|
|opt_network_connect|boolean|True|False|Network connection state|None|True|None|None|
|opt_network_fakenet|boolean|False|False|FakeNet feature status|None|False|None|None|
|opt_network_geo|string||False|TOR geo location option|None|fastest|None|None|
|opt_network_mitm|boolean|False|False|HTTPS MITM proxy option|None|False|None|None|
|opt_network_residential_proxy|boolean|False|False|Residential Proxy option|None|False|None|None|
|opt_network_residential_proxy_geo|string||False|Residential Proxy Geo option|None|fastest|None|None|
|opt_network_tor|boolean|False|False|TOR using|None|False|None|None|
|opt_privacy_type|string|bylink|False|Privacy settings|["", "public", "bylink", "owner", "byteam"]|bylink|None|None|
|opt_timeout|integer|240|False|Timeout option, size range 10-660|None|240|None|None|
|run_as_root|boolean|True|False|Run file with superuser privileges|None|True|None|None|
|user_tags|string||False|Append User Tags to new analysis. Only characters a-z, A-Z, 0-9, hyphen (-), and comma (,) are allowed. Max tag length - 16 characters. Max unique tags per analysis - 8|None|insight-connect|None|None|
  
Example input:

```
{
  "env_locale": "",
  "env_os": "ubuntu",
  "file_content": "bytes",
  "filename": "malware.zip",
  "obj_ext_cmd": "cmd",
  "obj_ext_extension": true,
  "obj_ext_startfolder": "temp",
  "opt_auto_delete_after": "",
  "opt_network_connect": true,
  "opt_network_fakenet": false,
  "opt_network_geo": "",
  "opt_network_mitm": false,
  "opt_network_residential_proxy": false,
  "opt_network_residential_proxy_geo": "",
  "opt_network_tor": false,
  "opt_privacy_type": "bylink",
  "opt_timeout": 240,
  "run_as_root": true,
  "user_tags": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|analysis_url|string|False|Link to the interactive analysis|0cf223f2-530e-4a50-b68f-563045268648|
|analysis_uuid|string|False|Analysis UUID|0ec0a4cc-72a4-41b9-8a13-9f283b3b4e15|
  
Example output:

```
{
  "analysis_url": "0cf223f2-530e-4a50-b68f-563045268648",
  "analysis_uuid": "0ec0a4cc-72a4-41b9-8a13-9f283b3b4e15"
}
```

#### Linux URL Analysis

This action is used to run URL analysis using Linux VM

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|env_locale|string||False|Operation System language. Use locale identifier or country name Example - ( "en-US" or "Brazil"). Case insensitive|None|en-US|None|None|
|env_os|string|ubuntu|True|Operation System. Supports ubuntu, debian|["ubuntu", "debian"]|ubuntu|None|None|
|obj_ext_browser|string|Google Chrome|False|Browser name. Supports Google Chrome, Mozilla Firefox|["", "Google Chrome", "Mozilla Firefox"]|Google Chrome|None|None|
|obj_ext_extension|boolean|True|False|Change extension to valid|None|True|None|None|
|obj_url|string|None|True|Target URL. Size range 5-512. Example -> (http/https)://(your-link)|None|https://example.org|None|None|
|opt_auto_delete_after|string||False|Specify after what period of time this report should be deleted|["", "day", "week", "2 weeks", "month"]|month|None|None|
|opt_network_connect|boolean|True|False|Network connection state|None|True|None|None|
|opt_network_fakenet|boolean|False|False|FakeNet feature status|None|False|None|None|
|opt_network_geo|string||False|TOR geo location option|None|fastest|None|None|
|opt_network_mitm|boolean|False|False|HTTPS MITM proxy option|None|False|None|None|
|opt_network_residential_proxy|boolean|False|False|Residential Proxy option|None|False|None|None|
|opt_network_residential_proxy_geo|string||False|Residential Proxy Geo option|None|fastest|None|None|
|opt_network_tor|boolean|False|False|TOR using|None|False|None|None|
|opt_privacy_type|string|bylink|False|Privacy settings|["", "public", "bylink", "owner", "byteam"]|bylink|None|None|
|opt_timeout|integer|120|False|Timeout option, size range 10-660|None|120|None|None|
|user_tags|string||False|Append User Tags to new analysis. Only characters a-z, A-Z, 0-9, hyphen (-), and comma (,) are allowed. Max tag length - 16 characters. Max unique tags per analysis - 8|None|insight-connect|None|None|
  
Example input:

```
{
  "env_locale": "",
  "env_os": "ubuntu",
  "obj_ext_browser": "Google Chrome",
  "obj_ext_extension": true,
  "obj_url": "https://example.org",
  "opt_auto_delete_after": "",
  "opt_network_connect": true,
  "opt_network_fakenet": false,
  "opt_network_geo": "",
  "opt_network_mitm": false,
  "opt_network_residential_proxy": false,
  "opt_network_residential_proxy_geo": "",
  "opt_network_tor": false,
  "opt_privacy_type": "bylink",
  "opt_timeout": 120,
  "user_tags": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|analysis_url|string|False|Link to the interactive analysis|0cf223f2-530e-4a50-b68f-563045268648|
|analysis_uuid|string|False|Analysis UUID|0ec0a4cc-72a4-41b9-8a13-9f283b3b4e15|
  
Example output:

```
{
  "analysis_url": "0cf223f2-530e-4a50-b68f-563045268648",
  "analysis_uuid": "0ec0a4cc-72a4-41b9-8a13-9f283b3b4e15"
}
```

#### Windows File Analysis

This action is used to run File analysis using Windows VM

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|auto_confirm_uac|boolean|True|False|Auto confirm Windows UAC requests|None|True|None|None|
|env_bitness|int|64|True|Bitness of Operation System. Supports 32, 64 for Windows. 64 for Windows Server 2025|[32, 64]|64|None|None|
|env_locale|string||False|Operation System language. Use locale identifier or country name Example - ( "en-US" or "Brazil"). Case insensitive|None|en-US|None|None|
|env_type|string|complete|True|Environment preset type. You can select **development** env for OS Windows 10 x64. For all other cases, **complete** env is required|["complete", "development"]|complete|None|None|
|env_version|string|10|True|Version of OS. Supports 7, 10, 11, server 2025|["7", "10", "11", "server 2025"]|10|None|None|
|file_content|bytes|None|True|File bytes|None|bytes|None|None|
|filename|string|None|True|Filename|None|malware.zip|None|None|
|obj_ext_cmd|string|None|False|Optional command line|None|cmd|None|None|
|obj_ext_extension|boolean|True|False|Change extension to valid|None|True|None|None|
|obj_ext_startfolder|string|temp|False|Start object from|["", "desktop", "home", "downloads", "appdata", "temp", "windows", "root"]|temp|None|None|
|obj_force_elevation|boolean|True|False|Forces the file to execute with elevated privileges and an elevated token (for PE32, PE32+, PE64 files only)|None|True|None|None|
|opt_auto_delete_after|string||False|Specify after what period of time this report should be deleted|["", "day", "week", "2 weeks", "month"]|month|None|None|
|opt_network_connect|boolean|True|False|Network connection state|None|True|None|None|
|opt_network_fakenet|boolean|False|False|FakeNet feature status|None|False|None|None|
|opt_network_geo|string||False|TOR geo location option|None|fastest|None|None|
|opt_network_mitm|boolean|False|False|HTTPS MITM proxy option|None|False|None|None|
|opt_network_residential_proxy|boolean|False|False|Residential Proxy option|None|False|None|None|
|opt_network_residential_proxy_geo|string||False|Residential Proxy Geo option|None|fastest|None|None|
|opt_network_tor|boolean|False|False|TOR using|None|False|None|None|
|opt_privacy_type|string|bylink|False|Privacy settings|["", "public", "bylink", "owner", "byteam"]|bylink|None|None|
|opt_timeout|integer|240|False|Timeout option, size range 10-660|None|240|None|None|
|user_tags|string||False|Append User Tags to new analysis. Only characters a-z, A-Z, 0-9, hyphen (-), and comma (,) are allowed. Max tag length - 16 characters. Max unique tags per analysis - 8|None|insight-connect|None|None|
  
Example input:

```
{
  "auto_confirm_uac": true,
  "env_bitness": 64,
  "env_locale": "",
  "env_type": "complete",
  "env_version": 10,
  "file_content": "bytes",
  "filename": "malware.zip",
  "obj_ext_cmd": "cmd",
  "obj_ext_extension": true,
  "obj_ext_startfolder": "temp",
  "obj_force_elevation": true,
  "opt_auto_delete_after": "",
  "opt_network_connect": true,
  "opt_network_fakenet": false,
  "opt_network_geo": "",
  "opt_network_mitm": false,
  "opt_network_residential_proxy": false,
  "opt_network_residential_proxy_geo": "",
  "opt_network_tor": false,
  "opt_privacy_type": "bylink",
  "opt_timeout": 240,
  "user_tags": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|analysis_url|string|False|Link to the interactive analysis|0cf223f2-530e-4a50-b68f-563045268648|
|analysis_uuid|string|False|Analysis UUID|0ec0a4cc-72a4-41b9-8a13-9f283b3b4e15|
  
Example output:

```
{
  "analysis_url": "0cf223f2-530e-4a50-b68f-563045268648",
  "analysis_uuid": "0ec0a4cc-72a4-41b9-8a13-9f283b3b4e15"
}
```

#### Windows URL Analysis

This action is used to run URL analysis using Windows VM

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|env_bitness|int|64|True|Bitness of Operation System. Supports 32, 64 for Windows. 64 for Windows Server 2025|[32, 64]|64|None|None|
|env_locale|string||False|Operation System language. Use locale identifier or country name Example - ( "en-US" or "Brazil"). Case insensitive|None|en-US|None|None|
|env_type|string|complete|True|Environment preset type. You can select **development** env for OS Windows 10 x64. For all other cases, **complete** env is required|["complete", "development"]|complete|None|None|
|env_version|string|10|True|Version of OS. Supports 7, 10, 11, server 2025|["7", "10", "11", "server 2025"]|10|None|None|
|obj_ext_browser|string|Microsoft Edge|False|Browser name. Supports Google Chrome, Mozilla Firefox, Internet Explorer, Microsoft Edge for Windows 7, 10, 11. Microsoft Edge for Windows Server 2025|["", "Microsoft Edge", "Google Chrome", "Mozilla Firefox", "Internet Explorer"]|Microsoft Edge|None|None|
|obj_ext_extension|boolean|True|False|Change extension to valid|None|True|None|None|
|obj_url|string|None|True|Target URL. Size range 5-512. Example -> (http/https)://(your-link)|None|https://example.org|None|None|
|opt_auto_delete_after|string||False|Specify after what period of time this report should be deleted|["", "day", "week", "2 weeks", "month"]|month|None|None|
|opt_network_connect|boolean|True|False|Network connection state|None|True|None|None|
|opt_network_fakenet|boolean|False|False|FakeNet feature status|None|False|None|None|
|opt_network_geo|string||False|TOR geo location option|None|fastest|None|None|
|opt_network_mitm|boolean|False|False|HTTPS MITM proxy option|None|False|None|None|
|opt_network_residential_proxy|boolean|False|False|Residential Proxy option|None|False|None|None|
|opt_network_residential_proxy_geo|string||False|Residential Proxy Geo option|None|fastest|None|None|
|opt_network_tor|boolean|False|False|TOR using|None|False|None|None|
|opt_privacy_type|string|bylink|False|Privacy settings|["", "public", "bylink", "owner", "byteam"]|bylink|None|None|
|opt_timeout|integer|120|False|Timeout option, size range 10-660|None|120|None|None|
|user_tags|string||False|Append User Tags to new analysis. Only characters a-z, A-Z, 0-9, hyphen (-), and comma (,) are allowed. Max tag length - 16 characters. Max unique tags per analysis - 8|None|insight-connect|None|None|
  
Example input:

```
{
  "env_bitness": 64,
  "env_locale": "",
  "env_type": "complete",
  "env_version": 10,
  "obj_ext_browser": "Microsoft Edge",
  "obj_ext_extension": true,
  "obj_url": "https://example.org",
  "opt_auto_delete_after": "",
  "opt_network_connect": true,
  "opt_network_fakenet": false,
  "opt_network_geo": "",
  "opt_network_mitm": false,
  "opt_network_residential_proxy": false,
  "opt_network_residential_proxy_geo": "",
  "opt_network_tor": false,
  "opt_privacy_type": "bylink",
  "opt_timeout": 120,
  "user_tags": ""
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|analysis_url|string|False|Link to the interactive analysis|0cf223f2-530e-4a50-b68f-563045268648|
|analysis_uuid|string|False|Analysis UUID|0ec0a4cc-72a4-41b9-8a13-9f283b3b4e15|
  
Example output:

```
{
  "analysis_url": "0cf223f2-530e-4a50-b68f-563045268648",
  "analysis_uuid": "0ec0a4cc-72a4-41b9-8a13-9f283b3b4e15"
}
```
### Triggers


#### Get TI Feeds

This trigger is used to loads IPv4, URL, and Domain-Name indicators

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|feed_fetch_depth|integer|90|True|Specify feed fetch depth in days|None|90|None|None|
|feed_fetch_interval|integer|120|True|Specify feed fetch interval in minutes|None|120|None|None|
|threat_feed_access_key|string|None|True|Threat Feed Access Key|None|3b682134-c0f3-404d-84ba-34430df3e832|None|None|
  
Example input:

```
{
  "feed_fetch_depth": 90,
  "feed_fetch_interval": 120,
  "threat_feed_access_key": "3b682134-c0f3-404d-84ba-34430df3e832"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|anyrun_feed_domains|[]string|False|Domain-Name IOCs|["proxusert.com"]|
|anyrun_feed_ips|[]string|False|IPv4 IOCs|["172.217.6.14"]|
|anyrun_feed_urls|[]string|False|URL IOCs|["https://seatefitters.com/"]|
|threat_feed_access_key|string|True|Threat Feed Access Key|3b682134-c0f3-404d-84ba-34430df3e832|
  
Example output:

```
{
  "anyrun_feed_domains": [
    "proxusert.com"
  ],
  "anyrun_feed_ips": [
    "172.217.6.14"
  ],
  "anyrun_feed_urls": [
    "https://seatefitters.com/"
  ],
  "threat_feed_access_key": "3b682134-c0f3-404d-84ba-34430df3e832"
}
```
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
**hashes**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Head Hash|string|None|False|Head hash|None|
|MD5|string|None|False|MD5 hash|None|
|SHA1|string|None|False|SHA1 hash|None|
|SHA256|string|None|False|SHA256 hash|None|
|Ssdeep|string|None|False|Ssdeep hash|None|
  
**analysis**

|Name|Type|Default|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- | :--- |
|Date|string|None|True|Analysis date|2020-04-17 18:44:37.483000+00:00|
|File|string|None|True|Analysis file URL|https://content.any.run/tasks/0cb5990e-7858-4455-a5f8-8d704051901b/download/files/005d7277-b4c1-4b96-bcd9-ac02b799eec9|
|Hashes|hashes|None|True|Analysis hashes|None|
|JSON|string|None|True|Analysis JSON URL|https://api.any.run/report/0cb5990e-7858-4455-a5f8-8d704051901b/summary/json|
|MISP|string|None|True|Analysis MISP URL|https://api.any.run/report/0cb5990e-7858-4455-a5f8-8d704051901b/summary/misp|
|Name|string|None|True|Analysis name|setup.exe|
|PCAP|string|None|True|Analysis PCAP URL|https://content.any.run/tasks/0cb5990e-7858-4455-a5f8-8d704051901b/download/pcap|
|Related|string|None|True|Analysis related URL|https://app.any.run/tasks/0cb5990e-7858-4455-a5f8-8d704051901b|
|Tags|[]string|None|True|Analysis tags|["suspicious"]|
|UUID|string|None|False|Analysis UUID|None|
|Verdict|string|None|True|Analysis verdict|Malicious activity|


## Troubleshooting

* Configure the connection with either an API key without a prefix.

# Version History

* 4.0.0 - Add new trigger for the TI Feeds
* 3.0.0 - Migrate to the ANY.RUN SDK | Update existing actions | Add new actions
* 2.0.0 - Actions: `Get Report` - Updated output schema types | Updated SDK to the latest version (6.4.0)
* 1.1.2 - Fix issue with file defaulting to Windows 7 32-Bit
* 1.1.1 - Fix issue with invalid inputs in Run Analysis action | Fix issue where Run Analysis action fails if optional inputs are provided as empty strings | Fix issue where Get Report action fails when fields in output contain `None` value | Improve error handling
* 1.1.0 - Allow user agent input when using URL type in Run Analysis action
* 1.0.0 - Initial plugin

# Links

* [ANY.RUN](https://any.run/)

## References

* [ANY.RUN](https://any.run/)
* [ANY.RUN API documentation](https://any.run/api-documentation/)
* [ANY.RUN Integrations](https://any.run/integrations/)
* [ANY.RUN SDK](https://github.com/anyrun/anyrun-sdk)