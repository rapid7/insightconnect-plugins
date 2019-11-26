# Description

[Dig](https://linux.die.net/man/1/dig) is a powerful DNS lookup utility. This plugin uses Dig to make forward and reverse DNS requests.

For example, from the command line:

```

# Forward lookup
$ dig google.com +short
216.58.192.174

# Reverse lookup
$ dig -x 216.58.192.174 +short
ord36s02-in-f174.1e100.net.
ord36s02-in-f14.1e100.net.

```

# Key Features

* Forward and reverse DNS lookup

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

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
|query|string|None|False|Query type e.g. ANY, A, MX, NS, etc|['A', 'AAAA', 'ANY', 'CNAME', 'MX', 'NS', 'PTR', 'SOA']|
|domain|string|None|True|Domain name to resolve|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|Query status [ NOERROR \| FORMERR \| NXDOMAIN \| SERVFAIL \| REFUSED ...]|
|last_answer|string|False|The last answer found in the answers section|
|fulloutput|string|False|Full Dig output|
|answer|string|False|Answer received|
|nameserver|string|False|Nameserver that fulfilled request|
|question|string|False|Question asked|
|all_answers|[]string|False|A list of all answers found|

On success, the raw output will look like the following:

```

{
  "status": "NOERROR",
  "answer": "50.19.156.131",
  "nameserver": "10.0.2.3",
  "question": "komand.com",
  "fulloutput": "\n; <<>> Dig 9.9.5-9+deb8u9-Debian <<>> komand.com A\n;; global options: +cmd\n;; Got answer:\n;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 15364\n;; flags: qr rd ra ad; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0\n\n;; QUESTION SECTION:\n;komand.com.\t\t\tIN\tA\n\n;; ANSWER SECTION:\nkomand.com.\t\t2677\tIN\tA\t50.19.156.131\n\n;; Query time: 6 msec\n;; SERVER: 10.0.2.3#53(10.0.2.3)\n;; WHEN: Thu Jan 26 23:11:29 UTC 2017\n;; MSG SIZE  rcvd: 44\n\n"
  "all_answers": ["50.19.156.131"],
  "last_answer": "50.19.156.131"
},

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

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|status|string|False|Query status [ NOERROR \| FORMERR \| NXDOMAIN \| SERVFAIL \| REFUSED ...]|
|answer|string|False|Answer received|
|nameserver|string|False|Nameserver that fulfilled request|
|question|string|False|Question asked|
|fulloutput|string|False|Full Dig output|

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

This plugin does not contain any triggers.

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

* 1.0.3 - New spec and help.md format for the Hub
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

