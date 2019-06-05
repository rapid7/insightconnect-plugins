import komand
from .schema import GetActiveConfigInput, GetActiveConfigOutput
# Custom imports below


class GetActiveConfig(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_active_config',
                description='Fetch the currently active application configuration',
                input=GetActiveConfigInput(),
                output=GetActiveConfigOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        config = self.connection.api.get_active_config(app_id)
        return {'config': config}

    def test(self):
        return {}
