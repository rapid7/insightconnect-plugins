import insightconnect_plugin_runtime
from .schema import CreateUserInput, CreateUserOutput

# Custom imports below
from komand_rapid7_insightvm.util import endpoints
from komand_rapid7_insightvm.util.resource_requests import ResourceRequests
from komand_rapid7_insightvm.util.resource_helpers import ValidateUser


class CreateUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_user",
            description="Create a new user account (limited to external authentication sources)",
            input=CreateUserInput(),
            output=CreateUserOutput(),
        )

    def run(self, params={}):
        resource_helper = ResourceRequests(self.connection.session, self.logger)
        validate = ValidateUser(self.connection.session, self.logger)
        endpoint = endpoints.User.users(self.connection.console_url)
        self.logger.info(f"Using {endpoint}")

        # Set dict params and delete the original keys
        payload = params
        payload["authentication"] = {"type": payload.get("authentication_type")}

        # Handle default value which is invalid
        if payload.get("authentication_id") != 0:
            payload["authentication"]["id"] = payload.get("authentication_id")

        payload["role"] = {
            "allAssetGroups": payload.get("access_all_asset_groups"),
            "allSites": payload.get("access_all_sites"),
            "id": payload.get("role_id"),
            "superuser": payload.get("superuser"),
        }
        delete_keys = [
            "authentication_id",
            "authentication_type",
            "access_all_asset_groups",
            "access_all_sites",
            "role_id",
            "superuser",
        ]
        for k in list(payload.keys()):
            if k in delete_keys:
                del payload[k]

        # Validate/fix the user configuration
        payload = validate.validate_user(self.connection.console_url, payload)

        response = resource_helper.resource_request(endpoint=endpoint, method="post", payload=payload)

        return response
