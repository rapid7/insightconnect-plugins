import insightconnect_plugin_runtime
from .schema import GetUserInput, GetUserOutput, Input, Output, Component

# Custom imports below
from icon_zoom.util.api import AuthenticationRetryLimitError, AuthenticationError
from insightconnect_plugin_runtime.exceptions import PluginException


class GetUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_user",
            description=Component.DESCRIPTION,
            input=GetUserInput(),
            output=GetUserOutput(),
        )

    def run(self, params={}):
        try:
            self.connection.zoom_api.authenticate()
            user = self.connection.zoom_api.get_user(params.get(Input.USER_ID))
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

        return {Output.USER: user}
