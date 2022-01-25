# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Extracts all UUIDs, CVEs, dates, domains, emails, filepaths, IOCs, IPs, MACs, MD5 hashes, SHA1 hashes, SHA256 hashes, SHA 512 hashes and URLs from a string or file"


class Input:
    DATE_FORMAT = "date_format"
    FILE = "file"
    STR = "str"
    

class Output:
    INDICATORS = "indicators"
    

class ExtractAllInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "date_format": {
      "type": "string",
      "title": "Date Format",
      "description": "Dates matching this format are extracted. If All Formats is selected, found dates will be processed in the listed order documented (Note that selecting this option will increase the duration of the process)",
      "enum": [
        "dd/mm/yyyy",
        "mm/dd/yyyy",
        "dd/mm/yyyy",
        "dd\\\\mm\\\\yyyy",
        "dd.mm.yyyy",
        "dd-mm-yyyy",
        "dd.mm.yy",
        "dd-mm-yy",
        "dd/mm/yy",
        "dd\\\\mm\\\\yy",
        "mm/dd/yyyy",
        "mm\\\\dd\\\\yyyy",
        "mm.dd.yyyy",
        "mm-dd-yyyy",
        "mm/dd/yy",
        "mm\\\\dd\\\\yy",
        "mm.dd.yy",
        "mm-dd-yy",
        "dd/mmm/yyyy",
        "dd\\\\mmm\\\\yyyy",
        "dd.mmm.yyyy",
        "dd-mmm-yyyy",
        "dd/mmm/yy",
        "dd\\\\mmm\\\\yy",
        "dd.mmm.yy",
        "dd-mmm-yy",
        "yyyy.mm.dd",
        "yyyy-mm-dd",
        "yyyy/mm/dd",
        "yyyy\\\\mm\\\\dd",
        "yyyy.mmm.dd",
        "yyyy-mmm-dd",
        "yyyy/mmm/dd",
        "yyyy\\\\mmm\\\\dd",
        "yy.mm.dd",
        "yy-mm-dd",
        "yy/mm/dd",
        "yy\\\\mm\\\\dd",
        "yyyy-mm-ddThh:mm",
        "yyyy-mm-ddThh:mm:ss",
        "All Formats",
        ""
      ],
      "order": 1
    },
    "file": {
      "type": "string",
      "title": "File",
      "displayType": "bytes",
      "description": "Input file as bytes, supports text and binary file types such as PDF, DOCX, XLSX, PPTX, ODT, ODP, ODS",
      "format": "bytes",
      "order": 3
    },
    "str": {
      "type": "string",
      "title": "String",
      "description": "Input string",
      "order": 2
    }
  },
  "required": [
    "date_format"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ExtractAllOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "indicators": {
      "$ref": "#/definitions/indicators",
      "title": "Indicators",
      "description": "List of extracted indicators",
      "order": 1
    }
  },
  "definitions": {
    "hashes": {
      "type": "object",
      "title": "hashes",
      "properties": {
        "md5_hashes": {
          "type": "array",
          "title": "MD5 Hashes",
          "description": "Extracted MD5 Hashes from message",
          "items": {
            "type": "string"
          },
          "order": 1
        },
        "sha1_hashes": {
          "type": "array",
          "title": "SHA1 Hashes",
          "description": "Extracted SHA1 hashes from message",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "sha256_hashes": {
          "type": "array",
          "title": "SHA256 Hashes",
          "description": "Extracted SHA256 hashes from message",
          "items": {
            "type": "string"
          },
          "order": 3
        },
        "sha512_hashes": {
          "type": "array",
          "title": "SHA512 Hashes",
          "description": "Extracted SHA512 hashes from message",
          "items": {
            "type": "string"
          },
          "order": 4
        }
      }
    },
    "indicators": {
      "type": "object",
      "title": "indicators",
      "properties": {
        "cves": {
          "type": "array",
          "title": "CVEs",
          "description": "Extracted CVEs from message",
          "items": {
            "type": "string"
          },
          "order": 9
        },
        "dates": {
          "type": "array",
          "title": "Dates",
          "description": "Extracted dates from message",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "domains": {
          "type": "array",
          "title": "Domains",
          "description": "Extracted domains from message",
          "items": {
            "type": "string"
          },
          "order": 1
        },
        "email_addresses": {
          "type": "array",
          "title": "Email Addresses",
          "description": "Extracted email addresses from message",
          "items": {
            "type": "string"
          },
          "order": 5
        },
        "filepaths": {
          "type": "array",
          "title": "Filepaths",
          "description": "Extracted filepaths from message",
          "items": {
            "type": "string"
          },
          "order": 3
        },
        "hashes": {
          "$ref": "#/definitions/hashes",
          "title": "Hashes",
          "description": "Extracted hashes from message",
          "order": 6
        },
        "ip_addresses": {
          "$ref": "#/definitions/ip_addresses",
          "title": "IP Addressses",
          "description": "Extracted IP addresses from message",
          "order": 7
        },
        "mac_addresses": {
          "type": "array",
          "title": "MAC Addresses",
          "description": "Extracted MAC addresses from message",
          "items": {
            "type": "string"
          },
          "order": 8
        },
        "urls": {
          "type": "array",
          "title": "URLs",
          "description": "Extracted URLs from message",
          "items": {
            "type": "string"
          },
          "order": 4
        },
        "uuids": {
          "type": "array",
          "title": "UUIDs",
          "description": "Extracted UUIDs from message",
          "items": {
            "type": "string"
          },
          "order": 10
        }
      },
      "definitions": {
        "hashes": {
          "type": "object",
          "title": "hashes",
          "properties": {
            "md5_hashes": {
              "type": "array",
              "title": "MD5 Hashes",
              "description": "Extracted MD5 Hashes from message",
              "items": {
                "type": "string"
              },
              "order": 1
            },
            "sha1_hashes": {
              "type": "array",
              "title": "SHA1 Hashes",
              "description": "Extracted SHA1 hashes from message",
              "items": {
                "type": "string"
              },
              "order": 2
            },
            "sha256_hashes": {
              "type": "array",
              "title": "SHA256 Hashes",
              "description": "Extracted SHA256 hashes from message",
              "items": {
                "type": "string"
              },
              "order": 3
            },
            "sha512_hashes": {
              "type": "array",
              "title": "SHA512 Hashes",
              "description": "Extracted SHA512 hashes from message",
              "items": {
                "type": "string"
              },
              "order": 4
            }
          }
        },
        "ip_addresses": {
          "type": "object",
          "title": "ip_addresses",
          "properties": {
            "ipv4_addresses": {
              "type": "array",
              "title": "IPv4 Addressses",
              "description": "Extracted IPv4 addressses from message",
              "items": {
                "type": "string"
              },
              "order": 1
            },
            "ipv6_addresses": {
              "type": "array",
              "title": "IPv6 Addressses",
              "description": "Extracted IPv6 addresses from message",
              "items": {
                "type": "string"
              },
              "order": 2
            }
          }
        }
      }
    },
    "ip_addresses": {
      "type": "object",
      "title": "ip_addresses",
      "properties": {
        "ipv4_addresses": {
          "type": "array",
          "title": "IPv4 Addressses",
          "description": "Extracted IPv4 addressses from message",
          "items": {
            "type": "string"
          },
          "order": 1
        },
        "ipv6_addresses": {
          "type": "array",
          "title": "IPv6 Addressses",
          "description": "Extracted IPv6 addresses from message",
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
