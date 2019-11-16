# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Gets the ticket links for a single ticket"


class Input:
    TICKET_ID = "ticket_id"
    

class Output:
    DEPENDEDONBY = "DependedonBy"
    DEPENDSON = "DependsOn"
    HASMEMBER = "HasMember"
    MEMBEROF = "MemberOf"
    REFERREDTOBY = "ReferredToBy"
    REFERSTO = "RefersTo"
    

class TicketLinksInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ticket_id": {
      "type": "integer",
      "title": "Ticket ID",
      "description": "Ticket ID e.g. 3",
      "order": 1
    }
  },
  "required": [
    "ticket_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TicketLinksOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "DependedonBy": {
      "type": "array",
      "title": "Depended On By",
      "description": "Depended on by",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "DependsOn": {
      "type": "array",
      "title": "Depends On",
      "description": "Depends On",
      "items": {
        "type": "string"
      },
      "order": 6
    },
    "HasMember": {
      "type": "string",
      "title": "Has Member",
      "description": "Has member",
      "order": 1
    },
    "MemberOf": {
      "type": "string",
      "title": "Member Of",
      "description": "Member of",
      "order": 4
    },
    "ReferredToBy": {
      "type": "string",
      "title": "Referred To By",
      "description": "Referred to by",
      "order": 2
    },
    "RefersTo": {
      "type": "string",
      "title": "Refers To",
      "description": "Refers to",
      "order": 5
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
