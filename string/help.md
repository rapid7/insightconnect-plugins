
# String Operations

## About

The String Operations plugin allows easy manipulation of string data.

This plugin utilizes the Python 3 String library [set of methods](https://docs.python.org/3/library/stdtypes.html#string-methods).

## Actions

### Split String to List

This action is used to convert a string to a list of strings.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|string|string|None|True|String to convert e.g. Sentence one\nSentence two|None|
|delimiter|string|None|False|The character used to split the string into slices for the list. The default is a newline, if not provided by the user|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|list|[]string|False|List of string components|

Example output:

```
{
  "list": [
    "This",
    "is",
    "a",
    "sentence"
  ]
}
```

### Split String to Object

This action is used to convert a string to an object containing key:value strings.

Any input requiring more than a single key:value pair, e.g. `USER=Bob` needs to use the `block_delimiter` option.
In this case, the input string is split by the `block_delimiter` character first, and the resulting items are then split
by the `string_delimiter` option. Stripping of double-quotes is automatically applied in this situation for each item before the plugin returns it.

The [output schema object](https://docs.komand.com/v0.42.1/docs/python-script-plugins#section-configure-the-plugin-output-schema) on the action's page can be modified to pre-populate the workflow with the names of the keys.
It allows users the ability to use the green selector and choose a specific variable later in the workflow by name.
[Input templating](https://docs.komand.com/docs/input-templating) would need to be used to obtain variables by name otherwise.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|string|string|None|True|String to convert e.g. USER=bob|None|
|string_delimiter|string|None|False|The character used to split the string into slices for the list. The default is a space, if not provided by the user|None|
|block_delimiter|string|None|False|The character used to split a block of text (e.g. paragraph) into slices before applying a split with the string delimiter. This is an optional parameter and necessary in more complex splitting situations where a character split isn't enough|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|object|object|False|Object from string split|

Given an input string of `User=Bob`, setting `string_delimiter` to `=` would return the information presented in the example below.

Example output:

```
{
  "object": {
    "User": "Bob"
  }
}
```

Here is another example with a slightly more complex string input that contains multiple key:value pairs.
These pairs are separated from each other by a space, and the keys and values within each pair are separated by an equal sign:

```
Computer_ID="bef41e8b-47b8-e188-8e43-3a2b662dd55d" Computer_Name="dgdemo\RGWin64" Computer_Type="Windows"
```

Setting `block_delimiter` to ` ` and `string_delimiter` to `=` will return the information presented in the example below.

Example output:

```
{
  "object": {
    "Computer_ID": "bef41e8b-47b8-e188-8e43-3a2b662dd55d",
    "Computer_Name": "dgdemo\RGWin64",
    "Computer_Type": "Windows"
  }
}
```

### Upper

This action is used to convert lowercase letters to uppercase.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|string|string|None|True|String to convert e.g. USER=bob|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|upper|string|False|Uppercase string|

Example output:

```
{
  "upper": "LDAP"
}
```

### Lower

This action is used to convert uppercase letters to lowercase.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|string|string|None|True|String to convert e.g. USER=bob|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|lower|string|False|Lowercase string|

Example output:

```
{
  "lower": "hello"
}
```

### Set Encoding

This action is used to encode a string.

#### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|encoding|string|None|True|Encoding to use|['UTF-8', 'ASCII']|
|error_handling|string|None|True|Error handler to use for encoding and decoding|['strict', 'replace', 'ignore']|
|string|string|None|True|String to encode|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|encoded|string|True|Encoded string|

Example output:

```
{
  "encoded": "hello"
}
```

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

There may be complex string manipulation needs that are likely outside the scope of this plugin.
If this is the case, consider using the Python 3 Script plugin instead.

## Versions

* 1.0.0 - Initial plugin
* 1.0.1 - Update plugin tag from `util` to `utilities` for Marketplace searchability
* 1.1.0 - New action Set Encoding

## Workflows

Examples:

* Manipulate string data

## References

* [Python 3 String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
