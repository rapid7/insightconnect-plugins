# Description

The Ping plugin is used to check network connectivity and response times.

This plugin uses the uses the [GNU Ping](https://www.gnu.org/software/inetutils/manual/html_node/ping-invocation.html#ping-invocation).

# Key Features

* Ping an address

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Ping

This action is used to `ping` a host to check for connectivity.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|count|integer|4|True|None|The number of requests that will be sent, the default is 4|None|
|resolve_hostname|boolean|None|True|Whether to resolve a domain name to an IP address first|None|
|host|string|None|True|The domain name or IP of the the host to check|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|maximum_latency|string|False|Maximum latency|
|standard_deviation|string|False|Standard deviation|
|packets_received|integer|False|The number of packets that the host sent back|
|packets_transmitted|integer|False|The number of packets that were sent to the host|
|average_latency|string|False|Average latency|
|minimum_latency|string|False|Minimum latency|
|reply|boolean|True|Whether the host is responding to our echo|
|packets_percent_lost|float|False|The percentage of packets that were lost|
|response|string|True|The response to the request|

Example output:

```

{
  "average_latency": "0.059ms",
  "maximum_latency": "0.069ms",
  "minimum_latency": "0.044ms",
  "packets_percent_lost": 0,
  "packets_received": 4,
  "packets_transmitted": 4,
  "reply": true,
  "response": "PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.\n64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.044 ms\n64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.069 ms\n64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.066 ms\n64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.059 ms\n\n--- 127.0.0.1 ping statistics ---\n4 packets transmitted, 4 received, 0% packet loss, time 3131ms\nrtt min/avg/max/mdev = 0.044/0.059/0.069/0.012 ms\n",
  "standard_deviation": "0.012ms"
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.3 - New spec and help.md format for the Hub
* 1.0.2 - Bug fix to correct regex's search pattern
* 1.0.1 - Support web server mode
* 1.0.0 - Initial plugin

# Links

## References

* [GNU Ping](https://www.gnu.org/software/inetutils/manual/html_node/ping-invocation.html#ping-invocation)