# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Quarantine a host"


class Input:
    MAC_ADDRESS = "mac_address"
    POLICY = "policy"
    

class Output:
    ERS_ANC_ENDPOINT = "ers_anc_endpoint"
    

class QuarantineInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "mac_address": {
      "type": "string",
      "title": "MAC Address",
      "description": "The host MAC address",
      "order": 1
    },
    "policy": {
      "type": "string",
      "title": "Policy",
      "description": "The quarantine policy to apply",
      "order": 2
    }
  },
  "required": [
    "mac_address",
    "policy"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class QuarantineOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ers_anc_endpoint": {
      "$ref": "#/definitions/ErsAncEndpoint",
      "title": "ERS ANC Endpoint",
      "description": "Returns info on the endpoint and what policy was applied",
      "order": 1
    }
  },
  "definitions": {
    "ErsAncEndpoint": {
      "type": "object",
      "title": "ErsAncEndpoint",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ERS endpoint ID",
          "order": 1
        },
        "link": {
          "$ref": "#/definitions/link",
          "title": "Link",
          "description": "Link",
          "order": 4
        },
        "macAddress": {
          "type": "string",
          "title": "MAC Address",
          "description": "ERS endpoint MAC address",
          "order": 2
        },
        "policyName": {
          "type": "string",
          "title": "Policy Name",
          "description": "Name of the policy applied to the ERS endpoint",
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
