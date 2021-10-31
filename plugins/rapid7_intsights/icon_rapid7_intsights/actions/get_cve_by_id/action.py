import insightconnect_plugin_runtime
from .schema import GetCveByIdInput, GetCveByIdOutput, Input, Output, Component
# Custom imports below


class GetCveById(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_cve_by_id',
                description=Component.DESCRIPTION,
                input=GetCveByIdInput(),
                output=GetCveByIdOutput())

    def run(self, params={}):
        response = self.connection.client.get_cve(params.get(Input.CVE_ID))
        return {
            Output.CONTENT: response
        }
