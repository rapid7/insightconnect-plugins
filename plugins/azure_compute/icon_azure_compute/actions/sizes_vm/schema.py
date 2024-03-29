# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "List available virtual machine sizes for resizing"


class Input:
    RESOURCEGROUP = "resourceGroup"
    SUBSCRIPTIONID = "subscriptionId"
    VM = "vm"


class Output:
    VALUE = "value"


class SizesVmInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
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
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SizesVmOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "value": {
      "type": "array",
      "title": "Value",
      "description": "List sizes",
      "items": {
        "$ref": "#/definitions/value_size_vm"
      },
      "order": 1
    }
  },
  "definitions": {
    "value_size_vm": {
      "type": "object",
      "title": "value_size_vm",
      "properties": {
        "maxDataDiskCount": {
          "type": "integer",
          "title": "Max Data Disk Count",
          "description": "Specifies the maximum number of data disks that can be attached to the VM size",
          "order": 1
        },
        "memoryInMB": {
          "type": "integer",
          "title": "Memory In MB",
          "description": "Specifies the available ram in mb",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Specifies the name of the virtual machine size",
          "order": 3
        },
        "numberOfCores": {
          "type": "integer",
          "title": "Number Of Cores",
          "description": "Specifies the number of available CPU cores",
          "order": 4
        },
        "osDiskSizeInMB": {
          "type": "integer",
          "title": "OS Disk Size In MB",
          "description": "Specifies the size in mb of the operating system disk",
          "order": 5
        },
        "resourceDiskSizeInMB": {
          "type": "integer",
          "title": "Resource Disk Size In MB",
          "description": "Specifies the size in mb of the temporary or resource disk",
          "order": 6
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
