import insightconnect_plugin_runtime
from .schema import UpdateUserAssetGroupAccessInput, UpdateUserAssetGroupAccessOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class UpdateUserAssetGroupAccess(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_user_asset_group_access",
            description="Update the asset groups to which a user has access in bulk. It can be used to remove asset group access as well",
            input=UpdateUserAssetGroupAccessInput(),
            output=UpdateUserAssetGroupAccessOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.User.user_asset_groups(self.connection.console_url, params.get("user_id"))
        payload = params.get("asset_group_ids")
        self.logger.info(f"Using {endpoint}")

        response = resource_helper.resource_request(endpoint=endpoint, method="put", payload=payload)

        return response
