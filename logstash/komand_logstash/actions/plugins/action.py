import komand
from .schema import PluginsInput, PluginsOutput
# Custom imports below
from urllib.parse import urljoin
from komand_logstash.util import utils
import requests


class Plugins(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='plugins',
                description='Retrieves information about all Logstash plugins that are currently installed',
                input=PluginsInput(),
                output=PluginsOutput())

    def run(self, params={}):
        url = urljoin(self.connection.url, '/_node/plugins')
        r = requests.get(url)
        return {'response': utils.serialize(r.json())}

    def test(self):
        url = urljoin(self.connection.url, '_node/plugins')
        r = requests.get(url)
        if r.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (r.text, r.status_code))

        return {'status_code': r.status_code}
