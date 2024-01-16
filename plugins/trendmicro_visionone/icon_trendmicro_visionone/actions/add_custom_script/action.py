import insightconnect_plugin_runtime
from .schema import AddCustomScriptInput, AddCustomScriptOutput, Input, Output, Component
# Custom imports below


class AddCustomScript(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_custom_script',
                description=Component.DESCRIPTION,
                input=AddCustomScriptInput(),
                output=AddCustomScriptOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
