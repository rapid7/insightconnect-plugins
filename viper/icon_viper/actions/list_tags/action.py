import komand
from .schema import ListTagsInput, ListTagsOutput, Input, Output, Component
from ...util import project


class ListTags(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_tags',
                description=Component.DESCRIPTION,
                input=ListTagsInput(),
                output=ListTagsOutput())

    def run(self, params={}):
        return {
            Output.TAGS: project.Project(self.connection.config, params.get(Input.PROJECT_NAME)).list_tags()
        }
