import komand
from .schema import AdvancedQueryInput, AdvancedQueryOutput, Input, Output, Component
# Custom imports below


class AdvancedQuery(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='advanced_query',
                description=Component.DESCRIPTION,
                input=AdvancedQueryInput(),
                output=AdvancedQueryOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
