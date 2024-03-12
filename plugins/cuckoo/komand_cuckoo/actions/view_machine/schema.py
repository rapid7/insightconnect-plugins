# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Returns details on the analysis machine associated with the given name"


class Input:
    MACHINE_NAME = "machine_name"


class Output:
    MACHINE = "machine"


class ViewMachineInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "machine_name": {
      "type": "string",
      "description": "Machine name",
      "order": 1
    }
  },
  "required": [
    "machine_name"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ViewMachineOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "machine": {
      "$ref": "#/definitions/machine",
      "description": "Machine details",
      "order": 1
    }
  },
  "required": [
    "machine"
  ],
  "definitions": {
    "machine": {
      "type": "object",
      "title": "machine",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "order": 1
        },
        "interface": {
          "type": "string",
          "order": 2
        },
        "ip": {
          "type": "string",
          "title": "IP",
          "order": 3
        },
        "label": {
          "type": "string",
          "order": 4
        },
        "locked": {
          "type": "boolean",
          "title": "Locked?",
          "order": 5
        },
        "locked_changed_on": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "title": "Date on which locked status was changed",
          "order": 6
        },
        "name": {
          "type": "string",
          "order": 7
        },
        "platform": {
          "type": "string",
          "order": 8
        },
        "resultserver_ip": {
          "type": "string",
          "title": "Resultserver IP",
          "order": 9
        },
        "resultserver_port": {
          "type": "integer",
          "title": "Resultserver Port",
          "order": 10
        },
        "snapshot": {
          "type": "string",
          "order": 11
        },
        "status": {
          "type": "string",
          "order": 12
        },
        "status_changed_on": {
          "type": "string",
          "format": "date-time",
          "displayType": "date",
          "description": "Date on which status was changed",
          "order": 13
        },
        "tags": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "order": 14
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
