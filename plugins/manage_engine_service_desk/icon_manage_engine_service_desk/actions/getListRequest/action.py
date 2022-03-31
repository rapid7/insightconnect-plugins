import insightconnect_plugin_runtime
from .schema import GetListRequestInput, GetListRequestOutput, Input, Output, Component
# Custom imports below


class GetListRequest(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='getListRequest',
                description=Component.DESCRIPTION,
                input=GetListRequestInput(),
                output=GetListRequestOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
