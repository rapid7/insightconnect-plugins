# Description

The DNS plugin is used for forward and reverse DNS lookups. This plugin uses [Dig](https://linux.die.net/man/1/dig), or Domain Information Groper, which is a network administration command-line tool for querying Domain Name System (DNS) name servers

# Key Features

* Forward DNS lookup to find an IP address from a domain name
* Reverse DNS lookup to find a domain name from an IP address

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2024-09-10

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Forward Lookup
  
This action is used to request a forward lookup for a domain

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|domain|string|None|True|Domain name to resolve|None|rapid7.com|None|None|
|query|string|None|True|Query type e.g. ANY, A, MX, NS, etc|["A", "AAAA", "ANY", "CNAME", "MX", "NS", "PTR", "SOA"]|MX|None|None|
|resolver|string|None|False|Resolver. Leave blank to use default resolver for the system|None|8.8.8.8|None|None|
  
Example input:

```
{
  "domain": "rapid7.com",
  "query": "MX",
  "resolver": "8.8.8.8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|all_answers|[]string|False|A list of all answers found|["172.217.6.14"]|
|answer|string|False|Answer received|172.217.6.14|
|fulloutput|string|False|Full DNS output|\n; <<>> DiG 9.12.4-P2 <<>> google.com A\n;; global ...|
|last_answer|string|False|The last answer found in the answers section|172.217.6.14|
|nameserver|string|False|Nameserver that fulfilled request|192.168.65.1|
|question|string|False|Question asked|google.com|
|status|string|False|Query status [ NOERROR | FORMERR | NXDOMAIN | SERVFAIL | REFUSED ...]|NOERROR|
  
Example output:

```
{
  "all_answers": [
    "172.217.6.14"
  ],
  "answer": "172.217.6.14",
  "fulloutput": "\\n; <<>> DiG 9.12.4-P2 <<>> google.com A\\n;; global ...",
  "last_answer": "172.217.6.14",
  "nameserver": "192.168.65.1",
  "question": "google.com",
  "status": "NOERROR"
}
```

#### Reverse Lookup
  
This action is used to request a reverse lookup for an IP address

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|address|string|None|True|Internet address to resolve|None|1.2.3.4|None|None|
|resolver|string|None|False|Resolver. Leave blank to use default resolver for the system|None|8.8.8.8|None|None|
  
Example input:

```
{
  "address": "1.2.3.4",
  "resolver": "8.8.8.8"
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|answer|string|False|Answer received|google-public-dns-a.google.com|
|fulloutput|string|False|Full DNS output|\n; <<>> Dig 9.9.5-9+deb8u9-Debian <<>> -x 8.8.8.8\n;; global options: +cmd\n;; Got answer:\n;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 59406\n;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1\n\n;; OPT PSEUDOSECTION:\n; EDNS: version: 0, flags:; udp: 512\n;; QUESTION SECTION:\n;8.8.8.8.in-addr.arpa.\t\tIN\tPTR\n\n;; ANSWER SECTION:\n8.8.8.8.in-addr.arpa.\t68133\tIN\tPTR\tgoogle-public-dns-a.google.com.\n\n;; Query time: 22 msec\n;; SERVER: 10.0.2.3#53(10.0.2.3)\n;; WHEN: Thu Jan 26 23:43:43 UTC 2017\n;; MSG SIZE  rcvd: 93\n\n|
|nameserver|string|False|Nameserver that fulfilled request|10.0.2.3|
|question|string|False|Question asked|8.8.8.8|
|status|string|False|Query status [ NOERROR | FORMERR | NXDOMAIN | SERVFAIL | REFUSED ...]|NOERROR|
  
Example output:

```
{
  "answer": "google-public-dns-a.google.com",
  "fulloutput": "\\n; <<>> Dig 9.9.5-9+deb8u9-Debian <<>> -x 8.8.8.8\\n;; global options: +cmd\\n;; Got answer:\\n;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 59406\\n;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1\\n\\n;; OPT PSEUDOSECTION:\\n; EDNS: version: 0, flags:; udp: 512\\n;; QUESTION SECTION:\\n;8.8.8.8.in-addr.arpa.\\t\\tIN\\tPTR\\n\\n;; ANSWER SECTION:\\n8.8.8.8.in-addr.arpa.\\t68133\\tIN\\tPTR\\tgoogle-public-dns-a.google.com.\\n\\n;; Query time: 22 msec\\n;; SERVER: 10.0.2.3#53(10.0.2.3)\\n;; WHEN: Thu Jan 26 23:43:43 UTC 2017\\n;; MSG SIZE  rcvd: 93\\n\\n",
  "nameserver": "10.0.2.3",
  "question": "8.8.8.8",
  "status": "NOERROR"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting

* The `status` variable contains the [DNS status code](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml) name from the DNS server's response.
Dig has at least the following status codes implemented:

```
NOERROR
FORMERR
SERVFAIL
NXDOMAIN
NOTIMP
REFUSED
YXDOMAIN 
YXRRSET
NXRRSET
NOTAUTH
NOTZONE
BADVERS
```

You can test the `status` variable in a Decision or Filter step to check for its value.
For example, in your workflow, if the resolution doesn't return an answer, then you may want to attempt a second lookup from a passive DNS service.

Common examples:

* `status = "NOERRROR"` - The DNS response contains an answer
* `status = "NXDOMAIN"` - The DNS response did not have an answer i.e. Non-Existent Domain

# Version History

* 2.0.6 - Updated SDK to the latest version (6.3.10)
* 2.0.5 - Updated SDK to the latest version (6.2.5)
* 2.0.4 - Updated SDK to the latest version (v6.2.2) | Address vulnerabilities
* 2.0.3 - Initial updates for fedramp compliance | Updated SDK to the latest
* 2.0.2 - Updated SDK to the latest version | Added validation for input parameters
* 2.0.1 - Added `__init__.py` file to `unit_test` folder | Refreshed with new Tooling
* 2.0.0 - Rename Dig plugin to DNS
* 1.0.7 - Fix bug in `safe_parse` function | Fix bug when `answers` in function `execute_command` is str
* 1.0.6 - Upgrade to latest Python plugin runtime | Define `cloud_ready` in spec
* 1.0.5 - Update to v4 Python plugin runtime
* 1.0.4 - Add example inputs
* 1.0.3 - Use input and output constants | Change docker image from `komand/python-2-slim-plugin:2` to `komand/python-3-37-slim-plugin:3` to reduce plugin image size | Added "f" strings | Remove duplicate code | Add user nobody to Dockerfile
* 1.0.2 - New spec and help.md format for the Extension Library
* 1.0.1 - Update to use the `komand/python-2-slim-plugin:2` Docker image to reduce plugin size
* 1.0.0 - Support web server mode
* 0.3.2 - Update to v2 Python plugin architecture
* 0.3.1 - SSL bug fix in SDK
* 0.3.0 - Add all_answers and last_answer to the forward lookup action
* 0.2.0 - Add option to use custom resolver
* 0.1.1 - Increased result validation
* 0.1.0 - Initial plugin

# Links

* [Dig](https://linux.die.net/man/1/dig)

## References

* [Dig](https://linux.die.net/man/1/dig)
* [DNS Status Code](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml)