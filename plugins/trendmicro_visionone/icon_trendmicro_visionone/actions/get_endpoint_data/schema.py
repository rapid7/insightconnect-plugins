# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieves information about a specific endpoint"


class Input:
    ENDPOINT = "endpoint"
    QUERY_OP = "query_op"
    

class Output:
    ENDPOINT_DATA = "endpoint_data"
    

class GetEndpointDataInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "endpoint": {
      "type": "string",
      "title": "Endpoint",
      "description": "hostname, macAddress, agentGuid or ip of the endpoint to query",
      "order": 1
    },
    "query_op": {
      "type": "string",
      "title": "Query Operator",
      "description": "Logical operator to employ in the query. (AND/OR)",
      "default": " or ",
      "enum": [
        " or ",
        " and "
      ],
      "order": 2
    }
  },
  "required": [
    "endpoint",
    "query_op"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetEndpointDataOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "endpoint_data": {
      "type": "array",
      "title": "Endpoint Data",
      "description": "Array of Endpoint Data Objects, consisting of agent guid, login account, endpoint name, mac address, ip, os name, or version, os description, product code and installed product code",
      "items": {
        "$ref": "#/definitions/endpoint_data"
      },
      "order": 1
    }
  },
  "required": [
    "endpoint_data"
  ],
  "definitions": {
    "endpoint_data": {
      "type": "object",
      "title": "endpoint_data",
      "properties": {
        "agent_guid": {
          "type": "string",
          "title": "Agent GUID",
          "description": "Unique alphanumeric string that identifies an endpoint agent on the Trend Vision One platform",
          "order": 1
        },
        "endpoint_name": {
          "type": "object",
          "title": "Endpoint Name",
          "description": "Hostname of an endpoint with timestamp",
          "order": 3
        },
        "installed_product_codes": {
          "type": "string",
          "title": "Installed Product Codes",
          "description": "3-character code that identifies the installed Trend Micro products on an endpoint",
          "enum": [
            "sao",
            "sds",
            "xes"
          ],
          "order": 10
        },
        "ip": {
          "type": "object",
          "title": "IP",
          "description": "IPs of an endpoint with timestamp",
          "order": 5
        },
        "login_account": {
          "type": "object",
          "title": "Login Account",
          "description": "User accounts of an endpoint with timestamp",
          "order": 2
        },
        "mac_address": {
          "type": "object",
          "title": "MAC Address",
          "description": "MAC Address of an endpoint with timestamp",
          "order": 4
        },
        "os_description": {
          "type": "string",
          "title": "OS Description",
          "description": "Description of the operating system installed on an endpoint",
          "order": 8
        },
        "os_name": {
          "type": "string",
          "title": "OS Name",
          "description": "Operating system installed on an endpoint",
          "enum": [
            "Linux",
            "Windows",
            "macOS",
            "macOSX"
          ],
          "order": 6
        },
        "os_version": {
          "type": "string",
          "title": "OS Version",
          "description": "Version of the operating system installed on an endpoint",
          "order": 7
        },
        "product_code": {
          "type": "string",
          "title": "Product Code",
          "description": "3-character code that identifies Trend Micro products",
          "enum": [
            "sao",
            "sds",
            "xes"
          ],
          "order": 9
        }
      },
      "required": [
        "agent_guid",
        "endpoint_name",
        "installed_product_codes",
        "ip",
        "login_account",
        "mac_address",
        "os_description",
        "os_name",
        "os_version",
        "product_code"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
