# Description

The Ping plugin is used to check network connectivity and response times

# Key Features

* Ping a host to check for connectivity

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* 2026-02-11

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Ping

This action is used to ping a host to check for connectivity

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|count|integer|4|True|The number of requests that will be sent, the default is 4|None|4|None|None|
|host|string|None|True|The domain name or IP of the host to check|None|rapid7.com|None|None|
|resolve_hostname|boolean|None|True|Whether to resolve a domain name to an IP address first|None|False|None|None|
  
Example input:

```
{
  "count": 4,
  "host": "rapid7.com",
  "resolve_hostname": false
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|average_latency|string|False|Average latency|0.059ms|
|maximum_latency|string|False|Maximum latency|0.069ms|
|minimum_latency|string|False|Minimum latency|0.044ms|
|packets_percent_lost|float|False|The percentage of packets that were lost|0|
|packets_received|integer|False|The number of packets that the host sent back|4|
|packets_transmitted|integer|False|The number of packets that were sent to the host|4|
|reply|boolean|True|Whether the host is responding to our echo|True|
|response|string|True|The response to the request|PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.\n64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.044 ms\n64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.069 ms\n64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.066 ms\n64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.059 ms\n\n--- 127.0.0.1 ping statistics ---\n4 packets transmitted, 4 received, 0% packet loss, time 3131ms\nrtt min/avg/max/mdev = 0.044/0.059/0.069/0.012 ms\n|
|standard_deviation|string|False|Standard deviation|0.012ms|
  
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
  "response": "PING 127.0.0.1 (127.0.0.1) 56(84) bytes of data.\\n64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.044 ms\\n64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.069 ms\\n64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.066 ms\\n64 bytes from 127.0.0.1: icmp_seq=4 ttl=64 time=0.059 ms\\n\\n--- 127.0.0.1 ping statistics ---\\n4 packets transmitted, 4 received, 0% packet loss, time 3131ms\\nrtt min/avg/max/mdev = 0.044/0.059/0.069/0.012 ms\\n",
  "standard_deviation": "0.012ms"
}
```
### Triggers
  
*This plugin does not contain any triggers.*
### Tasks
  
*This plugin does not contain any tasks.*

### Custom Types
  
*This plugin does not contain any custom output types.*

## Troubleshooting
  
*This plugin does not contain a troubleshooting.*

# Version History

* 1.0.4 - Updated SDK version to 6.4.3
* 1.0.3 - New spec and help.md format for the Extension Library
* 1.0.2 - Bug fix to correct regex's search pattern
* 1.0.1 - Support web server mode
* 1.0.0 - Initial plugin

# Links

* [iputils-ping](https://packages.debian.org/sid/iputils-ping)

## References

* [iputils-ping](https://packages.debian.org/sid/iputils-ping)