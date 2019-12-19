import komand
from .schema import DoProxiedDatasourceCallInput, DoProxiedDatasourceCallOutput
# Custom imports below


class DoProxiedDatasourceCall(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='do_proxied_datasource_call',
                description='Proxies all calls to the actual datasource',
                input=DoProxiedDatasourceCallInput(),
                output=DoProxiedDatasourceCallOutput())

    def run(self, params={}):
        urlparts = [
            'datasources', 'proxy', params.get('datasource_id')
        ] + params.get('path').strip('/').split('/')

        response = self.connection.request(
            'GET', urlparts, params=params.get('parameters')
        )
        if response.ok:
            return {'response': response.json()}
        else:
            self.logger.error('Grafana API: ' + response.json().get('message', ''))
            response.raise_for_status()

    def test(self):
        return self.connection.test()
