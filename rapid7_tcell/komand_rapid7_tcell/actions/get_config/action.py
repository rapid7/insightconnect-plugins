import komand
from .schema import GetConfigInput, GetConfigOutput
# Custom imports below


class GetConfig(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_config',
                description='Fetch the configuration with the given ID',
                input=GetConfigInput(),
                output=GetConfigOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        config_id = params.get('config_id')
        config = self.connection.api.get_config(app_id, config_id)
        return {'config': config}

    def test(self):
        return {}
