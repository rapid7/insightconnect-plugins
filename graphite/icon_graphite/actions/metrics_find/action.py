import komand
from .schema import MetricsFindInput, MetricsFindOutput
# Custom imports below
from ... import helper


class MetricsFind(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='metrics_find',
                description='Find metrics under a given path',
                input=MetricsFindInput(),
                output=MetricsFindOutput())

    def run(self, params={}):
        query = {
            'query': params.get('query'),
            'format': 'treejson',
            'wildcards': int(params.get('wildcards')),
        }

        from_date = params.get('from')
        if from_date:
            query['from'] = helper.date_to_epoch(from_date)
        to_date = params.get('to')
        if to_date:
            query['to'] = helper.date_to_epoch(to_date)

        response = self.connection.request(
            'GET', ('metrics', 'find'),
            params=query
        )
        if response.ok:
            return {'metrics': list(map(
                helper.metric_to_json,
                response.json()
            ))}
        else:
            self.logger.error('Graphite API: ' + response.json().get('message', ''))
            response.raise_for_status()

    def test(self):
        return self.connection.test()
