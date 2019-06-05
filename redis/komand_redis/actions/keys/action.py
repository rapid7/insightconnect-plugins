import komand
from .schema import KeysInput, KeysOutput
# Custom imports below


class Keys(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='keys',
            description='Return keys matching pattern',
            input=KeysInput(),
            output=KeysOutput())

    def run(self, params={}):
        keys = self.connection.redis.keys(params['pattern'])
        keys = [key.decode('utf-8') for key in keys]
        count = len(keys or [])
        return {
            'count': count,
            'keys': keys
        }

    def test(self):
        return {
            'count': 0,
            'keys': []
        }
