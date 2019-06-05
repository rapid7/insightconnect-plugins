import komand
from .schema import SearchDocumentsInput, SearchDocumentsOutput
# Custom imports below
from komand_elasticsearch.util import helpers


class SearchDocuments(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_documents',
                description='Execute a search query and get back search hits that match the query',
                input=SearchDocumentsInput(),
                output=SearchDocumentsOutput())

    def run(self, params={}):
        host = self.connection.elastic_host
        username = self.connection.username
        password = self.connection.password
        index = params.get('_index')
        type_ = params.get('_type')
        routing = params.get('routing')
        query = params.get('query')

        params = {}
        if routing:
            params['routing'] = routing

        results = helpers.get_search(self.logger, host, index, type_, query, username, password, params)
        if not results:
            raise Exception('Run: Document search not run')

        if not results['hits']['max_score']:
            results['hits']['max_score'] = 0

        for hit in results['hits']['hits']:
            if hit["_score"] is None or "_score" not in hit:
                hit["_score"] = 0
                self.logger.info("One or most results lack a relevance score, assuming 0")

        return komand.helper.clean(results)

    def test(self):
        host = self.connection.elastic_host
        username = self.connection.username
        password = self.connection.password
        r = helpers.test_auth(self.logger, host, username, password)
        if not r:
            raise Exception('Test: Failed authentication')
        return {}
