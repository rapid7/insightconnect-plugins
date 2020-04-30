# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "List IPS rules"


class Input:
    ID = "id"
    SCOPE = "scope"
    

class Output:
    COVERED_CVES = "covered_cves"
    RESPONSE_JSON = "response_json"
    RULES_ASSIGNED = "rules_assigned"
    

class ListRulesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "ID of the computer or policy",
      "order": 2
    },
    "scope": {
      "type": "string",
      "title": "Scope",
      "description": "Set the scope",
      "enum": [
        "computer",
        "policy"
      ],
      "order": 1
    }
  },
  "required": [
    "scope"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListRulesOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "covered_cves": {
      "type": "array",
      "title": "CVEs",
      "description": "CVEs covered by the assigned rules",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "response_json": {
      "type": "object",
      "title": "Response JSON",
      "description": "Full response in JSON format",
      "order": 3
    },
    "rules_assigned": {
      "type": "array",
      "title": "Rules Assigned",
      "description": "All IPS rules currently assigned",
      "items": {
        "type": "integer"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
