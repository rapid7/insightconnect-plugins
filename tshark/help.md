# Description

[TShark](https://www.wireshark.org/docs/man-pages/tshark.html) is a tool for dumping and analyzing network traffic.
 With the TShark plugin for Rapid7 InsightConnect, users can open PCAP data for further analysis and intel gathering.

# Key Features

* Run TShark on a PCAP file

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Run

This action is used to run TShark on a user supplied PCAP file and return the output as `bytes` and a `string array` of packets.

##### Input

Supported options:

* TShark Flags
* Display Filter

A display filter is required, the default is set to `ip or ipv6` to encompass most traffic one would want to analyze.

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|filter|string|ip or ipv6|False|Display filter E.g. tcp.port eq 80|None|
|options|string|None|False|Tshark flags and options E.g. -n -c 10 -s 96. -r is implied|None|
|file|bytes|None|True|Base64 encoded pcap|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|dump_contents|[]string|False|Traffic dump as array|
|dump_file|bytes|False|Traffic dump file|

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

The default output of `dump_contents` creates an easily readable array of strings where each packet is an element of the array:

```

"dump_contents": [
  "  1   0.000000     10.1.2.4 -> 10.1.2.3     TCP 74 35850->80 [SYN] Seq=0 Win=29200 Len=0 MSS=1460 SACK_PERM=1 TSval=55329 TSecr=0 WS=128",
  "  2   0.000047     10.1.2.3 -> 10.1.2.4     TCP 74 80->35850 [SYN, ACK] Seq=0 Ack=1 Win=28960 Len=0 MSS=1460 SACK_PERM=1 TSval=302439 TSecr=55329 WS=128",
  "  3   0.000246     10.1.2.4 -> 10.1.2.3     TCP 66 35850->80 [ACK] Seq=1 Ack=1 Win=29312 Len=0 TSval=55329 TSecr=302439",
  "  4   0.000407     10.1.2.4 -> 10.1.2.3     HTTP 146 GET /test.zip HTTP/1.1 ",
  "  5   0.000440     10.1.2.3 -> 10.1.2.4     TCP 66 80->35850 [ACK] Seq=1 Ack=81 Win=29056 Len=0 TSval=302439 TSecr=55329"
]

```

Use of `-V` and other options that cause multiple lines of output for a single packet will disorganize the
`dump_contents` output variable. Each line of output will be a new string in the array and can make it hard to read.
For example, `-V` is used to return the following `dump_contents` array where each packet dissection comprises multiple elements of the array.

```

"Frame 1: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)",
"    Encapsulation type: Ethernet (1)",
"    Arrival Time: Dec 21, 2016 04:56:34.428222000 UTC",
"Ethernet II, Src: CadmusCo_4e:d9:39 (08:00:27:4e:d9:39), Dst: CadmusCo_fd:ca:eb (08:00:27:fd:ca:eb)",
"    Destination: CadmusCo_fd:ca:eb (08:00:27:fd:ca:eb)",
...
"Internet Protocol Version 4, Src: 10.1.2.4 (10.1.2.4), Dst: 10.1.2.3 (10.1.2.3)",
"    Version: 4",
...
"Transmission Control Protocol, Src Port: 35850 (35850), Dst Port: 80 (80), Seq: 0, Len: 0",
"                [Group: Sequence]",
"        [Bad Checksum: False]",
"            MSS Value: 1460",
"        TCP SACK Permitted Option: True",
"                .00. .... = Class: Control (0)",
"                ...0 0001 = Number: No-Operation (NOP) (1)",
...
"Frame 2: 74 bytes on wire (592 bits), 74 bytes captured (592 bits)",
"    Encapsulation type: Ethernet (1)",
"    Arrival Time: Dec 21, 2016 04:56:34.428269000 UTC",
"    [Time shift for this packet: 0.000000000 seconds]",
"    Frame Length: 74 bytes (592 bits)",
"    Capture Length: 74 bytes (592 bits)",
...

```

# Version History

* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - Fix issue where run action was excluded from plugin on build
* 1.0.0 - Update to v2 Python plugin architecture | Support web server mode
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Tshark](https://www.wireshark.org/docs/man-pages/tshark.html)

