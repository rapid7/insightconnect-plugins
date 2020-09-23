import insightconnect_plugin_runtime
from .schema import IntegerToBooleanInput, IntegerToBooleanOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class IntegerToBoolean(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='integer_to_boolean',
            description=Component.DESCRIPTION,
            input=IntegerToBooleanInput(),
            output=IntegerToBooleanOutput())

    def run(self, params={}):
        try:
            return {
                Output.OUTPUT: params.get(Input.INPUT) != 0
            }
        except Exception as e:
            raise PluginException(
                cause="Converting error.",
                assistance="Check input",
                data=e
            )
