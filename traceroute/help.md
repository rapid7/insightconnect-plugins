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

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Traceroute

This action is used to trace a route to a host. It returns the route used to communicate with the host.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|count|integer|3|True|The number of probes to be sent to each hop. The default is 3|None|
|host|string|None|True|The domain name or IP of the the host to find a route to|None|
|max_ttl|integer|30|True|Set the maximum TTL used in outgoing packets. The default is 30|None|
|port|integer|80|True|Set the port that traceroute will try to reach e.g. set it to port 443 for a host running an HTTPS server. The default is 80|None|
|resolve_hostname|boolean|True|True|If true traceroute will attempt to return a DNS name rather than an IP address. If false, traceroute will always return the IP address|None|
|set_ack|boolean|False|True|If true set the TCP ACK flag in outgoing packets. By doing so, it is possible to trace through stateless firewalls which permit outgoing TCP connections|None|
|time_out|integer|3|True|Set the timeout, in seconds, to wait for a response for each probe. The default is 3|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|ip|[]string|True|IP addresses|
|path|[]string|True|The path used to get to the host including response times|
|reply|boolean|True|Whether a route was found to the host|
|response|string|True|The full raw response from traceroute|

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

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.0.2 - New spec and help.md format for the Hub
* 1.0.1 - Support web server mode
* 1.0.0 - Initial plugin

# Links

## References

* [Man Page for tcptraceroute](https://linux.die.net/man/1/tcptraceroute)
* [Git Repository](https://github.com/mct/tcptraceroute)

