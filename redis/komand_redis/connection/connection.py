import komand
from .schema import ConnectionSchema, Input
# Custom imports below
import redis


class Connection(komand.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.redis = None

    def connect(self, params):
        self.logger.info("Connect: Connecting..")
        self.redis = redis.StrictRedis(host=params[Input.HOST], port=params[Input.PORT], db=params[Input.DB])
        self.redis.get("test")
