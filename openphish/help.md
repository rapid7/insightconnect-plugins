# Description

[OpenPhish](http://openphish.com) is a fully automated self-contained platform for phishing intelligence.
It identifies phishing sites and performs intelligence analysis in real time without human intervention and without using any external resources, such as blacklists.

# Key Features

* Feature 1
* Feature 2
* Feature 3

# Requirements

* Example: Requires an API Key from the product
* Example: API must be enabled on the Settings page in the product

# Documentation

## Setup

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|https://openphish.com/feed.txt|False|URL for feed file in OpenPhish|None|

## Technical Details

### Actions

#### Check URL Reputation

This action checks if a given URL is in the OpenPhish threat feed and returns a historic count of found URLs.

The feed is fetched by the Fetch Feed trigger which means this action must come after that step in the workflow.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|URL for checking in feed file|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|URLReputation|object|True|Object with total matches, match for every URL cached, and if the current supplied URL is found in feed file|

### Triggers

#### Fetch Feed

This trigger is used to poll the feed file and cache it for the Check URL Reputation action.
Note that the trigger only returns data if the feed has changed since the last fetch.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|interval|integer|3600|True|Length of time to wait between polling (in seconds)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.0 - Initial plugin

# Links

## References

* [OpenPhish](http://openphish.com)
* [OpenPhish feed file](https://openphish.com/feed.txt)
* [OpenPhish FAQ](https://openphish.com/faq.html)

