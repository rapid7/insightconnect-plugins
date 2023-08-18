# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a new security incident"


class Input:
    ADDITIONAL_FIELDS = "additional_fields"
    AFFECTED_USER = "affected_user"
    ASSIGNED_TO = "assigned_to"
    ASSIGNMENT_GROUP = "assignment_group"
    CALLER = "caller"
    CATEGORY = "category"
    CMDB_CI = "cmdb_ci"
    CONTACT_TYPE = "contact_type"
    DESCRIPTION = "description"
    LOCATION = "location"
    PRIORITY = "priority"
    SHORT_DESCRIPTION = "short_description"
    STATE = "state"
    SUBCATEGORY = "subcategory"
    SUBSTATE = "substate"
    

class Output:
    NUMBER = "number"
    SYSTEM_ID = "system_id"
    

class CreateSecurityIncidentInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "additional_fields": {
      "type": "object",
      "title": "Additional Fields",
      "description": "JSON object containing the additional fields and values to create security incident",
      "order": 15
    },
    "affected_user": {
      "type": "string",
      "title": "Affected User",
      "description": "The user ID, email or system ID of the user related to this security incident",
      "order": 5
    },
    "assigned_to": {
      "type": "string",
      "title": "Assigned To",
      "description": "The name, user ID, email or system id of the person primarily responsible for working this task",
      "order": 14
    },
    "assignment_group": {
      "type": "string",
      "title": "Assignment Group",
      "description": "The name or system id of the assignment group",
      "order": 13
    },
    "caller": {
      "type": "string",
      "title": "Requested By",
      "description": "The user ID, email or system ID of the person requesting the work to be done",
      "order": 3
    },
    "category": {
      "type": "string",
      "title": "Category",
      "description": "The code of the security incident category",
      "order": 7
    },
    "cmdb_ci": {
      "type": "string",
      "title": "Configuration Item",
      "description": "The name or system ID of the configuration item",
      "order": 4
    },
    "contact_type": {
      "type": "string",
      "title": "Source",
      "description": "The code of the security incident source",
      "order": 11
    },
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Description of the created security incident",
      "order": 2
    },
    "location": {
      "type": "string",
      "title": "Location",
      "description": "The name or system ID of the location",
      "order": 6
    },
    "priority": {
      "type": "integer",
      "title": "Priority",
      "description": "The code of the priority in which an Incident needs to be resolved, based on impact and urgency",
      "order": 12
    },
    "short_description": {
      "type": "string",
      "title": "Short Description",
      "description": "Short description of the created security incident",
      "order": 1
    },
    "state": {
      "type": "integer",
      "title": "State",
      "description": "The code of the security incident state",
      "order": 9
    },
    "subcategory": {
      "type": "string",
      "title": "Subcategory",
      "description": "The code of the security incident subcategory (available values depends on the `Category` field)",
      "order": 8
    },
    "substate": {
      "type": "integer",
      "title": "Substate",
      "description": "The code of the security incident substate",
      "order": 10
    }
  },
  "required": [
    "short_description"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateSecurityIncidentOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "number": {
      "type": "string",
      "title": "Number",
      "description": "Number of the security incident",
      "order": 2
    },
    "system_id": {
      "type": "string",
      "title": "System ID",
      "description": "System ID of the security incident",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
