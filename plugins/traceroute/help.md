# Description

This plugin uses [tcptraceroute](https://linux.die.net/man/1/tcptraceroute), an implementation of Traceroute that uses TCP rather than ICMP. Tcptraceroute can bypass some firewalls that block ICMP and UDP

# Key Features

* Trace a route to a host

# Requirements
  
*This plugin does not contain any requirements.*

# Supported Product Versions

* tcptraceroute 1.5beta7

# Documentation

## Setup
  
*This plugin does not contain a connection.*

## Technical Details

### Actions


#### Traceroute

This action is used to returns the route used to communicate with the host

##### Input

|Name|Type|Default|Required|Description|Enum|Example|Placeholder|Tooltip|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|count|integer|3|True|The number of probes to be sent to each hop. The default is 3|None|3|None|None|
|host|string|None|True|The domain name or IP of the the host to find a route to|None|example.com|None|None|
|max_ttl|integer|30|True|Set the maximum TTL used in outgoing packets. The default is 30|None|30|None|None|
|port|integer|80|True|Set the port that traceroute will try to reach. The default is 80|None|80|None|None|
|resolve_hostname|boolean|True|True|If true traceroute will attempt to return a DNS name rather than an IP address. If false, traceroute will always return the IP address|None|True|None|None|
|set_ack|boolean|False|True|If true set the TCP ACK flag in outgoing packets. By doing so, it is possible to trace through stateless firewalls which permit outgoing TCP connections|None|True|None|None|
|time_out|integer|3|True|Set the timeout, in seconds, to wait for a response for each probe. The default is 3|None|3|None|None|
  
Example input:

```
{
  "count": 3,
  "host": "example.com",
  "max_ttl": 30,
  "port": 80,
  "resolve_hostname": true,
  "set_ack": false,
  "time_out": 3
}
```

##### Output

|Name|Type|Required|Description|Example|
| :--- | :--- | :--- | :--- | :--- |
|ip|[]string|True|IP addresses|["1.1.1.1", "0.0.0.0"]|
|path|[]string|True|The path used to get to the host including response times|["1  1.1.1.1  2.218 ms  0.128 ms  0.068 ms", "2  example.example.net (0.0.0.0) [open]  189.590 ms  196.722 ms  194.262 ms"]|
|reply|boolean|True|Whether a route was found to the host|True|
|response|string|True|The full raw response from traceroute|1  1.1.1.1  2.218 ms  0.128 ms  0.068 ms
 2  example.example.net (0.0.0.0) [open]  189.590 ms  196.722 ms  194.262 ms
|
  
Example output:

```
{
  "ip": [
    "1.1.1.1",
    "0.0.0.0"
  ],
  "path": [
    "1  1.1.1.1  2.218 ms  0.128 ms  0.068 ms",
    "2  example.example.net (0.0.0.0) [open]  189.590 ms  196.722 ms  194.262 ms"
  ],
  "reply": true,
  "response": "1  1.1.1.1  2.218 ms  0.128 ms  0.068 ms\n 2  example.example.net (0.0.0.0) [open]  189.590 ms  196.722 ms  194.262 ms\n"
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

* 1.0.3 - Updated SDK version to 6.4.3
* 1.0.2 - New spec and help.md format for the Extension Library
* 1.0.1 - Support web server mode
* 1.0.0 - Initial plugin

# Links

* [Man Page for tcptraceroute](https://linux.die.net/man/1/tcptraceroute)

## References

* [Git Repository](https://github.com/mct/tcptraceroute)