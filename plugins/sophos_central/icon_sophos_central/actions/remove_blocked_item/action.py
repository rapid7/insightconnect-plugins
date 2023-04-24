import insightconnect_plugin_runtime
from .schema import RemoveBlockedItemInput, RemoveBlockedItemOutput, Input, Output, Component

# Custom imports below


class RemoveBlockedItem(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_blocked_item",
            description=Component.DESCRIPTION,
            input=RemoveBlockedItemInput(),
            output=RemoveBlockedItemOutput(),
        )

    def run(self, params={}):
        item_id = params.get(Input.BLOCKEDITEMID)
        self.logger.info(f"Removing blocked item with ID: {item_id}.")
        return {Output.SUCCESS: self.connection.client.remove_blocked_item(item_id)}
