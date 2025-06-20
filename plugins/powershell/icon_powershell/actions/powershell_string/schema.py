# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Execute PowerShell script in the form of a string"


class Input:
    ADDRESS = "address"
    HOST_NAME = "host_name"
    SCRIPT = "script"


class Output:
    STDERR = "stderr"
    STDOUT = "stdout"


class PowershellStringInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "address": {
      "type": "string",
      "title": "Address",
      "description": "IP address of the remote host e.g. 192.168.1.1. If address is left blank PowerShell will run locally",
      "order": 2
    },
    "host_name": {
      "type": "string",
      "title": "Host Name",
      "description": "Case-sensitive name of the remote host, eg. MyComputer for Kerberos connection only",
      "order": 3
    },
    "script": {
      "type": "string",
      "title": "Script",
      "description": "PowerShell script as a string. In this action you can use `$username`, `$password`, `$secret_key` variables if defined in connection",
      "order": 1
    }
  },
  "required": [
    "script"
  ],
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class PowershellStringOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(
        r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "stderr": {
      "type": "string",
      "title": "PowerShell Standard Error",
      "description": "PowerShell standard error",
      "order": 2
    },
    "stdout": {
      "type": "string",
      "title": "PowerShell Standard Output",
      "description": "PowerShell standard output",
      "order": 1
    }
  },
  "definitions": {}
}
    """
    )

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
