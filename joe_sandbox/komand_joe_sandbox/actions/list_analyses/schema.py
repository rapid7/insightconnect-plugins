# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Fetch a list of all analyses"


class Input:
    pass

class Output:
    ANALYSES = "analyses"
    

class ListAnalysesInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListAnalysesOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "analyses": {
      "type": "array",
      "title": "Analyses",
      "description": "A list of all analyses IDs",
      "items": {
        "$ref": "#/definitions/webid"
      },
      "order": 1
    }
  },
  "required": [
    "analyses"
  ],
  "definitions": {
    "webid": {
      "type": "object",
      "title": "webid",
      "properties": {
        "webid": {
          "type": "string",
          "title": "WebID",
          "description": "Web ID",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
