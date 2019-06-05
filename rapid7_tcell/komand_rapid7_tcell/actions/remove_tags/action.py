import komand
from .schema import RemoveTagsInput, RemoveTagsOutput
# Custom imports below


class RemoveTags(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='remove_tags',
                description='Remove all tags from the application',
                input=RemoveTagsInput(),
                output=RemoveTagsOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        tags = params.get('tags')
        success = self.connection.api.remove_tags(app_id, tags)
        return {'success': success}

    def test(self):
        return {}
