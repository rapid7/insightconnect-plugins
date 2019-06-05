import komand
from .schema import GetAppTagsInput, GetAppTagsOutput
# Custom imports below


class GetAppTags(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_app_tags',
                description='Fetch the set of tags for a tCell application',
                input=GetAppTagsInput(),
                output=GetAppTagsOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        tags = self.connection.api.get_app_tags(app_id)
        return tags

    def test(self):
        return {}
