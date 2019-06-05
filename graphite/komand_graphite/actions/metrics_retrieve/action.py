import komand
from .schema import MetricsRetrieveInput, MetricsRetrieveOutput
# Custom imports below


class MetricsRetrieve(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='metrics_retrieve',
                description='Retrieve raw metrics data',
                input=MetricsRetrieveInput(),
                output=MetricsRetrieveOutput())

    def run(self, params={}):
        query = komand.helper.clean_dict(params)
        for (tvar, tsub) in query.pop('templates', {}).items():
            query['template[%s]' % tvar] = tsub
        query['format'] = 'json'

        response = self.connection.request(
            'GET', ('render',),
            params=query
        )
        if response.ok:
            return {'metrics': response.json()}
        else:
            self.logger.error('Graphite API: ' + response.json().get('message', ''))
            response.raise_for_status()

    def test(self):
        return self.connection.test()
