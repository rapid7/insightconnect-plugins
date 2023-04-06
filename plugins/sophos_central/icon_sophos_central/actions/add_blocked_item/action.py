import insightconnect_plugin_runtime
from .schema import AddBlockedItemInput, AddBlockedItemOutput, Input, Output, Component

# Custom imports below
from icon_sophos_central.util.helpers import clean


class AddBlockedItem(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_blocked_item",
            description=Component.DESCRIPTION,
            input=AddBlockedItemInput(),
            output=AddBlockedItemOutput(),
        )

    def run(self, params={}):
        self.logger.info("Blocking new item...")
        item_data = {
            "type": params.get(Input.TYPE),
            "properties": {
                "fileName": params.get(Input.PROPERTIESFILENAME),
                "path": params.get(Input.PROPERTIESPATH),
                "sha256": params.get(Input.PROPERTIESSHA256),
                "certificateSigner": params.get(Input.PROPERTIESCERTIFICATESIGNER),
            },
            "comment": params.get(Input.COMMENT),
        }

        return {Output.BLOCKEDITEM: self.connection.client.add_blocked_item(clean(item_data))}
