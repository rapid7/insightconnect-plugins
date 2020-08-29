import insightconnect_plugin_runtime
from .schema import TrimInput, TrimOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class Trim(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='trim',
                description=Component.DESCRIPTION,
                input=TrimInput(),
                output=TrimOutput())

    def run(self, params={}):
        string = params.get(Input.STRING)
        return {Output.TRIMMED: string.strip()}
