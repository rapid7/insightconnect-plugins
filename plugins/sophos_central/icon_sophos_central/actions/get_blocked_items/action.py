import insightconnect_plugin_runtime
from .schema import GetBlockedItemsInput, GetBlockedItemsOutput, Input, Output, Component

# Custom imports below
from icon_sophos_central.util.helpers import clean


class GetBlockedItems(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_blocked_items",
            description=Component.DESCRIPTION,
            input=GetBlockedItemsInput(),
            output=GetBlockedItemsOutput(),
        )

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        page = params.get(Input.PAGE)
        page_size = params.get(Input.PAGESIZE)
        page_total = params.get(Input.PAGETOTAL)
        # END INPUT BINDING - DO NOT REMOVE

        self.logger.info("Getting list of blocked items...")

        parameters = {
            "page": page,
            "pageSize": page_size,
            "pageTotal": page_total,
        }

        result = self.connection.client.get_blocked_items(clean(parameters))

        return {
            Output.ITEMS: result.get("items", []),
            Output.PAGES: result.get("pages", {}),
        }
