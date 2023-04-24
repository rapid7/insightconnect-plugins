import insightconnect_plugin_runtime
from .schema import AddAllowedItemInput, AddAllowedItemOutput, Input, Output, Component

# Custom imports below

from icon_sophos_central.util.helpers import clean


class AddAllowedItem(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_allowed_item",
            description=Component.DESCRIPTION,
            input=AddAllowedItemInput(),
            output=AddAllowedItemOutput(),
        )

    def run(self, params={}):
        json_data = {
            "type": params.get(Input.TYPE),
            "properties": {
                "fileName": params.get(Input.PROPERTIESFILENAME),
                "path": params.get(Input.PROPERTIESPATH),
                "sha256": params.get(Input.PROPERTIESSHA256),
                "certificateSigner": params.get(Input.PROPERTIESCERTIFICATESIGNER),
            },
            "comment": params.get(Input.COMMENT),
            "originPersonId": params.get(Input.ORIGINPERSONID),
            "originEndpointId": params.get(Input.ORIGINENDPOINTID),
        }

        return {Output.ALLOWEDITEM: self.connection.client.add_allowed_item(clean(json_data))}
