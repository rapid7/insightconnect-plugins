import komand
from .schema import QueryInput, QueryOutput
# Custom imports below
import json
import urllib.request
import urllib.parse


class Query(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='query',
                description='Search the database using query syntax provided at https://www.hybrid-analysis.com/faq',
                input=QueryInput(),
                output=QueryOutput())

    def run(self, params={}):
        server = self.connection.server
        api_key = self.connection.api_key
        secret = self.connection.secret
        url = server + "/search?query=%s&apikey=%s&secret=%s" % (urllib.parse.quote(params.get('query')), api_key, secret)

        req = urllib.request.Request(url=url, headers={'User-Agent':'VxStream Sandbox'})
        response = urllib.request.urlopen(req)
        output = json.loads(response.read().decode("utf-8"))

        if output['response_code'] == 0:
            for result in output['response']['result']:
                if 'verdict' in result:
                    if result['verdict'] is None:
                        result['verdict'] = "Unknown"
            output['results'] = output['response']['result']
            output['query'] = output['response']['query']
        else:
            self.logger.error(output['response']['error'])
            raise Exception(output['response']['error'])

        del output['response']

        # Add count
        output['count'] = len(output.get('results') or [])

        return output

    def test(self):
        server = self.connection.server
        api_key = self.connection.api_key
        secret = self.connection.secret
        query = "filetype:exe"
        url = server + "/search?query=%s&apikey=%s&secret=%s" % (query, api_key, secret)

        req = urllib.request.Request(url=url, headers={'User-Agent':'VxStream Sandbox'})
        response = urllib.request.urlopen(req)
        output = json.loads(response.read().decode("utf-8"))

        if output['response_code'] != 0:
            self.logger.error("API returned response code %d. Check that the API key and secret are correct." % output['response_code'])
            raise Exception('VxStream Sandbox - "Query" - Invalid credentials')

        return output
