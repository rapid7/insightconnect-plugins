import insightconnect_plugin_runtime
from .schema import AddUserInput, AddUserOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
import validators


class AddUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="add_user", description=Component.DESCRIPTION, input=AddUserInput(), output=AddUserOutput()
        )

    def run(self, params={}):
        parameters = {
            "invite_user_email": params.get(Input.INVITE_USER_EMAIL),
            "all_cloud_accounts": params.get(Input.ALL_CLOUD_ACCOUNTS),
            "cloud_accounts": params.get(Input.CLOUD_ACCOUNTS),
            "should_send_email": params.get(Input.SHOULD_SEND_EMAIL),
        }
        role = params.get(Input.ROLE)

        if validators.uuid(role):
            if self.connection.api.get_role_by_id(role).get("data"):
                parameters["role_id"] = role
        else:
            roles = self.connection.api.get_roles({"search": role}).get("data")
            parameters["role_id"] = self.get_role_id(role, roles)

        return {Output.STATUS: self.connection.api.add_user(parameters).get("status")}

    @staticmethod
    def get_role_id(role_name: str, roles: list) -> str:
        for role in roles:
            if role_name.lower() == role.get("name").lower():
                role_id = role.get("id")
                if role_id:
                    return role_id
        raise PluginException(
            cause=f"Role {role_name} not found.", assistance="Please check that provided role is correct and try again."
        )
