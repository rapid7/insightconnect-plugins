import insightconnect_plugin_runtime
from .schema import ArrayToStringInput, ArrayToStringOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class ArrayToString(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='array_to_string',
            description=Component.DESCRIPTION,
            input=ArrayToStringInput(),
            output=ArrayToStringOutput())

    def run(self, params={}):
        delimiter = params.get(Input.DELIMITER)
        if not delimiter:
            delimiter = " "

        try:
            return {
                Output.OUTPUT: delimiter.join(params.get(Input.INPUT, []))
            }
        except Exception as e:
            raise PluginException(
                cause="Converting error.",
                assistance="Check input",
                data=e
            )
