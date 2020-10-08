# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Checks if provided Address Object name or host exists in the Address Group"


class Input:
    ADDRESS = "address"
    ENABLE_SEARCH = "enable_search"
    GROUP = "group"
    

class Output:
    ADDRESS_OBJECTS = "address_objects"
    FOUND = "found"
    

class CheckIfAddressInGroupInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "Address",
      "description": "Address Object name, or IP, CIDR, or domain name when Enable Search is on",
      "order": 2
    },
    "enable_search": {
      "type": "boolean",
      "title": "Enable Search",
      "description": "When enabled, the Address input will accept an IP, CIDR, or domain name to search across the available Address Objects in the system. This is useful when you don’t know the Address Object by its name",
      "default": false,
      "order": 3
    },
    "group": {
      "type": "string",
      "title": "Group",
      "description": "Name of address group to check",
      "order": 1
    }
  },
  "required": [
    "address",
    "group"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CheckIfAddressInGroupOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address_objects": {
      "type": "array",
      "title": "Address Objects",
      "description": "List of found address objects",
      "items": {
        "$ref": "#/definitions/address_object"
      },
      "order": 2
    },
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "Was address found in group",
      "order": 1
    }
  },
  "required": [
    "found"
  ],
  "definitions": {
    "address_object": {
      "type": "object",
      "title": "address_object",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "description": "User provided resource description",
          "order": 4
        },
        "dnsResolution": {
          "type": "string",
          "title": "DNS Resolution",
          "description": "DNS resolution",
          "order": 12
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Unique identifier representing response object",
          "order": 7
        },
        "links": {
          "$ref": "#/definitions/links",
          "title": "Links",
          "description": "This defines the self referencing links for the given resource",
          "order": 5
        },
        "metadata": {
          "$ref": "#/definitions/metadata",
          "title": "Metadata",
          "description": "Defines read only details about the object - whether it is system defined, last user who modified the object etc",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "User assigned resource name",
          "order": 3
        },
        "overridable": {
          "type": "boolean",
          "title": "Overridable",
          "description": "Boolean indicating whether object values can be overridden",
          "order": 2
        },
        "overrideTargetId": {
          "type": "string",
          "title": "Override Target ID",
          "description": "Unique identifier of domain or device when override assigned to child domain. Used as path parameter to GET override details for a specific object on a specific target (device or domain)",
          "order": 11
        },
        "overrides": {
          "$ref": "#/definitions/override",
          "title": "Overrides",
          "description": "Defines the override details for this object",
          "order": 6
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The unique type of this object",
          "order": 8
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Actual value of the network",
          "order": 9
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "Version number of the response object",
          "order": 10
        }
      },
      "definitions": {
        "domain": {
          "type": "object",
          "title": "domain",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "Unique UUID of this domain",
              "order": 3
            },
            "links": {
              "$ref": "#/definitions/links",
              "title": "Links",
              "description": "This defines the self referencing links for the given resource",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the domain",
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Domain type definition",
              "order": 4
            }
          },
          "definitions": {
            "links": {
              "type": "object",
              "title": "links",
              "properties": {
                "parent": {
                  "type": "string",
                  "title": "Parent",
                  "description": "Full resource URL path to reference the parent (if any) for this resource",
                  "order": 1
                },
                "self": {
                  "type": "string",
                  "title": "Self",
                  "description": "Full resource URL path to reference this particular resource",
                  "order": 2
                }
              }
            }
          }
        },
        "links": {
          "type": "object",
          "title": "links",
          "properties": {
            "parent": {
              "type": "string",
              "title": "Parent",
              "description": "Full resource URL path to reference the parent (if any) for this resource",
              "order": 1
            },
            "self": {
              "type": "string",
              "title": "Self",
              "description": "Full resource URL path to reference this particular resource",
              "order": 2
            }
          }
        },
        "metadata": {
          "type": "object",
          "title": "metadata",
          "properties": {
            "domain": {
              "$ref": "#/definitions/domain",
              "title": "Domain",
              "description": "The details about the domain",
              "order": 2
            },
            "ipType": {
              "type": "string",
              "title": "IP Type",
              "description": "IP type",
              "order": 5
            },
            "lastUser": {
              "$ref": "#/definitions/metadata_user",
              "title": "Last User",
              "description": "This object defines details about the user",
              "order": 1
            },
            "parentType": {
              "type": "string",
              "title": "Parent Type",
              "description": "Parent type",
              "order": 6
            },
            "readOnly": {
              "$ref": "#/definitions/read_only",
              "title": "Read Only",
              "description": "Defines the read only conditions if the referenced resource is read only",
              "order": 3
            },
            "timestamp": {
              "type": "integer",
              "title": "Timestamp",
              "description": "The last updated timestamp",
              "order": 4
            }
          },
          "definitions": {
            "domain": {
              "type": "object",
              "title": "domain",
              "properties": {
                "id": {
                  "type": "string",
                  "title": "ID",
                  "description": "Unique UUID of this domain",
                  "order": 3
                },
                "links": {
                  "$ref": "#/definitions/links",
                  "title": "Links",
                  "description": "This defines the self referencing links for the given resource",
                  "order": 2
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Name of the domain",
                  "order": 1
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "description": "Domain type definition",
                  "order": 4
                }
              },
              "definitions": {
                "links": {
                  "type": "object",
                  "title": "links",
                  "properties": {
                    "parent": {
                      "type": "string",
                      "title": "Parent",
                      "description": "Full resource URL path to reference the parent (if any) for this resource",
                      "order": 1
                    },
                    "self": {
                      "type": "string",
                      "title": "Self",
                      "description": "Full resource URL path to reference this particular resource",
                      "order": 2
                    }
                  }
                }
              }
            },
            "links": {
              "type": "object",
              "title": "links",
              "properties": {
                "parent": {
                  "type": "string",
                  "title": "Parent",
                  "description": "Full resource URL path to reference the parent (if any) for this resource",
                  "order": 1
                },
                "self": {
                  "type": "string",
                  "title": "Self",
                  "description": "Full resource URL path to reference this particular resource",
                  "order": 2
                }
              }
            },
            "metadata_user": {
              "type": "object",
              "title": "metadata_user",
              "properties": {
                "id": {
                  "type": "string",
                  "title": "ID",
                  "description": "The unique UUID of the user",
                  "order": 3
                },
                "links": {
                  "$ref": "#/definitions/links",
                  "title": "Links",
                  "description": "This defines the self referencing links for the given resource",
                  "order": 2
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "Name of the user",
                  "order": 1
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "description": "The user type",
                  "order": 4
                }
              },
              "definitions": {
                "links": {
                  "type": "object",
                  "title": "links",
                  "properties": {
                    "parent": {
                      "type": "string",
                      "title": "Parent",
                      "description": "Full resource URL path to reference the parent (if any) for this resource",
                      "order": 1
                    },
                    "self": {
                      "type": "string",
                      "title": "Self",
                      "description": "Full resource URL path to reference this particular resource",
                      "order": 2
                    }
                  }
                }
              }
            },
            "read_only": {
              "type": "object",
              "title": "read_only",
              "properties": {
                "reason": {
                  "type": "string",
                  "title": "Reason",
                  "description": "Reason the resource is read only - SYSTEM (if it is system defined), RBAC (if user RBAC permissions make it read only) or DOMAIN (if resource is read only in current domain)",
                  "order": 1
                },
                "state": {
                  "type": "boolean",
                  "title": "State",
                  "description": "True if this resource is read only and false otherwise",
                  "order": 2
                }
              }
            }
          }
        },
        "metadata_user": {
          "type": "object",
          "title": "metadata_user",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "The unique UUID of the user",
              "order": 3
            },
            "links": {
              "$ref": "#/definitions/links",
              "title": "Links",
              "description": "This defines the self referencing links for the given resource",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the user",
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "The user type",
              "order": 4
            }
          },
          "definitions": {
            "links": {
              "type": "object",
              "title": "links",
              "properties": {
                "parent": {
                  "type": "string",
                  "title": "Parent",
                  "description": "Full resource URL path to reference the parent (if any) for this resource",
                  "order": 1
                },
                "self": {
                  "type": "string",
                  "title": "Self",
                  "description": "Full resource URL path to reference this particular resource",
                  "order": 2
                }
              }
            }
          }
        },
        "override": {
          "type": "object",
          "title": "override",
          "properties": {
            "parent": {
              "$ref": "#/definitions/reference",
              "title": "Parent",
              "description": "Contains parent reference information",
              "order": 1
            },
            "target": {
              "$ref": "#/definitions/reference",
              "title": "Target",
              "description": "Contains target reference information",
              "order": 2
            }
          },
          "definitions": {
            "links": {
              "type": "object",
              "title": "links",
              "properties": {
                "parent": {
                  "type": "string",
                  "title": "Parent",
                  "description": "Full resource URL path to reference the parent (if any) for this resource",
                  "order": 1
                },
                "self": {
                  "type": "string",
                  "title": "Self",
                  "description": "Full resource URL path to reference this particular resource",
                  "order": 2
                }
              }
            },
            "reference": {
              "type": "object",
              "title": "reference",
              "properties": {
                "id": {
                  "type": "string",
                  "title": "ID",
                  "description": "Unique identifier representing resource",
                  "order": 3
                },
                "links": {
                  "$ref": "#/definitions/links",
                  "title": "Links",
                  "description": "This defines the self referencing links for the given resource",
                  "order": 2
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "description": "User chosen resource name",
                  "order": 1
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "description": "Response object associated with resource",
                  "order": 4
                }
              },
              "definitions": {
                "links": {
                  "type": "object",
                  "title": "links",
                  "properties": {
                    "parent": {
                      "type": "string",
                      "title": "Parent",
                      "description": "Full resource URL path to reference the parent (if any) for this resource",
                      "order": 1
                    },
                    "self": {
                      "type": "string",
                      "title": "Self",
                      "description": "Full resource URL path to reference this particular resource",
                      "order": 2
                    }
                  }
                }
              }
            }
          }
        },
        "read_only": {
          "type": "object",
          "title": "read_only",
          "properties": {
            "reason": {
              "type": "string",
              "title": "Reason",
              "description": "Reason the resource is read only - SYSTEM (if it is system defined), RBAC (if user RBAC permissions make it read only) or DOMAIN (if resource is read only in current domain)",
              "order": 1
            },
            "state": {
              "type": "boolean",
              "title": "State",
              "description": "True if this resource is read only and false otherwise",
              "order": 2
            }
          }
        },
        "reference": {
          "type": "object",
          "title": "reference",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "Unique identifier representing resource",
              "order": 3
            },
            "links": {
              "$ref": "#/definitions/links",
              "title": "Links",
              "description": "This defines the self referencing links for the given resource",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "User chosen resource name",
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Response object associated with resource",
              "order": 4
            }
          },
          "definitions": {
            "links": {
              "type": "object",
              "title": "links",
              "properties": {
                "parent": {
                  "type": "string",
                  "title": "Parent",
                  "description": "Full resource URL path to reference the parent (if any) for this resource",
                  "order": 1
                },
                "self": {
                  "type": "string",
                  "title": "Self",
                  "description": "Full resource URL path to reference this particular resource",
                  "order": 2
                }
              }
            }
          }
        }
      }
    },
    "domain": {
      "type": "object",
      "title": "domain",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Unique UUID of this domain",
          "order": 3
        },
        "links": {
          "$ref": "#/definitions/links",
          "title": "Links",
          "description": "This defines the self referencing links for the given resource",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the domain",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Domain type definition",
          "order": 4
        }
      },
      "definitions": {
        "links": {
          "type": "object",
          "title": "links",
          "properties": {
            "parent": {
              "type": "string",
              "title": "Parent",
              "description": "Full resource URL path to reference the parent (if any) for this resource",
              "order": 1
            },
            "self": {
              "type": "string",
              "title": "Self",
              "description": "Full resource URL path to reference this particular resource",
              "order": 2
            }
          }
        }
      }
    },
    "links": {
      "type": "object",
      "title": "links",
      "properties": {
        "parent": {
          "type": "string",
          "title": "Parent",
          "description": "Full resource URL path to reference the parent (if any) for this resource",
          "order": 1
        },
        "self": {
          "type": "string",
          "title": "Self",
          "description": "Full resource URL path to reference this particular resource",
          "order": 2
        }
      }
    },
    "metadata": {
      "type": "object",
      "title": "metadata",
      "properties": {
        "domain": {
          "$ref": "#/definitions/domain",
          "title": "Domain",
          "description": "The details about the domain",
          "order": 2
        },
        "ipType": {
          "type": "string",
          "title": "IP Type",
          "description": "IP type",
          "order": 5
        },
        "lastUser": {
          "$ref": "#/definitions/metadata_user",
          "title": "Last User",
          "description": "This object defines details about the user",
          "order": 1
        },
        "parentType": {
          "type": "string",
          "title": "Parent Type",
          "description": "Parent type",
          "order": 6
        },
        "readOnly": {
          "$ref": "#/definitions/read_only",
          "title": "Read Only",
          "description": "Defines the read only conditions if the referenced resource is read only",
          "order": 3
        },
        "timestamp": {
          "type": "integer",
          "title": "Timestamp",
          "description": "The last updated timestamp",
          "order": 4
        }
      },
      "definitions": {
        "domain": {
          "type": "object",
          "title": "domain",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "Unique UUID of this domain",
              "order": 3
            },
            "links": {
              "$ref": "#/definitions/links",
              "title": "Links",
              "description": "This defines the self referencing links for the given resource",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the domain",
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Domain type definition",
              "order": 4
            }
          },
          "definitions": {
            "links": {
              "type": "object",
              "title": "links",
              "properties": {
                "parent": {
                  "type": "string",
                  "title": "Parent",
                  "description": "Full resource URL path to reference the parent (if any) for this resource",
                  "order": 1
                },
                "self": {
                  "type": "string",
                  "title": "Self",
                  "description": "Full resource URL path to reference this particular resource",
                  "order": 2
                }
              }
            }
          }
        },
        "links": {
          "type": "object",
          "title": "links",
          "properties": {
            "parent": {
              "type": "string",
              "title": "Parent",
              "description": "Full resource URL path to reference the parent (if any) for this resource",
              "order": 1
            },
            "self": {
              "type": "string",
              "title": "Self",
              "description": "Full resource URL path to reference this particular resource",
              "order": 2
            }
          }
        },
        "metadata_user": {
          "type": "object",
          "title": "metadata_user",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "The unique UUID of the user",
              "order": 3
            },
            "links": {
              "$ref": "#/definitions/links",
              "title": "Links",
              "description": "This defines the self referencing links for the given resource",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "Name of the user",
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "The user type",
              "order": 4
            }
          },
          "definitions": {
            "links": {
              "type": "object",
              "title": "links",
              "properties": {
                "parent": {
                  "type": "string",
                  "title": "Parent",
                  "description": "Full resource URL path to reference the parent (if any) for this resource",
                  "order": 1
                },
                "self": {
                  "type": "string",
                  "title": "Self",
                  "description": "Full resource URL path to reference this particular resource",
                  "order": 2
                }
              }
            }
          }
        },
        "read_only": {
          "type": "object",
          "title": "read_only",
          "properties": {
            "reason": {
              "type": "string",
              "title": "Reason",
              "description": "Reason the resource is read only - SYSTEM (if it is system defined), RBAC (if user RBAC permissions make it read only) or DOMAIN (if resource is read only in current domain)",
              "order": 1
            },
            "state": {
              "type": "boolean",
              "title": "State",
              "description": "True if this resource is read only and false otherwise",
              "order": 2
            }
          }
        }
      }
    },
    "metadata_user": {
      "type": "object",
      "title": "metadata_user",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The unique UUID of the user",
          "order": 3
        },
        "links": {
          "$ref": "#/definitions/links",
          "title": "Links",
          "description": "This defines the self referencing links for the given resource",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the user",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "The user type",
          "order": 4
        }
      },
      "definitions": {
        "links": {
          "type": "object",
          "title": "links",
          "properties": {
            "parent": {
              "type": "string",
              "title": "Parent",
              "description": "Full resource URL path to reference the parent (if any) for this resource",
              "order": 1
            },
            "self": {
              "type": "string",
              "title": "Self",
              "description": "Full resource URL path to reference this particular resource",
              "order": 2
            }
          }
        }
      }
    },
    "override": {
      "type": "object",
      "title": "override",
      "properties": {
        "parent": {
          "$ref": "#/definitions/reference",
          "title": "Parent",
          "description": "Contains parent reference information",
          "order": 1
        },
        "target": {
          "$ref": "#/definitions/reference",
          "title": "Target",
          "description": "Contains target reference information",
          "order": 2
        }
      },
      "definitions": {
        "links": {
          "type": "object",
          "title": "links",
          "properties": {
            "parent": {
              "type": "string",
              "title": "Parent",
              "description": "Full resource URL path to reference the parent (if any) for this resource",
              "order": 1
            },
            "self": {
              "type": "string",
              "title": "Self",
              "description": "Full resource URL path to reference this particular resource",
              "order": 2
            }
          }
        },
        "reference": {
          "type": "object",
          "title": "reference",
          "properties": {
            "id": {
              "type": "string",
              "title": "ID",
              "description": "Unique identifier representing resource",
              "order": 3
            },
            "links": {
              "$ref": "#/definitions/links",
              "title": "Links",
              "description": "This defines the self referencing links for the given resource",
              "order": 2
            },
            "name": {
              "type": "string",
              "title": "Name",
              "description": "User chosen resource name",
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "description": "Response object associated with resource",
              "order": 4
            }
          },
          "definitions": {
            "links": {
              "type": "object",
              "title": "links",
              "properties": {
                "parent": {
                  "type": "string",
                  "title": "Parent",
                  "description": "Full resource URL path to reference the parent (if any) for this resource",
                  "order": 1
                },
                "self": {
                  "type": "string",
                  "title": "Self",
                  "description": "Full resource URL path to reference this particular resource",
                  "order": 2
                }
              }
            }
          }
        }
      }
    },
    "read_only": {
      "type": "object",
      "title": "read_only",
      "properties": {
        "reason": {
          "type": "string",
          "title": "Reason",
          "description": "Reason the resource is read only - SYSTEM (if it is system defined), RBAC (if user RBAC permissions make it read only) or DOMAIN (if resource is read only in current domain)",
          "order": 1
        },
        "state": {
          "type": "boolean",
          "title": "State",
          "description": "True if this resource is read only and false otherwise",
          "order": 2
        }
      }
    },
    "reference": {
      "type": "object",
      "title": "reference",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "Unique identifier representing resource",
          "order": 3
        },
        "links": {
          "$ref": "#/definitions/links",
          "title": "Links",
          "description": "This defines the self referencing links for the given resource",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "User chosen resource name",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Response object associated with resource",
          "order": 4
        }
      },
      "definitions": {
        "links": {
          "type": "object",
          "title": "links",
          "properties": {
            "parent": {
              "type": "string",
              "title": "Parent",
              "description": "Full resource URL path to reference the parent (if any) for this resource",
              "order": 1
            },
            "self": {
              "type": "string",
              "title": "Self",
              "description": "Full resource URL path to reference this particular resource",
              "order": 2
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
