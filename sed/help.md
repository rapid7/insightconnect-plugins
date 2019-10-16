
# Sed

## About

[Sed](https://www.gnu.org/software/sed/manual/sed.html) is a powerful stream editor. This plugin uses GNU Sed 4.2.2 to manipulate input data.
For example, from the command line, an example of the stream editor becomes clear:

```

$ printf 'Cats are enjoyable animals\n' | sed 's/Cats/Dogs/'
Dogs are enjoyable animals

```

## Actions

### Process Bytes

This action is used to process base64 encoded data. The data is decoded and then ran through the stream editor.

#### Input

It accepts an expression, options and a file input.

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|bytes|bytes|None|True|File/bytes to Process|None|
|expression|string|None|True|Sed Expression|None|
|options|string|None|False|Sed Options|None|

The entire input expression will be surrounded in double-quotes on the backend and thus are not required in the expression input.
E.g. the following will replace a lowercase one with a capitalized ONE: `s/one/ONE/`

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|string|False|Processed String|

### Process String

This action is used to process a string through the stream editor.

#### Input

It accepts an expression, options, and a string to process. The command-line options can be passed in via the options input.

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|expression|string|None|True|Sed Expression|None|
|string|string|None|True|String to Process|None|
|options|string|None|False|Sed Options|None|

The entire input expression will be surrounded in double-quotes on the backend, thus they should not be surrounding the expression.
E.g. the following will replace a lowercase `one` with a capitalized `ONE`: `s/one/ONE/`. Note that the expression is not surrounded
by any quotes, although, you could surround it with single-quotes and still maintain functionality.

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|output|string|False|Processed String|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

Careful attention to the use of double-quotes should be used, the expression will not work if it's surrounded by double-quotes.
If a literal double-quote is required it must be escaped by a backslash `\`. For example:

* `s/\"//g` - A stream editor expression to remove all double-quotes from a string.
* `'s/\"/\'/g'` - A stream editor expression to replace all double-quotes with single-quotes.

## Workflows

Examples:

* Data format and extraction

## Versions

* 0.1.0 - Initial plugin
* 0.1.1 - SSL bug fix in SDK
* 0.1.2 - Update to v2 Python plugin architecture
* 1.0.0 - Support web server mode | Rename action to "Process String"
* 1.0.1 - Add `utilities` plugin tag for Marketplace searchability
* 2.0.0 - Update action inputs to allow for multiple expressions
* 2.0.1 - Fix issue with both actions not returning all results

## References

* [Sed](https://www.gnu.org/software/sed/manual/sed.html)
