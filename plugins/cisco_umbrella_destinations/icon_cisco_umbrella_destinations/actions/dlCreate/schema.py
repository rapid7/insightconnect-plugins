# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Create a destination list"


class Input:
    PAYLOAD = "payload"
    

class Output:
    SUCCESS = "success"
    

class DlCreateInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "payload": {
      "$ref": "#/definitions/dlCreate",
      "title": "Payload",
      "description": "List of destinations",
      "order": 1
    }
  },
  "required": [
    "payload"
  ],
  "definitions": {
    "destinations": {
      "type": "object",
      "title": "destinations",
      "properties": {
        "comment": {
          "type": "string",
          "title": "Comment",
          "description": "None",
          "order": 3
        },
        "destination": {
          "type": "string",
          "title": "Destination",
          "description": "Destination can be DOMAIN, URL or IP",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type can be DOMAIN, URL, IPV4",
          "order": 2
        }
      },
      "required": [
        "destination",
        "type"
      ]
    },
    "dlCreate": {
      "type": "object",
      "title": "dlCreate",
      "properties": {
        "access": {
          "type": "string",
          "title": "Access",
          "description": "Access can be allow or block. It defines destinationList type.",
          "order": 1
        },
        "destinations": {
          "type": "array",
          "title": "Destinations",
          "description": "Destinations to add to new list",
          "items": {
            "$ref": "#/definitions/destinations"
          },
          "order": 4
        },
        "isGlobal": {
          "type": "boolean",
          "title": "IsGlobal",
          "description": "IsGlobal can be true or false. There is only one default destination list of type allow or block for an organization.",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "None",
          "order": 3
        }
      },
      "required": [
        "access",
        "isGlobal",
        "name"
      ],
      "definitions": {
        "destinations": {
          "type": "object",
          "title": "destinations",
          "properties": {
            "comment": {
              "type": "string",
              "title": "Comment",
              "description": "None",
              "order": 3
            },
            "destination": {
              "type": "string",
              "title": "Destination",
              "description": "Destination can be DOMAIN, URL or IP",
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type can be DOMAIN, URL, IPV4",
              "order": 2
            }
          },
          "required": [
            "destination",
            "type"
          ]
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DlCreateOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "$ref": "#/definitions/dlEntity",
      "title": "Success",
      "description": "Successful returned value",
      "order": 1
    }
  },
  "required": [
    "success"
  ],
  "definitions": {
    "dlEntity": {
      "type": "object",
      "title": "dlEntity",
      "properties": {
        "access": {
          "type": "string",
          "title": "Access",
          "description": "Access can be allow or block. It defines destinationList type.",
          "order": 3
        },
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "Timestamp for CreatedAt",
          "format": "date-time",
          "order": 7
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Unique ID of the destination list.",
          "order": 1
        },
        "isGlobal": {
          "type": "boolean",
          "title": "Is Global",
          "description": "IsGlobal can be true or false. There is only one default destination list of type allow or block for an organization.",
          "order": 4
        },
        "isMspDefault": {
          "type": "boolean",
          "title": "Is MSP Default",
          "description": "Boolean for isMspDefault",
          "order": 9
        },
        "markedForDeletion": {
          "type": "boolean",
          "title": "Marked For Deletion",
          "description": "None",
          "order": 10
        },
        "meta": {
          "$ref": "#/definitions/meta",
          "title": "Meta Data",
          "description": "None",
          "order": 11
        },
        "modifiedAt": {
          "type": "string",
          "title": "Modified At",
          "displayType": "date",
          "description": "Timestamp for ModifiedAt",
          "format": "date-time",
          "order": 8
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the DL list",
          "order": 5
        },
        "organizationId": {
          "type": "integer",
          "title": "Organization ID",
          "description": "ID of organization",
          "order": 2
        },
        "thirdpartyCategoryId": {
          "type": "integer",
          "title": "Third Party Category ID",
          "description": "ID, if any, for third parties",
          "order": 6
        }
      },
      "definitions": {
        "meta": {
          "type": "object",
          "title": "meta",
          "properties": {
            "destinationCount": {
              "type": "integer",
              "title": "DestinationCount",
              "description": "Total number of destinations in a destination list.",
              "order": 1
            },
            "domainCount": {
              "type": "integer",
              "title": "DomainCount",
              "description": "Total number of domains in a destination list. Domains are part of total destinations in a destination lists.",
              "order": 2
            },
            "ipv4Count": {
              "type": "integer",
              "title": "Ipv4Count",
              "description": "Total number of IP's in a destination list. IP's are part of total destinations in destination lists.",
              "order": 4
            },
            "urlCount": {
              "type": "integer",
              "title": "UrlCount",
              "description": "Total number of URLs in a destination list. URLs are part of total destinations in a destination lists.",
              "order": 3
            }
          }
        }
      }
    },
    "meta": {
      "type": "object",
      "title": "meta",
      "properties": {
        "destinationCount": {
          "type": "integer",
          "title": "DestinationCount",
          "description": "Total number of destinations in a destination list.",
          "order": 1
        },
        "domainCount": {
          "type": "integer",
          "title": "DomainCount",
          "description": "Total number of domains in a destination list. Domains are part of total destinations in a destination lists.",
          "order": 2
        },
        "ipv4Count": {
          "type": "integer",
          "title": "Ipv4Count",
          "description": "Total number of IP's in a destination list. IP's are part of total destinations in destination lists.",
          "order": 4
        },
        "urlCount": {
          "type": "integer",
          "title": "UrlCount",
          "description": "Total number of URLs in a destination list. URLs are part of total destinations in a destination lists.",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
