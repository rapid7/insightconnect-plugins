
# Translate

## About

The Translate plugin uses the `tr` command in UNIX which is a command line utility for translating or deleting characters. It supports a range of transformations including uppercase to lowercase, squeezing repeating characters, deleting specific characters and basic find and replace. `tr` stands for Translate.

## Actions

### Replace

This action is used to run a `tr` expression on a string input.

#### Input

It accepts a `tr` expression and a string to process using that expression. Any correct `tr` expression can be used, including all the options and interpreted sequences.

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|text|string|None|True|Text to process|None|
|expression|string|None|True|Correct tr expression (e.g. -s [\:space\:] ' ')|None|

#### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|result|string|False|Processed text|

Example output:

```

{
  "result": "Some reevant etters have been deeted"
}

```

## Triggers

This plugin does not contain any triggers.

## Connection

This plugin does not contain a connection.

## Troubleshooting

In case an error is raised, make sure that the given expression can be correctly handled by the `tr` program.

## Versions

* 1.0.0 - Initial plugin
* 2.0.0 - Rename "Tr" plugin title to "Translate"
* 2.0.1 - Add `utilities` plugin tag for Marketplace searchability

## Workflows

Examples:

* Removing characters from input
* Replacing characters (e.g. round brackets with square ones)

## References

* [tr examples](https://www.geeksforgeeks.org/tr-command-unixlinux-examples/)
