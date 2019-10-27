
# JSON

## About

The JSON plugin provides a way to parse or transform [JSON](http://www.json.org/) data.

## Actions

### Transform

This action is used to transform JSON data per template.

#### Input

This action is used to parse JSON data. It accepts the following parameters:

* Source JSON data
* Extraction template, in JSON format
* Target template, in JSON format

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|source_data|object|None|True|Input data in JSON layout|None|
|target_template|object|None|True|Desired output layout containing the same $ placeholder strings|None|
|extraction_template|object|None|True|Input layout containing placeholders (strings beginning with $)|None|

The extraction template has the same structure as the source JSON,
except that it can contain a placeholder instead of the data.  A
placeholder is simply a string beginning with a dollar sign.  It
allows us to reuse parts of the source JSON in the output JSON.

For instance, suppose we have the following source JSON:

```

{"Age":{"eons":8}, "Name":"SnowCrash", "Characters":["Hiro Protagonist","Y.T."]}

```

Here is an extraction template that indicates we want to reuse the
Name, Age, and the main Character in a new JSON layout.  The
placeholders are "$0", "$1", and "$3":

```

{"name":"$0", "characters":["$1"], "age":{"eons":"$2"}}

```

Here is a target template that indicates how we want the placeholder
data to appear in the output JSON:

```

{"bug":"$0", "owner":"$1", "age (eons)":"$2"}

```

Given the above example input, the plugin will produce:

```

{"bug":"SnowCrash", "owner":"Hiro Protagonist", "age (eons)":8}

```

This plugin also filters arrays of strings.  For example, the
following source, extraction template, and target template:

```

{"Reviews": ["So-so", "Banal", "Special!", "Puzzling", "Quite good"]}
{"Reviews": "$1:.*special.*|.*good.*|.*great.*"}
{"Critics Raved!": "$1"}

```

will produce: `{"Critics Raved!": ["Special!", "Quite good"]}`

The matcher accepts standard [Perl regular expressions](https://github.com/google/re2/wiki/Syntax).

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|target_data|object|False|Desired JSON layout, populated by placeholder data extracted from input|

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

The matching is case-insensitive.

## Versions

* 1.0.0 - Initial plugin
* 1.1.0 - Support web server mode
* 1.1.1 - Updating to Go SDK 2.6.4
* 1.1.2 - Regenerate with latest Go SDK to solve bug with triggers
* 1.1.3 - Add `utilities` plugin tag for Marketplace searchability

## Workflows

Examples:

* Data format and extraction

## References

* [Perl regular expressions](https://github.com/google/re2/wiki/Syntax)
