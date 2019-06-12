import komand
from .schema import DomainExtInput, DomainExtOutput
# Custom imports below
import json
import requests


class DomainExt(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='domain_ext',
                description='Fetches information related to a domain by URIs, certificates, or related samples',
                input=DomainExtInput(),
                output=DomainExtOutput())

    def _prune_domain(self, url):
        if url.startswith('http://'):
            url = url.replace('http://', '').split('/')[0]
            return url
        if url.startswith('https://'):
            url = url.replace('https://', '').split('/')[0]
            return url
        url = url.split('/')[0]
        return url

    def run(self, params={}):
        flag = params.get('query_type')
        flag = self.FLAGS[flag]
        domain = self._prune_domain(params.get('domain'))

        try:
            response = requests.get(self.API_URL, params = {"q": domain, "rt": flag})
            return { 'response': response.json() }

        except requests.exceptions.HTTPError as e:
            self.logger.error('Requests: HTTPError: status code %s for %s',
                          str(e.status_code), params.get('domain'))


    def test(self):
        params = {
            "q": "vwrm.com",
            "rt": self.FLAGS["Subdomains"]
        }
        response = requests.get(self.API_URL, params=params)
        if response.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (response.text, response.status_code))

        return {'status_code': response.status_code}

