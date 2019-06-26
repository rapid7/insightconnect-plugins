import komand
from .schema import CreateNoteInput, CreateNoteOutput, Input, Output, Component
from ...util import note


class CreateNote(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_note',
                description=Component.DESCRIPTION,
                input=CreateNoteInput(),
                output=CreateNoteOutput())

    def run(self, params={}):
        data = {}

        for param in [Input.TITLE, Input.BODY]:
            if params.get(param):
                data[param] = params.get(param)

        updated_note = note.Note(self.connection.config, params.get(Input.PROJECT_NAME), params.get(Input.MALWARE_SHA256), **data)
        updated_note.add()

        return {
            Output.NOTE: updated_note.dump()
        }
