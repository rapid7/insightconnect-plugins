# Description

[SQLMap](http://sqlmap.org/) is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration tester and a broad range of switches lasting from database fingerprinting, over data fetching from the database, to accessing the underlying file system and executing commands on the operating system via out-of-band connections. The SQLMap plugin allows you to scan targets and analyze the results

# Key Features

* Scan a target for SQL injection vulnerabilities
* Automate detection and exploitation of SQL injection flaws
* Database fingerprinting and data extraction
* Access underlying file system and execute OS commands

# Requirements

* Host and port of a target machine

# Supported Product Versions

* SQLMAP 2026-03-13

# Documentation

## Setup

The connection configuration accepts the following parameters:  

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|api_host|string|localhost|False|Host of the REST-JSON API server|None|localhost|None|None|
|api_port|string|8775|False|Port of the the REST-JSON API server|None|8775|None|None|

Example input:

```
{
  "api_host": "localhost",
  "api_port": 8775
}
```

## Technical Details

### Actions


#### Scan

This action is used to performs a SQLmap scan on target

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|aCert|bytes|None|False|HTTP authentication PEM cert/private key file|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|None|None|
|aCred|string|None|False|HTTP authentication credentials|None|username:password|None|None|
|aType|string|None|False|HTTP authentication type (Basic, Digest, NTLM or PKI)|None|Basic|None|None|
|agent|string|None|False|HTTP User-Agent header value|None|Mozilla/5.0|None|None|
|alert|string|None|False|Run host OS command(s) when SQL injection is found|None|python3 alert_script.py|None|None|
|answers|string|None|False|Set question answers|None|quit=N,follow=N|None|None|
|batch|boolean|True|False|Never ask for user input, use the default behaviour|None|True|None|None|
|binaryFields|string|None|False|Result fields having binary values|None|digest|None|None|
|bulkFile|bytes|None|False|Scan multiple targets given in a textual file|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|None|None|
|charset|string|None|False|Blind SQL injection charset|None|0123456789abcdef|None|None|
|checkWaf|boolean|None|False|Make a thorough testing for a WAF/IPS/IDS protection|None|False|None|None|
|cleanup|boolean|False|False|Clean up the DBMS from SQLmap specific UDF and tables|None|False|None|None|
|code|string|None|False|HTTP code to match when query is evaluated to True|None|200|None|None|
|col|string|None|False|DBMS database table column(s) to enumerate|None|column1|None|None|
|commonColumns|string|None|False|Check existence of common columns|None|common column|None|None|
|commonTables|boolean|None|False|Check existence of common tables|None|False|None|None|
|configFile|bytes|None|False|Load options from a configuration INI file|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|None|None|
|cookie|string|None|False|HTTP Cookie header value|None|name=value|None|None|
|crawlDepth|integer|1|False|Crawl the website starting from the target URL|[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]|1|None|None|
|csvDel|string|,|False|Delimiting character used in CSV output|None|,|None|None|
|dFile|string|None|False|Back-end DBMS absolute filepath to write to|None|/users/user1/docs/file.txt|None|None|
|data|string|None|False|Data string to be sent through POST|None|data1|None|None|
|database|boolean|None|False|DBMS database to enumerate|None|False|None|None|
|db|string|None|False|DBMS database to enumerate|None|db1|None|None|
|dbms|string|None|False|Force back-end DBMS to this value|None|value1|None|None|
|dbmsCred|string|None|False|DBMS authentication credentials|None|user:password|None|None|
|delay|integer|None|False|Delay in seconds between each HTTP request|None|0|None|None|
|dependencies|boolean|None|False|Check for missing (non-core) SQLmap dependencies|None|False|None|None|
|direct|string|None|False|Connection string for direct database connection|None|direct_string|None|None|
|dnsName|string|None|False|Domain name used for DNS exfiltration attack|None|example.com|None|None|
|dropSetCookie|boolean|None|False|Ignore Set-Cookie header from response|None|False|None|None|
|dummy|boolean|None|False|Dummy parameter value|None|False|None|None|
|dumpAll|boolean|None|False|Dump all DBMS databases tables entries|None|False|None|None|
|dumpFormat|string|CSV|False|Format of dumped data|["CSV", "HTML", "SQLITE"]|CSV|None|None|
|dumpTable|boolean|False|False|Dump DBMS database table entries|None|False|None|None|
|eta|boolean|None|False|Display for each output the estimated time of arrival|None|False|None|None|
|evalCode|string|None|False|Evaluate provided Python code before the request|None|import hashlib;id2=hashlib.md5(id).hexdigest()|None|None|
|excludeSysDbs|boolean|None|False|Exclude DBMS system databases when enumerating tables|None|False|None|None|
|extensiveFp|boolean|False|False|Perform an extensive DBMS version fingerprint|None|False|None|None|
|firstChar|string|None|False|First query output word character to retrieve|None|a|None|None|
|flushSession|boolean|False|False|Flush session files for current target|None|False|None|None|
|forceDns|boolean|None|False|Force DNS|None|False|None|None|
|forceSsl|boolean|None|False|Force usage of SSL/HTTPS|None|False|None|None|
|forms|boolean|None|False|Parse and test forms on target URL|None|False|None|None|
|freshQueries|boolean|None|False|Ignore query results stored in session file|None|False|None|None|
|getAll|boolean|None|False|Retrieve everything|None|False|None|None|
|getBanner|boolean|False|False|Retrieve DBMS banner|None|False|None|None|
|getColumns|boolean|None|False|Enumerate DBMS database table columns|None|False|None|None|
|getCount|boolean|False|False|Retrieve number of entries for table(s)|None|False|None|None|
|getCurrentDb|boolean|None|False|Retrieve DBMS current database|None|False|None|None|
|getCurrentUser|boolean|None|False|Retrieve DBMS current user|None|False|None|None|
|getDbs|boolean|None|False|Enumerate DBMS databases|None|False|None|None|
|getHostname|boolean|False|False|Retrieve DBMS server hostname|None|False|None|None|
|getPasswordHashes|boolean|None|False|Enumerate DBMS users password hashes|None|False|None|None|
|getPrivileges|boolean|None|False|Enumerate DBMS users privileges|None|False|None|None|
|getRoles|string|None|False|Enumerate DBMS users roles|None|role1|None|None|
|getSchema|boolean|None|False|Enumerate DBMS schema|None|False|None|None|
|getTables|boolean|False|False|Enumerate DBMS database tables|None|False|None|None|
|getUsers|boolean|None|False|Enumerate DBMS users|None|False|None|None|
|googleDork|string|None|False|Process Google dork results as target URLs|None|googleDork string|None|None|
|googlePage|integer|None|False|Use Google dork results from specified page number|None|1|None|None|
|headers|object|None|False|Extra headers as a JSON object|None|{"Accept-Language": "fr","ETag": 123}|None|None|
|hexConvert|boolean|None|False|Use DBMS hex function(s) for data retrieval|None|False|None|None|
|host|string|None|False|HTTP Host header value|None|localhost|None|None|
|hpp|boolean|False|False|Use HTTP parameter pollution method|None|False|None|None|
|identifyWaf|boolean|None|False|Connection string for direct database connection|None|False|None|None|
|ignoreProxy|boolean|None|False|Ignore system default proxy settings|None|False|None|None|
|invalidBignum|boolean|None|False|Use big numbers for invalidating values|None|False|None|None|
|invalidLogical|boolean|None|False|Use logical operations for invalidating values|None|False|None|None|
|isDba|boolean|None|False|Detect if the DBMS current user is DBA|None|False|None|None|
|keepAlive|boolean|None|False|Use persistent HTTP(s) connections|None|False|None|None|
|lastChar|string|None|False|Last query output word character to retrieve|None|a|None|None|
|level|integer|1|False|Level of tests to perform|[1, 2, 3, 4, 5]|1|None|None|
|limitStart|string|None|False|First dump table entry to retrieve|None|table1|None|None|
|limitStop|string|None|False|Last dump table entry to retrieve|None|table2|None|None|
|loadCookies|bytes|None|False|File containing cookies in Netscape/wget format|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|None|None|
|logFile|bytes|None|False|Parse target(s) from Burp or WebScarab proxy log file|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|None|None|
|mnemonics|string|None|False|Use short mnemonics|None|flu,bat,ban,tec=EU|None|None|
|mobile|boolean|None|False|Imitate smartphone through HTTP User-Agent header|None|False|None|None|
|noCast|boolean|None|False|Turn off payload casting mechanism|None|False|None|None|
|noEscape|boolean|False|False|Turn off string escaping mechanism|None|False|None|None|
|notString|string|None|False|String to match when query is evaluated to False|None|match|None|None|
|nullConnection|boolean|False|False|Retrieve page length without actual HTTP response body|None|False|None|None|
|optimize|boolean|None|False|Turn on all optimization switches|None|False|None|None|
|os|string|None|False|Force back-end DBMS operating system to this value|None|Windows10|None|None|
|osBof|boolean|None|False|Stored procedure buffer overflow exploitation|None|False|None|None|
|osCmd|string|None|False|Execute an operating system command|None|cd ~/dir1|None|None|
|pCred|string|None|False|Proxy authentication credentials|None|name:password|None|None|
|pDel|string|None|False|Character used for splitting parameter values|None|,|None|None|
|parseErrors|boolean|False|False|Parse and display DBMS error messages from responses|None|False|None|None|
|predictOutput|boolean|None|False|Predict common queries output|None|False|None|None|
|prefix|string|None|False|Injection payload prefix string|None|--prefix|None|None|
|privEsc|boolean|None|False|Database process user privilege escalation|None|False|None|None|
|proxy|string|None|False|Use a proxy to connect to the target URL|None|proxy|None|None|
|purgeOutput|boolean|False|False|Safely remove all content from output directory|None|False|None|None|
|query|string|None|False|SQL statement to be executed|None|SELECT * FROM table_name;|None|None|
|rFile|string|None|False|Read a file from the back-end DBMS file system|None|file.txt|None|None|
|rParam|string|None|False|Randomly change value for given parameter(s)|None|param1|None|None|
|randomAgent|boolean|None|False|Use randomly selected HTTP User-Agent header value|None|False|None|None|
|referer|string|None|False|HTTP Referer header value|None|HTTP Referer|None|None|
|regAdd|boolean|None|False|Write a Windows registry key value data|None|False|None|None|
|regData|string|None|False|Windows registry key value data|None|key:value|None|None|
|regDel|boolean|False|False|Delete a Windows registry key value|None|False|None|None|
|regKey|string|None|False|Windows registry key|None|win10RegKey|None|None|
|regRead|boolean|False|False|Read a Windows registry key value|None|False|None|None|
|regType|string|None|False|Windows registry key value type|None|reg type|None|None|
|regVal|string|None|False|Windows registry key value|None|key:value|None|None|
|regexp|string|None|False|Regex to match when query is evaluated to True|None|^The|None|None|
|requestFile|bytes|None|False|Load HTTP request from a file|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|None|None|
|retries|integer|3|False|Retries when the connection timeouts|None|3|None|None|
|risk|integer|1|False|Risk of tests to perform|[1, 2, 3]|1|None|None|
|saFreq|integer|0|False|Test requests between two visits to a given safe URL|None|0|None|None|
|safUrl|string|None|False|URL address to visit frequently during testing|None|https://www.example.com|None|None|
|scope|string|None|False|Regex to filter targets from provided proxy log|None|^The|None|None|
|search|boolean|False|False|Search column(s), table(s) and/or database name(s)|None|False|None|None|
|secondOrder|string|None|False|Resulting page URL searched for second-order response|None|https://www.example.com|None|None|
|sessionFile|bytes|None|False|Load session from a stored (.sqlite) file|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|None|None|
|shLib|string|None|False|Local path of the shared library|None|Network/SharedResources/SharedLibrary|None|None|
|skip|string|None|False|Skip testing for given parameter(s)|None|param1|None|None|
|skipUrlEncode|boolean|False|False|Skip URL encoding of payload data|None|False|None|None|
|smart|boolean|None|False|Conduct thorough tests only if positive heuristic(s)|None|False|None|None|
|sqlFile|bytes|None|False|Execute SQL statements from given file(s)|None|UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==|None|None|
|string|string|None|False|String to match when query is evaluated to True|None|match|None|None|
|suffix|string|None|False|Injection payload suffix string|None|--suffix|None|None|
|tamper|string|None|False|Use given script(s) for tampering injection data|None|script string|None|None|
|tbl|string|None|False|DBMS database table(s) to enumerate|None|table1|None|None|
|tech|string|BEUSTQ|False|SQL injection techniques to use (default 'BEUSTQ')|None|BEUSTQ|None|None|
|testFilter|string|None|False|Select tests by payloads and/or titles|None|ROW|None|None|
|testParameter|string|None|False|Testable parameter(s)|None|param1|None|None|
|textOnly|boolean|None|False|Compare pages based only on the textual content|None|False|None|None|
|threads|integer|None|False|Max number of concurrent HTTP(s) requests|None|1|None|None|
|timeSec|integer|5|False|Seconds to delay the DBMS response (default 5)|None|5|None|None|
|timeout|integer|30|False|Seconds to wait before timeout connection (default 30)|None|30|None|None|
|titles|boolean|None|False|Compare pages based only on their titles|None|False|None|None|
|uChar|string|None|False|Character to use for brute-forcing number of columns|None|a|None|None|
|uCols|string|None|False|Range of columns to test for UNION query SQL injection|None|C1,C2|None|None|
|uFrom|string|None|False|Table to use in FROM part of UNION query SQL injection|None|table1|None|None|
|udfInject|boolean|None|False|Inject custom user-defined functions|None|False|None|None|
|updateAll|boolean|None|False|Update SQLmap|None|False|None|None|
|url|string|None|False|Target URL|None|https://www.example.com|None|None|
|user|string|None|False|DBMS user to enumerate|None|user1|None|None|
|verbose|integer|1|False|Verbosity level|[1, 2, 3, 4, 5, 6]|1|None|None|
|wFile|string|None|False|Write a local file on the back-end DBMS file system|None|file.txt|None|None|
  
Example input:

```
{
  "aCert": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "aCred": "username:password",
  "aType": "Basic",
  "agent": "Mozilla/5.0",
  "alert": "python3 alert_script.py",
  "answers": "quit=N,follow=N",
  "batch": true,
  "binaryFields": "digest",
  "bulkFile": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "charset": "0123456789abcdef",
  "checkWaf": false,
  "cleanup": false,
  "code": 200,
  "col": "column1",
  "commonColumns": "common column",
  "commonTables": false,
  "configFile": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "cookie": "name=value",
  "crawlDepth": 1,
  "csvDel": ",",
  "dFile": "/users/user1/docs/file.txt",
  "data": "data1",
  "database": false,
  "db": "db1",
  "dbms": "value1",
  "dbmsCred": "user:password",
  "delay": 0,
  "dependencies": false,
  "direct": "direct_string",
  "dnsName": "example.com",
  "dropSetCookie": false,
  "dummy": false,
  "dumpAll": false,
  "dumpFormat": "CSV",
  "dumpTable": false,
  "eta": false,
  "evalCode": "import hashlib;id2=hashlib.md5(id).hexdigest()",
  "excludeSysDbs": false,
  "extensiveFp": false,
  "firstChar": "a",
  "flushSession": false,
  "forceDns": false,
  "forceSsl": false,
  "forms": false,
  "freshQueries": false,
  "getAll": false,
  "getBanner": false,
  "getColumns": false,
  "getCount": false,
  "getCurrentDb": false,
  "getCurrentUser": false,
  "getDbs": false,
  "getHostname": false,
  "getPasswordHashes": false,
  "getPrivileges": false,
  "getRoles": "role1",
  "getSchema": false,
  "getTables": false,
  "getUsers": false,
  "googleDork": "googleDork string",
  "googlePage": 1,
  "headers": {
    "Accept-Language": "fr",
    "ETag": 123
  },
  "hexConvert": false,
  "host": "localhost",
  "hpp": false,
  "identifyWaf": false,
  "ignoreProxy": false,
  "invalidBignum": false,
  "invalidLogical": false,
  "isDba": false,
  "keepAlive": false,
  "lastChar": "a",
  "level": 1,
  "limitStart": "table1",
  "limitStop": "table2",
  "loadCookies": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "logFile": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "mnemonics": "flu,bat,ban,tec=EU",
  "mobile": false,
  "noCast": false,
  "noEscape": false,
  "notString": "match",
  "nullConnection": false,
  "optimize": false,
  "os": "Windows10",
  "osBof": false,
  "osCmd": "cd ~/dir1",
  "pCred": "name:password",
  "pDel": ",",
  "parseErrors": false,
  "predictOutput": false,
  "prefix": "--prefix",
  "privEsc": false,
  "proxy": "proxy",
  "purgeOutput": false,
  "query": "SELECT * FROM table_name;",
  "rFile": "file.txt",
  "rParam": "param1",
  "randomAgent": false,
  "referer": "HTTP Referer",
  "regAdd": false,
  "regData": "key:value",
  "regDel": false,
  "regKey": "win10RegKey",
  "regRead": false,
  "regType": "reg type",
  "regVal": "key:value",
  "regexp": "^The",
  "requestFile": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "retries": 3,
  "risk": 1,
  "saFreq": 0,
  "safUrl": "https://www.example.com",
  "scope": "^The",
  "search": false,
  "secondOrder": "https://www.example.com",
  "sessionFile": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "shLib": "Network/SharedResources/SharedLibrary",
  "skip": "param1",
  "skipUrlEncode": false,
  "smart": false,
  "sqlFile": "UmFwaWQ3IEluc2lnaHRDb25uZWN0Cg==",
  "string": "match",
  "suffix": "--suffix",
  "tamper": "script string",
  "tbl": "table1",
  "tech": "BEUSTQ",
  "testFilter": "ROW",
  "testParameter": "param1",
  "textOnly": false,
  "threads": 1,
  "timeSec": 5,
  "timeout": 30,
  "titles": false,
  "uChar": "a",
  "uCols": "C1,C2",
  "uFrom": "table1",
  "udfInject": false,
  "updateAll": false,
  "url": "https://www.example.com",
  "user": "user1",
  "verbose": 1,
  "wFile": "file.txt"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|result|object|False|Scan Complete|{}|
  
Example output:

```
{
  "result": {}
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* To troubleshoot SQLmap, look at the INFO logs that are printed to see where the plugin failed

# Version History

* 2.0.1 - Updated SDK to the latest version (6.4.3)
* 2.0.0 - Changed SDK from Komand to ICON | Updated requests version to 2.20.0 | Added examples and required defaults
* 1.1.1 - New spec and help.md format for the Extension Library
* 1.1.0 - Support web server mode
* 1.0.0 - Initial plugin

# Links

* [SQLMap](http://sqlmap.org/)

## References

* [SQLmap GitHub](https://github.com/sqlmapproject/sqlmap)
* [Unofficial SQLmap API Documentation](http://volatile-minds.blogspot.com/2013/04/unofficial-sqlmap-restful-api.html)
* [DVWA](http://www.dvwa.co.uk/)