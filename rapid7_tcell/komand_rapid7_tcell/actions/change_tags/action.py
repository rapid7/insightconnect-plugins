import komand
from .schema import ChangeTagsInput, ChangeTagsOutput
# Custom imports below


class ChangeTags(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='change_tags',
                description='Assign a completely new set of tags to an app, removing any previously existing tags',
                input=ChangeTagsInput(),
                output=ChangeTagsOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        tags = params.get('tags')
        success = self.connection.api.change_tags(app_id, tags)
        return {'success': success}

    def test(self):
        return {}
