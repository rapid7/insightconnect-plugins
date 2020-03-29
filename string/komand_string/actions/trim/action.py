import komand
from .schema import TrimInput, TrimOutput, Input, Output, Component
# Custom imports below


class Trim(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='trim',
                description=Component.DESCRIPTION,
                input=TrimInput(),
                output=TrimOutput())

    def run(self, params={}):
        string = params.get(Input.STRING)
        return {Output.TRIMMED: string.strip()}
