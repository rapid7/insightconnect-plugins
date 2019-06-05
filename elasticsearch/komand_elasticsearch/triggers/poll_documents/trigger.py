import komand
import time
from .schema import PollDocumentsInput, PollDocumentsOutput
# Custom imports below
from komand_elasticsearch.util import helpers


class PollDocuments(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='poll_documents',
                description='Poll for new documents given a query',
                input=PollDocumentsInput(),
                output=PollDocumentsOutput())

    def run(self, params={}):
        host = self.connection.elastic_host
        username = self.connection.username
        password = self.connection.password
        frequency = params.get('frequency', 60)
        index = params.get('_index')
        type_ = params.get('_type')
        routing = params.get('routing')
        query = params.get('query')

        old_d = {}
        params = {}
        if routing:
            params['routing'] = routing

        while True:
            try:
                results = helpers.get_search(self.logger, host, index, type_, query, username, password, params)
            except:
                self.logger.error('Poll Documents: poll failed... trying again in %i seconds' % frequency)
                time.sleep(frequency)
                continue

            if not results or 'hits' not in results:
                self.logger.error('Poll Documents: poll failed... trying again in %i seconds' % frequency)
                time.sleep(frequency)
                continue

            hits = []
            for hit in results['hits']['hits']:
                if hit["_score"] is None or "_score" not in hit:
                    hit["_score"] = 0
                    self.logger.info("One or most results lack a relevance score, assuming 0")
                if hit['_id'] not in old_d:
                    hits.append(hit)
                    old_d[hit['_id']] = [hit['_version']]
                else:
                    if hit['_version'] not in old_d[hit['_id']]:
                        hits.append(hit)
                        old_d[hit['_id']].append(hit['_version'])

            if not hits:
                time.sleep(frequency)
                continue

            self.send({'hits': hits})
            time.sleep(frequency)

    def test(self):
        host = self.connection.elastic_host
        username = self.connection.username
        password = self.connection.password
        r = helpers.test_auth(self.logger, host, username, password)
        if not r:
            raise Exception('Test: Failed authentication')
        return {}
