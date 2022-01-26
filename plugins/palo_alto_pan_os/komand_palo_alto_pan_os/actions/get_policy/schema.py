# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get a policy by name. This action uses a direct connection to the firewall"


class Input:
    DEVICE_NAME = "device_name"
    POLICY_NAME = "policy_name"
    VIRTUAL_SYSTEM = "virtual_system"
    

class Output:
    ACTION = "action"
    APPLICATION = "application"
    CATEGORY = "category"
    DESTINATION = "destination"
    FROM = "from"
    HIP_PROFILES = "hip_profiles"
    SERVICE = "service"
    SOURCE = "source"
    SOURCE_USER = "source_user"
    TO = "to"
    

class GetPolicyInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "device_name": {
      "type": "string",
      "title": "Device Name",
      "description": "Device name",
      "default": "localhost.localdomain",
      "order": 2
    },
    "policy_name": {
      "type": "string",
      "title": "Policy Name",
      "description": "Policy name",
      "order": 1
    },
    "virtual_system": {
      "type": "string",
      "title": "Virtual System Name",
      "description": "Virtual system name",
      "default": "vsys1",
      "order": 3
    }
  },
  "required": [
    "device_name",
    "policy_name",
    "virtual_system"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetPolicyOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "action": {
      "type": "string",
      "title": "Action",
      "description": "Action",
      "order": 10
    },
    "application": {
      "type": "array",
      "title": "Application",
      "description": "Application",
      "items": {
        "type": "string"
      },
      "order": 7
    },
    "category": {
      "type": "array",
      "title": "Category",
      "description": "Category",
      "items": {
        "type": "string"
      },
      "order": 6
    },
    "destination": {
      "type": "array",
      "title": "Destination",
      "description": "Destination",
      "items": {
        "type": "string"
      },
      "order": 4
    },
    "from": {
      "type": "array",
      "title": "From",
      "description": "From",
      "items": {
        "type": "string"
      },
      "order": 2
    },
    "hip_profiles": {
      "type": "array",
      "title": "HIP Profiles",
      "description": "Host Information in Policy Enforcement profile",
      "items": {
        "type": "string"
      },
      "order": 9
    },
    "service": {
      "type": "array",
      "title": "Service",
      "description": "Service",
      "items": {
        "type": "string"
      },
      "order": 8
    },
    "source": {
      "type": "array",
      "title": "Source",
      "description": "Source",
      "items": {
        "type": "string"
      },
      "order": 3
    },
    "source_user": {
      "type": "array",
      "title": "Source User",
      "description": "Source user",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "to": {
      "type": "array",
      "title": "To",
      "description": "To",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
