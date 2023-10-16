import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import GetUserByIdInput, GetUserByIdOutput

# Custom imports below
from komand_pagerduty.util.util import empty_user, normalize_user


class GetUserById(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user_by_id",
            description="Get a User By ID",
            input=GetUserByIdInput(),
            output=GetUserByIdOutput(),
        )

    def run(self, params={}):
        """Get a user by ID"""

        # required
        user_id = params.get("id")

        if id is None:
            self.logger.warning("Please ensure a valid 'id' is provided")
            raise PluginException(
                cause="Missing required paramaters",
                assistance="Please ensure a valid 'id' is provided",
            )

        response = self.connection.api.get_user_by_id(user_id=user_id)

        if response.get("user"):
            normalized_user = normalize_user(response.get("user"))
            return {"user": normalized_user}
