# Description

[Sketchify](https://verylegit.link/) is a service used to turn any link into one that appears suspicious. 
With the Sketchify plugin for Rapid7 InsightConnect, users can conduct internal phishing campaigns or other forms of 
penetration testing within their organization.

This plugin utilizes the [Sketchify API](https://github.com/defaultnamehere/verylegit.link).

# Key Features

* Create suspicious links

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Sketchify Link

This action is used to turn a URL into a suspicious looking one.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|URL to Sketchify|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|True|Sketchy URL|

Example output:

```

{
  "url": "very.verylegit.link/;private-key)659notice(speedupurpc+malware.virus.exe"
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Initial plugin

# Links

## References

* [Sketchify](https://verylegit.link/)
* [Sketchify API](https://github.com/defaultnamehere/verylegit.link)

