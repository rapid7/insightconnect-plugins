import insightconnect_plugin_runtime
from .schema import StringToObjectInput, StringToObjectOutput, Input, Output, Component
# Custom imports below
import json
from insightconnect_plugin_runtime.exceptions import PluginException


class StringToObject(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='string_to_object',
            description=Component.DESCRIPTION,
            input=StringToObjectInput(),
            output=StringToObjectOutput())

    def run(self, params={}):
        try:
            return {
                Output.OUTPUT: json.loads(params.get(Input.INPUT))
            }
        except Exception as e:
            raise PluginException(
                cause="Converting error.",
                assistance="Check input",
                data=e
            )
