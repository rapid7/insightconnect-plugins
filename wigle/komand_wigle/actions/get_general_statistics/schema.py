# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Get a named map of general statistics"


class Input:
    pass

class Output:
    STATISTICS = "statistics"
    

class GetGeneralStatisticsInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetGeneralStatisticsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "statistics": {
      "type": "object",
      "title": "Statistics",
      "description": "Statistics",
      "order": 1
    }
  },
  "required": [
    "statistics"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
