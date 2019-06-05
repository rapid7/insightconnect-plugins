import komand
from .schema import ConnectionSchema
# Custom imports below
from pyhive import presto


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        host = params.get('host')
        port = params.get('port', 8080)

        self.host = host
        self.port = port

        kwargs = {
            'host': host,
            'port': port,
            'username': params.get('username'),
            'catalog': params.get('catalog', 'hive'),
            'schema': params.get('schema', 'default'),
            'poll_interval': params.get('poll_interval', 1),
            'source': params.get('source', 'pyhive'),
        }

        self.cursor = presto.connect(**kwargs).cursor()
        self.logger.info("Connecting to %s:%s " % (host, port))

        self.timeout = 5
