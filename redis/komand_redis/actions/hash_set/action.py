import komand
from .schema import HashSetInput, HashSetOutput
# Custom imports below


class HashSet(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='hash_set',
            description='Set Hash',
            input=HashSetInput(),
            output=HashSetOutput())

    def run(self, params={}):
        reply = 'OK'
        result = self.connection.redis.hmset(params['key'], params['values'] or {})

        if params.get('expire'):
            self.logger.info("Setting expiration: %s", params['expire'])
            self.connection.redis.expire(params['key'], params['expire'])
        if not result:
            reply = 'Failed'
        return {
            'reply': reply
        }

    def test(self):
        """TODO: Test action"""
        return {}
