# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This action is used to get all bookmarks for a given incident"


class Input:
    INCIDENTID = "incidentId"
    RESOURCEGROUPNAME = "resourceGroupName"
    SUBSCRIPTIONID = "subscriptionId"
    WORKSPACENAME = "workspaceName"
    

class Output:
    BOOKMARKS = "bookmarks"
    

class ListBookmarksInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incidentId": {
      "type": "string",
      "title": "Incident ID",
      "description": "Incident ID",
      "order": 1
    },
    "resourceGroupName": {
      "type": "string",
      "title": "Resource Group Name",
      "description": "The name of the resource group within the user's subscription",
      "order": 2
    },
    "subscriptionId": {
      "type": "string",
      "title": "Subscription ID",
      "description": "Azure subscription ID",
      "order": 3
    },
    "workspaceName": {
      "type": "string",
      "title": "Workspace Name",
      "description": "The name of the workspace",
      "order": 4
    }
  },
  "required": [
    "incidentId",
    "resourceGroupName",
    "subscriptionId",
    "workspaceName"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListBookmarksOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "bookmarks": {
      "type": "array",
      "title": "Bookmark List",
      "description": "All the bookmarks assigned to the given incident",
      "items": {
        "$ref": "#/definitions/HuntingBookmark"
      },
      "order": 1
    }
  },
  "definitions": {
    "CreatedByType": {
      "type": "object",
      "title": "CreatedByType",
      "properties": {
        "Application": {
          "type": "string",
          "title": "Application",
          "description": "Application",
          "order": 1
        },
        "Key": {
          "type": "string",
          "title": "Key",
          "description": "Description",
          "order": 2
        },
        "ManagedIdentity": {
          "type": "string",
          "title": "Managed Identity",
          "description": "Managed identity",
          "order": 3
        },
        "User": {
          "type": "string",
          "title": "User",
          "description": "User",
          "order": 4
        }
      }
    },
    "HuntingBookmark": {
      "type": "object",
      "title": "HuntingBookmark",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Resource ID",
          "order": 1
        },
        "kind": {
          "type": "string",
          "title": "Kind",
          "description": "The kind of the entity",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Resource name",
          "order": 3
        },
        "properties": {
          "$ref": "#/definitions/HuntingBookmarkProperties",
          "title": "Properties",
          "description": "Hunting bookmark properties",
          "order": 6
        },
        "systemData": {
          "$ref": "#/definitions/SystemData",
          "title": "System Data",
          "description": "Azure Resource Manager metadata containing createdBy and modifiedBy information",
          "order": 4
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Azure resource type",
          "order": 5
        }
      },
      "definitions": {
        "CreatedByType": {
          "type": "object",
          "title": "CreatedByType",
          "properties": {
            "Application": {
              "type": "string",
              "title": "Application",
              "description": "Application",
              "order": 1
            },
            "Key": {
              "type": "string",
              "title": "Key",
              "description": "Description",
              "order": 2
            },
            "ManagedIdentity": {
              "type": "string",
              "title": "Managed Identity",
              "description": "Managed identity",
              "order": 3
            },
            "User": {
              "type": "string",
              "title": "User",
              "description": "User",
              "order": 4
            }
          }
        },
        "HuntingBookmarkProperties": {
          "type": "object",
          "title": "HuntingBookmarkProperties",
          "properties": {
            "additionalData": {
              "type": "object",
              "title": "Additional Data",
              "description": "Custom fields that should be part of the entity and will be presented to the user",
              "order": 1
            },
            "created": {
              "type": "string",
              "title": "Created",
              "displayType": "date",
              "description": "The time the bookmark was created",
              "format": "date-time",
              "order": 2
            },
            "createdBy": {
              "$ref": "#/definitions/UserInfo",
              "title": "Created By",
              "description": "Describes a user that created the bookmark",
              "order": 3
            },
            "displayName": {
              "type": "string",
              "title": "Display Name",
              "description": "The display name of the bookmark",
              "order": 4
            },
            "eventTime": {
              "type": "string",
              "title": "Event Time",
              "displayType": "date",
              "description": "The time of the event",
              "format": "date-time",
              "order": 5
            },
            "friendlyName": {
              "type": "string",
              "title": "Friendly Name",
              "description": "The graph item display name which is a short human-readable description of the graph item instance",
              "order": 6
            },
            "incidentInfo": {
              "type": "object",
              "title": "Incident Info",
              "description": "Describes an incident that relates to bookmark",
              "order": 7
            },
            "labels": {
              "type": "array",
              "title": "Labels",
              "description": "List of labels relevant to this bookmark",
              "items": {
                "type": "string"
              },
              "order": 8
            },
            "notes": {
              "type": "string",
              "title": "Notes",
              "description": "The notes of the bookmark",
              "order": 9
            },
            "query": {
              "type": "string",
              "title": "Query",
              "description": "The query of the bookmark",
              "order": 10
            },
            "queryResult": {
              "type": "string",
              "title": "Query Result",
              "description": "The query result of the bookmark",
              "order": 11
            },
            "updated": {
              "type": "string",
              "title": "Updated",
              "displayType": "date",
              "description": "The last time the bookmark was updated",
              "format": "date-time",
              "order": 12
            },
            "updatedBy": {
              "$ref": "#/definitions/UserInfo",
              "title": "Updated By",
              "description": "Describes a user that updated the bookmark",
              "order": 13
            }
          },
          "definitions": {
            "UserInfo": {
              "type": "object",
              "title": "UserInfo",
              "properties": {
                "email": {
                  "type": "string",
                  "title": "Email",
                  "description": "The email of the user",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "The name of the user",
                  "order": 2
                },
                "objectId": {
                  "type": "string",
                  "title": "Object Identification",
                  "description": "The object ID of the user",
                  "order": 3
                }
              }
            }
          }
        },
        "SystemData": {
          "type": "object",
          "title": "SystemData",
          "properties": {
            "createdAt": {
              "type": "string",
              "title": "Created At",
              "displayType": "date",
              "description": "The timestamp of resource creation (UTC)",
              "format": "date-time",
              "order": 1
            },
            "createdBy": {
              "type": "string",
              "title": "Created By",
              "description": "The identity that created the resource",
              "order": 2
            },
            "createdByType": {
              "$ref": "#/definitions/CreatedByType",
              "title": "Created By Type",
              "description": "The type of identity that created the resource",
              "order": 3
            },
            "lastModifiedAt": {
              "type": "string",
              "title": "Last Modified At",
              "displayType": "date",
              "description": "The timestamp of resource last modification (UTC)",
              "format": "date-time",
              "order": 4
            },
            "lastModifiedBy": {
              "type": "string",
              "title": "Last Modified By",
              "description": "The identity that last modified the resource",
              "order": 5
            },
            "lastModifiedByType": {
              "$ref": "#/definitions/CreatedByType",
              "title": "Last Modified By Type",
              "description": "The type of identity that last modified the resource",
              "order": 6
            }
          },
          "definitions": {
            "CreatedByType": {
              "type": "object",
              "title": "CreatedByType",
              "properties": {
                "Application": {
                  "type": "string",
                  "title": "Application",
                  "description": "Application",
                  "order": 1
                },
                "Key": {
                  "type": "string",
                  "title": "Key",
                  "description": "Description",
                  "order": 2
                },
                "ManagedIdentity": {
                  "type": "string",
                  "title": "Managed Identity",
                  "description": "Managed identity",
                  "order": 3
                },
                "User": {
                  "type": "string",
                  "title": "User",
                  "description": "User",
                  "order": 4
                }
              }
            }
          }
        },
        "UserInfo": {
          "type": "object",
          "title": "UserInfo",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "description": "The email of the user",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the user",
              "order": 2
            },
            "objectId": {
              "type": "string",
              "title": "Object Identification",
              "description": "The object ID of the user",
              "order": 3
            }
          }
        }
      }
    },
    "HuntingBookmarkProperties": {
      "type": "object",
      "title": "HuntingBookmarkProperties",
      "properties": {
        "additionalData": {
          "type": "object",
          "title": "Additional Data",
          "description": "Custom fields that should be part of the entity and will be presented to the user",
          "order": 1
        },
        "created": {
          "type": "string",
          "title": "Created",
          "displayType": "date",
          "description": "The time the bookmark was created",
          "format": "date-time",
          "order": 2
        },
        "createdBy": {
          "$ref": "#/definitions/UserInfo",
          "title": "Created By",
          "description": "Describes a user that created the bookmark",
          "order": 3
        },
        "displayName": {
          "type": "string",
          "title": "Display Name",
          "description": "The display name of the bookmark",
          "order": 4
        },
        "eventTime": {
          "type": "string",
          "title": "Event Time",
          "displayType": "date",
          "description": "The time of the event",
          "format": "date-time",
          "order": 5
        },
        "friendlyName": {
          "type": "string",
          "title": "Friendly Name",
          "description": "The graph item display name which is a short human-readable description of the graph item instance",
          "order": 6
        },
        "incidentInfo": {
          "type": "object",
          "title": "Incident Info",
          "description": "Describes an incident that relates to bookmark",
          "order": 7
        },
        "labels": {
          "type": "array",
          "title": "Labels",
          "description": "List of labels relevant to this bookmark",
          "items": {
            "type": "string"
          },
          "order": 8
        },
        "notes": {
          "type": "string",
          "title": "Notes",
          "description": "The notes of the bookmark",
          "order": 9
        },
        "query": {
          "type": "string",
          "title": "Query",
          "description": "The query of the bookmark",
          "order": 10
        },
        "queryResult": {
          "type": "string",
          "title": "Query Result",
          "description": "The query result of the bookmark",
          "order": 11
        },
        "updated": {
          "type": "string",
          "title": "Updated",
          "displayType": "date",
          "description": "The last time the bookmark was updated",
          "format": "date-time",
          "order": 12
        },
        "updatedBy": {
          "$ref": "#/definitions/UserInfo",
          "title": "Updated By",
          "description": "Describes a user that updated the bookmark",
          "order": 13
        }
      },
      "definitions": {
        "UserInfo": {
          "type": "object",
          "title": "UserInfo",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "description": "The email of the user",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "The name of the user",
              "order": 2
            },
            "objectId": {
              "type": "string",
              "title": "Object Identification",
              "description": "The object ID of the user",
              "order": 3
            }
          }
        }
      }
    },
    "SystemData": {
      "type": "object",
      "title": "SystemData",
      "properties": {
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "displayType": "date",
          "description": "The timestamp of resource creation (UTC)",
          "format": "date-time",
          "order": 1
        },
        "createdBy": {
          "type": "string",
          "title": "Created By",
          "description": "The identity that created the resource",
          "order": 2
        },
        "createdByType": {
          "$ref": "#/definitions/CreatedByType",
          "title": "Created By Type",
          "description": "The type of identity that created the resource",
          "order": 3
        },
        "lastModifiedAt": {
          "type": "string",
          "title": "Last Modified At",
          "displayType": "date",
          "description": "The timestamp of resource last modification (UTC)",
          "format": "date-time",
          "order": 4
        },
        "lastModifiedBy": {
          "type": "string",
          "title": "Last Modified By",
          "description": "The identity that last modified the resource",
          "order": 5
        },
        "lastModifiedByType": {
          "$ref": "#/definitions/CreatedByType",
          "title": "Last Modified By Type",
          "description": "The type of identity that last modified the resource",
          "order": 6
        }
      },
      "definitions": {
        "CreatedByType": {
          "type": "object",
          "title": "CreatedByType",
          "properties": {
            "Application": {
              "type": "string",
              "title": "Application",
              "description": "Application",
              "order": 1
            },
            "Key": {
              "type": "string",
              "title": "Key",
              "description": "Description",
              "order": 2
            },
            "ManagedIdentity": {
              "type": "string",
              "title": "Managed Identity",
              "description": "Managed identity",
              "order": 3
            },
            "User": {
              "type": "string",
              "title": "User",
              "description": "User",
              "order": 4
            }
          }
        }
      }
    },
    "UserInfo": {
      "type": "object",
      "title": "UserInfo",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "description": "The email of the user",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "The name of the user",
          "order": 2
        },
        "objectId": {
          "type": "string",
          "title": "Object Identification",
          "description": "The object ID of the user",
          "order": 3
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
