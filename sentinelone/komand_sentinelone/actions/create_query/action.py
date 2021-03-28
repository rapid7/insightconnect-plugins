import insightconnect_plugin_runtime
from .schema import CreateQueryInput, CreateQueryOutput, Input, Output, Component
# Custom imports below


class CreateQuery(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_query',
                description=Component.DESCRIPTION,
                input=CreateQueryInput(),
                output=CreateQueryOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
