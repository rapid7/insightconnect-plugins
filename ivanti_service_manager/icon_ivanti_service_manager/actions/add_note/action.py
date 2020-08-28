import insightconnect_plugin_runtime
from .schema import AddNoteInput, AddNoteOutput, Input, Output, Component
# Custom imports below


class AddNote(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_note',
                description=Component.DESCRIPTION,
                input=AddNoteInput(),
                output=AddNoteOutput())

    def run(self, params={}):
        notes = params.get(Input.NOTES)
        category = params.get(Input.CATEGORY)
        source = params.get(Input.SOURCE)

        payload = {
            'ParentLink_RecID': self.connection.ivanti_service_manager_api.get_incident_by_number(
                params.get(Input.INCIDENT_NUMBER)
            ).get('RecId'),
            'Subject': params.get(Input.SUMMARY),
        }

        if notes:
            payload['NotesBody'] = notes
        if category:
            payload['Category'] = category
        if source:
            payload['Source'] = source

        return {
            Output.JOURNAL_NOTE: self.connection.ivanti_service_manager_api.post_journal_note(payload)
        }
