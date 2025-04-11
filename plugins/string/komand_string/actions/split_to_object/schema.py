# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "This action is used to convert a string to an object containing key:value strings.Any input requiring more than a single key:value pair, e.g. `USER=Bob` needs to use the `block_delimiter` option. In this case, the input string is split by the `block_delimiter` character first, and the resulting items are then split by the `string_delimiter` option. Stripping of double-quotes is automatically applied in this situation for each item before the plugin returns it.The [output object](https://docs.komand.com/v0.42.1/docs/python-script-plugins#section-configure-the-plugin-output-schema) on the action's page can be modified to pre-populate the workflow with the names of the keys. It allows users the ability to use the green selector and choose a specific variable later in the workflow by name. [Input templating](https://docs.komand.com/docs/input-templating) would need to be used to obtain variables by name otherwise.Please refer to troubleshooting section for a more complex example"


class Input:
    BLOCK_DELIMITER = "block_delimiter"
    STRING = "string"
    STRING_DELIMITER = "string_delimiter"


class Output:
    OBJECT = "object"


class SplitToObjectInput(insightconnect_plugin_runtime.Input):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "block_delimiter": {
      "type": "string",
      "title": "Block Delimiter",
      "description": "The character delimiter for the initial string split, applied before the string delimiter input. This parameter is optional but allows for more complex handling",
      "order": 3
    },
    "string": {
      "type": "string",
      "title": "String Input",
      "description": "String to convert e.g. USER=Bob",
      "order": 1
    },
    "string_delimiter": {
      "type": "string",
      "title": "String Delimiter",
      "description": "The character used to split the string into slices for the list. The default is a space, if not provided by the user",
      "order": 2
    }
  },
  "required": [
    "string"
  ],
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SplitToObjectOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads(r"""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "object": {
      "type": "object",
      "title": "Object",
      "description": "Object from string split",
      "order": 1
    }
  },
  "definitions": {}
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
