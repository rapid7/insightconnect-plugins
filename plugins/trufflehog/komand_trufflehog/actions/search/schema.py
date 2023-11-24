# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Looks for exposed secrets in the git commit history and branches"


class Input:
    CUSTOM_REGEXES = "custom_regexes"
    DO_ENTROPY = "do_entropy"
    DO_REGEX = "do_regex"
    GIT_URL = "git_url"
    MAX_DEPTH = "max_depth"
    SINCE_COMMIT = "since_commit"


class Output:
    ISSUES = "issues"


class SearchInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "custom_regexes": {
      "type": "object",
      "title": "Custom Regex Rules",
      "description": "Ignores default regexes. Provide your own",
      "order": 4
    },
    "do_entropy": {
      "type": "boolean",
      "title": "Entropy Checks",
      "description": "Evaluates the shannon entropy for both the base64 char set and hexadecimal char set for every blob of text greater than 20 characters comprised of those character sets in each diff",
      "default": true,
      "order": 3
    },
    "do_regex": {
      "type": "boolean",
      "title": "Regex Checks",
      "description": "Enable high signal regex checks",
      "default": false,
      "order": 2
    },
    "git_url": {
      "type": "string",
      "title": "GitHub Repository URL",
      "description": "The git repository that is going to be searched e.g. https://github.com/jonschipp/islet",
      "order": 1
    },
    "max_depth": {
      "type": "integer",
      "title": "Max Depth",
      "description": "Max commit depth to go back when searching for secrets",
      "default": 1000000,
      "order": 6
    },
    "since_commit": {
      "type": "string",
      "title": "Since Commit Hash",
      "description": "Scan from a given commit hash",
      "order": 5
    }
  },
  "required": [
    "git_url"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "issues": {
      "type": "array",
      "title": "Issues",
      "description": "Issues found with TruffleHog",
      "items": {
        "$ref": "#/definitions/issue"
      },
      "order": 1
    }
  },
  "definitions": {
    "issue": {
      "type": "object",
      "title": "issue",
      "properties": {
        "date": {
          "type": "string",
          "order": 1
        },
        "path": {
          "type": "string",
          "description": "File path",
          "order": 2
        },
        "branch": {
          "type": "string",
          "description": "Commit branch",
          "order": 3
        },
        "commit": {
          "type": "string",
          "description": "Commit subject",
          "order": 4
        },
        "diff": {
          "type": "string",
          "order": 5
        },
        "stringsFound": {
          "type": "array",
          "title": "Strings Found",
          "description": "List of found strings",
          "items": {
            "type": "string"
          },
          "order": 6
        },
        "printfDiff": {
          "type": "string",
          "title": "Diff",
          "order": 7
        },
        "commitHash": {
          "type": "string",
          "title": "Commit Hash",
          "order": 8
        },
        "reason": {
          "type": "string",
          "order": 9
        },
        "url": {
          "type": "string",
          "title": "Commit URL",
          "description": "Commit URL",
          "order": 10
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
