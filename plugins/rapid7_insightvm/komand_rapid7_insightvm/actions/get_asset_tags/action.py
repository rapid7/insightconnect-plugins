import insightconnect_plugin_runtime
from .schema import GetAssetTagsInput, GetAssetTagsOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetAssetTags(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_asset_tags",
            description=Component.DESCRIPTION,
            input=GetAssetTagsInput(),
            output=GetAssetTagsOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        asset_id = params.get(Input.ASSET_ID)

        endpoint = endpoints.Asset.asset_tags(self.connection.console_url, asset_id)
        self.logger.info(f"Using {endpoint}")

        tags = resource_helper.resource_request(endpoint=endpoint)

        return {Output.TAGS: tags["resources"]}
