import insightconnect_plugin_runtime
from .schema import RemediateItemsInput, RemediateItemsOutput, Input, Output, Component
# Custom imports below


class RemediateItems(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remediate_items',
                description=Component.DESCRIPTION,
                input=RemediateItemsInput(),
                output=RemediateItemsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
