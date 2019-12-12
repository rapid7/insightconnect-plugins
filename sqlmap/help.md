# Description

[SQLMap](http://sqlmap.org/) is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration tester and a broad range of switches lasting from database fingerprinting, over data fetching from the database, to accessing the underlying file system and executing commands on the operating system via out-of-band connections.

The SQLMap plugin allows you to scan targets and analyze the results.

# Key Features

* Scan a target

# Requirements

* Host and port of a target machine

# Documentation

## Setup

The connection configuration accepts the following parameters:
|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|host|string|None|False|Host of the REST-JSON API server (Default: localhost)|None|
|port|string|None|False|Port of the the REST-JSON API server, the default is 8775|None|

## Technical Details

### Actions

#### Scan

This action is used to perform a scan on a target.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|code|string|None|False|HTTP code to match when query is evaluated to True|None|
|getUsers|boolean|None|False|Enumerate DBMS users|None|
|getPasswordHashes|boolean|None|False|Enumerate DBMS users password hashes|None|
|excludeSysDbs|boolean|None|False|Exclude DBMS system databases when enumerating tables|None|
|uChar|string|None|False|Character to use for bruteforcing number of columns|None|
|regData|string|None|False|Windows registry key value data|None|
|prefix|string|None|False|Injection payload prefix string|None|
|googlePage|integer|None|False|Use Google dork results from specified page number|None|
|query|string|None|False|SQL statement to be executed|None|
|randomAgent|boolean|None|False|Use randomly selected HTTP User-Agent header value|None|
|aCert|bytes|None|False|HTTP authentication PEM cert/private key file|None|
|requestFile|bytes|None|False|Load HTTP request from a file|None|
|predictOutput|boolean|None|False|Predict common queries output|None|
|forms|boolean|None|False|Parse and test forms on target URL|None|
|skip|string|None|False|Skip testing for given parameter(s)|None|
|dropSetCookie|boolean|None|False|Ignore Set-Cookie header from response|None|
|smart|boolean|None|False|Conduct thorough tests only if positive heuristic(s)|None|
|risk|integer|None|False|Risk of tests to perform|[1, 2, 3]|
|sqlFile|bytes|None|False|Execute SQL statements from given file(s)|None|
|rParam|string|None|False|Randomly change value for given parameter(s)|None|
|db|string|None|False|DBMS database to enumerate|None|
|notString|string|None|False|String to match when query is evaluated to False|None|
|getRoles|string|None|False|Enumerate DBMS users roles|None|
|getPrivileges|boolean|None|False|Enumerate DBMS users privileges|None|
|testParameter|string|None|False|Testable parameter(s)|None|
|tbl|string|None|False|DBMS database table(s) to enumerate|None|
|charset|string|None|False|Blind SQL injection charset (e.g. '0123456789abcdef')|None|
|level|integer|None|False|Level of tests to perform|[1, 2, 3, 4, 5]|
|secondOrder|string|None|False|Resulting page URL searched for second-order response|None|
|pCred|string|None|False|Proxy authentication credentials (name\:password)|None|
|timeout|integer|None|False|Seconds to wait before timeout connection (default 30)|None|
|firstChar|string|None|False|First query output word character to retrieve|None|
|updateAll|boolean|None|False|Update SQLmap|None|
|binaryFields|string|None|False|Result fields having binary values (e.g. 'digest')|None|
|aType|string|None|False|HTTP authentication type (Basic, Digest, NTLM or PKI)|None|
|direct|string|None|False|Connection string for direct database connection|None|
|forceSsl|boolean|None|False|Force usage of SSL/HTTPS|None|
|saFreq|integer|None|False|Test requests between two visits to a given safe URL|None|
|titles|boolean|None|False|Compare pages based only on their titles|None|
|getSchema|boolean|None|False|Enumerate DBMS schema|None|
|identifyWaf|boolean|None|False|Connection string for direct database connection|None|
|checkWaf|boolean|None|False|Make a thorough testing for a WAF/IPS/IDS protection|None|
|regKey|string|None|False|Windows registry key|None|
|limitStart|string|None|False|First dump table entry to retrieve|None|
|loadCookies|bytes|None|False|File containing cookies in Netscape/wget format|None|
|dnsName|string|None|False|Domain name used for DNS exfiltration attack|None|
|csvDel|string|None|False|Delimiting character used in CSV output (default\: , )|None|
|osBof|boolean|None|False|Stored procedure buffer overflow exploitationn|None|
|invalidLogical|boolean|None|False|Use logical operations for invalidating values|None|
|getCurrentDb|boolean|None|False|Retrieve DBMS current database|None|
|hexConvert|boolean|None|False|Use DBMS hex function(s) for data retrieval|None|
|answers|string|None|False|Set question answers (e.g. 'quit=N,follow=N')|None|
|dependencies|boolean|None|False|Check for missing (non-core) SQLmap dependencies|None|
|threads|integer|None|False|Max number of concurrent HTTP(s) requests|None|
|proxy|string|None|False|Use a proxy to connect to the target URL|None|
|regexp|string|None|False|Regexp to match when query is evaluated to True|None|
|optimize|boolean|None|False|Turn on all optimization switches|None|
|limitStop|string|None|False|Last dump table entry to retrieve|None|
|mnemonics|string|None|False|Use short mnemonics (e.g. 'flu,bat,ban,tec=EU')|None|
|uFrom|string|None|False|Table to use in FROM part of UNION query SQL injection|None|
|noCast|boolean|None|False|Turn off payload casting mechanism|None|
|testFilter|string|None|False|Select tests by payloads and/or titles (e.g. ROW)|None|
|eta|boolean|None|False|Display for each output the estimated time of arrival|None|
|cookie|string|None|False|HTTP Cookie header value|None|
|logFile|bytes|None|False|Parse target(s) from Burp or WebScarab proxy log file|None|
|os|string|None|False|Force back-end DBMS operating system to this value|None|
|col|string|None|False|DBMS database table column(s) to enumerate|None|
|rFile|string|None|False|Read a file from the back-end DBMS file system|None|
|verbose|integer|None|False|Verbosity level|[0, 1, 2, 3, 4, 5, 6]|
|crawlDepth|integer|None|False|Crawl the website starting from the target URL|[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]|
|privEsc|boolean|None|False|Database process user privilege escalation|None|
|forceDns|boolean|None|False|Force DNS|None|
|getAll|boolean|None|False|Retrieve everything|None|
|url|string|None|False|Target URL (e.g. 'http\://www.site.com/vuln.php?id=1')|None|
|invalidBignum|boolean|None|False|Use big numbers for invalidating values|None|
|regType|string|None|False|Windows registry key value type|None|
|getDbs|boolean|None|False|Enumerate DBMS databases|None|
|freshQueries|boolean|None|False|Ignore query results stored in session file|None|
|uCols|string|None|False|Range of columns to test for UNION query SQL injection|None|
|pDel|string|None|False|Character used for splitting parameter values|None|
|wFile|string|None|False|Write a local file on the back-end DBMS file system|None|
|udfInject|boolean|None|False|Inject custom user-defined functions|None|
|configFile|bytes|None|False|Load options from a configuration INI file|None|
|scope|string|None|False|Regexp to filter targets from provided proxy log|None|
|dumpAll|boolean|None|False|Dump all DBMS databases tables entries|None|
|isDba|boolean|None|False|Detect if the DBMS current user is DBA|None|
|regVal|string|None|False|Windows registry key value|None|
|dummy|boolean|None|False|Dummy parameter value|None|
|commonTables|boolean|None|False|Check existence of common tables|None|
|search|boolean|False|False|Search column(s), table(s) and/or database name(s)|None|
|skipUrlEncode|boolean|False|False|Skip URL encoding of payload data|None|
|referer|string|None|False|HTTP Referer header value|None|
|purgeOutput|boolean|False|False|Safely remove all content from output directory|None|
|retries|integer|3|False|Retries when the connection timeouts|None|
|extensiveFp|boolean|False|False|Perform an extensive DBMS version fingerprint|None|
|dumpTable|boolean|False|False|Dump DBMS database table entries|None|
|database|boolean|None|False|DBMS database to enumerate|None|
|batch|boolean|True|False|Never ask for user input, use the default behaviour|None|
|headers|object|None|False|Extra headers (e.g. 'Accept-Language\: fr ETag\: 123')|None|
|flushSession|boolean|False|False|Flush session files for current target|None|
|osCmd|string|None|False|Execute an operating system command|None|
|suffix|string|None|False|Injection payload suffix string|None|
|dbmsCred|string|None|False|DBMS authentication credentials (user\:password)|None|
|regDel|boolean|False|False|Delete a Windows registry key value|None|
|shLib|string|None|False|Local path of the shared library|None|
|nullConnection|boolean|False|False|Retrieve page length without actual HTTP response body|None|
|timeSec|integer|5|False|Seconds to delay the DBMS response (default 5)|None|
|getHostname|boolean|False|False|Retrieve DBMS server hostname|None|
|sessionFile|bytes|None|False|Load session from a stored (.sqlite) file|None|
|noEscape|boolean|False|False|Turn off string escaping mechanism|None|
|getTables|boolean|False|False|Enumerate DBMS database tables|None|
|agent|string|None|False|HTTP User-Agent header value|None|
|lastChar|string|None|False|Last query output word character to retrieve|None|
|string|string|None|False|String to match when query is evaluated to True|None|
|dbms|string|None|False|Force back-end DBMS to this value|None|
|tamper|string|None|False|Use given script(s) for tampering injection data|None|
|hpp|boolean|False|False|Use HTTP parameter pollution method|None|
|delay|integer|None|False|Delay in seconds between each HTTP request|None|
|evalCode|string|None|False|Evaluate provided Python code before the request (e.g.'import hashlib;id2=hashlib.md5(id).hexdigest()')|None|
|cleanup|boolean|False|False|Clean up the DBMS from SQLmap specific UDF and tables|None|
|getBanner|boolean|False|False|Retrieve DBMS banner|None|
|regRead|boolean|False|False|Read a Windows registry key value|None|
|bulkFile|bytes|None|False|Scan multiple targets given in a textual file|None|
|safUrl|string|None|False|URL address to visit frequently during testing|None|
|getCurrentUser|boolean|None|False|Retrieve DBMS current user|None|
|dumpFormat|string|CSV|False|Format of dumped data|['CSV', 'HTML', 'SQLITE']|
|alert|string|None|False|Run host OS command(s) when SQL injection is found|None|
|host|string|None|False|HTTP Host header value|None|
|user|string|None|False|DBMS user to enumerate|None|
|parseErrors|boolean|False|False|Parse and display DBMS error messages from responses|None|
|aCred|string|None|False|HTTP authentication credentials (name\:password)|None|
|getCount|boolean|False|False|Retrieve number of entries for table(s)|None|
|dFile|string|None|False|Back-end DBMS absolute filepath to write to|None|
|data|string|None|False|Data string to be sent through POST|None|
|regAdd|boolean|None|False|Write a Windows registry key value data|None|
|ignoreProxy|boolean|None|False|Ignore system default proxy settings|None|
|getColumns|boolean|None|False|Enumerate DBMS database table columns|None|
|mobile|boolean|None|False|Imitate smartphone through HTTP User-Agent header|None|
|googleDork|string|None|False|Process Google dork results as target URLs|None|
|tech|string|None|False|SQL injection techniques to use (default 'BEUSTQ')|None|
|textOnly|boolean|None|False|Compare pages based only on the textual content|None|
|commonColumns|string|None|False|Check existence of common columns|None|
|keepAlive|boolean|None|False|Use persistent HTTP(s) connections|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|scan|object|False|Scan Complete|

Example output:

```

{
  "log": [
    {
      "message": "GET parameter 'Submit' does not seem to be injectable",
      "time": "15:24:29",
      "level": "WARNING"
    },
    {
      "message": "all tested parameters do not appear to be injectable. Try to increase values for '--level'/'--risk' options if you wish to perform more tests. If you suspect that there is some kind of protection mechanism involved (e.g. WAF) maybe you could try to use option '--tamper' (e.g. '--tamper=space2comment')",
      "time": "15:24:29",
      "level": "CRITICAL"
    }
  ]
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

To troubleshoot SQLmap, look at the INFO logs that are printed to see where the plugin failed.

# Version History

* 1.1.1 - New spec and help.md format for the Hub
* 1.1.0 - Support web server mode
* 1.0.0 - Initial plugin

# Links

## References

* [SQLmap](https://github.com/sqlmapproject/sqlmap)
* [Unofficial SQLmap API Documentation](http://volatile-minds.blogspot.com/2013/04/unofficial-sqlmap-restful-api.html)
* [DVWA](http://www.dvwa.co.uk/)

