# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Fetch details for the route with the given ID"


class Input:
    APP_ID = "app_id"
    ROUTE_ID = "route_id"
    

class Output:
    ROUTE = "route"
    

class GetRouteDetailsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "app_id": {
      "type": "string",
      "title": "App ID",
      "description": "App ID",
      "order": 1
    },
    "route_id": {
      "type": "string",
      "title": "Route ID",
      "description": "Route ID",
      "order": 2
    }
  },
  "required": [
    "app_id",
    "route_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetRouteDetailsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "route": {
      "$ref": "#/definitions/route",
      "title": "Route",
      "description": "Details for the provided route, including the route id, http method, route pattern used by the framework, and a code signature for the controller",
      "order": 1
    }
  },
  "definitions": {
    "route": {
      "type": "object",
      "title": "route",
      "properties": {
        "controller": {
          "type": "string",
          "title": "Controller",
          "description": "The name of the controller associated with the route (when applicable)",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The ID of the route",
          "order": 1
        },
        "method": {
          "type": "string",
          "title": "Method",
          "description": "The HTTP method (GET, POST, ...) for the route",
          "order": 2
        },
        "pattern": {
          "type": "string",
          "title": "Pattern",
          "description": "The path pattern for the route",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
