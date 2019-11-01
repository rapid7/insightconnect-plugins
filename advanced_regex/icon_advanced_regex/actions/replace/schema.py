# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Regex search and replace string"


class Input:
    ASCII = "ascii"
    DOTALL = "dotall"
    IGNORECASE = "ignorecase"
    IN_REGEX = "in_regex"
    IN_STRING = "in_string"
    MAX_REPLACE = "max_replace"
    MULTILINE = "multiline"
    REPLACE_STRING = "replace_string"
    

class Output:
    RESULT = "result"
    

class ReplaceInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ascii": {
      "type": "boolean",
      "title": "ASCII",
      "description": "Make \\\\w \\\\W \\\\b \\\\B follow ASCII rules",
      "default": false,
      "order": 8
    },
    "dotall": {
      "type": "boolean",
      "title": "Dot All",
      "description": "Make . match newline",
      "default": false,
      "order": 7
    },
    "ignorecase": {
      "type": "boolean",
      "title": "Ignore Case",
      "description": "Make regex non-case sensitive",
      "default": false,
      "order": 5
    },
    "in_regex": {
      "type": "string",
      "title": "Regex",
      "description": "Regex to match",
      "order": 3
    },
    "in_string": {
      "type": "string",
      "title": "Input String",
      "description": "Input string",
      "order": 1
    },
    "max_replace": {
      "type": "integer",
      "title": "Max Replace",
      "description": "Max occurences to replace - if zero all will be replaced",
      "default": 0,
      "order": 4
    },
    "multiline": {
      "type": "boolean",
      "title": "Multiline",
      "description": "Make begin/end consider each line",
      "default": false,
      "order": 6
    },
    "replace_string": {
      "type": "string",
      "title": "New String",
      "description": "The string to replace matches with",
      "order": 2
    }
  },
  "required": [
    "in_regex",
    "in_string",
    "replace_string"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ReplaceOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result": {
      "type": "string",
      "title": "Result String",
      "description": "The result of the replace operation",
      "order": 1
    }
  },
  "required": [
    "result"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
