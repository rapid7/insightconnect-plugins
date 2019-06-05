import komand
from .schema import UploadInput, UploadOutput
# Custom imports
import json
import requests
import base64


class Upload(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='upload',
                description='Upload capture file',
                input=UploadInput(),
                output=UploadOutput())

    def run(self, params={}):
        base     = self.connection.base
        token    = self.connection.token
        filename = params.get('filename')
        tags     = params.get('tags')
        comments = params.get('comments')

        '''Setup URL'''
        url = base + token + '/upload'
        if filename or tags or comments:
          url += '?'
          if filename:
            url += 'filename=%s' % filename
          if tags:
            if 'filename=' in url:
              url += '&'
            url += 'tags=%s' % filename
          if comments:
            if 'tags=' in url:
              url += '&'
            url += 'tags=%s' % filename
        self.logger.info('URL: %s', url)

        _file = base64.b64decode(params['file'])
        files = { 'file': (_file) }
        try:
          resp = requests.post(url, files=files)
          results = json.loads(resp.text)
          return  results
        except requests.exceptions.HTTPError:
          self.logger.error('Requests: HTTPError: status code %s for %s', str(resp.status_code), url)
        Exception('CloudShark: Failed')

    def test(self):
        """TODO: Test action"""
        return {}
