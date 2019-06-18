import komand
from .schema import RunInput, RunOutput, Input, Output
# Custom imports below


class Run(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='run',
                description='Run remote command',
                input=RunInput(),
                output=RunOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
