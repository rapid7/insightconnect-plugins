import insightconnect_plugin_runtime
from .schema import DeleteAssetInput, DeleteAssetOutput, Input, Output, Component

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class DeleteAsset(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_asset",
            description=Component.DESCRIPTION,
            input=DeleteAssetInput(),
            output=DeleteAssetOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)

        asset_id = params.get(Input.ID)
        endpoint = endpoints.Asset.assets(self.connection.console_url, asset_id)
        self.logger.info("Using %s ..." % endpoint)

        resource_helper.resource_request(endpoint, method="delete")

        return {Output.SUCCESS: True}
