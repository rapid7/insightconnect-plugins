import insightconnect_plugin_runtime
from .schema import DeleteAssetGroupInput, DeleteAssetGroupOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class DeleteAssetGroup(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_asset_group",
            description="Delete an existing asset group",
            input=DeleteAssetGroupInput(),
            output=DeleteAssetGroupOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        tag_id = params.get("id")
        self.logger.info("Deleting asset group ID %d" % tag_id)
        endpoint = endpoints.AssetGroup.asset_groups(self.connection.console_url, tag_id)

        response = resource_helper.resource_request(endpoint=endpoint, method="delete")

        return response
