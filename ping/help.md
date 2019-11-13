# Description

This plugin uses the uses the [GNU Ping](https://www.gnu.org/software/inetutils/manual/html_node/ping-invocation.html#ping-invocation) networking tool to check for host connectivity.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

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
  "average_latency": "50.135ms",
  "maximum_latency": "55.433",
  "minimum_latency": "48.005",
  "packets_percent_lost": 0,
  "packets_received": 4,
  "packets_transmitted": 4,
  "reply": true,
  "response": "PING 8.8.8.8 (8.8.8.8): 56 data bytes\n64 bytes from 8.8 .8 .8: icmp_seq = 0 ttl = 63 time = 50.108 ms\n64 bytes from 8.8 .8 .8: icmp_seq = 1 ttl = 63 time = 48.491 ms\n64 bytes from 8.8 .8 .8: icmp_seq = 2 ttl = 63 time = 49.144 ms\n64 bytes from 8.8 .8 .8: icmp_seq = 3 ttl = 63 time = 89.385 ms\n\n-- - 8.8 .8 .8 ping statistics---\n4 packets transmitted, 4 packets received, 0 % packet loss\nround - trip min / avg / max / stddev = 48.491 / 59.282 / 89.385 / 17.389 ms ",
  "standard_deviation": "3.083"
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - Support web server mode
* 1.0.0 - Initial plugin

# Links

## References

* [GNU Ping](https://www.gnu.org/software/inetutils/manual/html_node/ping-invocation.html#ping-invocation)

