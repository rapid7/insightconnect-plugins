import komand
from .schema import SetInput, SetOutput
# Custom imports below


class Set(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='set',
            description='Set',
            input=SetInput(),
            output=SetOutput())

    def run(self, params={}):
        reply = 'OK'
        expire = params.get('expire')
        if not expire:
            result = self.connection.redis.set(params['key'], params['value'])
        else:
            result = self.connection.redis.setex(params['key'], expire, params['value'])

        if not result:
            reply = 'Failed'
        return {
            'reply': reply
        }

    def test(self):
        """Test action"""
        return {}
