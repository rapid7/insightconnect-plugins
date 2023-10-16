import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import DeleteUserByIdInput, DeleteUserByIdOutput

# Custom imports below
from komand_pagerduty.util.util import normalize_user


class DeleteUserById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_user_by_id",
            description="Delete a User By ID",
            input=DeleteUserByIdInput(),
            output=DeleteUserByIdOutput(),
        )

    def run(self, params={}):
        """Delete user"""

        email = params.get("email")
        user_id = params.get("id")

        if email is None or user_id is None:
            self.logger.warning("Please ensure a valid 'email' and 'id' is provided")
            raise PluginException(
                cause="Missing required paramaters", assistance="Please ensure a valid 'email' and 'id' is provided"
            )

        self.connection.api.delete_user_by_id(email=email, user_id=user_id)

        return f"The user {user_id} has been deleted"
