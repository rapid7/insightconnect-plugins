import komand
from .schema import DeleteNoteInput, DeleteNoteOutput, Input, Output, Component
from ...util import malware


class DeleteNote(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_note',
                description=Component.DESCRIPTION,
                input=DeleteNoteInput(),
                output=DeleteNoteOutput())

    def run(self, params={}):
        malware.Malware(self.connection.config, params.get(Input.PROJECT_NAME), **{"sha256": params.get(Input.MALWARE_SHA256)})\
            .get_note(params.get(Input.ID)).delete()
        return {}
