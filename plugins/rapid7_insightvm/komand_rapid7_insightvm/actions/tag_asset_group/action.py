import insightconnect_plugin_runtime
from .schema import TagAssetGroupInput, TagAssetGroupOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class TagAssetGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="tag_asset_group",
            description="Add a tag to an asset group",
            input=TagAssetGroupInput(),
            output=TagAssetGroupOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        asset_group_id = params.get("asset_group_id")
        tag_id = params.get("tag_id")
        endpoint = endpoints.AssetGroup.asset_group_tags(self.connection.console_url, asset_group_id, tag_id)
        self.logger.info("Using %s ..." % endpoint)

        response = resource_helper.resource_request(endpoint=endpoint, method="put")

        return response
