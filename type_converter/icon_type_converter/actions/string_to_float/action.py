import insightconnect_plugin_runtime
from .schema import StringToFloatInput, StringToFloatOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class StringToFloat(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='string_to_float',
            description=Component.DESCRIPTION,
            input=StringToFloatInput(),
            output=StringToFloatOutput())

    def run(self, params={}):
        try:
            return {
                Output.OUTPUT: float(params.get(Input.INPUT))
            }
        except Exception as e:
            raise PluginException(
                cause="Converting error.",
                assistance="Check input",
                data=e
            )
