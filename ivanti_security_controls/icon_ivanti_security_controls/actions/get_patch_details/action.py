import insightconnect_plugin_runtime
from .schema import GetPatchDetailsInput, GetPatchDetailsOutput, Input, Output, Component
# Custom imports below


class GetPatchDetails(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_patch_details',
                description=Component.DESCRIPTION,
                input=GetPatchDetailsInput(),
                output=GetPatchDetailsOutput())

    def run(self, params={}):
        patch = self.connection.ivanti_api.get_patch_details(params.get(Input.ID))
        
        return {
            Output.PATCH: patch
        }
