import insightconnect_plugin_runtime
from .schema import AddUserAssetGroupAccessInput, AddUserAssetGroupAccessOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests


class AddUserAssetGroupAccess(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_user_asset_group_access",
            description="Grant a user account access to an asset group by ID",
            input=AddUserAssetGroupAccessInput(),
            output=AddUserAssetGroupAccessOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        endpoint = endpoints.User.user_asset_groups(
            self.connection.console_url, params.get("user_id"), params.get("asset_group_id")
        )
        self.logger.info(f"Using {endpoint}")

        response = resource_helper.resource_request(endpoint=endpoint, method="put")

        return response
