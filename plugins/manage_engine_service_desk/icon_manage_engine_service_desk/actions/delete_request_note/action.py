import insightconnect_plugin_runtime

from icon_manage_engine_service_desk.util.constants import Response, ResponseStatus
from .schema import DeleteRequestNoteInput, DeleteRequestNoteOutput, Input, Output, Component


# Custom imports below


class DeleteRequestNote(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="delete_request_note",
            description=Component.DESCRIPTION,
            input=DeleteRequestNoteInput(),
            output=DeleteRequestNoteOutput(),
        )

    def run(self, params: dict = None) -> dict:
        request_id = params.get(Input.REQUEST_ID)
        response_json = self.connection.api_client.delete_request_note(
            request_id=request_id, request_note_id=params.get(Input.REQUEST_NOTE_ID)
        )

        return {
            Output.REQUEST_ID: request_id,
            Output.STATUS: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS),
            Output.STATUS_CODE: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS_CODE),
        }
