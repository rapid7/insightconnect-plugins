# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Restart a virtual machine"


class Input:
    RESOURCEGROUP = "resourceGroup"
    SUBSCRIPTIONID = "subscriptionId"
    VM = "vm"
    

class Output:
    STATUS_CODE = "status_code"
    

class RestartVmInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "resourceGroup": {
      "type": "string",
      "title": "Resource Group",
      "description": "The resource group that will contain the virtual machine",
      "order": 2
    },
    "subscriptionId": {
      "type": "string",
      "title": "Subscription ID",
      "description": "The identifier of your subscription",
      "order": 1
    },
    "vm": {
      "type": "string",
      "title": "Name of Virtual Machine",
      "description": "The name of the virtual machine",
      "order": 3
    }
  },
  "required": [
    "resourceGroup",
    "subscriptionId",
    "vm"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RestartVmOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status_code": {
      "type": "integer",
      "title": "Status",
      "description": "HTTP status code",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
