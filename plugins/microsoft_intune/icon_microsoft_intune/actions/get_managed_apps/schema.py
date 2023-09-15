# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Returns InTune manageable apps"


class Input:
    APP = "app"
    

class Output:
    MANAGEDAPPS = "managedApps"
    

class GetManagedAppsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "app": {
      "type": "string",
      "title": "App",
      "description": "Application ID or name, if empty returns all applications",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetManagedAppsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "managedApps": {
      "type": "array",
      "title": "Managed Apps",
      "description": "Application details",
      "items": {
        "$ref": "#/definitions/value"
      },
      "order": 1
    }
  },
  "definitions": {
    "value": {
      "type": "object",
      "title": "value",
      "properties": {
        "@odata.context": {
          "type": "string",
          "title": "Odata Context",
          "description": "Odata context",
          "order": 2
        },
        "@odata.type": {
          "type": "string",
          "title": "Odata Type",
          "description": "Odata type",
          "order": 1
        },
        "appAvailability": {
          "type": "string",
          "title": "App Availability",
          "description": "App availability",
          "order": 17
        },
        "appStoreUrl": {
          "type": "string",
          "title": "App Store URL",
          "description": "App store URL",
          "order": 20
        },
        "createdDateTime": {
          "type": "string",
          "title": "Created Datetime",
          "description": "Created datetime",
          "order": 8
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 5
        },
        "developer": {
          "type": "string",
          "title": "Developer",
          "description": "Developer",
          "order": 14
        },
        "displayName": {
          "type": "string",
          "title": "Display Name",
          "description": "Display Name",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 3
        },
        "informationUrl": {
          "type": "string",
          "title": "Information URL",
          "description": "Information URL",
          "order": 12
        },
        "isFeatured": {
          "type": "boolean",
          "title": "Is Featured",
          "description": "Is featured",
          "order": 10
        },
        "largeIcon": {
          "type": "object",
          "title": "Large Icon",
          "description": "Large icon",
          "order": 7
        },
        "lastModifiedDateTime": {
          "type": "string",
          "title": "Last Modified Datetime",
          "description": "Last modified datetime",
          "order": 9
        },
        "minimumSupportedOperatingSystem": {
          "type": "object",
          "title": "Minimum Supported Operating System",
          "description": "Minimum supported operating system",
          "order": 21
        },
        "notes": {
          "type": "string",
          "title": "Notes",
          "description": "Notes",
          "order": 15
        },
        "owner": {
          "type": "string",
          "title": "Owner",
          "description": "Owner",
          "order": 13
        },
        "packageId": {
          "type": "string",
          "title": "Package ID",
          "description": "Package ID",
          "order": 19
        },
        "privacyInformationUrl": {
          "type": "string",
          "title": "Privacy Information URL",
          "description": "Privacy information URL",
          "order": 11
        },
        "publisher": {
          "type": "string",
          "title": "Publisher",
          "description": "Publisher",
          "order": 6
        },
        "publishingState": {
          "type": "string",
          "title": "Publishing State",
          "description": "Publishing state",
          "order": 16
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "Version",
          "order": 18
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
