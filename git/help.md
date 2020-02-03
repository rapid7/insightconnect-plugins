# Description

[Git](https://www.git-scm.com/) is a free and open source distributed version control system.
Git InsightConnect plugin allow you to add, remove, commit files to Git repository.

# Key Features

* Add file to Git repository
* Remove file from Git repository
* Commit file to Git repository

# Requirements

* Git repository URL
* Git account's username and password

# Documentation

## Setup

This plugin uses either a username and a password (if both values are provided) or a token (if only the `password` field is provided with the token).

The connection configuration accepts the following parameters:

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|credentials|credential_username_password|None|False|Git username (if empty, 'x-auth-token' is used and 'password' field is considered an access token)|None|
|url|string|None|True|Git repository URL (e.g ssh://myrepo.com/path/to/repo.git/; only SSH and HTTP/HTTPS protocols are supported)|None|

## Technical Details

### Actions

#### Remove File

This action is used to remove a file from the repository.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_path|string|None|True|Path to the file|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|commit_id|string|False|Commit's hash|
|commit_url|string|False|Commit's URL|
|success|boolean|True|Is successful?|

Example output:

```
{
  "success": true,
  "commit_id": "ee646cea7356dbd8be91490082a5596422dfbd3d",
  "commit_url":
      "https://gitlab.com/komand-test/test-repository/" +
      "commit/ee646cea7356dbd8be91490082a5596422dfbd3d"
}
```

#### Add File

This action is used to add a file to the repository.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_contents|bytes|None|False|Contents of the new file|None|
|file_path|string|None|True|Path of the new file (inside the repository)|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|commit_id|string|False|Commit's hash|
|commit_url|string|False|Commit's URL|
|success|boolean|True|Is successful?|

Example output:

```
{
  "success": true,
  "commit_id": "ee646cea7356dbd8be91490082a5596422dfbd3d",
  "commit_url":
      "https://gitlab.com/komand-test/test-repository/" +
      "commit/ee646cea7356dbd8be91490082a5596422dfbd3d"
}
```

#### Append Line to File

This action is used to append a line to a file and commit it.

##### Input

|Name|Type|Default|Required|Description|Enum|
|----|----|-------|--------|-----------|----|
|file_path|string|None|True|Path to the file|None|
|line|string|None|True|A line of text to append|None|

##### Output

|Name|Type|Required|Description|
|----|----|--------|-----------|
|commit_id|string|False|Commit's hash|
|commit_url|string|False|Commit's URL|
|success|boolean|True|Is successful?|

Example output:

```
{
  "success": true,
  "commit_id": "ee646cea7356dbd8be91490082a5596422dfbd3d",
  "commit_url":
      "https://gitlab.com/komand-test/test-repository/" +
      "commit/ee646cea7356dbd8be91490082a5596422dfbd3d"
}
```

### Triggers

_This plugin does not contain any triggers._

### Custom Output Types

_This plugin does not contain any custom output types._

## Troubleshooting

Make sure that the repository URL has the correct format (protocol, host, path, no username).

In case of problems with an `ssh` connection, check if the server supports it (GitHub and GitLab by default require SSH keys instead of a password).
If a token is used, make sure that it has sufficient permissions assigned to it.

# Version History

* 1.0.1 - New spec and help.md format for the Hub
* 1.0.0 - Initial plugin

# Links

## References

* [git-clone](https://www.git-scm.com/docs/git-clone)
* [git-add](https://www.git-scm.com/docs/git-add)
* [git-rm](https://www.git-scm.com/docs/git-rm)

