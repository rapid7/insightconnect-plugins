# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "List IPS rules"


class Input:
    COMPUTER_OR_POLICY = "computer_or_policy"
    ID = "id"
    

class Output:
    RULES_ASSIGNED = "rules_assigned"
    RULES_NOT_RECOMMENDED = "rules_not_recommended"
    RULES_RECOMMENDED = "rules_recommended"
    

class ListRulesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "computer_or_policy": {
      "type": "string",
      "title": "Target",
      "description": "Get IPS rules from a computer or policy",
      "enum": [
        "computer",
        "policy"
      ],
      "order": 1
    },
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "ID of the computer or policy",
      "order": 2
    }
  },
  "required": [
    "computer_or_policy",
    "id"
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
    "rules_assigned": {
      "type": "array",
      "title": "Rules Assigned",
      "description": "All IPS rules currently assigned",
      "items": {
        "type": "integer"
      },
      "order": 1
    },
    "rules_not_recommended": {
      "type": "array",
      "title": "Not recommended",
      "description": "IPS rules that are not recommended",
      "items": {
        "type": "integer"
      },
      "order": 3
    },
    "rules_recommended": {
      "type": "array",
      "title": "Recommended",
      "description": "Recommended IPS rules",
      "items": {
        "type": "integer"
      },
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
