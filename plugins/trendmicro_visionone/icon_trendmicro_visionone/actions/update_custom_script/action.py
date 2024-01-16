import insightconnect_plugin_runtime
from .schema import UpdateCustomScriptInput, UpdateCustomScriptOutput, Input, Output, Component
# Custom imports below


class UpdateCustomScript(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_custom_script',
                description=Component.DESCRIPTION,
                input=UpdateCustomScriptInput(),
                output=UpdateCustomScriptOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
