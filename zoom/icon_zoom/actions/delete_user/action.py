import insightconnect_plugin_runtime
from .schema import DeleteUserInput, DeleteUserOutput, Input, Output, Component
# Custom imports below


class DeleteUser(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_user',
                description=Component.DESCRIPTION,
                input=DeleteUserInput(),
                output=DeleteUserOutput())

    def run(self, params={}):
        query_params = {
            "action": params.get(Input.ACTION),
            "transfer_email": params.get(Input.TRANSFER_EMAIL),
            "transfer_webinar": params.get(Input.TRANSFER_WEBINARS),
            "transfer_recording": params.get(Input.TRANSFER_RECORDINGS),
            "transfer_meeting": params.get(Input.TRANSFER_MEETINGS)
        }
        self.connection.zoom_api.delete_user(params.get(Input.ID), query_params)

        return {Output.SUCCESS: True}
