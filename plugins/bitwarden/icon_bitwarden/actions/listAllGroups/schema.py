# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Return a list of your organization's groups. Group objects listed in this call do not include information about their associated collections"


class Input:
    pass

class Output:
    GROUPS = "groups"
    

class ListAllGroupsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListAllGroupsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "groups": {
      "type": "array",
      "title": "Groups",
      "description": "List of groups",
      "items": {
        "$ref": "#/definitions/group"
      },
      "order": 1
    }
  },
  "definitions": {
    "group": {
      "type": "object",
      "title": "group",
      "properties": {
        "accessAll": {
          "type": "boolean",
          "title": "Access All",
          "description": "Determines if this group can access all collections within the organization, or only the associated collections. If set to 'true', this option overrides any collection assignments",
          "order": 2
        },
        "externalId": {
          "type": "string",
          "title": "External ID",
          "description": "External identifier for reference or linking this group to another system, such as a user director",
          "order": 3
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The group's unique identifier",
          "order": 4
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the group",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
