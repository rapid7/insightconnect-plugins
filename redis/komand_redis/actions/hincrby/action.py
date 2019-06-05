import komand
from .schema import HincrbyInput, HincrbyOutput
# Custom imports below


class Hincrby(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='hincrby',
                description='Increments the number stored at field in the hash stored at key by increment',
                input=HincrbyInput(),
                output=HincrbyOutput())

    def run(self, params={}):
        key = params.get("key")
        field = params.get("field")
        value = params.get("value")
        try:
            result = self.connection.redis.hincrby(key, field, value)
        except Exception as e:
            self.logger.error("An error occurred while running HINCRBY: ", e)
            raise

        return {"result": result}

    def test(self):
        try:
            self.connection.redis.config_get()
        except Exception as e:
            self.logger.error("An error occurred while testing HMSET: ", e)
            raise
        return {"success": True}
