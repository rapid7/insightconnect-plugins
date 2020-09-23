import insightconnect_plugin_runtime
from .schema import IntegerToStringInput, IntegerToStringOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class IntegerToString(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='integer_to_string',
            description=Component.DESCRIPTION,
            input=IntegerToStringInput(),
            output=IntegerToStringOutput())

    def run(self, params={}):
        try:
            return {
                Output.OUTPUT: str(params.get(Input.INPUT))
            }
        except Exception as e:
            raise PluginException(
                cause="Converting error.",
                assistance="Check input",
                data=e
            )
