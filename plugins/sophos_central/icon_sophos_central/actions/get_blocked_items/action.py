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
        self.logger.info("Getting list of blocked items...")

        parameters = {
            "page": params.get(Input.PAGE),
            "pageSize": params.get(Input.PAGESIZE),
            "pageTotal": params.get(Input.PAGETOTAL),
        }

        result = self.connection.client.get_blocked_items(clean(parameters))

        return {
            Output.ITEMS: result.get("items", []),
            Output.PAGES: result.get("pages", {}),
        }
