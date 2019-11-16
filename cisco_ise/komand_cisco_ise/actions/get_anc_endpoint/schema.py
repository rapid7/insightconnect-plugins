# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Returns ANC information based on the MAC address supplied"


class Input:
    MAC = "mac"
    

class Output:
    RESULTS = "results"
    

class GetAncEndpointInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "mac": {
      "type": "string",
      "title": "MAC Address",
      "description": "MAC address of the endpoint",
      "order": 1
    }
  },
  "required": [
    "mac"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAncEndpointOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results": {
      "$ref": "#/definitions/ANCEndpoint",
      "title": "Results",
      "description": "Endpoint information",
      "order": 1
    }
  },
  "definitions": {
    "ANCEndpoint": {
      "type": "object",
      "title": "ANCEndpoint",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ANC endpoint ID",
          "order": 1
        },
        "link": {
          "$ref": "#/definitions/link",
          "title": "Link",
          "description": "ANC endpoint link",
          "order": 4
        },
        "macAddress": {
          "type": "string",
          "title": "MAC Address",
          "description": "MAC Address of ANC endpoint",
          "order": 2
        },
        "policyName": {
          "type": "string",
          "title": "Policy Name",
          "description": "Policy Name",
          "order": 3
        }
      },
      "definitions": {
        "link": {
          "type": "object",
          "title": "link",
          "properties": {
            "href": {
              "type": "string",
              "title": "HREF",
              "description": "Hyper text reference",
              "order": 1
            },
            "rel": {
              "type": "string",
              "title": "Rel",
              "description": "Rel",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Type",
              "order": 3
            }
          }
        }
      }
    },
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "href": {
          "type": "string",
          "title": "HREF",
          "description": "Hyper text reference",
          "order": 1
        },
        "rel": {
          "type": "string",
          "title": "Rel",
          "description": "Rel",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
