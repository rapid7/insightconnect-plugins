import komand
from .schema import CheckInput, CheckOutput
# Custom imports below
import json
import base64
import requests

class Check(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='check',
                description='Check a file for an SHA-1 collision',
                input=CheckInput(),
                output=CheckOutput())

    def run(self, params={}):
        _file = base64.b64decode(params.get('file'))
        url = 'http://shattered.io/sample/submit'
        files = { 'file': (_file) }
        try:
          r = requests.post(url, files=files)
          data = r.json()
        except requests.exceptions.HTTPError:
          self.logger.error('Requests: HTTPError: status code %s for %s', str(resp.status_code), url)
          raise
        return data['file']

    def test(self):
        try:
          url = 'http://shattered.io/sample/submit'
          r = requests.post(url).json()
        except requests.exceptions.HTTPError:
          self.logger.error('Requests: HTTPError: status code %s for %s', str(resp.status_code), url)
          raise
        return r
