import insightconnect_plugin_runtime
from .schema import SearchThreatsInput, SearchThreatsOutput, Input, Output, Component
# Custom imports below


class SearchThreats(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_threats',
                description=Component.DESCRIPTION,
                input=SearchThreatsInput(),
                output=SearchThreatsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
