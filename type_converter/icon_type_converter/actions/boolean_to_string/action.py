import insightconnect_plugin_runtime
from .schema import BooleanToStringInput, BooleanToStringOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class BooleanToString(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='boolean_to_string',
            description=Component.DESCRIPTION,
            input=BooleanToStringInput(),
            output=BooleanToStringOutput())

    def run(self, params={}):
        try:
            return {
                Output.OUTPUT: str(params.get(Input.INPUT)).lower()
            }
        except Exception as e:
            raise PluginException(
                cause="Converting error.",
                assistance="Check input",
                data=e
            )
