import komand
from .schema import UploadUrlInput, UploadUrlOutput
# Custom imports below
import json
import requests


class UploadUrl(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='upload_url',
                description='Upload capture file by URL',
                input=UploadUrlInput(),
                output=UploadUrlOutput())

    def run(self, params={}):
        base     = self.connection.base
        token    = self.connection.token
        link     = params.get('url')
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

        post = { 'url': link }
        try:
          resp = requests.post(url, params=post)
          results = json.loads(resp.text)
          return results
        except requests.exceptions.HTTPError:
          self.logger.error('Requests: HTTPError: status code %s for %s', str(resp.status_code), url)
        Exception('CloudShark: Failed')

    def test(self):
        """TODO: Test action"""
        return {}
