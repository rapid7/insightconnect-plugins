import insightconnect_plugin_runtime
from .schema import GetAssetSoftwareInput, GetAssetSoftwareOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class GetAssetSoftware(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_asset_software",
            description=Component.DESCRIPTION,
            input=GetAssetSoftwareInput(),
            output=GetAssetSoftwareOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        asset_id = params.get(Input.ASSET_ID)

        endpoint = endpoints.Asset.asset_software(self.connection.console_url, asset_id)
        self.logger.info(f"Using {endpoint}")

        software = resource_helper.resource_request(endpoint=endpoint)

        return {Output.SOFTWARE: software["resources"]}
