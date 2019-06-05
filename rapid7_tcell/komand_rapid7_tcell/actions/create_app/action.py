import komand
from .schema import CreateAppInput, CreateAppOutput
# Custom imports below


class CreateApp(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='create_app',
                description='Create an application',
                input=CreateAppInput(),
                output=CreateAppOutput())

    def run(self, params={}):
        app_display_name = params.get('app_display_name')
        app_id = self.connection.api.create_app(app_display_name)
        return app_id

    def test(self):
        return {}
