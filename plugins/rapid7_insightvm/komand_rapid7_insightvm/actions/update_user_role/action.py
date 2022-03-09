import insightconnect_plugin_runtime
from .schema import UpdateUserRoleInput, UpdateUserRoleOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests
from komand_rapid7_insightvm.util.resource_helpers import ValidateUser


class UpdateUserRole(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="update_user_role",
            description="Update the role associated with a user account",
            input=UpdateUserRoleInput(),
            output=UpdateUserRoleOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        validate = ValidateUser(self.connection.session, self.logger)
        endpoint = endpoints.User.users(self.connection.console_url, params.get("user_id"))
        self.logger.info(f"Using {endpoint}")

        # Get the existing details so the specific role ID key can be modified
        payload = resource_helper.resource_request(endpoint=endpoint)

        # Delete keys not required for user update
        del payload["links"]
        del payload["role"]["name"]
        del payload["role"]["privileges"]

        # Set role and permissions
        payload["role"]["id"] = params.get("role_id")
        payload["role"]["allAssetGroups"] = params.get("access_all_asset_groups")
        payload["role"]["allSites"] = params.get("access_all_sites")

        # Validate/fix the user configuration
        payload = validate.validate_user(self.connection.console_url, payload)

        # Modify the role if validated
        response = resource_helper.resource_request(endpoint=endpoint, method="put", payload=payload)

        return response
