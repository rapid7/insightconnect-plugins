import komand
from .schema import GetAppInput, GetAppOutput
# Custom imports below


class GetApp(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_app',
                description='Fetch the display name and app ID for the application with the given ID',
                input=GetAppInput(),
                output=GetAppOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        app = self.connection.api.get_app(app_id)
        return {'app': app}

    def test(self):
        return {}
