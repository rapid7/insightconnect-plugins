# Description

This plugin uses [tcptraceroute](https://linux.die.net/man/1/tcptraceroute) version 1.5beta, an implementation of Traceroute that uses TCP rather than ICMP.
Tcptraceroute can bypass some firewalls that block ICMP and UDP.

Traceroute sends out either UDP or ICMP ECHO packets with a TTL of one, and increments the TTL until the destination has been reached. By printing the gateways that generate ICMP time exceeded messages along the way, it is able to determine the path packets are taking to reach the destination.

# Key Features

* Trace a route to a host

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Traceroute

This action is used to trace a route to a host. It returns the route used to communicate with the host.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|count|integer|3|True|The number of probes to be sent to each hop. The default is 3|None|
|max_ttl|integer|30|True|Set the maximum TTL used in outgoing packets. The default is 30|None|
|host|string|None|True|The domain name or IP of the the host to find a route to|None|
|resolve_hostname|boolean|True|True|If true Traceroute will attempt to return a DNS name rather than an IP address. If false Traceroute will always return the IP address|None|
|set_ack|boolean|False|True|If True set the TCP ACK flag in outgoing packets. By doing so, it is possible to trace through stateless firewalls which permit outgoing TCP connections|None|
|time_out|integer|3|True|Set the timeout, in seconds, to wait for a response for each probe. The default is 3|None|
|port|integer|80|True|Set the port that Traceroute will try to reach default 80 eg set it to port 25 for a host that is running a mail server|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ip|[]string|False|A list of all IP address along the path|
|path|[]string|False|The path used to get to the host including response times|
|response|string|False|The full raw response from tracerout|
|reply|boolean|True|Traceroute found a route to the host|

Example output:

```

{
  "reply": true,
  "response": " 1  172.17.0.1  0.098 ms  0.095 ms  0.089 ms\n 2  104.17.197.123 [open]  43.307 ms  -526.721 ms  44.549 ms\n",
  "path": [
    " 1  172.17.0.1  0.098 ms  0.095 ms  0.089 ms",
    " 2  104.17.197.123 [open]  43.307 ms  -526.721 ms  44.549 ms"
  ],
  "ip": [
    "172.17.0.1",
    "104.17.197.123"
  ]
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - Support web server mode
* 1.0.0 - Initial plugin

# Links

## References

* [Man Page for tcptraceroute](https://linux.die.net/man/1/tcptraceroute)
* [Git Repository](https://github.com/mct/tcptraceroute)

