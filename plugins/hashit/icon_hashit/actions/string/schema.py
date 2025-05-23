# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Generate hashes from text"


class Input:
    STRING = "string"


class Output:
    MD5 = "md5"
    SHA1 = "sha1"
    SHA256 = "sha256"
    SHA512 = "sha512"


class StringInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "string": {
      "type": "string",
      "description": "String of text to hash",
      "order": 1
    }
  },
  "required": [
    "string"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class StringOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "md5": {
      "type": "string",
      "title": "MD5 Hash",
      "description": "MD5 hash",
      "order": 1
    },
    "sha1": {
      "type": "string",
      "title": "SHA1 Hash",
      "description": "SHA1 hash",
      "order": 2
    },
    "sha256": {
      "type": "string",
      "title": "SHA256 Hash",
      "description": "SHA256 hash",
      "order": 3
    },
    "sha512": {
      "type": "string",
      "title": "SHA512 Hash",
      "description": "SHA512 hash",
      "order": 4
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
