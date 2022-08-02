import insightconnect_plugin_runtime
from .schema import IntegerToBooleanInput, IntegerToBooleanOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class IntegerToBoolean(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="integer_to_boolean",
            description=Component.DESCRIPTION,
            input=IntegerToBooleanInput(),
            output=IntegerToBooleanOutput(),
        )

    def run(self, params={}):
        value = params.get(Input.INPUT)
        if value == 0:
            return {Output.OUTPUT: False}
        elif value == 1:
            return {Output.OUTPUT: True}
        else:
            raise PluginException(cause="Invalid input", assistance="Value must be 0 or 1")
        # try:
        #     return {Output.OUTPUT: params.get(Input.INPUT) != 0}
        # except Exception as error:
        #     raise PluginException(cause="Converting error.", assistance="Check input", data=error)
