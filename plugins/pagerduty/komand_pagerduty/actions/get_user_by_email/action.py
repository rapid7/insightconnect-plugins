import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from .schema import GetUserByEmailInput, GetUserByEmailOutput, Input, Output, Component

# Custom imports below
from komand_pagerduty.util.util import normalize_user


class GetUserByEmail(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user_by_email",
            description=Component.DESCRIPTION,
            input=GetUserByEmailInput(),
            output=GetUserByEmailOutput(),
        )

    def run(self, params={}):
        user_email = params.get(Input.USER_EMAIL)

        response = self.connection.api.get_user_by_email(user_email=user_email)

        for user in response.get("users", []):
            if user.get("email", "") == user_email:
                normalized_user = normalize_user(user)
                return {Output.USER: normalized_user}

        raise PluginException(cause=f"No user found for email {user_email}")
