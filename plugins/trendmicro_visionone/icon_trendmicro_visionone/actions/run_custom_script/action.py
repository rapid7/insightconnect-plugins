import insightconnect_plugin_runtime
from .schema import RunCustomScriptInput, RunCustomScriptOutput, Input, Output, Component
# Custom imports below


class RunCustomScript(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='run_custom_script',
                description=Component.DESCRIPTION,
                input=RunCustomScriptInput(),
                output=RunCustomScriptOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
