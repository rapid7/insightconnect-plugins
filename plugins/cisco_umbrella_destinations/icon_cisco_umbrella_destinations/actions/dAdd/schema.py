# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Add a destination to the destination list"


class Input:
    COMMENT = "comment"
    DESTINATION = "destination"
    DESTINATIONLISTID = "destinationListId"


class Output:
    SUCCESS = "success"


class DAddInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Information about domain",
      "order": 3
    },
    "destination": {
      "type": "string",
      "title": "Destination Name",
      "description": "Title for the destination list",
      "order": 2
    },
    "destinationListId": {
      "type": "integer",
      "title": "Destination List ID",
      "description": "Unique ID for destination list",
      "order": 1
    }
  },
  "required": [
    "destination",
    "destinationListId"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DAddOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "$ref": "#/definitions/dlCollection",
      "title": "Success",
      "description": "Successful returned value",
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {
    "dlCollection": {
      "type": "object",
      "title": "dlCollection",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Unique ID of the destination list",
          "order": 1
        },
        "organizationId": {
          "type": "integer",
          "title": "Organization ID",
          "description": "ID of organization",
          "order": 2
        },
        "access": {
          "type": "string",
          "title": "Access",
          "description": "Allow or block access to domain",
          "order": 3
        },
        "isGlobal": {
          "type": "boolean",
          "title": "Is Global",
          "description": "Boolean value indicating global state",
          "order": 4
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Title for the destination list",
          "order": 5
        },
        "thirdpartyCategoryId": {
          "type": "integer",
          "title": "Third Party Category ID",
          "description": "ID, if any, for third parties",
          "order": 6
        },
        "createdAt": {
          "type": "integer",
          "title": "Created At",
          "description": "The unix UTC timestamp in milliseconds for creation of the destination list",
          "order": 7
        },
        "modifiedAt": {
          "type": "integer",
          "title": "Modified At",
          "description": "The unix UTC timestamp in milliseconds for modification of the destination list",
          "order": 8
        },
        "isMspDefault": {
          "type": "boolean",
          "title": "Is MSP Default",
          "description": "Whether or not MSP is default",
          "order": 9
        },
        "markedForDeletion": {
          "type": "boolean",
          "title": "Marked for Deletion",
          "description": "Whether or not destination list is marked for deletion",
          "order": 10
        },
        "meta": {
          "$ref": "#/definitions/meta",
          "title": "Metadata",
          "description": "Secondary information",
          "order": 11
        }
      }
    },
    "meta": {
      "type": "object",
      "title": "meta",
      "properties": {
        "destinationCount": {
          "type": "integer",
          "description": "Total number of destinations in a destination list",
          "order": 1
        },
        "domainCount": {
          "type": "integer",
          "description": "Total number of domains in a destination list",
          "order": 2
        },
        "urlCount": {
          "type": "integer",
          "description": "Total number of URLs in a destination list",
          "order": 3
        },
        "ipv4Count": {
          "type": "integer",
          "description": "Total number of IPs in a destination list",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
