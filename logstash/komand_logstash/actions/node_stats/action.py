import komand
from .schema import NodeStatsInput, NodeStatsOutput
# Custom imports below
from urllib.parse import urljoin
from komand_logstash.util import utils
import requests


class NodeStats(komand.Action):

    TYPES = ['pipeline', 'os', 'jvm', 'reloads', 'process']

    def __init__(self):
        super(self.__class__, self).__init__(
                name='node_stats',
                description='Retrieves runtime stats about Logstash',
                input=NodeStatsInput(),
                output=NodeStatsOutput())

    def run(self, params={}):
        url = urljoin(self.connection.url, '/_node/stats')
        types = params.get('types')
        if types:
            error_types = utils.check_types(self.TYPES, types)
            if error_types:
                self.logger.error('Logstash: Node Stats: invalid types %s', ','.join(types))
                raise Exception("Logstash: Node Stats: Invalid types", types)

        r = requests.get(url, params=params)
        return {'response': utils.serialize(r.json())}

    def test(self):
        url = urljoin(self.connection.url, '_node/stats')
        r = requests.get(url)
        if r.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (r.text, r.status_code))

        return {'status_code': r.status_code}
