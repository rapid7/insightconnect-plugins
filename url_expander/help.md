
# URL Expander

## About

The URL Expander plugin expands shortened URLs.

## Actions

### Expand All

This action is used to expand all shortened URLs in some text.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|text|string|None|True|Block of text with URL's to expand|None|
|follow|boolean|None|True|Whether to follow the URL|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|text|string|False|Text with expanded URLs|

Example output:

```

{
  "text": "Tweeting some helpful info https://gist.github.com/jandre/38db0124e9c6c9761a34 hello.com http://google.foo"
}

```

### Expand

This action is used to expand a shortened URL.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|url|string|None|True|Shortened URL|None|
|follow|boolean|None|True|Whether to follow the URL|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|False|Expanded URL|

Example output:

```

{
  "url": "http://google.com/"
}

```

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

This plugin does not contain any troubleshooting information.

## Workflows

Examples:

* Phishing investigation

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 1.0.0 - Added support for optional following of a URL
* 1.1.0 - Support web server mode
* 1.1.1 - Add `utilities` plugin tag for Marketplace searchability
* 1.1.2 - Fix typo in plugin spec

## References

* [Python Urllib2 urlopen](https://docs.python.org/2/library/urllib2.html#urllib2.urlopen)
