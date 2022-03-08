import insightconnect_plugin_runtime
from .schema import GetAssetGroupAssetsInput, GetAssetGroupAssetsOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetAssetGroupAssets(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_asset_group_assets",
            description=Component.DESCRIPTION,
            input=GetAssetGroupAssetsInput(),
            output=GetAssetGroupAssetsOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        asset_group_id = params.get(Input.ID)
        endpoint = endpoints.AssetGroup.asset_group_assets(self.connection.console_url, asset_group_id)
        self.logger.info("Using %s ..." % endpoint)
        asset_group_assets = resource_helper.resource_request(endpoint)

        try:
            links = asset_group_assets["links"]
        except KeyError:
            self.logger.info("Warning: No links returned in response. Using empty list.")
            links = list()
        try:
            resources = asset_group_assets["resources"]
        except KeyError:
            self.logger.info("Warning: No resources returned in response. Using empty list.")
            resources = list()

        return {Output.LINKS: links, Output.RESOURCES: resources}
