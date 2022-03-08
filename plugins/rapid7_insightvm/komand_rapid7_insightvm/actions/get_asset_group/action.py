import insightconnect_plugin_runtime
from .schema import GetAssetGroupInput, GetAssetGroupOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetAssetGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_asset_group",
            description="Get an asset group by ID",
            input=GetAssetGroupInput(),
            output=GetAssetGroupOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        asset_group_id = params.get("id")
        endpoint = endpoints.AssetGroup.asset_groups(self.connection.console_url, asset_group_id)
        self.logger.info("Using %s ..." % endpoint)
        asset_group = resource_helper.resource_request(endpoint)

        return {"asset_group": asset_group}
