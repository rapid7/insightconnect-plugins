import komand
from .schema import SetEncodingInput, SetEncodingOutput, Input, Output, Component
# Custom imports below
from komand.exceptions import PluginException

class SetEncoding(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='set_encoding',
                description=Component.DESCRIPTION,
                input=SetEncodingInput(),
                output=SetEncodingOutput())

    def run(self, params={}):
        string = params.get(Input.STRING)
        encoding_val = params.get(Input.ENCODING).lower()
        error_handler = params.get(Input.ERROR_HANDLING)

        try:
            output = string.encode(encoding_val, error_handler)
        except UnicodeError:
            raise PluginException(cause="Encoding failed.", assistance="Could not encode given string.")
        
        output = output.decode(encoding_val, error_handler)

        return {Output.ENCODED: output}
