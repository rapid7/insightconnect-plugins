# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Add hashed content to global blacklist. The input makes use of contentHash from the threat summary"


class Input:
    HASH = "hash"


class Output:
    AFFECTED = "affected"


class BlacklistByContentHashInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "hash": {
      "type": "string",
      "title": "Hash",
      "description": "Content hash to add to blacklist",
      "order": 1
    }
  },
  "required": [
    "hash"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class BlacklistByContentHashOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "affected": {
      "type": "integer",
      "title": "Affected",
      "description": "Number of entities affected by the requested operation",
      "order": 1
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
