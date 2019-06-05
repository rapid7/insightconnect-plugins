import komand
from .schema import ListPushInput, ListPushOutput
# Custom imports below


class ListPush(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='list_push',
            description='List Push',
            input=ListPushInput(),
            output=ListPushOutput())

    def run(self, params={}):
        reply = 'OK'
        result = self.connection.redis.rpush(params['key'], params['value'])

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
