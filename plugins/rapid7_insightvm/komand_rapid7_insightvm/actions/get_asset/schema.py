# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Gets an asset by ID"


class Input:
    ASSET_ID = "asset_id"


class Output:
    ASSET = "asset"


class GetAssetInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "asset_id": {
      "type": "integer",
      "title": "Asset ID",
      "description": "Identifier of asset",
      "order": 1
    }
  },
  "required": [
    "asset_id"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAssetOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "asset": {
      "$ref": "#/definitions/asset",
      "title": "Asset",
      "description": "Asset details",
      "order": 1
    }
  },
  "required": [
    "asset"
  ],
  "definitions": {
    "asset": {
      "type": "object",
      "title": "asset",
      "properties": {
        "addresses": {
          "type": "array",
          "title": "Addresses",
          "description": "All addresses discovered on the asset",
          "items": {
            "$ref": "#/definitions/address"
          },
          "order": 1
        },
        "assessedForPolicies": {
          "type": "boolean",
          "title": "Assessed for Policies",
          "description": "Whether the asset has been assessed for policies at least once",
          "order": 2
        },
        "assessedForVulnerabilities": {
          "type": "boolean",
          "title": "Assessed for Vulnerabilities",
          "description": "Whether the asset has been assessed for vulnerabilities at least once",
          "order": 3
        },
        "configurations": {
          "type": "array",
          "title": "Configurations",
          "description": "Configuration key-values pairs enumerated on the asset",
          "items": {
            "$ref": "#/definitions/configuration"
          },
          "order": 4
        },
        "databases": {
          "type": "array",
          "title": "Databases",
          "description": "Databases enumerated on the asset",
          "items": {
            "$ref": "#/definitions/database"
          },
          "order": 5
        },
        "files": {
          "type": "array",
          "title": "Files",
          "description": "Files discovered with searching on the asset",
          "items": {
            "$ref": "#/definitions/insightvm_file"
          },
          "order": 6
        },
        "history": {
          "type": "array",
          "title": "History",
          "description": "History of changes to the asset over time",
          "items": {
            "$ref": "#/definitions/history"
          },
          "order": 7
        },
        "hostName": {
          "type": "string",
          "title": "Hostname",
          "description": "Primary host name (local or FQDN) of the asset",
          "order": 8
        },
        "hostNames": {
          "type": "array",
          "title": "Hostnames",
          "description": "All hostnames or aliases discovered on the asset",
          "items": {
            "$ref": "#/definitions/hostName"
          },
          "order": 9
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Identifier of the asset",
          "order": 10
        },
        "ids": {
          "type": "array",
          "title": "IDs",
          "description": "Unique identifiers found on the asset, such as hardware or operating system identifiers",
          "items": {
            "$ref": "#/definitions/id"
          },
          "order": 11
        },
        "ip": {
          "type": "string",
          "title": "IP",
          "description": "Primary IPv4 or IPv6 address of the asset",
          "order": 12
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "Hypermedia links to corresponding or related resources",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 13
        },
        "mac": {
          "type": "string",
          "title": "MAC",
          "description": "Media Access Control (MAC) address, e.g. AF:12:BC:5A:F7:48",
          "order": 14
        },
        "os": {
          "type": "string",
          "title": "OS",
          "description": "Full description of the operating system of the asset",
          "order": 15
        },
        "osFingerprint": {
          "$ref": "#/definitions/osFingerprint",
          "title": "OS Fingerprint",
          "description": "Details of the operating system of the asset",
          "order": 16
        },
        "rawRiskScore": {
          "type": "number",
          "title": "Raw Risk Score",
          "description": "Base risk score of the asset",
          "order": 17
        },
        "riskScore": {
          "type": "number",
          "title": "Risk Score",
          "description": "Risk score (with criticality adjustments) of the asset",
          "order": 18
        },
        "services": {
          "type": "array",
          "title": "Services",
          "description": "Services discovered on the asset",
          "items": {
            "$ref": "#/definitions/service"
          },
          "order": 19
        },
        "software": {
          "type": "array",
          "title": "Software",
          "description": "Software discovered on the asset",
          "items": {
            "$ref": "#/definitions/software"
          },
          "order": 20
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of asset e.g. unknown, guest, hypervisor, physical, mobile",
          "order": 21
        },
        "userGroups": {
          "type": "array",
          "title": "User Groups",
          "description": "User group accounts enumerated on the asset",
          "items": {
            "$ref": "#/definitions/userGroup"
          },
          "order": 22
        },
        "users": {
          "type": "array",
          "title": "Users",
          "description": "User accounts enumerated on the asset",
          "items": {
            "$ref": "#/definitions/user"
          },
          "order": 23
        },
        "vulnerabilities": {
          "$ref": "#/definitions/vulnerabilities",
          "title": "Vulnerabilities",
          "description": " Summary information for vulnerabilities on the asset",
          "order": 24
        }
      }
    },
    "address": {
      "type": "object",
      "title": "address",
      "properties": {
        "ip": {
          "type": "string",
          "title": "IP",
          "description": "IPv4 or IPv6 address",
          "order": 1
        },
        "mac": {
          "type": "string",
          "title": "MAC",
          "description": "Media Access Control (MAC) address, e.g. AF:12:BC:5A:F7:48",
          "order": 2
        }
      }
    },
    "configuration": {
      "type": "object",
      "title": "configuration",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the configuration value",
          "order": 1
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Configuration value",
          "order": 2
        }
      }
    },
    "database": {
      "type": "object",
      "title": "database",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description of the database instance",
          "order": 1
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Identifier of the database",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the database instance",
          "order": 3
        }
      }
    },
    "insightvm_file": {
      "type": "object",
      "title": "insightvm_file",
      "properties": {
        "attributes": {
          "type": "array",
          "title": "Attributes",
          "description": "Attributes detected on the file",
          "items": {
            "$ref": "#/definitions/configuration"
          },
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the file",
          "order": 2
        },
        "size": {
          "type": "integer",
          "title": "Size",
          "description": "Size of the regular file (in bytes). If the file is a directory, no value is returned",
          "order": 3
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of the file, e.g. file or directory",
          "order": 4
        },
        "content": {
          "type": "string",
          "format": "bytes",
          "displayType": "bytes",
          "title": "Contents",
          "description": "Contents of the file",
          "order": 5
        }
      }
    },
    "history": {
      "type": "object",
      "title": "history",
      "properties": {
        "date": {
          "type": "string",
          "title": "Date",
          "description": "Date the asset information was collected or changed",
          "order": 1
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Additional information describing the change",
          "order": 2
        },
        "scanId": {
          "type": "integer",
          "title": "Scan ID",
          "description": "If a scan-oriented change, the identifier of the corresponding scan the asset was scanned in",
          "order": 3
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type, for additional information see the help section of this plugin",
          "order": 4
        },
        "user": {
          "type": "string",
          "title": "User",
          "description": "User",
          "order": 5
        },
        "version": {
          "type": "integer",
          "title": "Version",
          "description": "Version",
          "order": 6
        },
        "vulnerabilityExceptionId": {
          "type": "integer",
          "title": "Vulnerability Exception ID",
          "description": "Vulnerability exception ID",
          "order": 7
        }
      }
    },
    "hostName": {
      "type": "object",
      "title": "hostName",
      "properties": {
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 1
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "Source",
          "order": 2
        }
      }
    },
    "id": {
      "type": "object",
      "title": "id",
      "properties": {
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "source": {
          "type": "string",
          "title": "Source",
          "description": "Source",
          "order": 2
        }
      }
    },
    "link": {
      "type": "object",
      "title": "link",
      "properties": {
        "href": {
          "type": "string",
          "title": "URL",
          "description": "A hypertext reference, which is either a URI (see RFC 3986) or URI template (see RFC 6570)",
          "order": 1
        },
        "rel": {
          "type": "string",
          "title": "Rel",
          "description": "Link relation type following RFC 5988",
          "order": 2
        }
      }
    },
    "osFingerprint": {
      "type": "object",
      "title": "osFingerprint",
      "properties": {
        "architecture": {
          "type": "string",
          "title": "Architecture",
          "description": "The architecture of the operating system",
          "order": 1
        },
        "configurations": {
          "type": "array",
          "title": "Configuration",
          "description": "Configuration key-values pairs enumerated on the operating system",
          "items": {
            "$ref": "#/definitions/configuration"
          },
          "order": 2
        },
        "cpe": {
          "$ref": "#/definitions/cpe",
          "title": "CPE",
          "description": "Common Platform Enumeration",
          "order": 3
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "The description of the operating system (containing vendor, family, product, version and architecture in a single string)",
          "order": 4
        },
        "family": {
          "type": "string",
          "title": "Family",
          "description": "Family of the operating system",
          "order": 5
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Identifier of the operating system",
          "order": 6
        },
        "product": {
          "type": "string",
          "title": "Product",
          "description": "Name of the operating system",
          "order": 7
        },
        "systemName": {
          "type": "string",
          "title": "System Name",
          "description": "A combination of vendor and family (with redundancies removed), suitable for grouping",
          "order": 8
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of operating system",
          "order": 9
        },
        "vendor": {
          "type": "string",
          "title": "Vendor",
          "description": "Vendor of the operating system",
          "order": 10
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "Version of the operating system",
          "order": 11
        }
      }
    },
    "cpe": {
      "type": "object",
      "title": "cpe",
      "properties": {
        "edition": {
          "type": "string",
          "title": "Edition",
          "description": "Edition-related terms applied by the vendor to the product",
          "order": 1
        },
        "language": {
          "type": "string",
          "title": "Language",
          "description": "Defines the language supported in the user interface of the product being described. The format of the language tag adheres to RFC 5646",
          "order": 2
        },
        "other": {
          "type": "string",
          "title": "Other",
          "description": "Captures any other general descriptive or identifying information which is vendor- or product-specific and which does not logically fit in any other attribute value",
          "order": 3
        },
        "part": {
          "type": "string",
          "title": "Part",
          "description": "A single letter code that designates the particular platform part that is being identified",
          "order": 4
        },
        "product": {
          "type": "string",
          "title": "Product",
          "description": "Most common and recognizable title or name of the product",
          "order": 5
        },
        "swEdition": {
          "type": "string",
          "title": "Software Edition",
          "description": "Characterizes how the product is tailored to a particular market or class of end users",
          "order": 6
        },
        "targetHW": {
          "type": "string",
          "title": "Target Hardware",
          "description": "Characterize the instruction set architecture on which the product operates",
          "order": 7
        },
        "targetSW": {
          "type": "string",
          "title": "Target Software",
          "description": "Characterizes the software computing environment within which the product operates",
          "order": 8
        },
        "update": {
          "type": "string",
          "title": "Update",
          "description": "Vendor-specific alphanumeric strings characterizing the particular update, service pack, or point release of the product",
          "order": 9
        },
        "v2.2": {
          "type": "string",
          "title": "Version 2.2",
          "description": "The full CPE string in the CPE 2.2 format",
          "order": 10
        },
        "v2.3": {
          "type": "string",
          "title": "Version 2.3",
          "description": "The full CPE string in the CPE 2.3 format",
          "order": 11
        },
        "vendor": {
          "type": "string",
          "title": "Vendor",
          "description": "The person or organization that manufactured or created the product",
          "order": 12
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "Vendor-specific alphanumeric strings characterizing the particular release version of the product",
          "order": 13
        }
      }
    },
    "service": {
      "type": "object",
      "title": "service",
      "properties": {
        "configurations": {
          "type": "array",
          "title": "Configurations",
          "description": "Configuration key-values pairs enumerated on the service",
          "items": {
            "$ref": "#/definitions/configuration"
          },
          "order": 1
        },
        "databases": {
          "type": "array",
          "title": "Databases",
          "description": "Databases enumerated on the service",
          "items": {
            "$ref": "#/definitions/database"
          },
          "order": 2
        },
        "family": {
          "type": "string",
          "title": "Family",
          "description": "Family of the service",
          "order": 3
        },
        "links": {
          "type": "array",
          "title": "Links",
          "description": "Hypermedia links to corresponding or related resources",
          "items": {
            "$ref": "#/definitions/link"
          },
          "order": 4
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the service",
          "order": 5
        },
        "port": {
          "type": "integer",
          "title": "Port",
          "description": "Port of the service",
          "order": 6
        },
        "product": {
          "type": "string",
          "title": "Product",
          "description": "Product running the service",
          "order": 7
        },
        "protocol": {
          "type": "string",
          "title": "Protocol",
          "description": "Protocol of the service",
          "order": 8
        },
        "userGroups": {
          "type": "array",
          "title": "User Groups",
          "description": "User groups",
          "items": {
            "$ref": "#/definitions/userGroup"
          },
          "order": 9
        },
        "users": {
          "type": "array",
          "title": "Users",
          "description": "Users",
          "items": {
            "$ref": "#/definitions/user"
          },
          "order": 10
        },
        "vendor": {
          "type": "string",
          "title": "Vendor",
          "description": "Vendor of the service",
          "order": 11
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "Version of the service",
          "order": 12
        },
        "webApplications": {
          "type": "array",
          "title": "Web Applications",
          "description": "Web applications found on the service",
          "items": {
            "$ref": "#/definitions/webApplication"
          },
          "order": 13
        }
      }
    },
    "userGroup": {
      "type": "object",
      "title": "userGroup",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Identifier of the user group",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the user group",
          "order": 2
        }
      }
    },
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "fullName": {
          "type": "string",
          "title": "Full Name",
          "description": "Full name of the user account",
          "order": 1
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Identifier of the user account",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of the user account",
          "order": 3
        }
      }
    },
    "webApplication": {
      "type": "object",
      "title": "webApplication",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Identifier of the web application",
          "order": 1
        },
        "pages": {
          "type": "array",
          "title": "Pages",
          "description": "Pages",
          "items": {
            "$ref": "#/definitions/page"
          },
          "order": 2
        },
        "root": {
          "type": "string",
          "title": "Root",
          "description": "Web root of the web application",
          "order": 3
        },
        "virtualHost": {
          "type": "string",
          "title": "Virtual Host",
          "description": "Virtual host of the web application",
          "order": 4
        }
      }
    },
    "page": {
      "type": "object",
      "title": "page",
      "properties": {
        "linkType": {
          "type": "string",
          "title": "Link Type",
          "description": "Type of link used to traverse or detect the page",
          "order": 1
        },
        "path": {
          "type": "string",
          "title": "Path",
          "description": "Path to the page (URI)",
          "order": 2
        },
        "response": {
          "type": "integer",
          "title": "Response",
          "description": "HTTP response code observed with retrieving the page",
          "order": 3
        }
      }
    },
    "software": {
      "type": "object",
      "title": "software",
      "properties": {
        "configurations": {
          "type": "array",
          "title": "Configurations",
          "description": "Configurations",
          "items": {
            "$ref": "#/definitions/configuration"
          },
          "order": 1
        },
        "cpe": {
          "$ref": "#/definitions/cpe",
          "title": "CPE",
          "description": "CPE",
          "order": 2
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description of the software",
          "order": 3
        },
        "family": {
          "type": "string",
          "title": "Family",
          "description": "Family of the software",
          "order": 4
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 5
        },
        "product": {
          "type": "string",
          "title": "Product",
          "description": "Product of the software",
          "order": 6
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of the software",
          "order": 7
        },
        "vendor": {
          "type": "string",
          "title": "Vendor",
          "description": "Vendor of the software",
          "order": 8
        },
        "version": {
          "type": "string",
          "title": "Version",
          "description": "Version of the software",
          "order": 9
        }
      }
    },
    "vulnerabilities": {
      "type": "object",
      "title": "vulnerabilities",
      "properties": {
        "critical": {
          "type": "integer",
          "title": "Critical",
          "description": "Number of critical vulnerabilities",
          "order": 1
        },
        "exploits": {
          "type": "integer",
          "title": "Exploits",
          "description": "Number of distinct exploits that can exploit any of the vulnerabilities on the asset",
          "order": 2
        },
        "malwareKits": {
          "type": "integer",
          "title": "Malware Kits",
          "description": "Number of distinct malware kits that vulnerabilities on the asset are susceptible to",
          "order": 3
        },
        "moderate": {
          "type": "integer",
          "title": "Moderate",
          "description": "Number of moderate vulnerabilities",
          "order": 4
        },
        "severe": {
          "type": "integer",
          "title": "Severe",
          "description": "Number of severe vulnerabilities",
          "order": 5
        },
        "total": {
          "type": "integer",
          "title": "Total",
          "description": "Total number of vulnerabilities",
          "order": 6
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
