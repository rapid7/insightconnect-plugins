import komand
from .schema import MetricsExpandInput, MetricsExpandOutput
# Custom imports below


class MetricsExpand(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='metrics_expand',
                description='Expands metrics with matching paths',
                input=MetricsExpandInput(),
                output=MetricsExpandOutput())

    def run(self, params={}):
        query = {
            'query': params.get('query'),
            'leavesOnly': int(params.get('leaves_only'))
        }

        response = self.connection.request(
            'GET', ('metrics', 'expand'),
            params=query
        )
        if response.ok:
            return {'metrics': response.json().get('results', [])}
        else:
            self.logger.error('Graphite API: ' + response.json().get('message', ''))
            response.raise_for_status()

    def test(self):
        return self.connection.test()
