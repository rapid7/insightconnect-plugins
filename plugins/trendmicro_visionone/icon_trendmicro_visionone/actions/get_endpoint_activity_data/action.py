import insightconnect_plugin_runtime
from .schema import GetEndpointActivityDataInput, GetEndpointActivityDataOutput, Input, Output, Component
# Custom imports below


class GetEndpointActivityData(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_endpoint_activity_data',
                description=Component.DESCRIPTION,
                input=GetEndpointActivityDataInput(),
                output=GetEndpointActivityDataOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
