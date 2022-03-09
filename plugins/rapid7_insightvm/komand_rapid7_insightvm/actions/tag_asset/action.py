import insightconnect_plugin_runtime
from .schema import TagAssetInput, TagAssetOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class TagAsset(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="tag_asset",
            description="Add a tag to an asset",
            input=TagAssetInput(),
            output=TagAssetOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        asset_id = params.get("asset_id")
        tag_id = params.get("tag_id")
        endpoint = endpoints.Asset.asset_tags(self.connection.console_url, asset_id, tag_id)
        self.logger.info(f"Using {endpoint}")

        response = resource_helper.resource_request(endpoint=endpoint, method="put")

        return response
