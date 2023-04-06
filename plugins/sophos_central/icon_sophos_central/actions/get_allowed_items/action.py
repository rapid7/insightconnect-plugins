import insightconnect_plugin_runtime
from .schema import GetAllowedItemsInput, GetAllowedItemsOutput, Input, Output, Component

# Custom imports below
from icon_sophos_central.util.helpers import clean


class GetAllowedItems(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_allowed_items",
            description=Component.DESCRIPTION,
            input=GetAllowedItemsInput(),
            output=GetAllowedItemsOutput(),
        )

    def run(self, params={}):
        params = {
            "page": params.get(Input.PAGE),
            "pageSize": params.get(Input.PAGESIZE),
            "pageTotal": params.get(Input.PAGETOTAL),
        }

        output = self.connection.client.get_allowed_items(params=clean(params))

        return clean({Output.ITEMS: output.get("items", []), Output.PAGES: output.get("pages", {})})
