import insightconnect_plugin_runtime
from .schema import ObjectToStringInput, ObjectToStringOutput, Input, Output, Component
# Custom imports below
import json
from insightconnect_plugin_runtime.exceptions import PluginException


class ObjectToString(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='object_to_string',
            description=Component.DESCRIPTION,
            input=ObjectToStringInput(),
            output=ObjectToStringOutput())

    def run(self, params={}):
        try:
            return {
                Output.OUTPUT: json.dumps(params.get(Input.INPUT))
            }
        except Exception as e:
            raise PluginException(
                cause="Converting error.",
                assistance="Check input",
                data=e
            )
