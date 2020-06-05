# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Retrieve agent details"


class Input:
    AGENT = "agent"
    

class Output:
    AGENT = "agent"
    

class GetAgentDetailsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent": {
      "type": "string",
      "title": "Agent",
      "description": "Agent to retrieve device information from. Accepts IP address, MAC address, hostname, or device ID",
      "order": 1
    }
  },
  "required": [
    "agent"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAgentDetailsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agent": {
      "type": "object",
      "title": "Agent",
      "description": "Detailed information about agent found",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
