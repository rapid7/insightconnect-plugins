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
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        type_ = params.get(Input.TYPE)
        properties_file_name = params.get(Input.PROPERTIESFILENAME)
        properties_path = params.get(Input.PROPERTIESPATH)
        properties_sha256 = params.get(Input.PROPERTIESSHA256)
        properties_certificate_signer = params.get(Input.PROPERTIESCERTIFICATESIGNER)
        comment = params.get(Input.COMMENT)
        origin_person_id = params.get(Input.ORIGINPERSONID)
        origin_endpoint_id = params.get(Input.ORIGINENDPOINTID)
        # END INPUT BINDING - DO NOT REMOVE

        json_data = {
            "type": type_,
            "properties": {
                "fileName": properties_file_name,
                "path": properties_path,
                "sha256": properties_sha256,
                "certificateSigner": properties_certificate_signer,
            },
            "comment": comment,
            "originPersonId": origin_person_id,
            "originEndpointId": origin_endpoint_id,
        }

        return {Output.ALLOWEDITEM: self.connection.client.add_allowed_item(clean(json_data))}
