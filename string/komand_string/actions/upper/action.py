import komand
from .schema import UpperInput, UpperOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException


class Upper(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name='upper',
            description=Component.DESCRIPTION,
            input=UpperInput(),
            output=UpperOutput())

    def run(self, params={}):
        string = params.get(Input.STRING)
        if not string:
            raise PluginException(cause='Action failed! Missing required user input.',
                                  assistance='Please provide the input string.')
        return {Output.UPPER: string.upper()}
