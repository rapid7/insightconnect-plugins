import komand
from .schema import LookupSslInput, LookupSslOutput
# Custom imports below
from komand_passivetotal.util import util
import json
import requests


class LookupSsl(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lookup_ssl',
                description='Lookup SSL Certificate',
                input=LookupSslInput(),
                output=LookupSslOutput())

    def run(self, params={}):
        url = 'https://api.passivetotal.org/v2/ssl-certificate'
        auth = (self.connection.username, self.connection.api_key)
        sha1 = params.get('sha1')
        params = {'query': sha1}
        self.logger.info('Lookup hash: %s', sha1)
        response = requests.get(url, auth=auth, params=params)
        content = json.loads(response.content)
        self.logger.debug('Returned: %s', content)
        if not content:
            return {'found': False}
        content['found'] = True
        output = util.clean_dict_recursive(content)
        return output

    def test(self):
        # TODO: Implement test function
        return {}
