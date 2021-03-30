import insightconnect_plugin_runtime
from .schema import GetQueryStatusInput, GetQueryStatusOutput, Input, Output, Component
# Custom imports below


class GetQueryStatus(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_query_status',
                description=Component.DESCRIPTION,
                input=GetQueryStatusInput(),
                output=GetQueryStatusOutput())

    def run(self, params={}):
        return {Output.RESPONSE: self.connection.get_query_status(params.get(Input.QUERY_ID))}
