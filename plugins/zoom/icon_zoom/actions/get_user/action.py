import insightconnect_plugin_runtime
from .schema import GetUserInput, GetUserOutput, Input, Output, Component

# Custom imports below
from icon_zoom.util.util import oauth_retry_limit_exception, authentication_error_exception
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
            raise oauth_retry_limit_exception
        except AuthenticationError:
            raise authentication_error_exception

        return {Output.USER: user}
