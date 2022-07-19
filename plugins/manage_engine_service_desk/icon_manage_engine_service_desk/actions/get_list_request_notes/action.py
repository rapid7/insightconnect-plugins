import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.helper import clean

from icon_manage_engine_service_desk.util.constants import Response, Note, ResponseStatus, Time, User
from icon_manage_engine_service_desk.util.helpers import remove_other_keys
from .schema import GetListRequestNotesInput, GetListRequestNotesOutput, Input, Output, Component


# Custom imports below


class GetListRequestNotes(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_list_request_notes",
            description=Component.DESCRIPTION,
            input=GetListRequestNotesInput(),
            output=GetListRequestNotesOutput(),
        )

    def run(self, params: dict = None) -> dict:
        request_id = params.get(Input.REQUEST_ID)
        response_json = self.connection.api_client.get_request_notes(request_id=request_id)
        updated_notes = []
        for note in response_json.get(Response.NOTES, []):
            clean_note = remove_other_keys(note, Note().get_all_attributes())
            clean_note[Note.LAST_UPDATED_BY] = remove_other_keys(note.get(Note.LAST_UPDATED_BY), [User.NAME, User.ID])
            clean_note[Note.ADDED_BY] = remove_other_keys(note.get(Note.ADDED_BY), [User.NAME, User.ID])
            clean_note[Note.LAST_UPDATED_TIME] = clean_note.get(Note.LAST_UPDATED_TIME, {}).get(Time.DISPLAY_VALUE)
            clean_note[Note.ADDED_TIME] = clean_note.get(Note.ADDED_TIME, {}).get(Time.DISPLAY_VALUE)
            updated_notes.append(clean_note)
        return clean(
            {
                Output.REQUEST_ID: request_id,
                Output.NOTES: updated_notes,
                Output.STATUS: response_json.get(Response.RESPONSE_STATUS, [{}])[0].get(ResponseStatus.STATUS),
                Output.STATUS_CODE: response_json.get(Response.RESPONSE_STATUS, [{}])[0].get(
                    ResponseStatus.STATUS_CODE
                ),
            }
        )
