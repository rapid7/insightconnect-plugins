import komand
from .schema import HotThreadsInput, HotThreadsOutput
# Custom imports below
from urllib.parse import urljoin
from komand_logstash.util import utils
import requests


class HotThreads(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='hot_threads',
                description='Retrieves the current hot threads for Logstash',
                input=HotThreadsInput(),
                output=HotThreadsOutput())

    def run(self, params={}):
        url = urljoin(self.connection.url, '_node/hot_threads')
        human = params.get('human', False)
        threads = params.get('threads', 3)
        ignore_idle_threads = params.get('ignore_idle_threads', True)
        params = {
            'human': human,
            'threads': threads,
            'ignore_idle_threads': ignore_idle_threads
        }
        r = requests.get(url, params=params)
        if human:
            return {'response': utils.serialize(r.content, human=True)}

        return {'response': utils.serialize(r.json())}

    def test(self):
        url = urljoin(self.connection.url, '_node/hot_threads')
        r = requests.get(url)
        if r.status_code != 200:
            raise Exception('%s (HTTP status: %s)' % (r.text, r.status_code))

        return {'status_code': r.status_code}
