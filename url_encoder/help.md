# Description

URL encoding (also known as percent encoding) converts special characters in a URL into a standard `%XX` representation, using only safe ASCII characters. For example, the space character ` ` is encoded as `%20`.

# Key Features

* Encode a URL into an ASCII format that is safe and universally accepted by servers and web browsers
* Decode a URL to reveal original input

# Requirements

_This plugin does not contain any requirements._

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Encode URL

This action is used to encode special, reserved, unsafe, or non-ASCII characters in a `string` to make it safe for use as URL components.
It does not encode the characters `/?=&#` by default, though you may encode these characters anyway by setting the `encode_all` variable to `true`.

The `://` protocol separator is unchanged if it is present in the input, regardless of the `encode_all` value.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|encode_all|boolean|False|False|If true will encode all special characters|None|True|
|url|string|None|True|URL to encode|None|https://example.com?test string&key=value|

Example input:

```
{
  "encode_all": false,
  "url": "https://example.com?test string&key=value"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|True|Encoded URL|

Example output:

```
{
  "url": "https://example.com?test%20string&key=value"
}
```

#### Decode URL

This action is used to decode an encoded URL `string` to the original characters.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|errors|string|replace|False|Set to ignore or replace invalid encodings|None|replace|
|url|string|None|True|URL to decode|None|https://example.com/utf8%3D%E2%9C%93%26replace%3D%99|

Example input:

```
{
  "errors": "replace",
  "url": "https://example.com/utf8%3D%E2%9C%93%26replace%3D%99"
}
```

Note that `%99`, the last encoding in `url`, is an invalid percent encoding.

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|True|Decoded URL|

Example output:

```
{
  "url": "https://example.com/utf8=✓&replace=�"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

For the URL decode action, be sure that the input contains valid percent-encoded data.

The decode action has an `errors` option to set how invalid percent-encodings are to be handled.
These options are "replace" and "ignore". The default is to replace.
Replace will change all invalid percent-encodings to `�`.
Ignore will drop the character from the output.

# Version History

* 1.0.2 - Patch misspelled input variable retrieval
* 1.0.1 - Patch encode action to include # as safe characters
* 1.0.0 - Initial plugin

# Links

## References

* [Wikipedia: URL encoding (also known as percent encoding)](https://en.wikipedia.org/wiki/Percent-encoding)
* [Wikipedia: UTF-8 Unicode character encoding](https://en.wikipedia.org/wiki/UTF-8)
* [Python 3 URL encoding method](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.quote)
* [Python 3 URL decoding method](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.unquote)
