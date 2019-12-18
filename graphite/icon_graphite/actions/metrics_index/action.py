import komand
from .schema import MetricsIndexInput, MetricsIndexOutput
# Custom imports below


class MetricsIndex(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='metrics_index',
                description='Walks the metrics tree and returns every metric found',
                input=MetricsIndexInput(),
                output=MetricsIndexOutput())

    def run(self, params={}):
        response = self.connection.request(
            'GET', ('metrics', 'index.json')
        )
        if response.ok:
            return {'metrics': response.json()}
        else:
            self.logger.error('Graphite API: ' + response.json().get('message', ''))
            response.raise_for_status()

    def test(self):
        return self.connection.test()
