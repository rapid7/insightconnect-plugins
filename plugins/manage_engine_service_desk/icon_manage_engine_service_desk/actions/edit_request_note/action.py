import insightconnect_plugin_runtime

from icon_manage_engine_service_desk.util.constants import Response, ResponseStatus
from .schema import EditRequestNoteInput, EditRequestNoteOutput, Input, Output, Component


# Custom imports below


class EditRequestNote(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="edit_request_note",
            description=Component.DESCRIPTION,
            input=EditRequestNoteInput(),
            output=EditRequestNoteOutput(),
        )

    def run(self, params: dict = None) -> dict:
        request_id = params.get(Input.REQUEST_ID)
        response_json = self.connection.api_client.edit_request_note(
            request_id=request_id,
            request_note_id=params.get(Input.REQUEST_NOTE_ID),
            description=params.get(Input.DESCRIPTION),
            show_to_requester=params.get(Input.SHOW_TO_REQUESTER),
            notify_technician=params.get(Input.NOTIFY_TECHNICIAN),
            mark_first_response=params.get(Input.MARK_FIRST_RESPONSE),
            add_to_linked_requests=params.get(Input.ADD_TO_LINKED_REQUEST),
        )

        return {
            Output.REQUEST_ID: request_id,
            Output.STATUS: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS),
            Output.STATUS_CODE: response_json.get(Response.RESPONSE_STATUS, {}).get(ResponseStatus.STATUS_CODE),
        }
