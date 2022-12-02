import insightconnect_plugin_runtime
from .schema import GetResourceDetailsInput, GetResourceDetailsOutput, Input, Output, Component

# Custom imports below


class GetResourceDetails(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_resource_details",
            description=Component.DESCRIPTION,
            input=GetResourceDetailsInput(),
            output=GetResourceDetailsOutput(),
        )

    def run(self, params={}):
        return {Output.RESOURCEDETAILS: self.connection.api.get_resource_details(params.get(Input.RESOURCEID))}
