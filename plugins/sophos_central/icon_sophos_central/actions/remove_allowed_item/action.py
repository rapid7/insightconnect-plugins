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
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        allowed_item_id = params.get(Input.ALLOWEDITEMID)
        # END INPUT BINDING - DO NOT REMOVE

        return {Output.SUCCESS: self.connection.client.remove_allowed_item(allowed_item_id).get("deleted")}
