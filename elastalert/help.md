
# ElastAlert

## About

[ElastAlert](https://github.com/Yelp/elastalert) allows for easy & flexible alerting with ElasticSearch.
This plugin listens for alerts from an ElastAlert webhook and triggers on them.

## Actions

This plugin does not contain any actions.

## Triggers

### Get Alerts

This trigger is used to listen for and trigger on new alerts from a simple ElastAlert webhook.
It opens a network socket on the specified port and endpoint. ElastAlert should be configured to use the specified port and endpoint.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|tcp_port|integer|None|True|TCP port to listen for messages|None|
|endpoint|string|0.0.0.0|True|IP address of the Komand host to listen on. Use 0.0.0.0 to listen on the all address|None|
|interval|integer|5|False|Interval to wait before reading another message|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|alert|string|True|None|

## Connection

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|True|Basic Auth username and password|None|

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Versions

* 0.1.0 - Initial plugin
* 1.0.0 - Support web server mode | Update to new credential types

## Workflows

Examples:

* Receive alerts

## References

* [ElastAlert](https://github.com/Yelp/elastalert)
