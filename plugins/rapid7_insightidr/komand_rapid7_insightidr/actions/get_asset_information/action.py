import insightconnect_plugin_runtime
from .schema import GetAssetInformationInput, GetAssetInformationOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightidr.util.endpoints import Assets
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper


class GetAssetInformation(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_asset_information",
            description=Component.DESCRIPTION,
            input=GetAssetInformationInput(),
            output=GetAssetInformationOutput(),
        )

    def run(self, params={}):
        asset_rrn = params.get(Input.ASSET_RRN)
        self.connection.headers["Accept-version"] = "strong-force-preview"
        request = ResourceHelper(self.connection.headers, self.logger)
        self.logger.info(f"Getting the asset information for {asset_rrn}...", **self.connection.cloud_log_values)
        response = request.make_request(Assets.get_asset_information(self.connection.url, asset_rrn), "get")
        return {Output.ASSET: response, Output.SUCCESS: True}
