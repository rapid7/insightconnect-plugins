import insightconnect_plugin_runtime
from .schema import RemediateItemsInput, RemediateItemsOutput, Input, Output, Component

# Custom imports below


class RemediateItems(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remediate_items",
            description=Component.DESCRIPTION,
            input=RemediateItemsInput(),
            output=RemediateItemsOutput(),
        )

    def run(self, params={}):
        return {
            Output.RESPONSE: self.connection.api.remediate(
                params.get(Input.INITIATOR_USER_NAME),
                params.get(Input.ACTIONS_BY_MACHINE),
                malop_id=params.get(Input.MALOP_ID, None),
            )
        }
