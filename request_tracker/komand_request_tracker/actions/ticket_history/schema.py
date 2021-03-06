# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Gets a list of all the history items for a given ticket"


class Input:
    TICKET_ID = "ticket_id"
    

class Output:
    HISTORY = "History"
    

class TicketHistoryInput(komand.Input):
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


class TicketHistoryOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "History": {
      "type": "array",
      "title": "History",
      "description": "History",
      "items": {
        "$ref": "#/definitions/HistoryEntry"
      },
      "order": 1
    }
  },
  "definitions": {
    "HistoryEntry": {
      "type": "object",
      "title": "HistoryEntry",
      "properties": {
        "Attachments": {
          "type": "array",
          "title": "Attachments",
          "items": {
            "type": "object"
          },
          "order": 13
        },
        "Content": {
          "type": "string",
          "title": "Content",
          "order": 10
        },
        "Created": {
          "type": "string",
          "title": "Created",
          "order": 12
        },
        "Creator": {
          "type": "string",
          "title": "Creator",
          "order": 11
        },
        "Data": {
          "type": "string",
          "title": "Data",
          "order": 8
        },
        "Description": {
          "type": "string",
          "title": "Description",
          "order": 9
        },
        "Field": {
          "type": "string",
          "title": "Field",
          "order": 5
        },
        "NewValue": {
          "type": "string",
          "title": "NewValue",
          "order": 7
        },
        "OldValue": {
          "type": "string",
          "title": "OldValue",
          "order": 6
        },
        "Ticket": {
          "type": "string",
          "title": "Ticket",
          "order": 2
        },
        "TimeTaken": {
          "type": "string",
          "title": "TimeTaken",
          "order": 3
        },
        "Type": {
          "type": "string",
          "title": "Type",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "Id",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
