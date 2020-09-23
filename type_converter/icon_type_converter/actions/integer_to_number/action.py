import insightconnect_plugin_runtime
from .schema import IntegerToNumberInput, IntegerToNumberOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class IntegerToNumber(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='integer_to_number',
            description=Component.DESCRIPTION,
            input=IntegerToNumberInput(),
            output=IntegerToNumberOutput())

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
