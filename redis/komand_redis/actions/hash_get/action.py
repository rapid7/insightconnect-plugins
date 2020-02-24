import komand
from .schema import HashGetInput, HashGetOutput, Input, Output, Component
# Custom imports below


class HashGet(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='hash_get',
            description=Component.DESCRIPTION,
            input=HashGetInput(),
            output=HashGetOutput())

    def run(self, params={}):
        """Run action"""
        values = self.connection.redis.hgetall(params[Input.KEY])
        found = not not values
        if values:
            v = {}
            for key, val in values.items():
                v[key.decode('utf-8')] = val.decode('utf-8')
            values = v

        return {
            Output.VALUES: values or {},
            Output.FOUND: found
        }
