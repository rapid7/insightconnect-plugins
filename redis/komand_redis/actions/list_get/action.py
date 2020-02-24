import komand
from .schema import ListGetInput, ListGetOutput, Input, Output, Component
# Custom imports below


class ListGet(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='list_get',
            description=Component.DESCRIPTION,
            input=ListGetInput(),
            output=ListGetOutput())

    def run(self, params={}):
        values = []
        found = False

        result = self.connection.redis.lrange(params[Input.KEY], 0, params[Input.COUNT])
        if result:
            for r in result:
                values.append(r.decode("utf-8"))
            found = True

        return {
            Output.VALUES: values,
            Output.FOUND: found
        }
