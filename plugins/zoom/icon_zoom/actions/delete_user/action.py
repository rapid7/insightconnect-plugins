import insightconnect_plugin_runtime
from .schema import DeleteUserInput, DeleteUserOutput, Input, Output, Component

# Custom imports below
from icon_zoom.util.api import AuthenticationRetryLimitError, AuthenticationError
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

        return {Output.SUCCESS: True}
