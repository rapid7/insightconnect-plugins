import komand
from .schema import ClusterHealthInput, ClusterHealthOutput
# Custom imports below
from komand_elasticsearch.util import helpers


class ClusterHealth(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='cluster_health',
                description='Check cluster health',
                input=ClusterHealthInput(),
                output=ClusterHealthOutput())

    def run(self, params={}):
        host = self.connection.elastic_host
        username = self.connection.username
        password = self.connection.password
        results = helpers.get_health(self.logger, host, username, password)
        return {'cluster_health': komand.helper.clean(results)}

    def test(self):
        host = self.connection.elastic_host
        username = self.connection.username
        password = self.connection.password
        r = helpers.test_auth(self.logger, host, username, password)
        if not r:
            raise Exception('Test: Failed authentication')
        return {}
