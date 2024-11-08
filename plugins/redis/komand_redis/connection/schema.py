# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Input:
    DB = "db"
    HOST = "host"
    PORT = "port"


class ConnectionSchema(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "db": {
      "type": "integer",
      "description": "DB to use usually (0-15)",
      "default": 0,
      "order": 3
    },
    "host": {
      "type": "string",
      "description": "Host, e.g. 10.4.4.4",
      "order": 1
    },
    "port": {
      "type": "integer",
      "description": "Port",
      "default": 6379,
      "order": 2
    }
  },
  "required": [
    "db",
    "host",
    "port"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
