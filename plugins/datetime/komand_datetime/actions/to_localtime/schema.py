# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Convert time from UTC to localtime"


class Input:
    BASE_TIME = "base_time"
    TIMEZONE = "timezone"


class Output:
    CONVERTED_DATE = "converted_date"


class ToLocaltimeInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "base_time": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "Base Time",
      "description": "Datetime to convert, eg. 22 Jul 2020 21:20:33. Milliseconds is not supported",
      "order": 1
    },
    "timezone": {
      "type": "string",
      "title": "Timezone",
      "description": "Timezone to convert from UTC to localtime",
      "order": 2
    }
  },
  "required": [
    "base_time",
    "timezone"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ToLocaltimeOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "converted_date": {
      "type": "string",
      "format": "date-time",
      "displayType": "date",
      "title": "Converted Date",
      "description": "Date in localtime",
      "order": 1
    }
  },
  "required": [
    "converted_date"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
