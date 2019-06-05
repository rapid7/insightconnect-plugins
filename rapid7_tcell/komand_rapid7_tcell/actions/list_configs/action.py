import komand
from .schema import ListConfigsInput, ListConfigsOutput
# Custom imports below


class ListConfigs(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_configs',
                description='Fetch details for all configurations (matching the provided criteria)',
                input=ListConfigsInput(),
                output=ListConfigsOutput())

    def run(self, params={}):
        app_id = params.get('app_id')
        from_ = params.get('from')
        to = params.get('to')
        per_page = params.get('per_page', 10)
        page = params.get('page', 1)

        configs = self.connection.api.list_configs(
            app_id, from_, to, per_page, page
        )
        if configs is None:
            configs = {'total': 0, 'configs': []}

        return configs

    def test(self):
        return {}
