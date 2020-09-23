import insightconnect_plugin_runtime
from .schema import StringToIntegerInput, StringToIntegerOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import re


class StringToInteger(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='string_to_integer',
            description=Component.DESCRIPTION,
            input=StringToIntegerInput(),
            output=StringToIntegerOutput())

    def run(self, params={}):
        if not params.get(Input.STRIP, True) and not re.match(r'^\d+', params.get(Input.INPUT)):
            raise PluginException(
                cause="Converting error",
                assistance="When strip is enabled only number is allowed"
            )
        try:
            return {
                Output.OUTPUT: int(params.get(Input.INPUT))
            }
        except Exception as e:
            raise PluginException(
                cause="Converting error.",
                assistance="Check input",
                data=e
            )
