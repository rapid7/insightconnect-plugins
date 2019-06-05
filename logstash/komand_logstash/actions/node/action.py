import komand
from .schema import NodeInput, NodeOutput
# Custom imports below
from urllib.parse import urljoin
from komand_logstash.util import utils
import requests


class Node(komand.Action):

    TYPES = ['pipeline', 'os', 'jvm']

    def __init__(self):
        super(self.__class__, self).__init__(
                name='node',
                description='Retrieves information about the node',
                input=NodeInput(),
                output=NodeOutput())

    def run(self, params={}):
        url = urljoin(self.connection.url, '/_node')
        types = params.get('types')
        if types:
            error_types = utils.check_types(self.TYPES, types)
            if error_types:
                self.logger.error('Logstash: Node Info: invalid types %s', ','.join(error_types))
                raise Exception("Logstash: Node: Invalid types", types)

        r = requests.get(url, params=params)
        return {'response': utils.serialize(r.json())}

    def test(self):
        url = urljoin(self.connection.url, '_node')
        r = requests.get(url)
        if r.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (r.text, r.status_code))

        return {'status_code': r.status_code}
