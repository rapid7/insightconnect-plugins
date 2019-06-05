import komand 
from .schema import LookupInput, LookupOutput
# Custom imports below
import json
import urllib.request
import urllib.parse


class Lookup(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup',
                description='Get summary information for a given hash',
                input=LookupInput(),
                output=LookupOutput())

    def run(self, params={}):
        server = self.connection.server
        api_key = self.connection.api_key
        secret = self.connection.secret
        url = server + "/scan/%s?apikey=%s&secret=%s" % (urllib.parse.quote(params.get('hash')), api_key, secret)
        req = urllib.request.Request(url=url, headers={'User-Agent':'VxStream Sandbox'})
        response = urllib.request.urlopen(req)
        output = json.loads(response.read().decode("utf-8"))


        if output['response_code'] == 0: 
            for report in output["response"]:
                if 'verdict' in report:
                    if report['verdict'] is None:
                        report['verdict'] = "Unknown"
        else:
            if output.get('response').get('error'):
                self.logger.error(output['response']['error'])
                raise Exception(output['response']['error'])
            self.logger.error(output)
            raise Exception(output)

        output['reports'] = output.pop('response') or []
        output['count'] = len(output.get('reports') or [])

        return output

    def test(self):
        server = self.connection.server
        api_key = self.connection.api_key
        secret = self.connection.secret
        digest = "d6dcfa69ef0e437fbcc60a1ea4f03019e4814fa90b789e0e80d5179022e2b118"
        url = server + "/scan/%s?apikey=%s&secret=%s" % (digest, api_key, secret)
        req = urllib.request.Request(url=url, headers={'User-Agent':'VxStream Sandbox'})
        response = urllib.request.urlopen(req)
        output = json.loads(response.read().decode("utf-8"))

        if output['response_code'] != 0:
            self.logger.error("API returned response code %d. Check that the API key and secret are correct." % output['response_code'])
            raise Exception('VxStream Sandbox - "Lookup" - Invalid credentials')

        return output
