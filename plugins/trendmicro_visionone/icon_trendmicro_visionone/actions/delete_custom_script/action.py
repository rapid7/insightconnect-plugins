import insightconnect_plugin_runtime
from .schema import DeleteCustomScriptInput, DeleteCustomScriptOutput, Input, Output, Component
# Custom imports below


class DeleteCustomScript(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_custom_script',
                description=Component.DESCRIPTION,
                input=DeleteCustomScriptInput(),
                output=DeleteCustomScriptOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
