import insightconnect_plugin_runtime
from .schema import CreateUserInput, CreateUserOutput, Input, Output, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_zoom.util.util import UserType, oauth_retry_limit_exception, authentication_error_exception
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
            raise oauth_retry_limit_exception
        except AuthenticationError:
            raise authentication_error_exception

        return user
