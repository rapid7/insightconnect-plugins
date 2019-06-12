
# Sketchify

## About

[Sketchify](https://verylegit.link/) is a free service, developed by security researcher @mangopdf, that turns any link into a suspicious looking one.

This plugin utilizes the [Sketchify API](https://github.com/defaultnamehere/verylegit.link).

## Actions

### Sketchify Link

This action is used to turn a URL into a suspicious looking one.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|URL to Sketchify|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|True|Sketchy URL|

Example output:

```

{
  "url": "very.verylegit.link/;private-key)659notice(speedupurpc+malware.virus.exe"
}

```

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Versions

* 1.0.0 - Initial plugin

## Workflows

Examples:

* Phishing campaigns

## References

* [Sketchify](https://verylegit.link/)
* [Sketchify API](https://github.com/defaultnamehere/verylegit.link)
