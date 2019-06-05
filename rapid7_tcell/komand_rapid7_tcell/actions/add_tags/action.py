import komand
from .schema import AddTagsInput, AddTagsOutput
# Custom imports below


class AddTags(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='add_tags',
                description='All the tags posted in the body will be added to the set of tags the app already has',
                input=AddTagsInput(),
                output=AddTagsOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        tags = params.get('tags')
        success = self.connection.api.add_tags(app_id, tags)
        return {'success': success}

    def test(self):
        return {}
