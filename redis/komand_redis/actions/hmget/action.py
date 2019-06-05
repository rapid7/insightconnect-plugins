import komand
from .schema import HmgetInput, HmgetOutput
# Custom imports below


class Hmget(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='hmget',
                description='Returns the values associated with the specified fields in the hash stored at key',
                input=HmgetInput(),
                output=HmgetOutput())

    def run(self, params={}):
        key = params["key"]
        fields = params["fields"]
        get_all = params["get_all"]

        try:
            if get_all:
                result = self.connection.redis.hgetall(key)
            else:
                result = self.connection.redis.hmget(key, fields)
        except Exception as e:
            self.logger.error("An error occurred while running HMSET: ", e)
            raise

        if result:
            v = {}
            for key, val in result.items():
                v[key.decode('utf-8')] = val.decode('utf-8')
            result = v

        return {"values": result}

    def test(self):
        try:
            self.connection.redis.config_get()
        except Exception as e:
            self.logger.error("An error occurred while testing HMSET: ", e)
            raise
        return {"success": True}
