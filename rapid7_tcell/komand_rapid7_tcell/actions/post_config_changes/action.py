import komand
from .schema import PostConfigChangesInput, PostConfigChangesOutput
# Custom imports below


class PostConfigChanges(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='post_config_changes',
                description='Rewrite the app configuration, either in part or in full',
                input=PostConfigChangesInput(),
                output=PostConfigChangesOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        config = params.get('config')
        id_ = self.connection.api.post_config_changes(app_id, config)
        return id_

    def test(self):
        return {}
