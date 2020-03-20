# Description

[Dig](https://linux.die.net/man/1/dig), or Domain Information Groper, is a network administration command-line tool for querying Domain Name System (DNS) name servers. This plugin uses Dig to make forward and reverse DNS requests.

# Key Features

* Forward DNS lookup to find an IP address from a domain name
* Reverse DNS lookup to find a domain name from an IP address

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Forward Lookup

This action is used to request a forward lookup for a domain.

##### Input

It accepts a domain name of type `string` and one of the following record types:

* A
* AAAA
* ANY
* CNAME
* MX
* NS
* PTR
* SOA

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|domain|string|None|True|Domain name to resolve|None|
|query|string|None|True|Query type e.g. ANY, A, MX, NS, etc|['A', 'AAAA', 'ANY', 'CNAME', 'MX', 'NS', 'PTR', 'SOA']|
|resolver|string|None|False|Resolver. Leave blank to use default resolver for the system|None|

Example input:

```

{
  "domain": "google.com",
  "query": "A"
}

```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|all_answers|[]string|False|A list of all answers found|
|answer|string|False|Answer received|
|fulloutput|string|False|Full Dig output|
|last_answer|string|False|The last answer found in the answers section|
|nameserver|string|False|Nameserver that fulfilled request|
|question|string|False|Question asked|
|status|string|False|Query status [ NOERROR | FORMERR | NXDOMAIN | SERVFAIL | REFUSED ...]|

On success, the raw output will look like the following:

Example output:

```
{
  "last_answer": "172.217.6.14",
  "nameserver": "192.168.65.1",
  "question": "google.com",
  "status": "NOERROR",
  "all_answers": [
    "172.217.6.14"
  ],
  "answer": "172.217.6.14",
  "fulloutput": "\n; <<>> DiG 9.12.4-P2 <<>> google.com A\n;; global ..."
}
```


On failure, the raw output will look like the following:

```

{
  "status": "NOERROR",
  "answer": "google-public-dns-a.google.com",
  "nameserver": "10.0.2.3",
  "question": "8.8.8.8.8",
  "fulloutput": "\n; <<>> Dig 9.9.5-9+deb8u9-Debian <<>> -x 8.8.8.8.8\n;; global options: +cmd\n;; Got answer:\n;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 20097\n;; flags: qr rd ra ad; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0\n\n;; QUESTION SECTION:\n;8.8.8.8.8.in-addr.arpa.\t\tIN\tPTR\n\n;; ANSWER SECTION:\n8.8.8.8.8.in-addr.arpa.\t62286\tIN\tPTR\tgoogle-public-dns-a.google.com.\n\n;; Query time: 2 msec\n;; SERVER: 10.0.2.3#53(10.0.2.3)\n;; WHEN: Fri Jan 27 01:21:10 UTC 2017\n;; MSG SIZE  rcvd: 84\n\n"
},

```


#### Reverse Lookup

This action is used to request a reverse lookup for an IP address.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|address|string|None|True|Internet address to resolve|None|
|resolver|string|None|False|Resolver. Leave blank to use default resolver for the system|None|

Example input:

```

{
  "address": "8.8.8.8"
}

```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|answer|string|False|Answer received|
|fulloutput|string|False|Full Dig output|
|nameserver|string|False|Nameserver that fulfilled request|
|question|string|False|Question asked|
|status|string|False|Query status [ NOERROR | FORMERR | NXDOMAIN | SERVFAIL | REFUSED ...]|

On success, the raw output will look like the following:

```

{
  "status": "NOERROR",
  "answer": "google-public-dns-a.google.com",
  "nameserver": "10.0.2.3",
  "question": "8.8.8.8",
  "fulloutput": "\n; <<>> Dig 9.9.5-9+deb8u9-Debian <<>> -x 8.8.8.8\n;; global options: +cmd\n;; Got answer:\n;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 59406\n;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1\n\n;; OPT PSEUDOSECTION:\n; EDNS: version: 0, flags:; udp: 512\n;; QUESTION SECTION:\n;8.8.8.8.in-addr.arpa.\t\tIN\tPTR\n\n;; ANSWER SECTION:\n8.8.8.8.in-addr.arpa.\t68133\tIN\tPTR\tgoogle-public-dns-a.google.com.\n\n;; Query time: 22 msec\n;; SERVER: 10.0.2.3#53(10.0.2.3)\n;; WHEN: Thu Jan 26 23:43:43 UTC 2017\n;; MSG SIZE  rcvd: 93\n\n"
}

```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

The `status` variable contains the [DNS status code](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml) name from the DNS server's response.
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

* 1.0.4 - Add example inputs
* 1.0.3 - Use input and output constants | Change docker image from `komand/python-2-slim-plugin:2` to `komand/python-3-37-slim-plugin:3` to reduce plugin image size | Added "f" strings | Remove duplicate code | Add user nobody to Dockerfile
* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - Update to use the `komand/python-2-slim-plugin:2` Docker image to reduce plugin size
* 1.0.0 - Support web server mode
* 0.3.2 - Update to v2 Python plugin architecture
* 0.3.1 - SSL bug fix in SDK
* 0.3.0 - Add all_answers and last_answer to the forward lookup action
* 0.2.0 - Add option to use custom resolver
* 0.1.1 - Increased result validation
* 0.1.0 - Initial plugin

# Links

## References

* [Dig](https://linux.die.net/man/1/dig)
* [DNS Status Code](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml)

