import insightconnect_plugin_runtime
from .schema import NumberToIntegerInput, NumberToIntegerOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class NumberToInteger(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='number_to_integer',
            description=Component.DESCRIPTION,
            input=NumberToIntegerInput(),
            output=NumberToIntegerOutput())

    def run(self, params={}):
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
