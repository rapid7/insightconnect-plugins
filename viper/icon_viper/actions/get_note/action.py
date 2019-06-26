import komand
from .schema import GetNoteInput, GetNoteOutput, Input, Output, Component
from ...util import project


class GetNote(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_note',
                description=Component.DESCRIPTION,
                input=GetNoteInput(),
                output=GetNoteOutput())

    def run(self, params={}):
        return {
            Output.NOTE: project.Project(self.connection.config, params.get(Input.PROJECT_NAME)).get_note(params.get(Input.ID)).dump()
        }
