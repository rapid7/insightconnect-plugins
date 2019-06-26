import komand
from .schema import DeleteTagInput, DeleteTagOutput, Input, Output, Component
from ...util import project


class DeleteTag(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='delete_tag',
                description=Component.DESCRIPTION,
                input=DeleteTagInput(),
                output=DeleteTagOutput())

    def run(self, params={}):
        project.Project(self.connection.config, params.get(Input.PROJECT_NAME)).get_tag(params.get(Input.ID)).delete()
        return {}
