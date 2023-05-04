import insightconnect_plugin_runtime
from .schema import CreateUserInput, CreateUserOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_zoom.util.util import UserType
from icon_zoom.util.api import AuthenticationRetryLimitError, AuthenticationError


class CreateUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="create_user",
            description=Component.DESCRIPTION,
            input=CreateUserInput(),
            output=CreateUserOutput(),
        )

    def run(self, params={}):
        payload = {
            "action": params.get(Input.ACTION),
            "user_info": {
                "email": params.get(Input.EMAIL),
                "type": UserType.value_of(params.get(Input.TYPE)),
                "first_name": params.get(Input.FIRST_NAME),
                "last_name": params.get(Input.LAST_NAME),
            },
        }
        try:
            self.connection.zoom_api.authenticate()
            user = self.connection.zoom_api.create_user(payload)
        except AuthenticationRetryLimitError:
            raise PluginException(
                cause="OAuth authentication retry limit was met.",
                assistance="Ensure your OAuth connection credentials are valid. "
                           "If running a large number of integrations with Zoom, consider "
                           "increasing the OAuth authentication retry limit to accommodate.",
            )
        except AuthenticationError:
            raise PluginException(
                cause="The OAuth token credentials or JWT token provided in the connection configuration is invalid.",
                assistance="Please verify the credentials are correct and try again."
            )

        return user
