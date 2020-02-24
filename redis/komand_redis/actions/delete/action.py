import komand
from .schema import DeleteInput, DeleteOutput, Input, Output, Component


class Delete(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='delete',
            description=Component.DESCRIPTION,
            input=DeleteInput(),
            output=DeleteOutput())

    def run(self, params={}):
        """Run action"""
        return {
            Output.COUNT: self.connection.redis.delete(params[Input.KEY])
        }
