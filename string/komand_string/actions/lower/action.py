import komand
from .schema import LowerInput, LowerOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class Lower(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='lower',
            description=Component.DESCRIPTION,
            input=LowerInput(),
            output=LowerOutput())

    def run(self, params={}):
        string = params.get(Input.STRING)
        if not string:
            raise PluginException(cause='Action failed! Missing required user input.',
                                  assistance='Please provide the input string.')

        return {Output.LOWER: string.lower()}
