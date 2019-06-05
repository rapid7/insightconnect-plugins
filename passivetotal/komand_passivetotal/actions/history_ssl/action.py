import komand
from .schema import HistorySslInput, HistorySslOutput
# Custom imports below
import requests
import json


class HistorySsl(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='history_ssl',
                description='Lookup SSL History',
                input=HistorySslInput(),
                output=HistorySslOutput())

    def run(self, params={}):
        url = 'https://api.passivetotal.org/v2/ssl-certificate/history'
        auth = (self.connection.username, self.connection.api_key)
        query = params.get('query')
        params = {'query': query}
        self.logger.info('Lookup query: %s', query)
        response = requests.get(url, auth=auth, params=params)
        content = json.loads(response.content)
        self.logger.debug('Returned: %s', content)
        return content

    def test(self):
        # TODO: Implement test function
        return {}
