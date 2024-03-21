# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "List all assets found in the model"


class Input:
    FIELDS = "fields"
    FILTER = "filter"
    RANGE = "range"


class Output:
    DATA = "data"


class GetAssetsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "fields": {
      "type": "string",
      "title": "Fields",
      "description": "Specify the list of fields to be returned in the response. Specify the subfields in parentheses. Multiple fields in the same object must be comma separated. Sample fields to filter are id, domain_id, hostnames(id), interfaces, products. More information about the fields can be found in plugin documentation",
      "order": 3
    },
    "filter": {
      "type": "string",
      "title": "Filter",
      "description": "Restrict the elements in a list based on the contents of various fields",
      "order": 2
    },
    "range": {
      "type": "string",
      "title": "Range",
      "description": "Paging requests are specified with the Range parameter. E.g. the example default range returns the first 50 records, a custom range of 6-10 returns the 6th to 10th records",
      "default": "1-50",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetAssetsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "array",
      "title": "Assets Data",
      "description": "JSON data of the Assets",
      "items": {
        "$ref": "#/definitions/assets"
      },
      "order": 1
    }
  },
  "definitions": {
    "assets": {
      "type": "object",
      "title": "assets",
      "properties": {
        "vulnerability_count": {
          "type": "integer",
          "title": "Vulnerability Count",
          "description": "Vulnerability count",
          "order": 1
        },
        "interfaces": {
          "type": "array",
          "title": "Interfaces",
          "description": "Interfaces",
          "items": {
            "$ref": "#/definitions/interfaces"
          },
          "order": 2
        },
        "risk_score_sum": {
          "type": "number",
          "title": "Risk Score Sum",
          "description": "Risk score sum",
          "order": 3
        },
        "host_urls": {
          "type": "array",
          "title": "Hostnames",
          "description": "Hostnames",
          "items": {
            "$ref": "#/definitions/host_urls"
          },
          "order": 4
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 5
        },
        "users": {
          "type": "array",
          "title": "Users",
          "description": "Users",
          "items": {
            "type": "object"
          },
          "order": 6
        },
        "domain_id": {
          "type": "integer",
          "title": "Domain ID",
          "description": "Domain ID",
          "order": 7
        },
        "properties": {
          "type": "array",
          "title": "Properties",
          "description": "Properties",
          "items": {
            "$ref": "#/definitions/properties"
          },
          "order": 8
        },
        "products": {
          "type": "array",
          "title": "Products",
          "description": "Products",
          "items": {
            "$ref": "#/definitions/products"
          },
          "order": 9
        }
      }
    },
    "interfaces": {
      "type": "object",
      "title": "interfaces",
      "properties": {
        "created": {
          "type": "integer",
          "title": "Created",
          "description": "Created",
          "order": 1
        },
        "first_seen_profiler": {
          "type": "string",
          "title": "First Seen Profiler",
          "description": "First seen profiler",
          "order": 2
        },
        "first_seen_scanner": {
          "type": "string",
          "title": "First Seen Scanner",
          "description": "First seen scanner",
          "order": 3
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 4
        },
        "ip_addresses": {
          "type": "array",
          "title": "IP Addresses",
          "description": "IP addresses",
          "items": {
            "$ref": "#/definitions/ip_addresses"
          },
          "order": 5
        },
        "last_seen_profiler": {
          "type": "string",
          "title": "Last Seen Profiler",
          "description": "Last seen profiler",
          "order": 6
        },
        "last_seen_scanner": {
          "type": "string",
          "title": "Last Seen Scanner",
          "description": "Last seen scanner",
          "order": 7
        },
        "mac_address": {
          "type": "string",
          "title": "MAC Address",
          "description": "MAC address",
          "order": 8
        }
      }
    },
    "ip_addresses": {
      "type": "object",
      "title": "ip_addresses",
      "properties": {
        "created": {
          "type": "integer",
          "title": "Created",
          "description": "Created",
          "order": 1
        },
        "first_seen_profiler": {
          "type": "string",
          "title": "First Seen Profiler",
          "description": "First seen profiler",
          "order": 2
        },
        "first_seen_scanner": {
          "type": "string",
          "title": "First Seen Scanner",
          "description": "First seen scanner",
          "order": 3
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 4
        },
        "last_seen_profiler": {
          "type": "string",
          "title": "Last Seen Profiler",
          "description": "Last seen profiler",
          "order": 5
        },
        "last_seen_scanner": {
          "type": "string",
          "title": "Last Seen Scanner",
          "description": "Last seen scanner",
          "order": 6
        },
        "network_id": {
          "type": "integer",
          "title": "Network ID",
          "description": "Network ID",
          "order": 7
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 8
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Value",
          "order": 9
        }
      }
    },
    "host_urls": {
      "type": "object",
      "title": "host_urls",
      "properties": {
        "created": {
          "type": "integer",
          "title": "Created",
          "description": "Created",
          "order": 1
        },
        "first_seen_profiler": {
          "type": "string",
          "title": "First Seen Profiler",
          "description": "First seen profiler",
          "order": 2
        },
        "first_seen_scanner": {
          "type": "string",
          "title": "First Seen Scanner",
          "description": "First seen scanner",
          "order": 3
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 4
        },
        "last_seen_profiler": {
          "type": "string",
          "title": "Last Seen Profiler",
          "description": "Last seen profiler",
          "order": 5
        },
        "last_seen_scanner": {
          "type": "string",
          "title": "Last Seen Scanner",
          "description": "Last seen scanner",
          "order": 6
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 7
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type",
          "order": 8
        }
      }
    },
    "properties": {
      "type": "object",
      "title": "properties",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 1
        },
        "last_reported": {
          "type": "integer",
          "title": "Last Reported",
          "description": "Last reported",
          "order": 2
        },
        "last_reported_by": {
          "type": "string",
          "title": "Last Reported By",
          "description": "Last reported by",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name",
          "order": 4
        },
        "type_id": {
          "type": "integer",
          "title": "Type ID",
          "description": "Type ID",
          "order": 5
        },
        "value": {
          "type": "string",
          "title": "Value",
          "description": "Value",
          "order": 6
        }
      }
    },
    "products": {
      "type": "object",
      "title": "products",
      "properties": {
        "first_seen_profiler": {
          "type": "string",
          "title": "First Seen Profiler",
          "description": "First seen profiler",
          "order": 1
        },
        "first_seen_scanner": {
          "type": "string",
          "title": "First Seen Scanner",
          "description": "First seen scanner",
          "order": 2
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "ID",
          "order": 3
        },
        "last_scanned_for": {
          "type": "string",
          "title": "Last Scanned For",
          "description": "Last scanned for",
          "order": 4
        },
        "last_seen_profiler": {
          "type": "string",
          "title": "Last Seen Profiler",
          "description": "Last seen profiler",
          "order": 5
        },
        "last_seen_scanner": {
          "type": "string",
          "title": "Last Seen Scanner",
          "description": "Last seen scanner",
          "order": 6
        },
        "product_variant_id": {
          "type": "integer",
          "title": "Product Variant ID",
          "description": "Product variant ID",
          "order": 7
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
