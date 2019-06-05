import komand
from .schema import GetInput, GetOutput
# Custom imports below


class Get(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get',
            description='Get',
            input=GetInput(),
            output=GetOutput())

    def run(self, params={}):
        value = self.connection.redis.get(params['key']) or None
        found = value is not None
        if found:
            value = value.decode("utf-8")
        else:
            value = ''

        return {
            'value': value,
            'found': found
        }

    def test(self):
        """TODO: Test action"""
        return {}
