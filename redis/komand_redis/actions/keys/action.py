import komand
from .schema import KeysInput, KeysOutput, Input, Output, Component


class Keys(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='keys',
            description=Component.DESCRIPTION,
            input=KeysInput(),
            output=KeysOutput())

    def run(self, params={}):
        keys = self.connection.redis.keys(params[Input.PATTERN])
        keys = [key.decode('utf-8') for key in keys]
        count = len(keys or [])
        return {
            Output.COUNT: count,
            Output.KEYS: keys
        }
