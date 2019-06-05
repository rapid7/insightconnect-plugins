import komand
from .schema import UpdateDocumentInput, UpdateDocumentOutput
# Custom imports below
from komand_elasticsearch.util import helpers


class UpdateDocument(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='update_document',
                description='Update a document',
                input=UpdateDocumentInput(),
                output=UpdateDocumentOutput())

    def run(self, params={}):
        host = self.connection.elastic_host
        username = self.connection.username
        password = self.connection.password
        index = params.get('_index')
        type_ = params.get('_type')
        id_ = params.get('_id')
        retry_on_conflict = params.get('retry_on_conflict')
        wait_for_active_shards = params.get('wait_for_active_shards')
        refresh = params.get('refresh')
        source = params.get('_source')
        version = params.get('_version')
        routing = params.get('routing')
        parent = params.get('parent')
        timeout = params.get('timeout')
        script = params.get('script')

        params = {}
        if retry_on_conflict:
            params['retry_on_conflict'] = str(retry_on_conflict)
        if wait_for_active_shards:
            params['wait_for_active_shards'] = str(wait_for_active_shards)
        if refresh:
            params['refresh'] = refresh
        if source:
            params['source'] = source
        if version:
            params['version'] = str(version)
        if routing:
            params['routing'] = routing
        if parent:
            params['parent'] = parent
        if timeout:
            params['timeout'] = timeout

        results = helpers.post_update(self.logger, host, index, type_, id_, script, username, password, params)

        if not results:
            raise Exception('Run: Document was not updated')
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
