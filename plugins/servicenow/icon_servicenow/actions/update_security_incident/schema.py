# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Update an existing security incident"


class Input:
    ADDITIONAL_FIELDS = "additional_fields"
    AFFECTED_USER = "affected_user"
    ASSIGNED_TO = "assigned_to"
    ASSIGNMENT_GROUP = "assignment_group"
    CALLER = "caller"
    CATEGORY = "category"
    CLOSE_CODE = "close_code"
    CLOSE_NOTES = "close_notes"
    CMDB_CI = "cmdb_ci"
    CONTACT_TYPE = "contact_type"
    DESCRIPTION = "description"
    LOCATION = "location"
    PRIORITY = "priority"
    SHORT_DESCRIPTION = "short_description"
    STATE = "state"
    SUBCATEGORY = "subcategory"
    SUBSTATE = "substate"
    SYS_ID = "sys_id"
    

class Output:
    NUMBER = "number"
    SYSTEM_ID = "system_id"
    

class UpdateSecurityIncidentInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "additional_fields": {
      "type": "object",
      "title": "Additional Fields",
      "description": "JSON object containing the additional fields and values to update security incident",
      "order": 18
    },
    "affected_user": {
      "type": "string",
      "title": "Affected User",
      "description": "The user ID, email or system ID of the user related to this security incident",
      "order": 6
    },
    "assigned_to": {
      "type": "string",
      "title": "Assigned To",
      "description": "The name, user ID, email or system id of the person primarily responsible for working this task",
      "order": 15
    },
    "assignment_group": {
      "type": "string",
      "title": "Assignment Group",
      "description": "The name or system id of the assignment group",
      "order": 14
    },
    "caller": {
      "type": "string",
      "title": "Requested By",
      "description": "The user ID, email or system ID of the person requesting the work to be done",
      "order": 4
    },
    "category": {
      "type": "string",
      "title": "Category",
      "description": "The code of the security incident category",
      "order": 8
    },
    "close_code": {
      "type": "string",
      "title": "Close Code",
      "description": "The code of the incident closure reason",
      "order": 16
    },
    "close_notes": {
      "type": "string",
      "title": "Close Notes",
      "description": "Incident closure notes",
      "order": 17
    },
    "cmdb_ci": {
      "type": "string",
      "title": "Configuration Item",
      "description": "The name or system ID of the configuration item",
      "order": 5
    },
    "contact_type": {
      "type": "string",
      "title": "Source",
      "description": "The code of the security incident source",
      "order": 12
    },
    "description": {
      "type": "string",
      "title": "Description",
      "description": "Description of the security incident",
      "order": 3
    },
    "location": {
      "type": "string",
      "title": "Location",
      "description": "The name or system ID of the location",
      "order": 7
    },
    "priority": {
      "type": "integer",
      "title": "Priority",
      "description": "The code of the priority in which an Incident needs to be resolved, based on impact and urgency",
      "order": 13
    },
    "short_description": {
      "type": "string",
      "title": "Short Description",
      "description": "Short description of the security incident",
      "order": 2
    },
    "state": {
      "type": "integer",
      "title": "State",
      "description": "The code of the security incident state",
      "order": 10
    },
    "subcategory": {
      "type": "string",
      "title": "Subcategory",
      "description": "The code of the security incident subcategory (available values depends on the `Category` field)",
      "order": 9
    },
    "substate": {
      "type": "integer",
      "title": "Substate",
      "description": "The code of the security incident substate",
      "order": 11
    },
    "sys_id": {
      "type": "string",
      "title": "System ID",
      "description": "The system ID of the security incident to be updated",
      "order": 1
    }
  },
  "required": [
    "sys_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class UpdateSecurityIncidentOutput(insightconnect_plugin_runtime.Output):
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
