# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get a full report for an MD5 hash of a file that was analyzed by Sandbox"


class Input:
    HASH = "hash"
    

class Output:
    FULL_REPORT = "full_report"
    

class GetSandboxReportForHashInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "hash": {
      "type": "string",
      "title": "Hash",
      "description": "MD5 hash to get report",
      "order": 1
    }
  },
  "required": [
    "hash"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetSandboxReportForHashOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "full_report": {
      "$ref": "#/definitions/full_report",
      "title": "Full Report",
      "description": "Full report of an analyzed MD5 hash",
      "order": 1
    }
  },
  "required": [
    "full_report"
  ],
  "definitions": {
    "Classification": {
      "type": "object",
      "title": "Classification",
      "properties": {
        "Category": {
          "type": "string",
          "title": "Category",
          "description": "Category",
          "order": 1
        },
        "DetectedMalware": {
          "type": "string",
          "title": "Detectedmalware",
          "description": "Detectedmalware",
          "order": 2
        },
        "Score": {
          "type": "integer",
          "title": "Score",
          "description": "Score",
          "order": 3
        },
        "Type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 4
        }
      }
    },
    "FileProperties": {
      "type": "object",
      "title": "FileProperties",
      "properties": {
        "DigitalCerificate": {
          "type": "string",
          "title": "Digitalcerificate",
          "description": "Digitalcerificate",
          "order": 1
        },
        "FileSize": {
          "type": "integer",
          "title": "Filesize",
          "description": "Filesize",
          "order": 2
        },
        "FileType": {
          "type": "string",
          "title": "Filetype",
          "description": "Filetype",
          "order": 3
        },
        "Issuer": {
          "type": "string",
          "title": "Issuer",
          "description": "Issuer",
          "order": 4
        },
        "MD5": {
          "type": "string",
          "title": "Md5",
          "description": "Md5",
          "order": 5
        },
        "RootCA": {
          "type": "string",
          "title": "Rootca",
          "description": "Rootca",
          "order": 6
        },
        "SHA1": {
          "type": "string",
          "title": "Sha1",
          "description": "Sha1",
          "order": 7
        },
        "SSDeep": {
          "type": "string",
          "title": "Ssdeep",
          "description": "Ssdeep",
          "order": 8
        },
        "Sha256": {
          "type": "string",
          "title": "Sha256",
          "description": "Sha256",
          "order": 9
        }
      }
    },
    "FullDetails": {
      "type": "object",
      "title": "FullDetails",
      "properties": {
        "Classification": {
          "$ref": "#/definitions/Classification",
          "title": "Classification",
          "description": "Classification",
          "order": 1
        },
        "FileProperties": {
          "$ref": "#/definitions/FileProperties",
          "title": "Fileproperties",
          "description": "Fileproperties",
          "order": 2
        },
        "Networking": {
          "type": "array",
          "title": "Networking",
          "description": "Networking",
          "items": {
            "$ref": "#/definitions/PersistenceSummary"
          },
          "order": 6
        },
        "Persistence": {
          "type": "array",
          "title": "Persistence",
          "description": "Persistence",
          "items": {
            "$ref": "#/definitions/PersistenceSummary"
          },
          "order": 3
        },
        "SecurityBypass": {
          "type": "array",
          "title": "Securitybypass",
          "description": "Securitybypass",
          "items": {
            "$ref": "#/definitions/PersistenceSummary"
          },
          "order": 4
        },
        "Stealth": {
          "type": "array",
          "title": "Stealth",
          "description": "Stealth",
          "items": {
            "$ref": "#/definitions/PersistenceSummary"
          },
          "order": 7
        },
        "Summary": {
          "$ref": "#/definitions/Summary",
          "title": "Summary",
          "description": "Summary",
          "order": 5
        },
        "SystemSummary": {
          "type": "array",
          "title": "Systemsummary",
          "description": "Systemsummary",
          "items": {
            "$ref": "#/definitions/PersistenceSummary"
          },
          "order": 8
        }
      },
      "definitions": {
        "Classification": {
          "type": "object",
          "title": "Classification",
          "properties": {
            "Category": {
              "type": "string",
              "title": "Category",
              "description": "Category",
              "order": 1
            },
            "DetectedMalware": {
              "type": "string",
              "title": "Detectedmalware",
              "description": "Detectedmalware",
              "order": 2
            },
            "Score": {
              "type": "integer",
              "title": "Score",
              "description": "Score",
              "order": 3
            },
            "Type": {
              "type": "string",
              "title": "Type",
              "description": "Type",
              "order": 4
            }
          }
        },
        "FileProperties": {
          "type": "object",
          "title": "FileProperties",
          "properties": {
            "DigitalCerificate": {
              "type": "string",
              "title": "Digitalcerificate",
              "description": "Digitalcerificate",
              "order": 1
            },
            "FileSize": {
              "type": "integer",
              "title": "Filesize",
              "description": "Filesize",
              "order": 2
            },
            "FileType": {
              "type": "string",
              "title": "Filetype",
              "description": "Filetype",
              "order": 3
            },
            "Issuer": {
              "type": "string",
              "title": "Issuer",
              "description": "Issuer",
              "order": 4
            },
            "MD5": {
              "type": "string",
              "title": "Md5",
              "description": "Md5",
              "order": 5
            },
            "RootCA": {
              "type": "string",
              "title": "Rootca",
              "description": "Rootca",
              "order": 6
            },
            "SHA1": {
              "type": "string",
              "title": "Sha1",
              "description": "Sha1",
              "order": 7
            },
            "SSDeep": {
              "type": "string",
              "title": "Ssdeep",
              "description": "Ssdeep",
              "order": 8
            },
            "Sha256": {
              "type": "string",
              "title": "Sha256",
              "description": "Sha256",
              "order": 9
            }
          }
        },
        "PersistenceSummary": {
          "type": "object",
          "title": "PersistenceSummary",
          "properties": {
            "Risk": {
              "type": "string",
              "title": "Risk",
              "description": "Risk",
              "order": 1
            },
            "Signature": {
              "type": "string",
              "title": "Signature",
              "description": "Signature",
              "order": 2
            },
            "SignatureSources": {
              "type": "array",
              "title": "Signaturesources",
              "description": "Signaturesources",
              "items": {
                "type": "string"
              },
              "order": 3
            }
          }
        },
        "Summary": {
          "type": "object",
          "title": "Summary",
          "properties": {
            "Category": {
              "type": "string",
              "title": "Category",
              "description": "Category",
              "order": 1
            },
            "Duration": {
              "type": "integer",
              "title": "Duration",
              "description": "Duration",
              "order": 2
            },
            "FileType": {
              "type": "string",
              "title": "Filetype",
              "description": "Filetype",
              "order": 3
            },
            "StartTime": {
              "type": "integer",
              "title": "Starttime",
              "description": "Starttime",
              "order": 4
            },
            "Status": {
              "type": "string",
              "title": "Status",
              "description": "Status",
              "order": 5
            }
          }
        }
      }
    },
    "PersistenceSummary": {
      "type": "object",
      "title": "PersistenceSummary",
      "properties": {
        "Risk": {
          "type": "string",
          "title": "Risk",
          "description": "Risk",
          "order": 1
        },
        "Signature": {
          "type": "string",
          "title": "Signature",
          "description": "Signature",
          "order": 2
        },
        "SignatureSources": {
          "type": "array",
          "title": "Signaturesources",
          "description": "Signaturesources",
          "items": {
            "type": "string"
          },
          "order": 3
        }
      }
    },
    "Summary": {
      "type": "object",
      "title": "Summary",
      "properties": {
        "Category": {
          "type": "string",
          "title": "Category",
          "description": "Category",
          "order": 1
        },
        "Duration": {
          "type": "integer",
          "title": "Duration",
          "description": "Duration",
          "order": 2
        },
        "FileType": {
          "type": "string",
          "title": "Filetype",
          "description": "Filetype",
          "order": 3
        },
        "StartTime": {
          "type": "integer",
          "title": "Starttime",
          "description": "Starttime",
          "order": 4
        },
        "Status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 5
        }
      }
    },
    "full_report": {
      "type": "object",
      "title": "full_report",
      "properties": {
        "FullDetails": {
          "$ref": "#/definitions/FullDetails",
          "title": "Full Details",
          "description": "Full details",
          "order": 1
        }
      },
      "definitions": {
        "Classification": {
          "type": "object",
          "title": "Classification",
          "properties": {
            "Category": {
              "type": "string",
              "title": "Category",
              "description": "Category",
              "order": 1
            },
            "DetectedMalware": {
              "type": "string",
              "title": "Detectedmalware",
              "description": "Detectedmalware",
              "order": 2
            },
            "Score": {
              "type": "integer",
              "title": "Score",
              "description": "Score",
              "order": 3
            },
            "Type": {
              "type": "string",
              "title": "Type",
              "description": "Type",
              "order": 4
            }
          }
        },
        "FileProperties": {
          "type": "object",
          "title": "FileProperties",
          "properties": {
            "DigitalCerificate": {
              "type": "string",
              "title": "Digitalcerificate",
              "description": "Digitalcerificate",
              "order": 1
            },
            "FileSize": {
              "type": "integer",
              "title": "Filesize",
              "description": "Filesize",
              "order": 2
            },
            "FileType": {
              "type": "string",
              "title": "Filetype",
              "description": "Filetype",
              "order": 3
            },
            "Issuer": {
              "type": "string",
              "title": "Issuer",
              "description": "Issuer",
              "order": 4
            },
            "MD5": {
              "type": "string",
              "title": "Md5",
              "description": "Md5",
              "order": 5
            },
            "RootCA": {
              "type": "string",
              "title": "Rootca",
              "description": "Rootca",
              "order": 6
            },
            "SHA1": {
              "type": "string",
              "title": "Sha1",
              "description": "Sha1",
              "order": 7
            },
            "SSDeep": {
              "type": "string",
              "title": "Ssdeep",
              "description": "Ssdeep",
              "order": 8
            },
            "Sha256": {
              "type": "string",
              "title": "Sha256",
              "description": "Sha256",
              "order": 9
            }
          }
        },
        "FullDetails": {
          "type": "object",
          "title": "FullDetails",
          "properties": {
            "Classification": {
              "$ref": "#/definitions/Classification",
              "title": "Classification",
              "description": "Classification",
              "order": 1
            },
            "FileProperties": {
              "$ref": "#/definitions/FileProperties",
              "title": "Fileproperties",
              "description": "Fileproperties",
              "order": 2
            },
            "Networking": {
              "type": "array",
              "title": "Networking",
              "description": "Networking",
              "items": {
                "$ref": "#/definitions/PersistenceSummary"
              },
              "order": 6
            },
            "Persistence": {
              "type": "array",
              "title": "Persistence",
              "description": "Persistence",
              "items": {
                "$ref": "#/definitions/PersistenceSummary"
              },
              "order": 3
            },
            "SecurityBypass": {
              "type": "array",
              "title": "Securitybypass",
              "description": "Securitybypass",
              "items": {
                "$ref": "#/definitions/PersistenceSummary"
              },
              "order": 4
            },
            "Stealth": {
              "type": "array",
              "title": "Stealth",
              "description": "Stealth",
              "items": {
                "$ref": "#/definitions/PersistenceSummary"
              },
              "order": 7
            },
            "Summary": {
              "$ref": "#/definitions/Summary",
              "title": "Summary",
              "description": "Summary",
              "order": 5
            },
            "SystemSummary": {
              "type": "array",
              "title": "Systemsummary",
              "description": "Systemsummary",
              "items": {
                "$ref": "#/definitions/PersistenceSummary"
              },
              "order": 8
            }
          },
          "definitions": {
            "Classification": {
              "type": "object",
              "title": "Classification",
              "properties": {
                "Category": {
                  "type": "string",
                  "title": "Category",
                  "description": "Category",
                  "order": 1
                },
                "DetectedMalware": {
                  "type": "string",
                  "title": "Detectedmalware",
                  "description": "Detectedmalware",
                  "order": 2
                },
                "Score": {
                  "type": "integer",
                  "title": "Score",
                  "description": "Score",
                  "order": 3
                },
                "Type": {
                  "type": "string",
                  "title": "Type",
                  "description": "Type",
                  "order": 4
                }
              }
            },
            "FileProperties": {
              "type": "object",
              "title": "FileProperties",
              "properties": {
                "DigitalCerificate": {
                  "type": "string",
                  "title": "Digitalcerificate",
                  "description": "Digitalcerificate",
                  "order": 1
                },
                "FileSize": {
                  "type": "integer",
                  "title": "Filesize",
                  "description": "Filesize",
                  "order": 2
                },
                "FileType": {
                  "type": "string",
                  "title": "Filetype",
                  "description": "Filetype",
                  "order": 3
                },
                "Issuer": {
                  "type": "string",
                  "title": "Issuer",
                  "description": "Issuer",
                  "order": 4
                },
                "MD5": {
                  "type": "string",
                  "title": "Md5",
                  "description": "Md5",
                  "order": 5
                },
                "RootCA": {
                  "type": "string",
                  "title": "Rootca",
                  "description": "Rootca",
                  "order": 6
                },
                "SHA1": {
                  "type": "string",
                  "title": "Sha1",
                  "description": "Sha1",
                  "order": 7
                },
                "SSDeep": {
                  "type": "string",
                  "title": "Ssdeep",
                  "description": "Ssdeep",
                  "order": 8
                },
                "Sha256": {
                  "type": "string",
                  "title": "Sha256",
                  "description": "Sha256",
                  "order": 9
                }
              }
            },
            "PersistenceSummary": {
              "type": "object",
              "title": "PersistenceSummary",
              "properties": {
                "Risk": {
                  "type": "string",
                  "title": "Risk",
                  "description": "Risk",
                  "order": 1
                },
                "Signature": {
                  "type": "string",
                  "title": "Signature",
                  "description": "Signature",
                  "order": 2
                },
                "SignatureSources": {
                  "type": "array",
                  "title": "Signaturesources",
                  "description": "Signaturesources",
                  "items": {
                    "type": "string"
                  },
                  "order": 3
                }
              }
            },
            "Summary": {
              "type": "object",
              "title": "Summary",
              "properties": {
                "Category": {
                  "type": "string",
                  "title": "Category",
                  "description": "Category",
                  "order": 1
                },
                "Duration": {
                  "type": "integer",
                  "title": "Duration",
                  "description": "Duration",
                  "order": 2
                },
                "FileType": {
                  "type": "string",
                  "title": "Filetype",
                  "description": "Filetype",
                  "order": 3
                },
                "StartTime": {
                  "type": "integer",
                  "title": "Starttime",
                  "description": "Starttime",
                  "order": 4
                },
                "Status": {
                  "type": "string",
                  "title": "Status",
                  "description": "Status",
                  "order": 5
                }
              }
            }
          }
        },
        "PersistenceSummary": {
          "type": "object",
          "title": "PersistenceSummary",
          "properties": {
            "Risk": {
              "type": "string",
              "title": "Risk",
              "description": "Risk",
              "order": 1
            },
            "Signature": {
              "type": "string",
              "title": "Signature",
              "description": "Signature",
              "order": 2
            },
            "SignatureSources": {
              "type": "array",
              "title": "Signaturesources",
              "description": "Signaturesources",
              "items": {
                "type": "string"
              },
              "order": 3
            }
          }
        },
        "Summary": {
          "type": "object",
          "title": "Summary",
          "properties": {
            "Category": {
              "type": "string",
              "title": "Category",
              "description": "Category",
              "order": 1
            },
            "Duration": {
              "type": "integer",
              "title": "Duration",
              "description": "Duration",
              "order": 2
            },
            "FileType": {
              "type": "string",
              "title": "Filetype",
              "description": "Filetype",
              "order": 3
            },
            "StartTime": {
              "type": "integer",
              "title": "Starttime",
              "description": "Starttime",
              "order": 4
            },
            "Status": {
              "type": "string",
              "title": "Status",
              "description": "Status",
              "order": 5
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
