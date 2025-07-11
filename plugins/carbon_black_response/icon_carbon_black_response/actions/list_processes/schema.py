# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "List Carbon Black processes with given parameters"


class Input:
    QUERY = "query"
    ROWS = "rows"
    START = "start"


class Output:
    PROCESSES = "processes"


class ListProcessesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "query": {
      "type": "string",
      "title": "Query String",
      "description": "Accepts the same data as the search box on the Process Search page",
      "order": 1
    },
    "rows": {
      "type": "integer",
      "title": "Rows",
      "description": "How many rows of data to return. Default is 10",
      "default": 10,
      "order": 2
    },
    "start": {
      "type": "integer",
      "title": "Start",
      "description": "What row of data to start at. Default is 0",
      "default": 0,
      "order": 3
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListProcessesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "processes": {
      "type": "array",
      "title": "Processes",
      "description": "The list of processes",
      "items": {
        "$ref": "#/definitions/process"
      },
      "order": 1
    }
  },
  "definitions": {
    "process": {
      "type": "object",
      "title": "process",
      "properties": {
        "mod_load": {
          "type": "integer",
          "title": "Mod Load",
          "order": 1
        },
        "sensor_id": {
          "type": "integer",
          "title": "Sensor ID",
          "order": 2
        },
        "uid": {
          "type": "string",
          "title": "UID",
          "order": 3
        },
        "filtering_known_dls": {
          "type": "boolean",
          "title": "Filtering Known Downloads",
          "order": 4
        },
        "process_md5": {
          "type": "string",
          "title": "MD5",
          "order": 5
        },
        "parent_unique_id": {
          "type": "string",
          "title": "Parent Unique ID",
          "order": 6
        },
        "cmdline": {
          "type": "string",
          "title": "CMD Line",
          "order": 7
        },
        "path": {
          "type": "string",
          "title": "Path",
          "order": 8
        },
        "filemod_count": {
          "type": "integer",
          "title": "Filemod Count",
          "order": 9
        },
        "id": {
          "type": "string",
          "title": "ID",
          "order": 10
        },
        "parent_name": {
          "type": "string",
          "title": "Parent Name",
          "order": 11
        },
        "crossproc_count": {
          "type": "integer",
          "title": "Crossproc Count",
          "order": 12
        },
        "parent_pid": {
          "type": "integer",
          "title": "Parent PID",
          "order": 13
        },
        "hostname": {
          "type": "string",
          "title": "Hostname",
          "order": 14
        },
        "last_update": {
          "type": "string",
          "title": "Last Update",
          "order": 15
        },
        "start": {
          "type": "string",
          "title": "Start",
          "order": 16
        },
        "comms_ip": {
          "type": "integer",
          "title": "Comms IP",
          "order": 17
        },
        "regmod_count": {
          "type": "integer",
          "title": "Regmod Count",
          "order": 18
        },
        "interface_ip": {
          "type": "integer",
          "title": "Interface IP",
          "order": 19
        },
        "process_pid": {
          "type": "integer",
          "title": "PID",
          "order": 20
        },
        "username": {
          "type": "string",
          "title": "Username",
          "order": 21
        },
        "terminated": {
          "type": "boolean",
          "title": "Terminated",
          "order": 22
        },
        "process_name": {
          "type": "string",
          "title": "Name",
          "order": 23
        },
        "emet_count": {
          "type": "integer",
          "title": "EMET Count",
          "order": 24
        },
        "group": {
          "type": "string",
          "title": "Group",
          "order": 25
        },
        "netconn_count": {
          "type": "integer",
          "title": "Netconn Count",
          "order": 26
        },
        "segment_id": {
          "type": "integer",
          "title": "Segment ID",
          "order": 27
        },
        "host_type": {
          "type": "string",
          "title": "Host Type",
          "order": 28
        },
        "processblock_count": {
          "type": "integer",
          "title": "Process Block Count",
          "order": 29
        },
        "filemod_complete": {
          "type": "array",
          "title": "Filemod Complete",
          "items": {
            "type": "string"
          },
          "order": 30
        },
        "os_type": {
          "type": "string",
          "title": "OS Type",
          "order": 31
        },
        "binaries": {
          "type": "object",
          "title": "Binaries",
          "order": 32
        },
        "childproc_count": {
          "type": "integer",
          "title": "Childproc Count",
          "order": 33
        },
        "unique_id": {
          "type": "string",
          "title": "Unique ID",
          "order": 34
        }
      }
    }
  }
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
