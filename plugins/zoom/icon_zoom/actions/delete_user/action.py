import insightconnect_plugin_runtime
from .schema import DeleteUserInput, DeleteUserOutput, Input, Output, Component

# Custom imports below
from icon_zoom.util.api import AuthenticationRetryLimitError, AuthenticationError
from icon_zoom.util.util import oauth_retry_limit_exception, authentication_error_exception
from insightconnect_plugin_runtime.exceptions import PluginException


class DeleteUser(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_user",
            description=Component.DESCRIPTION,
            input=DeleteUserInput(),
            output=DeleteUserOutput(),
        )

    def run(self, params={}):
        query_params = {
            "action": params.get(Input.ACTION),
            "transfer_email": params.get(Input.TRANSFER_EMAIL),
            "transfer_webinar": params.get(Input.TRANSFER_WEBINARS),
            "transfer_recording": params.get(Input.TRANSFER_RECORDINGS),
            "transfer_meeting": params.get(Input.TRANSFER_MEETINGS),
        }
        try:
            self.connection.zoom_api.authenticate()
            self.connection.zoom_api.delete_user(params.get(Input.ID), query_params)
        except AuthenticationRetryLimitError:
            raise oauth_retry_limit_exception
        except AuthenticationError:
            raise authentication_error_exception

        return {Output.SUCCESS: True}
