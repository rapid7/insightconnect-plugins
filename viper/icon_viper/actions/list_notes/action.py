import komand
from .schema import ListNotesInput, ListNotesOutput, Input, Output, Component
from ...util import project


class ListNotes(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_notes',
                description=Component.DESCRIPTION,
                input=ListNotesInput(),
                output=ListNotesOutput())

    def run(self, params={}):
        return {
            Output.NOTES: project.Project(self.connection.config, params.get(Input.PROJECT_NAME)).list_notes()
        }
