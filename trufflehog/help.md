# Description

Search through git repositories for high entropy strings and secrets, digging deep into commit history

# Key Features

* Find confidential information in git history

# Requirements

* Requires an API Key from the product
* API must be enabled on the Settings page in the product's user interface

# Documentation

## Setup

_This plugin does not contain a connection._

## Technical Details

### Actions

#### Search

This action looks for exposed secrets in the git commit history and branches.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|custom_regexes|object|None|False|Ignores default regexes. Provide your own|None|
|do_entropy|boolean|True|False|Evaluates the shannon entropy for both the base64 char set and hexadecimal char set for every blob of text greater than 20 characters comprised of those character sets in each diff|None|
|do_regex|boolean|False|False|Enable high signal regex checks|None|
|git_url|string|None|True|The git repository that is going to be searched e.g. https://github.com/jonschipp/islet|None|
|max_depth|integer|1000000|False|Max commit depth to go back when searching for secrets|None|
|since_commit|string|None|False|Scan from a given commit hash|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|issues|[]issue|False|Issues found with TruffleHog|

Example output:

```
{     
  "issues": [
    { 
      "branch": "origin/master",
      "commit": "make bash style consistent\n",
      "commitHash": "d6bb404c8ab20982c1f8c7961a392f4386b53aba",
      "date": "2016-02-08 05:32:02",
      "diff": "<snip console output>",
      "path": "functions.sh",
      "printDiff": "<snip console output>",
      "reason": "High Entropy",
      "stringsFound": [
        "36A1D7869245C8950F966E92D8576A8BA88D21E9"
      ],
      "url": "https://github.com/jonschipp/islet/commit/d6bb404c8ab20982c1f8c7961a392f4386b53aba"
    },
    <snip other array elements>
  ]
}               
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

#### issue

|Name|Type|Required|Description|
|----|----|--------|-----------|
|Branch|string|False|Commit branch|
|Commit|string|False|Commit subject|
|Commit Hash|string|False|None|
|Date|string|False|None|
|Diff|string|False|None|
|Path|string|False|File path|
|Diff|string|False|None|
|Reason|string|False|None|
|Strings Found|[]string|False|List of found strings|
|Commit URL|string|False|Commit URL|

## Troubleshooting

_This plugin does not contain any troubleshooting information._

# Version History

* 1.1.3 - Updated spec and help.md format for the Extension Library
* 1.1.2 - New spec and help.md format for the Extension Library
* 1.1.1 - Fix issue where custom_regexes input field in Search action was not working
* 1.1.0 - Update to v2 Python plugin architecture | Support web server mode
* 1.0.0 - Initial plugin

# Links

## References

* [TruffleHog](https://github.com/dxa4481/truffleHog)
