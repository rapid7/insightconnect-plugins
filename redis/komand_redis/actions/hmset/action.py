import komand
from .schema import HmsetInput, HmsetOutput
# Custom imports below


class Hmset(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='hmset',
                description='Sets the specified fields to their respective values in the hash stored at key',
                input=HmsetInput(),
                output=HmsetOutput())

    def run(self, params={}):
        key = params['key']
        values = params['values']
        try:
            result = self.connection.redis.hmset(key, values)
        except Exception as e:
            self.logger.error("An error occurred while running HMSET: ", e)
            raise

        if params.get('expire'):
            self.logger.info("Setting expiration: %s", params['expire'])
            self.connection.redis.expire(params['key'], params['expire'])
        return {
            'reply': result
        }

    def test(self):
        try:
            self.connection.redis.config_get()
        except Exception as e:
            self.logger.error("An error occurred while testing HMSET: ", e)
            raise
        return {"success": True}
