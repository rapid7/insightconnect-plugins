# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Resolve an incident"


class Input:
    DESCRIPTION = "description"
    DETAILS = "details"
    INCIDENT_KEY = "incident_key"
    SERVICE_KEY = "service_key"
    

class Output:
    INCIDENT_KEY = "incident_key"
    MESSAGE = "message"
    STATUS = "status"
    

class SendResolveEventInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Text that will appear in the incident's log associated with this event",
      "order": 3
    },
    "details": {
      "type": "object",
      "title": "Details",
      "description": "An arbitrary JSON object containing any data you'd like included in the incident log",
      "order": 4
    },
    "incident_key": {
      "type": "string",
      "title": "Incident Key",
      "description": "Incident Key",
      "order": 2
    },
    "service_key": {
      "type": "string",
      "title": "Service Key",
      "description": "Service Key (aka Integration Key)",
      "order": 1
    }
  },
  "required": [
    "incident_key",
    "service_key"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SendResolveEventOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incident_key": {
      "type": "string",
      "title": "Incident Key",
      "description": "Incident Key",
      "order": 3
    },
    "message": {
      "type": "string",
      "title": "Message",
      "description": "Message",
      "order": 2
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Status",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
