import komand
from .schema import ConnectionSchema
# Custom imports below
import redis


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.redis = None

    def connect(self, params):
        self.logger.info("Connect: Connecting..")
        db = params['db']
        host = params['host']
        port = params['port']
        self.redis = redis.StrictRedis(host=host, port=port, db=db)
        self.redis.get("test")
