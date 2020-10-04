import insightconnect_plugin_runtime
from .schema import StringToListInput, StringToListOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class StringToList(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='string_to_list',
            description=Component.DESCRIPTION,
            input=StringToListInput(),
            output=StringToListOutput())

    def run(self, params={}):
        delimiter = params.get(Input.DELIMITER)
        if not delimiter:
            delimiter = "\n"

        try:
            return {
                Output.OUTPUT: params.get(Input.INPUT).split(delimiter)
            }
        except Exception as e:
            raise PluginException(
                cause="Converting error.",
                assistance="Check input",
                data=e
            )
