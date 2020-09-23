import insightconnect_plugin_runtime
from .schema import BooleanToIntegerInput, BooleanToIntegerOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class BooleanToInteger(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='boolean_to_integer',
            description=Component.DESCRIPTION,
            input=BooleanToIntegerInput(),
            output=BooleanToIntegerOutput())

    def run(self, params={}):
        try:
            return {
                Output.OUTPUT: int(params.get(Input.INPUT) is True)
            }
        except Exception as e:
            raise PluginException(
                cause="Converting error.",
                assistance="Check input",
                data=e
            )
