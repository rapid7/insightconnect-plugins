import komand
from .schema import IndexDocumentInput, IndexDocumentOutput
# Custom imports below
from komand_elasticsearch.util import helpers


class IndexDocument(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='index_document',
                description='Create or replace a document by index',
                input=IndexDocumentInput(),
                output=IndexDocumentOutput())

    def run(self, params={}):
        host = self.connection.elastic_host
        username = self.connection.username
        password = self.connection.password
        index = params.get('_index')
        type_ = params.get('_type')
        id_ = params.get('_id')
        version_type = params.get('version_type')
        version = params.get('_version')
        document = params.get('document')
        routing = params.get('routing')
        parent = params.get('parent')
        timeout = params.get('timeout')

        params = {}
        if version_type:
            params['version_type'] = version_type
        if version:
            params['version'] = str(version)
        if routing:
            params['routing'] = routing
        if parent:
            params['parent'] = str(parent)
        if timeout:
            params['timeout'] = timeout

        if not id_:
            results = helpers.post_index(self.logger, host, index, type_, document, username, password, params)
        else:
            results = helpers.put_index(self.logger, host, index, type_, id_, document, username, password, params)

        if not results:
            raise Exception('Run: Document was not indexed')
        else:
            return komand.helper.clean(results)

    def test(self):
        host = self.connection.elastic_host
        username = self.connection.username
        password = self.connection.password
        r = helpers.test_auth(self.logger, host, username, password)
        if not r:
            raise Exception('Test: Failed authentication')
        return {}
