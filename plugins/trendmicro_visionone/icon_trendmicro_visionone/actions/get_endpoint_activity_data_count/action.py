import insightconnect_plugin_runtime
from .schema import GetEndpointActivityDataCountInput, GetEndpointActivityDataCountOutput, Input, Output, Component
# Custom imports below


class GetEndpointActivityDataCount(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_endpoint_activity_data_count',
                description=Component.DESCRIPTION,
                input=GetEndpointActivityDataCountInput(),
                output=GetEndpointActivityDataCountOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
