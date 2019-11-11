import komand
from .schema import TrimInput, TrimOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class Trim(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='trim',
                description=Component.DESCRIPTION,
                input=TrimInput(),
                output=TrimOutput())

    def run(self, params={}):
        string = params.get(Input.STRING)
        if not string:
            raise PluginException(cause='Action failed! Missing required user input.',
                                  assistance='Please provide the input string.')

        return {Output.TRIMMED: string.strip()}
