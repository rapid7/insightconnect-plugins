import insightconnect_plugin_runtime
from .schema import SearchPatchesInput, SearchPatchesOutput, Input, Output, Component
# Custom imports below


class SearchPatches(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_patches',
                description=Component.DESCRIPTION,
                input=SearchPatchesInput(),
                output=SearchPatchesOutput())

    def run(self, params={}):
        return {
            Output.VULNERABILITIES: self.connection.ivanti_api.search_patches(params.get(Input.SECURITY_ID))
        }
