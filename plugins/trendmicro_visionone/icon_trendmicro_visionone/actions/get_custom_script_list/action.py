import insightconnect_plugin_runtime
from .schema import GetCustomScriptListInput, GetCustomScriptListOutput, Input, Output, Component
# Custom imports below


class GetCustomScriptList(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_custom_script_list',
                description=Component.DESCRIPTION,
                input=GetCustomScriptListInput(),
                output=GetCustomScriptListOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
