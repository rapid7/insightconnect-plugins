import insightconnect_plugin_runtime
from .schema import RunCommandInput, RunCommandOutput, Input, Output, Component
# Custom imports below


class RunCommand(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='run_command',
                description=Component.DESCRIPTION,
                input=RunCommandInput(),
                output=RunCommandOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
