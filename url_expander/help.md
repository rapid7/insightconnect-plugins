# Description

The URL Expander plugin expands shortened URLs.

# Key Features

* Expand a shortened URL

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

This plugin does not contain a connection.

## Technical Details

### Actions

#### Expand All

This action is used to expand all shortened URLs in some text.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|follow|boolean|False|True|Whether to follow the URL|None|
|text|string|None|True|Block of text with URL's to expand|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|text|string|False|Text with expanded URLs|

Example output:

```

{
  "text": "Tweeting some helpful info https://gist.github.com/jandre/38db0124e9c6c9761a34 hello.com http://google.foo"
}

```

#### Expand

This action is used to expand a shortened URL.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|follow|boolean|False|True|Whether to follow the URL|None|
|url|string|None|True|Shortened URL|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|False|Expanded URL|

Example output:

```

{
  "url": "http://google.com/"
}

```

### Triggers

This plugin does not contain any triggers.

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

This plugin does not contain any troubleshooting information.

# Version History

* 1.1.3 - New spec and help.md format for the Extension Library
* 1.1.2 - Fix typo in plugin spec
* 1.1.1 - Add `utilities` plugin tag for Marketplace searchability
* 1.1.0 - Support web server mode
* 1.0.0 - Added support for optional following of a URL
* 0.1.1 - SSL bug fix in SDK
* 0.1.0 - Initial plugin

# Links

## References

* [Python Urllib2 urlopen](https://docs.python.org/2/library/urllib2.html#urllib2.urlopen)

