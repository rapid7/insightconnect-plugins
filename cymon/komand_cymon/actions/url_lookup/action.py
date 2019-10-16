import komand
from .schema import UrlLookupInput, UrlLookupOutput
# Custom imports below
import json
import urllib


class UrlLookup(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='url_lookup',
                description='Lookup URL',
                input=UrlLookupInput(),
                output=UrlLookupOutput())

    def run(self, params={}):
        base = self.connection.server
        token = self.connection.token
        if token:
            token = 'Token ' + token
            self.logger.info('API token was provided by user')
        url = base + '/api/nexus/v1/url/%s' % urllib.quote_plus(params.get('url'))
        eurl = url.replace('%', '%25')  # Cymon requires encoding the percent sign too
        try:
            resp = komand.helper.open_url(eurl, Authorization=token)
            dic = json.loads(resp.read())
        except:
            return {'found': False}

        # {"detail":"Not found."}
        if 'detail' in dic:
            return {'found': False}

        dic['found'] = True
        return dic

    def test(self):
        # TODO: Implement test function
        return {}
