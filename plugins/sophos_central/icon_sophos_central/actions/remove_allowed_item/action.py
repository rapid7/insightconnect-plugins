import insightconnect_plugin_runtime
from .schema import RemoveAllowedItemInput, RemoveAllowedItemOutput, Input, Output, Component

# Custom imports below


class RemoveAllowedItem(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_allowed_item",
            description=Component.DESCRIPTION,
            input=RemoveAllowedItemInput(),
            output=RemoveAllowedItemOutput(),
        )

    def run(self, params={}):
        return {
            Output.SUCCESS: self.connection.client.remove_allowed_item(params.get(Input.ALLOWEDITEMID)).get("deleted")
        }
