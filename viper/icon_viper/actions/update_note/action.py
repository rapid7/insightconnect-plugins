import komand
from .schema import UpdateNoteInput, UpdateNoteOutput, Input, Output, Component
from ...util import note


class UpdateNote(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_note',
                description=Component.DESCRIPTION,
                input=UpdateNoteInput(),
                output=UpdateNoteOutput())

    def run(self, params={}):
        data = {}

        for param in [Input.ID, Input.TITLE, Input.BODY]:
            if params.get(param):
                data[param] = params.get(param)

        updated_note = note.Note(self.connection.config, params.get(Input.PROJECT_NAME), params.get(Input.MALWARE_SHA256), **data)
        updated_note.save()

        return {
            Output.NOTE: updated_note.dump()
        }
