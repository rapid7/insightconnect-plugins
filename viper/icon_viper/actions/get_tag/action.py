import komand
from .schema import GetTagInput, GetTagOutput, Input, Output, Component
from ...util import project


class GetTag(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_tag',
                description=Component.DESCRIPTION,
                input=GetTagInput(),
                output=GetTagOutput())

    def run(self, params={}):
        return {
            Output.TAG: project.Project(self.connection.config, params.get(Input.PROJECT_NAME)).get_tag(params.get(Input.ID)).dump()
        }
