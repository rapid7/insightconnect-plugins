import insightconnect_plugin_runtime
from .schema import StringToBooleanInput, StringToBooleanOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class StringToBoolean(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='string_to_boolean',
            description=Component.DESCRIPTION,
            input=StringToBooleanInput(),
            output=StringToBooleanOutput())

    def run(self, params={}):
        try:
            return {
                Output.OUTPUT: params.get(Input.INPUT).lower() == "true"
            }
        except Exception as e:
            raise PluginException(
                cause="Converting error.",
                assistance="Check input",
                data=e
            )
