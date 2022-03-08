import insightconnect_plugin_runtime
from .schema import RemoveAssetGroupTagsInput, RemoveAssetGroupTagsOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class RemoveAssetGroupTags(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="remove_asset_group_tags",
            description="Removes all tags from an asset group",
            input=RemoveAssetGroupTagsInput(),
            output=RemoveAssetGroupTagsOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        asset_group_id = params.get("id")
        endpoint = endpoints.AssetGroup.asset_group_tags(self.connection.console_url, asset_group_id)
        self.logger.info("Using %s ..." % endpoint)

        response = resource_helper.resource_request(endpoint=endpoint, method="delete")

        return response
