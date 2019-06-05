import komand
from .schema import SampleConnectionsInput, SampleConnectionsOutput
# Custom imports below


class SampleConnections(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='sample_connections',
                description='Information about network activity associated with this sample, such as connections to other domains or IPs',
                input=SampleConnectionsInput(),
                output=SampleConnectionsOutput())

    def run(self, params={}):
        hash = params.get('hash')
        limit = params.get('limit', None)
        offset = params.get('offset', None)
        
        if not limit or limit == 0:
            limit = 10
        
        if not offset:
            offset = 0

        try:
            sample_connections = self.connection.investigate.sample_connections(hash, limit=limit, offset=offset)
        except Exception as e:
            self.logger.error("SampleConnections: Run: Problem with request")
            raise e
        return sample_connections

    def test(self):
        return {"connections": []}
