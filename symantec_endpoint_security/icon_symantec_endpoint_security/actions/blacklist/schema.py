# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Blacklist an MD5 or SHA256 hash"


class Input:
    DESCRIPTION = "description"
    DOMAIN_ID = "domain_id"
    HASHES = "hashes"
    NAME = "name"
    

class Output:
    BLACKLIST_ID = "blacklist_id"
    

class BlacklistInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Description for the blacklist",
      "order": 2
    },
    "domain_id": {
      "type": "string",
      "title": "Domain ID",
      "description": "ID of the domain to apply the blacklist to",
      "order": 4
    },
    "hashes": {
      "type": "array",
      "title": "Hashes",
      "description": "Hashes (MD5 or SHA256) to add to the blacklist",
      "items": {
        "type": "string"
      },
      "order": 1
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name for the blacklist",
      "order": 3
    }
  },
  "required": [
    "description",
    "domain_id",
    "hashes",
    "name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class BlacklistOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "blacklist_id": {
      "type": "string",
      "title": "Blacklist ID",
      "description": "ID of the resulting blacklist",
      "order": 1
    }
  },
  "required": [
    "blacklist_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
