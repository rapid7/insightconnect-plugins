import komand
from .schema import MergeInput, MergeOutput
# Custom imports below
import json


class Merge(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='merge',
                description='Merge capture files',
                input=MergeInput(),
                output=MergeOutput())

    def run(self, params={}):
        base       = self.connection.base
        token      = self.connection.token
        cids       = params.get('cids')
        filename   = params.get('filename')
        tags       = params.get('tags')
        duplicates = params.get('duplicates')

        '''Setup URL'''
        url = base + token + '/merge?capture_ids=' + cids
        if filename or tags or duplicates:
          url += '&'
          if filename:
            url += 'filename=%s' % filename
          if tags:
            if 'filename=' in url:
              url += '&'
            url += 'additional_tags=%s' % tags
          if duplicates:
            if 'additional_tags=' in url:
              url += '&'
            url += 'duplicates=remove'
        self.logger.info('URL: %s', url)

        resp = komand.helper.open_url(url, data='')
        results = json.loads(resp.read())
        return results

    def test(self):
        """TODO: Test action"""
        return {}
