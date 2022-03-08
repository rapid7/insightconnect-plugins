# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve details for an individual event given the event ID"


class Input:
    EVENT_IDS = "event_ids"
    

class Output:
    EVENTINFO = "eventinfo"
    SUCCESS = "success"
    

class GetDetailsForSpecificEventInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "event_ids": {
      "type": "string",
      "title": "Event ID",
      "description": "Event ID used to retrieve event details. Example: 422af3fc3a7411ea8da649e797467dc0",
      "order": 1
    }
  },
  "required": [
    "event_ids"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetDetailsForSpecificEventOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "eventinfo": {
      "$ref": "#/definitions/event_info",
      "title": "Event Info",
      "description": "Detailed information on the event",
      "order": 2
    },
    "results": {
      "type": "array",
      "title": "Results",
      "description": "Detailed information on the event",
      "items": {
        "$ref": "#/definitions/event_info"
      },
      "order": 8
    },
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Success",
      "order": 1
    }
  },
  "definitions": {
    "event_info": {
      "type": "object",
      "title": "event_info",
      "properties": {
        "backend_timestamp": {
          "type": "string",
          "title": "Backend Timestamp",
          "displayType": "date",
          "description": "Backend timestamp",
          "format": "date-time",
          "order": 55
        },
        "device_external_ip": {
          "type": "array",
          "title": "Device External IP",
          "description": "Device external IP",
          "items": {
            "type": "string"
          },
          "order": 37
        },
        "device_group_id": {
          "type": "integer",
          "title": "Device Group ID",
          "description": "Device group ID",
          "order": 8
        },
        "device_id": {
          "type": "integer",
          "title": "Device ID",
          "description": "Device ID",
          "order": 47
        },
        "device_internal_ip": {
          "type": "string",
          "title": "Device Internal IP",
          "description": "Device internal IP",
          "order": 41
        },
        "device_location": {
          "type": "string",
          "title": "Device Location",
          "description": "Device location",
          "order": 50
        },
        "device_name": {
          "type": "array",
          "title": "Device Name",
          "description": "Device name",
          "items": {
            "type": "string"
          },
          "order": 54
        },
        "device_os": {
          "type": "string",
          "title": "Device OS",
          "description": "Device OS",
          "order": 45
        },
        "device_os_version": {
          "type": "string",
          "title": "Device OS Version",
          "description": "Device OS version",
          "order": 52
        },
        "device_policy": {
          "type": "string",
          "title": "Device Policy",
          "description": "Device policy",
          "order": 57
        },
        "device_policy_id": {
          "type": "integer",
          "title": "Device Policy ID",
          "description": "Device policy ID",
          "order": 46
        },
        "device_target_priority": {
          "type": "string",
          "title": "Device Target Priority",
          "description": "Device target priority",
          "order": 3
        },
        "device_timestamp": {
          "type": "string",
          "title": "Device Timestamp",
          "displayType": "date",
          "description": "Device timestamp",
          "format": "date-time",
          "order": 15
        },
        "document_guid": {
          "type": "string",
          "title": "Document GUID",
          "description": "Document GUID",
          "order": 23
        },
        "enriched": {
          "type": "boolean",
          "title": "Enriched",
          "description": "Enriched",
          "order": 26
        },
        "enriched_event_type": {
          "type": "string",
          "title": "Enriched Event Type",
          "description": "Enriched event type",
          "order": 25
        },
        "event_description": {
          "type": "string",
          "title": "Event Description",
          "description": "Event description",
          "order": 19
        },
        "event_id": {
          "type": "string",
          "title": "Event ID",
          "description": "Event ID",
          "order": 21
        },
        "event_network_inbound": {
          "type": "boolean",
          "title": "Event Network Inbound",
          "description": "Event network inbound",
          "order": 48
        },
        "event_network_local_ipv4": {
          "type": "string",
          "title": "Event Network Local IPv4",
          "description": "Event network local IPv4",
          "order": 42
        },
        "event_network_location": {
          "type": "string",
          "title": "Event Network Location",
          "description": "Event network location",
          "order": 1
        },
        "event_network_protocol": {
          "type": "string",
          "title": "Event Network Protocol",
          "description": "Event network protocol",
          "order": 29
        },
        "event_network_remote_ipv4": {
          "type": "string",
          "title": "Event Network Remote IPv4",
          "description": "Event network remote IPv4",
          "order": 32
        },
        "event_network_remote_port": {
          "type": "integer",
          "title": "Event Network Remote Port",
          "description": "Event network remote port",
          "order": 7
        },
        "event_report_code": {
          "type": "string",
          "title": "Event Report Code",
          "description": "Event report code",
          "order": 39
        },
        "event_threat_score": {
          "type": "array",
          "title": "Event Threat Score",
          "description": "Event threat score",
          "items": {
            "type": "integer"
          },
          "order": 40
        },
        "event_type": {
          "type": "string",
          "title": "Event Type",
          "description": "Event type",
          "order": 4
        },
        "ingress_time": {
          "type": "integer",
          "title": "Ingress Time",
          "description": "Ingress time",
          "order": 44
        },
        "legacy": {
          "type": "boolean",
          "title": "Legacy",
          "description": "Legacy",
          "order": 10
        },
        "netconn_domain": {
          "type": "string",
          "title": "Netconn Domain",
          "description": "Netconn domain",
          "order": 18
        },
        "netconn_inbound": {
          "type": "boolean",
          "title": "Netconn Inbound",
          "description": "Netconn inbound",
          "order": 5
        },
        "netconn_ipv4": {
          "type": "integer",
          "title": "Netconn IPv4",
          "description": "Netconn IPv4",
          "order": 38
        },
        "netconn_local_ipv4": {
          "type": "integer",
          "title": "Netconn Local IPv4",
          "description": "Netconn local IPv4",
          "order": 27
        },
        "netconn_local_port": {
          "type": "integer",
          "title": "Netconn Local Port",
          "description": "Netconn local port",
          "order": 51
        },
        "netconn_location": {
          "type": "string",
          "title": "Netconn Location",
          "description": "Netconn location",
          "order": 16
        },
        "netconn_port": {
          "type": "integer",
          "title": "Netconn Port",
          "description": "Netconn port",
          "order": 13
        },
        "netconn_protocol": {
          "type": "string",
          "title": "Netconn Protocol",
          "description": "Netconn protocol",
          "order": 14
        },
        "org_id": {
          "type": "string",
          "title": "Org ID",
          "description": "Org ID",
          "order": 53
        },
        "parent_effective_reputation": {
          "type": "string",
          "title": "Parent Effective Reputation",
          "description": "Parent effective reputation",
          "order": 34
        },
        "parent_effective_reputation_source": {
          "type": "string",
          "title": "Parent Effective Reputation Source",
          "description": "Parent effective reputation source",
          "order": 30
        },
        "parent_guid": {
          "type": "string",
          "title": "Parent GUID",
          "description": "Parent GUID",
          "order": 22
        },
        "parent_hash": {
          "type": "array",
          "title": "Parent Hash",
          "description": "Parent hash",
          "items": {
            "type": "string"
          },
          "order": 28
        },
        "parent_name": {
          "type": "string",
          "title": "Parent Name",
          "description": "Parent name",
          "order": 36
        },
        "parent_pid": {
          "type": "integer",
          "title": "Parent PID",
          "description": "Parent PID",
          "order": 56
        },
        "parent_reputation": {
          "type": "string",
          "title": "Parent Reputation",
          "description": "Parent reputation",
          "order": 58
        },
        "process_cmdline": {
          "type": "array",
          "title": "Process Cmdline",
          "description": "Process cmdline",
          "items": {
            "type": "string"
          },
          "order": 20
        },
        "process_cmdline_length": {
          "type": "array",
          "title": "Process Cmdline Length",
          "description": "Process cmdline length",
          "items": {
            "type": "integer"
          },
          "order": 24
        },
        "process_effective_reputation": {
          "type": "string",
          "title": "Process Effective Reputation",
          "description": "Process effective reputation",
          "order": 6
        },
        "process_effective_reputation_source": {
          "type": "string",
          "title": "Process Effective Reputation Source",
          "description": "Process effective reputation source",
          "order": 9
        },
        "process_guid": {
          "type": "string",
          "title": "Process GUID",
          "description": "Process GUID",
          "order": 49
        },
        "process_hash": {
          "type": "array",
          "title": "Process Hash",
          "description": "Process hash",
          "items": {
            "type": "string"
          },
          "order": 33
        },
        "process_name": {
          "type": "array",
          "title": "Process Name",
          "description": "Process name",
          "items": {
            "type": "string"
          },
          "order": 2
        },
        "process_pid": {
          "type": "array",
          "title": "Process PID",
          "description": "Process PID",
          "items": {
            "type": "integer"
          },
          "order": 31
        },
        "process_reputation": {
          "type": "string",
          "title": "Process Reputation",
          "description": "Process reputation",
          "order": 43
        },
        "process_sha256": {
          "type": "string",
          "title": "Process SHA-256",
          "description": "Process SHA-256",
          "order": 35
        },
        "process_start_time": {
          "type": "string",
          "title": "Process Start Time",
          "description": "Process start time",
          "order": 11
        },
        "process_username": {
          "type": "array",
          "title": "Process Username",
          "description": "Process username",
          "items": {
            "type": "string"
          },
          "order": 12
        },
        "ttp": {
          "type": "array",
          "title": "TTP",
          "description": "TTP",
          "items": {
            "type": "string"
          },
          "order": 17
        },
        "watchlist_hit": {
          "type": "array",
          "title": "Watchlist Hit",
          "description": "Identifier for specific hit record(s) generated by a watchlist, from report metadata; format '\\u003cwatchlist_id\\u003e:\\u003creport_id\\u003e:\\u003creport_severity\\u003e'",
          "items": {
            "type": "string"
          },
          "order": 184
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
