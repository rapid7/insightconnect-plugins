# Description

[URL encoding](https://en.wikipedia.org/wiki/Percent-encoding) converts unprintable or special characters in a URL into a standard `%XX` representation, using only legal ASCII characters. For example, the space character ` ` is encoded as `%20`.

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

#### Encoder

This action is used to encode special characters and non-ASCII text in a `string` to make it safe for use as URL components.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|encode_all|boolean|False|False|If true will encode all non-alphanumeric characters, including ?=&# but not /|None|False|
|url|string|None|True|URL to encode|None|https://example.com?test string&key=value|

Example input:

```
{
  "encode_all": "false",
  "url": "https://example.com?test string\u0026key=value"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|True|Encoded URL|

Example output:

```
{
  "data": "example.com/page%3Ftext%3Dabc%24%25%5E-~%3Cscript%3E%28%29%23%21123"
}
```

#### Decoder

This action is used to decode an encoded URL `string` to the original characters.

##### Input

|Name|Type|Default|Required|Description|Enum|Example|
|----|----|-------|--------|-----------|----|-------|
|url|string|None|True|URL to decode|None|https://example.com?test%20string|

Example input:

```
{
  "url": "https://example.com?test%20string"
}
```

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|url|string|True|Decoded URL|

Example output:

```
{
  "": "example.com/page?text=abc$%^-~<script>()#!123"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

For the URL decode action, be sure that the input contains valid percent-encoded data.

If the URL you're decoding contains any non UTF-8 characters the plugin will fail. To remedy this issue, there's a
option to set how errors are to be handled. These options are "replace" and "ignore". Replace will change all non-UTF-8
characters to `\uffd` or `?`. While ignore will drop the character from the output.

# Version History

* 1.0.0 - Initial plugin

# Links

## References


