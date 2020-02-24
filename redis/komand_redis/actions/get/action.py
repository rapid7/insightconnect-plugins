import komand
from .schema import GetInput, GetOutput, Input, Output, Component


class Get(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='get',
            description=Component.DESCRIPTION,
            input=GetInput(),
            output=GetOutput())

    def run(self, params={}):
        value = self.connection.redis.get(params[Input.KEY]) or None
        found = value is not None
        if found:
            value = value.decode("utf-8")
        else:
            value = ''

        return {
            Output.VALUE: value,
            Output.FOUND: found
        }
