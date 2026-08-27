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
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        page = params.get(Input.PAGE)
        page_size = params.get(Input.PAGESIZE)
        page_total = params.get(Input.PAGETOTAL)
        # END INPUT BINDING - DO NOT REMOVE

        query_params = {
            "page": page,
            "pageSize": page_size,
            "pageTotal": page_total,
        }

        output = self.connection.client.get_allowed_items(params=clean(query_params))

        return clean({Output.ITEMS: output.get("items", []), Output.PAGES: output.get("pages", {})})
