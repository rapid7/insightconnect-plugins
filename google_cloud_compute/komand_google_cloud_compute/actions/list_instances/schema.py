# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This action is used to retrieve the list of instances contained within the specified zone"


class Input:
    FILTER = "filter"
    MAXRESULTS = "maxResults"
    ORDERBY = "orderBy"
    ZONE = "zone"
    

class Output:
    ID = "id"
    ITEMS = "items"
    KIND = "kind"
    SELFLINK = "selfLink"
    

class ListInstancesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "filter": {
      "type": "string",
      "title": "Filter",
      "description": "Sets a filter expression for filtering listed resources",
      "order": 2
    },
    "maxResults": {
      "type": "integer",
      "title": "Max Results",
      "description": "The maximum number of results per page that should be returned. Acceptable values are 0 to 500. Default 500",
      "order": 3
    },
    "orderBy": {
      "type": "string",
      "title": "OrderBy",
      "description": "Sorts list results by a certain order",
      "order": 4
    },
    "zone": {
      "type": "string",
      "title": "Zone",
      "description": "The name of the zone for this request",
      "order": 1
    }
  },
  "required": [
    "zone"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListInstancesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "string",
      "title": "ID",
      "description": "The unique identifier for the resource. This identifier is defined by the server",
      "order": 2
    },
    "items": {
      "type": "array",
      "title": "Items",
      "description": "A list of instances",
      "items": {
        "$ref": "#/definitions/items_instance"
      },
      "order": 3
    },
    "kind": {
      "type": "string",
      "title": "Kind",
      "description": "Type of resource. Always compute#instanceList for lists of Instance resources",
      "order": 1
    },
    "selfLink": {
      "type": "string",
      "title": "Self Link",
      "description": "The unique identifier for the resource. This identifier is defined by the server",
      "order": 4
    }
  },
  "definitions": {
    "accessConfigs": {
      "type": "object",
      "title": "accessConfigs",
      "properties": {
        "kind": {
          "type": "string",
          "title": "Kind",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 2
        },
        "natIP": {
          "type": "string",
          "title": "NatIP",
          "order": 3
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 4
        }
      }
    },
    "disks": {
      "type": "object",
      "title": "disks",
      "properties": {
        "autoDelete": {
          "type": "boolean",
          "title": "AutoDelete",
          "order": 1
        },
        "boot": {
          "type": "boolean",
          "title": "Boot",
          "order": 2
        },
        "deviceName": {
          "type": "string",
          "title": "DeviceName",
          "order": 3
        },
        "index": {
          "type": "integer",
          "title": "Index",
          "order": 4
        },
        "interface": {
          "type": "string",
          "title": "Interface",
          "order": 5
        },
        "kind": {
          "type": "string",
          "title": "Kind",
          "order": 6
        },
        "licenses": {
          "type": "array",
          "title": "Licenses",
          "items": {
            "type": "string"
          },
          "order": 7
        },
        "mode": {
          "type": "string",
          "title": "Mode",
          "order": 8
        },
        "source": {
          "type": "string",
          "title": "Source",
          "order": 9
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 10
        }
      }
    },
    "items_instance": {
      "type": "object",
      "title": "items_instance",
      "properties": {
        "canIpForward": {
          "type": "boolean",
          "title": "CanIpForward",
          "order": 1
        },
        "cpuPlatform": {
          "type": "string",
          "title": "CpuPlatform",
          "order": 2
        },
        "creationTimestamp": {
          "type": "string",
          "title": "CreationTimestamp",
          "order": 3
        },
        "description": {
          "type": "string",
          "title": "Description",
          "order": 4
        },
        "disks": {
          "type": "array",
          "title": "Disks",
          "items": {
            "$ref": "#/definitions/disks"
          },
          "order": 5
        },
        "id": {
          "type": "string",
          "title": "Id",
          "order": 6
        },
        "kind": {
          "type": "string",
          "title": "Kind",
          "order": 7
        },
        "machineType": {
          "type": "string",
          "title": "MachineType",
          "order": 8
        },
        "metadata": {
          "$ref": "#/definitions/metadata",
          "title": "Metadata",
          "order": 9
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 10
        },
        "networkInterfaces": {
          "type": "array",
          "title": "NetworkInterfaces",
          "items": {
            "$ref": "#/definitions/networkInterfaces"
          },
          "order": 11
        },
        "scheduling": {
          "$ref": "#/definitions/scheduling",
          "title": "Scheduling",
          "order": 12
        },
        "selfLink": {
          "type": "string",
          "title": "SelfLink",
          "order": 13
        },
        "serviceAccounts": {
          "type": "array",
          "title": "ServiceAccounts",
          "items": {
            "$ref": "#/definitions/serviceAccounts"
          },
          "order": 14
        },
        "status": {
          "type": "string",
          "title": "Status",
          "order": 15
        },
        "tags": {
          "$ref": "#/definitions/tags",
          "title": "Tags",
          "order": 16
        },
        "zone": {
          "type": "string",
          "title": "Zone",
          "order": 17
        }
      },
      "definitions": {
        "accessConfigs": {
          "type": "object",
          "title": "accessConfigs",
          "properties": {
            "kind": {
              "type": "string",
              "title": "Kind",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            },
            "natIP": {
              "type": "string",
              "title": "NatIP",
              "order": 3
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 4
            }
          }
        },
        "disks": {
          "type": "object",
          "title": "disks",
          "properties": {
            "autoDelete": {
              "type": "boolean",
              "title": "AutoDelete",
              "order": 1
            },
            "boot": {
              "type": "boolean",
              "title": "Boot",
              "order": 2
            },
            "deviceName": {
              "type": "string",
              "title": "DeviceName",
              "order": 3
            },
            "index": {
              "type": "integer",
              "title": "Index",
              "order": 4
            },
            "interface": {
              "type": "string",
              "title": "Interface",
              "order": 5
            },
            "kind": {
              "type": "string",
              "title": "Kind",
              "order": 6
            },
            "licenses": {
              "type": "array",
              "title": "Licenses",
              "items": {
                "type": "string"
              },
              "order": 7
            },
            "mode": {
              "type": "string",
              "title": "Mode",
              "order": 8
            },
            "source": {
              "type": "string",
              "title": "Source",
              "order": 9
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 10
            }
          }
        },
        "items_meta": {
          "type": "object",
          "title": "items_meta",
          "properties": {
            "key": {
              "type": "string",
              "title": "Key",
              "order": 1
            },
            "value": {
              "type": "string",
              "title": "Value",
              "order": 2
            }
          }
        },
        "metadata": {
          "type": "object",
          "title": "metadata",
          "properties": {
            "fingerprint": {
              "type": "string",
              "title": "Fingerprint",
              "order": 1
            },
            "items": {
              "type": "array",
              "title": "Items",
              "items": {
                "$ref": "#/definitions/items_meta"
              },
              "order": 2
            },
            "kind": {
              "type": "string",
              "title": "Kind",
              "order": 3
            }
          },
          "definitions": {
            "items_meta": {
              "type": "object",
              "title": "items_meta",
              "properties": {
                "key": {
                  "type": "string",
                  "title": "Key",
                  "order": 1
                },
                "value": {
                  "type": "string",
                  "title": "Value",
                  "order": 2
                }
              }
            }
          }
        },
        "networkInterfaces": {
          "type": "object",
          "title": "networkInterfaces",
          "properties": {
            "accessConfigs": {
              "type": "array",
              "title": "AccessConfigs",
              "items": {
                "$ref": "#/definitions/accessConfigs"
              },
              "order": 1
            },
            "kind": {
              "type": "string",
              "title": "Kind",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 3
            },
            "network": {
              "type": "string",
              "title": "Network",
              "order": 4
            },
            "networkIP": {
              "type": "string",
              "title": "NetworkIP",
              "order": 5
            },
            "subnetwork": {
              "type": "string",
              "title": "Subnetwork",
              "order": 6
            }
          },
          "definitions": {
            "accessConfigs": {
              "type": "object",
              "title": "accessConfigs",
              "properties": {
                "kind": {
                  "type": "string",
                  "title": "Kind",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "order": 2
                },
                "natIP": {
                  "type": "string",
                  "title": "NatIP",
                  "order": 3
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "order": 4
                }
              }
            }
          }
        },
        "scheduling": {
          "type": "object",
          "title": "scheduling",
          "properties": {
            "automaticRestart": {
              "type": "boolean",
              "title": "AutomaticRestart",
              "order": 1
            },
            "onHostMaintenance": {
              "type": "string",
              "title": "OnHostMaintenance",
              "order": 2
            },
            "preemptible": {
              "type": "boolean",
              "title": "Preemptible",
              "order": 3
            }
          }
        },
        "serviceAccounts": {
          "type": "object",
          "title": "serviceAccounts",
          "properties": {
            "email": {
              "type": "string",
              "title": "Email",
              "order": 1
            },
            "scopes": {
              "type": "array",
              "title": "Scopes",
              "items": {
                "type": "string"
              },
              "order": 2
            }
          }
        },
        "tags": {
          "type": "object",
          "title": "tags",
          "properties": {
            "fingerprint": {
              "type": "string",
              "title": "Fingerprint",
              "order": 1
            },
            "items": {
              "type": "array",
              "title": "Items",
              "items": {
                "type": "string"
              },
              "order": 2
            }
          }
        }
      }
    },
    "items_meta": {
      "type": "object",
      "title": "items_meta",
      "properties": {
        "key": {
          "type": "string",
          "title": "Key",
          "order": 1
        },
        "value": {
          "type": "string",
          "title": "Value",
          "order": 2
        }
      }
    },
    "metadata": {
      "type": "object",
      "title": "metadata",
      "properties": {
        "fingerprint": {
          "type": "string",
          "title": "Fingerprint",
          "order": 1
        },
        "items": {
          "type": "array",
          "title": "Items",
          "items": {
            "$ref": "#/definitions/items_meta"
          },
          "order": 2
        },
        "kind": {
          "type": "string",
          "title": "Kind",
          "order": 3
        }
      },
      "definitions": {
        "items_meta": {
          "type": "object",
          "title": "items_meta",
          "properties": {
            "key": {
              "type": "string",
              "title": "Key",
              "order": 1
            },
            "value": {
              "type": "string",
              "title": "Value",
              "order": 2
            }
          }
        }
      }
    },
    "networkInterfaces": {
      "type": "object",
      "title": "networkInterfaces",
      "properties": {
        "accessConfigs": {
          "type": "array",
          "title": "AccessConfigs",
          "items": {
            "$ref": "#/definitions/accessConfigs"
          },
          "order": 1
        },
        "kind": {
          "type": "string",
          "title": "Kind",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 3
        },
        "network": {
          "type": "string",
          "title": "Network",
          "order": 4
        },
        "networkIP": {
          "type": "string",
          "title": "NetworkIP",
          "order": 5
        },
        "subnetwork": {
          "type": "string",
          "title": "Subnetwork",
          "order": 6
        }
      },
      "definitions": {
        "accessConfigs": {
          "type": "object",
          "title": "accessConfigs",
          "properties": {
            "kind": {
              "type": "string",
              "title": "Kind",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            },
            "natIP": {
              "type": "string",
              "title": "NatIP",
              "order": 3
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 4
            }
          }
        }
      }
    },
    "scheduling": {
      "type": "object",
      "title": "scheduling",
      "properties": {
        "automaticRestart": {
          "type": "boolean",
          "title": "AutomaticRestart",
          "order": 1
        },
        "onHostMaintenance": {
          "type": "string",
          "title": "OnHostMaintenance",
          "order": 2
        },
        "preemptible": {
          "type": "boolean",
          "title": "Preemptible",
          "order": 3
        }
      }
    },
    "serviceAccounts": {
      "type": "object",
      "title": "serviceAccounts",
      "properties": {
        "email": {
          "type": "string",
          "title": "Email",
          "order": 1
        },
        "scopes": {
          "type": "array",
          "title": "Scopes",
          "items": {
            "type": "string"
          },
          "order": 2
        }
      }
    },
    "tags": {
      "type": "object",
      "title": "tags",
      "properties": {
        "fingerprint": {
          "type": "string",
          "title": "Fingerprint",
          "order": 1
        },
        "items": {
          "type": "array",
          "title": "Items",
          "items": {
            "type": "string"
          },
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
