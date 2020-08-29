import insightconnect_plugin_runtime
from .schema import LowerInput, LowerOutput
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException


class Lower(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='lower',
                description='Converts uppercase letters to lowercase',
                input=LowerInput(),
                output=LowerOutput())

    def run(self, params={}):
        string = params.get('string')
        if not string:
            raise PluginException(cause='Action failed! Missing required user input.',
                                  assistance='Please provide the input string.')

        return {'lower': string.lower()}
