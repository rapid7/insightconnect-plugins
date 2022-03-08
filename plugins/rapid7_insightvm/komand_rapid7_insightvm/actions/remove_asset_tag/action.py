import insightconnect_plugin_runtime
from .schema import RemoveAssetTagInput, RemoveAssetTagOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class RemoveAssetTag(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_asset_tag",
            description="Remove a tag from an asset",
            input=RemoveAssetTagInput(),
            output=RemoveAssetTagOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        tag_id = params.get("tag_id")
        asset_id = params.get("asset_id")
        endpoint = endpoints.Asset.asset_tags(self.connection.console_url, asset_id, tag_id)
        self.logger.info("Using %s ..." % endpoint)

        response = resource_helper.resource_request(endpoint=endpoint, method="delete")

        return response
