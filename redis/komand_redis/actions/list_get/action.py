import komand
from .schema import ListGetInput, ListGetOutput
# Custom imports below


class ListGet(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='list_get',
            description='Get all elements in a list',
            input=ListGetInput(),
            output=ListGetOutput())

    def run(self, params={}):
        values = []
        found = False

        result = self.connection.redis.lrange(params['key'], 0, params['count'])
        if result:
            for r in result:
                values.append(r.decode("utf-8"))
            found = True

        return {
            'values': values,
            'found': found
        }

    def test(self):
        """TODO: Test action"""
        return {}
