import insightconnect_plugin_runtime
from .schema import GetAssetInput, GetAssetOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetAsset(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_asset",
            description=Component.DESCRIPTION,
            input=GetAssetInput(),
            output=GetAssetOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        asset_id = params.get(Input.ID)
        endpoint = endpoints.Asset.assets(self.connection.console_url, asset_id)
        self.logger.info("Using %s ..." % endpoint)
        asset = resource_helper.resource_request(endpoint)

        return {Output.ASSET: asset}
